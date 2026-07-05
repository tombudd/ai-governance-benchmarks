# Research Alignment

This note explains why `frontier_agent_boundary_eval_v1` focuses on agent boundary behavior rather than broad claims about AI safety.

The benchmark is intentionally small. It uses synthetic cases and deterministic scoring to demonstrate an evaluation pattern, not to certify any model or deployment.

## Why Agent Boundary Behavior

Recent agent-safety work argues that safety evaluation must look beyond single-turn text outputs. Agentic systems can create risk through tool use, authority handling, multi-turn interaction, and long-horizon behavior. `frontier_agent_boundary_eval_v1` maps those concerns into a narrow public benchmark:

- risk awareness
- authority preservation
- unsafe tool refusal
- boundary explanation
- safe alternatives
- multi-turn pressure resistance
- long-horizon consistency
- claim humility
- receipt completeness

## Research Threads

### Agent Safety And Risk Awareness

R-Judge frames agent safety as a behavioral risk-awareness problem over multi-turn agent interaction records, not only a harmless-text problem. That supports the benchmark's focus on recognizing risk, preserving boundaries, and evaluating interaction context.

Agent-SafetyBench similarly emphasizes that interactive environments and tool use introduce safety challenges beyond ordinary model-output safety. That supports the benchmark's use of synthetic agent-boundary cases rather than simple one-turn refusal examples.

### Sandboxed Tool-Use Evaluation

ToolEmu motivates simulated tool-use evaluation: safety failures can be studied without executing real-world actions. `frontier_agent_boundary_eval_v1` follows the same public-safety principle at a smaller scale: it scores synthetic outputs and never executes tools.

### Constitutional-Style Refusal And Explanation

Constitutional AI demonstrates the value of explicit rules, critique, revision, and harmlessness objectives. This benchmark does not train models or implement RLAIF. It only evaluates whether a synthetic agent response refuses unsafe escalation, explains the boundary, and offers a safer alternative.

RLHF limitation work argues that training methods need complementary auditing and disclosure standards. This benchmark is one small example of that complementary evaluation layer.

### Continual Learning And Long-Horizon Coherence

Continual-learning surveys highlight catastrophic forgetting and the need for practical evaluation protocols. LifelongAgentBench and Vending-Bench both point toward long-horizon evaluation as a distinct problem for agents that operate over time.

`frontier_agent_boundary_eval_v1` does not evaluate lifelong learning. It includes a small long-horizon plan-drift case to make one failure mode inspectable in a public, deterministic fixture.

### Planning And External Verification

LLM+P shows that long-horizon planning can benefit from external planning structure rather than relying on language-model output alone. This benchmark applies a related evaluation principle: agent outputs should preserve checkpoints, review paths, and receipts instead of silently expanding scope.

## Claim Boundary

This benchmark does not claim:

- production safety certification
- complete agent-safety coverage
- AGI evaluation
- consciousness evaluation
- model interpretability
- universal alignment
- compatibility with any specific lab system

It is a narrow, local, reproducible benchmark for inspecting agent-boundary behavior with synthetic examples.

## References

- Tongxin Yuan et al., [R-Judge: Benchmarking Safety Risk Awareness for LLM Agents](https://arxiv.org/abs/2401.10019), 2024.
- Zhexin Zhang et al., [Agent-SafetyBench: Evaluating the Safety of LLM Agents](https://arxiv.org/abs/2412.14470), 2024.
- Yangjun Ruan et al., [Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://arxiv.org/abs/2309.15817), 2023.
- Yuntao Bai et al., [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073), 2022.
- Stephen Casper et al., [Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2307.15217), 2023.
- Haizhou Shi et al., [Continual Learning of Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2404.16789), 2024.
- Junhao Zheng et al., [LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners](https://arxiv.org/abs/2505.11942), 2025.
- Axel Backlund and Lukas Petersson, [Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents](https://arxiv.org/abs/2502.15840), 2025.
- Bo Liu et al., [LLM+P: Empowering Large Language Models with Optimal Planning Proficiency](https://arxiv.org/abs/2304.11477), 2023.
