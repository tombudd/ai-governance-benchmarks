from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GUARD_TERMS = [
    "proves",
    "certifies",
    "guarantees",
    "solves alignment",
    "agi",
    "consciousness",
    "deployment-ready",
    "production-ready",
    "frontier-certified",
    "universal alignment",
]

ALLOW_CONTEXT_MARKERS = [
    "unsupported",
    "claims not made",
    "claims to avoid",
    "what this does not",
    "does not claim",
    "does not measure",
    "does not support",
    "do not claim",
    "avoid claims",
    "claim discipline",
    "public boundary",
    "limitations",
    "intentionally excludes",
    "must not",
    "does not prove",
    "not a",
    "not externally",
    "not production",
    "not validated",
]

CONTEXT_END_MARKERS = [
    "supported public claim",
    "supported claims",
    "proper citation language",
    "prefer claims",
    "acceptable public claim",
]


def public_claim_files() -> list[Path]:
    paths = [
        ROOT / "README.md",
        ROOT / "PROJECT_STATUS.md",
        ROOT / "PUBLIC_RELEASE_STANDARD.md",
        ROOT / "CONTRIBUTING.md",
    ]
    paths.extend(sorted((ROOT / "docs").glob("*.md")))
    for benchmark in [
        ROOT / "frontier_agent_boundary_eval_v1",
        ROOT / "human_sovereignty_eval_v1",
    ]:
        paths.extend(sorted(benchmark.glob("*.md")))
        paths.extend(sorted((benchmark / "docs").glob("*.md")))
        paths.extend(sorted((benchmark / "reports").glob("*.md")))
    return [path for path in paths if path.exists()]


def contains_guard_term(line: str) -> bool:
    normalized = line.lower()
    return any(term in normalized for term in GUARD_TERMS)


def starts_allow_context(line: str) -> bool:
    normalized = line.lower()
    return any(marker in normalized for marker in ALLOW_CONTEXT_MARKERS)


def ends_allow_context(line: str) -> bool:
    normalized = line.lower().lstrip("# ").strip()
    return any(normalized.startswith(marker) for marker in CONTEXT_END_MARKERS)


def test_public_claim_language_is_caveated() -> None:
    violations = []

    for path in public_claim_files():
        in_allowed_context = False
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            stripped = line.strip()
            if stripped.startswith("#"):
                in_allowed_context = starts_allow_context(stripped)
            elif ends_allow_context(stripped):
                in_allowed_context = False
            elif starts_allow_context(stripped):
                in_allowed_context = True

            if not contains_guard_term(stripped):
                continue

            if in_allowed_context or starts_allow_context(stripped):
                continue

            violations.append(f"{path.relative_to(ROOT)}:{line_number}: {stripped}")

    assert violations == []
