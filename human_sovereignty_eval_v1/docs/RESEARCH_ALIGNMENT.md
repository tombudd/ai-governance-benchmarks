# Research Alignment

This benchmark connects agent safety evaluation with a human-sovereignty thesis: AI systems should be tested not only for whether they avoid harmful actions, but for whether they preserve human authority, strengthen human judgment, and avoid creating hidden dependency.

## Relevant Research Threads

### Human Agency And Meaningful Control

Work on meaningful human control argues that humans should not become nominal approvers of opaque automation. This benchmark operationalizes a small version of that concern by checking for visible delegation, review checkpoints, and reversibility.

### Human-Centered AI

Human-centered AI emphasizes systems that augment human capability rather than replacing human judgment. This benchmark scores whether a response explains tradeoffs, supports decision-making, and leaves the human better positioned to act next time.

### Capability And Flourishing-Oriented Evaluation

Capability-oriented ethics asks what people are able to do and become. This benchmark does not measure flourishing directly, but it tests response signals related to authority, understanding, judgment, and capability growth.

### Agent Safety And Auditability

Agent-safety work increasingly focuses on behavior in interactive contexts, tool-use risk, and long-horizon reliability. `human_sovereignty_eval_v1` adds a complementary question: even when an assistant is safe and useful, does it keep the human in the loop in a way that is visible, reversible, and evidence-linked?

## Claim Boundary

This benchmark does not claim clinical validity, production certification, complete flourishing measurement, or universal alignment. It is a narrow public fixture for testing whether synthetic assistant responses contain human-sovereignty support signals.
