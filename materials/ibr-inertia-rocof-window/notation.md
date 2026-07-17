# Notation — Wang et al., online IBR inertia estimation

All quantities per-unit unless noted (paper drops the `*` after Eq 3). Equations read from
the rendered PDF (see `flags.md`).

| Symbol | Meaning | Loc |
|---|---|---|
| $H,\ D$ | IBR-plant inertia constant (s) and damping coefficient (unified FR model) | Eq (3) |
| $H_{CS},D_{CS}$ / $H_{VS},D_{VS}$ | inertia/damping of current-source / voltage-source IBR types | Eq (1),(2) |
| $\Delta f = f_N - f$ | frequency deviation ($f_N$ nominal, $f$ actual) | Eq (1) |
| $\Delta P_{FR}$ | frequency-response power (per-unit) | Eq (3) |
| $\Delta P_D,\ \Delta P_H$ | damping power ($\propto\Delta f$) and inertia power ($\propto$ RoCoF) | Eq (4) |
| $r = \mathrm{d}\Delta f/\mathrm{d}t$ | RoCoF | Eq (4) |
| $\Delta f_\infty$ | steady-state frequency deviation | Eq (5) |
| $T_w = N\,T_s$ | RoCoF calculation window length; $N$ samples, $T_s$ sampling interval | Eq (8),(17) |
| $\tau$ | LPF time constant, $\in[0.05,0.2]$ | Eq (9) |
| $n_P,\ n_f$ ; $\sigma_P^2,\sigma_f^2$ | post-LPF noise terms and their variances (assumed zero-mean, independent) | Eq (10),(11) |
| $\hat{P},\hat{f},\hat{r},\bar H$ | estimates of power, frequency, RoCoF, and final (averaged) inertia | Eq (10),(19),(22) |
| $\Omega=[t_{0.8},t_{0.2}]$ | valid inertia-estimation interval (RoCoF between 80% and 20% of peak $r_p$) | Eq (20),(21) |
| $\delta p,\ \delta r$ | inertia-power and RoCoF estimation errors | Eq (23) |
| $f^{(k)}$ | $k$-th time derivative of $f$ at window centre $t_c$ (Taylor expansion) | Eq (31) |
| $E_b,\ E_n$ | bias ($\propto T_w^2$) and noise ($\propto T_w^{-3}$) components of relative error | Eq (36) |
| $T_w^{*}$ | optimal window (fifth-root form) | Eq (37) |

**Core relations:** $\Delta P_{FR}=\Delta P_D+\Delta P_H = D\,\Delta f + 2H\,r$ (Eq 4);
$D=\Delta P_{FR,\infty}/\Delta f_\infty$ (Eq 6); $H=\Delta P_H/(2r)$ (Eq 7).
