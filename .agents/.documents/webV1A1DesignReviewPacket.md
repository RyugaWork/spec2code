# Web v1.0 — Independent A.1 preparation and decision handoff

Date: 2026-11-23; reviewer input candidate `fa2ba44e4a2076cf004160831fdaa7a3f2ec8148` (must re-pin to post-documentation commit before review). **AUTHOR_PREPARATION_ONLY / OWNER_REVIEW_PENDING**. This packet is not a signed validation report. [Review criteria authority](../.workflow/validationSpecification.md), [template](../.workflow/validationReportTemplate.md), [owner decisions](webV1OwnerDecisionRegister.md).

## Proposed Web architecture / ADR choices for owner signoff

| Design choice | Recommendation and limitation | Required owner / status |
| --- | --- | --- |
| ADR-WEB-01 scope and external boundaries | Restrict v1 distribution to allowlisted Markdown. Manual ChatGPT Web can read only actual supplied material or permitted provider sources. No shell, Python, local Path Guard, auto workers, native Spec Kit CLI or CI. Provider/tool access is neither presumed nor OS sandbox enforcement. | Product + Security; OWNER_PENDING |
| ADR-WEB-02 authority and artifacts | Development root `AGENTS.md` governs the S2C repository, not universal host files. The host owns existing AGENTS and customized docs; upstream Spec Kit owns `.specify/` and `specs/`. Future package under `.source/profiles/web/` only after B, no distribution of prototype scripts/config. | Architecture + Host; OWNER_PENDING |
| ADR-WEB-03 version/data contract | Candidate `productVersion=1.0.0`, `schemaVersion=1`, independently pinned `bundleVersion`, release commit/checksums; `UNKNOWN` is not permission. Manual three-way migration and rollback, manifest version updated last after verified readback. | Architecture + Host; OWNER_PENDING |
| ADR-WEB-04 Git integration | Maintain one documentation branch, no forced merge. Reconcile main's unique change, four stacked draft PRs, external reviewer findings and Google BRD semantic source parity; release only from separately approved immutable source. | Git Integrator + Release Owner; OWNER_PENDING |
| ADR-WEB-05 QA and release policy | All 21 Web case oracles proposed, QA/owner defines valid mandatory groups, denominator and evidence. Independent A.1 required before Phase B, independent B.1 after implementation; no P0 waiver, no approval-by-author. | QA + Security + Product; OWNER_PENDING |

These proposed ADR names do not supersede existing architecture decisions/BRD and are not new runtime feature identifiers.

## A1-VAL-01..09 independent reviewer prep matrix

| Gate | Evidence available to review | Open question / blocker | Author-prep status |
| --- | --- | --- | --- |
| A1-VAL-01 Source authority | PLAN-116, master SRS, Web DEC packet, Git PR baseline | Product owner must approve exact Web BR/AC and Git/Google source relation | NEEDS_OWNER |
| A1-VAL-02 Requirements and AC | [15 AC crosswalk](webV1AcceptanceAndTraceability.md), [canonical tests](../.workflow/testingAndDelivery.md) | ACs, mandatory group metrics/denominators, consented test fixtures unsigned | NEEDS_OWNER_QA |
| A1-VAL-03 Bidirectional RTM | [64-feature mapping](webV1PreflightAndCapabilityMatrix.md), [RTM](../.traceMatrix.md) | Confirm Web-only requirement reverse traces, orphans and exclusions | NEEDS_REVIEW |
| A1-VAL-04 Feature design | Manual Web stages and authority from PLAN-116; negative paths from WEB-TC | Confirm denied/blocked paths and host ownership on concrete fixture | NEEDS_REVIEW |
| A1-VAL-05 Architecture/workflow | ADR-WEB-01..05 proposals, STOP/RESUME and package plan | Version/schema authority, effective provider boundary and release target unsigned | NEEDS_OWNER |
| A1-VAL-06 Risk discovery | [52-row risk applicability overlay](webV1RiskApplicability.md), existing 52 global IDs | Security owner must validate each profile exposure and exclusions | NEEDS_SECURITY |
| A1-VAL-07 Risk management | Existing L/I/E risk register, RM-001 P0 OPEN, negative test designs | No residual-risk treatment verification, unsupported P0 waiver forbidden | BLOCKED_RISK |
| A1-VAL-08 Design handoff | [WEB task ledger](../.plans.md), owner packet and this review prep | Bind final source SHA, responsible owner/reviewer, explicit next task | PREPARED_NOT_SIGNED |
| A1-VAL-09 Independent signoff | Existing formal review criterion/template | No actually independent reviewer or source-bound nine-gate report | NOT_RUN |

### Independent review procedure (not executed)

