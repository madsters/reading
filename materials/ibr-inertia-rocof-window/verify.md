# Verification — Wang et al., online IBR inertia estimation (TSTE submission)

Soundness pass on the load-bearing error-analysis result (Section IV, Eqs 31–37). The
paper's equations render as images in `material.md` (see `flags.md`); the forms below were
read off the rendered PDF (bundle pp. 8–9) and checked in a standalone sympy session
(symbolic solve of the optimum + a continuum least-squares derivation of the bias/variance).
The standard `verify.py`/`checks.json` flow didn't apply here because the equations weren't
machine-extracted.

| Result | Location | Check | Verdict |
|---|---|---|---|
| Optimal window from dε/dT_w = 0, ε = a·T_w² + b/T_w³ ⟹ **fifth-root** T_w\* = (3b/2a)^{1/5} | Eq (37) | symbolic solve | ✅ **pass** — structure correct |
| Noise variance of LS slope Var(r̂)=12σ²/(N·T_w²) = 12·T_s·σ²/T_w³ ∝ **1/T_w³** | Eq (33), (36) E_n | symbolic | ✅ **pass** — matches paper's E_n∝T_w⁻³ |
| Truncation-bias scaling ∝ f⁽³⁾·T_w² | Eq (33) Bias | continuum LS | ✅ scaling correct |
| Truncation-bias **coefficient** | Eq (33) | continuum LS | ⚠️ **discrepancy to check**: I get f⁽³⁾·T_w²/**40**; the paper appears to print /**80** |

## Notes
- **Verified sound (structure):** the central claim — a bias term rising as T_w² (linear-fit
  truncation) competing with a noise term falling as 1/T_w³ (window averaging), yielding a
  fifth-root optimum weakly sensitive to parameters (hence a flat, robust plateau) — is
  mathematically correct. This is the paper's key theoretical contribution and it holds up.
- **⚠️ Coefficient (factor ~2), concern not confirmed error:** my continuum least-squares
  derivation of the cubic-term truncation bias gives `f⁽³⁾·T_w²/40`; Eq (33) reads `/80` in
  the rendered proof. This could be a τ-indexing/normalisation convention (discrete Σ vs
  continuum ∫, N vs N−1, or T_w=(N−1)T_s vs N·T_s) rather than an error — but the constants
  flow into the numeric T_w\* in (37), so **the authors should show the (31)→(33)→(36)→(37)
  algebra explicitly**; a reviewer can't currently reproduce the exact "720" constant.
  (Mitigated by the paper's own point that the optimum is a flat plateau, so a 2× coefficient
  shifts T_w\* only ~2^{1/5} ≈ 15%.)
- **⚠️ White-noise assumption (see assumptions.md M3):** the Var∝1/T_w³ result assumes
  independent (white) samples. The method low-pass-filters f and P first (Section III.A),
  which colours the noise — this is *not* modelled and would change the noise-term scaling.
  Not a maths error, but a modelling gap that undercuts the quantitative T_w\* prediction.
