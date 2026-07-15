#!/usr/bin/env python3
"""Shared Docling conversion helper: file -> markdown + confidence flags.

Used by convert_pdf.py and convert_doc.py. Docling can recover formulae as LaTeX
(so boldedness/notation survive) — but only with formula enrichment turned ON,
which is off by default. We enable it here, since maths fidelity is the whole
point. OCR is toggleable: leave it on for scanned input, turn it off for
born-digital PDFs (a clean text layer) to save a lot of time.

Per-page confidence grades become an honest flags list rather than silent trust.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

# Grades Docling assigns; POOR/FAIR are worth surfacing to the user.
LOW_GRADES = {"POOR", "FAIR"}


def _build_converter(do_ocr: bool, do_formula: bool):
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    from docling.document_converter import DocumentConverter, PdfFormatOption

    opts = PdfPipelineOptions()
    opts.do_ocr = do_ocr
    opts.do_formula_enrichment = do_formula  # equations -> LaTeX (CodeFormulaV2)
    return DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
    )


def _confidence_flags(result) -> list[dict]:
    """Pull low-confidence pages out of Docling's ConfidenceReport, if present."""
    flags: list[dict] = []
    conf = getattr(result, "confidence", None)
    if conf is None:
        return flags
    pages = getattr(conf, "pages", None) or {}
    for pno, report in pages.items():
        grade = getattr(report, "mean_grade", None)
        name = getattr(grade, "name", str(grade)) if grade is not None else None
        if name and name.upper() in LOW_GRADES:
            flags.append({"page": pno, "kind": "low-confidence",
                          "reason": f"Docling layout/OCR grade: {name}"})
    return flags


def _heuristic_flags(md: str) -> list[dict]:
    """Cheap sanity checks on the markdown itself."""
    flags: list[dict] = []
    for i, line in enumerate(md.splitlines(), start=1):
        if line.count("$") % 2 == 1:
            flags.append({"line": i, "kind": "unbalanced-math",
                          "reason": "odd number of '$' on line",
                          "snippet": line.strip()[:120]})
        if re.search(r"[�]", line):
            flags.append({"line": i, "kind": "garbled",
                          "reason": "replacement characters present",
                          "snippet": line.strip()[:120]})
    return flags


def convert_with_docling(src: Path, out: Path, do_ocr: bool = True,
                         do_formula: bool = True) -> dict:
    """Convert `src` to out/material.md, writing out/flags.json. Returns paths."""
    out.mkdir(parents=True, exist_ok=True)
    result = _build_converter(do_ocr, do_formula).convert(str(src))
    md = result.document.export_to_markdown()

    md_path = out / "material.md"
    md_path.write_text(md)

    flags = _confidence_flags(result) + _heuristic_flags(md)
    flags_path = out / "flags.json"
    flags_path.write_text(json.dumps(flags, indent=2))

    return {"markdown_path": str(md_path), "flags_path": str(flags_path),
            "n_flags": len(flags), "do_ocr": do_ocr, "do_formula": do_formula}
