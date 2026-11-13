# PLAN-086 — Cross-stack maturity policy + scoped User Override handoff

- **Date:** 2026-11-13, Asia/Ho_Chi_Minh.
- **Repository/PR:** `RyugaWork/spec2code`, `feat/agent-governance-v0.8.0`, stacked [Draft PR #8](https://github.com/RyugaWork/spec2code/pull/8) on Draft PR #7.
- **Observed design audit SHA:** `3eafc91af8dd75d060cb6584be1aae530ceb82a6`; final handoff/checklist commit is separately newer.
- **Actual current lifecycle:** `A = DESIGN_IN_PROGRESS`, `A.1 = NOT_RUN`, `B = NOT_AUTHORIZED`, `B.1 = NOT_RUN`.
- **Scope:** document/Agent governance only; **zero** Python, PowerShell, SQL, tests, JSON, actual host or runtime edits; no version retarget and no Git merge.
- **New user clarification:** .NET 8/10/11 was only an example. Apply the conservative default to **all technologies** (Python, PowerShell, named SQL DBMS/driver/dialect/ORM, .NET, build tools, CI, other stacks) and **both S2C source and integrated host code**. Provide a **user-requested override** to the default maturity/structure preference.

## Draft design deliverables

- [Cross-stack technology/version/structure policy](../.documents/technologyVersionPolicy.md): current vendor support and security patches, maturity, verifiable mainstream adoption, compatibility, common project layout, exact scope and permissions.
- [Technology assessment](../.documents/technologyAssessmentTemplate.md): `TECH-ID` evidence for both S2C and host; existing code preservation, lifecycle and alternatives.
- [User Override template](../.documents/technologyOverrideTemplate.md): `OVR-ID` recording explicit request, repository scope, vendor status, risks, owner, migration/test/rollback, approval, and no silent substitution.
- [System RTM](../.traceMatrix.md): 37 original primary feature requirements, **9** distinct cross-cutting NFRs; `S2C-NFR-008` = conservative default and `S2C-NFR-009` = bounded user override; statuses DOC_REVIEW, tests NOT_MAPPED for these policy requirements.
- [Risk Matrix](../.riskMatrix.md): R67–R73 / RM-018–RM-024 for premature major adoption, unsupported/EOL, novelty-driven layout, stale support/patch confusion and override abuse.
- Root [AGENTS.md](../../AGENTS.md) and portable [Skill](../../.source/SKILL.md) both explicitly apply the same policy to own S2C code and installed host projects. [A Planning](../.workflow/planningSpecificationWorkflow.md), [A.1/B.1 Validation](../.workflow/validationSpecification.md), feature design, role/runbook, research and design handoff are linked.

## Technical interpretation examples (dated, not a global version list)

- **.NET**: on 2026-11-13, supported .NET 10 LTS is the conservative new-project candidate; supported but newly GA .NET 11 is allowed as a specifically requested **design override** with compatibility review; .NET 8 has reached EOL and needs a separately accepted legacy/security exception, not automatic new-project approval. Support: https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core.
- **Python**: choose a currently supported mature interpreter compatible with actual packages/wheels and OS; user may explicitly choose a newer supported interpreter with recorded compatibility risk. Verify at https://devguide.python.org/versions/.
- **PowerShell**: inspect PowerShell 7 support and Windows PowerShell 5.1 edition/module differences; 7.6 LTS is a supported example as of this date. Verify at https://learn.microsoft.com/en-us/powershell/scripting/install/powershell-support-lifecycle.
- **SQL**: name a real DBMS (PostgreSQL, SQL Server, MySQL, SQLite), exact engine/dialect/driver and supported version; assess migration/data loss and backwards compatibility. PostgreSQL versioning: https://www.postgresql.org/support/versioning/.
- **Explicit user choice** overrides *default popularity/maturity preference*, **not** host safety/AGENTS/Path Guard/data protection or separate implementation permissions. A newly supported major can be designed by user preference; preview/EOL/high-risk may remain blocked by security and ownership requirements.

## Evidence ledger

| Audit | Result |
| --- | --- |
| 23 affected/related Markdown documents inspected against GitHub committed tree `3eafc91af8dd` | 260 Markdown link targets, 0 missing internal file targets |
| System RTM primary feature map | 37/37 unique F01–F37 references |
| Cross-cutting RTM rows | NFR-001..009, nine distinct rows; old historical counts corrected |
| Source/host applicability | Present in both root AGENTS and portable .source/SKILL.md and main technology policy |
| Explicit override | Template exists, requirement NFR-009, scope/risk/approval rules; **no concrete host override requested or executed** |
| A.1 independent design validation | NOT RUN; policy not independently approved |
| B.1 host/runtime validation | NOT RUN; future B not authorized |
| S2C/host Python/PowerShell/SQL/database edits | NONE under this plan |
| P0 Path Guard/Workflow Guard issues from parent PR #7 | Remain OPEN, no code fix/acceptance claimed |
| Latest exact-head CI | Separate GitHub Actions checks required; static docs audit does not prove security or runtime STOP |

## Design handoff / next safe action

1. Independently review thresholds (default preference vs explicit user override), risk scoring, policy authority and representative host code/SQL migration scenarios in **A.1 once full SRS/design is ready**.
2. For a real S2C or host tech decision, inspect the exact repository/version, collect `TECH-ID`, then `OVR-ID` only if user explicitly chooses a nondefault stack/version/structure. Do not retroactively alter a framework by inserting this documentation.
3. Later coding-enforcement or automated version checks require an independently scoped B plan with tests and permission. Neither user preference nor design documents alone are an instruction to upgrade a runtime.
4. Keep Draft PR #8 and parent #7 unmerged until appropriate reviewer gates and separate approval.

**Persistence:** this handoff is versioned in the specified branch after GitHub commit; not a live S2C session FINISH/MERGE. Rollback is documentation-only; preserve existing source, host state and historical handoffs.
