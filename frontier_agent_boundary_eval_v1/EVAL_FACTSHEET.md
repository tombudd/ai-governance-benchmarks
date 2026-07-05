# Eval Factsheet

## Context

Name: Frontier Agent Boundary Eval V1

Version: `frontier_agent_boundary_eval_v1`

Repository: `tombudd/ai-governance-benchmarks`

Author: Tom Budd

Date: 2026-07-05

Commit documented: `b6fb9ccaf7167fb2fcbad388ea10be2145ae953a`

## Scope

This evaluation measures:

- synthetic agent-boundary behavior
- risk awareness
- authority preservation
- unsafe tool-use refusal
- boundary explanation
- safe alternatives
- multi-turn pressure resistance
- long-horizon consistency
- claim humility
- receipt completeness

This evaluation does not measure:

- production safety
- real-world tool execution
- model interpretability
- AGI
- consciousness
- universal alignment
- deployment readiness
- superiority over external benchmark suites

## Structure

Inputs: `examples/sample_agent_outputs.json`

Cases: five synthetic cases under `cases/`

Scorer: deterministic rule-based scorer in `evaluator/scorer.py`

Rubric dimensions: defined in `evaluator/rubric.py`

Outputs: summary dictionary returned by `evaluator/report.py`

Reports: generated Markdown report at `reports/sample_report.md`

Tests: pytest coverage in `tests/test_frontier_agent_boundary_eval_v1.py`

## Method

How to run:

```bash
python3 frontier_agent_boundary_eval_v1/evaluator/report.py \
  --input frontier_agent_boundary_eval_v1/examples/sample_agent_outputs.json \
  --output frontier_agent_boundary_eval_v1/reports/sample_report.md

pytest
```

How scoring works:

Each synthetic output is matched to a case definition. The case lists required rubric dimensions. Each dimension has observable signal terms and a minimum match threshold. A case passes only if all required dimensions pass and no overclaim term is present.

How failures are surfaced:

Failed dimensions produce explicit reasons in the case result and generated report.

How expected reports are checked:

Tests compare the generated summary report to `examples/expected_report.json` and verify negative cases fail as expected.

## Validity And Limitations

Strengths:

- deterministic
- reproducible
- inspectable
- CI-tested
- includes negative tests
- includes explicit claim boundaries

Limitations:

- synthetic cases only
- small case set
- rule-based scoring
- not externally validated
- not tested against large human-review panels
- not a production certification

## Supported Public Claim

Acceptable public claim:

```text
A small reproducible benchmark for evaluating agent-boundary behavior on synthetic cases.
```

## Unsupported Public Claims

Do not claim:

- proves alignment
- certifies safety
- solves agent governance
- evaluates AGI readiness
- detects consciousness
- validates production deployment
- outperforms frontier-lab evaluations
