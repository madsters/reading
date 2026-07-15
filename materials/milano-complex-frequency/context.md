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
Grounded in `profile/current-work.md` — this connects to specific active threads, not just
"power systems":

- **`effective_inertia` (your paper-facing study) ↔ complex frequency + RoCoP.** Your core
  finding is $H_{\text{eff}} \approx H_{\text{load}} + \text{offset}$, where the ~0.2–0.25 s
  offset is a *fast frequency response* beyond pure stored inertia. Milano's
  $\bar\eta=\rho+j\omega$ splits a device's response into a **voltage-magnitude rate $\rho$**
  and an **angular-frequency rate $\omega$**, and the RoCoP relation $\bar s' = \bar\eta\,\bar
  s + \bar v\circ\bar\imath'^{*}$ decomposes the *rate of change of power* into a
  complex-frequency-driven term plus a current-variation term. That is a candidate analytic
  language for the very thing you're trying to separate: the ω-part is your inertial RoCoF
  response, the ρ-part is the voltage-driven fast response your offset lumps in. Milano's own
  "From Stored Energy to Delivered Response" framing is the same stored-vs-delivered gap as
  your $r = H_{\text{eff}}/H_{\text{load}}$. **Concrete idea:** logging $\rho$ and $\omega$
  separately (you already log `vrms_pu` and `freq_hz`) might let you attribute the offset to
  voltage vs frequency instead of leaving it as one lumped term.
- **Induction-motor slip–torque coupling ↔ local synchronization / $\bar\chi=\bar\xi-\bar\eta$.**
  Your motors couple to grid frequency via slip with a first-order lag $\tau(H)\approx$70–170 ms.
  Milano's device-side component $\bar\chi=\bar\xi-\bar\eta$ (current growth rate vs grid
  complex frequency) and the local-sync condition $\rho\to0,\ \omega\to\omega_r$ formalise how
  a device tracks the grid — a possibly cleaner handle on your response factor $r$ than
  window-dependent RoCoF differencing.
- **CMLD voltage-dependent response + feeder aggregation ↔ $\rho$.** Your open question —
  aggregate feeder impedance → voltage drop → CMLD voltage-dependent response → frequency
  contribution — is exactly what $\rho=\dot v/v$ captures dynamically. Complex frequency gives
  a unified $(\rho,\omega)$ treatment of the coupled voltage+frequency load response, useful
  when you state and test the feeder-aggregation assumption's effect on frequency.
- **`pv_trip` / DER_A backlog ↔ Dual-GFM & grid-forming.** Milano's Dual-GFM application (§5)
  and the local-synchronization criteria bear on your planned electrical **DER_A** and the
  grid-forming/-following framing behind your DER-trip scenarios.

**Caveat:** Milano's framework is continuous/analytic (complex frequency of smooth signals),
so it speaks to your *inertia/response* work — **not** to `pv_trip`'s discrete, path-dependent
protection switching (49.5 Hz DER trip, 49.0 Hz UFLS), which its smooth formulation doesn't
capture.
