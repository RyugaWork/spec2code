# Tasks: Spec Kit Integration for S2C

**Feature:** [spec.md](spec.md) | [plan.md](plan.md)  
**Status:** DRAFT_TASKS; checkboxes are **authoring status only**, not automatic B-phase authorization or runtime test PASS.  
**Work branch:** `docs/plan-089-a1-readiness`. Spec Kit feature identity is bound by `.specify/feature.json`, **not** this branch name.

## Phase 1 — Web/GitHub bootstrap (documentation; no code execution)

- [x] T001 Create a draft project constitution at `.specify/memory/constitution.md` that respects root AGENTS and the master BRD.
- [x] T002 Select `specs/001-s2c-speckit-integration` in `.specify/feature.json` without creating a Git feature branch.
- [x] T003 Author this feature's `spec.md`, `plan.md`, `tasks.md`, and an explicit quality checklist; map to S2C BR/REQ/AC.
- [x] T004 Update S2C AGENTS, RTM, plans/risk, adapter guide and README to support Web and native modes without duplicating BRD.
- [x] T005 Static-check the JSON pointer, repository-contained paths, task ID format, uniqueness, documentation links, and Git diff against the pre-integration HEAD.

**Bootstrap evidence:** GitHub tree HEAD `ebdbd03f027a8e65ce5cde8ddc5ea0af5a1cad14` was read after authoring. `.specify/feature.json` parses to a contained `specs/` path, `spec.md`/`plan.md`/`tasks.md` exist, T001..T015 are unique and match the existing S2C bridge's `T\d{3,6}` convention, and 171 relative Markdown links from the relevant edited files resolve in the Git tree. This is a **read-only static GitHub inspection**, not Python bridge or native Spec Kit CLI test evidence. T001..T005 are document/bootstrap tasks only.

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

## SK-03 attempted native pilot — evidence register (2026-11-13)

- **Actual research:** upstream `v1.2.6` release and declared Python `>=3.11` support examined; latest `v1.4.0` security-hardening changes reviewed as a warning. Candidate `v1.2.6` is **not owner-approved**.
- **Actual local tools:** Python 3.13.5, Git 2.47.3 and `uv`; `specify` unavailable. `git ls-remote` could not resolve GitHub and `uvx --offline --from git+https://github.com/github/spec-kit.git@v1.2.6 specify version` failed with exit 1 because the Git dependency was unavailable. `specify init` was **NOT_RUN**.
- **Prepared runbook:** [SK-03 native pilot and acceptance matrix](../../.agents/.documents/specKitNativePilot.md) defines a disposable detached Git worktree, exact `--integration codex --script py` invocation, artifact hashes, candidate security review and per-case outcome evidence.
- **Current task statuses:** T006 = RESEARCHED / OWNER_SELECTION_PENDING, still unchecked. T007–T009 = NATIVE_NOT_RUN (network/runner unavailable), still unchecked. T010–T015 = independent review/code/host tests NOT_RUN/NOT_AUTHORIZED.
- **Next safe action:** run the official pinned tool in a network-enabled authorized disposable Codespaces/Codex checkout, preserve the generated diff, then obtain actual owner authorization to adopt any artifacts. No new branch or CI workflow.

## PLAN-094 — Spec Kit template-completeness continuation (no new task IDs)

T003/T004/T005 documentation and preflight scope now also includes the standard Spec Kit feature supporting artifacts: [research](research.md), [logical data model](data-model.md), [Web/Native interface contract](contracts/web-native-interface.md), [quickstart](quickstart.md) and [24-case acceptance design](checklists/integrationAcceptance.md). The feature [specification](spec.md) includes explicit success criteria and assumptions, and [plan](plan.md) includes technical context, Constitution Check, project structure and complexity rationale. Master RTM Section L uses **12 exact SKI-FR IDs** with corresponding 24 exact test IDs instead of slash shorthand.

**Important:** T001..T005 remain marked completed as *documentation bootstrap* tasks only. This authoring extension is not an observed native CLI execution or independent A.1. All existing T006..T015 remain unchecked, and none of the 24 feature acceptance cases is reported PASS. Future static Git tree/source checks may report `STATIC_INSPECTED` with exact source SHA separately.
