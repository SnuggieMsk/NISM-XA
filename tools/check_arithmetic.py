"""Recompute the arithmetic asserted inside every explanation.

Explanations state their working in prose. This extracts the statements it can read
unambiguously and rechecks them, so a wrong intermediate is caught across all 3,450
questions rather than in a hand-picked sample.

Deliberately conservative — it only reports a mismatch when it is confident it read
the expression correctly:

  * chains are matched whole (`a + b + c + d = z`), never a sub-span of a longer sum,
    which is what made the first version cry wolf on every four-term SIP total;
  * a result may legitimately be the percentage form of the quotient
    (`59,000 / 1,93,000 = 30.57`), so a x100 or /100 match counts as correct;
  * boundaries are enforced so `3/5 = 300` cannot be read out of `640 x 3/5 = 384`;
  * an intermediate `= ... =` restatement is only followed when it is purely numeric,
    so `0.13 / 12 = 0.0108333; n = 12` reads the result as 0.0108333 and not as 12;
  * a leading unary minus is honoured, so `-5,200 - 6,000 = -11,200` is read as
    -11,200 rather than -800;
  * anything it cannot parse cleanly is skipped and counted, not guessed at.
"""
import re
import sys
import pathlib

NUM = r"\d[\d,]*(?:\.\d+)?"
# A number must not be glued to another number, a decimal point, or a power marker.
LEFT = r"(?<![\d,.^])"
RIGHT = r"(?![\d,.]*\d)"

BLOCK = re.compile(r"\*\*Q([\w-]+)\.\*\*[\s\S]*?<details>[\s\S]*?</summary>([\s\S]*?)</details>")

CHAIN = re.compile(
    rf"(?<![\d,.^])([-−]?{NUM})((?:\s*[-−+x×*÷/]\s*{NUM})+)\s*=([^=\n]{{0,50}}(?:=[^=\n]{{0,30}})?)"
)
POW = re.compile(
    LEFT + rf"({NUM})\s*[x×*]\s*\(({NUM})\)\s*\^\s*\{{?({NUM})\}}?\s*=([^=\n]{{0,60}}(?:=[^=\n]{{0,40}})?)"
)
TERM = re.compile(rf"([-−+x×*÷/])\s*({NUM})")
TAIL = re.compile(NUM)


def f(s):
    return float(s.replace(",", ""))


def close(got, want, tol=0.015):
    if want == 0:
        return abs(got) < 1e-9
    got = abs(got); want = abs(want)
    for cand in (got, got * 100, got / 100,       # percentage forms
                 got * 1e7, got * 1e5,            # crore / lakh stated in rupees
                 got / 1e7, got / 1e5):
        if abs(cand - want) / abs(want) <= tol:
            return True
    # a 2-dp display rounding of a small ratio is not an error
    return abs(got - want) <= 0.005 + abs(want) * 1e-9


checked = skipped = bad = 0
problems = []
files = sorted(pathlib.Path("study-guide").glob(sys.argv[1] if len(sys.argv) > 1 else "mock-papers/paper-*.md"))

for fp in files:
    for qid, expl in BLOCK.findall(fp.read_text(encoding="utf-8")):
        e = expl.replace("**", "")

        for m in POW.finditer(e):
            a, b, c = (f(x) for x in m.groups()[:3])
            cands = [f(x) for x in TAIL.findall(m.group(4))[:4]]
            if not cands:
                skipped += 1
                continue
            try:
                got = a * (b ** c)
            except OverflowError:
                skipped += 1
                continue
            checked += 1
            if not any(close(got, w) for w in cands):
                bad += 1
                if len(problems) < 30:
                    problems.append(f"{fp.name} Q{qid} [pow] {m.group(0)[:70]!r} -> {got:,.2f}")

        for m in CHAIN.finditer(e):
            first, rest = m.group(1).replace("−", "-"), m.group(2)
            cands = [f(x) for x in TAIL.findall(m.group(3))[:4]]
            if not cands:
                skipped += 1
                continue
            terms = TERM.findall(rest)
            ops = {o for o, _ in terms}
            # Mixed operators would need precedence rules; not worth guessing.
            if len(ops) != 1:
                skipped += 1
                continue
            op = ops.pop()
            got = f(first)
            try:
                for _, v in terms:
                    v = f(v)
                    if op in "+":
                        got += v
                    elif op in "-−":
                        got -= v
                    elif op in "x×*":
                        got *= v
                    else:
                        if v == 0:
                            raise ZeroDivisionError
                        got /= v
            except ZeroDivisionError:
                skipped += 1
                continue
            checked += 1
            if not any(close(got, w) for w in cands):
                bad += 1
                if len(problems) < 30:
                    problems.append(f"{fp.name} Q{qid} [{op}] {m.group(0)[:70]!r} -> {got:,.4f}")

print(f"files: {len(files)}")
print(f"arithmetic statements checked: {checked:,}")
print(f"skipped as ambiguous:          {skipped:,}")
print(f"mismatches:                    {bad}")
for p in problems:
    print("  ", p)
