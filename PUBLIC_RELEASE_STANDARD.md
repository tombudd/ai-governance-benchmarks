# Public Release Standard

This repository should meet a high-trust public release bar before it is treated as portfolio-ready.

The internal goal is maximum credibility without exposing private systems. Publicly, that means every artifact should be reproducible, bounded, redacted, and evidence-first.

## Release Criteria

A public artifact should satisfy all of the following:

1. **Clear scope** — the artifact states what it does and what it does not prove.
2. **Reproducible path** — a reviewer can run or inspect the artifact without private access.
3. **Synthetic or public data only** — no private logs, receipts, prompts, schemas, or operational details.
4. **Evidence before claims** — claims are supported by code, examples, reports, or explicit methodology.
5. **Limitations included** — the artifact explains where the benchmark can fail or mislead.
6. **Redaction boundary preserved** — no proprietary architecture, internal labels, private codenames, or production traces.
7. **Security checked** — no secrets, credentials, personal data, tokens, or private metadata.
8. **Independent-review friendly** — a skeptical reviewer can understand the method without needing private context.

## Minimum Artifact Checklist

Before an artifact is promoted as public portfolio material, it should include:

- `README.md` section describing purpose, scope, and limitations
- Reproducible example or clearly marked roadmap status
- Synthetic input fixture, if data is needed
- Expected output or sample report, if evaluation is involved
- Clear license
- Redaction review
- Security review

## Claim Discipline

Avoid claims such as:

- "proves safety"
- "guarantees alignment"
- "production-ready"
- "autonomous deployment safe"
- "verified governance" without independent reproduction

Prefer claims such as:

- "demonstrates a toy evaluation method"
- "provides a clean-room scoring rubric"
- "shows a reproducible example under bounded assumptions"
- "supports independent review of one governance property"

## Promotion Rule

Documentation-only artifacts are acceptable as public methodology, but they should not be described as implemented benchmarks until executable files, fixtures, and sample outputs exist.

Runnable artifacts should include tests where practical.

## Public Boundary

The public repository is not the private system. It is a safe demonstration layer.

When a private method is useful, publish only the clean-room abstraction, toy example, or synthetic benchmark.