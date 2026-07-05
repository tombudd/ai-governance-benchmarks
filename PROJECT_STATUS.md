# Project Status

Current public status:

- Constitutional Adherence V1: verified
- Accountability Completeness V1: verified
- Frontier Agent Boundary Eval V1: verified
- Human Sovereignty Eval V1: verified
- Local runners: verified
- Tests: 21 passing
- Hiring Proof Map: published
- Data boundary: synthetic only
- Release: [v1.0.0](https://github.com/tombudd/ai-governance-benchmarks/releases/tag/v1.0.0)

Overview: [Evaluation Stack Overview](docs/EVALUATION_STACK_OVERVIEW.md)

## Verification Commands

```bash
python3 evaluation/runner.py --input examples/sample_model_outputs.json --output results/sample_report.json
python3 evaluation/runner.py --input examples/sample_accountability_receipts.json --output results/sample_accountability_report.json
python3 frontier_agent_boundary_eval_v1/evaluator/report.py --input frontier_agent_boundary_eval_v1/examples/sample_agent_outputs.json --output frontier_agent_boundary_eval_v1/reports/sample_report.md
python3 human_sovereignty_eval_v1/evaluator/report.py --input human_sovereignty_eval_v1/examples/sample_agent_outputs.json --output human_sovereignty_eval_v1/reports/sample_report.md
pytest
```

## Public Boundary

This repository is a clean-room public benchmark portfolio. It uses synthetic examples and fake public receipts only. It does not include proprietary systems, private logs, customer data, private prompts, real receipts, internal architecture, or deployment details.

## Safe Public Summary

```text
Clean-room AI governance benchmark portfolio with synthetic evaluation design, local reproducibility, rule-based scoring, expected reports, pytest verification, GitHub Actions CI, and public-safe documentation.
```
