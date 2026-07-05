# Human Sovereignty Eval V1

A reproducible benchmark for evaluating whether AI assistance preserves human authority, understanding, judgment, and reversibility.

This benchmark is synthetic only. It does not evaluate private systems, execute tools, call models, certify safety, or claim to measure human flourishing in full.

## What It Tests

- human authority preserved
- human understanding increased
- human judgment supported
- human agency not bypassed
- appropriate friction preserved
- delegation visible
- reversibility available
- claim evidence linked
- dependency risk disclosed
- capability growth supported

## Run Locally

From the repository root:

```bash
python3 human_sovereignty_eval_v1/evaluator/report.py \
  --input human_sovereignty_eval_v1/examples/sample_agent_outputs.json \
  --output human_sovereignty_eval_v1/reports/sample_report.md

pytest
```

## Expected Result

The sample benchmark should produce:

```text
benchmark: human_sovereignty_eval_v1
score: 100
grade: A
passed: 5
failed: 0
```

## Public Boundary

This benchmark intentionally excludes:

- real private data
- real user records
- real clinical, educational, employment, or customer evaluations
- private prompts or schemas
- production architecture
- deployment evidence
- claims of measuring human flourishing completely
- claims of production safety certification

See [CLAIMS_AND_LIMITATIONS.md](CLAIMS_AND_LIMITATIONS.md) for claim boundaries.
