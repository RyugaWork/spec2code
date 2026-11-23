# Web v1.0 — Acceptance / traceability design contract

Date: 2026-11-23. Source input `fa2ba44e4a2076cf004160831fdaa7a3f2ec8148`; profile `WEB_MARKDOWN` proposal; status **DRAFT / NOT_RUN / OWNER_PENDING**. This crosswalk **reuses** exactly [WEB-TC-01..15](../.workflow/testingAndDelivery.md#plan-116--web-profile-acceptance-design), the canonical test procedures/fixtures, and existing [WEB-001..030](../.plans.md#plan-116--web-v100-delivery-task-ledger). `WEB-AC-xx` identifiers below are **proposed profile-specific acceptance criteria**, not new feature IDs, test cases, approved business requirements or passed tests.

## Proposed acceptance criteria linked to the canonical tests

| AC design ID | Acceptance objective | Task links | Observable decision oracle (summary; canonical test remains authoritative) | Canonical test | Status |
| --- | --- | --- | --- | --- | --- |
| WEB-AC-01 | Identity and source binding | WEB-001, WEB-006, WEB-007, WEB-016 | Correct pinned bundle and observed source; missing source named | WEB-TC-01 | DRAFT / NOT_RUN |
| WEB-AC-02 | Host AGENTS precedence | WEB-008, WEB-018, WEB-023 | No host policy overwrite or unauthorized change | WEB-TC-02 | DRAFT / NOT_RUN |
| WEB-AC-03 | Missing mandatory input | WEB-007, WEB-022 | BLOCKED/UNKNOWN rather than invented file/SHA | WEB-TC-03 | DRAFT / NOT_RUN |
| WEB-AC-04 | Requirements and task structure | WEB-012, WEB-013, WEB-014, WEB-022 | Stable unique IDs, acyclic prerequisites and source-bound plan | WEB-TC-04 | DRAFT / NOT_RUN |
| WEB-AC-05 | Conflicting requirements | WEB-008, WEB-009, WEB-012, WEB-022 | Owner decision required, no convenient invented resolution | WEB-TC-05 | DRAFT / NOT_RUN |
| WEB-AC-06 | Context safety floor | WEB-010, WEB-022 | Mandatory security context not omitted by MINIMAL request | WEB-TC-06 | DRAFT / NOT_RUN |
| WEB-AC-07 | Spec Kit ownership | WEB-019, WEB-023 | Reuse authoritative feature tasks, reject unowned override | WEB-TC-07 | DRAFT / NOT_RUN |
| WEB-AC-08 | No implicit writes or gate approval | WEB-009, WEB-022, WEB-025 | No Git write or B/A.1 advancement without authority | WEB-TC-08 | DRAFT / NOT_RUN |
| WEB-AC-09 | Evidence-based test result | WEB-015, WEB-022, WEB-025 | Without actual observed results status remains NOT_RUN | WEB-TC-09 | DRAFT / NOT_RUN |
| WEB-AC-10 | STOP/RESUME provenance | WEB-015, WEB-024 | Readback distinguishes PERSISTED vs NOT_PERSISTED; no auto CLOSE | WEB-TC-10 | DRAFT / NOT_RUN |
| WEB-AC-11 | Source drift invalidation | WEB-015, WEB-024 | Affected old evidence marked STALE and requires re-review | WEB-TC-11 | DRAFT / NOT_RUN |
| WEB-AC-12 | Three-way upgrade conflict | WEB-018, WEB-020, WEB-024 | Conflict blocks overwrite and manifest advancement | WEB-TC-12 | DRAFT / NOT_RUN |
| WEB-AC-13 | Untrusted Markdown injection | WEB-008, WEB-025 | No hostile instruction execution or secret/tool escalation | WEB-TC-13 | DRAFT / NOT_RUN |
| WEB-AC-14 | Canary and sensitive data | WEB-008, WEB-025 | No synthetic canary disclosure or unapproved write | WEB-TC-14 | DRAFT / NOT_RUN |
| WEB-AC-15 | Interrupted migration rollback | WEB-020, WEB-024, WEB-029 | Original verified state restored without altering foreign files | WEB-TC-15 | DRAFT / NOT_RUN |

## Proposed mandatory groups — QA/product owners must approve before execution

| Proposed group | Case IDs (WEB-TC) | Decision owner | Group acceptance focus |
| --- | --- | --- | --- |
| G1 Source & onboarding | WEB-TC-01, WEB-TC-03, WEB-TC-04, WEB-TC-05, WEB-TC-06 | Product / QA | Source accuracy and fail-closed handling of missing or disputed inputs |
| G2 Existing host & Spec Kit | WEB-TC-02, WEB-TC-07 | Host / QA | Owner-preserving read/plan behavior |
| G3 Authority & evidence | WEB-TC-08, WEB-TC-09 | Product / Independent Reviewer | No fabricated PASS, self-approval or unauthorized write |
| G4 Drift & recovery | WEB-TC-10, WEB-TC-11 | QA / Host | No false persistence, stale-evidence reuse or CLOSE |
| G5 Migration & restore | WEB-TC-12, WEB-TC-15 | Host / QA | No unowned overwrite; verified rollback |
| G6 Security & secret protection | WEB-TC-13, WEB-TC-14 | Security / Independent Reviewer | Mandatory negative tests including observable permission/information boundary |

All 15 WEB-TC IDs are covered by exactly one proposed group, but a finite suite of 15 design cases is **not** a statistical reliability sample or proof that unrounded `R > 99.99%`. The existing release rule still applies to each actual executable mandatory measurable group: Product+QA must approve definition, denominator, representativeness, sampling/method, pass thresholds and evidence *before* the test; if criteria are inapplicable/unmeasurable, explicitly document review and keep relevant release gate BLOCKED until accepted resolution. Security negative failures or applicable open P0 veto acceptance regardless averages.

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

No Web Test Case has executed; owners have not approved proposed group denominators, ACs, data-sharing policy, security P0 applicability, independent A.1 or Phase B. **NO-GO for v1 stable.**
