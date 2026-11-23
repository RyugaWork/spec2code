# Web v1.0 — Acceptance / traceability design contract

Date: 2026-11-23. Source input `fa2ba44e4a2076cf004160831fdaa7a3f2ec8148`; profile `WEB_MARKDOWN` proposal; status **DRAFT / NOT_RUN / OWNER_PENDING**. This crosswalk **reuses** baseline [WEB-TC-01..15] and extends it with [WEB-TC-16..21](../.workflow/testingAndDelivery.md#plan-116--web-profile-acceptance-design), the canonical test procedures/fixtures, and existing [WEB-001..030](../.plans.md#plan-116--web-v100-delivery-task-ledger). `WEB-AC-xx` identifiers below are **proposed profile-specific acceptance criteria**, not new feature IDs, test cases, approved business requirements or passed tests.

## Proposed acceptance criteria linked to the canonical tests

| AC design ID | Acceptance objective | Task links | Observable decision oracle (summary; canonical test remains authoritative) | Canonical test | Status |
| --- | --- | --- | --- | --- | --- |
| WEB-AC-01 | Identity and source binding | WEB-001, WEB-006, WEB-007, WEB-016 | Correct pinned bundle and observed source; missing source named | WEB-TC-01 | DRAFT / NOT_RUN |
| WEB-AC-02 | Host AGENTS precedence | WEB-008, WEB-018, WEB-023 | No host policy overwrite or unauthorized change | WEB-TC-02 | DRAFT / NOT_RUN |
| WEB-AC-03 | Missing mandatory input | WEB-007, WEB-022 | Offline complete-upload grounded plan; missing source BLOCKED/UNKNOWN, no invented SHA | WEB-TC-03 | DRAFT / NOT_RUN |
| WEB-AC-04 | Requirements and task structure | WEB-012, WEB-013, WEB-014, WEB-022 | Stable unique IDs, acyclic prerequisites and source-bound plan | WEB-TC-04 | DRAFT / NOT_RUN |
| WEB-AC-05 | Conflicting requirements | WEB-008, WEB-009, WEB-012, WEB-022 | Owner decision required, no convenient invented resolution | WEB-TC-05 | DRAFT / NOT_RUN |
| WEB-AC-06 | Context safety floor | WEB-010, WEB-022 | Mandatory security context not omitted by MINIMAL request | WEB-TC-06 | DRAFT / NOT_RUN |
| WEB-AC-07 | Spec Kit ownership | WEB-019, WEB-023 | Pinned Spec Kit v1.4.3 structure read-only; reuse feature tasks, reject unowned override and unknown versions | WEB-TC-07 | DRAFT / NOT_RUN |
| WEB-AC-08 | No implicit writes or gate approval | WEB-009, WEB-022, WEB-025 | No Git write or B/A.1 advancement without authority | WEB-TC-08 | DRAFT / NOT_RUN |
| WEB-AC-09 | Evidence-based test result | WEB-015, WEB-022, WEB-025 | Without actual observed results status remains NOT_RUN | WEB-TC-09 | DRAFT / NOT_RUN |
| WEB-AC-10 | STOP/RESUME provenance | WEB-015, WEB-024 | Readback distinguishes PERSISTED vs NOT_PERSISTED; no auto CLOSE | WEB-TC-10 | DRAFT / NOT_RUN |
| WEB-AC-11 | Source drift invalidation | WEB-015, WEB-024 | Affected old evidence marked STALE and requires re-review | WEB-TC-11 | DRAFT / NOT_RUN |
| WEB-AC-12 | Three-way upgrade conflict | WEB-018, WEB-020, WEB-024 | Conflict blocks overwrite and manifest advancement | WEB-TC-12 | DRAFT / NOT_RUN |
| WEB-AC-13 | Untrusted Markdown injection | WEB-008, WEB-025 | No hostile instruction execution or secret/tool escalation | WEB-TC-13 | DRAFT / NOT_RUN |
| WEB-AC-14 | Canary and sensitive data | WEB-008, WEB-025 | No synthetic canary disclosure or unapproved write | WEB-TC-14 | DRAFT / NOT_RUN |
| WEB-AC-15 | Interrupted migration rollback | WEB-020, WEB-024, WEB-029 | Original verified state restored without altering foreign files | WEB-TC-15 | DRAFT / NOT_RUN |
| WEB-AC-16 | New host AGENTS creation | WEB-016, WEB-018, WEB-023 | Agent-executed CREATE only with verified absence, approved source/policy/path and readback | WEB-TC-16 | DRAFT / NOT_RUN |
| WEB-AC-17 | Existing/nested host AGENTS preservation | WEB-008, WEB-018, WEB-023 | Only bounded authorized insert; original and nested rules unchanged | WEB-TC-17 | DRAFT / NOT_RUN |
| WEB-AC-18 | S2C-adopted section version upgrade | WEB-011, WEB-017, WEB-018, WEB-020, WEB-024 | Old/current/new three-way comparison preserves custom content and version updated last | WEB-TC-18 | DRAFT / NOT_RUN |
| WEB-AC-19 | Conflict and denied AGENTS path | WEB-008, WEB-018, WEB-023, WEB-025 | STOP/HANDOFF, independently verified no unauthorized effects | WEB-TC-19 | DRAFT / NOT_RUN |
| WEB-AC-20 | Idempotence and source drift | WEB-017, WEB-020, WEB-024 | Same version NO_CHANGE; stale write denied and re-reviewed | WEB-TC-20 | DRAFT / NOT_RUN |
| WEB-AC-21 | Provider unavailable / untrusted authority | WEB-008, WEB-016, WEB-025 | Matrix/diff only; no inferred write/commit, secrets or false persistence | WEB-TC-21 | DRAFT / NOT_RUN |

## Proposed mandatory groups — QA/product owners must approve before execution

| Proposed group | Case IDs (WEB-TC) | Decision owner | Group acceptance focus |
| --- | --- | --- | --- |
| G1 Source & onboarding | WEB-TC-01, WEB-TC-03, WEB-TC-04, WEB-TC-05, WEB-TC-06 | Product / QA | Source accuracy and fail-closed handling of missing or disputed inputs |
| G2 Existing host & Spec Kit | WEB-TC-02, WEB-TC-07 | Host / QA | Owner-preserving read/plan behavior |
| G3 Authority & evidence | WEB-TC-08, WEB-TC-09 | Product / Independent Reviewer | No fabricated PASS, self-approval or unauthorized write |
| G4 Drift & recovery | WEB-TC-10, WEB-TC-11 | QA / Host | No false persistence, stale-evidence reuse or CLOSE |
| G5 Migration & restore | WEB-TC-12, WEB-TC-15 | Host / QA | No unowned overwrite; verified rollback |
| G6 Security & secret protection | WEB-TC-13, WEB-TC-14 | Security / Independent Reviewer | Mandatory negative tests including observable permission/information boundary |
| G7 AGENTS.md integration | WEB-TC-16, WEB-TC-17, WEB-TC-18, WEB-TC-19, WEB-TC-20, WEB-TC-21 | Host / Security / Independent Reviewer | Real authorized create/adopt/upgrade, conflict denial and idempotent readback |

All 21 WEB-TC IDs are covered by exactly one proposed group, but a finite suite of 21 design cases is **not** a statistical reliability sample or proof that unrounded `R > 99.99%`. The existing release rule still applies to each actual executable mandatory measurable group: Product+QA must approve definition, denominator, representativeness, sampling/method, pass thresholds and evidence *before* the test; if criteria are inapplicable/unmeasurable, explicitly document review and keep relevant release gate BLOCKED until accepted resolution. Security negative failures or applicable open P0 veto acceptance regardless averages.

## Evidence schema for every eventual execution

Record `caseId`, `acId`, `group`, release bundle/version/checksum, source Git SHA or `UNKNOWN`, original input/fixture hash, host/provider capability observation, allowed read/write permissions, actual GPT Web transcript excerpt (synthetic/redacted), actual outcome `PASS|FAIL|BLOCKED|NOT_RUN|INCONCLUSIVE`, reproduction, executor, independent reviewer (if required), date, risk ID, issue/rollback, and immutable evidence link. Presence of Markdown instructions only means `DESIGNED`; no `PASS` without actual tool/host observations. Authorization and product-version claims remain separate.

## Bidirectional trace and owner dependencies

- Design authority: [PLAN-116](markdownFirstReleasePlan.md) + [pending DEC-WEB-01..05](webV1OwnerDecisionRegister.md); this AC draft does not replace owner-approved BR/AC or the master SRS.
- Feature applicability: [64-row feature matrix](webV1PreflightAndCapabilityMatrix.md), statuses not promoted.
- Risk: [52-row scope overlay](webV1RiskApplicability.md), all decisions pending; scope changes trigger fresh mapping and A.1.
- Implementation: WEB-006..020 are **not authorized**; no profile exists or package acceptance can be inferred.
- Verification: WEB-021..025 require actual static/functional/adversarial evidence on an exact candidate, not this author-preflight.
- Final gate: WEB-026..030 require reviewed final RTM, risk disposition, independent B.1, immutable allowlisted Markdown payload, separate release decision.

## Current stop state

No Web Test Case (WEB-TC-01..21) has executed; owners have not approved proposed group denominators, ACs, data-sharing policy, security P0 applicability, independent A.1 or Phase B. **NO-GO for v1 stable.**

**Integration design amendment:** [AGM-01..17](webV1AgentsIntegrationMatrix.md) defines declarative content and a permissioned agent-execution path. These six ACs and cases are design-only; their host-write proof requires actual before/after evidence, not merely a Markdown diff.

## Proposed U-04 Web metric / source authority clarification (Gemini review)

[Owner addendum](webV1GeminiReviewDisposition20261123.md) proposes deterministic **100% of applicable mandatory Web test variants and all security-negative tests PASS** with evidence. This is **not yet approved** as a replacement for the global unrounded `R>99.99%` rule, whose applicability/denominator or scoped amendment requires Product+QA decision in canonical governance. Keep 21 case IDs, all NOT_RUN; subvariants of WEB-TC-03 count as distinct observed fixtures under the same case ID. Normative Google BRD acceptance requires an owner-approved exact revision and authorized immutable Git-linked snapshot/hash; a live Draft URL alone has no approved AC authority.

## 21-case A-Closure execution precision supplement (2026-11-23)

[Per-case observable oracles, negative signals and required proof](webV1AClosureWebTestOracleDesign20261123.md) supplement the canonical case identities without adding duplicate test IDs. [Proposed BR/F reverse coverage](webV1AClosureFeatureReverseMatrix20261123.md) explicitly marks BR-007/008 without a direct Web case; owner must approve REFERENCE_ONLY or refine a canonical fixture. All `WEB-AC-01..21` remain DRAFT / NOT_RUN and their corresponding 21 canonical cases remain NOT_RUN. Inherited quality threshold requires Product+QA decision before treating a deterministic-case metric as a sufficient release criterion.

## Requester conditions on source and AGENTS acceptance (2026-11-23)

[Decision record](webV1RequesterConditionalDecisions20261123.md) adds proposed `WEB-TC-03-C` **subvariant** (simultaneous GitHub/ZIP same-path mismatch => conflict and no hidden precedence) and strengthens `WEB-TC-18/19/20` to assert **BLOCKED/no-write/no retry on unchanged customized-AGENTS conflict**. The canonical 21 IDs and 21 ACs stay unchanged; no verdict can be promoted from a designed case. BR-007/008 and Git-versus-Google normative authority are **Product/QA decision pending** (author recommends reference-only BR-007/008 for V1 and Git technical master with owner-approved Google business snapshot).
