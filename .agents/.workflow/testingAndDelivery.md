# Testing and delivery gates — PLAN-080

Workflow: DISCOVER → SPECIFY_PLAN → IMPLEMENT → VERIFY → HANDOFF_REVIEW.

Each stage has a machine-checkable preflight, explicit transition events, and external approval where necessary. Workflow Guard never invokes shell commands, Spec Kit stage executors, Git writes or tests. It cannot issue approval or PASS evidence for an external system.

Maintain deterministic test evidence with command, exit code, environment/platform, source snapshot and required assertions. Report PASS/FAIL/BLOCKED/SKIP/NOT_RUN accurately. Re-run affected validation if requirements, source or configuration changed. Failure during VERIFY returns to IMPLEMENT only by an explicit recorded transition; retain failure evidence.

Release requires real regression in the development repository and disposable host installations. Test source changes follow the host's policy; Gymuro's separate feature/test commit convention is not universally mandatory. Record rollback steps and preserve machine/human handoff ownership.

## PLAN-081 agent evidence requirements

The agent's own text or a machine event cannot independently certify a test or grant approval. For every verification claim record the exact command, platform, revision, relevant result and skipped scenarios; distinguish `PASS`, `FAIL`, `BLOCKED`, `NOT RUN` and `SKIPPED`. A static GitHub source review is not a local test. CI on the precise commit establishes compatibility only for exercised tests; security and migration risks need separate evidence or explicit authorized risk acceptance.

Do not mark a task closed from `workflow_guard.py` on PR #7: its CLOSE scope, phase policy routing, post-VERIFY input invalidation and scope-free status issues are unresolved. Missing gate integrity means `NEEDS_REVIEW`/BLOCKED or a documented limitation, not a fabricated successful end-to-end transition. Follow the [agent runbook](agentRunbook.md) and [security roles](agentRoles.md).

## STOP evidence is not delivery evidence

A STOP handoff summarizes **partial** work and may leave a local session ACTIVE. It must identify current phase, source revision, actual modified paths, pending ACs, evidence freshness, author/ownership uncertainty, risk and a verified persistence flag. It does not turn incomplete tests into PASS or waive independent approval. Do not call `session_guard finish/merge` or Workflow Guard `close` as a STOP implementation. See the [specification](workflowSpecification.md), [STOP protocol](stopAndHandoff.md), [handoff template](../../.source/references/stop-handoff-template.md) and [RTM](../.traceMatrix.md).
