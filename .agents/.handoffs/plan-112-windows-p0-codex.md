# PLAN-112 — P0 Windows containment, A-return and Codex handoff

**Dated:** 2026-11-15 (Asia/Ho_Chi_Minh). **Working branch:** docs/plan-089-a1-readiness; **input SHA:** 2f520d97b3d709aeb9c2bac563c37553925c0ec1. **Change class:** scoped A/P6-P8 design, acceptance and handoff, NOT native security execution, CODEX dispatch or formal A.1. No branch creation, code/config change, merge or release. Output SHA is the exact resulting Git commit reported after this combined documentation write.

## Review matrix completed before edits (G1)

| ID | Baseline factual gap | Risk | Planned affected owner file | Expected result | Failed result / rollback |
| --- | --- | --- | --- | --- | --- |
| P112-R01 | Windows scope_io fallback is path-based despite GetFileAttributesW reparse check | RM-001 P0 | docs/PATH_GUARD.md | Clear fail-closed host support boundary | Missing OS enforcement => NO_GO; revert only scoped docs |
| P112-R02 | Existing L1-SC test catalogue lacks full hostile interleaving evidence fields | RM-001 P0 | .agents/.workflow/testingAndDelivery.md | Concrete bounded negative fixtures and observable canary results | Any escape/inconclusive race => P0 OPEN |
| P112-R03 | Risk record has no explicit treatment choice/owner decision for Windows host classes | RM-001/005 P0 | .agents/.riskMatrix.md | Options, veto and unchanged residual | No approval => BLOCKED_OWNER |
| P112-R04 | No executable Codex packet and per-phase task counters for next wave | Workflow/owner P1 | .agents/.plans.md and this handoff | Task IDs, dependencies, expected/failed output, 9-task ledger | No Codex transport => HANDOFF_REQUIRED |
| P112-R05 | Parallel A.1 work and source drift | Collision P0 | Same branch, reviewed set of five Markdown files | Atomic fast-forward SHA lease; no runtime files overwritten | HEAD changed => stop and re-review, no force |

Review owner: author-side GPTWEB; independent reviewer count zero. The PLAN-111 source/CI is historical evidence, not a test executed by this update. No unsupported action is authorized by a review matrix. Preserve source/Spec Kit and host ownership.

## Observed progress before this design packet

Exact input branch 2f520d97b3d709aeb9c2bac563c37553925c0ec1. On that SHA, two GitHub Actions workflow runs 43593667987 and 43593664043 finished SUCCESS with Ubuntu Python 3.10/3.11/3.13 and Windows Python 3.14 (8/8 jobs). This is ordinary CI regression, not a validated hostile Windows race or A.1. .source/scripts/path_guard.py statically checks Windows reparse attributes; .source/scripts/scope_io.py explicitly documents Windows fallback non-anchored IO. RM-001 OPEN / RESIDUAL_UNKNOWN, A1-VAL-01..09 NOT_RUN, B_NOT_AUTHORIZED. This packet does not alter prior tests, version support or actual risk score.

## CODEX task request — T112-05 through T112-07

**Executor:** CODEX (real local environment, not GPTWEB simulation). **Status:** HANDOFF_REQUIRED; not actually sent to Codex by this Markdown commit. **Task parent:** PLAN-112. **Scope permission:** existing requester-directed targeted Path Guard/Workflow Guard P0 testing/remediation only; no general Phase-B authorization, installation, MCP, elevated host rights or merge. **Owned paths for any later separately scoped patch:** .source/scripts/path_guard.py, .source/scripts/scope_io.py, .source/tests/test_path_guard.py and existing relevant guard tests, only after preflight. The present documentation writer does not own those files.

