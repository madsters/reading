---
updated: 2026-07-15
source: ../sb_grid_lab/memory.md  (+ studies/*/memory.md) — refresh from here when focus shifts
---

# Current work

## Research focus
Late-PhD, **power-system frequency dynamics**. Central thesis thrust: **load-model
fidelity changes frequency-stability outcomes in low-inertia grids** — i.e. how detailed
you model demand (WECC composite load model, CMLD) materially affects RoCoF, nadir, and
discrete protection actions. Rig: `sb_grid_lab` (Simulink + Simscape Electrical), engine
`+sb_grid_sim`, harness `+sb_grid_testbench`.

## Active threads
- **effective_inertia** *(active, paper-facing — PowerTech/PowerTech-style paper).* Does
  the draft paper's closed form `H_load = Σ_i (F_mi/LF_i)·H_i` scale under heterogeneous
  per-motor inertia and fractions? **Result so far:** measured `H_eff ≈ 1.0·H_load +
  offset` (slope≈1, R²≈0.99, offset ~0.2–0.25 s). The formula predicts the *sensitivity*
  but misses a **fast-frequency-response offset** — so `H_load` is a stored-energy upper
  bound, not delivered inertia. Physics: an induction motor ≈ synchronous inertia behind a
  first-order lag τ≈70–170 ms, delivering >90% of its KE by 500 ms; motors couple to
  frequency only via **slip–torque**. Calibrating the response factor `r = H_eff/H_load`.
  Currently exploring a genuinely **weak grid** corner (M_g1≈1, H≈2.6 s).
- **reducing_cmld** *(active).* Model-reduction ladder L0→L1→L2 of the CMLD, judged by
  regression vs the full model. Headline: a single **variable-torque equivalent motor**
  reproduces the 3-motor CMLD (RoCoF 0%, nadir 1.2%). Defines `H_eq` (MVA-weighted over
  motor MVA — *distinct* from `H_load`).
- **pv_trip** *(complete, merged).* Load-model fidelity **flips a discrete protection
  outcome**: static load predicts frequency below the **49.5 Hz DER-trip line** (rooftop
  PV trips → cascade) while the CMLD rides through; a second flip at the **49.0 Hz UFLS**
  line. Event ordering (PV trips at 49.5 *before* UFLS at 49.0) makes the response
  nonlinear/path-dependent.

## Open questions
- Is the reported "effective inertia" the whole 500 ms-RoCoF response (rotor coupling +
  load relief) or just the rotor part? Decides the headline number.
- What is the right static baseline (constant-Z vs constant-P) for defining the offset?
- **Feeder aggregation** as an explicit modelling assumption: a single aggregate feeder
  impedance sets voltage drop → CMLD voltage-dependent response → frequency contribution.
  How representative is one aggregate feeder, and how sensitive are RoCoF/nadir to it?
- Building a *genuine* full CMLD: Motor D (1-φ A/C, stall/restart), voltage-tripping
  electronic load (Fv/Vd1/Vd2), and **DER_A** distributed PV (electrical current injection,
  inverter dynamics) rather than the current frequency-triggered net-load proxy.

## Methods & tools
WECC composite load model (`cmld_3m` = 3-phase-motor subset); RoCoF-based `H_eff`
extraction (window-dependent, 500 ms); matched-MW / 1-pu operating-point conventions;
grid strength via SCR and inertia via `M_g1` (H seconds, not MW·s); Simulink/Simscape SPS;
SQLite-dedup sweep harness. Grid-forming vs grid-following framing for DER.

## Keywords
composite load model (CMLD), effective inertia, H_load / H_eff, RoCoF, frequency nadir,
low-inertia grid, induction motor slip–torque, voltage-dependent load, feeder aggregation,
DER / rooftop PV tripping, UFLS, grid-forming converter, model reduction, frequency
stability.
