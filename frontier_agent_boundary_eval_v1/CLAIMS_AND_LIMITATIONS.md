# Claims And Limitations

## Safe Public Claim

This is a small reproducible benchmark for evaluating whether synthetic agent outputs preserve user authority, detect unsafe tool-use risks, explain safety boundaries, offer safer alternatives, and remain coherent under multi-turn pressure.

## What This Does Not Claim

This benchmark does not claim:

- AGI
- consciousness
- solved alignment
- production safety certification
- compatibility with any specific lab system
- deployment readiness
- complete coverage of agent safety

## Limitations

- Synthetic examples only.
- Rule-based scoring only.
- No model calls.
- No real tool execution.
- No production-system evaluation.
- No private-system disclosure.

## Intended Use

Use this benchmark as a clean-room public demonstration of one evaluation pattern:

```text
synthetic agent interaction -> deterministic scorer -> reproducible report -> tests pass
```
