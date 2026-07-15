# Reading Assistant

Drop a dense document — a research paper, a tutorial slide deck, a technical report —
into `inbox/`, and this tool processes it at high fidelity into a corpus that a **Claude
Project** can use to help you *understand* it, with the maths rendered properly.

It's built around a few ideas:

- **Source-first ingestion.** Pull the original LaTeX for arXiv papers (zero fidelity
  loss); extract text + speaker notes + slide images for decks; use math-aware conversion
  only as a fallback. Boldedness and notation survive.
- **Type-aware routing.** A dropped file is auto-detected as a paper, slide deck, or
  document; you confirm or override at the start of each run and can add author/group/
  source hints for context lookup.
- **Content-triggered stages.** Maths verification and notation work fire whenever there
  *is* maths — paper or tutorial, not keyed to file type.
- **Adaptive to you.** A toggleable learner profile records what maths you already know
  and pitches every explanation, warning, and derivation to your level — updating as you
  learn.
- **Two deliverables.** A rich markdown corpus (what the Claude Project reads) and a
  polished one-page PDF.

## Layout

```
inbox/            drop files here to process
.claude/skills/   the build pipeline (Phase A): ingest, contextualise,
                  verify-maths, expand-derivation, one-pager
scripts/          deterministic helpers (detect, fetch, convert, verify, build)
templates/        profile-aware one-pager LaTeX (paper + tutorial digest)
profile/          learner profile (blank on main; real data on a private branch)
materials/        per-material output corpora
CLAUDE.md         Phase B brief for the Claude Project (comprehension)
reading-assistant-plan.md   full design & workflow
```

## Usage

1. **Build (Claude Code):** drop a file in `inbox/`, then run the `ingest` skill and its
   downstream skills. Output lands in `materials/<slug>/`.
2. **Comprehend (Claude Project):** point a Claude Project at this repo and ask questions;
   `CLAUDE.md` tells it to read the corpus, cite locations, render maths, and adapt to
   your learner profile.

## Learner profile & privacy

`main` ships a **blank** `profile/maths-background.md`. Keep your real profile on a
separate branch (e.g. `maddy-learning`) with private access, and merge improvements
forward from `main` as the tool evolves.

## Install

You provide the tooling: a LaTeX toolchain + `latexpand`, a math-aware PDF converter,
`python-pptx` (+ a headless renderer for slide images), a docx→markdown converter,
`requests`, `sympy`, and a static file server if you want terminal-phase HTML rendering.
See `reading-assistant-plan.md` for where each is used.
