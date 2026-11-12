# Spec2Code PLAN-080.1 — Governance / Core Development handoff

Date: 2026-11-13 (Asia/Ho_Chi_Minh)
Status: IN PROGRESS / Draft PR; NOT a stable release
Repository: RyugaWork/spec2code
Base branch: spec2code/InitialVersion_v0
Work branch: feat/governance-integration-v0.8.0
PR: https://github.com/RyugaWork/spec2code/pull/7

## Confirmed Git actions
- PR #6 v0.7.0 merged into target as `84fc0599b561fae3515467144e04f29b16b61940` after latest-head CI review.
- v0.8 was synchronized with target using two-parent merge `887867e85aaa9183dacf7087edfdeb35ef68c3f2`; no history rewriting or content conflict.
- PLAN-080.1 planning/risk entries were committed before code modifications.

## Implemented changes
- `.source/scripts/workflow_guard.py`: task description/path binding through SHA-256; actual task scoped Policy Resolver; snapshot hashes of root/nested AGENTS, relevant required/candidate policy docs and context pack; no raw task text persisted; reject cross-task state mutation and invalidation of the wrong phase.
- `.source/scripts/context_router.py`: do not write a new pack when governance is BLOCKED; expose NEEDS_REVIEW without losing METADATA_ONLY/NEEDS_EXPLICIT_PATH safety semantics. Keep existing CLI options, output fields and stage gate.
- `.source/tests/test_workflow_guard.py`: negative coverage for missing scoped security policy, nested AGENTS drift, changed task scope, invalid phase and missing implementation scope.
- `.source/tests/test_policy_resolver.py`: malformed host map, scoped policy enforcement without matching keywords, unrelated prefix behavior.
- `.source/tests/test_context_router.py`: blocked-policy pack preservation and NEEDS_REVIEW.
- `.source/tests/test_target_checkout_layout.py`: CLI chain and copied-bundle smoke on disposable target repository.
- `.source/SKILL.md`, `README.md`, `.agents/.workflow/README.md`, `.agents/.features.md`, `.agents/.plans.md`, `.agents/.risk.md` and `.agents/.checklist.md`: governance protocol, responsibilities, trace and acceptance.

## Test evidence and unresolved gates
- CI workflows on intermediate commits (e.g. `43270947996`) FAILED due to one existing regression test: sensitive metadata routing_status was changed from METADATA_ONLY to NEEDS_REVIEW. Do not erase or relabel this FAIL.
- Fix commit `615825d550a265891e75627c378696ccebbe1cbf` restores METADATA_ONLY precedence; full latest-head CI matrix verification is required.
- Tests in intermediate failure logs that cover copied-bundle and task-bound workflow show PASS individually. This is not equivalent to full matrix PASS.
- Independent reviewer approval and real Windows OneDrive/junction stress test: NOT RUN / OPEN.
- Legacy v0.6.x/v0.7 migration of existing session and handoff evidence requires manual backup/review; no migration was executed.

## Known residual security risks
R01/R36 Windows TOCTOU, R02/R06/R23 managed-path collisions, R07 verified deletion, R08 data leakage via cloud sync, R21-R25 legacy handoff/state migration, R43 compatibility, and non-authorizing review gates remain under tracked disposition. Path Guard is not an OS sandbox.

## Rollback
Revert isolated PLAN-080.1 commits through a reviewed PR. Never delete `s2c/`, `.agents/state/`, legacy `.handoffs/`, or application-owned files as a rollback shortcut. Finish existing active sessions using their matching installed version before migration.

## Merge policy
PR #7 stays Draft while CI, host installation validation, independent review and security acceptance are unresolved. Only report complete after verifying exact head SHA, CI job counts, and reviewer decisions. Do not authorize Git mutations, arbitrary shell, MCP transport or release by inference.
