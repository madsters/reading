---
name: expand-derivation
description: Fill in the omitted algebra behind a compressed step ("substituting and rearranging yields…"), marking which leaps are routine and which are genuinely non-obvious. Expansion granularity defaults to the learner profile. Use when the user is stuck on how one line follows from another.
---

# Expand derivation

Make a compressed step explicit. Stage 5 of Phase A — on demand, where most reading time
goes.

## Set the granularity from the profile
Read `profile/maths-background.md`. Expand at the level the profile implies: skip steps
the user has marked `known`, spell out steps touching `learning`/`not-yet` concepts. If
`learning_mode: off`, default to a medium level of detail.

## Expand
Take the source step from `material.md` and reconstruct the intermediate algebra line by
line. For each line, mark it **routine** (mechanical, safe to skim) or **non-obvious**
(a real insight, a non-trivial identity, a hidden assumption). Cross-check against
`notation.md` so symbols keep their roles, and against `verify.md` for anything already
flagged as suspect.

## Prerequisite gaps
If the expansion needs a concept the profile marks `not-yet`, say so explicitly and, when
useful, suggest which missing concept to shore up first (what it unlocks). Optionally
record newly-understood concepts back into the profile.

## Output
Append the expansion to `material.md` (or a `derivations/` note), keeping equation
references intact so the Q&A phase can cite them.
