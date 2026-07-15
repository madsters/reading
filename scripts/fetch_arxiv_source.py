#!/usr/bin/env python3
"""Fetch an arXiv paper's LaTeX source and flatten it to a single .tex.

Path 1 of the ingestion waterfall — zero fidelity loss. Downloads the author's
e-print tarball, unpacks it, finds the root .tex, and flattens \\input/\\include
with latexpand so every equation arrives exactly as written.

    python fetch_arxiv_source.py 2401.01234 --out materials/<slug>/source
"""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

EPRINT_URL = "https://arxiv.org/e-print/{arxiv_id}"


def fetch(arxiv_id: str, out: Path) -> Path:
    """Download + unpack + flatten. Returns path to flattened .tex."""
    out.mkdir(parents=True, exist_ok=True)
    # TODO: GET EPRINT_URL (it's a gzipped tar, sometimes a bare .tex.gz).
    #       Save to out/source.tar.gz, detect format, extract into out/raw/.
    # TODO: locate root tex = the file containing \documentclass.
    # TODO: run latexpand to flatten:
    #           latexpand <root>.tex > out/flattened.tex
    #       (subprocess.run, check=True; surface stderr on failure).
    raise NotImplementedError("fetch_arxiv_source: wire up download + latexpand")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("arxiv_id")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    print(fetch(args.arxiv_id, args.out))


if __name__ == "__main__":
    main()
