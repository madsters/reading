#!/usr/bin/env python3
"""Build context for a material: citation graph when possible, web search otherwise.

Two branches feeding one context payload:

  * Identity branch (papers): hit the free Semantic Scholar API for references
    (what it builds on) and citations (who cites it). No key required.
  * Fallback branch (slides / documents / orphan papers): no DOI/arXiv id, so
    web-search instead — seeded by the author / research-group / source hints the
    user optionally supplied at run start.

Honesty: if neither branch yields usable context, say so — the caller records
"context could not be established" in flags.md rather than inventing lineage.

    python citations.py --arxiv 2401.01234 --out materials/<slug>
    python citations.py --hints "Author, Group, Course title" --out materials/<slug>
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import requests

S2_BASE = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "title,year,authors,abstract,venue,externalIds"
UA = "reading-assistant/0.1"


def _s2_edges(paper_id: str, edge: str) -> list[dict]:
    """Page through /paper/{id}/{references|citations}. `edge` in {references, citations}."""
    key = "citedPaper" if edge == "references" else "citingPaper"
    out, offset, limit = [], 0, 100
    while True:
        r = requests.get(
            f"{S2_BASE}/paper/{paper_id}/{edge}",
            params={"fields": S2_FIELDS, "offset": offset, "limit": limit},
            headers={"User-Agent": UA}, timeout=30,
        )
        if r.status_code == 429:  # rate limited — back off and retry
            time.sleep(3)
            continue
        r.raise_for_status()
        data = r.json()
        for item in data.get("data", []):
            paper = item.get(key)
            if paper:
                out.append(paper)
        offset = data.get("next")
        if not offset:
            break
    return out


def by_identity(paper_id: str) -> dict:
    """Semantic Scholar references + citations. paper_id like 'arXiv:2401.01234' or a DOI."""
    return {
        "source": "semantic-scholar",
        "paper_id": paper_id,
        "references": _s2_edges(paper_id, "references"),
        "citations": _s2_edges(paper_id, "citations"),
    }


def by_search(hints: str, max_results: int = 8) -> dict:
    """Web-search fallback seeded by author/group/source hints."""
    from duckduckgo_search import DDGS

    terms = [h.strip() for h in hints.split(",") if h.strip()]
    queries = terms + [f"{terms[0]} publications" if terms else hints,
                       f"{' '.join(terms)} related work"]
    seen, related, used = set(), [], []
    with DDGS() as ddgs:
        for q in queries:
            used.append(q)
            for hit in ddgs.text(q, max_results=max_results):
                url = hit.get("href")
                if url and url not in seen:
                    seen.add(url)
                    related.append({"title": hit.get("title"), "url": url,
                                    "snippet": hit.get("body")})
    return {"source": "web-search", "hints": terms, "queries": used,
            "related": related}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--arxiv")
    ap.add_argument("--doi")
    ap.add_argument("--hints", help="author / group / source, comma-separated")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    try:
        if args.arxiv:
            payload = by_identity(f"arXiv:{args.arxiv}")
        elif args.doi:
            payload = by_identity(f"DOI:{args.doi}")
        elif args.hints:
            payload = by_search(args.hints)
        else:
            payload = {"source": None, "context": None,
                       "reason": "no identity and no hints provided"}
    except Exception as e:
        payload = {"source": "error", "context": None, "reason": str(e)}

    args.out.mkdir(parents=True, exist_ok=True)
    dest = args.out / "context.json"
    dest.write_text(json.dumps(payload, indent=2))
    print(json.dumps({"written": str(dest), "source": payload.get("source")}, indent=2))


if __name__ == "__main__":
    main()
