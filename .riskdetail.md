# Spec2Code — Detailed Security, Data-Safety and Reliability Risk Register

> **Snapshot:** 2026-11-12 (Asia/Ho_Chi_Minh).  
> **Reviewed code:** stable `spec2code/InitialVersion_v0` / `20e81bf`; proposed Windows changes `fix/windows-portability-v0.6.4` / `e760bf0`.  
> **Linked status:** [`.handoff.md`](.handoff.md). **Mitigation roadmap:** [`.plan.md`](.plan.md).  
> **Review method:** source inspection and existing GitHub/local test reports; **not** a full dynamic penetration test or security certification.

## 1. Severity and disposition rules

- **CRITICAL:** verified or credible uncontrolled system-wide damage, remote code execution or secret extraction.
- **HIGH:** potentially destructive or boundary-breaking behavior involving user files, unsupported OS isolation, or privileged tool delegation.
- **MEDIUM:** integrity/reliability or information-exposure issue requiring plausible operational conditions.
- **LOW:** contained usability/documentation/observability limitation.
- **OPEN:** no complete mitigation evidence. **IN PROGRESS:** a patch exists but acceptance is not met. **MITIGATED:** code and independent regression/CI evidence confirmed. **ACCEPTED:** accountable review explicitly accepts residual exposure. A unit-test skip is not mitigation.

A severity is an engineering priority assessment, **not** proof that a vulnerability is exploitable.

## 2. Executive safety boundary

The Python core can:
- Read eligible files and metadata within the validated Git checkout, plus its own bundled configuration.
- Create/replace generated architecture indexes, `.agents/state/*`, context packs and `.handoffs/*` files.
- Delete a stale managed context pack or exact verified pending log; remove owned temp files and a merge lock.
- Execute bounded **read-only** local Git commands and optional local version probes.

The inspected Python core has no automatic Git remote fetch/push, destructive Git reset/rebase, arbitrary MCP shell capability, or general source-code deletion command. However, **the skill is not an OS sandbox**: a separate AI agent equipped with unrestricted shell/filesystem tools may modify or delete files independently of Spec2Code. The operating system's account privileges remain the ultimate boundary.

## 3. Risk entries

### RISK-001 — Windows filesystem TOCTOU protection is incomplete
- **Severity:** HIGH; **Likelihood:** environment-dependent; **State:** OPEN.
- **Affected:** `scripts/scope_io.py`, `scripts/path_guard.py`; Windows (including synced/shared workspaces).
- **Evidence:** Windows fallback revalidates path before file operations but has no POSIX-style directory-handle + `O_NOFOLLOW` guarantee. Explicitly documented in `docs/CONTINUOUS_SCOPE_ENFORCEMENT.md`.
- **Impact:** hostile concurrent path replacement could invalidate an earlier path validation; file read/write/unlink may target a different object than expected under some race conditions.
- **Existing controls:** root and path checks; symlink checks; OS ACLs; exact hash for handoff unlink.
- **Required mitigation:** assess Windows handle-based no-follow/file-identity APIs or isolate the process under dedicated filesystem permissions; adversarial concurrent swap tests with untouched external sentinels. Never claim complete containment based only on repeated `Path.resolve()` checks.
- **Closure evidence:** reproducible Windows adversarial test suite and documented OS-level guarantee/limitation.
- **Related plan:** M-02, M-03, M-04.

### RISK-002 — Case-insensitive collisions between generated architecture and source
- **Severity:** HIGH; **State:** IN PROGRESS / NOT ACCEPTED.
- **Affected:** `.config/architecture.json` (generated folder `API`), `.config/scanner.json` (source root `api`), scanner and architecture publisher.
- **Evidence:** user's Windows Python 3.14.2 run logged `REVIEW_UNATTRIBUTED | api/.summerize.md` and repeated `SESSION_FAILED | Session has unclassified path changes`. A scanner exemption was drafted in PR #5.
- **Impact:** self-generated files may be mistaken for source changes; sessions blocked; output/source collisions may disrupt a real project.
- **Existing controls:** some managed-marker checks; draft scanner exclusion for generated dot-prefixed Markdown.
- **Required mitigation:** reserve distinct nonconflicting output namespace (preferred) or enforce preflight case-folded collision checks across all generated names; test `api/API`, `present/Present`, other mapped layers on Windows.
- **Closure evidence:** clean session, no false source deltas, no user-file mutation, Windows CI PASS; validate several framework layouts.
- **Related plan:** M-01, M-03.

