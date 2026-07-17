# Flags — Wang et al., online IBR inertia estimation

Ingestion: `journal-paper`, Docling `--no-ocr --no-formula`. Formula enrichment was
**deliberately skipped** — a first full-formula pass ran >20 min on CPU (dense 13-page
equation-heavy paper) with all-or-nothing output. Instead:

- **Equations are `<!-- formula-not-decoded -->` placeholders in `material.md`.** The
  load-bearing equations (FR model 1–3; estimation 4–22; error analysis 23–37) were read
  directly off the **rendered PDF pages** (bundle pp. 4–9, via PyMuPDF) — more reliable than
  bulk per-equation OCR (cf. the `\wp`→`j` misreads on the Milano deck). Soundness checks in
  `verify.md` are based on those hand-read forms.
- **Front-matter duplication:** `material.md` begins with the submission cover bundle
  (author CRediT blocks, affiliations ×4, keywords) before the paper proper at line ~99.
  Not paper content.
- **Tables II–III** (experimental parameters) came through with garbled cell alignment in the
  proof conversion — values are legible but the table structure is messy; cross-check against
  the PDF if a specific parameter matters.
- **This is an initial submission proof for peer review** (TSTE-00929-2026), not a published
  paper — no arXiv/DOI identity, so no citation-graph lookup (see `context.md`).
