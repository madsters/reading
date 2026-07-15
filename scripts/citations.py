#!/usr/bin/env python3
"""Build context for a material: citation graph when possible, web search otherwise.

Two branches feeding one context payload:

  * Identity branch (papers): hit the free Semantic Scholar API for references
    (what it builds on) and citations (who cites it). No key required.
  * Fallback branch (slides / documents / orphan papers): no DOI/arXiv id, so
    web-search instead — seeded by the author / research-group / source hints the
    user optionally supplied at run start. Those hints let the search surface the
    group's related publications and locate the material in their body of work.

Honesty: if neither branch yields usable context, say so — the caller records
"context could not be established" in flags.md rather than inventing lineage.

    python citations.py --arxiv 2401.01234 --out materials/<slug>
    python citations.py --hints "Author, Group, Course title" --out materials/<slug>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

S2_BASE = "https://api.semanticscholar.org/graph/v1"


def by_identity(paper_id: str) -> dict:
    """Semantic Scholar references + citations.

    Sketch: GET {S2_BASE}/paper/{paper_id}/references and /citations with
    fields=title,year,authors,abstract; paper_id may be 'arXiv:<id>' or a DOI.
    Return {references: [...], citations: [...]}.
    """
    # TODO: requests.get with polite rate limiting; paginate.
    raise NotImplementedError("citations.by_identity: wire up Semantic Scholar")


def by_search(hints: str) -> dict:
    """Web-search fallback seeded by author/group/source hints.

    Sketch: run queries built from the hints ("<group> <topic>", author name,
    course title) against a web-search backend; collect candidate related works
    and origin pages. Return {related: [...], origin: [...], queries: [...]}.
    The LLM stage turns this into context.md; this script only gathers.
    """
    # TODO: wire to the web-search backend available at build time.
    raise NotImplementedError("citations.by_search: wire up web-search fallback")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--arxiv")
    ap.add_argument("--doi")
    ap.add_argument("--hints", help="author / group / source, comma-separated")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    if args.arxiv or args.doi:
        payload = by_identity(f"arXiv:{args.arxiv}" if args.arxiv else args.doi)
    elif args.hints:
        payload = by_search(args.hints)
    else:
        payload = {"context": None, "reason": "no identity and no hints provided"}

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "context.json").write_text(json.dumps(payload, indent=2))
    print(json.dumps({"written": str(args.out / "context.json")}, indent=2))


if __name__ == "__main__":
    main()
