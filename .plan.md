# Spec2Code — Forward Development and Security Plan

> **Created:** 2026-11-12 (Asia/Ho_Chi_Minh)  
> **Applies to:** `spec2code/InitialVersion_v0` (stable code baseline v0.6.4).  
> **Planning status:** proposals, not shipped promises; no scheduled release dates are committed.  
> **Read with:** [`.handoff.md`](.handoff.md) (actual shipped/test status) and [`.riskdetail.md`](.riskdetail.md) (evidence and risk acceptance).

## 1. Non-negotiable product principles

1. Universal, project-agnostic core: no hardcoded application names, framework-specific logic, credentials, host paths, or business requirements.
2. Explicit repository boundary: no reads, writes or removals outside the authorized Git checkout; reject ambiguous root identities and symlink/junction escapes.
3. Safe-by-default operation: detect -> describe -> request authorized action -> verify -> handoff. Do not implement arbitrary code mutation as an implicit side effect of scanning.
4. Keep substantive policy in validated `.config/*.json`; Python must retain immutable safety invariants.
5. Official GitHub Spec Kit remains separately installed/owned; Spec2Code is only the compatibility and orchestration layer.
6. File ownership and rollback precede convenience. User source, existing documents and secrets cannot be overwritten by default.
7. Local-only and minimal-data operations unless explicitly approved. Do not give MCP clients shell, root selection, privilege escalation or unsupervised deletion.
8. PASS requires reproducible verification; document FAIL, BLOCKED, SKIPPED and NOT RUN without conflation.

## 2. Milestones and acceptance gates

| Priority | Milestone | Work items | Acceptance / definition of done | State |
| --- | --- | --- | --- | --- |
| P0 | M-01: Finish Windows compatibility patch | Resolve latest PR #5 Windows failures; retain strict Path Guard; fix `api`/`API` generated-document collision, LF/CRLF behavior and 8.3 aliases | Linux 3.10/3.11/3.13 and Windows 3.14 CI PASS; manual Windows test confirms normal `start -> checkpoint -> record -> finish -> merge`; no unexpected files | IN PROGRESS / FAIL |
| P0 | M-02: Prove no damage outside repository | Negative tests for absolute paths, traversal, symlinks, junctions, nested Git repositories, root swaps, malicious cached paths and alternate-drive/UNC paths | Every attempted out-of-root read/write/delete is denied; external sentinel bytes unchanged; tests run in appropriate Windows permissions and POSIX | PLANNED |
| P0 | M-03: Protect existing project data | Dedicated managed-artifact namespace or collision-proof preflight for all output paths; fail closed if non-managed file occupies a destination; no source/architecture directory aliasing | Install + session on existing repo does not overwrite user files; collision fixture blocks; pre/post file hash comparisons and recovery guidance | PLANNED |
| P0 | M-04: Make deletion auditable | Enumerate all file deletion paths; require exact owned paths, session context and hash checks; distinguish temporary cache invalidation from irreversible log deletion | Deterministic allowlist, no wildcard deletes, rollback/recovery test, audit entry for each deletion, fail-closed on hash mismatch | PLANNED |
| P1 | M-05: Harden privacy and Git hygiene | Ignore runtime state, generated architecture and handoff ledgers appropriately; review repository type/policy before modifying ignore rules; no secrets in logs | `git status` after a clean session does not expose or stage generated sensitive artifacts; tests for files named `.env`, tokens and secret-like configs | PLANNED |
| P1 | M-06: Package and Windows portability | Explicit version metadata in `SKILL.md` and docs, consistent install/test commands, CI Python/OS matrix, Windows newline discipline | Cross-platform install and test guide verified; exact-version compatibility documented | PLANNED |
| P1 | M-07: Deepen session integrity | Crash/restart recovery, repeated merge idempotency, adversarial session-state edits, external Git drift, stale source and concurrent writers | No false FINISH or unverified deletion; recovery procedures covered by tests; protected state not silently migrated | PLANNED |
| P1 | M-08: Transparent risk dashboard | Generate concise read-only status with feature, test and risk links derived from committed artifacts, not free-form PASS claims | Status never presents unrun CI/security checks as PASS; bounded output; no private data in agent context | PLANNED |
| P2 | M-09: Actual MCP server adapter | Implement transport plus authenticated server-owned trusted root, read-only default, per-action consent, audit and limited write grants | Host rejects root override/arbitrary shell, has authentication, least privilege, replay protection and security integration tests | NOT IMPLEMENTED |
| P2 | M-10: Safer Spec Kit integration | Strengthen feature-path resolution and exact stage/manifest gating on Windows; maintain read-only bridge behavior | Spec Kit sources never modified by bridge; missing/unsafe spec, plan or tasks block implement; Windows + Linux integration tests | PARTIAL |
| P2 | M-11: Versioned release process | Adopt tags, compatibility matrix, migration procedures and maintenance criteria | Release notes map each claim to test evidence and known risks; reproducible package inventory | PLANNED |

