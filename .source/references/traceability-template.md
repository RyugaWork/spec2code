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

## PLAN-109 / M07 — Trace template evidence columns

A feature trace row needs `requirementId, approvedRequirementRevision, ACIdOrPending, featureId, designContract, producerConsumer, taskId, testCaseId, fixtureHash, actualResult, riskIds, ownerDecisionRef, sourceSha`. Use `AC_PENDING` where product metrics have not been accepted, not an invented stable AC ID. Distinguish `DESIGNED/NOT_RUN` from measured PASS and distinguish an author reviewer from independent A.1.

Reverse-trace each executable task back to an accepted requirement or an explicitly approved security/infrastructure obligation. Shared cases require separate statements of which BR semantics were actually proven. If source SHA or owner scope changes, flag impacted evidence STALE and preserve previous mapping. STOP/handoff makes status durable but cannot convert a test intent into a completed acceptance case.
