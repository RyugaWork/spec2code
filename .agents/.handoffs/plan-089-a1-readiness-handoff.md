# PLAN-089 — Staged specification completion and A.1 review handoff

- Capture date: 2026-11-13 (Asia/Ho_Chi_Minh); recorded from current connected tools, not a running local S2C session.
- Task: fulfill request to finish S2C documentation in dependency order without fragmenting the BRD or bypassing safety/independent validation.
- Repository: `RyugaWork/spec2code`; branch `docs/plan-089-a1-readiness`; parent `docs/plan-088-unified-s2c` (PR #9 Draft, targeting `feat/agent-governance-v0.8.0`).
- Document source inventory HEAD observed before handoff creation: `dda201351a1842fc471d9b5bd29980a74adf966d`; this record's own commit changes the branch HEAD. A.1 reviewer **must re-fetch exact HEAD** and assess that final revision.
- Google Docs BRD: `https://docs.google.com/document/d/1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4/edit?tab=t.0`, Draft v1.4; observed revision `AHj4eMTy010-onHfZMUHIKHnPTyUwz--CNXjySLMrCrNt3Hs8NUXJ4zF0WPeedE8mT5JmmiwXE0yvP0TvdmsymGiBw3QTV27wvVANN9gIg`.
- Scope actually changed: **documentation only** on Git + authorized Google BRD text. No `.source/scripts/*.py`, `.source/.config/*.json`, host state, CI test, migration, deployment or Git merge done in PLAN-089.
- Local Path Guard, session ID, exact checkout and CI: **NOT OBSERVED / NOT RUN** (GitHub and Google connector edits are remote, not an OS-sandboxed local runtime session).
- STOP/RESUME status: no STOP requested; this is a design-stage handoff. No native `PAUSED`/resume event has been executed.

## Stage evidence and honest disposition

| Stage | Source of artifact | Authoring status | Approval/verification |
| --- | --- | --- | --- |
| A0 Authority/source | `AGENTS.md`, `.agents/.documents/.documentGovernance.md`, unified BRD version | DOCUMENTED | Host/stakeholder owner still UNKNOWN |
| A1 SRS-01..12 | [Canonical BRD Sections 15](../.spec.md), [chapter inventory](../.documents/systemSpecificationPlan.md) | 12/12 CONTENT_DRAFT (some known gaps explicitly marked) | Owner validation NOT_RUN |
| A2 Interface contracts | [Canonical BRD Sections 16](../.spec.md) | Component table, ReviewManifest/Finding/Synthesis, STOP, drift and errors DESIGN_DRAFT | No runtime schema/API implemented or tested |
| A3 Tests/RTM | [Test catalogue](../.workflow/testingAndDelivery.md), [RTM Section J](../.traceMatrix.md) | 21 BRs × positive/negative = 42 planned TC identifiers; bidirectional map present | 0 acceptance scenarios executed by PLAN-089 |
| A4 Risks/recovery | [Risk Matrix Section 10](../.riskMatrix.md), [master](../.spec.md) | RM-001..033 preserved; safety M1 precedes reviewer engine M3; recovery and decision gaps identified | Verified residual UNKNOWN; P0/P1 OPEN |
| P9 Handoff/A.1 package | This record | PREPARED_FOR_REVIEW | A.1 NOT_RUN; no independent signoff |

## A.1 independent validation preflight (author inventory only, NOT a validation run)

| Criterion | Evidence present for reviewer | Pending or blocking fact | Actual A.1 outcome |
| --- | --- | --- | --- |
| A1-VAL-01 Source authority | BR source links and Git/Google versions | Stakeholder/host approval owner and accepted canonical revision missing | NOT_RUN / OWNER_UNKNOWN |
| A1-VAL-02 Testability | 21 BR requirement statements, AC examples, SRS chapters | Quantitative SLOs, quota and support bounds need owner decisions | NOT_RUN |
| A1-VAL-03 Traceability | Existing S2C-REQ/FR status, BR-001..021 ↔ 42 designed scenarios | Evidence for proposed F38..42 and real host testing cannot be fabricated | NOT_RUN |
| A1-VAL-04 Feature design | Inputs/outputs and error, STOP/review alternate paths in Sections 15–16 | Domain role catalog, storage namespace and cross-worker actual capability not approved | NOT_RUN |
| A1-VAL-05 Architecture/workflow | Seven boundaries, five machine stages, A/A.1/B/B.1, optional Spec Kit | Native pause/resume schema, legacy compatibility, Windows support open | NOT_RUN |
| A1-VAL-06 Risk discovery | Security/OS/connector/prompt injection and existing RM-001..033 | Independent security reviewer and real threat validation absent | NOT_RUN |
| A1-VAL-07 Risk treatment | BEFORE/AFTER design action and planned adversarial cases | Mandatory P0 and P1 not resolved or risk-accepted | NOT_RUN |
| A1-VAL-08 Design handoff | Source snapshots, exact branch, next steps, rollback and open tasks | Exact final HEAD must be re-read by evaluator | NOT_RUN |
| A1-VAL-09 Independent signoff | Validation criteria and report template exist | No independent A.1 report or authorized reviewer decision | NOT_RUN |

**Overall gate:** `A1_NOT_RUN` and `APPROVED_FOR_IMPLEMENTATION = NO` (not an assertion that formal A.1 has been performed and failed). This preflight does not supply reviewer independence or waive a critical risk.

## Prioritized next safe action and risk

1. Review PR #9 then this staged documentation branch; decide integration target with `spec2code/InitialVersion_v0` deliberately (branches diverged). No automatic merge.
2. Obtain accountable BR/host/security/QA owners; select/confirm host/OS/legacy support matrix, budget/n role limits and acceptance thresholds. Write explicit decision records in master and RTM where approved.
3. Request independent A.1 using the exact Git HEAD and Google revision. Use `.agents/.workflow/validationReportTemplate.md`; record each A1-VAL-01..09 result, not only aggregate outcome.
4. Address highest risk **RM-001 (Path Guard, Windows TOCTOU)** and known workflow/policy/freshness P0 source defects under distinct owner-approved B task **only** after A.1 and permission; host-adversarial validation required.
5. Design/implement native STOP/RESUME and bounded review worker runtime after safety and schema acceptance; conduct representative host tests, separate B.1 and release decision.

## Rollback and preservation

Revert only PLAN-089 documentation commits if the design is rejected, preserving PLAN-088/087 history and all host/legacy/session data. For Google BRD use document revision history with stakeholder permission; do not assume Git revert changes Google Docs. Actual future code/host migrations require tested backups and independent owner approval. No destructive cleanup is authorized by this handoff.
