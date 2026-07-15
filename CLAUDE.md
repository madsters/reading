# Reading Assistant — project brief

This repo processes dense material (papers, tutorial slide decks, technical documents)
into a high-fidelity corpus, then helps you comprehend it. There are two phases.

## Phase A — Build (in Claude Code)
When a file lands in `inbox/`, run the pipeline via the skills in `.claude/skills/`. By
default every material runs `ingest` → `contextualise` → `verify-maths` → `one-pager`;
`expand-derivation` is on-demand (invoked per question, not up front). Each material
becomes a folder under `materials/<slug>/`. See `reading-assistant-plan.md` for the full
design.

## Phase B — Comprehend (this Claude Project / cowork)
When answering questions about a material, you MUST:

1. **Read the corpus first.** Treat `materials/<slug>/` as ground truth — read
   `material.md`, `notation.md`, `context.md`, `verify.md`, and `assumptions.md` before
   answering. Never answer from memory of the general topic when the corpus is present.
2. **Cite locations.** Every claim references a slide number / section / equation in
   `material.md`.
3. **Render maths.** Render answers as inline HTML/MathJax artifacts — never dump raw
   LaTeX or unrendered maths as terminal text.
4. **Adapt to the reader.** Read `profile/maths-background.md`. If `learning_mode: on`,
   pitch to each concept's mastery level (`unseen → seen → followed → applied →
   intuitive`): teach `unseen`/`seen` from basics; for `followed`, **don't re-derive the
   definition — build intuition, worked examples, and connections to the reader's own
   work** (respect each concept's `target`); treat `applied`/`intuitive` as recall or
   building blocks. Warn about prerequisite gaps before diving into a result. Update the
   ledger conversationally when the user demonstrates or declares understanding (move up
   the ladder, dated) — e.g. `followed → intuitive` once they can relate it to their work.
5. **Trust the verification.** If `verify.md` flags a discrepancy in an equation, say so
   when that equation comes up — don't smooth over it.
6. **Relate to their work.** Where relevant, connect the material to the user's existing
   notes and active projects (see the "relevance" sections in `context.md`).

## Honesty
`flags.md` records what couldn't be read or contextualised. Respect it: don't present
flagged-uncertain content as settled, and don't invent context that couldn't be found.
