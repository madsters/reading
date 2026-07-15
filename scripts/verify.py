#!/usr/bin/env python3
"""Symbolic/numeric verification harness for load-bearing equations.

The trust layer. For each equation the user flags as important, run whichever of
these apply and record the result to verify.json (the skill renders verify.md):

  * rederive    — simplify(lhs - rhs) under the given substitutions; a nonzero
                  residual is a discrepancy (catches factor-of-2 typos etc.);
  * dimensions  — substitute each symbol's unit and compare dimensional exprs;
  * indices     — free-index balance across terms and both sides;
  * limits      — evaluate declared cases / symbolic limits numerically.

Each check returns pass | discrepancy(detail) | not-applicable | error, so
verify.json is an honest ledger. Content-triggered: runs whenever there's maths.

Spec (materials/<slug>/checks.json) is a list of steps, e.g.:
  [{"eq_ref": "eq. 14",
    "checks": ["rederive", "dimensions", "limits"],
    "lhs": "F", "rhs": "m*a",
    "substitutions": {"F": "m*a"},
    "dimensions": {"F": "newton", "m": "kilogram", "a": "meter/second**2"},
    "cases": [{"expr": "sin(x)/x - 1", "subs": {"x": 1e-6}, "expected": 0}],
    "limit": {"expr": "sin(x)/x", "var": "x", "to": 0, "expected": 1},
    "lhs_indices": "A_ij B_jk", "rhs_indices": "C_ik"}]

    python verify.py --spec materials/<slug>/checks.json --out materials/<slug>
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import sympy
from sympy.physics import units as u
from sympy.physics.units.systems.si import SI, dimsys_SI

NA = {"status": "not-applicable"}
TOL = 1e-6

# Keep genuine constants; everything else (incl. E, I, N, S, Q...) is a variable.
_CONST_KEEP = {"pi", "oo", "zoo", "nan"}


def _parse(expr: str):
    """sympify, but force bare identifiers to Symbols so physics variables named
    E, I, N, ... aren't captured as sympy built-in constants. Function names
    (anything followed by '(') are left alone so sin/exp/log still work."""
    names = set(re.findall(r"[A-Za-z_]\w*", expr))
    funcs = set(re.findall(r"([A-Za-z_]\w*)\s*\(", expr))
    local = {n: sympy.Symbol(n) for n in (names - funcs) if n not in _CONST_KEEP}
    return sympy.sympify(expr, locals=local)


def rederive(step: dict) -> dict:
    if "lhs" not in step or "rhs" not in step:
        return NA
    try:
        subs = {sympy.Symbol(k): _parse(v) for k, v in step.get("substitutions", {}).items()}
        residual = sympy.simplify(_parse(step["lhs"]).subs(subs) - _parse(step["rhs"]).subs(subs))
        if residual == 0:
            return {"status": "pass"}
        return {"status": "discrepancy", "detail": f"residual lhs-rhs = {residual}"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


def check_dimensions(step: dict) -> dict:
    dims = step.get("dimensions")
    if not dims or "lhs" not in step or "rhs" not in step:
        return NA
    try:
        subs = {sympy.Symbol(k): sympy.sympify(v, locals=vars(u)) for k, v in dims.items()}
        dl = SI.get_dimensional_expr(_parse(step["lhs"]).subs(subs))
        dr = SI.get_dimensional_expr(_parse(step["rhs"]).subs(subs))
        # Reduce both to base dimensions (so 'force' == 'mass*length/time**2').
        base_l = dimsys_SI.get_dimensional_dependencies(dl)
        base_r = dimsys_SI.get_dimensional_dependencies(dr)
        if base_l == base_r:
            return {"status": "pass", "detail": f"both sides ~ {dict(base_l)}"}
        return {"status": "discrepancy",
                "detail": f"lhs {dict(base_l)} != rhs {dict(base_r)}"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


def _free_sets(expr: str) -> list[list[str]]:
    """Free indices per additive term. Index letters live after '_'; a letter
    appearing once in a term is free, repeated (twice) is summed (bound)."""
    terms = re.split(r"(?<![eE\^])[+\-]", expr)
    out = []
    for term in terms:
        if not term.strip():
            continue
        letters = []
        for grp in re.findall(r"_([A-Za-z]+)", term):
            letters.extend(list(grp))
        counts = Counter(letters)
        out.append(sorted(k for k, v in counts.items() if v == 1))
    return out


def check_indices(step: dict) -> dict:
    if "lhs_indices" not in step or "rhs_indices" not in step:
        return NA
    try:
        lhs_terms = _free_sets(step["lhs_indices"])
        rhs_terms = _free_sets(step["rhs_indices"])
        all_terms = lhs_terms + rhs_terms
        first = all_terms[0]
        bad = [t for t in all_terms if t != first]
        if bad:
            return {"status": "discrepancy",
                    "detail": f"inconsistent free indices; expected {first}, saw {bad}"}
        return {"status": "pass", "detail": f"free indices balanced: {first}"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


def _close(a, b) -> bool:
    return abs(float(a) - float(b)) <= TOL * max(1.0, abs(float(b)))


def check_limits(step: dict) -> dict:
    cases, lim = step.get("cases"), step.get("limit")
    if not cases and not lim:
        return NA
    results = []
    try:
        for c in cases or []:
            subs = {sympy.Symbol(k): v for k, v in c.get("subs", {}).items()}
            val = complex(_parse(c["expr"]).subs(subs).evalf())
            val = val.real if abs(val.imag) < TOL else val
            ok = _close(val, c.get("expected", 0))
            results.append({"expr": c["expr"], "value": str(val),
                            "expected": c.get("expected"), "ok": ok})
        if lim:
            val = sympy.limit(_parse(lim["expr"]), sympy.Symbol(lim["var"]), lim["to"])
            ok = _close(val, lim["expected"])
            results.append({"limit": lim["expr"], "value": str(val),
                            "expected": lim["expected"], "ok": ok})
        status = "pass" if all(r["ok"] for r in results) else "discrepancy"
        return {"status": status, "detail": results}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


CHECKS = {"rederive": rederive, "dimensions": check_dimensions,
          "indices": check_indices, "limits": check_limits}


def run(spec: Path, out: Path) -> dict:
    steps = json.loads(spec.read_text())
    results = []
    for step in steps:
        res = {name: CHECKS[name](step) for name in step.get("checks", []) if name in CHECKS}
        results.append({"eq_ref": step.get("eq_ref"), "results": res})
    out.mkdir(parents=True, exist_ok=True)
    dest = out / "verify.json"
    dest.write_text(json.dumps(results, indent=2))
    return {"written": str(dest), "n": len(results)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    print(json.dumps(run(args.spec, args.out), indent=2))


if __name__ == "__main__":
    main()
