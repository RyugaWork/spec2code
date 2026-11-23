# PLAN-116 — Full tracked Markdown file-target static audit (2026-11-23)

**Scope: static file-reference checks only**. Source `RyugaWork/spec2code@e8efc36b78f991efc618d1ca98865609d032bb0d` through the connected GitHub read provider; tree was complete (199 Git tree entries), with **136 tracked Markdown blob paths**. Each 136/136 blob was retrieved by immutable SHA, and parsed without changing files.

## Audit method and observed counts

| Metric | Result |
| --- | ---: |
| Tracked Markdown blobs read by SHA | **136/136** |
| Matched Markdown link occurrences `[...](...)` across those files | **1,446** |
| Apparent missing relative tracked-path targets | **11** |
| Missing relative paths **outside archived v0.6.4 handoffs** | **0 observed** |
| Files with unterminated simple triple backtick/tilde code fences | **0 observed** |
| Blob fetch errors | **0** |

The scanner skipped fenced code blocks and simple inline backtick spans, extracted Markdown `[]()`-shaped targets, resolved local relative paths against the pinned Git tree, and recorded missing paths. External URLs, page anchors, bare HTML hrefs, reference-style links, semantic target equivalence, full Markdown rendering, case-sensitive filesystem materialization, program behavior, native Spec Kit and hostile OS containment **were not verified**. These are **not** 1,446 validated remote URLs.

## Eleven known historical missing links, do not rewrite history

| Archived file | Missing relative targets and occurrences | Count |
| --- | --- | ---: |
| `.agents/.handoffs/legacy-v0.6.4-handoff.md` | `.handoff.md`, `.plan.md`, `.riskdetail.md` (lines 15–17, 74, 106) | 6 |
| `.agents/.handoffs/legacy-v0.6.4-plan.md` | `.handoff.md`, `.riskdetail.md` (line 6) | 2 |
| `.agents/.handoffs/legacy-v0.6.4-riskdetail.md` | `.handoff.md`, `.plan.md` (lines 5, 181) | 3 |

These are already known migration-era paths from the older [source audit](webV1StaticMarkdownAudit20261123.md). Historical handoff text is retained for provenance, not silently edited or deleted to improve the count. Relative tracked-file targets outside these three archived files had no missing result under the test's recognized syntax.

## Key separately observed semantic risk

The [PR #11 ID collision report](webV1Pr11CollisionReconciliation20261123.md) proves that successful link-target checks do **not** imply correct cross-branch feature/requirement semantics: PR #11 reuses F43..F50, RM-034..040 and PLAN-091 differently. Integrating those definitions without owner review would invalidate RTM and A.1 evidence.

## Disposition and recheck policy

**`AUTHOR_STATIC_LINK_PREFLIGHT_COMPLETED`** for the 136-file immutable source tree. No current active-document missing relative targets observed under this bounded scanner. `WEB-021` **final package/static acceptance remains PLANNED/NOT_RUN**, because the Web distribution bundle is not yet created and there was no real host install. All 21 behavior/negative Web cases NOT_RUN, A.1 NOT_RUN, Phase B NOT_AUTHORIZED, B.1 NOT_RUN, RM-001 P0 OPEN.

Re-run on any post-scan source/tree change, PR integration or release package. This report does not substitute for markdownlint, fragment/anchor validation, SRS semantic review or independent gate decisions.
