# Chapter 3 — Prompt Recipes That Pull Proof From Your Resume

## The core idea: mine, don't invent

The single biggest failure of AI cover letters is invention. The model was trained on millions of letters full of "spearheaded" and "results-driven," and left alone it will give them back to you — attached to accomplishments you never had. The fix is to make the AI work only from material **you supply**, and to structure your prompts so the model's job is *transfer and phrasing*, not fabrication.

## Step 0 — Build a proof bank (do this once, reuse forever)

Before any letter, write — by hand — 10–15 bullets of raw fact from your career. Not polished resume lines; raw true things with whatever numbers you remember:

```
- 6 years med-surg, then 2 years PACU
- charge nurse ~2 shifts/week for last 3 years on a 32-bed unit
- ran the unit's fall-prevention huddle for a quarter; falls dropped from 9 to 4 in the month (small sample, be careful how it's worded)
- precepted 5 new grads
- built a shift-change handoff checklist in Word that charge nurses kept using after I left
- Epic certified Ask- me flow... (whatever is literally true)
- volunteered to pilot the unit's smart-pump rollout; trained 20 night-shift RNs
```

Keep this file. It is the raw material for every letter, and — sanitized per Chapter 6 — the only thing that ever goes into an AI tool.

## Recipe 1 — The extraction prompt (resume → proof bank)

Prompt shape (local Ollama or any chat):

> "I will paste raw career notes. Extract every fact that could serve as evidence for these skills: [three skills]. Group them under each skill. Flag anything that sounds boastful beyond what the notes support. Do not invent or upgrade anything. Notes: [paste]"

Then delete anything you can't back with a real memory.

## Recipe 2 — The five-hooks prompt

> "I'm applying for [ROLE TITLE]. The posting repeats these wants: [list]. Here are true facts from my background: [paste proof bank section]. Give me 5 opening sentences, each using only facts I provided, each naming either the role or a want from the posting. Keep them under 25 words. Number them."

Pick one, then rewrite it in your own voice. Expect to edit heavily — that's fine, the AI did the scaffolding.

## Recipe 3 — The one-argument draft prompt

> "Draft a 200-word cover letter. One argument: [e.g., 'I've already done parts of this job in a different setting']. Use only the facts listed below — if you're unsure whether something supports the argument, leave it out and note that at the end. Neutralize employer names (say 'a 400-bed community hospital'). Plain sentences, not resume-speak. After the draft, list any sentence where you added a word stronger than the facts support, so I can soften it.
> Facts: [paste]
> Role details: [paste sanitized posting]"

## Recipe 4 — The interview-probe prompt (your honesty stress-test)

> "Act as an interviewer for [role]. For each claim in this letter, tell me what question I should expect in an interview. Mark any claim you think I'd struggle to defend. Letter: [paste]"

Whatever it flags, soften or cut. This is the single best guard against exaggeration: the letter only makes promises you're glad to defend.

## Recipe 5 — The voice match prompt

> "Here's a paragraph I wrote myself, in my own voice: [paste something from a real email or message]. Here's my letter draft: [paste]. Rewrite the draft to match my voice's length of sentences and word choices. Do not change the facts or add anything new."

## Rules that keep prompts honest

1. **Facts in, phrasing out.** Never ask "write me a cover letter for X" cold — that is how fiction is born.
2. **Ask for uncertainty flags.** Every recipe above ends with an instruction to flag weak or invented-sounding lines. Models do this surprisingly well when asked.
3. **Money quote testing:** if a sentence contains a number, it must be *your* number. If the AI produced a number you never gave it, that sentence dies.
4. **Small sample honesty.** "Falls dropped 9→4 in one month" can be said truthfully in an interview with context; in a letter, write "led our unit's fall-prevention huddle" and save the number for conversation where you can qualify it.

---
Copyright (c) 2026 Asdale Dynamics, LLC. Licensed under the MIT License.