1. T112-05 / Preflight: Check git status, current working branch/head, effective AGENTS and active feature; use a disposable clone/worktree, Windows build, FS/volume and user/ACL scope; verify installed Codex CLI and supported flags, sandbox, cancellation, output directories, allowed commands and tested time/attempt/cost limits. Do not use unverified --full-auto/YOLO. **Expected:** host evidence and sandbox proof. **Failure:** BLOCKED_HOST with exact observed stderr and zero mutation.
2. T112-06 / Verification: Execute the existing unit regression (python -m unittest discover -s .source/tests -v) and the synthetic Windows negative-case matrix in .agents/.workflow/testingAndDelivery.md, including the preflight-to-file-use interleaving; capture host audit, outside/protected sentinel hashes before/after, whether the race actually triggered, and files changed. **Expected:** no unauthorized read/write, verified OS denial, all mandatory cases evidenced. **Failure:** any escape => P0 FAIL and STOP; no race reached => INCONCLUSIVE, not security PASS.
3. T112-07 / Conditional repair: If a gap is observed and exact scope/authorization holds, propose a minimal source patch after a refreshed matrix and tests. Prefer preserving compatibility and a formally supported OS boundary rather than relying on repeated lexical path checks. Build and rerun all relevant tests and adverse host scenarios at new SHA; no unbounded loops, no external root writes, no clean/reset/stash/force or generated secret disclosure. **Expected:** source-bound patch, negative tests and evidence for independent review. **Failure:** rollback only own patch and return A/P6-P8; do not claim P0 closed.

**Security guardrails:** Synthetic fixtures only, hardened sandbox denies real outside-root data; never run race mutators on production data, home folders, active collaborative checkouts or real network sync. Set bounded process budgets, preserve before/after sentinel SHA-256 and exact failure reasons. No known unsafe CLI flags guessed. One writer per path; refresh branch source before any write. If the active user host lacks an authorized OS sandbox, do NOT execute the adversarial mutation; report BLOCKED_HOST instead.

**Expected handoff output schema:** task_id, baseline_sha, resulting_sha (if authorized), branch, reviewed matrix, host OS/build/filesystem, Codex CLI version and flags actually supported, sandbox/ACL evidence, test cases/commands/timeouts, pass/fail/skipped/inconclusive/blocked per case, sentinel hash ledger, scope/write diff, RM-001 disposition with source evidence, failures/rollback, remaining task counts and next independent reviewer.

## Gate and phase checkpoint

- T112-01..03: GPTWEB author-side source review, matrix and test/handoff design are completed as documentation work.
- T112-04: GPTWEB single-commit publication and post-commit source verification must be performed, not pre-declared PASS.
- T112-05..07: CODEX outstanding, require actual executor and authenticated host.
- T112-08: independent host/security owner outstanding; decides Windows support constraints and RM-001 residual; cannot waive mandatory containment.
- T112-09: independent A.1 reviewer outstanding, needs owner-backed BR-022..027 AC/quantitative denominators, ADR/host decisions and fresh Git/Google pair; A1-VAL-01..09 remain NOT_RUN.

Nine unique PLAN-112 tasks: at pre-write checkpoint done=3, remaining=6; upon verified commit done=4, remaining=5 (CODEX=3, owner/reviewer=2). Zero tasks may be treated as Codex-dispatched or security-completed merely because this record exists. A.1 FAIL/BLOCKED returns to A then fresh A.1; P0 or incomplete data => NO_GO. A.1 PASS never independently authorizes B.

## Authoritative references

- [PLAN-111 P0 handoff](plan-111-a1-p0-return-to-a.md)
- [Windows Path Guard design](../../docs/PATH_GUARD.md)
- [Risk matrix](../.riskMatrix.md)
- [Negative-case catalogue](../.workflow/testingAndDelivery.md)
- [Independent A.1 checks](../.workflow/validationSpecification.md)
- [AGENTS routing and review contract](../../AGENTS.md)
- Microsoft reparse behavior: https://learn.microsoft.com/en-us/windows/win32/fileio/reparse-points-and-file-operations
- Microsoft Win32 CreateFileW flags: https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew

**Final author disposition:** A_REWORK_REQUIRED / P0_OPEN / CODEX_HANDOFF_REQUIRED / FORMAL_A1_NOT_RUN / B_NOT_AUTHORIZED. Neither the native test runner nor a real Codex executor was invoked by the remote GitHub documentation author.
