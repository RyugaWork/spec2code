# Testing and delivery gates — PLAN-080

Workflow: DISCOVER → SPECIFY_PLAN → IMPLEMENT → VERIFY → HANDOFF_REVIEW.

Each stage has a machine-checkable preflight, explicit transition events, and external approval where necessary. Workflow Guard never invokes shell commands, Spec Kit stage executors, Git writes or tests. It cannot issue approval or PASS evidence for an external system.

Maintain deterministic test evidence with command, exit code, environment/platform, source snapshot and required assertions. Report PASS/FAIL/BLOCKED/SKIP/NOT_RUN accurately. Re-run affected validation if requirements, source or configuration changed. Failure during VERIFY returns to IMPLEMENT only by an explicit recorded transition; retain failure evidence.

Release requires real regression in the development repository and disposable host installations. Test source changes follow the host's policy; Gymuro's separate feature/test commit convention is not universally mandatory. Record rollback steps and preserve machine/human handoff ownership.
