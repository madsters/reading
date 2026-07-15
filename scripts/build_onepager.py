#!/usr/bin/env python3
"""Compile a filled one-pager template to PDF and assert it's exactly one page.

The one-page guarantee is compile-and-check, not vibes: if the draft overflows,
this fails loudly (non-zero exit) so the LLM trims and retries. Template is
profile-aware — the caller picks onepager_paper.tex or onepager_digest.tex.

    python build_onepager.py materials/<slug>/onepager.tex --out materials/<slug>/onepager.pdf
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader


def page_count(pdf: Path) -> int:
    return len(PdfReader(str(pdf)).pages)


def _compile(tex: Path, outdir: Path) -> None:
    """Prefer tectonic (single binary, auto-fetches packages); fall back to latexmk."""
    if shutil.which("tectonic"):
        cmd = ["tectonic", str(tex), "--outdir", str(outdir)]
    elif shutil.which("latexmk"):
        cmd = ["latexmk", "-pdf", f"-outdir={outdir}", str(tex)]
    else:
        sys.exit("no LaTeX engine found (install tectonic or latexmk)")
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"LaTeX compile failed:\n{proc.stdout[-2000:]}\n{proc.stderr[-2000:]}")


def build(tex: Path, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    _compile(tex, out.parent)

    produced = out.parent / (tex.stem + ".pdf")
    if produced != out and produced.exists():
        produced.replace(out)

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
