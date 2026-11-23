# PLAN-091 — Review remediation: authoring handoff and independent A.1 queue

> Recorded: 2026-11-13 (Asia/Ho_Chi_Minh), development repository `RyugaWork/spec2code`, working documentation branch `docs/plan-089-a1-readiness`, PR #10 [source update](https://github.com/RyugaWork/spec2code/pull/10), parent `docs/plan-088-unified-s2c`. The protected historical [PLAN-090 review report](https://github.com/RyugaWork/spec2code/blob/docs/plan-090-a1-review-findings/.agents/.handoffs/plan-090-a1-preflight-review.md) stays on PR #11, pinned to PRE-FIX Git SHA `1dae9338f4d38518e897212cdf80ba47239a7671`.
>
> **Snapshot before creation of this handoff:** Git head `156e6c42630e6fe5b69a6088753d7ab4ae94ae7d`; Google BRD document ID `1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4`, tab `t.0`, revision `AHj4eMR6P777cUP79P9FOKQiIQLmVkfAu21lVJv9J7WyBmizNLSPJxGPIx0PaH8K6v3fBSaHjVsc8HANpdinScrs2KJihOf5OJncnC3giw`, Draft v1.4 Section 24. **This file's own commit changes HEAD; all next reviewers must re-fetch final Git SHA, latest Google revision, and any changed BR sections.**
>
> This is a documentation authoring/handoff update, **not an independent A.1 outcome, security acceptance, CI test, host migration or approval**. No claim of multi-worker orchestration or actual Host Windows race reproduction.

## 1. Actual changed artifacts and scope

| Artifact | Actual PLAN-091 authoring change | Status |
| --- | --- | --- |
| `.agents/.spec.md` Sections 15–18 | Correct exact A1-VAL IDs and 160 escaped inline-code markers; draft typed logical review contracts, states/errors, owner/benchmark decisions DEC-091-01..10 | SOURCE_TEXT_REPAIRED / CONTRACT_DESIGN_PROPOSED |
| `.agents/.workflow/testingAndDelivery.md` | Expand to 42 planned cases, each with preconditions/input partition, step, expected outcome, evidence and milestone | DESIGN_REMEDIATED; ALL NOT_RUN |
| `.agents/.traceMatrix.md` Section K | Review findings REV-090-01..10 to BR/REQ/TC/risk/decision mapping without inventing evidence | MAPPED_IN_DESIGN |
| `.agents/.plans.md` PLAN-091 | P091-01..06 status and M1/M3 dependency | AUTHORED; remaining gates OPEN |
| `.agents/.riskMatrix.md` Section 11 | Risk BEFORE / design action / AFTER, RM-001 P0 prioritized, all residual UNKNOWN | MITIGATION_SPECIFIED_ONLY |
| `AGENTS.md` Section 15 | Route agents through canonical master, corrected test catalogue, historic review and distinct external A.1 | GOVERNANCE_DRAFT |
| `.agents/.documents/.documentGovernance.md` | Git/Google exact revision pair requirement and historical review preservation | GOVERNANCE_DRAFT |
| [Google stakeholder BRD](https://docs.google.com/document/d/1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4/edit?tab=t.0) | Section 24: truthful PLAN-091 summary; Markdown is more technically precise | MIRROR_UPDATED, OWNER_NOT_APPROVED |

No `.source/scripts/*.py`, `.source/.config/*.json`, actual host AGENTS, CI workflow or executable acceptance scripts are modified by this stage. A technical finding being **source-text-repaired** does not mean A.1 or B.1 passed.

## 2. Findings dispositions — preserve unresolved blockers

| Finding | Technical documentation disposition | What remains to be approved or tested |
| --- | --- | --- |
| REV-090-01 P0 | DEC-091-01/02/09 recorded | Named product/host/security owner and actual source/BR signoff UNKNOWN |
| REV-090-02 P0 | Risk treatment and adverse tests specified | RM-001..005 P0 source defects OPEN, actual safe M1 code and adversarial tests NOT_RUN |
| REV-090-03 P1 | 42 cases expanded with setup/action/outcome/evidence | Fixture versions, supported host and real execution NOT_RUN |
| REV-090-04 P1 | ReviewRequest/Snapshot/Manifest/Finding/Synthesis/STOP proposed | Host capabilities, output ownership, approved schema, n/quorum/budget UNKNOWN |
| REV-090-05 P1 | DEC-091-08 created | Actual branch integration/merge target and approval UNKNOWN |
| REV-090-06 P1 | Git SHA + Google revision binding contract; actual draft revision recorded | Owner-approved reconciliation of material BR/AC and drift decision UNKNOWN |
| REV-090-07 P1 | Required independent reviewer/gate preserved | Actual independent A.1 reviewer and signoff NOT_RUN |
| REV-090-08 P2 | Canonical `A1-VAL-01..09` repaired in master | Independent review of new exact revision pending |
| REV-090-09 P2 | 160 escaped code delimiters repaired in SRS | Render/standalone docs test and independent acceptance pending |
| REV-090-10 P1 | Metric and host-support decision protocol specified | Numeric threshold, baseline fixture and supported OS/model approved values UNKNOWN |

## 3. A1-VAL design gate and next permitted work

A1-VAL-01/09 source authority and independent signoff = **NOT_RUN**; 02/04/05 need actual owner input for acceptance targets, schema/permissions/host; 03 may inspect complete ID mapping but cannot treat planned cases as executed evidence; 06/07 open risks must remain explicit; 08 owner must review this exact final handoff. Formal aggregate `A1_NOT_RUN`; approval for B `NOT_AUTHORIZED`; B.1 `NOT_RUN`; release `NOT_AUTHORIZED`. This is a **self-authored design package, not a formally signed validation report**.

Priority remains: (a) obtain owner identities, authority decisions and approved environment/metrics; (b) commission real independent A.1 on pinned final Git/Google revision and all applicable A1-VAL-01..09; (c) only after A.1 PASS and separate B scope approval fix M1 Path Guard/phase-policy/fingerprint/CLOSE/security with exact-source regression; (d) M2 STOP/data compatibility; (e) M3 optional multi-agent runtime; (f) M4 real host acceptance and B.1; (g) M5 separate release decision. Do not let persona consensus or documentation PASS substitute for human approval.

## 4. Provenance, STOP and rollback

Source changes are remote Git connector edits and a Google Docs connector change. No local S2C Path Guard, Python tests, live subprocess, session ID, benchmark run, actual reviewer worker fleet or security OS instrumentation was executed. Their status is `NOT_OBSERVED` or `NOT_RUN`, **not PASS**. If stopped, use this factual handoff and check the latest branch/ref before resuming; do not transform it into a Workflow Guard `close` or artificial `PAUSED` state.

Rollback: revert only PLAN-091 documentation commits after review while preserving historic review/handoffs; use Google Docs revision history separately under owner authority. No deletion of unowned host files, production migration or automatic PR merge is permitted by this record.
