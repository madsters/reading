---
name: one-pager
description: Draft and compile a single-page PDF summary from a processed material, using the profile-aware LaTeX template (paper layout vs tutorial/document digest). Enforces the one-page guarantee by compile-and-check. Use when the corpus is built and the user wants the polished deliverable.
---

# One-pager

Produce the polished single-page PDF. Stage 7 of Phase A. Both a deliverable in its own
right and a forcing function for a tight summary.

## Pick the template
- Paper → `templates/onepager_paper.tex` (problem / method / key equations / results /
  limitations / relevance).
- Slides or document → `templates/onepager_digest.tex` (key ideas / concept map / worked
  takeaways / where it fits / relevance).

Copy the template to `materials/<slug>/onepager.tex`.

## Draft to the limits
Fill the template from `material.md`, `context.md`, `verify.md`, and `assumptions.md`.
Respect the template's per-box character/length limits — the constraint is the point.
Include the load-bearing equations verbatim (source-first fidelity), and note any
verification discrepancies rather than hiding them.

## Compile + assert one page
`scripts/build_onepager.py materials/<slug>/onepager.tex --out materials/<slug>/onepager.pdf`

If it exits non-zero for overflow, **trim and recompile** — do not relax the one-page
rule. Repeat until it reports `ok: ... (1 page)`.
