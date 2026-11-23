# Web v1.0 — Remote Markdown link/ID static preflight (2026-11-23)

Source: `RyugaWork/spec2code`, branch `docs/plan-089-a1-readiness`, pinned **input HEAD `fa2ba44e4a2076cf004160831fdaa7a3f2ec8148`**. Method: GitHub tree and exact blob reads at the same revision, followed by a conservative Markdown inline-link target check. **AUTHOR_PREFLIGHT_ONLY**, not independent A.1, complete semantic audit, Web test execution or released package QA.

## Inventory and observed results

| Check | Observed result | Qualification |
| --- | --- | --- |
| Markdown blob coverage | **125/125** tracked `.md` blobs fetched without read errors | HEAD at input; includes historical handoffs, not only active normative files |
| Relative inline-link targets | **1,189** checked | Parsed Markdown inline `[label](target)` relative links; does not include reference-style links, arbitrary HTML or verified heading anchors |
| Active file-path missing | **0 observed** | Checked target against tracked file paths at the input HEAD; not proof of semantic correctness |
| Historical missing references | **11 occurrences** | Three preserved legacy V0.6.4 handoffs, pointing to removed/renamed old `.handoff.md`, `.plan.md`, `.riskdetail.md` records |
| Directory link | **1** `../.handoffs/` | In `.agents/.workflow/planningSpecificationWorkflow.md`; valid Git tree directory, not missing file |
| GitHub/HTTP external URLs | **Not checked** | No online HTTP status/read correctness verification |
| Markdown fragment anchors | **Not checked** | File existence check only, not heading-slug or rendered Markdown consistency |
| Requirement/AC semantics | **Not independently audited** | Requires subject review on authoritative BR/AC plus independent A.1 |
| Real Web profile and host tests | **NOT_RUN** | There is no `.source/profiles/web/` distribution at input HEAD |

The 11 historical broken references occur in:
- `.agents/.handoffs/legacy-v0.6.4-handoff.md` (6 link occurrences);
- `.agents/.handoffs/legacy-v0.6.4-riskdetail.md` (3 occurrences);
- `.agents/.handoffs/legacy-v0.6.4-plan.md` (2 occurrences).

They are **archive/provenance-only**, not active V1 package paths. Preserve those records without destructive rewrite. An archive-specific index or link rewrite may be proposed separately only with a clear original-path mapping and approval.

## Targeted consistency checks

- PR #11 `REV-090-08`: in current master `.agents/.spec.md`, zero occurrences of noncanonical literal `A.1-VAL-0x`; canonical `A1-VAL-0x` labels remain. Narrow source issue appears corrected, pending independent confirmation.
- PR #11 `REV-090-09`: master `.agents/.spec.md` has zero literal escaped-backtick sequences `\\`` under a text search. This does not validate browser Markdown rendering.
- Current [feature crosswalk](webV1PreflightAndCapabilityMatrix.md) enumerates exactly 64 unique F IDs; this is an author-led design count, not functional verification.
- Canonical PLAN-116 ledger has WEB-001..030 **PLANNED/NOT_RUN**; the acceptance suite has WEB-TC-01..15 **NOT_RUN**; this report does not change those statuses.

## Limitations and required next checks

1. Re-run target and anchor checks on **post-commit HEAD** including all newly authored files, not just the input revision; record exact SHA.
2. Add Markdown reference-style link and HTML link support if claiming full link coverage. Check duplicate/colliding heading anchors with GitHub-compatible slug rules, then review false positives.
3. Perform source-of-truth semantic checks on master SRS ↔ approved BR/AC ↔ RTM ↔ test catalog and owner-signed Google BRD revision; a plain link checker cannot approve meanings.
4. Perform true A.1 external review, Web-host fixture testing and security acceptance only when authority and implementation gates allow.

**Disposition:** `STATIC_FILE_LINK_PREFLIGHT_COMPLETE_WITH_ARCHIVE_EXCEPTIONS`; **A1_NOT_RUN / B_NOT_AUTHORIZED / WEB_TC_NOT_RUN**.


## Later all-tracked-Markdown path check (2026-11-23)

The previous 125-file limited scan is **historical baseline evidence**, not the latest comprehensive tracked-file input. [New read-only 136-file audit at `e8efc36b78f991efc618d1ca98865609d032bb0d`](webV1FullMarkdownLinkAudit20261123.md) observed 1,446 Markdown link occurrences and the same 11 archived v0.6.4 missing relative targets, with no other missing tracked target in the recognized syntax. It does not validate anchors, renderer behavior or functional correctness. No archival history was modified.
