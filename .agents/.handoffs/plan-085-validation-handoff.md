# PLAN-085 — Validation gates (A.1 and B.1) specification handoff

> **DESIGN_IN_PROGRESS.** This is a written design checkpoint, not an A.1 or B.1 validation report and not an implementation authorization.

- **Date:** 2026-11-13 (Asia/Ho_Chi_Minh).
- **Repository / branch:** `RyugaWork/spec2code` / `feat/agent-governance-v0.8.0`.
- **PR:** [Draft #8](https://github.com/RyugaWork/spec2code/pull/8), stacked on Draft #7.
- **Design source revision audited:** `ab6dfc6a14b971a2bba005427dc08893dfcae49f`; this handoff is added by a subsequent documentation commit.
- **User-specified change:** add **A.1 Validation** after **A Planning & Specification** and **B.1 Validation** after **B Implementation**, while keeping the current scope in A/design only.

## Design artifacts

- [Validation Specification](../.workflow/validationSpecification.md): two separate loops with 9 check IDs each, result and risk gates, feedback/rework, external authorization boundaries and explicit NOT_RUN states.
- [Validation Report Template](../.workflow/validationReportTemplate.md): exact source/revision, check result, reviewer, risk, defect and handoff.
- [A Planning Workflow](../.workflow/planningSpecificationWorkflow.md): A/P1–P9 → A.1 (do not skip) → external approval → future B.
- [B Workflow](../.workflow/workflowSpecification.md): internal VERIFY distinct from external B.1 acceptance and real host/security validation.
- [System RTM](../.traceMatrix.md): design gate trace `DS-085-A1` and `DS-085-B1`, retaining 37 unique primary F01–F37 requirement links and 7 existing NFRs.
- [Risk Matrix](../.riskMatrix.md): proposed `RM-015..017` risk scores for A.1 authority, B.1 evidence/security and unsafe transitions; linked to register `R63..R66`.
- Root AGENTS, feature register, SRS authoring plan, workflow index/runbook, delivery and STOP handoff instructions aligned without source-code changes.

## Validation and audit ledger (not runtime acceptance)

| Item | Observed evidence | Outcome |
| --- | --- | --- |
| 21 relevant Markdown files | Parsed Markdown links at audited tree `ab6dfc6a14b`: batch 1 95 references, batch 2 109 references; zero missing internal repository file targets | STATIC DOCUMENT PATH REVIEW PASS |
| A.1 check IDs | `A1-VAL-01..09` present and unique in validation spec | STATIC CONTENT REVIEW PASS |
| B.1 check IDs | `B1-VAL-01..09` present and unique in validation spec | STATIC CONTENT REVIEW PASS |
| Requirement trace | 37/37 distinct F01–F37 primary RTM links remain, `DS-085-A1/B1` both present | STATIC TRACE REVIEW PASS |
| Code/config/test diff vs PLAN-084 baseline | GitHub compare from `caf9008` to `ab6dfc6` changed 21 Markdown files; **zero non-Markdown** | SOURCE SCOPE REVIEW PASS |
| Push/PR CI on `ab6dfc6` | [Push 43346695979](https://github.com/RyugaWork/spec2code/actions/runs/43346695979) and [PR 43346703305](https://github.com/RyugaWork/spec2code/actions/runs/43346703305) running at observation | IN_PROGRESS; final-head CI must be checked separately |
| Actual A.1 Design Validation | SRS content and independent source/requirements/risk signoff not yet complete | **A1_NOT_RUN** |
| Actual B.1 System Validation | B not yet authorized or implemented for PLAN-085 | **B1_NOT_RUN** |
| Independent acceptance/merge/release | No authorized reviewer signoff | **NOT_APPROVED** |

## Decision and remaining work

- **A current:** DESIGN_IN_PROGRESS; finish SRS, feature designs and Risk Management first, then perform real A.1 validation on exact approved document revisions.
- **A.1 currently:** NOT_RUN. PASS on a criteria report would not itself authorize B. Fail or blocked returns to affected A stage(s) and requires a revised review report/handoff.
- **B currently:** NOT_AUTHORIZED/NOT_STARTED under PLAN-085.
- **B.1 currently:** NOT_RUN. When B is separately authorized and delivered, B.1 validates actual behavior/host/OS/security/user acceptance, and defects return to B or to A for design changes.
- **Risks:** P0 Path Guard Windows/OneDrive TOCTOU, PR #7 Workflow Guard P0/P1, and migration/ownership approvals remain OPEN. Documentation did not remedy them.
- **Next safe task:** complete remaining design and source-authority decisions, then prepare an **actual** A.1 report using the template with independent reviewer evidence. Do not start code, host migration, deployment or Git merge on the basis of these documents.

**Persistence:** this handoff is a Markdown governance file committed to the specified development branch. It is **not** a live-host runtime checkpoint; it does not finish or close a session.

**Rollback:** revert PLAN-085 docs only; preserve prior handoffs, actual host state, Spec Kit files and parent PR history.
