#!/usr/bin/env python3
"""Bundle the study hub into ONE self-contained .html file.

The GitHub Pages site (docs/index.html) loads style.css, vendor/marked.min.js,
content.js and app.js as separate files. Some hosts — notably sandboxed
preview/artifact environments with a strict Content-Security-Policy — block
every external request and only accept a single inlined document.

This script produces exactly that: one HTML file with the stylesheet, the
markdown parser, the bundled content and the app all inlined, and no reference
to any external host (no CDN, no web fonts — the CSS already falls back to
system fonts).

    python3 docs/build.py           # refresh content.js first
    python3 docs/build_artifact.py  # then bundle

Output: docs/standalone.html
"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "standalone.html"

TITLE = "NISM X-A Study Hub — Investment Adviser (Level 1)"


def read(name):
    fp = HERE / name
    if not fp.exists():
        raise SystemExit(f"missing {fp} — run `python3 docs/build.py` first")
    return fp.read_text(encoding="utf-8")


def body_of(html):
    """Extract everything between <body> and </body> from index.html."""
    m = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    if not m:
        raise SystemExit("could not find <body> in index.html")
    inner = m.group(1)
    # drop the external <script src=...> tags — we inline them below instead
    inner = re.sub(r"<script[^>]*\bsrc=[^>]*>\s*</script>", "", inner, flags=re.I)
    # drop any HTML comments that referenced the removed scripts
    inner = re.sub(r"<!--.*?-->", "", inner, flags=re.S)
    return inner.strip()


def main():
    index = read("index.html")
    css = read("style.css")
    marked = read("vendor/marked.min.js")
    content = read("content.js")
    app = read("app.js")

    parts = [
        f"<title>{TITLE}</title>",
        # No theme bootstrap here on purpose: app.js already honours a
        # data-theme stamped on <html> by the host, then the OS colour-scheme
        # preference, and only persists a theme the reader actively picks.
        "<style>\n" + css + "\n</style>",
        body_of(index),
        "<script>\n" + marked + "\n</script>",
        "<script>\n" + content + "\n</script>",
        "<script>\n" + app + "\n</script>",
    ]
    html = "\n".join(parts) + "\n"
    OUT.write_text(html, encoding="utf-8")

    assert "cdn.jsdelivr.net" not in html, "external CDN reference survived"
    assert "fonts.googleapis.com" not in html, "external font reference survived"
    print(f"Wrote {OUT.name}: {len(html):,} bytes — fully self-contained "
          f"(no external requests)")


if __name__ == "__main__":
    main()
