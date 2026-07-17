# Review — Online Inertia Estimation for IBR Plants: Error Analysis and RoCoF Window Length Selection

- **Venue:** IEEE Transactions on Sustainable Energy (initial submission, TSTE-00929-2026)  ·  **Recommendation:** **major revision**  ·  **Reviewer confidence:** **high**

## Summary
The paper proposes an online, per-plant inertia estimation method for inverter-based
resource (IBR) plants. A unified second-order frequency-response (FR) model $\Delta P_{FR}=
D\Delta f + 2Hr$ is posited for both current- and voltage-source plants; under a controllable
small step active-power disturbance, damping $D$ is identified from the steady-state response
and the inertia power $\Delta P_H$ is then isolated to estimate $H$ from RoCoF. The core
contribution is an analytical error-propagation model (Section IV) that quantifies how
sampling noise and the RoCoF window length $T_w$ affect accuracy, yielding a bias/noise
trade-off and a fifth-root optimal-window expression, and hence a theoretical guideline
($T_w\approx250$–$300$ ms). A full-power hardware platform validates the scheme across six
inertia levels and four disturbance amplitudes.

## Significance & novelty
The problem is timely and practically important: per-plant inertia (not just system-level)
is what compliance verification and inertia allocation actually need. The genuine novelty is
the **analytical window-length selection** — replacing the inconsistent empirical grid-code
windows (Table I) with a derived optimum. The per-plant active-disturbance framing and the
D/H power decomposition that needs no internal control parameters are useful and, to my
knowledge, a reasonable advance over the passive/system-level and event-driven methods
surveyed in §I.

## Claims ↔ evidence

| # | Claim (location) | Type | Evidence offered | Verdict |
|---|---|---|---|---|
| C1 | Unified FR model captures both CS- and VS-type IBR plants (Eq 1–3) | theory | algebraic per-unit normalisation | **partial** — unification shown algebraically, but validity for *real* IBR control not tested (see M1) |
| C2 | Method estimates per-plant H (and D) from terminal measurements under a step disturbance (Eq 4–22) | method+expt | hardware, 6 H-levels; ~5% H error, ~1% D error | **supported on the emulator** (caveat M1) |
| C3 | Analytical error model → bias∝$T_w^2$, noise∝$1/T_w^3$, fifth-root optimum (Eq 31–37) | theory | derivation | **structurally sound** (verified) — coefficient + noise-model caveats M2, M3 |
| C4 | $T_w=250$–$300$ ms is a robust choice (flat optimum) | theory+expt | Eq 37 + Figs 12,16 | **supported** — experiment shows the U-shaped error and plateau |

## Strengths
- Addresses a real gap (per-plant inertia; theoretical vs empirical window selection).
- The error-analysis structure is **correct**: I re-derived the fifth-root optimum from a
  competing $a T_w^2 + b/T_w^3$ error and confirmed the LS-slope noise variance scales as
  $1/T_w^3$ (see `verify.md`). The "flat plateau → don't over-optimise $T_w$" argument is a
  nice, genuinely useful practical insight.
- Hardware (not simulation-only) validation across a sensible H and disturbance range.
- Damping/inertia decomposition without internal control parameters is practical.

## Weaknesses
### Major
- **[M1] Validation circularity / generality of the (H,D) model.** The method *defines* the
  estimand through the unified model $\Delta P_{FR}=D\Delta f+2Hr$ (Eq 3–4), and the hardware
  "IBR plant" is an inverter **programmed with exactly that H/D model** (Table III sets H, D
  on the emulator). So the experiments demonstrate the estimator's numerical accuracy, not
  that *real* IBR plants — with VSG/droop/PLL dynamics, filters, current limiting — actually
  present a constant-(H,D) second-order FR. The paper's central applicability claim needs
  either (a) validation against a plant whose control is *not* the assumed model, or (b) an
  explicit argument/bound for when the constant-(H,D) reduction is valid. As written, this is
  the main barrier to the "works for IBR plants" claim.
- **[M2] Reproducibility of the error-model constants.** The derivation $ (31)\to(33)\to
  (36)\to(37)$ compresses several steps. My independent continuum least-squares derivation
  gives a truncation-bias coefficient $f^{(3)}T_w^2/40$, whereas Eq (33) appears to use $/80$
  (factor ~2), and I could not reproduce the exact "720" constant in Eq (37) from the given
  equations. Please show the intermediate algebra (Σ over $\tau_i$: definitions, $N$ vs $N-1$,
  $T_w=NT_s$ vs $(N-1)T_s$). *Verified* that this only shifts $T_w^*$ by $\sim2^{1/5}\approx
  15\%$ given the flat optimum, so it does not sink the result — but the constants must be
  checkable. _(reviewer note: coefficient read off the rendered proof; confirm against source.)_
- **[M3] White-noise assumption under low-pass filtering.** The noise-term variance
  $12\sigma^2/(NT_w^2)$ (Eq 33) assumes independent samples, but the pipeline applies a
  first-order LPF (Eq 9) *before* differentiation, which colours the noise. Correlated noise
  changes the noise-term scaling and therefore the optimal $T_w$. The interaction of the LPF
  time constant $\tau\in[0.05,0.2]$ with $T_w$ should be modelled or at least discussed;
  right now $\tau$ appears in preprocessing but not in the error model.

