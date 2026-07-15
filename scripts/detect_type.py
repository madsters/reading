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

# 2401.01234 or 2401.01234v2, optionally prefixed with "arXiv:"
ARXIV_RE = re.compile(r"(?:arxiv[:\s]*)?(\d{4}\.\d{4,5})(v\d+)?", re.IGNORECASE)

# Front-matter cues that mark an academic paper.
PAPER_CUES = ("abstract", "introduction", "references", "et al.", "doi:", "\\begin{abstract}")
DOI_RE = re.compile(r"\b10\.\d{4,9}/\S+\b")


def _pdf_signals(path: Path) -> dict:
    """Inspect a PDF: arXiv id, DOI, page geometry, text density."""
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    meta_blob = " ".join(str(v) for v in (reader.metadata or {}).values())

    # Sample text + geometry from the first few pages.
    sample, landscape_pages, words = [], 0, 0
    for page in reader.pages[:5]:
        try:
            txt = page.extract_text() or ""
        except Exception:
            txt = ""
        sample.append(txt)
        words += len(txt.split())
        box = page.mediabox
        if float(box.width) > float(box.height):
            landscape_pages += 1
    head = ("\n".join(sample) + " " + meta_blob)
    head_lower = head.lower()

    n = max(1, min(5, len(reader.pages)))
    words_per_page = words / n

    return {
        "arxiv": ARXIV_RE.search(head),
        "doi": DOI_RE.search(head),
        "landscape_ratio": landscape_pages / n,
        "words_per_page": words_per_page,
        "paper_cues": sum(cue in head_lower for cue in PAPER_CUES),
    }


def detect(path: Path) -> dict:
    """Return {profile, confidence, signals, arxiv_id?}."""
    ext = path.suffix.lower()

    if ext == ".pptx":
        return {"profile": "slides", "confidence": "high",
                "signals": ["extension .pptx"]}

    # arXiv id in the filename is a strong, cheap signal.
    m = ARXIV_RE.search(path.name)
    if m:
        return {"profile": "arxiv-paper", "confidence": "high",
                "signals": [f"arxiv id in filename: {m.group(1)}"],
                "arxiv_id": m.group(1)}

    if ext == ".pdf":
        try:
            s = _pdf_signals(path)
        except Exception as e:  # unreadable PDF — fall back to a low-confidence guess
            return {"profile": "journal-paper", "confidence": "low",
                    "signals": [f"pdf inspection failed: {e}"]}

        if s["arxiv"]:
            aid = s["arxiv"].group(1)
            return {"profile": "arxiv-paper", "confidence": "high",
                    "signals": [f"arxiv id in content: {aid}"], "arxiv_id": aid}

        # Landscape + sparse text = slide deck exported to PDF.
        if s["landscape_ratio"] >= 0.6 and s["words_per_page"] < 120:
            return {"profile": "slides", "confidence": "medium",
                    "signals": [f"landscape pages {s['landscape_ratio']:.0%}",
                                f"~{s['words_per_page']:.0f} words/page"]}

        if s["doi"] or s["paper_cues"] >= 2:
            sig = []
            if s["doi"]:
                sig.append(f"doi: {s['doi'].group(0)}")
            if s["paper_cues"]:
                sig.append(f"{s['paper_cues']} academic front-matter cues")
            return {"profile": "journal-paper", "confidence": "medium", "signals": sig}

        return {"profile": "document", "confidence": "low",
                "signals": ["pdf with no paper/slide signals; default document"]}

    if ext in {".docx", ".doc", ".md", ".txt", ".rtf", ".odt"}:
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
