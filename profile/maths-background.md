---
learning_mode: on          # off disables all probing and adaptation
owner: maddy
---

# Maths background

## Mastery ladder
Each concept is graded on a ladder that separates *mechanics* from *intuition/transfer* —
so "worked through the definition" is distinct from "can relate it to my own work":

| Level | Meaning | How Phase B should pitch |
|---|---|---|
| `unseen` | never encountered | teach from scratch |
| `seen` | aware of it, not worked through | build up from basics |
| `followed` | worked through the definition/derivation; can reproduce it (mechanics, not intuition) | **skip re-deriving; build intuition + worked examples + connect to my work** |
| `applied` | can use it independently in new problems | recall only; clarify edge cases |
| `intuitive` | intuitive, transferable grasp; can relate to my own work and explain why it matters | use freely as a building block |

Concepts carry an optional **`target`**. Movement is dated; provenance is `self-reported`
or `demonstrated`. Levels marked *(confirm)* were inferred from a batched probe (concept
not selected as comfortable) and should be checked conversationally.

Row format: **concept** | level | target | confidence | provenance | last-updated | note

## Concepts
| concept | level | target | conf | provenance | updated | note |
|---|---|---|---|---|---|---|
| phasors & analytic signals | applied | — | med | self-reported | 2026-07-15 | |
| admittance (Y-bus) matrix | applied | — | med | self-reported | 2026-07-15 | |
| DAE modelling (z'=f, 0=g) | applied | — | med | self-reported | 2026-07-15 | |
| RoCoF / frequency stability | applied | — | med | self-reported | 2026-07-15 | |
| grid-forming vs grid-following (concept) | applied | — | med | self-reported | 2026-07-15 | concept only |
| GFM/GFL device dynamics | seen | followed | low | self-reported | 2026-07-15 | gets concept, never went into exact dynamics |
| complex power S = V∘I* | followed | applied | low | self-reported | 2026-07-15 | "kinda familiar" |
| local synchronization | followed | — | low | self-reported | 2026-07-15 | general notion; confirm vs Milano §3 formalization |
| **complex frequency (η = ρ + jω)** | **followed** | **intuitive** | med | self-reported | 2026-07-15 | worked through the definition; no transferable intuition yet — the target |
| Park / dq transform | seen | followed | low | self-reported | 2026-07-15 | (confirm) |
| Hadamard product (∘) | seen | followed | low | self-reported | 2026-07-15 | (confirm) |
| synchronous machine dq dynamics | seen | — | low | self-reported | 2026-07-15 | (confirm) |
| small-signal / eigenvalue stability | seen | — | low | self-reported | 2026-07-15 | (confirm) |

## Prerequisite chains observed
- **complex frequency (η=ρ+jω): `followed` → target `intuitive`.** Mechanics are there;
  the gap is transferable intuition. It builds on *complex power* (`followed`) and *Park/dq
  transform* (`seen`). To reach `intuitive`: (1) firm up Park/dq → `followed`, (2) complex
  power → `applied`, then (3) spend the effort on **intuition + connecting η to my own work**
  (grid-forming / low-inertia), not on re-deriving the definition. Hadamard (∘) is a quick,
  isolated fix.

## Notation conventions I use
<!-- add as they come up -->
