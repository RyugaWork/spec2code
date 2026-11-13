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

## A.1 validation checkpoint

- A.1 validation report ID and exact document revision (or `A1_NOT_RUN`):
- Outstanding A1-VAL-01..09 checks, failure owner and affected A stage(s):
- Actual independent design reviewer and decision (or `NOT_REVIEWED`):
- Implementation authorization: `NOT_AUTHORIZED` unless explicitly granted for a reviewed revision.

A handoff at P9 is **input** to [A.1](validationSpecification.md), not automatic design approval. Keep separate [validation report](validationReportTemplate.md) and never promote `READY_FOR_REVIEW` to `APPROVED_FOR_IMPLEMENTATION` without the owner's actual decision.

## Technology and requester override handoff (PLAN-086)

- Applicable target: `S2C_SOURCE` / `HOST_REPOSITORY` / `BOTH` (actual repository/ref):
- Python interpreter/libs, PowerShell edition/modules, SQL DBMS/dialect/driver, .NET/other versions as affected:
- Technology assessment `TECH-ID`, official vendor support checked date and adoption/compatibility evidence:
- Conservative **supported mature default** and mainstream project layout:
- Explicit user-selected alternative or structure override `OVR-ID` / [template](../.documents/technologyOverrideTemplate.md), or NONE:
- Override classification: supported newly GA / preview / EOL / experimental / other, with real host security and permission decision:
- Risk R67–R73, mitigation, rollback/migration, planned tests, source/RTM changes:
- A.1/B.1 **NOT_RUN** or exact observed report and reviewer; user approval of a version **not** automatic write/merge approval:

See [cross-stack policy](../.documents/technologyVersionPolicy.md) and [assessment](../.documents/technologyAssessmentTemplate.md). A handoff is planning evidence; it cannot self-approve code changes, new tools or a database migration.
