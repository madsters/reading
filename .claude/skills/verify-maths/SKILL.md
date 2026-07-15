---
name: verify-maths
description: Verify load-bearing equations symbolically and numerically with sympy — re-derivation, dimensional consistency, index balance, and limiting cases — and record honest pass/discrepancy results to verify.md. Content-triggered: runs whenever there is maths, paper or tutorial. Use when the user flags equations to trust-check.
---

# Verify maths

The trust layer. Stage 4 of Phase A. Runs whenever there's maths — not paper-specific.

## Pick the load-bearing equations
Runs by default after contextualise. **Propose** the load-bearing equations yourself (main
results, anything a later argument leans on) and confirm the shortlist with the user before
checking. Don't try to verify everything — verify what carries weight.

## Build the check spec
Write `materials/<slug>/checks.json` as a list of steps, each:
`{eq_ref, lhs, rhs, substitutions, checks: [...]}` where checks ⊆
`rederive | dimensions | indices | limits`. Pull symbols/roles from `notation.md` so
sympy interprets them correctly (this is where the bold/vector work pays off).

## Run
`scripts/verify.py --spec materials/<slug>/checks.json --out materials/<slug>`

## Write verify.md
Turn `verify.json` into an honest ledger: for each equation, `pass` /
`discrepancy(detail)` / `not-applicable`. Be specific — e.g. "re-derived eq. 14:
factor-of-2 discrepancy in the second term". A discrepancy is a finding, not a failure —
surface it clearly.
