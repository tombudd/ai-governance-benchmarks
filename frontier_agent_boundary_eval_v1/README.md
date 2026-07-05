# Frontier Agent Boundary Eval V1

A small reproducible benchmark for evaluating whether agentic AI systems preserve user authority, detect unsafe tool-use risks, explain safety boundaries, and maintain coherent behavior across multi-turn interactions.

This benchmark is synthetic only. It does not execute tools, call models, evaluate production systems, certify safety, or disclose private systems.

## What It Tests

- risk awareness
- authority preservation
- unsafe tool refusal
- boundary explanation
- safe alternative offered
- multi-turn pressure resistance
- long-horizon consistency
- claim humility
- receipt completeness

## Run Locally

From the repository root:

```bash
python3 frontier_agent_boundary_eval_v1/evaluator/report.py \
  --input frontier_agent_boundary_eval_v1/examples/sample_agent_outputs.json \
  --output frontier_agent_boundary_eval_v1/reports/sample_report.md

pytest
```

## Expected Result

The sample benchmark should produce:

```text
benchmark: frontier_agent_boundary_eval_v1
score: 100
grade: A
passed: 5
failed: 0
```

The generated report is deterministic for the included synthetic examples.

## Public Boundary

This benchmark intentionally excludes:

- real tool execution
- real private data
- real audit logs or receipts
- private prompts or schemas
- production architecture
- deployment evidence
- claims of solved alignment or production safety certification

See [CLAIMS_AND_LIMITATIONS.md](CLAIMS_AND_LIMITATIONS.md) for claim boundaries.
