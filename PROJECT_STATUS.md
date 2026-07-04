# Project Status

Current public status:

- Constitutional Adherence V1: verified
- Accountability Completeness V1: verified
- Local runners: verified
- Tests: 9 passing
- Hiring Proof Map: published
- Data boundary: synthetic only

## Verification Commands

```bash
python3 evaluation/runner.py --input examples/sample_model_outputs.json --output results/sample_report.json
python3 evaluation/runner.py --input examples/sample_accountability_receipts.json --output results/sample_accountability_report.json
pytest
```

## Public Boundary

This repository is a clean-room public benchmark portfolio. It uses synthetic examples and fake public receipts only. It does not include proprietary systems, private logs, customer data, private prompts, real receipts, internal architecture, or deployment details.

## Safe Public Summary

```text
Clean-room AI governance benchmark portfolio with synthetic evaluation design, local reproducibility, rule-based scoring, expected reports, pytest verification, GitHub Actions CI, and public-safe documentation.
```
