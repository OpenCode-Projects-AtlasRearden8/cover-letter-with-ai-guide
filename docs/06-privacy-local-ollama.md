# Chapter 6 — The Privacy Rule: Local AI With Ollama

## The rule, stated once and plainly

**Never paste employer names, colleague details, patient information, dates or places that identify you, or anything else personal into cloud AI tools.**

Everything a cloud tool receives may be stored, logged, used for training, or breached. A cover letter is full of identifying material: where you worked, what years, what unit, whom you trained, what your employer's quality issues were. Treat all of it as potentially identifying information — because a determined person can often reconstruct "which nurse" from surprisingly little. (And if you are a healthcare worker, the bar is higher still: anything resembling patient details may carry compliance obligations far beyond embarrassment.)

The good news: you do not need cloud tools for any of this. A modern laptop runs excellent models locally, free, with nothing ever leaving the machine.

## The swap technique (minimum safe practice, if you must use a cloud chat)

If a cloud chat is your only option, sanitize first using neutral stand-ins:

| Real | Swapped |
|---|---|
| St. Vincent Regional Medical Center | "a 400-bed community hospital" |
| Mercy Health Network, 2019–2025 | "a multi-site provider network, six recent years" |
| precepted Priya and Marcus | "precepted two new grads" |
| Lakeview Clinic's fall rates | "our unit's fall rates" |

Write letters addressed to the neutral stand-in, and put the real names back only in your local final file, after the AI work is done. The letter content does not change — the AI never needed the truth of the names, only the shape of the facts.

Even with swaps, prefer local. Swaps are the fallback, not the plan.

## Local-first with Ollama (the real solution)

**Ollama** runs open-weight models entirely on your computer. No account, no upload, no cloud round trip. Free.

**One-time setup (10 minutes):**

1. Download Ollama from `ollama.com` (Windows/macOS/Linux).
2. Open a terminal and pull a good general model:
   - `ollama pull llama3.1` (balanced; runs on most 16 GB machines)
   - `ollama pull qwen2.5` — strong writing quality, similar size
   - If you have 16 GB+ RAM and patience, `ollama pull qwen2.5:14b` writes noticeably better.
3. Test: `ollama run llama3.1 "Say hello in one sentence."`

**The daily flow:**

- Interactive chat: `ollama run llama3.1`, then paste your sanitized prompt. Type `/bye` to exit.
- One-shot (great for the Chapter 3 recipes): 
  ```
  ollama run llama3.1 "Draft a 200-word cover letter using ONLY these facts: ..." < proof-bank.txt
  ```
  or write your prompt to a file and pipe it: `ollama run llama3.1 "$(cat prompt.txt)"`.
- Long proof banks work fine — paste the whole thing. Local context windows on these models (8–32k) handle entire sanitized resumes and postings at once.

**UI wrapper (optional):** tools like **Open WebUI** give Ollama a browser-style chat window, still fully local. Nice if you prefer chat windows to terminals.

## What local models can and can't do (honest calibration)

- **Can:** brainstorm hooks, restructure sentences, translate clinical → nonclinical language, draft from your facts, red-team your letter's claims, match voice.
- **Cannot (as reliably as giant cloud models):** recall niche industry conventions, and — the big one — they are more confident and less self-critical. Chapter 3's "flag weak claims" instructions matter more locally, not less. You are the editor regardless.
- **Speed:** a 8B model on a modern laptop is fully usable for text work; expect a few seconds per answer, not instant.

## Local file hygiene (often forgotten)

The privacy rule extends past AI:

- Keep the proof bank and letters in a folder with no auto-sync to cloud drives (or accept and audit that sync).
- Emails: paste the letter, never attach the proof bank.
- Portfolio/website: if you publish a letter as a writing sample (as this project's site does with fictional examples), keep it fictional and scrubbed — which is exactly why all examples here are fictional composites, not Dylan's real letters.

## A quick self-audit before you hit send 

1. Does the letter contain any credential, name, or identifier the *cloud tool ever saw*? (If you used Ollama locally throughout: it can't have.)
2. Does my sent file contain my real contact info only where the employer expects it? Yes — that is the one place identifying data *belongs*: in your application to the employer, never in the tools.

Local tools, swapped drafts, real letter at the end. That is the whole technique.

---
Copyright (c) 2026 Asdale Dynamics, LLC. Licensed under the MIT License.
