#!/usr/bin/env python3
"""Stitch the per-section drafts of each mock paper into study-guide/mock-papers/.

Each paper is written by three agents into three fragments:

    paper-NN-A1.md   the "## Section A" heading + Q1-Q47
    paper-NN-A2.md   Q48-Q90, with no heading of its own
    paper-NN-BC.md   "## Section B" (Q91-Q120) and "## Section C" (Q121-Q135)

They are concatenated in that order under a title and a meta line. The meta line
matters: docs/app.js lifts it verbatim into the paper header via /\\*\\*(Total:[^*]*)\\*\\*/.

The section headings matter even more. app.js decides a section's per-question mark
value with /2\\s*marks?/ against the heading text, so Section C's heading must contain
the literal "2 marks" and Sections A and B must not. This script refuses to write a
paper that gets that wrong, because the failure is silent: the paper would simply
score out of 120 instead of 150.
"""
import re
import sys
import pathlib

SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("/tmp/papers")
DST = pathlib.Path("study-guide/mock-papers")
DST.mkdir(parents=True, exist_ok=True)

TITLE = "# Mock Paper {n} — NISM Series X-A (Investment Adviser Level 1)"
META = ("**Total: 150 marks · 135 questions · Time: 3 hours · "
        "Pass: 90/150 (60%) · Negative marking: 25% of the marks for a wrong answer.**")

QID = re.compile(r"^\*\*Q(\d+)\.\*\*", re.M)
TWO_MARKS = re.compile(r"2\s*marks?")
HEADING = re.compile(r"^##\s+(.*)$", re.M)

written, problems = [], []

for n in range(1, 11):
    nn = f"{n:02d}"
    parts = [SRC / f"paper-{nn}-A1.md", SRC / f"paper-{nn}-A2.md", SRC / f"paper-{nn}-BC.md"]
    missing = [p.name for p in parts if not p.exists()]
    if missing:
        problems.append(f"paper-{nn}: missing {', '.join(missing)}")
        continue

    a1, a2, bc = (p.read_text(encoding="utf-8").strip() for p in parts)

    # A2 must not carry its own "## Section A" heading — it is a continuation.
    a2 = re.sub(r"\A##\s+Section A[^\n]*\n+", "", a2)

    body = f"{a1}\n\n{a2}\n\n{bc}\n"
    doc = f"{TITLE.format(n=n)}\n\n{META}\n\n{body}"

    # --- checks that would otherwise fail silently in the app ---
    errs = []

    ids = [int(m) for m in QID.findall(doc)]
    if len(ids) != 135:
        errs.append(f"{len(ids)} questions, expected 135")
    if sorted(ids) != list(range(1, 136)):
        missing_ids = sorted(set(range(1, 136)) - set(ids))
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        if missing_ids:
            errs.append(f"missing Q{missing_ids[:8]}")
        if dupes:
            errs.append(f"duplicate Q{dupes[:8]}")

    heads = HEADING.findall(doc)
    if len(heads) != 3:
        errs.append(f"{len(heads)} '##' sections, expected 3")
    else:
        a_head, b_head, c_head = heads
        if TWO_MARKS.search(a_head):
            errs.append("Section A heading matches '2 marks' — A would score 2x")
        if TWO_MARKS.search(b_head):
            errs.append("Section B heading matches '2 marks' — B would score 2x")
        if not TWO_MARKS.search(c_head):
            errs.append("Section C heading lacks '2 marks' — C would score 1x, paper out of 120")

    cases = len(re.findall(r"^###\s+", doc, re.M))
    if cases != 9:
        errs.append(f"{cases} caselets, expected 9")

    if doc.count("<details>") != doc.count("</details>"):
        errs.append(f"details mismatch {doc.count('<details>')}/{doc.count('</details>')}")

    if errs:
        problems.append(f"paper-{nn}: " + "; ".join(errs))
        continue

    out = DST / f"paper-{nn}.md"
    out.write_text(doc, encoding="utf-8")
    written.append(f"{out} ({len(doc):,} bytes, {len(ids)} questions)")

for w in written:
    print("✓", w)
for p in problems:
    print("✗", p)
print(f"\n{len(written)} papers assembled, {len(problems)} rejected")
sys.exit(1 if problems else 0)
