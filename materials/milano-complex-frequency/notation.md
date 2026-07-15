# Notation — Milano complex-frequency tutorial

Convention: an **overbar** ($\bar x$) marks a **complex-valued** quantity (Park's vector /
analytic signal), valid in transient conditions. Lowercase = scalar/per-bus complex value;
**bold or capital** letters denote vectors/matrices over buses. `*` = complex conjugate,
`∘` = Hadamard (element-wise) product, prime `'` and dot = time derivative.

⚠️ The imaginary unit is written inconsistently by the converter as `j`, `\jmath` (ȷ), and
— erroneously — `\wp` (℘). **Everywhere `\wp` appears it means the imaginary unit $j$.** See
`flags.md`.

| Symbol | Role | Meaning | Loc (line) |
|---|---|---|---|
| $\bar v = v_d + j v_q = v\,e^{\,u+j\theta}$ | complex | Park-vector bus voltage; polar form with $u=\ln v$ | 101–127 |
| $v$, $\theta$ | scalar | voltage magnitude, phase angle | 117–127 |
| $u = \ln v$ | scalar | log-voltage magnitude (so $\bar v = e^{u+j\theta}$) | 127 |
| $\bar s = p + j q = \bar v \circ \bar\imath^{\,*}$ | complex | complex power; $p$ active, $q$ reactive | 101, 207, 241 |
| $\bar\imath$ | complex | Park-vector current (misread as $\bar a$ at line 101) | 189, 231 |
| $\bar Y$ | complex matrix | network admittance; $\bar\imath \approx \bar Y\,\bar v$ | 189, 207 |
| $\bar S$ | complex matrix | $\mathrm{diag}(\bar s)$ — diagonalised power vector | 241 |
| $\bar I$ | complex matrix | $\mathrm{diag}(\bar\imath)$ | 231 |
| **$\bar\eta = \rho + j\omega$** | complex | **complex frequency** $= \tfrac{d}{dt}(u+j\theta) = u' + j\theta'$ | 145 |
| $\rho = u' = \dot v / v$ | scalar | real part: normalised rate of change of voltage *magnitude* | 145 |
| $\omega = \theta'$ | scalar | imaginary part: instantaneous angular *frequency* | 145 |
| $\bar s' $ | complex | rate of change of power (RoCoP); $\bar s' = \bar s\circ\bar\eta + \bar v\circ\bar\imath'^{*}$ | 263 |
| $\bar\chi$ | complex | device-side RoCoP quantity; $\bar\chi = \bar\xi - \bar\eta$ | 648, 672 |
| $\bar\xi$ | complex | current growth rate, $\bar\imath' = \bar\imath\,\bar\xi$ | 648 |
| $\bar\kappa_\rho,\ \bar\kappa_\omega$ | complex | sensitivity coefficients of $\bar\xi$ to $\rho,\omega$ | 676 |
| $z,\ y$ | vector | DAE differential / algebraic variables: $z'=f(z,y),\ 0=g(z,y)$ | 307 |
| $\omega_r$ | scalar | rotor / reference angular speed | 774, 804 |
| $R_s,\ x_{d},\ x_{q}$ | scalar | machine stator resistance, d/q reactances (subscripts unreliable — see flags) | 774 |

## Key relations (confirmed)
- Voltage derivative: $\bar v' = \bar v \circ \bar\eta$  (line 217)
- Current derivative: $\bar\imath' = \bar Y\,\bar v' = \bar I\,\bar\eta$  (line 231)
- Local synchronization condition: $\rho \to 0 \ \wedge\ \omega \to \omega_r$  (line 804)

## Acronyms
**RoCoP** rate of change of power · **TSC** transient slack capability · **GFM**
grid-forming (converter) · **Dual-GFM** the deck's application (§5) · **BLS/ALS** bounded /
asymptotic local synchronization (slides 706/716).
