# Spec2Code STOP Handoff — <Task ID> — <UTC timestamp>

> **Stop record, not completion or approval.** Author/owner: <actor> | Captured: <actual UTC> | Persistence: PERSISTED / NOT_PERSISTED (path or reason) | Source of evidence: <observed read / previous report / unknown>

## 1. Identity and authorization
- Task ID / brief task:
- Requester-approved actions: READ / PLAN / IMPLEMENT / VERIFY / DELIVERY (state exact permissions):
- Repository/worktree: <observed root or remote repository>
- Branch / exact commit SHA: <observed or UNKNOWN>
- Authorized affected paths / exclusions:
- Session ID and observed session status: <ACTIVE / CLOSED / NONE / UNKNOWN>
- Workflow phase and observed machine status: <DISCOVER / SPECIFY_PLAN / IMPLEMENT / VERIFY / HANDOFF_REVIEW / UNKNOWN; machine status if seen>
- This STOP's reason code: USER_STOP / SAFETY_BLOCK / MISSING_APPROVAL / REQUIREMENT_CONFLICT / SOURCE_DRIFT / TEST_FAILURE / TOOL_UNAVAILABLE / CONTEXT_LIMIT / INTERRUPTED_UNKNOWN / OTHER
- Stop reason / last safe action / potentially in-flight action:

## 2. Current work (facts only)

| Requirement / task / AC ID | State: DONE_AND_EVIDENCED / IN_PROGRESS / BLOCKED / NOT_STARTED / UNKNOWN | Observed files / artifacts | Evidence or limitation |
| --- | --- | --- | --- |
| <ID> | <state> | <repo-relative paths or NONE> | <actual observed evidence/unknown> |

- Self-authored uncommitted paths:
- External commits/edits (not attributed to self):
- Unattributed/unknown changes:
- Local dirty / untracked file status (or NOT CHECKED):
- Official Spec Kit active feature and spec/plan/tasks revisions (or NONE/UNKNOWN):

## 3. Verification — do not invent PASS

| Check / command | Source revision and platform | PASS / FAIL / BLOCKED / SKIPPED / NOT RUN | Evidence reference |
| --- | --- | --- | --- |
| <check> | <SHA, environment> | <status> | <log or reason> |

- Stale evidence to re-run after resume:
- Unverified acceptance criteria:
- Risks/known defects:

## 4. Decisions and recovery

- Missing requirements/policy or external approvals:
- Safety/rollback guidance without destructive cleanup:
- Ordered first safe steps for the next session/agent:
  1. Revalidate checkout, current AGENTS and authority, task and affected paths.
  2. Compare HEAD/working tree, session state and Spec Kit feature with this snapshot; handle drift.
  3. Confirm scope/write approval, then rerun affected checks and continue from the earliest valid phase.
- Next responsible owner / requested decision:
- Reference to previous STOP record, if this task was interrupted before:

## 5. Final STOP record

- Agent-level outcome: STOPPED_WITH_HANDOFF / STOPPED_UNPERSISTED / INTERRUPTED_UNKNOWN
- Persistence: PERSISTED at <verified exact path> / NOT_PERSISTED because <reason>
- Machine workflow state: UNCHANGED / UNKNOWN / <observed difference, if any>
- Session finish or handoff merge performed? **NO unless separately authorized and actually evidenced.**
- Git commit/push/merge performed? <NO / exact authorized action with SHA, if actually done>

**Note:** Do not include secret/PII contents, raw prompt histories or claim a completed test or independent review from this handoff.

## PLAN-109 / M08 — Required pause and rollback uncertainty

When populating this template, name **what was actually executed and where** (GitHub connector, local CLI, external MCP or static read), not simply what the agent planned. Include last verified source SHA and branch, changed-file allowlist, pre-existing uncommitted files, pending tool actions, source/Google revision drift, failed checks, open P0 and exact next owner action. Mark interrupted or unverified operations `UNKNOWN` instead of `PASS`.

A handoff contains redacted IDs and evidence links, never credentials, personal secrets, raw provider conversations or guessed approval signatures. On resume require source/policy/host revalidation; when a prior write may have succeeded but returned no confirmation, inspect actual state before any retry. Rollback must name a scoped proposed revert and protect other writers' work; avoid automated deletion of old handoffs.
