# PLAN-095 — Actual scoped Spec Kit Web/GitHub test evidence

> **Execution surface:** authenticated GitHub Contents connector and GitHub source/tree comparison, not a local checkout. **Recorded date:** 2026-11-13 Asia/Ho_Chi_Minh. **Tested S2C revision:** `916ed6aa769e1fb9c25d9bd988277275613ae695` on `docs/plan-089-a1-readiness` (Draft PR #10). All observations are **author/agent-executed**, not independent A.1, B.1 or native Spec Kit acceptance. Subsequent documentary commits must be distinguished from the pinned tested snapshot.

## 1. Result summary with exact scope

| Case | Execution mode | Observed result and output | Status and limits |
| --- | --- | --- | --- |
| `SKI-TC-001-P` | GitHub JSON parsing + exact-SHA Git tree | `.specify/feature.json` decoded to `{"feature_directory":"specs/001-s2c-speckit-integration"}`; contained two-component `specs/` selection; required `spec.md`, `plan.md`, `tasks.md` and quality checklist present in same source tree | **PASS (SCOPED_STATIC_GITHUB)**. Does not exercise local symlink/junction/Path Guard; `SKI-TC-001-N` NOT_RUN |
| `SKI-TC-003-P` | GitHub tree + existing `.source/.config/speckit.json` task-ID regex | Four expected artifact paths present; regex extracted **15 T001–T015 IDs**, all distinct and format-compatible, after `[USn]` tagging | **PASS (SCOPED_STATIC_GITHUB)**. No Python bridge execution, empty-file/negative host test or approved source semantics |
| `SKI-TC-004-P` | **Real GitHub connector file UPDATE** followed by branch/commit/blob re-fetch and exact compare | Single authorized Markdown file update at `specs/001-s2c-speckit-integration/quickstart.md`, one new commit, no other file modified; marker read back; returned blob SHA matched re-fetched blob; branch HEAD matched returned commit | **PASS (WEB_CONNECTOR_WRITE)**. Does not imply upstream Spec Kit CLI, local Python or host code permission |
| `SKI-TC-006-P` | Exact-SHA Markdown requirements-to-RTM-to-test ID audit | 12 feature `SKI-FR` rows, **12 individually keyed RTM rows**, **24 unique `SKI-TC-xxx-P/N` records**, both cases linked in each mapping row, zero missing IDs/orphans | **PASS (SCOPED_STATIC_GITHUB)**. Requirements-quality signoff and real execution of remaining cases NOT_RUN |

**Test inventory:** 4 cases completed with narrow, reproducible provider/static evidence; **20 of the original 24 planned feature acceptance cases remain NOT_RUN**. All extra `SK95-GATE-01..08` native authorization negative cases are `DESIGN_NOT_RUN`. There is no independent reviewer identity or host security QA pass.

## 2. `SKI-TC-004-P` exact GitHub write evidence

- **Before Git HEAD:** `1709037a6975b846478e8014a68151d129fb486a`.
- **Written path:** `specs/001-s2c-speckit-integration/quickstart.md` only, via a GitHub Contents file update using the then-current blob SHA `03f885c0207386cf5ede9419d61480f7a0dfafb2`.
- **After commit / tested source:** `916ed6aa769e1fb9c25d9bd988277275613ae695`.
- **Re-fetched blob SHA:** `69dda9d4437827141f272caa85c82d34d0c22b2c`, matching the connector's returned new content SHA.
- **Compare command (GitHub API):** [before...after comparison](https://github.com/RyugaWork/spec2code/compare/1709037a6975b846478e80151d129fb486a...916ed6aa769e1fb9c25d9bd988277275613ae695). **Ahead = 1 commit**; exactly one modified path, the allowed quickstart file.
- **Readback:** contained the exact marker `## PLAN-095 — Controlled Web-mode GitHub edit evidence`, and returned branch HEAD equalled the new commit.
- **Actual assertion:** 1 commit AND 1 changed authorized document AND readback contains unique marker AND blob SHA equal AND live branch HEAD equal ⇒ **PASS**.
- **No claim:** no `specify init`, `$speckit-implement`, `$speckit-analyze`, terminal, S2C Python guard, CI, additional Git branch, release, third-party independent review or code/test execution occurred.

## 3. Source identities and reproducible static checks

- JSON feature pointer blob: `8172bcc56b4407df9fd5f000f2de2a94d6f8ab40`.
- Feature `spec.md` blob: `b875ba8d3759c5b072334347dc9cb451db2a2f0b`; `plan.md` blob: `0ee95e0b142dee528b245cf314bfa3e60151b35f`.
- Feature `tasks.md` blob: `85db4ae9e976f294cd721911fe22609ad097cd01`; checklist blob: `1ec02d31c3ff0f7df45d32f13630158b7da02ad1`.
- Acceptance catalogue blob: `eee32a26ce8466891223cd9609ae985a048a40fb`; RTM blob: `9f4297bbc5fdd6a9981bc4de75e8f391fa3aff1f`; config blob: `f2a26f3b5e8a18a9b2d19dc48367b287fe790172`.
- Task matching rule as read from real S2C config: `^\\s*-\\s*\\[[ xX]\\]\\s*(?:\\*\\*)?(T\\d{3,6})\\b`; 15 matches and 15 distinct IDs after adding `[US1..4]` story labels.
- ID audit algorithm: read feature table `^| SKI-FR-... |`, master RTM Section L `^| `SKI-FR-...` |`, feature acceptance table `^| `SKI-TC-...-[PN]` |`; compare exact ID counts and corresponding `-P`/`-N` refs in each mapping row. No parser is committed as a runtime guard, and these tests do not validate the semantic correctness of each BR→REQ association.

## 4. Failure, authorization and drift boundaries

The four positive results are **provider-based or static** checks only. They do not exercise negative/host code paths; `SKI-TC-001-N`, `003-N`, `004-N`, `006-N`, other `SKI-TC` cases, `SK95-GATE` checks and `SK3-01..08` native acceptance remain unrun. No owner-approved Spec Kit native release, CLI or skill installation is available in the local runner.

**A.1:** NOT_RUN; **B:** NOT_AUTHORIZED; **B.1:** NOT_RUN. The [native gate](../.workflow/specKitNativeExecutionGate.md) is a draft procedural rule, not deployed interception. Existing RM-001..005 risks remain open. After commits to RTM/Constitution/feature case content, redo any affected static audit at that new exact source SHA instead of treating historical PASS as independent source-fresh signoff.

**Evidence owner:** this ChatGPT session's connected GitHub operations; no named independent reviewer or production security executor is asserted.
