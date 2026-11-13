# PLAN-082/083 — System RTM, Workflow STOP and resumable handoff

- **Captured (UTC date):** 2026-11-13
- **Repository:** `RyugaWork/spec2code`
- **Working branch / PR:** `feat/agent-governance-v0.8.0` / [Draft PR #8](https://github.com/RyugaWork/spec2code/pull/8), stacked on Draft PR #7.
- **Source snapshot audited:** `9632719962377caf36a37d47a2f46ad83568c4f8`. This handoff file and the checklist are an additional documentation commit beyond that audit snapshot.
- **Change type:** development-governance Markdown documents only; `.source/scripts/*.py`, `.source/tests/*.py`, `.source/.config/*.json` unchanged.
- **Lifecycle state:** implementation of the **agent-facing design docs** completed; RTM review and CI acceptance still in progress. This is **not** a machine workflow STOP event and is not reviewer approval.

## Documents and accepted source context

The work started from current root AGENTS, `.agents/.spec.md`, F01–F36 feature register, 12 Python test modules, the existing five-stage `workflow_guard.py` state machine, `session_guard.py` status/checkpoint/finish CLI, `handoff_store.py` exact-session merge and Spec Kit read-only bridge. The user requested both a concrete requirements **traceability matrix** and a workflow specification with **STOP → snapshot → handoff → RESUME**.

New primary documents:
- [System RTM](../.traceMatrix.md): 37 system requirements corresponding 1:1 to F01–F37, seven cross-cutting NFRs, distinct AC IDs, plan pointers, implementation/doc path, actual test method or `NOT_MAPPED`, status and open gaps.
- [Workflow Specification](../.workflow/workflowSpecification.md): five current phases and an orthogonal **agent-level** STOP, not a fabricated machine PAUSED state.
- [STOP/Handoff Protocol](../.workflow/stopAndHandoff.md): freeze new mutations, collect only observed facts, clearly flag `PERSISTED` or `NOT_PERSISTED`, no unauthorized session FINISH/handoff MERGE/workflow CLOSE, validated RESUME.
- [Portable STOP template](../../.source/references/stop-handoff-template.md): task, phase, source/session, changed files and attribution, actual verification, open ACs and the next safe actions.
- Root `AGENTS.md`, `.source/SKILL.md`, README, policies, checklist, feature register, spec and templates cross-reference the RTM and STOP protocol.

## Verification ledger

| Check | Exact evidence | Result |
| --- | --- | --- |
| F01–F37 primary requirement mapping | 37 distinct IDs in RTM against feature register; no missing F-ID | SOURCE REVIEW PASS |
| Cross-cutting requirements | 7 NFR rows S2C-NFR-001..007 | SOURCE REVIEW PASS |
| Actual test method references | 34 quoted `test_*.py::test_*` entries matched against the current 12 test files, all methods found; 28 distinct methods | SOURCE REVIEW PASS |
| Markdown links | 20 relevant documents checked against actual committed Git tree; zero broken internal file links | SOURCE REVIEW PASS |
| Latest exact-head CI at audit snapshot | Push run [43340515356](https://github.com/RyugaWork/spec2code/actions/runs/43340515356), PR run [43340523524](https://github.com/RyugaWork/spec2code/actions/runs/43340523524): in progress when checked | PENDING |
| Local script tests / actual STOP+RESUME runtime | No usable local clone; no Python STOP/RESUME operation; not run | NOT RUN |
| Human review / Windows hostile junction, OneDrive and migration proof | Independent approvals and manual adversarial environment evidence absent | OPEN |

The previous push CI run 43337690688 (on old source SHA `d49da3eb12c0`) did pass four Python jobs (124 tests each; three Linux Windows-only skips; zero skips Windows) but must not be relabeled as final-head evidence.

## Limitations / next steps

1. Obtain exact-head CI and independent docs/requirements review for PR #8. Keep PR Draft and parent PR #7 Draft.
2. Parent PR #7 still has three P0 Workflow Guard defects (CLOSE scope loss, incorrect VERIFY/HANDOFF policy operation and incomplete post-VERIFY source/spec fingerprinting) and one P1 status mismatch; these are **not** fixed by AGENTS or the STOP protocol.
3. F37 is specified at the interactive-agent level only. Any actual `pause`/`resume` CLI event, persistent machine snapshot and recovery integration needs a separate approved runtime plan, schema migration, negative tests and safety review.
4. Run installed-host and Windows OneDrive/TOCTOU/legacy migration acceptance before stable release; do not presume a system-level RTM means all ACs passed.
5. No user-owned host AGENTS, state, handoff logs, Spec Kit files or branches were replaced; no automatic merge, push outside this agreed work branch or release operation.

**Rollback:** revert PLAN-082/083 docs commits only; preserve existing local runtime state, source, previous handoffs and original PR #7 branch. Handoff records are documentary, not authorization.
