# Tasks: Spec Kit Integration for S2C

**Feature:** [spec.md](spec.md) | [plan.md](plan.md)  
**Status:** DRAFT_TASKS; checkboxes are **authoring status only**, not automatic B-phase authorization or runtime test PASS.  
**Work branch:** `docs/plan-089-a1-readiness`. Spec Kit feature identity is bound by `.specify/feature.json`, **not** this branch name.

## Phase 1 — Web/GitHub bootstrap (documentation; no code execution)

- [x] T001 [US4] Create a draft project constitution at `.specify/memory/constitution.md` that respects root AGENTS and the master BRD.
- [x] T002 [US1] Select `specs/001-s2c-speckit-integration` in `.specify/feature.json` without creating a Git feature branch.
- [x] T003 [US1] Author this feature's `spec.md`, `plan.md`, `tasks.md`, and an explicit quality checklist; map to S2C BR/REQ/AC.
- [x] T004 [US1] Update S2C AGENTS, RTM, plans/risk, adapter guide and README to support Web and native modes without duplicating BRD.
- [x] T005 [US3] Static-check the JSON pointer, repository-contained paths, task ID format, uniqueness, documentation links, and Git diff against the pre-integration HEAD.

**Bootstrap evidence:** GitHub tree HEAD `ebdbd03f027a8e65ce5cde8ddc5ea0af5a1cad14` was read after authoring. `.specify/feature.json` parses to a contained `specs/` path, `spec.md`/`plan.md`/`tasks.md` exist, T001..T015 are unique and match the existing S2C bridge's `T\d{3,6}` convention, and 171 relative Markdown links from the relevant edited files resolve in the Git tree. This is a **read-only static GitHub inspection**, not Python bridge or native Spec Kit CLI test evidence. T001..T005 are document/bootstrap tasks only.

## Phase 2 — Official CLI preparation (separate reviewed execution)

- [ ] T006 [US2] Select and verify a mature supported official Spec Kit release, installation source/tag, hash and CLI/agent integration.
- [ ] T007 [US2] In a disposable **local checkout**, back up any existing `.specify` and agent skill files; execute official `specify init --here --force --non-interactive --integration <approved-key> --script py` only with explicit authorization; inspect generated diff.
- [ ] T008 [US2] Prove official skills/scripts exist and work in the selected coding agent; capture actual `specify version`, pointer, stage and platform evidence.
- [ ] T009 [US2] Reconcile official generated templates/scripts and feature pointer without overwriting owner content; separately review any proposed integration into this working branch.

## Phase 3 — Independent design validation (before any B code task)

- [x] T010 [US4] Reconcile master BRD, Google stakeholder revision, Constitution, feature AC, RTM, risk and exact Git SHA **as a draft revision crosswalk only**; no owner approval or A.1 status implied.
- [ ] T011 [US4] Obtain actual independent A.1 report (`A1-VAL-01..09`) and source-bound signoff. Report P0/P1 risks explicitly; do not infer PASS from markdown creation.
- [ ] T012 [US4] Record a separately approved B task and scope for any adapter, CLI/script, config, security, or host-source modifications.

## Phase 4 — Future authorized implementation and acceptance

- [ ] T013 [US3] Implement only approved bridge/runtime enhancements and regression tests on exact source revisions; reject missing or unsafe paths.
- [ ] T014 [US3] Validate on disposable representative hosts (Windows/OneDrive/junction, Linux, without Spec Kit, with official CLI), capture logs, source hashes and actual results.
- [ ] T015 [US4] Obtain independent B.1 and release/merge authorization; preserve handoff, migration and rollback evidence.

## Dependencies

T001–T005 (Markdown bootstrap) → T010 (independent **draft/document** source reconciliation, possible before native setup); T006–T009 (separately approved native pilot, optional for drafting but required before claiming native integration) and T010 current-revision recheck → T011 independent A.1; **only** A.1 PASS + T012 explicit B approval can permit T013 implementation, followed by T014 host tests and T015 independent B.1/release decision. Source drift invalidates affected T010 evidence and requires remapping. Actual CLI may be installed *for development verification in an authorized disposable environment* before A.1, but **must not use that as permission to mutate product/host code**.

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

## PLAN-094 — T010 exact source crosswalk (documentary completion only)

