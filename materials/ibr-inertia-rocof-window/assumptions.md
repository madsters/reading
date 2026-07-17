# Assumptions — Wang et al., online IBR inertia estimation

Load-bearing preconditions the method/results depend on, with locations. Flagged where an
assumption is a genuine limitation on the paper's claims (feeds the review weaknesses).

## Modelling
- **A1 — IBR frequency response ≈ constant (H, D) second-order swing.** The "unified FR
  model" collapses both CS- and VS-type plants to $\Delta P_{FR}=D\,\Delta f + 2H\,r$
  (Eq 3–4). ⚠️ **Major limitation:** real IBR control (VSG, droop, PLL dynamics, filters,
  current limiting, saturation) is not generally a clean constant-(H,D) second order. The
  method *defines* the estimand by this model, so it can only recover an (H,D) that exists
  if the plant actually behaves this way. The hardware "plant" is an inverter **programmed
  with exactly this H/D model** (Table III sets H, D on the emulator) → the validation tests
  the estimator's numerics, not whether real IBRs obey A1.
- **A2 — Clean step active-power disturbance**, single, controllable, with well-defined
  pre/post steady states (Eq 4–6, 12–14). Damping is identified purely from the steady-state
  ratio $\Delta P_{FR,\infty}/\Delta f_\infty$; ongoing grid frequency drift or non-step
  disturbances would corrupt this.
- **A3 — Damping/inertia power are cleanly separable** as $\Delta P_D=D\Delta f$ (algebraic)
  and $\Delta P_H=2Hr$ (Eq 4). Assumes no other fast-frequency-response component (e.g. a
  transient term that is neither pure $\propto\Delta f$ nor pure $\propto r$).

## Statistical / numerical (error analysis)
- **A4 — Zero-mean, mutually independent (white) noise** on P and f (Eq 11), and δp–δr
  correlation neglected (Eq 29). ⚠️ **Concern:** the method applies a first-order LPF first
  (Eq 9), which **colours** the noise; the LS-slope variance $12\sigma^2/(N T_w^2)$ (Eq 33)
  assumes white samples. Coloured noise changes the noise-term scaling and hence $T_w^{*}$.
- **A5 — N ≫ 1** for the asymptotic bias/variance forms (Eq 33); fine for sub-second $T_w$
  at typical $T_s$.
- **A6 — Frequency locally analytic** (Taylor expansion to a few terms, Eq 31); higher-order
  derivative $f^{(3)}$ well-defined and dominant truncation source.

## Scope of validation
- **A7 — Grid inertia $H_g = 6$ s fixed.** When plant $H$ exceeds $H_g$, "significant
  electromagnetic oscillations" appear and degrade estimation (line 477); the authors set
  this aside rather than treat it as a bound on the validated range. ⚠️ State as a limitation.
- **A8 — Single plant, terminal measurement**, 2.85 kW lab scale; no aggregation, no
  multi-plant / PCC-vs-plant measurement-point sensitivity.

## Transferability to my work (`effective_inertia`)
Your finding that measured $H_{\text{eff}}\approx H_{\text{load}}+\text{offset}$ (a fast
frequency-response term beyond stored inertia) bears directly on **A3**: if IBR FR power
carries a fast-response component that isn't purely $\propto r$, the clean $D\Delta f + 2Hr$
split would fold it into the $H$ estimate — a *systematic* bias this paper's error model
(which only treats zero-mean noise, not model-structure bias) would not capture. This is a
substantive scientific angle you're uniquely placed to see — **but it rests on your
unpublished results; weigh how to raise it in review** (see the honesty ledger in
`review.md`).