### RISK-003 — Windows short-path/8.3 aliases falsely rejected
- **Severity:** MEDIUM; **State:** IN PROGRESS.
- **Affected:** root and bundled-skill canonicalization (`scripts/path_guard.py`, `scripts/config_loader.py`, `scripts/session_guard.py`, `scripts/scope_io.py`).
- **Evidence:** an earlier Windows CI run rejected legitimate temporary root `RUNNER~1` as `PATH_GUARD_BLOCKED: missing or symlinked repository root`. PR #5 contains an attempted fix; its latest Windows job still fails.
- **Impact:** valid Windows checkout cannot run, with potential incorrect interpretation of path identity.
- **Required mitigation:** normalize aliases by *actual filesystem identity*, while separately refusing genuine symlinks/junctions; test long/short path pairs, installed skill paths, worktrees.
- **Closure evidence:** Windows CI and dedicated 8.3 root tests PASS without weakening cross-repository protection.
- **Related plan:** M-01, M-02.

### RISK-004 — CRLF/LF conversion breaks binary integrity and handoff parsing
- **Severity:** MEDIUM; **State:** IN PROGRESS.
- **Affected:** `scripts/scope_io.py`, `scripts/handoff_store.py`, emitted Markdown/JSONL.
- **Evidence:** Windows original test expected `b'first\nsecond\n'` but observed `b'first\r\nsecond\r\n'`; separate failure `Pending log header mismatch`.
- **Impact:** failed byte comparisons, unexpected re-writes or inability to finish/merge a session.
- **Existing controls:** PR #5 attempts LF writing and CRLF-compatible legacy log parsing; raw-file hashes still used for deletion.
- **Required mitigation:** LF-only writes for managed state; legacy text normalization for *parsing only*; exact original bytes for hash verification and deletion; migration regression test.
- **Closure evidence:** Windows end-to-end `start -> record -> finish -> merge` with both LF and legacy CRLF logs, idempotent archive and verified cleanup.
- **Related plan:** M-01, M-04.

### RISK-005 — Symlink/junction coverage on unprivileged Windows is insufficient
- **Severity:** HIGH for security assurance; **State:** OPEN.
- **Affected:** repository-root, managed-path, parent-directory and Spec Kit feature checks.
- **Evidence:** user's local run skipped 10 tests due to unavailable symlinks and errored in `test_symlinked_feature_pointer_rejected` with `WinError 1314`; PR #5 changes the latter to skip when unsupported.
- **Impact:** PASS on other tests would not demonstrate successful symlink/junction escape denial on this platform.
- **Required mitigation:** retain non-admin functional tests; run privileged developer-mode or equivalent dedicated negative tests with real symlink/junction fixtures; test file, directory, ancestor and root swaps.
- **Closure evidence:** verified external-sentinel unchanged and every path-escape attempt denied, with explicit tested privileges.
- **Related plan:** M-02.

### RISK-006 — Existing project-owned files may conflict with managed paths
- **Severity:** HIGH; **State:** OPEN.
- **Affected:** `.agents/state`, `.handoffs`, root `.summerize.md`, generated layer/component docs.
- **Evidence:** `scope_io.atomic_text()` replaces its target; `save_state()`, manifests and context packs are written to fixed managed paths. Some architecture docs detect non-managed markers, but not every state file has equivalent ownership/collision safeguards.
- **Impact:** data in an existing project sharing a managed path can be overwritten, or the skill can fail to operate.
- **Required mitigation:** explicit installation preflight, ownership manifest, reserved namespace, no overwrite without managed marker/expected hash, backup/rollback path; test preexisting arbitrary files.
- **Closure evidence:** fixture with conflicting state and docs preserved byte-for-byte; operation aborts with clear error before mutation.
- **Related plan:** M-03, M-04.

### RISK-007 — File deletion is real, even when constrained
- **Severity:** MEDIUM; **State:** OPEN (expected behavior requiring audit).
- **Affected:** `scope_io.unlink_verified()`, stale `.agents/state/context-pack.json` invalidation, handoff pending-log deletion, temporary-file and lock cleanup.
- **Evidence:** exact unlink calls exist in `scripts/session_guard.py`, `scripts/handoff_store.py` and `scripts/scope_io.py`; handoff deletion checks session ID, header, raw SHA-256 and persisted archive.
- **Impact:** operator may expect read-only behavior but lose managed ephemeral content during checkpoint/merge, or on a software defect.
- **Required mitigation:** document lifecycle/ownership, make destructive operations auditable, preserve backups where appropriate, test crash/partial-write/retry cases; prohibit wildcard deletion.
- **Closure evidence:** read/write/delete access matrix and regression tests prove only explicitly owned exact files removed.
- **Related plan:** M-04, M-07.

