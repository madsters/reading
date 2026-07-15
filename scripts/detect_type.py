#!/usr/bin/env python3
"""Route a dropped file to an ingestion profile.

Profiles: arxiv-paper | journal-paper | slides | document

Detection is best-effort and always overridable by the run-start prompt.
Returns the profile plus a confidence and the signals that drove the guess,
so the caller can show the user *why* before asking them to confirm.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ARXIV_RE = re.compile(r"\b\d{4}\.\d{4,5}(v\d+)?\b")  # e.g. 2401.01234v2


def detect(path: Path) -> dict:
    """Return {profile, confidence, signals, arxiv_id?}.

    Sketch of the decision waterfall:
      1. .pptx                       -> slides (high)
      2. arXiv id in name/text/meta  -> arxiv-paper (high), capture id
      3. PDF whose page geometry is landscape/slide-shaped, few words/page
                                     -> slides (medium)
      4. PDF with DOI or academic front-matter (abstract/references)
                                     -> journal-paper (medium)
      5. .docx / other PDF           -> document (low)
    """
    ext = path.suffix.lower()
    signals: list[str] = []

    if ext == ".pptx":
        return {"profile": "slides", "confidence": "high",
                "signals": ["extension .pptx"]}

    # arXiv id: check filename first, then (TODO) PDF text + XMP metadata.
    m = ARXIV_RE.search(path.name)
    if m:
        return {"profile": "arxiv-paper", "confidence": "high",
                "signals": [f"arxiv id in filename: {m.group(0)}"],
                "arxiv_id": m.group(0)}

    if ext == ".pdf":
        # TODO: open with pypdf; inspect page dims (slide aspect ratio),
        # words-per-page, presence of "References"/"DOI"/"Abstract".
        signals.append("pdf: geometry/front-matter inspection TODO")
        return {"profile": "journal-paper", "confidence": "low", "signals": signals}

    if ext in {".docx", ".doc", ".md", ".txt"}:
        return {"profile": "document", "confidence": "medium",
                "signals": [f"extension {ext}"]}

    return {"profile": "document", "confidence": "low",
            "signals": [f"unrecognised extension {ext}; default document"]}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", type=Path)
    args = ap.parse_args()
    print(json.dumps(detect(args.path), indent=2))


if __name__ == "__main__":
    main()
