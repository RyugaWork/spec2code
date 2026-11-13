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

## PLAN-085 independent validation loops

The [validation specification](validationSpecification.md) separates **A.1 design validation** (requirements authority, RTM, design, safety, risk and handoff consistency) from **B.1 system acceptance validation** (actual approved behavior, integration, adversarial security, migration/recovery, user/host acceptance on an exact implementation SHA). The [validation report template](validationReportTemplate.md) tracks PASS/FAIL/BLOCKED/NOT_RUN/N/A per criterion and an independent reviewer. A.1 FAIL blocks B; B.1 FAIL blocks release and returns to B or A when design changes. Current planning-stage document checks and existing Python CI are **not** A.1/B.1 outcomes. No change to machine stage enum or runtime test behavior.
