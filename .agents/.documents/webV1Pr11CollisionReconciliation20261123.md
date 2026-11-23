# PLAN-116 — PR #11 unique-delta and ID collision reconciliation (2026-11-23)

**AUTHOR REVIEW / PR11_NOT_MERGED / ARCH_GIT_OWNER_PENDING.** Main author branch source `e8efc36b78f991efc618d1ca98865609d032bb0d`, historical PR #11 branch head `e119100e17ed138a1bbd1d2b600d9b890d5441b7`, historical parent `1dae9338f4d38518e897212cdf80ba47239a7671`. These are source comparison SHAs, **not** an approved A.1 baseline. [Existing REV-090 finding audit](webV1AClosureEvidence20261123.md) records the ten review findings; no human independent signature is inferred from that report.

## 1. Inspected historical delta

PR #11 adds **3 unique commits and 7 changed paths** against its historical parent. The specific paths and additions are:

| Path | Additions | Distinct content |
| --- | ---: | --- |
| `.agents/.features.md` | 19 | Different F43..F50 identifiers and proposed module registry |
| `.agents/.handoffs/plan-090-a1-preflight-review.md` | 150 | Historical REV-090-01..10 author-side findings; preserve historical source |
| `.agents/.plans.md` | 23 | Proposed T091-01..10 module/CI plan |
| `.agents/.riskMatrix.md` | 16 | Reuses RM-034..040 with **different** threats and scoring |
| `.agents/.spec.md` | 97 | New Section 18 / PLAN-091 module contract, which **collides** with current Section 18 review-contract owner |
| `.agents/.traceMatrix.md` | 17 | Proposed S2C-REQ-043..050, AC-MOD-01..10 tied to colliding F IDs |
| `AGENTS.md` | 8 | Alternative PLAN-091 CI/adapter governance policy; no automatic host-wide override |

**Direct conflict:** current F43=AST, F44=AI Firewall, F45=semantic Spec-Code drift, F46=feature evolution, F47=coding conventions, F48=strict fail-safe, F49=GPT Web/Codex routing, F50=lightweight CI/SLM. PR #11 reuses all eight for different proposals. The PR also redefines `PLAN-091` / `T091` and `RM-034..040`, while those IDs already have active canonical meanings in current [feature design](featureDesign.md), [technical SRS](../.spec.md), [global risk ledger](../.riskMatrix.md) and [RTM](../.traceMatrix.md). This is a **semantic trace collision even though the original PR diff is append-heavy**. Unreviewed cherry-pick/whole-file merge is unsafe.

## 2. Candidate PR #11 concept mapping (not an ID reassignment)

| Historical PR11 alias | Proposal | Candidate current existing F | Proposed treatment | Compatibility limitation |
| --- | --- | --- | --- | --- |
| PR11-F43 | Capability Registry / module manifest | F54; F08; F44 | `PROPOSED_REUSE` | F43 on current branch is AST manipulation, no registry runtime |
| PR11-F44 | Adapter contract negotiation | F54; F53; F07 | `PROPOSED_REUSE` | F44 on current branch is AI Firewall/RBAC; no provider admission proof |
| PR11-F45 | Fail-closed fallback / circuit breaker | F48; F59; F44 | `PROPOSED_REUSE` | F45 on current branch is semantic Spec-Code drift |
| PR11-F46 | Scoped Auto-Approve / external tool execution | F44; F64; F48 | `BLOCKED_POLICY` | F46 on current branch is controlled feature evolution; self-approval forbidden |
| PR11-F47 | Bounded multi-worker scheduler / handoff | F38..F42; F33; F37 | `PROPOSED_REUSE` | F47 on current branch is official coding conventions; real workers NOT_RUN |
| PR11-F48 | Browser UI/E2E adapter | F47; F52 | `UNMAPPED_ADAPTER` | F48 on current branch is strict fail-safe; browser runtime not implemented |
| PR11-F49 | CI/CD admission firewall | F50; F62; F44 | `PROPOSED_REUSE` | F49 on current branch is GPT Web/Codex routing; no CI dispatcher |
| PR11-F50 | Jules cloud PR worker adapter | F54; F38..F42; F63 | `UNMAPPED_PROVIDER` | F50 on current branch is lightweight CI/SLM; external account/API unverified |

