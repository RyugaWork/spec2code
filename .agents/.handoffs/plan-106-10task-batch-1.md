# PLAN-106 — Batch 1 of 5: ten governance and traceability tasks

**Base:** `847a4b3fb1de1bcc8e93163ed52954570f99338e` on `docs/plan-089-a1-readiness`. **Output:** the Git commit containing this handoff; read back branch HEAD. **Mode:** docs-only via GitHub connector, not a Codex CLI session. **Review type:** author-side, not independent A.1.

| ID | Existing owner file | Delivered scope | Author status |
| --- | --- | --- | --- |
| R01 | `AGENTS.md` | Governance precedence | DOCUMENTED / STATIC_PRECHECK |
| R02 | `.agents/.spec.md` | Requirement state invariants | DOCUMENTED / STATIC_PRECHECK |
| R03 | `.agents/.traceMatrix.md` | Reverse trace validation | DOCUMENTED / STATIC_PRECHECK |
| R04 | `.agents/.riskMatrix.md` | Risk re-evaluation | DOCUMENTED / STATIC_PRECHECK |
| R05 | `.agents/.plans.md` | Scope-gated future coding | DOCUMENTED / STATIC_PRECHECK |
| R06 | `.agents/.documents/.documentGovernance.md` | Cross-source evidence | DOCUMENTED / STATIC_PRECHECK |
| R07 | `.agents/.workflow/validationSpecification.md` | Independent A.1 safeguards | DOCUMENTED / STATIC_PRECHECK |
| R08 | `.agents/.workflow/testingAndDelivery.md` | Executable-case fixture minimum | DOCUMENTED / STATIC_PRECHECK |
| R09 | `.agents/.documents/featureDesign.md` | Design data/control boundaries | DOCUMENTED / STATIC_PRECHECK |
| R10 | `.agents/.workflow/agentRoles.md` | Weighted worker conflict review | DOCUMENTED / STATIC_PRECHECK |

### Validation and limitations

Pre-commit requirements: exactly 10 independently described documentary changes in 10 existing Markdown owner files, no duplicate normative BRD, one separate handoff, valid new relative links, checked branch parent and no executable runtime/config/CI changes. Post-commit verification must confirm HEAD SHA, file scope, presence of all 10 sections and preserved approval statuses.

The source baseline contains candidate F43–F64, 44 designed/unrun cases, 12 MM-REQ/TC, 9 A1 gates, open P0s, an unapproved Google Draft mirror and Draft PR #10. This batch does not modify those approvals or run host tests. Existing local uncommitted changes are not accessed through GitHub connector.

**Next batch:** PLAN-107 security/OS/Path Guard ten-task document review. On resume, re-read the exact output SHA; if the branch moved unexpectedly, stop rather than force update. `A1_NOT_RUN`, `B_NOT_AUTHORIZED`, `B1_NOT_RUN`.