**Reviewed Git source snapshot:** `fce2a8e4c425f9e21b15592e3f5f9e653703c3d9` on `docs/plan-089-a1-readiness`. **Google BRD stakeholder revision:** `AHj4eMRu50FIWgL_K17Wef7cveq_qCIe8Kq-pV-robhc37C8Gu9H5AxWK3QuEPL1cD7P6iFgRJQH2lSraIPO5DPP15fTuHPOmCZwAwFV5g` (Draft v1.5, sections 25 PLAN-092, 26 PLAN-093 and 27 PLAN-094 present). **Project Constitution:** DRAFT/NOT_RATIFIED; root AGENTS/global SRS/risk retain authority.

**Observed documentary crosswalk:** 12 unique SKI-FR rows in `spec.md`, 12 explicit mapping rows in master RTM Section L, 24 distinct planned P/N IDs in the feature acceptance catalogue, 15 unique T IDs in the task register and zero unresolved referenced global BR/REQ/NFR IDs. Global critical security/authority risks remain OPEN. Google BRD is a stakeholder-level summary, **not a byte-identical source SRS**, and its update is not signoff. `T010` check means this one source-revision pair was mapped at **draft** level only; recheck on source drift and obtain real owner/independent review under T011. No native CLI/host test was executed and no version/OS decision granted.

**Current tasks:** 6 documentation/reconciliation tasks `T001..T005, T010` recorded done; native T006..T009 remain unchecked, independent T011 unchecked, explicit B T012 unchecked, source/host/release T013..T015 unchecked. Do not collapse these statuses into an invented release gate.


## PLAN-095 — Native implement safety separation (do NOT execute whole queue)

The official Spec Kit task format is `[ID] [P?] [Story]`; task IDs remain stable and every T001–T015 row now includes its `[USn]` association. These records form a **mixed governance/document/toolchain/approval/code backlog**, **not** an executable `$speckit-implement` queue. Adding a story tag does not authorize runtime execution or represent story-based implementation completion.

**Ownership:** T001–T005 and T010 = Markdown/document review; T006–T009 = external native operator/owner decisions; T011 = independent A.1 reviewer; T012 = explicit B authorization owner; T013 = B-authorized source developer if separately permitted; T014 = host QA; T015 = independent B.1/release owner. T011, T012 and T015 must never be auto-checked by an implementing agent.

Upstream `implement` can offer a continuation prompt when requirements checklists are incomplete. An answer of 'yes' to that prompt is **not** a substitute for independent S2C A.1, separate B scope, runtime Path Guard or host policy. Refer to [native execution safety gate](../../.agents/.workflow/specKitNativeExecutionGate.md); it is a **documentation policy**, not a deployed CLI interception hook.

**Current gate:** `A1_NOT_RUN`, `B_NOT_AUTHORIZED`, `NATIVE_NOT_INSTALLED`. Do not run `$speckit-implement` or `$speckit-converge` on the mixed queue. For a future implementation, derive a separately reviewed executable coding subset with stable IDs, dependency/test mapping and explicit allowed files; preserve the original task and gate evidence.

### PLAN-095 — User story label crosswalk

Upstream task tokens `[US1]`, `[US2]`, `[US3]`, `[US4]` refer respectively to stable feature story headings `US-01`, `US-02`, `US-03`, `US-04` in `spec.md`. The bracketed syntax is a **task classification label**, not a permission to execute; Tnnn prefixes remain unchanged and 6 documentary task checkboxes retain their source-bound state. See [Web-mode source evidence](../../.agents/.documents/specKitWebModeEvidence095.md) for the actual S2C bridge-regex compatibility inspection.

## PLAN-108 / K03 — Task checkbox authority and test provenance

A task checkbox is not an authorization primitive. `T011/T012/T015` remain as they were at the source revision and are **not** checked by an agent because a Markdown acceptance plan exists. For every later task completion attach: actual tool/host version, starting and ending SHA, changed-path diff, command/fixture, observed result, review authority and any rollback. An unsupported native CLI yields `NOT_RUN/UNAVAILABLE`, not a completed task.

Keep Web-only source-reading/provisional pass evidence separate from native mutating task outcomes; do not promote an upstream Spec Kit step from a GitHub bridge `READY` flag. On plan/spec revision drift, re-evaluate dependencies, invalidate affected proof and record a new handoff rather than rewriting historical task execution claims.