These associations are **conceptual overlaps**, not feature-equivalent implementations, approved extensions or permission grants. Preserve current F43..F64 IDs and feature statuses. Do not create F65 just to resolve a number collision. If a future truly distinct adapter is required, Architecture Owner must assign a reviewed new capability contract and versioned ID without overwriting existing history.

## 3. Candidate risk relationships (no merging scores)

| Historical PR11 risk alias | Threat | Related current risk IDs | Existing current ID must not be overwritten |
| --- | --- | --- | --- |
| PR11-RM-034 | Untrusted plugin/manifest gets broader tools | RM-043, RM-047, RM-031 | Current RM-034 covers protected-core bypass |
| PR11-RM-035 | Fallback drops Path Guard/AC/tests | RM-043, RM-046, RM-049 | Current RM-035 covers untrusted code with CI/LLM credentials |
| PR11-RM-036 | CI trigger/token/action gives unauthorized dispatch | RM-035, RM-043, RM-047 | Current RM-036 covers workspace collision/cleanup |
| PR11-RM-037 | Provider prompt/tool injection forges approvals | RM-031, RM-041, RM-051 | Current RM-037 covers semantic/AST information loss |
| PR11-RM-038 | CLI exit 0 despite denial is marked PASS | RM-049, RM-046 | Current RM-038 covers DBA/quality false positives |
| PR11-RM-039 | Provider API/version/contract drifts | RM-032, RM-046, RM-049 | Current RM-039 covers token/CI/SLM costs/policy loss |
| PR11-RM-040 | Cloud worker overexposes secrets/Git credentials | RM-043, RM-048, RM-035 | Current RM-040 covers irreversible retry/feature flags |

Risk relationships are **proposed**; shared theme is not confirmed shared root cause. Preserve all original L/I, P0 status and evidence in RM-001..052. RM-001 stays P0 OPEN (4×5=20). No PR #11 threat is declared closed or accepted by mapping it to a different identifier.

## 4. Integration decisions and next admissible action

| Decision | Recommendation | Authority |
| --- | --- | --- |
| PR11-C01 identifiers | Keep existing F43..64, RM-034..52, S2C-REQ/PLAN-091 references; historical PR11 names are review aliases only | Architecture Owner |
| PR11-C02 design reuse | Accept only reviewed nonduplicate policies using current F54/F48/F44/F47/F52 and others; defer browser/CI/cloud/runtime adapter additions beyond Web V1 | Architecture + QA |
| PR11-C03 PR disposition | No wholesale PR #11 merge/cherry-pick; retain the historical handoff; optionally reconcile one bounded approved docs patch, then Git Owner may close/supersede PR | Git/Release Owner |
| PR11-C04 target branch | Resolve stacked PR #8–#11 and main unique `.gitignore` change; one approved integrated baseline for A.1, then one Phase B branch if authorized | Git/Release Owner |
| PR11-C05 threat mapping | Review cause/evidence before linking risk aliases; never replace RM IDs/scores or waive current P0 | Security Owner |

**Web V1 boundary:** S2C Markdown-first, read-only source intake plus separately authorized *remote GitHub API AGENTS-only writes*; no local Codex/OS write, autonomous worker orchestration, CI/CD admission, browser runner or Jules adapter in V1. Existing 17 AGMs/21 Web test IDs remain untouched, all actual tests NOT_RUN. No PR merge/tag/branch is authorized by this analysis.

**Verified method:** GitHub PR #11 base-to-head comparison and readback of its six pre-existing changed files compared to corresponding current-branch text. The special `.agents/.spec.md` delta includes non-tail insertions, so appending only the new tail is not a safe merge method. No independent merge trial, host/runtime tests or A.1 PASS.
