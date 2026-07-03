# Redaction Policy

This repository is a clean-room public research surface. It is designed to show governance methodology without exposing private systems, proprietary architecture, customer data, or internal operational details.

## Allowed Public Content

The repository may include:

- Toy examples
- Synthetic prompts
- Public scoring rubrics
- Fake or synthetic governance receipts
- Redacted methodology
- Non-production evaluation scripts
- Public research notes
- Clearly labeled roadmap items

## Prohibited Content

Do not commit:

- Private production logs
- Real deployment receipts
- Proprietary schemas
- Internal architecture diagrams
- System prompts from private systems
- Secret keys, tokens, credentials, or environment files
- Customer, partner, employee, or personal data
- Internal codenames, private governance labels, or private incident records
- Any file that reveals non-public system boundaries, routing, authority models, or runtime internals

## Review Rule

Before adding any artifact, ask:

1. Could this reveal how a private system works internally?
2. Could this help bypass a private governance boundary?
3. Could this expose confidential data, relationships, or operational practice?
4. Could a reviewer learn the method from a safer toy version instead?

If the answer to any of the first three is yes, do not publish it. Create a synthetic or redacted version instead.

## Preferred Pattern

Use this pattern for public artifacts:

```text
private method -> clean-room abstraction -> toy example -> public benchmark
```

Never publish the private method directly.