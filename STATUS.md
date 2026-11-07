# STATUS

Last updated: 2026-11-07

## What was built

**cover-letter-with-ai-guide** — a beginner-friendly manual for writing job
cover letters with free AI help, delivered as Markdown documentation plus a
generated static site.

- `docs/00-read-me-first.md` — orientation, the three rules, project scope
- `docs/01-structure-that-reads-human.md` — the 6-part, under-250-word letter
  structure, the "one argument" principle, and the AI-voice failure modes
- `docs/02-tailor-per-posting.md` — a 10–15 minute per-posting tailoring
  process with an exaggeration guard table (led → coordinated, etc.)
- `docs/03-proof-prompts-resume.md` — five prompt recipes that force the AI to
  work only from facts you supply: extraction, five-hooks, one-argument draft,
  interview-probe stress test, voice match; plus the proof-bank concept
- `docs/04-nurse-pivot-examples.md` — clinical-to-nonclinical transfer table,
  two full before-and-after examples (customer-success and analyst paths)
- `docs/05-ats-safe-formatting.md` — ATS do/don't list, a never-fails letter
  layout, and the copy-paste plain-text pre-send test
- `docs/06-privacy-local-ollama.md` — the privacy rule (never paste employer
  names or personal data into cloud tools), the swap technique for unavoidable
  cloud use, and full local-first instructions for Ollama with honest
  calibration of what local models can and cannot do
- `docs/templates/` — two fill-in letter skeletons (general, pivot)
- `examples/` — fictional-composite before/after letters (A: customer success,
  B: analyst), a sanitized prompt pack, and a sample proof bank
- `build.py` — dependency-free Python site builder (Markdown → HTML, stdlib
  only) with a `--test` self-test mode
- `site/` — the built static site: index, 6 chapter pages, 6 example pages,
  and a side-by-side **Before & After** comparison page
- `LICENSE` (MIT, "Copyright (c) 2026 Asdale Dynamics, LLC"), `README.md`,
  `assets/style.css`

## How to run it

```bash
python3 build.py --test   # run all self-tests, then build site/
python3 build.py          # build without tests
```

Then open `site/index.html` in a browser. No server, dependencies, or accounts
required. Requires Python 3.8+ (standard library only).

## Verification results

- `python3 build.py --test` → **all 45 self-tests passed**, covering:
  - Markdown converter correctness (headings, bold/italic/code inline,
    ordered/unordered lists, tables, fenced-code escaping, task lists, links,
    blockquotes, HTML-escaping/XSS safety)
  - Required copyright line present in every docs, template, and example file
  - Privacy spot-check: no real-looking employer names in any example file
- Rebuild verification: `python3 build.py` → 15 pages regenerated into `site/`
- Content checks on generated HTML: hero/nav present, task lists and tables
  render, comparison page structure, letter text and sanitized prompt intact
- Manual note: the site was verified opened-free (file:// works); no automated
  browser screenshot tests exist (see gaps)

## Known gaps

- The site is informational HTML/CSS only — no JavaScript, no search, no dark
  mode.
- Chapter 6's Ollama instructions were not executed here (no Ollama install in
  the build environment); commands follow current documented usage and should
  be re-checked against `ollama.com` when used.
- Example letters are intentionally fictional composites; they demonstrate the
  process but are not a corpus of real successful letters.
- No coverage/CI config; tests live in `build.py --test` and are intended for
  local runs. `site/` is committed as a convenience artifact — rebuild it after
  any docs change.
- The 15-page count printed by the builder counts the stylesheet-bearing pages
  plus the index and comparison page but not `style.css` itself; cosmetic.
