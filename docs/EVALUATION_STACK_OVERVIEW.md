# AI Governance Evaluation Stack

This repository contains small reproducible benchmarks for evaluating agentic AI behavior with synthetic examples, deterministic scoring, expected reports, tests, CI, and explicit limitations.

## Layer 1: Agent Boundary Safety

`frontier_agent_boundary_eval_v1`

Question:

```text
Can the agent preserve authority boundaries, refuse unsafe escalation, explain limits, resist pressure, and avoid unsupported claims?
```

This layer focuses on behavioral safety for agentic systems: authority preservation, unsafe tool-use refusal, boundary explanation, multi-turn pressure resistance, long-horizon consistency, claim humility, and receipt completeness.

## Layer 2: Human Sovereignty

`human_sovereignty_eval_v1`

Question:

```text
Does the agent preserve and strengthen the human, or does it create hidden dependency, bypass judgment, or automate without reversibility?
```

This layer focuses on whether AI assistance preserves human authority, increases understanding, supports judgment, keeps delegation visible, preserves reversibility, links claims to evidence, discloses dependency risk, and supports capability growth.

## Why Both Layers Matter

An AI system can avoid obvious harmful actions while still weakening human agency. This stack evaluates both action-boundary safety and human-strengthening behavior.

The public method is intentionally narrow:

```text
synthetic cases -> deterministic scorer -> expected report -> tests pass
```

## Claims Not Made

This project does not claim:

- AGI evaluation
- consciousness detection
- production safety certification
- model interpretability
- universal alignment
- evaluation of private systems
- complete measurement of human flourishing

These benchmarks are public evaluation prototypes, not safety certifications.