### Minor
- **[m1]** When plant $H>H_g$ (=6 s), "significant electromagnetic oscillations" degrade
  estimation (¶ near line 477) — this is dismissed rather than stated as a validated-range
  limitation. Please frame it as a bound and, ideally, show the error growth.
- **[m2]** Only single, clean step disturbances are tested. Real operation has ongoing
  frequency variation and non-step events; the steady-state damping identification (Eq 6) is
  sensitive to this. Comment on robustness.
- **[m3]** Measurement point (plant terminal) and single-plant scope: does the method hold at
  the PCC, or under aggregation of multiple units?
- **[m4]** $A3$: the FR power is assumed to split cleanly into $D\Delta f$ and $2Hr$ with no
  other component — see Question Q3.
- **[m5]** Presentation: Tables II–III are hard to parse (formatting); several symbol
  definitions ($K_m$, grid-emulator PI values) are truncated in the proof.

## Soundness
Verified the load-bearing theory (`verify.md`): the fifth-root optimum and the $1/T_w^3$
noise scaling are correct; the $T_w^2$ truncation-bias scaling is correct. Open items: the
numeric coefficients (M2) and the white-noise assumption (M3). No outright error found in the
structure of the analysis.

## Assumptions & scope
See `assumptions.md`. The results are conditional on: a constant-(H,D) plant FR (A1, the big
one), a clean single step disturbance (A2), a clean D/H power split (A3), and white post-LPF
noise (A4). These are reasonable for a first analytical treatment but bound the claims more
tightly than the abstract implies.

## Reproducibility & methodology
Hardware setup and parameters are given (Tables II–III), which is good. Gaps: no statement of
code/data availability; the noise variances $\sigma_P^2,\sigma_f^2$ used in the error model
are not reported, so the *quantitative* $T_w^*$ prediction can't be reproduced and compared
to the empirical 250–300 ms optimum; the emulator-as-plant issue (M1) limits external
validity.

## Questions to the authors
1. **(M1)** Can you validate against an IBR plant whose control is *not* the assumed
   constant-(H,D) model (e.g. a droop/VSG controller with realistic limits), or bound the
   error when the true FR departs from Eq (3)?
2. **(M2)** Please provide the explicit $(31)\to(37)$ algebra and confirm the truncation-bias
   constant and the "720" in Eq (37).
3. **(M3/Q3)** Does the $D\Delta f + 2Hr$ decomposition risk absorbing a *fast
   frequency-response* component (neither purely damping nor purely inertial) into the $H$
   estimate? How would such a term appear in your error model, which currently treats only
   zero-mean noise, not model-structure bias?
4. **(M3)** How does the LPF ($\tau$) interact with $T_w$ in the noise term — is the white-noise
   variance in Eq (33) still valid after filtering?

## Detailed comments (line-referenced)
- Eq (4): state explicitly that $r=\mathrm{d}\Delta f/\mathrm{d}t$ uses the sign convention
  $\Delta f=f_N-f$ (sign of the $2Hr$ term matters for the decomposition).
- Table I: give the specific clauses/refs for each region's window; "IEEE >100 ms" is vague.
- §V: report $\sigma_P,\sigma_f$ and the predicted vs measured $T_w^*$ per H so the theory is
  quantitatively (not just qualitatively) validated.

## Recommendation
**Major revision** — reviewer confidence **high**. The core theoretical contribution (the
window-length error analysis and fifth-root optimum) is sound and genuinely useful, and the
per-plant estimation framing is a real advance. But the central applicability claim rests on
a plant model that the hardware validation assumes rather than tests (M1), the error model
omits the effect of its own preprocessing filter (M3), and the derivation constants are not
currently reproducible (M2). These are addressable in revision without new fundamental work,
and the paper would be a solid contribution once they are. *Advisory — the editor/reviewer
decides.*

## Honesty ledger
- **Verified issues** (grounded): fifth-root optimum and $1/T_w^3$ noise scaling are correct
  (sympy, `verify.md`); truncation-bias coefficient shows a probable factor-of-2 vs my
  continuum derivation (M2) — flagged as *to-confirm*, not asserted error, since read off the
  rendered proof.
- **Concerns to check** (reviewer judgement, not verified): M1 (validation circularity — an
  inference from Table III + method structure, strong but the reader should confirm how the
  emulator is programmed), M3 (coloured-noise effect), and the minors.
- **Reviewer expertise / conflict of interest:** high confidence — this is the reviewer's
  active research area (RoCoF-window inertia estimation; see `profile/current-work.md`,
  `effective_inertia`). **No institutional COI** (authors at Xi'an Jiaotong; not
  collaborators) — confirm. **Prior-work caution:** the reviewer's *unpublished* results
  suggest a fast-frequency-response term beyond stored inertia (the $H_{\text{eff}}\approx
  H_{\text{load}}+\text{offset}$ finding), which motivates Q3/M-A3. This is a legitimate
  modelling question but must be raised **as a general question**, not as a claim backed by
  unpublished data. Do not let a divergent private prior harden into an unfair demand.