## 3. Work breakdown and dependencies

### Phase A — Security stabilization (P0, prerequisite to merge/release)

**A1. Windows diagnosis:** Reproduce all current failures using latest `fix/windows-portability-v0.6.4`; capture actual tracebacks for each remaining failure. Do not assume old causes still apply.

**A2. Filesystem naming and path rules:** Compare canonical Windows file identities instead of treating legal 8.3 aliases as symlinks; still reject actual symlink/junction paths. Ensure generated architecture output cannot overlap source roots on case-insensitive filesystems.

**A3. I/O and cleanup rules:** Standardize UTF-8/LF managed output, migrate/read legacy CRLF logs safely, retain SHA-256 checks over *raw* bytes for deletion. Preflight every write target and provide deterministic failure on collisions.

**A4. Threat-model tests:** Run both normal-user and appropriately privileged symlink/junction test scenarios; use temporary repos plus external sentinel files. Include Windows non-admin skip reporting, but do not consider skipped tests coverage.

**A5. Release gate:** All targeted automated tests PASS, no unresolved P0 risk is accepted by assumption, PR reviewed and then merged explicitly.

### Phase B — Operational hardening (P1)

- Document what Spec2Code can read, generate, replace and delete, with file ownership conventions.
- Introduce safe backup/recovery instructions and non-destructive dry-run/preview of proposed managed changes.
- Add source-vs-generated namespace regression tests for `API`, `Present`, `DataAccess` and other reserved names on Windows.
- Tighten log data minimization and `.gitignore` handling; never silently modify the target project's ignores.
- Add integration tests for interrupted `finish`/`merge`, stale locks, corrupt JSONL and retry behavior.
- Standardize documentation naming/version references and establish tested supported platforms.

### Phase C — Optional future integration (P2)

- Implement a **separate** real MCP host/server with explicit authentication and user approval for mutations; do not treat `mcp_boundary.py` as deployed transport.
- Explore agent/editor integrations only after independent permission controls and reliable rollback are demonstrated.
- Keep Spec Kit integration optional and read-only in the core; run actual Spec Kit commands only with separate authorization.
- Consider release tags and conservative upgrade/migration tooling after M-01 through M-08 have objective evidence.

## 4. Test plan

**Minimum commands (from exact repository root):**

```powershell
git status --short
git branch --show-current
python -m unittest discover -s tests -t tests -v
```

**Required operating-system matrix:**
- Linux: CPython 3.10, 3.11 and 3.13 (existing automated CI baseline).
- Windows: CPython 3.14; no administrator requirement for normal features; explicitly documented privileges for real symlink tests.
- Additional OS/filesystem checks (macOS, network shares, OneDrive-synced folders) are **NOT RUN** until evidence exists; do not label them supported merely because local tests pass.

**Safety invariants tested with external sentinels:** No out-of-repository writes; no unauthorized source overwrites; no unmanaged document overwrites; no wildcard deletion; no context release of secret values; no automatic commit/push/reset/rebase.

## 5. Change-control and handoff protocol

