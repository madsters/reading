#!/usr/bin/env python3
"""Compile a filled one-pager template to PDF and assert it's exactly one page.

The one-page guarantee is compile-and-check, not vibes: if the draft overflows,
this fails loudly so the LLM trims and retries. Template is profile-aware —
onepager_paper.tex for papers, onepager_digest.tex for tutorials/documents.

    python build_onepager.py materials/<slug>/onepager.tex --out materials/<slug>/onepager.pdf
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def page_count(pdf: Path) -> int:
    """Sketch: `pdfinfo <pdf>` -> parse 'Pages:' line (or use pypdf)."""
    raise NotImplementedError


def build(tex: Path, out: Path) -> None:
    """Compile with a single-binary LaTeX engine, then assert one page.

    Sketch:
      1. subprocess.run(["tectonic", str(tex), "--outdir", out.parent]) — or the
         installed engine; check=True and surface the log on failure.
      2. n = page_count(out); if n != 1: raise SystemExit(f"overflow: {n} pages")
         so the caller knows to trim.
    """
    # TODO: compile tex -> out
    n = page_count(out)
    if n != 1:
        sys.exit(f"one-pager is {n} pages, not 1 — trim and recompile")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tex", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    build(args.tex, args.out)
    print(f"ok: {args.out} (1 page)")


if __name__ == "__main__":
    main()
