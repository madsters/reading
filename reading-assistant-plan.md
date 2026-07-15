# Reading Assistant — Design & Workflow Plan

A tool for deeply understanding dense material — maths-heavy research papers, tutorial
slide decks, technical reports — by ingesting it at the highest possible fidelity,
processing it into a rich set of artifacts, and feeding those to a **Claude Project**
(cowork session) that helps you comprehend it, with maths rendered properly.

You drop a file into the repo; the pipeline detects what it is, runs the processing
that applies, and produces both a machine-readable markdown corpus and a polished
one-page PDF. A Claude Project rooted at this repo then reads those artifacts to answer
questions, expand derivations, and relate the material to your own work.

---

## Core principles

**1. Source-first ingestion.** The biggest fidelity win is *not OCRing when you don't
have to*. Most arXiv papers ship their original LaTeX source; pull that and every
equation, subscript, and bold vector arrives exactly as the author wrote it. `.pptx`
decks carry structured text and speaker notes natively. OCR / vision conversion is the
fallback, not the default.

**2. Type-aware routing.** The input can be a paper, a slide deck, or a general
document. A detection layer inspects the dropped file and picks an ingestion **profile**;
a **prompt at the start of each run** shows the detected type for you to confirm or
override, and optionally lets you supply hints — author, research group, or source — that
help the contextualise stage when there's no citation graph to lean on.

**3. Content-triggered stages.** Downstream work isn't keyed to "is this a paper." Maths
verification fires whenever there *is* maths — paper or tutorial slide. Contextualisation
fires when the material has a discoverable identity. Stages are capabilities that turn on
based on what's actually in the material, not on its file type.

**4. Two phases, split by output surface.** A terminal can't render maths, so don't ask
it to.
- **Phase A — Build** (script-heavy, runs in Claude Code): everything mechanical plus
  one-shot LLM work. Output is *files*, not terminal text. Run once per dropped file.
- **Phase B — Comprehend** (runs in a Claude Project / cowork, where maths renders): the
  session reads the built artifacts and renders each answer inline as an HTML/MathJax
  artifact. This is the real point of the tool.

**5. Adaptive to the reader.** A toggleable learner profile records what maths you already
know and pitches everything — explanation depth, which gaps to warn about, how much of a
derivation to expand — to your actual background, updating as you learn. See *Learner
profile* below.

---

## Flow

```
inbox/  ──drop a file──▶  detect type  ──▶  confirm/override + optional hints
                                                   │      (author, group, source)
                                                   ▼
                              Phase A build pipeline (stages below)
                                                   │
                                                   ▼
                              materials/<slug>/  (markdown corpus + onepager.pdf)
                                                   │
                                                   ▼
                     Claude Project at repo root ── Phase B comprehension
```

---

## Source profiles

Detection picks one; each drives ingestion and sets default expectations. Downstream
stages still gate on detected content, not on the profile alone.

| Profile | Detected by | Ingestion path | Context stage |
|---|---|---|---|
| `arxiv-paper` | arXiv ID in name/metadata | LaTeX e-print source + `latexpand` | Semantic Scholar |
| `journal-paper` | PDF with DOI / academic structure | math-aware PDF conversion | Semantic Scholar → web fallback |
| `slides` | `.pptx`, or slide-structured PDF | text + speaker notes + slide images | web search fallback |
| `document` | other PDF / DOCX (reports, notes) | doc → markdown conversion | web search fallback |

---

## Ingestion waterfall (Phase A, stage 1)

Per profile, best fidelity first:

1. **LaTeX source** (`arxiv-paper`) — `https://arxiv.org/e-print/<id>` returns the
   author's `.tex` tarball; flatten multi-file sources. Zero fidelity loss; solves the
   bold-vector problem outright.
2. **Slide extraction** (`slides`) — pull per-slide text **and speaker notes** (notes are
   gold for comprehension), and export each slide as an image so diagrams survive. A
   slide-shaped PDF is treated the same way.
3. **Math-aware conversion** (`journal-paper`, `document`, PDF slides) — a converter that
   emits real LaTeX commands (`\mathbf`, `\boldsymbol`), not flattened vision-to-markdown,
   so boldedness largely survives.
4. **Flag-and-confirm** — whatever paths 2–3 produced gets a review pass that tags
   low-confidence regions, lists anything unreadable or possibly misread, and builds a
   notation table for you to confirm before you trust the outputs.

---

## Pipeline stages (Phase A)

The pipeline runs stages 1–4 and 6–8 **by default** every time; only stage 5
(expand-derivation) is **on-demand**, invoked per question rather than up front. Stages
marked *conditional* additionally gate on detected content (e.g. maths present).

**1. Ingest** *(scripts + LLM review).* Detect type → run the profile's ingestion path →
produce `material.md`. LLM does the flag-and-confirm pass into `flags.md`.

