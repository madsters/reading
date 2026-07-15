#!/usr/bin/env python3
"""Render a Q&A markdown log to a MathJax HTML page for the terminal phase.

For Q&A in the terminal rather than a Claude Project: Claude appends each answer
(with $...$ / $$...$$) to qa/<slug>.md, then this regenerates qa/<slug>.html with
MathJax so you read the rendered maths in a browser pane beside the terminal.
The rule: the terminal is for asking, a rendered file is for reading.

Math spans are protected from the markdown pass so underscores/backslashes inside
equations survive intact for MathJax.

    python make_qa_html.py materials/<slug>/qa/<slug>.md
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import markdown

HTML_TEMPLATE = """<!doctype html>
<html><head><meta charset="utf-8">
<title>{title}</title>
<script>
window.MathJax = {{ tex: {{ inlineMath: [['$','$']], displayMath: [['$$','$$']] }} }};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
<style>
 body{{max-width:48rem;margin:2rem auto;font:16px/1.6 system-ui,sans-serif;padding:0 1rem}}
 pre,code{{background:#f4f4f4;border-radius:4px}}
 pre{{padding:.8em;overflow:auto}} code{{padding:.1em .3em}}
 h1,h2,h3{{line-height:1.2}} hr{{border:none;border-top:1px solid #ddd;margin:2em 0}}
</style>
</head><body>
{body}
</body></html>
"""


def _protect_math(text: str):
    """Replace $$...$$ and $...$ spans with placeholders; return (text, spans)."""
    spans: list[str] = []

    def stash(m):
        spans.append(m.group(0))
        return f"\x00MATH{len(spans) - 1}\x00"

    text = re.sub(r"\$\$.*?\$\$", stash, text, flags=re.S)      # display first
    text = re.sub(r"(?<!\$)\$(?!\$).+?(?<!\$)\$(?!\$)", stash, text, flags=re.S)
    return text, spans


def render(md_path: Path) -> Path:
    raw = md_path.read_text()
    protected, spans = _protect_math(raw)
    body = markdown.markdown(protected, extensions=["extra", "sane_lists", "tables"])
    for i, span in enumerate(spans):
        body = body.replace(f"\x00MATH{i}\x00", span)

    html_path = md_path.with_suffix(".html")
    html_path.write_text(HTML_TEMPLATE.format(title=md_path.stem, body=body))
    return html_path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("md", type=Path)
    args = ap.parse_args()
    print(render(args.md))


if __name__ == "__main__":
    main()