The named reviewer must independently inspect the **exact resulting Git SHA** and authoritative stakeholder source, compare BR/AC authority, review 64-feature scope + 52-risk overlay + proposed tests and negative scenarios, record criterion-specific PASS/FAIL/BLOCKED with evidence and dissent, and sign the proper validation report. Same-model multiple perspectives, self-review, or author-created statuses do not qualify. A scope/contract change returns to A/A.1.

## Approved and unapproved activities boundary

- **Allowed now (A):** document drafting, risk applicability proposal, static path/ID preflight, review packet preparation, owner questions.
- **Blocked until A.1 + separate B:** actual `.source/profiles/web/` portable product implementation, host files, automatic Git write/profile installer, runtime/source/CI modifications.
- **Blocked until implementation + evidence:** 15 actual Web tests, migration/restore evidence, independent B.1, published release tag and release owner signoff.
- **Persistent global blocker:** RM-001 P0 L4×I5=20 OPEN; Web-only exclusion does not repair the Windows runtime or authorize any local write.

## Handoff queue

| Owner action | Owner role | Minimum evidence / outcome |
| --- | --- | --- |
| Accept/revise DEC-WEB-01 and scopes across F01..64 | Product + Security | Approved Web profile boundary, precise permissions/provider/data treatment and source SHA |
| Accept/revise DEC-WEB-02/03 and ADR-WEB-01..05 | Architecture + Git/Host | Contract, ownership/target, version/schema and integration decision |
| Accept/revise DEC-WEB-04 and 21 AC/group decisions | Product + QA | BR/source authority, case oracles, group method, test fixtures and evidence |
| Decide applicability for RM-001..052 | Security Owner | 52 row dispositions + mandatory negative test plan, no open applicable P0 |
| Conduct scoped A.1 | Actually independent reviewer | Exact-SHA A1-VAL-01..09 report, dissent and dated identity |
| Authorize B if A.1 passed | Responsible Product/Host Owner | **Separate** explicit scope for WEB-006..020, not inferred by reading this document |

**Result:** `REVIEW_PACKET_DRAFTED / A1_NOT_RUN / B_NOT_AUTHORIZED / B1_NOT_RUN / NO_RELEASE`.

## Scope change for A.1 reviewer — agent-executed AGENTS integration (2026-11-23)

Re-evaluate A1-VAL-01/02 for [DEC-WEB-06 and 17 AGM rows](webV1AgentsIntegrationMatrix.md), A1-VAL-03 for new WEB-TC-16..21 reverse mappings, A1-VAL-04/05 for create/adopt/upgrade/three-way conflicts, A1-VAL-06/07 for AGENTS write/owner risks and A1-VAL-08/09 for approval/readback/rollback evidence. Proposed **ADR-WEB-06:** S2C is the declarative source only; a separately authorized AI agent performs AGENTS writes using real capabilities, otherwise outputs a patch/handoff. This is a **new design candidate** and invalidates any older scoped approval assumptions, though no previous independent A.1 PASS exists. **21 test designs, 0 executions.** Bind any independent review to the final post-amendment SHA, not the initial candidate SHA quoted above. No host AGENTS change was made.

## Gemini feedback after AGENTS scope revision — independent-review gate correction

The reviewer must also inspect the [Gemini review disposition](webV1GeminiReviewDisposition20261123.md), particularly named independent reviewer identity/actual authority, BRD immutable owner-approved Git snapshot, proposed Spec Kit v1.4.3 read-only mapping boundaries and permissioned AGENTS host writes. A.1 baseline is **not yet frozen**: `d23e981073a8e4419d992b1b0fe4de0ee11730da` is an observed author input, not a signed scope-freeze SHA. Reconcile stacked PR #8–#11 and main's unique change before selecting one immutable final candidate. No role-lens/Gemini review substitutes for independent A1-VAL-09. A Web-only RM-001 exclusion requires distinct Security Owner scope/evidence for remote connector vs Codex/local Windows execution; the latter remains blocked pending OS proof. All 21 Web tests are NOT_RUN; no release acceptance is inferred.

## A-Closure source snapshot and independent reviewer handoff (2026-11-23)

Use [source-bound A-Closure evidence and REV-090 statuses](webV1AClosureEvidence20261123.md), [the 64-F/27-BR reverse matrix](webV1AClosureFeatureReverseMatrix20261123.md) and [21-case oracle worksheet](webV1AClosureWebTestOracleDesign20261123.md). Current Google BRD Draft v1.5 revision and pinned upstream Spec Kit v1.4.3 commit are recorded there. The identity/source/semantic/release decisions are explicitly in [owner packet](webV1AClosureApprovalPacket20261123.md); **do not freeze an old author SHA or self-sign A1-VAL-01..09**. Final independent reviewer must inspect the *post-author-commit exact SHA* after stakeholder decisions. `A1_NOT_RUN`, `RM-001 P0 OPEN`, `B_NOT_AUTHORIZED` remain.