**2. Confirm notation** *(LLM + you, conditional on maths present).* Extract every
symbol/operator into `notation.md` with meaning and vector/matrix/scalar role.
Boldedness is locked down here: single letters in vector/matrix roles are bold unless
proven scalar; anything ambiguous is flagged, not guessed. The extracted concept list
then feeds **learner-profile calibration** (see *Learner profile* below) — diffed against
what you already know so only the new concepts get probed.

**3. Contextualise** *(script + LLM).* For papers with an identity, hit the Semantic
Scholar API for what the work builds on and who cites it. For slides / documents with no
citation-graph identity, **fall back to web search**, seeded by any hints you gave at the
start of the run — an author, research group, or source name lets the search find that
group's related publications, the course or origin, and where this material sits in their
body of work. LLM writes `context.md`: lineage, contribution, positioning. Honestly
records in `flags.md` when context couldn't be established.

**3b. Resolve sources** *(script + LLM, conditional).* Fires automatically when a converted
material has **flagged low-confidence equations** *and* a **core reference on arXiv**: fetch
that paper's lossless LaTeX source (`fetch_arxiv_source.py` into `materials/<slug>/refs/`)
and reconcile the flagged equations against ground truth — correcting `material.md` and
marking flags **resolved** with a citation. This is the package self-healing recognition
errors instead of asking you to cross-check by hand. Skipped when maths converted cleanly
or no reference is on arXiv.

**4. Verify the maths** *(LLM + sympy scripts, conditional on maths present).* The trust
layer. Re-derive selected steps symbolically, check dimensional consistency, confirm
indices balance, test limiting/edge cases numerically. Results go to `verify.md`. Runs by
default: the LLM proposes the load-bearing equations (main results, anything later steps
lean on) and confirms the shortlist with you before checking.

**5. Expand derivations** *(LLM, on demand, conditional).* Take a compressed step
("substituting and rearranging yields…") and fill the omitted algebra explicitly, marking
which leaps are routine and which are genuinely non-obvious.

**6. Assumptions ledger** *(LLM).* Scattered preconditions collected into `assumptions.md`
— what each key result requires to hold — so it's obvious when a method won't transfer to
your setting. (Lighter for a tutorial than for a paper, but still useful.)

**7. One-pager** *(LLM fills, script compiles + verifies).* **Profile-aware template:** a
paper gets a problem/method/results/limitations layout; a tutorial deck gets a key-ideas /
concept-map digest. LLM drafts to the template's limits; the build script compiles to PDF
and asserts exactly one page, failing loudly on overflow.

**8. Zettelkasten source note** *(LLM).* A **small** literature note — a few hundred words
and a few key equations, in your source-note format, linked to related notes you hold.
Written *out* to your Zettelkasten source-notes folder (path TBC), not kept in this repo.

**9. Comprehend** *(Phase B, in the Claude Project).* The cowork session reads the
artifacts and answers questions, rendering maths inline. Answers cite slide numbers /
section / equation numbers from `material.md`.

---

## Repository layout

```
reading/
├── CLAUDE.md                     # Claude Project instructions (Phase B: how to comprehend)
├── inbox/                        # drop files here to be processed
├── .claude/
│   └── skills/
│       ├── ingest/               # detect type → profile ingestion → material.md + flags
│       ├── contextualise/        # Semantic Scholar OR web-search fallback
│       ├── verify-maths/         # sympy: re-derive, dim-check, index balance, limits
│       ├── expand-derivation/    # fill omitted algebra; flag non-obvious leaps
│       └── one-pager/            # fill profile-aware template, compile, verify 1 page
├── scripts/                      # deterministic muscle (no token cost)
│   ├── detect_type.py            # route a dropped file to a profile
│   ├── fetch_arxiv_source.py     # e-print tarball + flatten
│   ├── convert_pdf.py            # math-aware PDF → markdown + confidence flags
│   ├── extract_slides.py         # pptx → text + speaker notes + slide images
│   ├── convert_doc.py            # docx / other → markdown
│   ├── citations.py              # Semantic Scholar; web-search fallback
│   ├── verify.py                 # sympy harness
│   ├── build_onepager.py         # render template → PDF, assert single page
│   └── make_qa_html.py           # qa/*.md → qa/*.html with MathJax (terminal-phase render)
├── templates/
│   ├── onepager_paper.tex        # paper layout
│   └── onepager_digest.tex       # tutorial / document layout
├── profile/
│   └── maths-background.md        # learner profile (blank on main; real data on maddy-learning)
├── materials/
│   └── <slug>/
│       ├── source/               # raw .tex / PDF / pptx + extracted slide images
│       ├── material.md           # clean markdown + LaTeX, the reading copy
│       ├── notation.md           # confirmed symbol table
│       ├── flags.md              # unreadable / low-confidence / context-not-found
│       ├── assumptions.md        # preconditions each key result relies on
│       ├── context.md            # lineage, positioning, related work
│       ├── verify.md             # what the maths checks found
│       ├── refs/                 # fetched arXiv sources for flagged-equation reconciliation
│       ├── onepager.pdf          # the deliverable
│       └── qa/                   # Q&A logs (.md + rendered .html)
└── README.md
```

