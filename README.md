# Cover Letters with AI

A beginner-friendly manual for writing job cover letters with free AI help —
clear, warm, step by step, never condescending. Explained "like a friend would."
A project by **Asdale Dynamics, LLC** (Dylan Asdale, author of *The Massive AI
Manual*).

## What's inside

| Resource | What it is |
|---|---|
| `docs/` | The manual: 6 chapters in Markdown — structure that reads human, tailoring one letter per posting, proof-pulling prompts, nurse-to-nonclinical pivot examples, ATS-safe formatting, and the privacy rule (local AI with Ollama) |
| `docs/templates/` | Copy-paste letter skeletons (general + clinical-to-nonclinical pivot) |
| `examples/` | Before-and-after letters, a sanitized prompt pack, and a sample proof bank (all fictional composites — no real personal data) |
| `site/` | A generated static site: the whole manual plus a side-by-side **Before & After** comparison page |

## The three rules worth remembering

1. **The AI drafts; you decide.** Every sentence must be true about you and sound like you.
2. **One posting, one letter.** Mass-applied identical letters read identical.
3. **Names out, meaning in.** Never paste employer names or personal details into cloud AI tools — swap them for neutral descriptions, or better, keep everything local with Ollama.

## How to view the site

```bash
python3 build.py --test    # run build self-tests and (re)build site/
python3 build.py           # build only
```

Then open `site/index.html` in any browser — no server, no dependencies, no data leaves your machine. (Optional: `python3 -m http.server -d site 8000` and visit `http://localhost:8000`.)

Requires only Python 3.8+ (standard library only). Building overwrites
`site/` — treat it as a build artifact, versioned for convenience.

## Privacy promise

- No secrets, API keys, or personal data live in this repository.
- All worked examples are fictional composites, written deliberately so they
  cannot leak anyone's real employer, dates, or details.
- The manual actively teaches local-first AI: every prompt should aim at an
  Ollama-style local model, with cloud tools as the sanitized fallback only.
- A build self-test (`python3 build.py --test`) checks for accidental
  real-looking employer-name leaks in the examples.

## Related projects

- `ats-resume-checker-cli` — resume parsing/scoring (the *resume* side of ATS safety)
- `free-interview-prep-pack` — interview coaching (the step *after* the letter)

## Education, not advice

This manual is software-education material. It is not legal, career, medical,
or professional advice. Healthcare-worker content is educational only and is
never medical advice.

## License

MIT — see `LICENSE`.

Copyright (c) 2026 Asdale Dynamics, LLC