### RISK-008 — Generated artifacts and change notes may leak through Git/OneDrive
- **Severity:** MEDIUM; **State:** OPEN.
- **Affected:** root `.summerize.md`, `API/`, `Present/` and other generated layer directories; `.handoffs/.buildnotes.handoff.md`.
- **Evidence:** repository `.gitignore` excludes `.agents/state/` and `.handoffs/.details/` but does not cover all generated architecture folders or merged handoff ledger. The latter may include source paths and user-entered change notes.
- **Impact:** unintended commits, external sync, metadata exposure and source-tree noise. This is not evidence of automatic exfiltration by Spec2Code.
- **Required mitigation:** project-safe ignore/install instructions, keep generated artifacts in one reserved path, redact notes, test `git status` before/after session; account for cloud-sync behavior.
- **Closure evidence:** no managed sensitive files staged by `git add .` in a fixture; documented opt-in rules for publishing handoff summaries.
- **Related plan:** M-05.

### RISK-009 — Path Guard does not constrain a separate AI agent's shell
- **Severity:** HIGH; **State:** OPEN (architectural boundary).
- **Affected:** any integration invoking Spec2Code from an agent that also has unrestricted command/filesystem capabilities.
- **Evidence:** the guard applies only when code enters guarded functions. `mcp_boundary.py` explicitly denies arbitrary shell *through its own interface*, but does not revoke a host's independent tools.
- **Impact:** an overprivileged agent could modify or delete machine files outside the guarded repository without going through Spec2Code.
- **Required mitigation:** run external agents under dedicated OS accounts/workspaces, restrict shell and filesystem permissions independently, require approval for destructive writes.
- **Closure evidence:** end-to-end host permission tests and OS-level containment demonstration; document residual exposure.
- **Related plan:** M-02, M-09.

### RISK-010 — MCP authorization library is not a deployed secure service
- **Severity:** HIGH if mistaken for complete MCP deployment; **State:** NOT IMPLEMENTED.
- **Affected:** `scripts/mcp_boundary.py`; any future MCP integration.
- **Evidence:** only request-authorization logic exists; no network listener, authenticated transport, production credential handling, or real-host consent flow.
- **Impact:** deployment without these additional controls could allow unauthorized or unaudited write operations.
- **Required mitigation:** server-owned checkout, authN/authZ, write-consent UX, replay protection, rate limits and per-operation audit; prohibit client root override and arbitrary shell.
- **Closure evidence:** independent security tests for an actual MCP server (not only authorization unit tests).
- **Related plan:** M-09.

### RISK-011 — Sensitive-file detection is allowlist/heuristic-based
- **Severity:** MEDIUM; **State:** OPEN (residual).
- **Affected:** scanner permitted paths, file name/extension filters and task-specific logging.
- **Evidence:** exclusion protects known names such as `.env`, key files and sensitive config names; new or unusual secret files may not match. Spec2Code normally reports hashes/metadata, but names can still be exposed in generated indexes/handoff notes.
- **Impact:** private path names or accidentally included readable content in future integrations.
- **Required mitigation:** conservative content-access allowlist, no source content in model-facing context packs, no tokens in log notes, security tests for unusual secret names.
- **Closure evidence:** privacy regression set including novel secret patterns and redacted generated output.
- **Related plan:** M-05.

### RISK-012 — Stale or corrupt session state can block work
- **Severity:** MEDIUM; **State:** OPEN.
- **Affected:** `.agents/state/session.json`, architecture/symbol caches, `.handoffs` pending logs, Git HEAD checkpoints.
- **Evidence:** deliberate fail-closed checks on missing binding, changed HEAD, corrupt audit evidence and unclassified changes.
- **Impact:** interrupted or upgraded sessions may be unrecoverable without manual procedure; bypassing checks to restore availability risks data integrity.
- **Required mitigation:** versioned state migration/backup, guided manual recovery, corruption and interrupted-process tests; never silently drop an ACTIVE session.
- **Closure evidence:** tested restart and disaster-recovery fixtures with consistent audit trail.
- **Related plan:** M-07.

