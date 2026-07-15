#!/usr/bin/env python3
"""Extract a .pptx deck into markdown: per-slide text, speaker notes, and images.

Path 2 of the waterfall. Speaker notes are first-class here — for a tutorial they
often carry the explanation that the slide only gestures at, so they're the best
comprehension signal in the whole deck. Each slide is also rendered to an image so
diagrams and hand-drawn maths survive for the Q&A phase.

    python extract_slides.py deck.pptx --out materials/<slug>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def extract(pptx: Path, out: Path) -> dict:
    """Return {markdown_path, images_dir, n_slides}.

    Sketch:
      1. python-pptx: iterate slides. For each, pull title + body text (walk
         shape.text_frame) and slide.notes_slide.notes_text_frame.text.
      2. Emit material.md as one section per slide:
             ## Slide {n}: {title}
             {body text}
             **Notes:** {speaker notes}
             ![slide {n}](source/slides/slide-{n}.png)
      3. Render slide images: python-pptx can't rasterise, so shell out to a
         headless converter (LibreOffice --headless --convert-to, or unoconv)
         pptx -> pdf, then pdf pages -> png. Write to out/source/slides/.
    """
    out.mkdir(parents=True, exist_ok=True)
    # TODO: python-pptx text + notes extraction -> out/material.md
    # TODO: headless render slides -> out/source/slides/slide-*.png
    raise NotImplementedError("extract_slides: wire up python-pptx + headless render")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pptx", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    print(json.dumps(extract(args.pptx, args.out), indent=2))


if __name__ == "__main__":
    main()
