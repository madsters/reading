#!/usr/bin/env python3
"""Render a Q&A markdown log to a MathJax HTML page for the terminal phase.

For when you're doing Q&A in the terminal rather than a Claude Project: Claude
appends each answer (with $...$ / $$...$$) to qa/<slug>.md, then this regenerates
qa/<slug>.html with MathJax so you read the rendered maths in a browser pane
beside the terminal. The rule: the terminal is for asking, a rendered file is for
reading.

    python make_qa_html.py materials/<slug>/qa/<slug>.md
"""
from __future__ import annotations

import argparse
from pathlib import Path

HTML_TEMPLATE = """<!doctype html>
<html><head><meta charset="utf-8">
<title>{title}</title>
<script>
window.MathJax = {{ tex: {{ inlineMath: [['$','$']], displayMath: [['$$','$$']] }} }};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
<style>body{{max-width:48rem;margin:2rem auto;font:16px/1.6 system-ui;padding:0 1rem}}</style>
</head><body>
{body}
</body></html>
"""


def render(md_path: Path) -> Path:
    """Markdown -> MathJax HTML next to the source. Returns the html path.

    Sketch: convert markdown body to HTML (leave $...$/$$...$$ untouched so
    MathJax handles them), drop into HTML_TEMPLATE, write qa/<slug>.html.
    Pair with a live-reloading static server for ask-while-you-read.
    """
    # TODO: md -> html body (markdown lib), preserving math delimiters
    raise NotImplementedError("make_qa_html: wire up markdown->html body render")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("md", type=Path)
    args = ap.parse_args()
    print(render(args.md))


if __name__ == "__main__":
    main()