1. Create a scoped branch from the canonical v0 branch for code or policy changes; link to a milestone and a `RISK-xxx` entry when relevant.
2. Add a failing regression test that represents the problem; fix the root cause without weakening safety invariants.
3. Execute and record actual tests, skipped cases and artifact hash/cleanup outcomes.
4. Review permissions, Git diff, generated files, and changes to security invariants.
5. Keep a draft PR while tests are failing; only merge after an explicit acceptance decision.
6. Update `.handoff.md` with exact code commit, CI evidence and completion status; update `.riskdetail.md` with mitigations and residual risks; then update this plan.
7. Never delete the history of a risk; mark it `MITIGATED` or `ACCEPTED` with evidence and decision-maker instead.

**Immediate next action:** M-01 and M-02, not feature expansion. Draft [PR #5](https://github.com/RyugaWork/spec2code/pull/5) still fails the Windows job on [Actions run 43196836721](https://github.com/RyugaWork/spec2code/actions/runs/43196836721).


## 6. Concrete patch program — security and Windows stabilization (2026-11-12)

**Status:** PLANNED ONLY. This section is an implementation specification, **not** a claim that source patches have been applied, tests have passed, or a release is approved. The stable branch remains the v0.6.4 code baseline; PR #5 is an unmerged draft with Windows CI FAIL.

### 6.1 Evidence-driven risk prioritization

| Priority | Patch ID | Affected risks | Expected change | Implementation status |
| --- | --- | --- | --- | --- |
| P0 / hotfix | PATCH-01 | RISK-003, RISK-013 | Canonical Windows root and session identity across path aliases without bypassing link/junction restrictions | PLANNED |
| P0 / hotfix | PATCH-02 | RISK-003, RISK-005, RISK-013 | Correct Windows-safe Spec Kit feature/artefact containment | PLANNED |
| P0 / data safety | PATCH-03 | RISK-002, RISK-006, RISK-008 | Preflight all generated-output destinations; prevent case-folding collision and non-managed overwrites | PLANNED |
| P0 / data safety | PATCH-04 | RISK-001, RISK-005, RISK-009 | Establish Windows filesystem threat boundary and validate escape denial | PLANNED |
| P0 / data safety | PATCH-05 | RISK-006, RISK-007, RISK-012 | Central managed-write/delete policy, collision refusal, rollback and auditable exact-file deletion | PLANNED |
| P1 / integrity | PATCH-06 | RISK-004, RISK-007, RISK-012 | Normalize LF managed writes and legacy CRLF parsing; preserve raw-byte hash identity and retry safety | PLANNED |
| P1 / integrity | PATCH-07 | RISK-012, RISK-014 | Prevent silent cached fingerprint reuse across adversarial same-size/mtime changes; strengthen session recovery | PLANNED |
| P1 / privacy | PATCH-08 | RISK-008, RISK-011 | Minimize/redact emitted metadata and notes; safe ignore/installation guidance | PLANNED |
| P1 / quality | PATCH-09 | RISK-005, RISK-013 | Deterministic cross-OS CI and a distinct privileged security test job | PLANNED |
| P2 / integration | PATCH-10 | RISK-009, RISK-010 | Authenticated, per-repository, read-only-first MCP service with explicit write consent | FUTURE / NOT IMPLEMENTED |

**Dependencies:** PATCH-01 before PATCH-02 and PATCH-07; PATCH-03 before PATCH-05 and PATCH-08; PATCH-04 before claiming Windows security clearance; PATCH-06 before handoff/merge acceptance; PATCH-09 verifies each P0/P1 patch. PATCH-10 cannot begin production acceptance until PATCH-03/04/05 are closed.

### 6.2 Patch implementation cards

#### PATCH-01 — Windows root aliases and session binding

- **Observed blocker:** PR #5 Windows CI test `test_cache_document_path_escape_rejected` ends at `SCOPE_VIOLATION: session repository binding changed` instead of exercising the injected cached-document path.
- **Likely cause to prove:** `capture_scope()` stores a root string which can differ across Windows 8.3 and long-path aliases despite referring to the same worktree. No unverified alias normalization may authorize a second checkout.
- **Edit targets:** `scripts/path_guard.py`, `scripts/session_guard.py`, `scripts/context_router.py`, `scripts/config_loader.py`, `scripts/scope_io.py`.
- **Implementation:** introduce one tested canonical-identity contract (physical root identity + canonical Git admin dir) shared by capture/compare operations. Detect actual reparse points separately. Do not change an ACTIVE session's stored identity in place; provide deliberate versioned migration or finish with matching code.
- **Tests:** long-path vs 8.3 same worktree allowed; different worktree denied; root junction/symlink denied; cached `../outside/keep.txt` rejected with external sentinel intact.
- **Done only when:** affected Path Guard tests PASS on Windows 3.14, exact malicious cached-path rejection remains enforced, and Linux regression stays PASS.

#### PATCH-02 — Spec Kit feature path portability

- **Observed blockers (latest Windows CI):** `test_active_feature_static_manifest_without_content` and `test_router_includes_spec_kit_artifacts` ERROR at `FEATURE_DIRECTORY_NOT_FOUND_OR_UNSAFE`; `test_missing_plan_blocks_implement` FAILS with the same error before reaching `SPEC_KIT_GATE_BLOCKED`.
- **Edit targets:** `scripts/speckit_bridge.py`, `tests/test_speckit_bridge.py`, optionally shared identity helper from PATCH-01.
- **Implementation:** reject unsafe lexical input first; resolve both candidate and authorized root against the *same canonical identity representation*, then verify feature and artifact ancestry; explicitly reject symlink/junction redirection, including existing ancestors. Preserve read-only semantics and official Spec Kit ownership.
- **Tests:** existing in-repo feature accepted; missing `plan.md` correctly raises `SPEC_KIT_GATE_BLOCKED`; external/UNC/drive/`..` feature pointers denied; symlink/junction adversarial cases run in a dedicated security suite.
- **Done only when:** three current Spec Kit failures resolved on Windows without a regression of escape tests.

#### PATCH-03 — Managed-artifact namespace and write preflight

- **Observed defect:** `.config/scanner.json` accepts source root `api`, while `.config/architecture.json` generates `API/`. On case-insensitive Windows, the paths may coincide. A scanner exemption for dot-prefixed Markdown in PR #5 is a containment workaround, not proof that directory names cannot collide.
- **Edit targets:** `.config/architecture.json`, `.config/scanner.json`, `scripts/config_loader.py`, `scripts/architecture_tree.py`, `scripts/scan_infrastructure.py`, `scripts/scope_io.py`.
- **Immediate v0.6.x fix:** preflight every intended output for case-insensitive collision with real project paths; refuse conflict *before any write*; protect every managed-file destination against replacing existing unowned content. Keep current files untouched upon refusal.
- **Longer-term breaking change (separate version/migration):** move all generated architecture under a single reserved `.agents/generated-architecture/` namespace. Do **not** silently move/delete historical top-level architecture docs; perform versioned migration after backup and explicit approval.
- **Tests:** projects with `api/`, `API/`, `Present/`, `DataAccess/`; conflicting arbitrary user `.summerize.md`; compare hashes of all preexisting files before/after attempted start.
- **Done only when:** no false unclassified change, no output/source aliasing, zero modification to user-owned collision fixtures.

#### PATCH-04 — Windows filesystem containment and hostile swaps

- **Boundary decision:** Path Guard is a Python operation boundary, not an OS sandbox. The current Windows path-open fallback is not race-proof.
- **Edit targets:** `scripts/scope_io.py`, `scripts/path_guard.py`, Windows-specific tests and security guide.
- **Implementation choices to assess:** robust Windows native handle/reparse-point checks and destination identity revalidation, or document a reduced guarantee with mandatory OS ACL/container isolation for untrusted workspaces. **Never** claim protection simply by adding another `resolve()` check.
- **Tests:** symlink/junction directory, leaf substitution, root replacement, alternate drive, UNC, nested Git, path swap between check and write, external sentinel content/hash unchanged.
- **Done only when:** the actual supported security guarantee is reproducible; unsupported threat models remain explicitly unapproved.

#### PATCH-05 — Managed operations, collision refusal, deletion safety

- **Edit targets:** `scripts/scope_io.py`, `scripts/session_guard.py`, `scripts/handoff_store.py`, architecture/state writers, supporting `.config/` policy.
- **Implementation:** central inventory of allowed outputs and exact deletion types; preflight ownership/managed marker or expected hash before replace; deny unexpected existing files; every delete bound to a known owned path and expected hash; idempotent `merge` with retained source evidence on failure.
- **Tests:** initial install into occupied destinations, concurrent change before write/delete, mismatched SHA-256, interrupted archive write, stale lock, repeated merge; assert no `rmtree` or wildcard cleanup.
- **Done only when:** authorized managed files alone can be changed; all collision tests preserve external/user files byte-for-byte.

#### PATCH-06 — Cross-platform newline and audit reproducibility

- **Edit targets:** `scripts/scope_io.py`, `scripts/handoff_store.py`, `tests/test_continuous_scope.py`, `tests/test_hierarchy_and_handoff.py`.
- **Implementation:** managed text uses UTF-8 and deterministic LF; convert CRLF only when parsing textual records; verify deletes with exact raw bytes and hashes. Do not normalize bytes before deletion attestation.
- **Tests:** LF and legacy CRLF sessions, multiple records, non-ASCII text, duplicate merge, checksum mismatch; no unexpected file rewrite.
- **Done only when:** end-to-end `start -> checkpoint -> record -> finish -> merge` passes on Windows and Linux.

#### PATCH-07 — Fingerprint freshness and interrupted sessions

- **New risk evidence:** the scanner may reuse a prior SHA-256 when `size` and `mtime_ns` match; the context router checks selected path metadata for changes. Same-size edits with deliberately restored timestamps may not be detected by the fast path.
- **Edit targets:** `scripts/scan_infrastructure.py`, `scripts/context_router.py`, `scripts/session_guard.py`, integrity regression tests.
- **Implementation:** make explicit `--verify`/rehash a required boundary for security-critical finalization or stale-source checks as appropriate; evaluate performance caps so the full checkout is not repeatedly hashed. Preserve fail-closed behavior on missing/corrupted state.
- **Tests:** byte-modified file with equal size and restored mtime; crash between state and ledger writes; cloned sessions; manual recovery without suppressing alerts.
- **Done only when:** provenance and selected-file freshness cannot be passed using deliberately stale metadata alone within the documented threat model.

#### PATCH-08 — Metadata privacy and Git hygiene

- **Edit targets:** scanner and handoff output, installation docs, `.gitignore` guidance and tests.
- **Implementation:** minimize paths/notes in generated ledger; sanitize high-risk note inputs; exclude generated transient state from target project's commits without blindly changing an existing target `.gitignore`. The three tracked root governance files `.handoff.md`, `.plan.md`, `.riskdetail.md` remain intentionally versioned.
- **Tests:** unusual secret filenames, token-shaped notes, `git add .` in disposable repository, OneDrive/shared folder behavior documented rather than assumed prevented.
- **Done only when:** neither source secrets nor unreviewed sensitive runtime state is exposed in model-facing or commit-ready artifacts.

#### PATCH-09 — Separate functional and security certification

- **Edit targets:** `.github/workflows/tests.yml`, test fixtures, `docs/INSTALL.md`, `docs/CONTINUOUS_SCOPE_ENFORCEMENT.md`, `SKILL.md`.
- **Implementation:** preserve Linux 3.10/3.11/3.13 and Windows 3.14 functional jobs; add Windows security job capable of real symlink/junction tests in an isolated runner; publish skip reasons and job result separately. Add deterministic smoke test for packaging and installation paths.
- **Tests:** all P0 tests must pass; security-critical negative cases must **not** be silently counted as PASS when skipped; manual OneDrive/network-share result stays NOT RUN until performed.
- **Done only when:** green matrix with actual security coverage and no unreviewed skip masking.

#### PATCH-10 — Future authenticated MCP service (not part of Windows hotfix)

- **Edit targets:** separate adapter/server package, `scripts/mcp_boundary.py` integration, authentication and audit docs.
- **Implementation:** read-only by default; server-owned fixed repository; per-operation allowlist and consent; authenticated principal; no arbitrary shell or client-selected root; replay/rate protections and audit.
- **Tests:** cross-repository, changed HEAD, mismatched Session ID, unauthorized write, arbitrary-command injection, replay, user-denied mutation.
- **Done only when:** production host tests independently verify authorization and filesystem isolation. The existing `mcp_boundary.py` is **not** the completed MCP server.

### 6.3 Proposed patch/PR delivery order

1. **PR #5a (small, targeted):** PATCH-01 and PATCH-02 plus focused Windows CI regressions. May update the current draft PR #5, but do not merge it while failures exist.
2. **PR #6 (protection first):** PATCH-03 and PATCH-05 with non-destructive ownership/collision tests; no silent file migration.
3. **PR #7 (filesystem assurance):** PATCH-04 with Windows security tests and explicit supported threat model.
4. **PR #8 (integrity):** PATCH-06 and PATCH-07; include CRLF compatibility and stale metadata/adversarial session tests.
5. **PR #9 (privacy and quality):** PATCH-08 and PATCH-09; update `.handoff.md` and `.riskdetail.md` from actual evidence.
6. **Future separate version:** PATCH-10 only after core data-safety gates are demonstrably satisfied.

Numbers #6–#9 are *proposed ordering labels*, not created pull requests. Do not assume those PRs exist. No schedule or engineer allocation is asserted.

### 6.4 Release and rollback gates

**Gate G0 — Before code mutation:** clean Git status, canonical branch verified, no existing ACTIVE session requiring recovery, disposable test project and pre-change hashes/backups; risks and intended write/delete paths enumerated.

**Gate G1 — Feature correctness:** tests covering the patch fail before the fix and pass after it; all Linux 3.10/3.11/3.13 and Windows 3.14 functional jobs PASS; original four Windows regressions explicitly named.

**Gate G2 — Data protection:** every existing user-owned collision fixture preserved byte-for-byte; no out-of-root reads/writes/deletes or accidental Git mutation; real symlink/junction tests exercise the denial path (not just skip).

**Gate G3 — Integrity and privacy:** exact hash verification before any pending-log deletion; crash/retry safety; sensitive content not emitted to logs/context; reproducible results in a temporary Git checkout.

**Gate G4 — Approval and merge:** reviewer checks changed files, expected mutations, CI evidence and residual risks; close P0 blockers with links; update `.handoff.md` and `.riskdetail.md`; merge only after explicit approval.

**Rollback:** retain the prior stable commit and any generated-data backup; revert an unsafe patch commit rather than deleting user files or resetting the worktree destructively. If a version migration is involved, use an explicit migration/restore procedure and never auto-remove old artifacts.

### 6.5 Evidence captured at planning time

- Stable v0.6.4: Linux 3.10/3.11/3.13 PASS, [run 43192199099](https://github.com/RyugaWork/spec2code/actions/runs/43192199099).
- Draft PR #5: Linux jobs PASS; Windows 3.14 reports `79 tests, failures=2, errors=2`, [run 43196836721](https://github.com/RyugaWork/spec2code/actions/runs/43196836721).
- Direct current failures: `test_active_feature_static_manifest_without_content`, `test_router_includes_spec_kit_artifacts`, `test_missing_plan_blocks_implement`, `test_cache_document_path_escape_rejected`.
- The Windows Spec Kit failures reach `FEATURE_DIRECTORY_NOT_FOUND_OR_UNSAFE`; the Path Guard regression sees `SCOPE_VIOLATION` instead of the expected cached-path refusal. The root-alias explanation is a source-supported **hypothesis requiring regression proof**, not a verified exploit.
