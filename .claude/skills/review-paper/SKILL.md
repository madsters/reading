---
name: review-paper
description: Run the peer-review pipeline on a paper — assess correctness, novelty, claims-vs-evidence, methodology/reproducibility, assumptions and clarity, then draft a structured venue-style review with a recommendation and reviewer confidence. Use when the reader wants to review/referee a paper (not just comprehend it). Distinct from the built-in PR "review" skill.
---

# Review a paper

The second pipeline. Where the comprehend pipeline helps the reader *understand* a paper,
this one helps them *judge* it and draft a referee report. **Review always runs the full
comprehend pipeline first** — you cannot fairly referee what you haven't understood,
verified, and pinned the assumptions of — then adds the critical-assessment stages on top.

**Stance:** balanced peer review for a venue — fair, evidence-based, strengths *and*
weaknesses, ending in a recommendation + reviewer confidence. **Deliverable:**
`materials/<slug>/review.md` (fill `templates/review.md`).

## Pipeline
0. **Run the full comprehend pipeline first** — `ingest` → `contextualise` →
   `resolve-sources` → `verify-maths` → `assumptions` → `one-pager`. The review stages below
   build directly on those artifacts (`verify.md`, `assumptions.md`, `context.md`). Do not
   start the review until comprehend is complete.
1. **Ingest + notation** — from the comprehend run: the high-fidelity corpus. You can't
   fairly review what you can't read cleanly.
2. **Claims & contributions ledger** — extract what the paper *explicitly claims* to
   contribute (theoretical and empirical) and its central claims; locate each. This is the
   spine of the review.
3. **Novelty & positioning** — run `contextualise`, then judge critically: is each claimed
   contribution actually new vs the cited *and* known prior art? Missing citations?
   Overclaimed novelty?
4. **Soundness** — run `verify-maths` on the load-bearing results (re-derive, dimensions,
   limits). Also check internal consistency (claims vs stated results, notation, units).
   Separate confirmed errors from steps to double-check.
5. **Assumptions & scope** — run `assumptions`, then judge: are they stated and reasonable,
   and are results overclaimed beyond what they support?
6. **Evidence & methodology** — do the experiments/simulations actually support the claims?
   Fair baselines, adequate evaluation, statistical validity, ablations; reproducibility
   (code/data availability, enough detail). For theory: are proofs complete?
7. **Claims ↔ evidence map** — for each claim from (2): supported / partial / unsupported,
   citing the paper's own evidence and the findings from 4–6.
8. **Clarity & presentation** — structure, notation consistency, figures/tables.
9. **Write the review** — fill `templates/review.md` → `materials/<slug>/review.md`.

## Honesty (non-negotiable — a review can do real harm if sloppy)
- **Ground every criticism** in a location (§/eq/p/line in `material.md`) and a reason.
  Never invent a flaw to look thorough.
- **Separate verified issues from concerns.** A maths discrepancy from `verify.md` is
  *verified*; "the baseline may be unfair" is a *concern to check*. The review's honesty
  ledger must keep these apart.
- **The recommendation is advisory.** Present the evidence and a suggested verdict with
  reasoning; the reviewer makes the call.
- **Reviewer confidence & COI:** read `profile/current-work.md` to state the reviewer's
  expertise basis for confidence, and flag any conflict of interest (e.g. the paper is by a
  group the reader collaborates with or competes with directly).

## Relationship to the comprehend pipeline
Review is a **superset**: it always runs the entire comprehend pipeline first, then adds the
review-only stages (claims ledger, evidence/methodology, claims↔evidence, clarity) and the
`review.md` deliverable. So selecting "review" at drop time yields both the comprehend corpus
*and* the referee report — there is no separate "both" option.
