# Context — Milano, *Complex Frequency, Local Synchronization and Transient Slack Capability*

**Source.** PSCC 2026 tutorial, "Modelling, Control, Stability Analysis and Simulation of
Low-Inertia Power Systems" (subtitle: *New Concepts for New Power Systems*). Author:
**Federico Milano**, University College Dublin. 127-slide Beamer deck (slides 1–2 title;
§6 References).

> Context was built from the deck's own reference list (reliable, with arXiv IDs), not
> from web search — the web-search fallback backend was unavailable at build time (see
> `flags.md`). The lineage below is therefore the author's own cited body of work.

## What it is
A synthesis tutorial pulling together Milano's research programme on **complex frequency**
— a single complex-valued quantity $\bar\eta = \rho + j\omega$ that unifies the rate of
change of a bus voltage's *magnitude* ($\rho$) and its *phase/angular frequency* ($\omega$)
into one object, valid in transient conditions (Park vectors / analytic signals). The deck
develops it toward **local synchronization** (a grid-side view of synchronism/stability)
and **transient slack capability** (what a device needs to sustain the grid after a large
disturbance), with a **dual grid-forming converter** as the application.

## Problem lineage (from §6 References)
Foundational and directly-building work, all Milano-group:

- **Complex Frequency** — F. Milano, *IEEE TPWRS* 37(2):1230–1240, 2022. arXiv:2105.07769.
  The originating paper; defines $\bar\eta$.
- **A Geometrical Interpretation of Frequency** — F. Milano, *IEEE TPWRS* 37(1):816–819,
  2022. The geometric grounding of the frequency concept.
- **Local Synchronization of Power System Devices** — I. Ponce, F. Milano, *IEEE TPWRS*
  40(5):4194–4204, 2025. arXiv:2407.02661. (§3 of the deck.)
- **Dual Grid-Forming Converter** — F. Milano, *IEEE TPWRS* 40(2):1993–1996, 2025.
  arXiv:2408.13185. (§5 application.)
- **Transient Slack Capability** — R. Bernal, F. Milano. arXiv:2505.17984. (§4.)

## Reception / generalization (Further Reading)
- Taxonomy of converter control schemes via complex frequency — Moutevelis et al.
  (arXiv:2209.11107).
- A complex-frequency-based control for inverter-based resources — Bernal & Milano
  (arXiv:2501.00448).
- Generalizations: *Equivalence between Geometric Frequency and Lagrange Derivative*
  (arXiv:2410.02340); *Quasi Steady-State Frequency* (arXiv:2505.21461); coherency and
  power-system-strength framings (arXiv:2511.02486, 2507.16061).

## Relevance to my work
Grounded in `profile/current-work.md` and the corpus. Each link cites where in the deck it
comes from, and keeps clear what is *Milano's* framing vs *your* study's.

- **`effective_inertia`: stored vs delivered.** *Your* study draws the distinction between
  stored energy `H_load` (an upper bound) and delivered `H_eff`, and calibrates
  `r = H_eff/H_load` — that stored-vs-delivered framing is from your draft paper, not this
  deck. What the deck independently offers (§Transient Slack Capability, material.md
  lines 1366–1451) is a **technology-agnostic structure for the same split**: a
  port-Hamiltonian device with stored energy `H_k` (eq. 31), whose **Condition 1 — Energy
  Storage Capacity** (`H_k` positive semi-definite; examples: rotating-mass KE for an SM,
  DC-link capacitor energy for an IBR) is separated from **Condition 2 — Dynamic Slack**,
  the source dynamics needed to actually *sustain* power under a prolonged ΔP. That
  storage-vs-sustained-delivery split is structurally what your `r` measures empirically for
  induction-motor load — so the deck may give a formal (pH) language to frame your result,
  while your `r` is the measurement it lacks.

- **Complex frequency `η = ρ + jω` ↔ how you measure and decompose the response** (def. at
  material.md line 145; RoCoP `s' = η·s + v∘i'*` at line 263). You extract `H_eff` from
  RoCoF — the **ω** side. The deck treats **ρ = v̇/v** (voltage-magnitude rate) as a
  co-equal channel. Since you already log `freq_hz` *and* `vrms_pu`, computing ρ and ω
  separately is a concrete way to test whether your ~0.2–0.25 s offset is voltage-driven,
  frequency-driven, or both — rather than leaving it as one lumped term. (This is a proposed
  use of the deck's decomposition, not a claim the deck makes about loads.)

- **CMLD voltage-dependent response + feeder aggregation ↔ ρ.** Your open question —
  aggregate feeder impedance → voltage drop → CMLD voltage-dependent response → frequency
  contribution — is exactly the voltage-magnitude dynamics ρ captures. The deck's unified
  (ρ, ω) view is a candidate lens for stating and testing the feeder-aggregation assumption's
  effect on the load's frequency contribution.

- **Low-inertia motivation & DER.** The deck opens (line 1358) on IBR displacing physical
  rotational inertia — the regime your whole thesis addresses — and its Dual-GFM application
  (§5) and TSC metric concern whether a device can sustain the grid under a prolonged
  imbalance, which connects to your `DER_A` modelling and, thematically, to the ride-through
  question behind `pv_trip` (note `pv_trip` itself is framed around AEMO's operational
  49.5 Hz DER-trip / 49.0 Hz UFLS thresholds — an operational lens the deck doesn't address).
