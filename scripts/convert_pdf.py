#!/usr/bin/env python3
"""Math-aware PDF -> markdown, with per-region confidence flags.

Path 3 of the waterfall — for journal papers / documents / slide-PDFs with no
LaTeX source. Uses a converter that emits real LaTeX commands (\\mathbf,
\\boldsymbol) rather than flattened vision-to-markdown, so boldedness largely
survives. Emits a confidence sidecar so the notation stage knows which regions
to put in front of the user (flag-driven confirmation).

    python convert_pdf.py in.pdf --out materials/<slug>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def convert(pdf: Path, out: Path) -> dict:
    """Return {markdown_path, flags_path}.

    Sketch:
      1. Run the math-aware converter (marker/nougat/docling — chosen at install
         time) over `pdf`, writing material.md.
      2. Capture per-block confidence where the tool exposes it; anything below
         threshold, or any region the tool marks as low-quality, goes into
         flags.json as {page, snippet, reason}.
      3. Do NOT auto-correct — flagging is honest, correction is the user's call.
    """
    out.mkdir(parents=True, exist_ok=True)
    # TODO: invoke converter; write out/material.md
    # TODO: collect low-confidence regions -> out/flags.json
    raise NotImplementedError("convert_pdf: wire up math-aware converter + flags")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    print(json.dumps(convert(args.pdf, args.out), indent=2))


if __name__ == "__main__":
    main()
