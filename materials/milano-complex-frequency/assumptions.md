# Assumptions — Milano complex-frequency tutorial

Preconditions the load-bearing results depend on (the shortlist verified in `verify.md`),
each with where it's stated in `material.md`. Transferability notes relate them to
`profile/current-work.md` (CMLD / effective-inertia work). Only assumptions the deck states
or clearly implies are listed; inferred ones are marked *(inferred)*.

## Complex frequency & its link to current/power (verify.md #1–#3)

- **Fast transmission-line dynamics → quasi-static (algebraic) network:**
  $\bar\imath(t) \approx \bar Y\,\bar v(t)$, with $\bar Y$ the conventional admittance
  matrix (**stated**, line 190, "Assumption"). This is what lets the current and its
  derivative be written algebraically in $\bar v$ and $\bar\eta$.
  - ⚠️ **Transferability:** your frequency-dynamics studies are transient/EMT-style; where
    line/network dynamics are *not* negligible, the algebraic $\bar\imath=\bar Y\bar v$ step
    (and the RoCoP relations built on it) is an approximation, not an identity. Worth stating
    if you borrow the RoCoP decomposition.

- **Park's-vector / analytic-signal representation valid in transient conditions:**
  $\bar v = v_d + j v_q$ (**stated**, line 115). The whole framework is written in complex
  (positive-sequence-like) Park vectors.
  - **Transferability:** compatible with a positive-sequence rig; less so for explicitly
    unbalanced conditions *(inferred — the deck doesn't address unbalance)*.

- **Constant admittance $\bar Y$** for the clean $\bar\imath' = \bar\eta\,\bar\imath$ result
  (verify.md #1; special-case slides ~line 449).
  - ⚠️ **Direct clash with your CMLD work:** your load is deliberately **voltage-dependent**
    (the constant-Z static is only a baseline), so the constant-$\bar Y$ simplification does
    **not** describe the CMLD. The general case ($\bar\chi=\bar\xi-\bar\eta$, time-varying
    admittance $\bar y'=\bar y\bar\chi$, verify.md #3) is the branch relevant to you — the
    device's admittance *changes*, which is exactly the voltage-dependent response you model.

## System model / DAE (context for the device equations)

- **Index-1 DAE:** the algebraic Jacobian $\partial\bfg g/\partial\bfg y$ is non-singular, so
  an implicit function $\bfg y=\phi(\bfg z)$ exists (**stated**, lines ~490–500). Model is
  smooth except at a finite number of discrete events (line ~486).
  - **Transferability:** matches your own DAE framing ($z'=f,\ 0=g$) — compatible.

- **4th-order synchronous-machine example** (Sauer & Pai): the worked machine model assumes
  the standard two-axis transient model — $R_a$, $X'_d$, $X'_q$, transient EMFs $e'_{d,q}$
  (**stated**, eq. `syn`, line ~1276). Higher-order/subtransient effects are outside it (the
  deck's higher-order slide is the one flagged garbled in `flags.md`).

## Transient Slack Capability (§ TSC, lines 1366–1451)

- **Device is a port-Hamiltonian system with a valid storage function $H_k$:** $H_k$ must be
  **positive semi-definite and radially unbounded** (Condition 1, **stated**, line 1442);
  physical examples: rotating-mass KE (SM) or DC-link capacitor energy (IBR), line 1443.
- **Dynamic slack:** to survive a *sustained* $\Delta P$ the source power must be dynamic,
  $u'_{S,k}=f_s(\cdot)$ (Condition 2, **stated**, line 1451).
  - **Transferability:** technology-agnostic — both your induction-motor load (KE storage)
    and your planned `DER_A` (DC-link) satisfy Condition 1; the storage-vs-sustained-delivery
    split is the structural analogue of your stored ($H_{\text{load}}$) vs delivered
    ($H_{\text{eff}}$) distinction (see `context.md`).

## Not stated
- The deck does not state error bounds for the "fast line dynamics" approximation, nor the
  operating conditions under which local synchronization ($\rho\to0,\ \omega\to\omega_r$) is
  guaranteed vs merely observed — treat those as open.
