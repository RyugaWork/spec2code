# Spec2Code — Design-stage Handoff Template

> Use for **planning/specification/design/review**, not as a completed runtime session ledger. A design handoff may be delivered at any stage boundary, explicit STOP or context transfer. It does **not** call `workflow_guard close`, `session_guard finish` or `merge`.

- Handoff ID and captured UTC:
- Status: `DESIGN_IN_PROGRESS` / `DESIGN_PAUSED` / `READY_FOR_REVIEW` / `APPROVED_FOR_IMPLEMENTATION` (requires actual approval)
- Task/work scope, requester-authorized actions:
- Selected repository, branch and exact commit SHA (or `UNKNOWN`):
- Last complete planning stage P1–P9; currently open stage:
- Evidence sources `SRC-ID` with revision, ownership and confidence:
- Specifications reviewed/changed and current status:
- Requirement/AC and RTM rows affected:
- Feature design cards/decision IDs reviewed:
- Architecture/workflow decisions (proposed vs independently approved):
- Current risk matrix revision and latest pass:
- Highest open risk (L, I, exposure, priority, owner, mitigation design, residual evidence):
- Work completed **as designed** (not runtime implemented):
- Work incomplete and blocked decisions:
- Future implementation backlog / tests **NOT RUN**:
- Known external/host/Spec Kit scope constraints:
- Next stage/research question; smallest safe authorized next step:
- Explicit requester/human approvals still required:
- Persistence: `PERSISTED` + verified path/ref / `NOT_PERSISTED` + reason:
- No automatic source code change, CI claim, migration or merge:

## Design-stage evidence map

| Artifact / question | Actual current source/ref | Status: OBSERVED / DRAFT / REVIEWED / BLOCKED / NOT RUN | Owner / next action |
| --- | --- | --- | --- |
| <item> | <path / revision> | <status> | <owner/action> |

## Design risk review at handoff

| Risk ID | Previous E | Current E (L×I) | Action this pass | Design mitigation / evidence | Residual & status |
| --- | ---: | ---: | --- | --- | --- |
| RM-... | | | | | |

A handoff author must not claim a durable file exists unless the exact location was verified. For chat-only handoff write `NOT_PERSISTED`; never fabricate host approvals or present a design mitigation as a successfully executed runtime fix.
