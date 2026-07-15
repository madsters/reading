# Verification — Milano complex-frequency tutorial

Symbolic/numeric re-derivation of the load-bearing relations (sympy harness,
`scripts/verify.py`, spec in `checks.json`). The verified relations are the *algebraic
structure* given each stage's definitions — the fully complex/calculus definitions
(e.g. differentiating $\bar v = e^{u+j\theta}$) are taken as given upstream. All checks
**pass**.

| Relation | Location | Check | Result |
|---|---|---|---|
| $\bar\imath' = \bar\eta\,\bar\imath$ (constant admittance) | ~line 449 | re-derive from $\bar\imath=\bar Y\bar v$, $\bar v'=\bar\eta\bar v$ | ✅ pass |
| **RoCoP:** $\bar s' = \bar\eta\,\bar s + \bar v\circ\bar\imath'^{*}$ | line 263 | re-derive via product rule, $\bar v'=\bar\eta\bar v$ | ✅ pass |
| $\bar\imath' = \bar\imath(\bar\chi+\bar\eta) \Rightarrow \bar\chi=\bar\xi-\bar\eta$ | line 648 | re-derive from $\bar\imath=\bar y\bar v$, $\bar y'=\bar y\bar\chi$, $\bar v'=\bar v\bar\eta$ | ✅ pass |
| $\rho,\ \omega$ dimensionally compatible | line 145 | dimensional check: both $[\mathrm{time}]^{-1}$ | ✅ pass |
| Local-sync condition $-\rho+j(\omega_r-\omega)\to0$ | line 804 | numeric: $=0$ iff $\rho=0,\ \omega=\omega_r$ | ✅ pass |

## Notes
- **Why the dimensional check matters (intuition).** $\rho = \dot v/v$ (a
  magnitude-growth rate) and $\omega=\dot\theta$ (an angular rate) are *both* frequencies
  in the units sense — $[\text{time}]^{-1}$ — which is exactly what licenses packing them
  into one complex frequency $\bar\eta=\rho+j\omega$. This is the crux of building
  intuition for the concept (see profile: complex frequency is `followed → intuitive`).
- **RoCoP** ($\bar s' = \bar\eta\bar s + \bar v\circ\bar\imath'^{*}$) is the pivotal
  relation: the rate of change of complex power splits into a term driven by the complex
  frequency $\bar\eta$ and a term driven by the current's own variation.
- These checks validate the *manipulations*, not the flagged misreads in `flags.md`
  (the `\wp`→`j` substitution and the garbled xth-order model equations at lines 774/784
  were **not** verified and remain to be cross-checked against arXiv:2105.07769).
