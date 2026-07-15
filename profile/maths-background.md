---
learning_mode: on          # off disables all probing and adaptation
owner: maddy
---

# Maths background

Concepts move `not-yet → learning → known` as you demonstrate or declare understanding.
The `ingest` skill probes only *new* concepts per material; Phase B updates this
conversationally.

Each row: **concept** | status | confidence | provenance | last-updated
(provenance = self-reported | demonstrated).

## Known
| concept | status | confidence | provenance | last-updated |
|---|---|---|---|---|
| phasors & analytic signals | known | med | self-reported | 2026-07-15 |
| admittance (Y-bus) matrix | known | med | self-reported | 2026-07-15 |
| DAE modelling (z'=f, 0=g) | known | med | self-reported | 2026-07-15 |
| grid-forming vs grid-following (concept) | known | med | self-reported | 2026-07-15 |
| RoCoF / frequency stability | known | med | self-reported | 2026-07-15 |
| local synchronization (general term) | known | low | self-reported | 2026-07-15 |

## Learning
| concept | status | confidence | provenance | last-updated | note |
|---|---|---|---|---|---|
| complex power S = V I* | learning | low | self-reported | 2026-07-15 | "kinda familiar" |
| GFM/GFL exact dynamics | learning | low | self-reported | 2026-07-15 | gets concept, not the detailed device dynamics |

## Not yet
| concept | status | provenance | last-updated | first seen in |
|---|---|---|---|---|
| Park / dq transform | not-yet | self-reported | 2026-07-15 | milano-complex-frequency |
| Hadamard product (∘) | not-yet | self-reported | 2026-07-15 | milano-complex-frequency |
| synchronous machine dq dynamics | not-yet | self-reported | 2026-07-15 | milano-complex-frequency |
| small-signal / eigenvalue stability | not-yet | self-reported | 2026-07-15 | milano-complex-frequency |
| complex frequency (η = ρ + jω) | not-yet | self-reported | 2026-07-15 | milano-complex-frequency |

## Prerequisite chains observed
- **complex frequency (η=ρ+jω)** ⟸ builds on *complex power* (learning) + *Park/dq
  transform* (not-yet). Suggested order to unlock the deck's core: Park/dq → solidify
  complex power → complex frequency. Hadamard product is a quick, isolated fix.

## Notation conventions I use
<!-- add as they come up -->