---

## Learner profile (adaptive, toggleable)

A repo-level `profile/maths-background.md` records concepts on a **mastery ladder** that
separates mechanics from intuition — `unseen → seen → followed → applied → intuitive` —
with an optional per-concept `target`, a confidence, provenance (self-reported vs
demonstrated), and a last-updated date. The key distinction is `followed` (worked through
the definition, can reproduce it) vs `intuitive` (can relate it to your own work): a
concept can be mechanically understood yet not yet transferable. Its header carries
`learning_mode: on|off` — turning it off disables all probing and adaptation and restores
plain processing.

Populated two ways, both writing to the same ledger:

- **Per-ingestion probe.** After stage 2 extracts the concept list, it's diffed against
  the profile and you get **one batched multi-select** covering only concepts not already
  recorded. Early on this asks a lot; as the ledger fills it shrinks toward nothing.
- **Conversational.** During Phase B the session infers your level from how you ask, and
  moves items up the ladder (dated) when you signal understanding — e.g. `followed →
  intuitive` once you can relate a concept to your own work — no explicit quiz.

What the profile drives (all on):

- **Explanation depth** — Phase B skips the known, expands the unknown.
- **Prerequisite-gap warnings** — at ingestion, flags results that lean on `not-yet`
  concepts, so you see the gap before you read.
- **Derivation-expansion default** — stage 5's granularity is set from the profile rather
  than asked each time.
- **Suggested learning order** — when gaps exist, recommends which missing concept to
  shore up first, by what it unlocks.

**Packaging / privacy.** `main` ships a **blank template** profile so the repo is
shareable. Your real profile lives on a **`maddy-learning` branch**, kept private via
GitHub's access controls; pull improvements forward from `main` as the tool evolves.

---

## The Claude Project at the root

`CLAUDE.md` at the repo root is the **Phase B** brief — the instructions the cowork
comprehension session runs under. It tells Claude to:
- treat `materials/<slug>/` as the ground truth, reading `material.md`, `notation.md`,
  `context.md`, `verify.md`, `assumptions.md` before answering;
- cite slide numbers / section / equation numbers in every answer;
- render maths inline as HTML/MathJax artifacts, never as raw terminal text;
- read `profile/maths-background.md` and pitch explanation depth to it, updating the
  ledger conversationally as you demonstrate or declare understanding;
- relate the material to your existing notes and active projects.

This is distinct from the `.claude/skills/` used at build time (Phase A).

---

## Fidelity safeguards

- **Boldedness:** source-first avoids it entirely; conversion path uses LaTeX-emitting
  tools; notation pass enforces the vector/matrix convention and flags doubt.
- **Trust the maths:** sympy verification catches typos and skipped steps.
- **Honesty about failure:** `flags.md` is a first-class output — including "context
  could not be established" for orphan materials.
- **One-page guarantee:** compile-and-check, not vibes.
- **Small notes:** the Zettelkasten entry is a lean source note, not a dumped summary.
- **Traceability:** every answer references a location in `material.md`.

---

## Packages

`latexpand` + a LaTeX toolchain (a single-binary compiler is lightest), a math-aware PDF
converter, `python-pptx` for slide extraction (plus a headless converter for slide
images), a docx→markdown converter, `requests` (Semantic Scholar), `sympy`, and a static
file server if you want terminal-phase HTML rendering. You'll handle installation.

---

## Decided

- **Type routing** — auto-detect, then a **prompt at the start of each run** to confirm or
  override the profile and optionally supply author / research-group / source hints.
- **One-pager templates** — I design both the paper layout and the tutorial-digest layout.
- **Learner profile** — toggleable adaptive profile; per-ingestion probe of new concepts
  *plus* conversational updates; drives explanation depth, prerequisite-gap warnings,
  derivation-expansion default, and suggested learning order. `main` ships blank; real
  data on a `maddy-learning` branch kept private via GitHub access controls.
- **Notation confirmation** — **flag-driven**: interactive confirmation only where the
  converter flags low confidence. The near-lossless arXiv source path isn't quizzed.

## Open questions / next steps

1. **Source notes folder path** *(TODO, non-blocking)* — the Zettelkasten source note
   (stage 8) needs a destination path and your source-note format/template. Deferred; the
   `expand-derivation`/one-pager stages don't depend on it.
2. **Scaffold** — lay down the skills, script stubs (with logic sketched), the two
   templates, `profile/maths-background.md`, `CLAUDE.md`, and README; `git init`, commit
   the blank template on `main`, and cut the `maddy-learning` branch.
```