#!/usr/bin/env python3
"""Static site builder for the cover-letter-with-ai-guide project.

Converts the markdown chapters in docs/ and the before/after examples in
examples/ into a plain, dependency-free static site in site/.

Usage:
    python3 build.py           # build site/ from docs/ and examples/
    python3 build.py --test    # run build self-tests, then build

No external packages are used, so this runs anywhere Python 3.8+ runs.
Everything stays strictly local: no network, no accounts, no uploads.
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
EXAMPLES = ROOT / "examples"
SITE = ROOT / "site"

COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"

CHAPTERS = [
    ("00-read-me-first.md", "Read Me First"),
    ("01-structure-that-reads-human.md", "1. Structure That Reads Human"),
    ("02-tailor-per-posting.md", "2. Tailoring One Letter Per Posting"),
    ("03-proof-prompts-resume.md", "3. Proof-Pulling Prompt Recipes"),
    ("04-nurse-pivot-examples.md", "4. Nurse-to-Nonclinical Pivot Examples"),
    ("05-ats-safe-formatting.md", "5. ATS-Safe Formatting"),
    ("06-privacy-local-ollama.md", "6. Privacy & Local AI (Ollama)"),
]

EXAMPLE_PAGES = [
    ("before-letter-A.md", "Example A — Before"),
    ("after-letter-A.md", "Example A — After"),
    ("before-letter-B.md", "Example B — Before (snippet)"),
    ("after-letter-B.md", "Example B — After"),
    ("sanitized-prompt-pack.md", "Sanitized Prompt Pack"),
    ("proof-bank-sample.md", "Sample Proof Bank"),
]


# --------------------------------------------------------------------------
# Minimal markdown -> HTML (enough for this manual)
# --------------------------------------------------------------------------

def inline_md(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  r'<a href="\2">\1</a>', text)
    return text


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^a-z0-9 -]", "", text.lower())
    return re.sub(r"\s+", "-", text.strip())


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):                      # fenced code block
            lang = line[3:].strip()
            block = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1  # closing fence
            cls = f' class="language-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>{html.escape(chr(10).join(block))}</code></pre>")
            continue

        if re.match(r"^#{1,4} ", line):                 # headings
            level = len(line) - len(line.lstrip("#"))
            content = inline_md(line[level + 1:].strip())
            if level == 1:
                out.append(f"<h1>{content}</h1>")
            else:
                out.append(f'<h{level} id="{slugify(line[level+1:])}">{content}</h{level}>')
            i += 1
            continue

        if line.strip() == "---":                       # horizontal rule
            out.append("<hr>")
            i += 1
            continue

        if re.match(r"^\s*\|.*\|\s*$", line):           # table
            rows = []
            while i < len(lines) and re.match(r"^\s*\|.*\|\s*$", lines[i]):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):  # skip separator row
                    rows.append(cells)
                i += 1
            if rows:
                head = rows[0]
                t = ["<table>", "<thead><tr>",
                     "".join(f"<th>{inline_md(c)}</th>" for c in head),
                     "</tr></thead>", "<tbody>"]
                for r in rows[1:]:
                    t.append("<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in r) + "</tr>")
                t.append("</tbody></table>")
                out.append("\n".join(t))
            continue

        if re.match(r"^\s*[-*] \[[ xX]\] ", line):      # GitHub-style task list
            items = []
            while i < len(lines) and re.match(r"^\s*[-*] \[[ xX]\] ", lines[i]):
                m = re.match(r"^\s*[-*] \[([ xX])\] (.*)", lines[i])
                done = m.group(1).strip() != ""
                items.append(
                    f'<li><input type="checkbox" disabled {"checked" if done else ""}> '
                    f"{inline_md(m.group(2))}</li>")
                i += 1
            out.append('<ul class="task-list">\n' + "\n".join(items) + "\n</ul>")
            continue

        m = re.match(r"^(\s*)([-*]|\d+\.) ", line)      # lists
        if m:
            ordered = not m.group(2).startswith(("-", "*"))
            tag = "ol" if ordered else "ul"
            items = []
            while i < len(lines) and re.match(fr"^{m.group(1)}([-*]|\d+\.) ", lines[i]):
                items.append(f"<li>{inline_md(lines[i][len(m.group(0)):])}</li>")
                i += 1
            out.append(f"<{tag}>\n" + "\n".join(items) + f"\n</{tag}>")
            continue

        if line.startswith(">"):                        # blockquote
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i].lstrip("> ").rstrip())
                i += 1
            out.append("<blockquote>" + md_to_html("\n".join(block)) + "</blockquote>")
            continue

        if not line.strip():                            # blank line
            i += 1
            continue

        para = []                                       # paragraph
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^(#{1,4} |```|\s*\||\s*([-*]|\d+\.) |>|---)", lines[i]):
            para.append(lines[i].rstrip())
            i += 1
        out.append("<p>" + inline_md(" ".join(para)) + "</p>")

    return "\n".join(out)


# --------------------------------------------------------------------------
# Site assembly
# --------------------------------------------------------------------------

def page(title: str, body: str, nav_html: str, extra_css: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — Cover Letters with AI</title>
<link rel="stylesheet" href="style.css">
{extra_css}
</head>
<body>
<header class="site-head">
  <a href="index.html" class="brand">Cover Letters with AI</a>
  <p class="tagline">Plain-English job-letter help, AI-assisted and privacy-aware.
  A project by <strong>Asdale Dynamics, LLC</strong> (Dylan Asdale, <em>The Massive AI Manual</em>).</p>
</header>
<div class="wrap">
<nav class="side">
{nav_html}
</nav>
<main>
{body}
</main>
</div>
<footer class="site-foot">
<p>{COPYRIGHT}. Licensed under the MIT License (see LICENSE in the project repository).</p>
</footer>
</body>
</html>
"""


