---
name: ingest
description: Ingest a dropped file (paper, slide deck, or document) into a materials/<slug>/ corpus at highest fidelity. Detects type, confirms with the user, runs the right extraction path, builds notation and flags, and calibrates the learner profile. Use when a new file appears in inbox/ or the user asks to process/read a document.
---

# Ingest

Turn a file in `inbox/` into a clean `materials/<slug>/` corpus. This is stage 1–3 of
Phase A. Do the mechanical work with the scripts; do judgement work (flags, notation,
calibration) yourself.

## Run-start prompt (always)
1. Run `scripts/detect_type.py <file>` to get the profile guess + signals.
2. **Ask the user** to confirm or override the detected profile, and optionally supply
   hints — **author, research group, or source** — used later by `contextualise` when
   there's no citation graph. Record hints in `materials/<slug>/context-hints.txt`.
3. **Ask which pipeline** to run: **comprehend** (understand — the default chain ending in
   the one-pager) or **review** (referee a paper). **Review is a superset** — it runs the
   full comprehend pipeline first, then the `review-paper` stages — so there's no separate
   "both". `ingest` always runs first either way.

## Ingestion (pick by confirmed profile — best fidelity first)
- `arxiv-paper` → `scripts/fetch_arxiv_source.py <id> --out materials/<slug>/source`
  then read the flattened `.tex` into `material.md`. **Near-lossless — do not quiz
  notation on this path.**
- `slides` **and `.pptx`** → `scripts/extract_slides.py <file> --out materials/<slug>`
  (text + speaker notes + slide images). Speaker notes are the richest comprehension
  signal — keep them.
- `slides` **but a PDF** (e.g. a Beamer deck) → `scripts/convert_pdf.py <file> --out
  materials/<slug> --no-ocr` — python-pptx can't read a PDF, and a Beamer PDF has no
  speaker notes. Use `--no-ocr` for born-digital PDFs (clean text layer); formula
  enrichment stays on so equations come through as LaTeX.
- `journal-paper` / PDF → `scripts/convert_pdf.py <file> --out materials/<slug>`
  (add `--no-ocr` if it's born-digital rather than scanned).
- `document` → `scripts/convert_doc.py <file> --out materials/<slug>`.

## Flag-and-confirm (flag-driven)
Read the converter's `flags.json`. Write `flags.md` listing unreadable / low-confidence /
possibly-misread regions. **Only** put regions in front of the user where confidence is
low — don't quiz the near-lossless source path.

## Notation
Extract every symbol/operator into `notation.md` (meaning + scalar/vector/matrix role).
Enforce the bold convention: single letters in vector/matrix roles are bold unless proven
scalar; ambiguous cases are flagged, not guessed.

## Learner-profile calibration (if profile/maths-background.md has `learning_mode: on`)
Diff the extracted concept list against `profile/maths-background.md`. Ask the user **one
batched multi-select** covering only concepts not already recorded. Grade each on the
**mastery ladder** (`unseen → seen → followed → applied → intuitive`) — don't collapse to
"comfortable or not": a concept can be `followed` (worked through the definition) without
being `intuitive` (relatable to their own work). Capture a `target` where they're actively
learning something. Write back level/target/confidence/provenance/date. Early materials
ask a lot; it tapers as the ledger fills.

## Verify + one-pager run by default
After ingest, the pipeline continues into `contextualise`, `verify-maths`, and `one-pager`
automatically (only `expand-derivation` waits to be asked).

## Outputs
`material.md`, `notation.md`, `flags.md`, `context-hints.txt`, updated
`profile/maths-background.md`.
