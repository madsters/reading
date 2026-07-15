#!/usr/bin/env python3
"""Math-aware PDF -> markdown, with per-region confidence flags.

Path 3 of the waterfall — for journal papers / documents / slide-PDFs with no
LaTeX source. Uses Docling, which emits real LaTeX commands (\\mathbf,
\\boldsymbol) rather than flattened vision-to-markdown, so boldedness largely
survives. Emits a confidence sidecar so the notation stage knows which regions
to put in front of the user (flag-driven confirmation).

    python convert_pdf.py in.pdf --out materials/<slug>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from docling_convert import convert_with_docling


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--no-ocr", action="store_true",
                    help="skip OCR (use for born-digital PDFs with a text layer)")
    ap.add_argument("--no-formula", action="store_true",
                    help="skip formula->LaTeX enrichment")
    args = ap.parse_args()
    print(json.dumps(convert_with_docling(
        args.pdf, args.out, do_ocr=not args.no_ocr, do_formula=not args.no_formula),
        indent=2))


if __name__ == "__main__":
    main()
