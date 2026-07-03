# Hiring Proof Map

This repository is a clean-room public proof artifact for AI governance and evaluation work. It is designed to show that the work can be inspected, run, tested, and reviewed without exposing private systems or proprietary architecture.

## Best Public Framing

```text
A clean-room public benchmark prototype for evaluating AI governance behavior, starting with synthetic Constitutional Adherence and Accountability Completeness tests.
```

## What This Repository Demonstrates

- Reproducible AI evaluation workflows
- Synthetic benchmark design
- Rule-based governance scoring
- Expected report fixtures
- Pytest verification
- GitHub Actions CI
- Redaction and public disclosure discipline

## Role Fit

### AI Safety / Governance

Relevant proof:

- Synthetic Constitutional Adherence benchmark
- Synthetic Accountability Completeness benchmark
- Public redaction boundary
- Limitations that avoid safety overclaiming

This shows practical governance evaluation work: bounded inputs, deterministic scoring, expected outputs, and explicit caveats.

### AI Evaluation Engineering

Relevant proof:

- `evaluation/runner.py`
- `evaluation/scorer.py`
- `evaluation/report.py`
- `examples/expected_report.json`
- `examples/expected_accountability_report.json`
- `tests/test_sample_benchmark.py`

This shows an inspectable test harness with local reproducibility and CI verification.

### AI Workflow / Controls

Relevant proof:

- Synthetic receipt fixtures
- Reconstructability checks
- Review-path fields
- Public boundary checks

This shows how workflow evidence can be represented and tested with fake public data.

### Technical Program / Responsible AI

Relevant proof:

- README limitations
- Public boundary section
- `PUBLIC_RELEASE_STANDARD.md`
- `REDACTION_POLICY.md`
- CI-backed runnable examples

This shows safety-conscious documentation, scope control, and implementation discipline.

## How To Use This In Applications

Use a specific proof artifact instead of a generic GitHub link:

```text
Relevant proof artifact: github.com/tombudd/ai-governance-benchmarks

This is a clean-room AI governance benchmark showing synthetic inputs, a reproducible local runner, rule-based scoring, expected reports, pytest verification, and GitHub Actions CI. It demonstrates how I approach AI evaluation, auditability, and public safety boundaries.
```

## Safe Public Claim

```text
I published a clean-room AI governance benchmark repository with synthetic Constitutional Adherence and Accountability Completeness benchmarks, reproducible local runners, rule-based scorers, expected reports, pytest verification, and GitHub Actions CI.
```

## Claims To Avoid

Do not claim that this repository:

- proves AI safety
- proves alignment
- evaluates production systems
- validates private governance architecture
- contains private system prompts, private logs, real receipts, or proprietary architecture

## Public Boundary

This repository uses synthetic examples only. It does not include private system prompts, production logs, customer data, proprietary architecture, internal governance labels, or deployment details.
