<!-- Structured peer-review template. Fill every section from the corpus; cite locations
     (slide/section/eq/line in material.md). Keep VERIFIED issues separate from CONCERNS.
     The recommendation is advisory — the reviewer decides. -->
# Review — {{TITLE}}

- **Venue:** {{VENUE}}  ·  **Recommendation:** {{accept | minor revision | major revision | reject}}  ·  **Reviewer confidence:** {{low | medium | high}}

## Summary
{{2–4 sentences, in your own words: the problem, the approach, and the claimed contribution.
Shows the authors you understood the paper.}}

## Significance & novelty
{{Is the problem important? Is each claimed contribution genuinely new vs the cited + known
prior art (from context.md)? Note any missing related work or overclaimed novelty.}}

## Claims ↔ evidence
{{The spine. One row per claimed contribution/central claim.}}

| # | Claim (location) | Type | Evidence offered | Verdict |
|---|---|---|---|---|
| C1 | {{…}} (§/eq/p) | theory / empirical | {{paper's own evidence + our findings}} | supported / partial / unsupported |

## Strengths
- {{…}}

## Weaknesses
### Major
- **[M1]** {{issue}} — {{location}} — {{why it matters}} — _{{verified | concern}}_

### Minor
- **[m1]** {{…}} — {{location}}

## Soundness
{{From verify-maths (verify.md): what was re-derived/checked, pass vs discrepancy, and any
unjustified or hand-waved steps. Distinguish confirmed errors from things to double-check.}}

## Assumptions & scope
{{From assumptions.md: are assumptions stated and reasonable? Are results overclaimed beyond
what the assumptions/scope support?}}

## Reproducibility & methodology
{{Do the experiments/simulations support the claims? Fair baselines, adequate evaluation,
statistical validity, ablations. Is code/data available and is there enough detail to
reproduce? For theory: are proofs complete?}}

## Clarity & presentation
{{Structure, notation consistency, figure/table quality, anything that impeded understanding.}}

## Questions to the authors
1. {{…}}

## Detailed comments (line-referenced)
- {{§/eq/p/line}}: {{…}}

## Recommendation
**{{accept | minor revision | major revision | reject}}** — reviewer confidence **{{…}}**.
{{One paragraph tying the recommendation to the major weaknesses and the claims↔evidence
verdicts. Advisory only — the reviewer makes the call.}}

## Honesty ledger
- **Verified issues** (grounded — e.g. maths discrepancies from verify.md): {{…}}
- **Concerns to check** (not verified; reviewer judgement needed): {{…}}
- **Reviewer expertise / conflicts** (from current-work.md): {{confidence basis; any COI}}
