# Tasks: Spec Kit Integration for S2C

**Feature:** [spec.md](spec.md) | [plan.md](plan.md)  
**Status:** DRAFT_TASKS; checkboxes are **authoring status only**, not automatic B-phase authorization or runtime test PASS.  
**Work branch:** `docs/plan-089-a1-readiness`. Spec Kit feature identity is bound by `.specify/feature.json`, **not** this branch name.

## Phase 1 — Web/GitHub bootstrap (documentation; no code execution)

- [ ] T001 Create a draft project constitution at `.specify/memory/constitution.md` that respects root AGENTS and the master BRD.
- [ ] T002 Select `specs/001-s2c-speckit-integration` in `.specify/feature.json` without creating a Git feature branch.
- [ ] T003 Author this feature's `spec.md`, `plan.md`, `tasks.md`, and an explicit quality checklist; map to S2C BR/REQ/AC.
- [ ] T004 Update S2C AGENTS, RTM, plans/risk, adapter guide and README to support Web and native modes without duplicating BRD.
- [ ] T005 Static-check the JSON pointer, repository-contained paths, task ID format, uniqueness, documentation links, and Git diff against the pre-integration HEAD.

## Phase 2 — Official CLI preparation (separate reviewed execution)

- [ ] T006 Select and verify a mature supported official Spec Kit release, installation source/tag, hash and CLI/agent integration.
- [ ] T007 In a disposable **local checkout**, back up any existing `.specify` and agent skill files; execute official `specify init --here --force --non-interactive --integration <approved-key> --script py` only with explicit authorization; inspect generated diff.
- [ ] T008 Prove official skills/scripts exist and work in the selected coding agent; capture actual `specify version`, pointer, stage and platform evidence.
- [ ] T009 Reconcile official generated templates/scripts and feature pointer without overwriting owner content; separately review any proposed integration into this working branch.

## Phase 3 — Independent design validation (before any B code task)

- [ ] T010 Reconcile master BRD, Google stakeholder revision, Constitution, feature AC, RTM, risk and exact Git SHA.
- [ ] T011 Obtain actual independent A.1 report (`A1-VAL-01..09`) and source-bound signoff. Report P0/P1 risks explicitly; do not infer PASS from markdown creation.
- [ ] T012 Record a separately approved B task and scope for any adapter, CLI/script, config, security, or host-source modifications.

## Phase 4 — Future authorized implementation and acceptance

- [ ] T013 Implement only approved bridge/runtime enhancements and regression tests on exact source revisions; reject missing or unsafe paths.
- [ ] T014 Validate on disposable representative hosts (Windows/OneDrive/junction, Linux, without Spec Kit, with official CLI), capture logs, source hashes and actual results.
- [ ] T015 Obtain independent B.1 and release/merge authorization; preserve handoff, migration and rollback evidence.

## Dependencies

T001–T005 (documentation bootstrap) → T006–T009 (approved native pilot) → T010–T012 (independent gate and explicit permission) → T013–T015 (future implementation/acceptance). Actual CLI may be installed *for development verification in an authorized disposable environment* before A.1, but **must not use that as permission to mutate product/host code**.

## STOP / RESUME

Record `feature_directory`, exact current Git SHA, completed task checkboxes with evidence, Google revision, next smallest safe action and known uncertainty. On RESUME re-check `.specify/feature.json` and consulted policy/source; never call runtime `close` merely because writing stopped.
