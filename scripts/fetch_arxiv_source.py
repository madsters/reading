#!/usr/bin/env python3
"""Fetch an arXiv paper's LaTeX source and flatten it to a single .tex.

Path 1 of the ingestion waterfall — zero fidelity loss. Downloads the author's
e-print tarball, unpacks it, finds the root .tex, and flattens \\input/\\include
with latexpand so every equation arrives exactly as written.

    python fetch_arxiv_source.py 2401.01234 --out materials/<slug>/source
"""
from __future__ import annotations

import argparse
import gzip
import io
import re
import shutil
import subprocess
import tarfile
from pathlib import Path

import requests

EPRINT_URL = "https://arxiv.org/e-print/{arxiv_id}"
# arXiv asks for a descriptive User-Agent on programmatic access.
UA = "reading-assistant/0.1 (+https://github.com/; contact: local)"
DOCCLASS_RE = re.compile(rb"\\documentclass")
BEGINDOC_RE = re.compile(rb"\\begin\{document\}")


def _normalise(arxiv_id: str) -> str:
    """Strip an 'arXiv:' prefix and trailing version, if present."""
    m = re.search(r"(\d{4}\.\d{4,5})", arxiv_id)
    return m.group(1) if m else arxiv_id


def _download(arxiv_id: str) -> bytes:
    r = requests.get(EPRINT_URL.format(arxiv_id=arxiv_id),
                     headers={"User-Agent": UA}, timeout=60)
    r.raise_for_status()
    return r.content


def _unpack(blob: bytes, raw: Path) -> None:
    """e-print payloads are usually a gzipped tar; sometimes a single .tex.gz."""
    raw.mkdir(parents=True, exist_ok=True)
    try:
        with tarfile.open(fileobj=io.BytesIO(blob)) as tar:
            tar.extractall(raw, filter="data")
            return
    except tarfile.ReadError:
        pass
    # Not a tar: try a single gzipped tex file.
    try:
        text = gzip.decompress(blob)
    except OSError:
        text = blob  # already plain
    (raw / "main.tex").write_bytes(text)


def _find_root(raw: Path) -> Path:
    """The root .tex is the one that declares the document class + body."""
    texs = sorted(raw.rglob("*.tex"))
    if not texs:
        raise FileNotFoundError(f"no .tex files under {raw}")
    scored = []
    for t in texs:
        b = t.read_bytes()
        score = bool(DOCCLASS_RE.search(b)) * 2 + bool(BEGINDOC_RE.search(b))
        # A file literally named main/ms/paper is a good tie-breaker.
        score += t.stem.lower() in {"main", "ms", "paper", "article"}
        scored.append((score, t))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[0][1]


def fetch(arxiv_id: str, out: Path) -> Path:
    """Download + unpack + flatten. Returns path to flattened .tex."""
    arxiv_id = _normalise(arxiv_id)
    out.mkdir(parents=True, exist_ok=True)
    raw = out / "raw"

    blob = _download(arxiv_id)
    (out / "eprint.tar.gz").write_bytes(blob)
    _unpack(blob, raw)

    root = _find_root(raw)
    flattened = out / "flattened.tex"

    if shutil.which("latexpand"):
        # latexpand resolves \input relative to CWD, so run it inside raw/.
        proc = subprocess.run(
            ["latexpand", str(root.relative_to(raw))],
            cwd=raw, capture_output=True, text=True,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"latexpand failed:\n{proc.stderr}")
        flattened.write_text(proc.stdout)
    else:
        # No latexpand — keep the root file; multi-file \input stays unresolved.
        flattened.write_text(root.read_text(errors="replace"))
        print("WARNING: latexpand not found; using root .tex without flattening")

    return flattened


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("arxiv_id")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    print(fetch(args.arxiv_id, args.out))


if __name__ == "__main__":
    main()
