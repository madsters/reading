---
name: assumptions
description: Collect the preconditions each load-bearing result depends on into assumptions.md — what must hold for it to be valid — and flag where those assumptions clash with the reader's own setting (so it's obvious when a method won't transfer). Runs by default after verify-maths.
---

# Assumptions ledger

Gather the scattered preconditions a material's key results rely on into one place, so it's
obvious **when a result won't transfer** to the reader's setting. Stage 6 of Phase A; runs
by default after `verify-maths`. Lighter for a tutorial than a dense paper, but still worth
doing.

## Build the ledger
For each load-bearing result (reuse the shortlist from `verify-maths`/`verify.md`), list the
assumptions it needs to hold. Draw them from the corpus and `notation.md`. Typical sources:
stated hypotheses, "we assume / consider / for simplicity" phrasing, the modelling choices
behind a definition, regularity/limit conditions, and special cases the result is restricted
to.

Write `assumptions.md`: group by result, one line per assumption, each with the location it
comes from (slide/section/equation/line in `material.md`).

## Ground & attribute (same discipline as contextualise)
- Only list assumptions the material **states or clearly implies** — cite where. Mark
  anything you infer as *(inferred)*, don't present it as the author's.
- Don't invent preconditions to look thorough. If a result's assumptions aren't stated,
  say "not stated in the material".

## Transferability to the reader's work
Read `profile/current-work.md`. Where an assumption **clashes with the reader's setting**,
flag it explicitly — e.g. "assumes a constant/linear X; your setting has voltage-dependent
X, so this result may not carry over as-is". This is the payoff: the ledger tells the reader
which results they can borrow and which need rework before they apply.

## Output
`materials/<slug>/assumptions.md`. Phase B reads it (see `CLAUDE.md`) before leaning on any
result.