### RISK-013 — Cross-platform CI passing is not security certification
- **Severity:** MEDIUM; **State:** OPEN.
- **Evidence:** stable CI covers Linux Python 3.10/3.11/3.13; local Windows 3.14.2 original run had 77 tests (17 failures, 1 error, 10 skipped). Draft PR #5 Windows CI run 43196836721 had 79 tests (2 failures, 2 errors). macOS, OneDrive/network filesystem races, real MCP and hostile concurrency remain NOT RUN.
- **Impact:** false confidence from platform-limited PASS or security skips.
- **Required mitigation:** separate functional CI from OS-specific security suite; publish explicit PASS/FAIL/SKIPPED counts; audit critical escape tests using real filesystem constructs.
- **Closure evidence:** comprehensive platform matrix with limitations and repeatable artifacts.
- **Related plan:** M-01, M-02, M-06.

## 4. Ranked security priorities

1. **P0:** RISK-002, RISK-003, RISK-004 — restore correct Windows behavior without weakening boundaries.
2. **P0:** RISK-001, RISK-005, RISK-006, RISK-009 — prove containment and user-data ownership before use on sensitive repositories.
3. **P1:** RISK-007, RISK-008, RISK-011, RISK-012, RISK-013 — controlled cleanup, privacy, recovery and verified test coverage.
4. **P2:** RISK-010 — only when implementing an actual authenticated MCP server.

No RISK item is marked `MITIGATED` merely because a draft patch or unit test exists.

## 5. Safe-use guidance pending closure

- Test on a disposable Git clone with no irreplaceable data; back up the working tree first.
- Run as a normal restricted Windows account, not elevated, except in dedicated symlink tests.
- Inspect existing `.agents/`, `.handoffs/`, `.summerize.md` and architecture-directory names before installation.
- Check `git status` and untracked generated files after a session; keep sensitive state out of commits and cloud sync.
- Do not give an AI agent machine-wide PowerShell or filesystem permissions merely because Spec2Code has Path Guard.
- Do not merge draft PR #5 or label Windows production-ready until current Windows CI and destructive-operation tests have passed.

## 6. Evidence and follow-up references

- Stable code: https://github.com/RyugaWork/spec2code/tree/spec2code/InitialVersion_v0
- Windows patch and review: https://github.com/RyugaWork/spec2code/pull/5
- Stable CI: https://github.com/RyugaWork/spec2code/actions/runs/43192199099
- Latest audited Windows CI: https://github.com/RyugaWork/spec2code/actions/runs/43196836721
- Implementation paths: `scripts/path_guard.py`, `scripts/scope_io.py`, `scripts/session_guard.py`, `scripts/architecture_tree.py`, `scripts/handoff_store.py`, `scripts/mcp_boundary.py`, `.config/*.json`.
- Local Windows test evidence was provided in the conversation on 2026-11-12; repository does not contain an authenticated copy of that local runtime log.

**Risk update rule:** revise severity/state only with observed evidence; retain the original finding and attach the test run, commit, review decision and residual limitation. Distinguish design intent, tests that actually ran, and untested scenarios.


## 7. Patch-to-risk traceability and closure criteria (2026-11-12)

The patch IDs below identify **planned work**, not released fixes. Each risk remains OPEN or IN PROGRESS until an exact commit, a passing regression test, cross-platform evidence, and residual-risk decision are recorded. The implementation contracts, prerequisites and release gates are in [`.plan.md`](.plan.md), section 6.

| Risk ID | Planned patch | Priority | Mandatory regression evidence | Closure decision |
| --- | --- | --- | --- | --- |
| RISK-001 | PATCH-04 | P0 | Actual Windows symlink/junction/path-swap and external-sentinel tests; documented OS guarantee | OPEN |
| RISK-002 | PATCH-03 | P0 | Case-folded output/source collision fixtures; no user-owned file replaced | IN PROGRESS, patch not accepted |
| RISK-003 | PATCH-01, PATCH-02 | P0 | Windows long/8.3-path equality and distinct-worktree rejection | IN PROGRESS, patch not accepted |
| RISK-004 | PATCH-06 | P1 | LF and legacy CRLF start/record/finish/merge with raw SHA-256 check | IN PROGRESS, patch not accepted |
| RISK-005 | PATCH-02, PATCH-04, PATCH-09 | P0 | Real symlink and junction tests without treating privilege-related skips as PASS | OPEN |
| RISK-006 | PATCH-03, PATCH-05 | P0 | Pre-existing user files and generated output collision fixtures retain original bytes | OPEN |
| RISK-007 | PATCH-05, PATCH-06 | P0 | Exact-file deletion allowlist, crash/retry, checksum mismatch and no wildcard removal | OPEN |
| RISK-008 | PATCH-03, PATCH-08 | P1 | `git add .` hygiene and safe handling of generated architecture/handoff notes | OPEN |
| RISK-009 | PATCH-04, PATCH-10 | P0 boundary / P2 adapter | OS/host permission test; no assumption that Python guard controls host shell | OPEN |
| RISK-010 | PATCH-10 | P2 | Authenticated real MCP server tests, write-consent and cross-repo denial | NOT IMPLEMENTED |
| RISK-011 | PATCH-08 | P1 | Sensitive-content filtering, unusual secret names, redacted notes/context | OPEN |
| RISK-012 | PATCH-05, PATCH-07 | P1 | Stale/corrupt state, interrupted write and verified recovery | OPEN |
| RISK-013 | PATCH-01, PATCH-02, PATCH-04, PATCH-09 | P0/P1 | All required OS CI green; security-critical scenarios actually exercised | OPEN |
| RISK-014 | PATCH-07 | P1 | Same-size source edit with unchanged/restored `mtime_ns` detected at security-critical revalidation | OPEN |

