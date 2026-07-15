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

## Relevance to your work
Directly relevant to power-systems / low-inertia grid dynamics: complex frequency is a
control-and-stability framing for **grid-forming converters and inverter-based resources**
in low-inertia systems — the regime a modern energy portfolio increasingly operates in.
The RoCoP (rate of change of power) decomposition and the "constant power / constant
admittance / constant current" special cases (slides §2) are practical device-behaviour
models worth connecting to any inverter/converter modelling you hold.

*(If you keep Zettelkasten notes on grid-forming control, frequency stability, or
inverter-based resources, this deck is the hub linking Milano's 2022 complex-frequency
paper to the 2025 local-synchronization and dual-GFM results.)*
