# Context — Wang et al., "Online Inertia Estimation for IBR Plants" (TSTE submission)

**Identity:** initial submission to IEEE Trans. Sustainable Energy (TSTE-00929-2026), Wang,
Xiong, Liu, Wang (Xi'an Jiaotong Univ.). No arXiv/DOI, so no citation-graph lookup; the
positioning below is from the paper's own §I literature review.

## Where it sits
Inertia estimation splits into **passive observation** (PMU/ambient data, modal or
data-driven — refs [10]–[15]; low SNR) and **active disturbance** (fault/event/HVDC
excitation — [16]–[18]; disrupts operation). This paper's niche: a **controllable, small
active-power disturbance at a single IBR plant**, giving per-plant (not system-level)
inertia with good SNR and without disrupting the grid — and, distinctively, an **analytical
error model** that turns RoCoF window-length selection from the *empirical* grid-code values
(Table I: 100–500 ms, no consensus) into a *theoretically grounded* optimum.

## Genuine contribution (on its own terms)
The **error-propagation model + fifth-root optimal-window result (Eqs 31–37)** is the real
novelty and is mathematically sound in structure (see `verify.md`). Per-plant estimation and
the D/H power decomposition without internal control parameters are practical and useful.
The theoretical window-length guideline addressing the Table-I inconsistency is the strongest
selling point.

## Relevance to my work (`effective_inertia`) — grounded, with a caveat
This is almost exactly your active area, so the connection is direct and the critique
potential is high:

- **RoCoF window-length trade-off.** Your T2 back-computes $H_{\text{eff}}$ from RoCoF and
  you've seen it is **window-dependent**; this paper derives the bias/noise trade-off
  ($\propto T_w^2$ vs $\propto 1/T_w^3$) and an optimal $T_w$ analytically. Their guideline
  (250–300 ms) is a concrete external reference point for your own window choice.
- **The decomposition assumption vs your offset finding.** They assume FR power splits
  cleanly into $D\Delta f + 2Hr$ (Eq 4). Your result — measured $H_{\text{eff}} \approx
  H_{\text{load}} + \text{offset}$, the offset being a fast frequency-response term beyond
  stored inertia — suggests a component that is *neither* pure damping nor pure inertia and
  would be **misattributed to $H$** by their split. That's a substantive scientific
  divergence, directly on point for a review of this paper (see `assumptions.md` A3).
- **Their plant = your grid-side vs device-side distinction.** They estimate a *plant* $H$;
  your CMLD work estimates *load* effective inertia — complementary sides of the same
  low-inertia frequency-stability problem.

> ⚠️ **Honesty:** the offset critique rests on your *unpublished* results. It is a strong,
> legitimate prior, but a referee report can't cite unpublished work as grounds; frame any
> such comment as a general modelling question ("does the D·Δf + 2H·r split risk absorbing a
> fast-frequency-response term into H?"), not as "my results show…". Carried into
> `review.md`'s honesty ledger.
