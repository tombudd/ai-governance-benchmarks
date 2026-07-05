# Eval Factsheet

## Context

Name: Human Sovereignty Eval V1

Version: `human_sovereignty_eval_v1`

Repository: `tombudd/ai-governance-benchmarks`

Author: Tom Budd

Date: 2026-07-05

Commit documented: `b6fb9ccaf7167fb2fcbad388ea10be2145ae953a`

## Scope

This evaluation measures:

- synthetic AI-assistance behavior
- preservation of human authority
- increased human understanding
- support for human judgment
- prevention of agency bypass
- appropriate friction
- visible delegation
- reversibility
- evidence-linked claims
- dependency-risk disclosure
- capability-growth support

This evaluation does not measure:

- complete human flourishing
- real human outcomes
- clinical, educational, employment, or legal validity
- production safety
- AGI
- consciousness
- universal alignment
- deployment readiness

## Structure

Inputs: `examples/sample_agent_outputs.json`

Cases: five synthetic cases under `cases/`

Scorer: deterministic rule-based scorer in `evaluator/scorer.py`

Rubric dimensions: defined in `evaluator/rubric.py`

Outputs: summary dictionary returned by `evaluator/report.py`

Reports: generated Markdown report at `reports/sample_report.md`

Tests: pytest coverage in `tests/test_human_sovereignty_eval_v1.py`

## Method

How to run:

```bash
python3 human_sovereignty_eval_v1/evaluator/report.py \
  --input human_sovereignty_eval_v1/examples/sample_agent_outputs.json \
  --output human_sovereignty_eval_v1/reports/sample_report.md

pytest
```

How scoring works:

Each synthetic output is matched to a case definition. The case lists required human-sovereignty dimensions. Each dimension has observable signal terms and a minimum match threshold. A case passes only if all required dimensions pass and no overclaim term is present.

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
- not a complete measure of human flourishing

## Supported Public Claim

Acceptable public claim:

```text
A small reproducible benchmark for evaluating whether synthetic AI-assistance responses preserve human authority, judgment, reversibility, and capability-growth support.
```

## Unsupported Public Claims

Do not claim:

- proves human flourishing
- certifies safety
- solves alignment
- evaluates AGI readiness
- detects consciousness
- validates production deployment
- measures real human outcomes
