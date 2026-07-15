#!/usr/bin/env python3
"""Convert a general document (.docx and friends) to markdown.

Path for the `document` profile — reports, notes, anything that isn't a paper or
a deck. Prefers a converter that preserves equations; falls back to pandoc.

    python convert_doc.py report.docx --out materials/<slug>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def convert(doc: Path, out: Path) -> dict:
    """Return {markdown_path, flags_path}.

    Sketch:
      1. .docx -> markdown via pandoc (--from docx --to gfm --mathjax) or a
         math-preserving converter; write out/material.md.
      2. If the doc embeds images/equations as pictures, hand those to the
         math-aware path (convert_pdf-style) and flag as low-confidence.
      3. Write any doubtful regions to out/flags.json for flag-driven review.
    """
    out.mkdir(parents=True, exist_ok=True)
    # TODO: pandoc/docling conversion -> out/material.md (+ flags.json)
    raise NotImplementedError("convert_doc: wire up docx->md conversion")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("doc", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    print(json.dumps(convert(args.doc, args.out), indent=2))


if __name__ == "__main__":
    main()
