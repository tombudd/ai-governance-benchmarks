# Scope Notes

This repository contains small public benchmarks for clean-room AI governance evaluation.

The included benchmarks use synthetic examples, deterministic rule-based scorers, expected reports, and tests. They are designed to make narrow governance claims inspectable.

## In Scope

- Synthetic benchmark cases
- Deterministic scoring rules
- Expected report fixtures
- Local test execution
- Eval factsheets
- Claims and limitations
- Anti-overclaim language checks

## Out of Scope

- Real user data
- Live model calls
- Real tool execution
- Private system evaluation
- Deployment evidence
- Compliance certification
- Complete coverage of agent safety

## Proper Use

Use this repository as a public proof-of-method artifact for reproducible governance evaluation patterns.

Do not treat passing results as broad safety evidence. The supported claim is narrower: the included synthetic cases run locally, score deterministically, and generate reproducible reports under the documented rubrics.
