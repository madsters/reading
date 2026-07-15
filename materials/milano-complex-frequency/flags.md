# Flags — Milano PSCC 2026 tutorial

Honest record of what couldn't be read cleanly or needs confirmation. Ingestion path:
`slides` profile, Docling conversion of a born-digital Beamer PDF (`--no-ocr`, formula
enrichment on). Docling's own confidence report was empty (`flags.json = []`), so the
items below come from a manual review pass, not automated grading — treat them as
*flag-driven confirmation targets*.

## Formula-recognition misreads (confirm before trusting)
The CodeFormula model recovered most equations well, but made systematic symbol errors:

1. **Imaginary unit inconsistent.** Rendered as `\jmath` (ȷ), `j`, and — wrongly — as
   `\wp` (Weierstrass ℘) in the *same* role. E.g. line 117 `\bar v = v_d + \jmath v_q`
   (correct) vs line 127 `\bar v = v\,e^{\wp\theta}` (should be `e^{j\theta}`). Everywhere
   `\wp` appears in an exponent/derivative it means the **imaginary unit j**.
2. **Power definition symbol.** Line 101/113: `\bar s = \bar v \circ \bar a^*`. The
   `\bar a` is almost certainly a misread of the **complex current ī** — complex power is
   $\bar s = \bar v \circ \bar\imath^{\,*}$, consistent with lines 207/241 which use ī.
3. **Garbled high-order model equations.** Slides around lines 774 and 784 (xth-order
   machine model) contain OCR-level corruption: `\int\limits_{\}eq`, inconsistent
   subscripts (`x_{2d}` vs `x_{1d}`, a stray `x_{aq}`), and mismatched brackets. Do **not**
   trust these two equations verbatim; cross-check against the source PDF / arXiv:2105.07769
   before using them.

## Structural artifact — Beamer overlay duplication
The 127 "pages" include many **overlay frames of the same logical slide** (progressive
builds), so most sections and equations appear **2–3× consecutively** in `material.md`
(e.g. `## Complex Frequency` at lines 123/135/151/167; the RoCoP derivation repeats). This
is not new content — it's the same slide revealed incrementally. When citing, cite the
*logical* slide, and expect repeats. (A future dedup pass could collapse these.)

## Context
- Web-search context fallback was **unavailable** (the installed search backend returned
  no usable results). `context.md` was therefore built from the deck's own §6 References,
  which is actually the higher-quality source here. No external "who-cites-this" graph was
  built.

## Not flagged / trustworthy
- The core conceptual equations (complex frequency $\bar\eta=\rho+j\omega$, its link to
  current and power, the RoCoP definition and special cases) came through cleanly modulo
  the `\wp`→`j` substitution above.
- Section structure, titles, and the reference list extracted reliably.
