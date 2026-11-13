# Requirement-to-Code Traceability — <Feature ID>

| Requirement ID | Approval source/version | AC IDs | Design IDs | Task IDs | Changed code paths | Test IDs/evidence | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <R01> | <approved source> | <AC01> | <DES01> | <T001,T002> | <path/line or symbol> | <command/log> | NOT RUN |

Trace rules:
- Every implemented behavior must map to an approved requirement; every in-scope AC maps to implementation and verification evidence.
- Never treat a technical implementation proposal as authority to add a new business rule.
- Use PASS / FAIL / BLOCKED / NOT RUN, not unverified blanket PASS.
- Record change IDs when requirements, design or code diverge.

## System RTM and interruptible workflow linkage

The development repository's [System Requirements Traceability Matrix](../../.agents/.traceMatrix.md) is the concrete system-wide matrix mapping requirements/AC IDs, Fxx features, plan, source paths, existing test methods, trace status and gaps. This file remains a **portable feature-level template**, not a substitute for a current host's approved requirements.

For interrupted feature work, link the relevant requirement/AC IDs to a separate [STOP Handoff](stop-handoff-template.md) and keep its state `IN_PROGRESS`/`BLOCKED` as applicable. A STOP snapshot records work but **does not** satisfy the feature's acceptance criteria. Revalidate the host's current spec and tests before continuing.
