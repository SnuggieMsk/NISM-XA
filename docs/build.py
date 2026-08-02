#!/usr/bin/env python3
"""Regenerate docs/content.js from the markdown in ../study-guide.

Run this whenever you edit the notes/flashcards/questions so the live
site picks up the changes:

    python3 docs/build.py
"""
import json
import pathlib

M1 = "Module 1: Personal Financial Planning"
M2 = "Module 2: Indian Financial Markets"
M3 = "Module 3: Investment Products"
M4 = "Module 4: Investment Through Managed Portfolio"
M5 = "Module 5: Portfolio Construction, Performance Monitoring & Evaluation"
M6 = "Module 6: Operations, Regulatory Environment, Compliance & Ethics"

META = [
    ("01", "Introduction to Personal Financial Planning", M1),
    ("02", "Time Value of Money", M1),
    ("03", "Cash Flow Management and Budgeting", M1),
    ("04", "Debt Management and Loans", M1),
    ("05", "Introduction to Indian Financial Markets", M2),
    ("06", "Securities Market Segments", M2),
    ("07", "Introduction to Investments", M3),
    ("08", "Investing in Stocks", M3),
    ("09", "Investing in Fixed Income Securities", M3),
    ("10", "Understanding Derivatives", M3),
    ("11", "Mutual Funds", M4),
    ("12", "Portfolio Manager", M4),
    ("13", "Overview of Alternative Investment Funds (AIFs)", M4),
    ("14", "Introduction to Modern Portfolio Theory", M5),
    ("15", "Portfolio Construction Process", M5),
    ("16", "Portfolio Performance Measurement and Evaluation", M5),
    ("17", "Operational Aspects of Investment Management", M6),
    ("18", "Key Regulations", M6),
    ("19", "Ethical Issues", M6),
    ("20", "Grievance Redress Mechanism", M6),
]

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent / "study-guide"


def read(rel):
    fp = BASE / rel
    return fp.read_text(encoding="utf-8") if fp.exists() else ""


def main():
    chapters, skipped = [], []
    for num, title, module in META:
        d = f"chapter-{num}"
        notes = read(f"{d}/notes.md")
        flashcards = read(f"{d}/flashcards.md")
        questions = read(f"{d}/questions.md")
        # A chapter folder can exist before its content is written. Omit empty
        # chapters so the site never shows a navigation entry that opens a
        # blank page.
        if not (notes or flashcards or questions):
            skipped.append(num)
            continue
        chapters.append({
            "num": num, "title": title, "module": module,
            "notes": notes, "flashcards": flashcards, "questions": questions,
        })
    # Mock papers (study-guide/mock-papers/paper-01.md …)
    papers = []
    mp_dir = BASE / "mock-papers"
    if mp_dir.exists():
        for fp in sorted(mp_dir.glob("paper-*.md")):
            num = fp.stem.split("-")[-1]
            papers.append({"num": num, "md": fp.read_text(encoding="utf-8")})
    data = {"readme": read("README.md"), "chapters": chapters, "papers": papers,
            "primer": read("financial-maths-primer.md"),
            "excel": read("excel-tvm-guide.md")}
    out = "window.STUDY_CONTENT = " + json.dumps(data, ensure_ascii=False) + ";\n"
    (HERE / "content.js").write_text(out, encoding="utf-8")
    total_q = sum(c["questions"].count("\n**Q") for c in chapters)
    paper_q = sum(p["md"].count("\n**Q") for p in papers)
    print(f"Wrote content.js: {len(out):,} bytes · {len(chapters)} chapters · "
          f"~{total_q} chapter questions · {len(papers)} mock papers (~{paper_q} questions)")
    if skipped:
        print(f"  (skipped {len(skipped)} chapter(s) with no content yet: "
              f"{', '.join(skipped)})")


if __name__ == "__main__":
    main()