### RISK-014 — Cached file fingerprint may miss changed bytes when metadata is preserved

- **Severity:** MEDIUM for audit correctness, potentially HIGH if relying solely on cached metadata to authorize security-critical source decisions; **State:** OPEN.
- **Affected:** `scripts/scan_infrastructure.py` (`describe_file` fast path), `scripts/context_router.py` (selected source `size`/`mtime_ns` recheck), `scripts/session_guard.py` (fingerprint attribution).
- **Source evidence:** when `verify=False`, an existing file's SHA-256 can be reused if size and `mtime_ns` match the previous snapshot; selected-file freshness uses metadata comparisons. This is a plausible false-negative under deliberate timestamp restoration, not a demonstrated external compromise.
- **Possible impact:** stale context, inaccurate provenance and approval based on incorrectly treated source equality, even while file bytes have changed.
- **Mitigation:** require a fresh bounded byte hash at decisions that require strong source identity (security-critical finish, source selection, record/change attribution); retain configurable scanning limits and protect against excessive large-file reads.
- **Required tests:** same-length mutation with restored `mtime_ns`, git HEAD unchanged, deliberate stale selected source, oversized/metadata-only file path and a valid unchanged control.
- **Closure evidence:** test must fail before the patch, pass after it, with safe resource use and no weakening of Path Guard.
- **Related plan:** PATCH-07, M-07.

### Windows PR #5 failure analysis (latest inspected run)

Latest recorded: [GitHub Actions run 43196836721](https://github.com/RyugaWork/spec2code/actions/runs/43196836721), Windows Python 3.14, `79 tests`, `2 failures`, `2 errors`. The Linux 3.10/3.11/3.13 jobs of that run were PASS.

- `test_active_feature_static_manifest_without_content` and `test_router_includes_spec_kit_artifacts`: errors from `speckit_bridge._feature_path()` with `FEATURE_DIRECTORY_NOT_FOUND_OR_UNSAFE`.
- `test_missing_plan_blocks_implement`: same premature feature-path failure instead of expected missing-plan gate.
- `test_cache_document_path_escape_rejected`: observed `SCOPE_VIOLATION: session repository binding changed` instead of expected `PATH_GUARD_BLOCKED` for injected `../outside/keep.txt`.

**Interpretation:** a Windows root-alias/session-binding issue and inconsistent `Path.resolve()` comparison are strong debugging hypotheses; the CI logs prove the error messages, **not** the root cause or an exploit. PATCH-01 and PATCH-02 must reproduce and validate the root cause before weakening or altering any security check.

### Patch acceptance checklist

- [ ] A scoped patch branch and risk-linked regression tests exist.
- [ ] Reproduction demonstrates the failure before the fix.
- [ ] Linux Python 3.10/3.11/3.13 functional CI PASS.
- [ ] Windows Python 3.14 functional CI PASS.
- [ ] Required Windows security-negative tests execute (not silently skipped) where the patch changes trust boundaries.
- [ ] An external sentinel remains byte-for-byte unchanged under rejected read/write/delete tests.
- [ ] Existing user-owned path collisions fail closed without alteration.
- [ ] All deletion paths retain exact ownership and SHA-256 verification; no wildcard cleanup.
- [ ] Residual limitations are documented in `.riskdetail.md`, with explicit review decision.
- [ ] `.handoff.md` records exact commit, test artifacts and merge state.

No closure boxes are checked by the act of writing this plan.
