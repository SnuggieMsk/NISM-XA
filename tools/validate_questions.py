#!/usr/bin/env python3
"""Validate every question bank against the exact parser the web app uses.

The study site (docs/app.js) extracts questions with a single regular
expression. If a question's markdown deviates even slightly — an option line
wrapped onto two lines, a missing "**Correct: X)**" marker, a stray tag between
the options and the <details> block — that question silently disappears from
the quiz instead of failing loudly.

This script re-implements that same regex and reports:
  * questions declared (**Qn.**) but not parseable
  * malformed option lines (A/B/C/D must be on ONE line)
  * missing or duplicated "**Correct: X)**" answer markers
  * duplicate question ids and unbalanced <details> tags
  * explanations containing self-correcting phrasing, where the machine-readable
    marker may disagree with the prose

Run from the repository root:

    python3 tools/validate_questions.py

Exit status is non-zero if any issue is found, so it can gate a commit.
"""
import re, sys, pathlib
BLOCK = re.compile(r"\*\*Q([\w-]+)\.\*\*\s*([\s\S]*?)\r?\n(A\)[^\n]*B\)[^\n]*C\)[^\n]*D\)[^\n]*)\r?\n<details>[\s\S]*?</summary>([\s\S]*?)</details>")
OPTS = re.compile(r"A\)\s*([\s\S]*?)\s*B\)\s*([\s\S]*?)\s*C\)\s*([\s\S]*?)\s*D\)\s*([\s\S]*)")
CORR = re.compile(r"\*\*Correct:\s*([A-D])\)", re.I)
# The marker usually restates the option text ("**Correct: C) Rs 30.00**"). When that
# restatement names a DIFFERENT option's text, the student sees a contradiction and the
# app grades on the letter — so the letter is probably the typo. Worth flagging.
CORR_FULL = re.compile(r"\*\*Correct:\s*([A-D])\)\s*([^*\n]*?)\s*\*\*", re.I)


def norm(s):
    """Compare option text loosely: markdown, spacing and rupee spelling vary."""
    s = re.sub(r"[*_`]", "", s or "")
    s = s.replace("₹", "Rs ").replace("–", "-").replace("—", "-")
    s = re.sub(r"[\s,]+", " ", s)
    return s.strip().rstrip(".").lower()
# phrases that signal a mid-explanation self-correction (marker may disagree with prose)
SMELL = re.compile(r"\bthe correct answer is\b|\bhold on\b|\bchecking the options\b|\bclosest option is\b|\bnearest option is\b|\bthe nearest is\b|\bamong the options the\b", re.I)
base = pathlib.Path("study-guide")
bad = 0
# Explicit paths win, so a half-written paper can be checked before it is assembled.
if len(sys.argv) > 1:
    files = [pathlib.Path(a) for a in sys.argv[1:]]
else:
    files = sorted(base.glob("chapter-*/questions.md")) + sorted(base.glob("mock-papers/paper-*.md"))
for fp in files:
    src = fp.read_text(encoding="utf-8")
    declared = re.findall(r"^\*\*Q([\w-]+)\.\*\*", src, re.M)
    parsed = BLOCK.findall(src)
    ids, errs = [m[0] for m in parsed], []
    seen = set()
    for qid, qtext, optline, expl in parsed:
        if qid in seen: errs.append(f"Q{qid}: duplicate id")
        seen.add(qid)
        om = OPTS.match(optline)
        if not om: errs.append(f"Q{qid}: malformed option line")
        c = CORR.search(expl)
        if not c: errs.append(f"Q{qid}: missing **Correct: X)** marker")
        if om and c:
            opts = [norm(x) for x in om.groups()]
            if len(set(opts)) < 4:
                errs.append(f"Q{qid}: duplicate option values -> two options are the same answer")
            cf = CORR_FULL.search(expl)
            # Only meaningful when the marker actually restates text to compare against.
            if cf and cf.group(2):
                said, letter = norm(cf.group(2)), cf.group(1).upper()
                shown = opts["ABCD".index(letter)]
                if said and said != shown:
                    other = [L for L, o in zip("ABCD", opts) if o == said]
                    hint = f" (matches {other[0]}))" if other else ""
                    errs.append(
                        f"Q{qid}: marker says {letter}) '{cf.group(2)[:40]}' but option "
                        f"{letter} is '{om.group('ABCD'.index(letter) + 1)[:40]}'{hint}")
        # multiple markers => ambiguous grading
        if len(CORR.findall(expl)) > 1: errs.append(f"Q{qid}: MULTIPLE Correct markers")
        if SMELL.search(expl): errs.append(f"Q{qid}: self-correction phrasing -> verify marker matches prose")
    for d in declared:
        if d not in ids: errs.append(f"Q{d}: declared but NOT parsed")
    if src.count("<details>") != src.count("</details>"):
        errs.append(f"details mismatch {src.count('<details>')}/{src.count('</details>')}")
    status = "✓" if not errs else "✗"
    print(f"{status} {fp}: {len(parsed)} parsed / {len(declared)} declared")
    for e in errs[:12]: print(f"     - {e}")
    bad += len(errs)
print(f"\nTOTAL ISSUES: {bad}")
sys.exit(1 if bad else 0)
