# PLAN-097 — Official Spec Kit native environment override and filesystem scope audit

> **SOURCE_VERIFIED / HOST_NOT_RUN / 2026-11-13**. Official upstream `github/spec-kit` tags `v1.2.6` and `v1.4.0` were read through the GitHub connector; S2C baseline source is commit `da7531bb029dbd3bad05bdd6a8d28808ac4b97eb`. This document does not claim an exploit executed against either project, CLI installation, test PASS, or A.1/B/B.1 authority.

## 1. Source facts confirmed on both official release tags

| Source | Exact code-level behavior | S2C integration consequence |
| --- | --- | --- |
| [v1.2.6 common.py](https://github.com/github/spec-kit/blob/v1.2.6/scripts/python/common.py), lines 79–185; [v1.4.0 common.py](https://github.com/github/spec-kit/blob/v1.4.0/scripts/python/common.py) | `get_feature_paths()` reads `SPECIFY_FEATURE_DIRECTORY` before persisted `.specify/feature.json`. It accepts either absolute or relative `Path`. The inspected function does not invoke S2C `path_guard.py` or an equivalent in-root containment validator. | Native scripts are **not automatically protected** by S2C's guarded `speckit_bridge.discover()`. Never pass untrusted absolute/outside or symlinked feature directories to an upstream mutating command. |
| Same `common.py`, lines 99–119 and 143–155 | With nonempty `SPECIFY_FEATURE_DIRECTORY`, `get_feature_paths()` invokes `persist_feature_json()` **unless** `no_persist=True` or `SPECIFY_FEATURE_NO_PERSIST` is exactly `1` or `true`. Persistence can update `.specify/feature.json` even when the operator expected a read-only metadata action. | For read-only orchestration use `SPECIFY_FEATURE_NO_PERSIST=1` and clear untrusted `SPECIFY_FEATURE_DIRECTORY` and `SPECIFY_FEATURE`. This prevents only feature-pointer persistence, **not all filesystem writes**. |
| [v1.2.6 setup_plan.py](https://github.com/github/spec-kit/blob/v1.2.6/scripts/python/setup_plan.py), lines 51–84 | Calls `get_feature_paths()`, creates `feature_dir` using `mkdir(parents=True, exist_ok=True)`, and writes `plan.md` template with `write_bytes` under selected directory as appropriate. | If the selected feature is outside the authorized checkout, script logic can potentially act outside S2C scope. **Source-derived hazard**, not a reproduced vulnerability in a tested host. |
| [v1.2.6 check_prerequisites.py](https://github.com/github/spec-kit/blob/v1.2.6/scripts/python/check_prerequisites.py), lines 216–261 | Checks plan existence **and plan size = 0**, optional spec/tasks existence; invokes feature-path logic above. | Upstream has more stringent empty-plan check than S2C's current static bridge (PLAN-096). A read/check stage can still update the pointer under an unchecked environment override. |
| [v1.2.6 create_new_feature.py](https://github.com/github/spec-kit/blob/v1.2.6/scripts/python/create_new_feature.py), lines 270–454 | Creates feature directories/spec template and can persist new feature pointer unless NO_PERSIST; optional git mechanisms are a separate choice. | A feature-creation command is a **write**, never a read-only preflight; do not silently create Git branches or overwrite existing source. |

**Important distinction:** legitimate upstream scripts do not necessarily promise S2C Path Guard semantics. Their ability to operate on a user-selected directory is not automatically an upstream bug. S2C's integration requirements are stricter and must enforce its own execution boundary.

## 2. Risk register additions (no fabricated exploitation results)

- `SK-R10` **Native upstream feature-directory escape / pointer persistence mismatch**. Cause: upstream accepts an environment override and has scripts that may write through it; S2C's bridge guard protects *its own call*, not an independent upstream process. Link `RM-001`, `RM-002`, `RM-003`, `SKI-FR-001`, `SKI-FR-005`, `SKI-FR-007`, `SKI-FR-008`. Impact can be high if untrusted overrides are permitted. Likelihood, verified exploitability and residual risk remain **UNKNOWN** until actual host tests and owner review.
- `SK-R11` **False read-only assumption**. Cause: feature path resolution may persist `feature.json`. Link `RM-003`, `RM-013`, `SKI-FR-004`, `SKI-FR-009`. Mitigation design: sanitize and pin feature selection; set NO_PERSIST for read-only phases; before/after hash check. No real host test yet.

## 3. Disposable environment preflight proposal (operator commands; NOT EXECUTED)

All commands must be run **inside an already verified, owner-authorized temporary detached worktree**. The following is an example for a read-only upstream prerequisites invocation after official scripts are installed:

### POSIX / Codespaces

```bash
set -euo pipefail
# Start in the authorized disposable S2C worktree; verify real root with S2C guard first.
unset SPECIFY_FEATURE_DIRECTORY SPECIFY_FEATURE
export SPECIFY_FEATURE_NO_PERSIST=1
test -f .specify/feature.json
sha256sum .specify/feature.json > /tmp/s2c-feature-before.sha256
# Confirm a contained, real (non-symlinked) specs/<id> feature using S2C preflight.
# Upstream checks are NOT a substitute for S2C's guard.
python .specify/scripts/python/check_prerequisites.py --json --require-spec --require-tasks --include-tasks
sha256sum -c /tmp/s2c-feature-before.sha256
git status --short
```

`/tmp/s2c-feature-before.sha256` is a temporary operator-owned file; use a unique, non-colliding location and remove only with ownership confirmation. The `sha256sum -c` check detects pointer change, **not** writes to other paths. For a stronger scoped check, compare the entire before/after Git status, generated artifacts and external sentinel hashes.

### Windows PowerShell

```powershell
$ErrorActionPreference = 'Stop'
Remove-Item Env:SPECIFY_FEATURE_DIRECTORY -ErrorAction SilentlyContinue
Remove-Item Env:SPECIFY_FEATURE -ErrorAction SilentlyContinue
$env:SPECIFY_FEATURE_NO_PERSIST = '1'
$before = (Get-FileHash .specify/feature.json -Algorithm SHA256).Hash
# Independently validate S2C root/feature containment and junctions.
python .specify/scripts/python/check_prerequisites.py --json --require-spec --require-tasks --include-tasks
if ($LASTEXITCODE -ne 0) { throw 'Native prerequisite check failed' }
$after = (Get-FileHash .specify/feature.json -Algorithm SHA256).Hash
if ($before -ne $after) { throw 'Unexpected feature pointer mutation' }
git status --short
```

**No guarantee:** even with NO_PERSIST=1, another upstream script (such as `setup_plan.py`) may create/write feature artifacts. Never use a read-only label for it. Do not invoke on the real working branch or permit arbitrary feature paths. Windows fallback security is not an OS-level TOCTOU sandbox; require trusted workspace/ACLs and adversarial tests.

## 4. Five new negative/integration tests (all NOT_RUN)

| Case | Fixture/action in disposable real checkout | Expected observation | Required evidence |
| --- | --- | --- | --- |
| `SK97-NEG-01` | Untrusted `SPECIFY_FEATURE_DIRECTORY` = absolute path to owned outside sentinel dir; request guarded native entrypoint | S2C integration **blocks before** upstream script call; no outside write | Sentinel SHA, command refusal, exact root, OS |
| `SK97-NEG-02` | Valid in-root pointer and override; `SPECIFY_FEATURE_NO_PERSIST=1`; call upstream prerequisites | No pointer hash change; read metadata correctly; record actual process exit and file inventory | Before/after hashes, stdout/stderr, exit |
| `SK97-NEG-03` | Valid but different in-root override with NO_PERSIST unset, read-intent stage | Show actual upstream pointer persistence; S2C wrapper must detect and disallow write when request is read-only | Before/after pointer data, source diff and refusal |
| `SK97-NEG-04` | Feature override to symlink/junction ancestor pointing outside authorized checkout | Preflight blocks before upstream read/write; no sentinel corruption | Platform, junction type, sentinel hashes, rejection |
| `SK97-NEG-05` | Invoke `setup_plan.py` only in an owner-authorized disposable worktree with selected in-root feature | Generated path inventory and before/after diff reviewed; no unowned/outside write or new Git branch | OS, tag, SHA, generated files, approvals, rollback |

These five tests are **additional** to original 24 feature acceptance cases and the four PLAN-096 bridge negatives. They are not PASS, not run against an actual S2C checkout, and do not authorize code patches. Prior 4/24 GitHub Web/static PASS and 20/24 NOT_RUN remain unchanged.

## 5. Integration decisions and current gate

- `DEC-SK97-01`: use **no untrusted environment override** for read-only phases; sanitize `SPECIFY_FEATURE_DIRECTORY`/`SPECIFY_FEATURE` and set NO_PERSIST=1. **Proposed**, not enacted host hook.
- `DEC-SK97-02`: native scripts must run behind actual preflight with repository containment/symlink/junction policies in a disposable checkout; upstream feature path resolution is not S2C guard.
- `DEC-SK97-03`: owner approves exact upstream tag and installation collision scope. Version comparison is source-verified v1.2.6 and v1.4.0; both have the override/persistence behavior described.
- `DEC-SK97-04`: independent A.1, separate B-authorized host enforcement/negative tests and later B.1/release decision remain distinct.

**STOP:** The current runner could not resolve GitHub DNS and does not have `specify-cli`, so no upstream CLI/official script execution, local S2C bridge run or new native-negative PASS is claimed. See [native pilot](specKitNativePilot.md), [execution gate](../.workflow/specKitNativeExecutionGate.md), [feature test catalogue](../../specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md).
