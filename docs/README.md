# 📚 NISM X-A Study Hub — Live Site

This folder is a **self-contained website** for studying the NISM Series X-A (Investment Adviser Level 1) material. It turns the chapter notes, flashcards and 2,000+ explained MCQs (in [`../study-guide`](../study-guide)) into a clean, navigable study app.

## ✨ Features
- **Sidebar navigation** — all 20 chapters grouped by the 6 official modules, each with Notes / Flashcards / Quiz.
- **Interactive flashcards** — click (or press Space) to flip; Shuffle and arrow-key navigation.
- **Quiz mode** — 100 MCQs per chapter; tap an option for instant right/wrong feedback, an inline explanation, a live score and tier filters.
- **Interactive mock tests** — 10 full-length papers built to the real **150-mark blueprint** (90 MCQs + 9 caselets), auto-scored with **25% negative marking**, a 3-hour timer and a pass/fail (60%) summary.
- **On-screen financial calculator** — TVM solver (matches Excel `PV`/`FV`/`PMT`/`RATE`/`NPER`), finance helpers (CAGR, real return, inflation, SIP, EMI) and a basic keypad.
- **Financial Maths Lab** — unlimited auto-generated PV/FV/PMT/CAGR/EMI practice with worked solutions and scoring.
- **Global search** — press `/` and search across every chapter.
- **Progress tracking** — mark sections "studied"; a progress bar remembers it (saved in your browser).
- **Dark / light mode**, adjustable text size, and a fully **mobile-friendly** layout.
- **Works offline** — all content is bundled into `content.js`, so no server is required (markdown rendering uses a CDN; if offline, text still shows).

## ▶️ How to view it

### Option A — Just open it
Open `docs/index.html` in any modern browser. Everything is bundled, so it works straight from disk.

### Option B — GitHub Pages (recommended)
1. Push this branch to GitHub.
2. Repo → **Settings → Pages**.
3. **Build and deployment → Source** → **Deploy from a branch**.
4. Pick the branch, set the folder to **`/docs`**, then **Save**.
5. After a minute the live page appears at `https://<username>.github.io/<repo-name>/`.

## 🔧 Editing content
The study text lives in `../study-guide/chapter-XX/*.md`. After editing any of those, regenerate the bundle:

```bash
python3 docs/build.py
```

This rewrites `docs/content.js` from the markdown. Commit both the markdown and the regenerated `content.js`.

## 🗂 Files
| File | Purpose |
|------|---------|
| `index.html` | Page shell |
| `style.css` | Styling + light/dark themes |
| `app.js` | Routing, flashcards, quiz, mock tests, calculator, search, progress |
| `content.js` | All chapter content, bundled (generated — do not edit by hand) |
| `build.py` | Regenerates `content.js` from `../study-guide` |
| `nism-tvm-practice.xlsx` | Downloadable TVM practice workbook |
| `.nojekyll` | Tells GitHub Pages to serve files as-is |
