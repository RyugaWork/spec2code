# Spec2Code — Project Handoff and Acceptance Ledger

> **Snapshot date:** 2026-11-12 (Asia/Ho_Chi_Minh)  
> **Repository:** https://github.com/RyugaWork/spec2code  
> **Canonical development branch:** `spec2code/InitialVersion_v0`  
> **Audited v0.6.4 code baseline:** `20e81bf51422e6a60c788bb175b7e8f8ec656a15`  
> **Latest Windows fix under review:** `fix/windows-portability-v0.6.4`, commit `e760bf0afe7e3d803034519810bce70a5cf90d61`, [PR #5](https://github.com/RyugaWork/spec2code/pull/5).  
> **Document scope:** source review plus reported/GitHub CI evidence; not a penetration test or blanket guarantee of filesystem safety.

## 1. Purpose and scope

Spec2Code is a universal, repository-independent agent skill and local Python core for planning and tracking spec-to-code work. It is **not** a privileged system sandbox, a general-purpose autonomous code editor, or an installed MCP server. It must respect the target repository's `AGENTS.md`, approved requirements, and security controls.

Keep these three tracked root documents synchronized:
- [`.handoff.md`](.handoff.md): implemented features, acceptance evidence, pass/fail/not-run handoff, outstanding work.
- [`.plan.md`](.plan.md): future work, order, ownership, acceptance gates.
- [`.riskdetail.md`](.riskdetail.md): risks, concrete evidence, mitigations, and residual exposure.

**Status vocabulary:** `PASS` = a cited test or check passed; `FAIL` = observed test failure; `IMPLEMENTED / NOT FULLY VERIFIED` = present in source but not validated across supported environments; `NOT IMPLEMENTED` = absent capability; `NOT RUN` = no supporting test or audit evidence. Never infer a PASS from a feature's presence in code.

## 2. Current implementation inventory (v0.6.4 stable)

| ID | Capability | Implementation / scope | Handoff state | Evidence |
| --- | --- | --- | --- | --- |
| CAP-01 | Universal source discovery and bounded infrastructure inventory | Common language/framework roots, file metadata, selected static facts; never a full semantic or runtime scan | IMPLEMENTED; Linux CI PASS; Windows not cleared | `scripts/scan_infrastructure.py`, `.config/scanner.json` |
| CAP-02 | Configuration-driven policies | Validated bundled `.config/*.json` tables for scanning, architecture, routing, sessions, security, MCP and Spec Kit | IMPLEMENTED; Linux CI PASS | `scripts/config_loader.py`, `tests/test_config_loader.py` |
| CAP-03 | Repository Path Guard | Exact Git-root validation, traversal/symlink checks, repository binding and fail-closed errors | IMPLEMENTED; OS-specific limits OPEN | `scripts/path_guard.py`, `tests/test_path_guard.py` |
| CAP-04 | Session lifecycle and provenance | `start`, `status`, `checkpoint`, `record`, `finish`, Git HEAD/drift classification and audit JSONL | IMPLEMENTED; Linux CI PASS; Windows original FAIL | `scripts/session_guard.py`, `tests/test_session_guard.py` |
| CAP-05 | Scoped read/write and safe targeted cleanup | Managed atomic file writes, appends, bounded reads, SHA-256-verified deletion of exact file | IMPLEMENTED; Windows TOCTOU limitation OPEN | `scripts/scope_io.py`, `tests/test_continuous_scope.py` |
| CAP-06 | Read-on-demand architecture routing | Root -> layer -> component -> function docs; static graph, symbol cache and revision summaries | IMPLEMENTED; Windows case-collision issue OPEN | `scripts/architecture_tree.py`, `tests/test_hierarchy_and_handoff.py` |
| CAP-07 | Adaptive context selection | Minimal/balanced/deep task routing, high-risk floor, stale HEAD/source detection, path-only context pack | IMPLEMENTED; Linux CI PASS | `scripts/context_router.py`, `tests/test_context_router.py` |
| CAP-08 | Session-scoped handoff | Separate external-change/spec-change logs; `merge` gated by FINISH, exact ID, header and SHA-256 | IMPLEMENTED; Windows newline issue OPEN | `scripts/handoff_store.py`, `tests/test_hierarchy_and_handoff.py` |
| CAP-09 | Official Spec Kit compatibility | Read-only active-feature discovery; `spec.md`, `plan.md`, `tasks.md` gate for implementation | IMPLEMENTED AS BRIDGE; Spec Kit not bundled | `scripts/speckit_bridge.py`, `integrations/speckit/README.md` |
| CAP-10 | MCP request authorization boundary | Trusted checkout, read/write action allowlists, session/HEAD gates, no arbitrary shell | IMPLEMENTED AS LIBRARY ONLY; no server | `scripts/mcp_boundary.py`, `.config/mcp.json` |
| CAP-11 | Sensitive-file filtering | Excludes recognized secret paths/extensions from content scans, metadata-only treatment for sensitive configs | IMPLEMENTED; not exhaustive secret discovery | `scripts/scan_infrastructure.py`, `.config/security.json` |
| CAP-12 | Git and runtime safety | Read-only local Git inspection; runtime probe is opt-in, not a deployment check | IMPLEMENTED; no fetch/push/reset/rebase automation | `scripts/session_guard.py`, `scripts/scan_infrastructure.py` |
| CAP-13 | Actual MCP server / remote adapter | Network transport, authentication, deployment and consent UI | NOT IMPLEMENTED | `docs/CONTINUOUS_SCOPE_ENFORCEMENT.md` |
| CAP-14 | Automated edits to user application code | User-authorized implementation may be done by a separate coding agent; core itself only tracks/scans/manages its artifacts | NOT IMPLEMENTED IN PYTHON CORE | `SKILL.md`, `docs/INSTALL.md` |

**Safety distinction:** the core does create/replace its own state, architecture and handoff documents and can remove verified pending/cache files. It does **not** grant an external agent permission to edit code or run arbitrary commands. The Path Guard cannot contain a separate agent's unrestricted shell access.

## 3. Acceptance and verification ledger

| Check ID | Target | Observed result (2026-11-12) | Decision |
| --- | --- | --- | --- |
| TEST-001 | Stable v0.6.4 Python 3.10 Linux CI | GitHub Actions completed successfully | PASS |
| TEST-002 | Stable v0.6.4 Python 3.11 Linux CI | GitHub Actions completed successfully | PASS |
| TEST-003 | Stable v0.6.4 Python 3.13 Linux CI | GitHub Actions completed successfully | PASS |
| TEST-004 | Stable v0.6.4 on user's Windows Python 3.14.2 | `Ran 77 tests`; 17 failures, 1 error, 10 skipped; 49 passed | FAIL |
| TEST-005 | Draft PR #5 Linux Python 3.10 / 3.11 / 3.13 | Jobs completed successfully on latest recorded run | PASS (Linux only) |
| TEST-006 | Draft PR #5 Windows Python 3.14 | `Ran 79 tests`; 2 failures, 2 errors on run 43196836721 | FAIL |
| TEST-007 | Symlink denial on unprivileged Windows | Several tests skipped due to OS privilege; one original test errored with WinError 1314 | NOT FULLY VERIFIED |
| TEST-008 | Windows hostile filesystem races, file overwrite/rollback recovery, real MCP host | No confirmed end-to-end evidence | NOT RUN |

**CI references:**
- Stable v0.6.4: https://github.com/RyugaWork/spec2code/actions/runs/43192199099
- Draft Windows fix: https://github.com/RyugaWork/spec2code/actions/runs/43196836721
- Draft PR: https://github.com/RyugaWork/spec2code/pull/5
- Local Windows test report: user-provided PowerShell output (2026-11-12), not stored in this repository.

**Release decision:** v0.6.4 source is merged into `spec2code/InitialVersion_v0`, but **Windows is not acceptance-cleared**. PR #5 is draft/open and must not be represented as merged or passing. Do not approve production or sensitive-repository deployment from Linux-only CI evidence.

## 4. Current risks and immediate blockers

- `RISK-001`: Windows time-of-check/time-of-use (TOCTOU) filesystem boundary is not an OS-level sandbox.
- `RISK-002`: Windows case-insensitive `api` vs generated `API` path collision caused false source changes and session failures.
- `RISK-003`: Windows 8.3/short-path alias handling can reject legitimate Git roots.
- `RISK-004`: CRLF/LF conversion changes byte checks and pending-log headers.
- `RISK-005`: Symlink/junction security scenarios lack complete non-admin Windows coverage.
- `RISK-006`: Managed-file collisions and unrestricted external coding-agent tools can affect project data.
- `RISK-007`: Generated documents and handoff ledgers may be accidentally committed or synced.
- `RISK-008`: No real authenticated MCP server or isolated execution boundary exists.

Detailed evidence, priority and mitigation: [`.riskdetail.md`](.riskdetail.md).

## 5. Handoff: what is complete and what is not

**Completed / accepted on the audited Linux baseline**
- Independent universal skill structure, documented installation model and separately managed official Spec Kit bridge.
- Config-driven source/architecture/routing/session/security policy loading with safety validation.
- Linux regression workflow for Python 3.10, 3.11, 3.13.
- Session tracking, context routing, architecture indexing, exact-session change logs and MCP-ready authorization library.

**Open / failed / not accepted**
- Windows Python 3.14 compatibility, especially path aliases and Spec Kit feature-directory checks.
- Symlink/junction end-to-end tests under appropriate Windows permissions.
- User-file collision safeguards and source/output directory separation.
- A full file write/delete threat-model test including interrupted writes and rollbacks.
- A real MCP transport/server and operation-level user consent.
- Verification that an external AI coding agent obeys all stated permissions.

## 6. Next handoff procedure

1. Read `.handoff.md`, `.riskdetail.md`, then `.plan.md` before editing code.
2. Check Git branch/HEAD, open PRs and latest CI; update the acceptance ledger with exact evidence, not guesses.
3. Fix Windows failures on a dedicated branch; do **not** relax the Path Guard, session attribution, hash validation or secret exclusions just to green CI.
4. Run: `python -m unittest discover -s tests -t tests -v`. Test Windows 3.14 and Linux 3.10/3.11/3.13. Classify skipped security tests explicitly.
5. Keep issue-specific risks linked to a fix commit, regression test and proof of closure in `.riskdetail.md`.
6. After validated merge, update this file's snapshot date, baseline commit and status entries. Never mark a test PASS before seeing its results.

**Git caution:** the repository's default `main` branch is not the canonical v0 code branch in this snapshot. Do not infer release state from a default-branch checkout without checking the branch contents.


## 7. Patch planning handoff — security-first remediation (2026-11-12)

**PLANNED ONLY:** A concrete patch program was added to [`.plan.md`](.plan.md), section 6, and a patch-to-risk closure matrix to [`.riskdetail.md`](.riskdetail.md), section 7. No application code has been modified by this planning step. No failures, skipped tests or unresolved risks have been promoted to PASS.

**Ordered patch sequence:**
1. `PATCH-01` canonical Windows path alias/session identity; `PATCH-02` read-only Spec Kit feature-path portability.
2. `PATCH-03` generated artifact vs project source collision prevention; `PATCH-05` ownership, safe replacement and deletion gates.
3. `PATCH-04` Windows filesystem isolation/TOCTOU verification, including real symlink and junction cases.
4. `PATCH-06` LF/CRLF fidelity and raw-hash merge; `PATCH-07` source freshness and interrupted session recovery.
5. `PATCH-08` privacy/Git hygiene; `PATCH-09` independent cross-platform security regression gates.
6. `PATCH-10` real MCP service postponed until core data safety is proven.

**New risk:** `RISK-014` — reuse of cached SHA-256 when source file size and `mtime_ns` remain unchanged can miss a deliberately altered file under the current fast path. This remains an unproven exploit; it requires a targeted regression test.

**Latest verified Windows blocker in draft PR #5:** `79 tests; 2 failures; 2 errors`. The failing cases are three Spec Kit feature-path checks and one Path Guard cached-document rejection test. Source of truth: [run 43196836721](https://github.com/RyugaWork/spec2code/actions/runs/43196836721).

**Merge gate:** Do not merge Windows fixes or claim machine-wide filesystem safety from unit-test success. Require validated functional Windows/Linux CI, independent security-negative tests, existing-file hash preservation, documented scope limits and an explicit review decision.

**Next operator action:** Start with the PATCH-01/PATCH-02 regressions on a dedicated branch, preserve all unmerged PR #5 history, and refresh these three root documents from actual CI evidence once implementation begins.
