---
name: resolve-sources
description: When a converted material has flagged low-confidence equations AND its references include an arXiv source paper, automatically fetch that paper's lossless LaTeX source and reconcile the flagged equations against it — upgrading fidelity and clearing flags. Runs by default after contextualise when both conditions hold.
---

# Resolve sources

Self-heal flagged maths using the authoritative source. A converted deck/paper may have
mis-recognised equations (see `flags.md`); if the material *cites* a paper that is on
arXiv, that paper's original LaTeX is ground truth — so fetch it and reconcile, rather
than leaving the reader to cross-check by hand.

## When to run (automatic)
Runs by default after `contextualise`. Trigger **iff both** hold:
1. `flags.md` (or `flags.json`) contains formula / low-confidence / possibly-misread items, **and**
2. `context.json` lists a core reference with an `arxiv` id.

If either fails, skip and note "no resolvable source" — never fetch for a material whose
maths converted cleanly (e.g. the near-lossless arXiv-source path).

## Steps
1. **Pick the source paper(s).** The core reference whose notation/equations the flagged
   content derives from — usually the foundational paper (the one that defines the symbols
   the deck uses). Take arXiv ids from `context.json` → `core_references`.
2. **Fetch lossless source:**
   `scripts/fetch_arxiv_source.py <arxivid> --out materials/<slug>/refs/<arxivid>`.
3. **Reconcile.** For each flagged equation, find its authoritative form in the flattened
   `.tex` and compare. Where they differ, correct `material.md` (optionally keep the
   converter's version inline as a struck note) and mark the flag **resolved** in
   `flags.md`, citing the source (`arXiv:<id>`, eq/section number).
4. **Leave the rest open.** If the source doesn't cover a flagged item (e.g. a slide-only
   equation not in the paper), keep the flag open and say so.

## Honesty
Mark a flag *resolved* only when the source actually confirms or corrects it. Always record
the source of truth for each correction so the reader can trace it.
