#!/usr/bin/env python3
"""Convert a general document (.docx and friends) to markdown.

Path for the `document` profile — reports, notes, anything that isn't a paper or
a deck. Uses Docling (equation-preserving); it handles docx/pptx/html/md natively.

    python convert_doc.py report.docx --out materials/<slug>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from docling_convert import convert_with_docling


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("doc", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    print(json.dumps(convert_with_docling(args.doc, args.out), indent=2))


if __name__ == "__main__":
    main()
