# Spec2Code — Validation Report Template (A.1 or B.1)

> **Draft template.** Do not label a validation PASS or sign for a reviewer merely because this file was created. Use a unique new report for each actual validation pass. Do not overwrite an earlier failed/blocked record.

- Report ID: `VAL-A1-...` / `VAL-B1-...`
- Loop: **A.1 Design Validation** / **B.1 System Acceptance Validation**
- Date/time and timezone:
- Requester and exact scope / authorization:
- Source repository/ref/branch and relevant SHA:
- Approved SRS version (or `NOT_APPROVED`):
- RTM version and applicable AC IDs:
- Design version or implementation artifact hash:
- Test/review host environment (B.1 only; else `N/A`):
- Current risk matrix revision and largest open P0/P1:
- Reviewer identity/authority: <observed real decision / `NOT_REVIEWED`>
- Persistence: `PERSISTED` + verified location / `NOT_PERSISTED` + reason

## Validation checks

| Check ID (A1-VAL-01..09 or B1-VAL-01..09) | Requirement/AC/risk refs | Evidence and exact revision | PASS / FAIL / BLOCKED / NOT_RUN / N/A | Defect and next owner |
| --- | --- | --- | --- | --- |
| <ID> | <IDs> | <observed source/report> | <real result> | <action> |

## Risk and scope decisions

| Risk | L | I | Exposure | Finding / change this pass | Residual risk (expected vs verified) | Owner |
| --- | ---: | ---: | ---: | --- | --- | --- |
| RM-... | | | | | | |

- Inapplicable check exclusions and exact authorized justification:
- Failed, blocked or unrun acceptance scenarios:
- Requirement/source/Spec Kit/host drift observed since prior validation:
- A.1 defect returns to A/P-stage(s); or B.1 defect returns to B task(s) / A stage(s):
- Pending independent approvals / source of actual signoff:
- Files or artifacts modified (or NONE):
- Actual execution evidence (commands, SHA, platform, exit code; `NOT_RUN` where applicable):
- Next smallest safe step; rollback and stop/handoff considerations:

## Outcome

- Per-check failures and missing evidence:
- Aggregate outcome: `A1_PASS` / `A1_FAIL` / `A1_BLOCKED` / `A1_NOT_RUN` **or** `B1_PASS` / `B1_FAIL` / `B1_BLOCKED` / `B1_NOT_RUN`
- Approval gate separately: `APPROVED_FOR_IMPLEMENTATION` / `APPROVED_FOR_RELEASE` / `NEEDS_REVIEW` / `NOT_AUTHORIZED`
- Owner decision and exact verified evidence:
- Handoff link / `NOT_PERSISTED`:

**Rules:** A.1 PASS does not authorize B; B.1 PASS does not authorize merge/release. FAIL/BLOCKED stops promotion and requires a dated handoff with targeted rework. Design phase cannot claim B.1 tests ran.

## PLAN-086 technology / version / structure override validation checklist

- Applicability: `S2C_SOURCE`, `HOST_REPOSITORY`, `BOTH`; exact affected paths/revision:
- Named runtime/interpreter/PowerShell edition/SQL DBMS+driver+dialect/other platform version:
- Baseline supported-mature-mainstream candidate and official support checked date:
- Dependency/OS/build/CI, database migration/backup, security servicing and architecture evidence:
- User override `OVR-ID`, request and risk/owner approval, or NONE:
- A1-VAL-01/05/07 actual source/design and risk decision (or `NOT_RUN`):
- B1-VAL-01/03/04/06 actual effective version/structure and regression/security evidence (or `NOT_RUN`):
- Explicit separate permission to modify code, schema, CI or host data (or `NOT_AUTHORIZED`):

Use [cross-stack technology policy](../.documents/technologyVersionPolicy.md) and [override template](../.documents/technologyOverrideTemplate.md). A user-approved version preference is **not** independent release acceptance or a waiver of host safety controls.
