# Chapter 5 — ATS-Safe Formatting

## What an ATS actually does

An Applicant Tracking System (ATS) parses your file into plain text: name, contact, sections, dates, keywords. Format it reads cleanly → you are evaluated as a candidate. Format it chokes on → you may be evaluated as a jumble of fragments, or not evaluated at all. Same humans, same words — completely different outcomes.

A cover letter is usually read lightly by ATS (resumes get the parsing pressure), but it is frequently routed with the resume as one packet, and sloppy files can corrupt the bundle. Keep letters ATS-clean for the same reason you keep a resume clean.

## The rules

**Do:**

- **File types:** `.docx` first, `.pdf` an accepted backup; if the portal asks for plain pasted text, paste plain text. Follow whatever the posting specifies, always.
- **Standard structure top to bottom:** Name, phone or email (one or the other — this guide prefers no street address), date optional, greeting, body, sign-off.
- **Plain section labels** if you use any ("Cover Letter" as a heading or title line is fine).
- **Standard fonts** (Calibri, Arial, Georgia, Times). 11–12 pt.
- **Simple margins** (1 inch is fine), left-aligned text.
- **Exact keyword echo** from the posting, spelled the way the posting spells it ("nurse case management," not "case-management nursing").
- **Straight quotes and normal dashes.** Smart quotes (`" "`) and em dashes from fancy editors usually survive, but straight ones never fail.

**Don't:**

- No text boxes, columns, tables, or sidebars — these scramble in extraction.
- No headers/footers holding important text; some parsers skip them entirely.
- No images, logos, icons, or graphics.
- No fancy bullet glyphs; hyphens only if bullets are needed at all.
- No watermarks or background shading.
- No tiny font or exotic spacing tricks to fit a page.

## The layout that never fails

```
Sam R.
sam.r.email@example.com

Dear Ms. Okafor,

You're hiring ..., and I've spent ...

[three short paragraphs, left aligned]

Thank you for reading.

Sam R.
```

Single column. Five visual blocks. That is the entire aesthetic — and it also happens to read best for humans.

## Test before you send: the two-minute check

1. **Copy-paste test.** Select all in your editor, copy, paste into Notepad (or any plain-text window). If the paste reads as clean top-to-bottom text with no lost sentences, an ATS extraction will likely survive too. If sentences appear out of order, you have a text box or column somewhere.
2. **Rename sanity.** `Cover-Letter-SamR-Customer-Success.docx` — not `letter_v7_FINAL_final(2).docx`.
3. **Filename and email match the application.** If you use a different first name in the letter than on the resume, one of them is wrong.

## The one overlap worth noting

ATS safety is mostly the *resume's* problem — that is a whole separate discipline, covered by the related `ats-resume-checker-cli` project, which scores resume parsing directly. This chapter keeps your letter from being the weak link in the packet.

---
Copyright (c) 2026 Asdale Dynamics, LLC. Licensed under the MIT License.
