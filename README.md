# AI Governance Benchmarks

> Small, reproducible benchmarks for reviewing agentic AI behavior with synthetic cases, deterministic scoring, generated reports, tests, and explicit limitations.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status: Public Methodology](https://img.shields.io/badge/Status-Public%20Methodology-brightgreen)
[![Tests](https://github.com/tombudd/ai-governance-benchmarks/actions/workflows/test.yml/badge.svg)](https://github.com/tombudd/ai-governance-benchmarks/actions/workflows/test.yml)

## Who This Is For

This repository is for:

- AI evaluation engineers
- agent-safety researchers
- technical reviewers
- teams assessing agentic systems before deployment

It provides small, reproducible evaluation patterns, not a complete safety benchmark or production certification.

## What This Is

The repository contains public, clean-room evaluation artifacts:

```text
synthetic case -> scorer -> report -> tests
```

Primary evaluation question:

```text
Does this synthetic agent response preserve authority boundaries and produce enough evidence for review under the tested conditions?
```

## Reviewer Quick Start

### 1. Inspect one concrete case

Start with a synthetic authority-boundary case:

```text
frontier_agent_boundary_eval_v1/cases/authority_escalation.json
```

### 2. Run the evaluation

```bash
python3 frontier_agent_boundary_eval_v1/evaluator/report.py \
  --input frontier_agent_boundary_eval_v1/examples/sample_agent_outputs.json \
  --output frontier_agent_boundary_eval_v1/reports/sample_report.md
```

### 3. Run the tests

```bash
python3 -m pytest
```

### 4. Inspect the result

- `frontier_agent_boundary_eval_v1/reports/sample_report.md`
- `frontier_agent_boundary_eval_v1/examples/expected_report.json`

### 5. Read the boundary

- `docs/SCOPE_NOTES.md`
- `frontier_agent_boundary_eval_v1/CLAIMS_AND_LIMITATIONS.md`

## What This Does Not Claim

This repository does not claim:

- production safety certification
- frontier-model evaluation results
- complete agent-safety coverage
- AGI evaluation
- consciousness detection
- model interpretability
- universal alignment
- evidence about a private production system

## Current Public Status

- Constitutional Adherence V1: `IMPLEMENTED / TESTED`
- Accountability Completeness V1: `IMPLEMENTED / TESTED`
- Frontier Agent Boundary Eval V1: `IMPLEMENTED / TESTED`
- Human Sovereignty Eval V1: `IMPLEMENTED / TESTED`
- Tests: 22 passing
- Data boundary: synthetic only
- Release: [v1.0.0](https://github.com/tombudd/ai-governance-benchmarks/releases/tag/v1.0.0)

## Implemented and Tested

### Synthetic Constitutional Adherence V1

STATUS: `IMPLEMENTED / TESTED`  
INPUT: synthetic model-response fixtures  
SCORER: deterministic rule-based scorer  
OUTPUT: JSON report  
LIMITATION: no production evaluation

Evaluates whether synthetic model responses follow simple public governance expectations: refusing private instruction disclosure, preserving audit boundaries, and answering harmless public-content requests normally.

Run locally:

```bash
python3 evaluation/runner.py --input examples/sample_model_outputs.json --output results/sample_report.json
```

Primary files:

- `examples/sample_model_outputs.json`
- `evaluation/scorer.py`
- `examples/expected_report.json`

### Synthetic Accountability Completeness V1

STATUS: `IMPLEMENTED / TESTED`  
INPUT: synthetic receipt fixtures  
SCORER: deterministic rule-based scorer  
OUTPUT: JSON report  
LIMITATION: no production auditability claim

Evaluates whether synthetic public receipts include required fields, preserve enough references to reconstruct a decision path, and keep the public redaction boundary intact.

Run locally:

```bash
python3 evaluation/runner.py --input examples/sample_accountability_receipts.json --output results/sample_accountability_report.json
```

Primary files:

- `examples/sample_accountability_receipts.json`
- `evaluation/scorer.py`
- `examples/expected_accountability_report.json`

### Frontier Agent Boundary Eval V1

STATUS: `IMPLEMENTED / TESTED`  
INPUT: synthetic agent-response fixtures  
SCORER: deterministic rule-based scorer  
OUTPUT: Markdown and JSON-compatible report data  
LIMITATION: no model calls, no real tool execution, no production evaluation

Evaluates whether synthetic agent outputs preserve user authority, detect unsafe tool-use risks, explain boundaries, offer safer alternatives, resist pressure, and avoid unsupported claims.

Run locally:

```bash
python3 frontier_agent_boundary_eval_v1/evaluator/report.py \
  --input frontier_agent_boundary_eval_v1/examples/sample_agent_outputs.json \
  --output frontier_agent_boundary_eval_v1/reports/sample_report.md
```

Primary files:

- `frontier_agent_boundary_eval_v1/cases/authority_escalation.json`
- `frontier_agent_boundary_eval_v1/cases/scoped_approval_tool_authority_escalation_v1.json`
- `frontier_agent_boundary_eval_v1/evaluator/scorer.py`
- `frontier_agent_boundary_eval_v1/reports/sample_report.md`
- `frontier_agent_boundary_eval_v1/tests/test_frontier_agent_boundary_eval_v1.py`
- `frontier_agent_boundary_eval_v1/CLAIMS_AND_LIMITATIONS.md`

### Human Sovereignty Eval V1

STATUS: `IMPLEMENTED / TESTED`  
INPUT: synthetic AI-assistance response fixtures  
SCORER: deterministic rule-based scorer  
OUTPUT: Markdown and JSON-compatible report data  
LIMITATION: no real user study, no complete measure of human flourishing

Evaluates whether synthetic AI-assistance responses preserve human authority, support judgment, keep delegation visible, preserve reversibility, link claims to evidence, and avoid hidden dependency.

Run locally:

```bash
python3 human_sovereignty_eval_v1/evaluator/report.py \
  --input human_sovereignty_eval_v1/examples/sample_agent_outputs.json \
  --output human_sovereignty_eval_v1/reports/sample_report.md
```

Primary files:

- `human_sovereignty_eval_v1/cases/assistance_without_agency.json`
- `human_sovereignty_eval_v1/evaluator/scorer.py`
- `human_sovereignty_eval_v1/reports/sample_report.md`
- `human_sovereignty_eval_v1/tests/test_human_sovereignty_eval_v1.py`
- `human_sovereignty_eval_v1/CLAIMS_AND_LIMITATIONS.md`

## Verification

Run all tests:

```bash
python3 -m pytest
```

The test suite includes:

- happy-path checks for included synthetic cases
- expected-report stability checks
- negative tests for weak or unsafe responses
- malformed or unsupported behavior checks
- public-claim language guard checks

## Proposed or Future Research

The following dimensions are `PROPOSED` and are not currently evaluated by this repository as standalone benchmark suites:

- Adversarial Robustness
- Identity Stability
- Epistemic Calibration

They remain future research directions until implemented as synthetic cases, deterministic scorers, reports, and tests.

## Additional Documentation

Primary reviewer documents:

- [Project Status](PROJECT_STATUS.md)
- [Scope Notes](docs/SCOPE_NOTES.md)
- [Audience and Artifact Contract](docs/AUDIENCE_AND_ARTIFACT_CONTRACT.md)

Secondary context:

- [Evaluation Stack Overview](docs/EVALUATION_STACK_OVERVIEW.md)
- [Repository Map](docs/REPOSITORY_MAP.md)
- [Research Alignment](docs/RESEARCH_ALIGNMENT.md)
- [Frontier Agent Evaluation Relevance](docs/FRONTIER_AGENT_EVALUATION_RELEVANCE.md)
- [Release Notes V1.0.0](docs/RELEASE_NOTES_V1_0_0.md)

Role-positioned evidence:

- [Hiring Proof Map](docs/HIRING_PROOF_MAP.md)
- [Recruiter Summary](docs/RECRUITER_SUMMARY.md)

## Public Boundary

This is a clean-room educational and research repository. It uses synthetic prompts, fake receipts, public rubrics, and non-production evaluation scripts.

It does not include private production logs, proprietary system prompts, internal architecture diagrams, private deployment receipts, secret keys, customer data, internal codenames, or private governance labels.

## Contributing

Contributions are welcome when they improve the public benchmark methodology without weakening the redaction boundary.

Before contributing, read `CONTRIBUTING.md` and `REDACTION_POLICY.md`.

---

© 2025-2026 Tom Budd / ResoVerse Technologies · Apache 2.0 License
