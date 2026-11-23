# Phase A — Google BRD ↔ Git SRS Semantic Reconciliation (27 BR)

**AUTHOR_SOURCE_COMPARISON / NO_BUSINESS_SIGNOFF / SHA_BOUND.** This report compares **native Google Docs text** against the **Git SRS**, not a copied ZIP. Audited Git SHA `79a45e0486ea8792a49fd9e7fa4a85c89ec4ca82`, branch `s2c/PhaseA`, path `.agents/.spec.md`. Google source [BRD_Spec2Code](https://docs.google.com/document/d/1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4/edit), **Draft v1.5**, exact read revision `AHj4eMTQo-4II6DrQF5kSGoY8OxDNISChHco-PFSx_OgzuUuEWu4R2qAsiNmlioUDwDF-cYLmUq__B8TxyeB5iOzSa8tL5uDM_9Rqh0Npw` (475 paragraphs as observed). Source paragraph labels below are **1-based extraction positions (P#)**, not permanent Google Docs anchors. Git locators are **input-file line numbers**, which shift after edits; the input SHA keeps them reproducible.

## Decision summary

The 27 requirement IDs are present on both sides **exactly once as primary requirement entries** under the source-matching method. These are **semantic candidate crosswalks only**, never owner-certified equivalence, approval or execution proof. All Git and Google requirements remain draft. Two concrete comparison issues need editorial clarification: **BR-003** (Google explicitly distinguishes 7/9/5 layers, while Git's primary table is generic despite its later detailed §5), and **BR-027** (Google explicitly marks 100% mandatory AC and >95% line/branch thresholds as unapproved proposals; Git's short BR group title could be mistaken for a binding threshold despite the detailed AC worksheet noting it is draft). Reviewer-group BR-017..021 are directionally similar, but autonomous worker support and human independent A.1 cannot be conflated.

| Group | Count | Meaning |
| --- | ---: | --- |
| APPROVAL_PENDING (generic draft) | 13 | Candidate aligned in intent but no owner approval |
| WORDING_DELTA | 1 | Primary SRS row should explicitly reflect 7/9/5 layers |
| SCOPE_DECISION_PENDING | 2 | BR-007/008 owner chooses reference-only or added Web test oracles |
| REVIEWER_SCOPE_PENDING | 5 | Worker/persona evidence not independent A.1 signature |
| FUTURE_AC_PENDING | 5 | BR-022..026 proposed future-scope acceptance remains owner-defined |
| METRIC_AUTHORITY_DELTA | 1 | BR-027 metric is only candidate |
| **Total** | **27** | **0 / 27 signed semantic equivalence approvals** |

## Per-BR source, behavior and resolution matrix

| BR ID | Google paragraph | Git SRS line at audited SHA | Shared behavior / differentiator | Comparison classification | Outstanding owner decision |
| --- | --- | --- | --- | --- | --- |
| BR-001 | P139 | L59 | Authorized checkout: scope/escape/sentinel | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-002 | P140 | L60 | Host policy ownership: root/nested AGENTS precedence | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-003 | P141 | L61 | Three-layer lifecycle: seven business / nine task / five machine phases | `WORDING_DELTA` | Approve exactly 7 business / 9 per-task / 5 runtime description; no runtime migration |
| BR-004 | P142 | L62 | Independent A.1/B.1: distinct reviewer and observed evidence | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-005 | P143 | L63 | Bidirectional traceability: BR→AC/design/task/risk/source/test | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-006 | P144 | L64 | Risk scoring each iteration: scenario,cause,evidence,L/I,BEFORE/AFTER | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-007 | P145 | L65 | Risk grouping: member causality and no hidden P0 | `SCOPE_DECISION_PENDING` | Choose REFERENCE_ONLY or reviewed assertion in existing Web cases |
| BR-008 | P146 | L66 | Mitigation research: verifiable provenance,alternative,experiment | `SCOPE_DECISION_PENDING` | Choose REFERENCE_ONLY or reviewed assertion in existing Web cases |
| BR-009 | P147 | L67 | Scoped risk treatment: highest exposure and permissions | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-010 | P148 | L68 | STOP/HANDOFF/RESUME: persistence and fresh permission | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-011 | P149 | L69 | Bounded private context: mandatory policy and secret redaction | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-012 | P150 | L70 | Optional read-only Spec Kit: feature containment and blocking | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-013 | P151 | L71 | Stable tech and override: compatibility evidence and no security bypass | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-014 | P152 | L72 | Owned docs/recoverable cleanup: current source owner and no unowned deletion | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-015 | P153 | L73 | Install/recovery: fresh copied bundle and OS fixtures | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-016 | P154 | L74 | Release dossier: versions,skips,risk,rollback,owner | `APPROVAL_PENDING` | Approve exact source revision and AC meaning |
| BR-017 | P155 | L75 | Weighted reviewer workers: n=1 cannot imply independent A.1 | `REVIEWER_SCOPE_PENDING` | Agree future reviewer mechanics and distinct human A.1/B.1 |
| BR-018 | P156 | L76 | Review source evidence: independent worker context is not human signature | `REVIEWER_SCOPE_PENDING` | Agree future reviewer mechanics and distinct human A.1/B.1 |
| BR-019 | P157 | L77 | Synthesis/dissent: no consensus-based P0 waiver | `REVIEWER_SCOPE_PENDING` | Agree future reviewer mechanics and distinct human A.1/B.1 |
| BR-020 | P158 | L78 | Review handoff/provenance: source/config fingerprint and no extra permission | `REVIEWER_SCOPE_PENDING` | Agree future reviewer mechanics and distinct human A.1/B.1 |
| BR-021 | P159 | L79 | Review tests/acceptance: A.1 vs B.1 separated; no self-scored review | `REVIEWER_SCOPE_PENDING` | Agree future reviewer mechanics and distinct human A.1/B.1 |
| BR-022 | P460 | L89,102 | Impact/contract graph: owner-selected graph, unknown edges | `FUTURE_AC_PENDING` | Approve concrete future AC inputs/method; not a V1 runtime claim |
| BR-023 | P461 | L90,103 | Path Guard/delegation: host OS+negative sentinel fixture | `FUTURE_AC_PENDING` | Approve concrete future AC inputs/method; not a V1 runtime claim |
| BR-024 | P462 | L91,104 | Quality/DBA gate: dialect,oracle,coverage,independent tests | `FUTURE_AC_PENDING` | Approve concrete future AC inputs/method; not a V1 runtime claim |
| BR-025 | P463 | L92,105 | Context/SLM budget: benchmarks,cap,secret fixture | `FUTURE_AC_PENDING` | Approve concrete future AC inputs/method; not a V1 runtime claim |
| BR-026 | P464 | L93,106 | Source/spec/schema/API rollback: stack,data,rollback/price owner | `FUTURE_AC_PENDING` | Approve concrete future AC inputs/method; not a V1 runtime claim |
| BR-027 | P465 | L94,107 | Protected Core self-evolution: 100% mandatory AC and >95% scoped coverage DRAFT | `METRIC_AUTHORITY_DELTA` | Approve applicability, denominator and exact threshold or revise |

## Source-specific findings and proposed repair

1. **BR-003:** Google Draft v1.5 directly identifies **7 business stages / 9 task execution steps / 5 existing Workflow Guard phases**, with explicit warning against creating 3 new state machines. Git §5 already explains the nine task steps and the five existing machine phases, but the **primary table row** does not display the count/relationships. Proposed *editorial-only* wording will make the distinction explicit, not add runtime phases or call it owner-approved.
2. **BR-007 and BR-008:** Git marks both as `Should`; Google describes risk grouping and research mitigation, not signed exclusions. The Web profile currently has **no direct case oracle** for these two groups. `REFERENCE_ONLY` is only the author's V1 suggestion until Product+QA select an alternative or adapt existing cases. No false claim that the business requirements are deleted.
3. **BR-017..021:** Google Draft stresses reviewer provenance, role coverage, quorum/budget, source grounding and dissent, and that **n=1 does not mean independently reviewed**. Git rows largely align in intent but do not supply separate human reviewer appointments or proof of provider worker isolation. Add a row-level caveat in BR-017; keep A.1/B.1 independently signed.
4. **BR-022..026:** Google describes the proposed source graph, permission/sentinel boundaries, quality/DBA, context budgeting and schema/rollback; Git provides more detailed positive/negative oracles and open owner parameters. Label these **candidate design elaborations**, not proven semantic parity or supported Web runtime capabilities.
5. **BR-027:** Google explicitly says proposed **100% mandatory AC** and **>95% line+branch coverage** are unapproved targets, pending scope/denominator. Git details already say this, but the overview table omits the `DRAFT` qualifier. Correct the table title to `candidate thresholds; owner approval pending` without waiving the mandatory protected-core denial.
6. **V1 release scope:** A separate **confirmed requester-level V1 environment scope** permits read/upload through ChatGPT Web and **specifically authorized remote GitHub API AGENTS-only writes**. Current SRS tail says only read/no agents; this is a **confirmed superseding description**, not new generic Git/code write permission. Update the active row while preserving explicit gate rules. Native Windows/Linux/macOS local agent writes remain excluded, and RM-001 global P0 OPEN.

## Authority, revision and acceptance boundary

**Proposed authority separation:** Versioned Git SRS is the current technical authoring master; the Google BRD draft is a stakeholder review surface until a real Product Owner approves **exact Google revision + exact final Git SHA + per-BR semantic delta disposition**, then records the normative business rule/source snapshot. When the two conflict, report `DRIFT/OWNER_REQUIRED`, do not auto-prefer recency or overwrite requirements. If a new Google revision is observed, invalidate this matrix and rerun source paragraphs/accepted decisions. A raw ZIP or pasted file has independent provenance; simultaneous Git/ZIP same-path conflicts must STOP affected tasks rather than silently selecting either source.

**Unchanged formal gates:** owner handles, true human independent A.1/B.1, Web-specific KPI `R>99.99%` denominator, BR-007/008 decision, 52 risk applicability dispositions, real remote provider/host path grants and approved V1 test oracles remain pending. **21 Web cases NOT_RUN; A.1 NOT_RUN; B NOT_AUTHORIZED; B.1 NOT_RUN; no release.** This is not the final signed baseline pair.

## Reviewer decision record template (no inferred approval)

`reviewId, ProductOwnerHandle, sourceGitSHA, googleDocumentId, googleRevisionId, BR_ID, semanticDisposition(ACCEPT/REVISE/BLOCK), approvedBusinessTextRef, ACRef, ownerDecisionDate, independentReviewRef`. A source URL alone does not grant `ACCEPT`. Keep unresolved BR values `OWNER_PENDING`.