def build_nav(active_file: str) -> str:
    links = []
    for f, t in CHAPTERS:
        href = "index.html" if f == "00-read-me-first.md" else f.replace(".md", ".html")
        cls = ' class="active"' if f == active_file else ""
        links.append(f'<a href="{href}"{cls}>{t}</a>')
    links.append("<h2>Examples</h2>")
    for f, t in EXAMPLE_PAGES:
        href = f"examples/{f.replace('.md', '.html')}"
        cls = ' class="active"' if f == active_file else ""
        links.append(f'<a href="{href}"{cls}>{t}</a>')
    links.append("<h2>Tools</h2>")
    links.append('<a href="before-after.html">Before &amp; After, side by side</a>')
    return "\n".join(links)


def strip_title(md: str) -> tuple[str, str]:
    """Remove the first H1 line; the page template supplies the title."""
    lines = md.splitlines()
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[0:0] + lines[1:]
    else:
        title = ""
    return title, "\n".join(lines)


def build() -> None:
    SITE.mkdir(exist_ok=True)
    (SITE / "examples").mkdir(exist_ok=True)

    # stylesheet: static source asset, copied verbatim
    css_src = ROOT / "assets" / "style.css"
    css = css_src.read_text()
    (SITE / "style.css").write_text(css)

    md_files = {f: (DOCS / f).read_text() for f, _ in CHAPTERS}
    md_files.update({f: (EXAMPLES / f).read_text() for f, _ in EXAMPLE_PAGES})

    # main chapters (and the intro as index)
    for name, title in CHAPTERS:
        md = md_files[name]
        _, content = strip_title(md)
        is_home = name == "00-read-me-first.md"
        if is_home:
            content = (
                '<div class="hero">\n'
                "  <h1>Write a Cover Letter with Free AI Help</h1>\n"
                "  <p>A plain-English manual: structure that reads human, one tailored "
                "letter per posting, prompts that pull proof from your own resume, "
                "nurse-to-nonclinical pivot examples, ATS-safe formatting, and a hard "
                "privacy rule for local-only AI.</p>\n"
                '  <p><a class="btn" href="01-structure-that-reads-human.html">Start with Chapter 1 &rarr;</a>'
                '  <a class="btn ghost" href="before-after.html">Jump to before &amp; after</a></p>\n'
                "</div>\n" + content
            )
            fname = "index.html"
            nav_active = "00-read-me-first.md"
        else:
            fname = name.replace(".md", ".html")
            nav_active = name
        (SITE / fname).write_text(page(title, md_to_html(content),
                                       build_nav(nav_active)))

    # example pages
    for name, title in EXAMPLE_PAGES:
        md = md_files[name]
        h1, content = strip_title(md)
        heading = f"<h1>{inline_md(h1)}</h1>" if h1 else ""
        body = heading + md_to_html(content)
        (SITE / "examples" / name.replace(".md", ".html")).write_text(
            page(title, body, build_nav(name)))

    # side-by-side comparison page
    before_html = md_to_html(strip_title(md_files["before-letter-A.md"])[1])
    after_html = md_to_html(strip_title(md_files["after-letter-A.md"])[1])
    compare = f"""<h1>Before &amp; After, Side by Side</h1>
<p>The same (fictional) writer, same skill set, same target job. The left letter
is what a chatbot produces from a cold, unguarded prompt. The right letter is the
output of Chapters 1&ndash;6: proof-bank facts only, one argument, honest bridge,
sanitized inputs, voice pass.</p>
<div class="compare">
  <div class="col"><h2>Before &mdash; generic AI draft</h2>{before_html}</div>
  <div class="col"><h2>After &mdash; the full process</h2>{after_html}</div>
</div>"""
    (SITE / "before-after.html").write_text(
        page("Before & After", compare, build_nav("before-after.html")))

    print(f"Built {len(CHAPTERS) + len(EXAMPLE_PAGES) + 2} pages into site/")


