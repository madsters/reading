---
name: contextualise
description: Build context.md for a material — what it builds on, how it was received, and where it sits in its field. Uses the Semantic Scholar citation graph for papers with an identity, and a web-search fallback (seeded by author/group/source hints) for slides and documents. Use after ingest, before or alongside verification.
---

# Contextualise

Situate the material. Stage 3 of Phase A. Two branches, one honest output.

## Choose the branch
- **Has an identity** (arXiv id / DOI): run
  `scripts/citations.py --arxiv <id> --out materials/<slug>` (or `--doi`). This pulls
  references (what it builds on) and citations (who cites it).
- **No identity** (slides, documents, orphan papers): read
  `materials/<slug>/context-hints.txt` and run
  `scripts/citations.py --hints "<author, group, source>" --out materials/<slug>`. The
  hints let the web search surface the group's related publications and the material's
  origin (course, talk, report series).

## Write context.md
From `context.json`, write `context.md`: the problem lineage, the core contribution, how
later work received it (papers) or where it fits in the source's body of work (fallback).

Then add a **"relevance to my work"** section — and make it *specific*. Read
`profile/current-work.md` and tie the material to the reader's **named active threads and
open questions**, not to the field in general. Good relevance says "this connects to your
`effective_inertia` study's delivered-vs-stored question because …"; bad relevance says
"this is relevant to power systems." Where a concept in the material maps onto a quantity
or method the reader is using, say so and how. If nothing genuinely connects, say that
plainly rather than forcing it.

## Honesty
If neither branch yields usable context, do **not** invent lineage. Write "context could
not be established" into `flags.md` and keep `context.md` minimal.
