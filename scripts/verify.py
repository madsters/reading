#!/usr/bin/env python3
"""Symbolic/numeric verification harness for load-bearing equations.

The trust layer. For each equation the user flags as important, run whichever of
these apply and record the result to verify.md:

  * re-derive     — reconstruct the step symbolically with sympy and compare to
                    the paper's stated result (catches factor-of-2 typos etc.);
  * dimensions    — check dimensional consistency across the equation;
  * indices       — confirm free/bound indices balance on both sides;
  * limits        — evaluate limiting/edge cases numerically and sanity-check.

Each check returns pass | discrepancy(detail) | not-applicable, so verify.md is
an honest ledger, e.g. "re-derived eq. 14: factor-of-2 discrepancy in the second
term". Checks are content-triggered: this runs whenever there's maths, paper or
tutorial.

    python verify.py --spec materials/<slug>/checks.json --out materials/<slug>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def rederive(step: dict) -> dict:
    """sympy re-derivation of one step. Sketch: parse lhs/rhs + substitutions
    from `step`, simplify(lhs - rhs), report zero (pass) or the residual."""
    raise NotImplementedError


def check_dimensions(step: dict) -> dict:
    """Dimensional consistency via a units map on each symbol."""
    raise NotImplementedError


def check_indices(step: dict) -> dict:
    """Free/bound index balance across the equation."""
    raise NotImplementedError


def check_limits(step: dict) -> dict:
    """Numeric evaluation of declared limiting cases."""
    raise NotImplementedError


CHECKS = {"rederive": rederive, "dimensions": check_dimensions,
          "indices": check_indices, "limits": check_limits}


def run(spec: Path, out: Path) -> dict:
    """spec = [{eq_ref, checks:[...], ...}]; returns per-eq results."""
    steps = json.loads(spec.read_text())
    results = []
    for step in steps:
        results.append({
            "eq_ref": step.get("eq_ref"),
            "results": {name: "TODO" for name in step.get("checks", [])},
        })
    # TODO: dispatch each requested check via CHECKS and collect pass/discrepancy.
    out.mkdir(parents=True, exist_ok=True)
    (out / "verify.json").write_text(json.dumps(results, indent=2))
    return {"written": str(out / "verify.json"), "n": len(results)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    print(json.dumps(run(args.spec, args.out), indent=2))


if __name__ == "__main__":
    main()