# --------------------------------------------------------------------------
# Self-tests (python3 build.py --test)
# --------------------------------------------------------------------------

def run_tests() -> None:
    import glob

    failures = []
    counter = {"n": 0}

    def check(name: str, cond: bool):
        counter["n"] += 1
        if not cond:
            failures.append(name)

    h = md_to_html("# Title\n\nPara with **bold**, *italic*, and `code`.\n")
    check("h1 converted", "<h1>Title</h1>" in h)
    check("bold converted", "<strong>bold</strong>" in h)
    check("italic converted", "<em>italic</em>" in h)
    check("code converted", "<code>code</code>" in h)

    h = md_to_html("- a\n- b\n")
    check("ul converted", h.count("<li>") == 2)

    h = md_to_html("1. one\n2. two\n")
    check("ol converted", "<ol>" in h)

    h = md_to_html("| a | b |\n|---|---|\n| 1 | 2 |\n")
    check("table converted", "<table>" in h and h.count("<td>") == 2 and h.count("<th>") == 2)

    h = md_to_html("```\n"""
                   "x = 1 < 2\n```\n")
    check("code fence escapes", "&lt;" in h)

    h = md_to_html("- [x] done\n- [ ] todo\n")
    check("task list converted", 'type="checkbox"' in h and "checked" in h)

    h = md_to_html("[link](http://example.com)\n")
    check("links converted", '<a href="http://example.com">link</a>' in h)

    h = md_to_html("> quote\n")
    check("blockquote converted", "<blockquote>" in h)

    h = md_to_html("HTML <script>alert(1)</script>\n")
    check("html escaped", "<script>" not in h)

    # every docs chapter and template must carry the correct copyright line
    copyright_re = re.compile(r"Copyright \(c\) 2026 Asdale Dynamics, LLC\. "
                              r"Licensed under the MIT License\.")
    for path in glob.glob(str(DOCS / "*.md")) + glob.glob(str(DOCS / "templates" / "*.md")) \
            + glob.glob(str(EXAMPLES / "*.md")):
        text = Path(path).read_text()
        check(f"copyright line present in {Path(path).name}", copyright_re.search(text) is not None)

    # privacy spot-check: no real-looking employer names leaking into examples
    banned = [r"St\.\s*Vincent", r"Mercy\s+Health", r"Lakeview\s+Clinic"]
    for path in glob.glob(str(EXAMPLES / "*.md")):
        text = Path(path).read_text()
        for b in banned:
            check(f"no real-ish employer leak '{b}' in {Path(path).name}",
                  re.search(b, text) is None)

    if failures:
        print("FAILED:\n  - " + "\n  - ".join(failures))
        sys.exit(1)
    print(f"All {counter['n']} self-tests passed.")


if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    build()
