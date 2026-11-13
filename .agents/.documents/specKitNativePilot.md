# PLAN-093 / SK-03 — Native Spec Kit pilot for the S2C development repository

> **Recorded 2026-11-13. Status: PILOT_PREPARED / NATIVE_NOT_RUN / NETWORK_BLOCKED.** This is an operator-run playbook, not a claim that the official Spec Kit CLI ran in S2C. No additional branches, repository code changes, CI/CD, host install, A.1/B.1 approval or merge.

## 1. Verified upstream version and environment

| Item | Observed evidence | Disposition |
| --- | --- | --- |
| Candidate stable previous-minor release | [Official v1.2.6](https://github.com/github/spec-kit/releases/tag/v1.2.6), published **2026-11-02**; upstream release explicitly supplies a pinned Git install | **CANDIDATE_FOR_DISPOSABLE_PILOT**, not owner-approved production baseline |
| Latest comparison | [v1.4.0](https://github.com/github/spec-kit/releases/tag/v1.4.0), published 2026-11-10, contains newer FileHelper/URL security changes | Do not auto-adopt immediately, but assess whether older-version security issues preclude use outside the disposable pilot |
| Python requirements | [v1.2.6 pyproject.toml](https://github.com/github/spec-kit/blob/v1.2.6/pyproject.toml) declares Python >=3.11 | Disposable environment: Python 3.13.5; this meets minimum, **does not prove dependency compatibility** |
| Installation syntax | [Official v1.2.6 command_init.py](https://github.com/github/spec-kit/blob/v1.2.6/src/specify_cli/command_init.py) accepts `--here`, `--force`, `--non-interactive`, `--integration` and `--script` | Static source verified; no actual execution |
| Existing Constitution behavior | `ensure_constitution_from_template` skips when `.specify/memory/constitution.md` exists | This *particular* path expected preserved; other generated files may still collide |
| Codex integration | [Official v1.2.6 Codex integration](https://github.com/github/spec-kit/blob/v1.2.6/src/specify_cli/integrations/codex/__init__.py) installs skills under `.agents/skills/speckit-*/SKILL.md` | S2C does not yet have native generated skills |
| Existing-project safety | [Official guidance](https://github.com/github/spec-kit/blob/v1.2.6/docs/guides/existing-projects.md) warns `--force` can overwrite managed files and requires a reviewable diff | Disposable worktree and collision review mandatory |
| Current runner | Git 2.47.3, Python 3.13.5, `uv` present, `specify` unavailable | DNS failure on `git ls-remote`; `uvx --offline --from git+https://github.com/github/spec-kit.git@v1.2.6 specify version` exited 1 (Git dependency unresolved). **No native install, init, test or skills executed** |

A previous-minor tag is not a blanket security or compatibility endorsement. Record an explicit owner version choice, official release and host-specific test result before adopting generated artifacts in any non-disposable checkout.

## 2. Required safe pilot procedure (for a real authorized Codex/Codespaces terminal)

**Preconditions:** explicit operator approval and tool network access; clean original checkout; sufficient disk; owned disposable directory; reviewed candidate release; Git SHA and the source/host AGENTS binding; no symlinked/junction path; no pre-existing unowned files at the target.

### Linux / GitHub Codespaces

```bash
set -euo pipefail
git diff --quiet && git diff --cached --quiet
test -z "$(git ls-files --others --exclude-standard)"

HEAD_SHA="$(git rev-parse HEAD)"
PILOT_PARENT="$(mktemp -d)"
PILOT_ROOT="$PILOT_PARENT/spec2code"
git worktree add --detach "$PILOT_ROOT" "$HEAD_SHA"
cd "$PILOT_ROOT"

# Capture before-state fingerprints for sensitive owner-controlled files.
git show HEAD:.specify/feature.json | sha256sum
git show HEAD:.specify/memory/constitution.md | sha256sum
git show HEAD:AGENTS.md | sha256sum

# Native commands: require network access and reviewed operator approval.
uvx --from 'git+https://github.com/github/spec-kit.git@v1.2.6' specify version
uvx --from 'git+https://github.com/github/spec-kit.git@v1.2.6' specify init   --here --force --non-interactive --integration codex --script py

# Examine the full generated state BEFORE choosing any files for adoption.
git status --short
git diff --name-status
git diff -- .specify/feature.json .specify/memory/constitution.md AGENTS.md
find .specify/scripts .agents/skills -type f -print 2>/dev/null | sort || true
python .specify/scripts/python/check_prerequisites.py   --json --require-spec --require-tasks --include-tasks
```

`git diff` does not list new untracked files; the `git status` and generated-file inventory must be reviewed as well. **No auto-merge or `worktree remove --force`**. Keep disposable output for inspection; clean up only after confirming ownership.

### Windows PowerShell

```powershell
$ErrorActionPreference = 'Stop'
git diff --quiet
if ($LASTEXITCODE -ne 0) { throw 'Uncommitted tracked changes' }
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { throw 'Staged changes present' }
if (git ls-files --others --exclude-standard) { throw 'Untracked files need review' }

$headSha = (git rev-parse HEAD).Trim()
$pilot = Join-Path $env:TEMP ('s2c-speckit-pilot-' + $headSha.Substring(0, 12))
if (Test-Path $pilot) { throw 'Disposable location already exists' }
git worktree add --detach $pilot $headSha
if ($LASTEXITCODE -ne 0) { throw 'Worktree creation failed' }

Push-Location $pilot
try {
    git status --short
    Get-FileHash .specify/feature.json, .specify/memory/constitution.md -Algorithm SHA256
    uvx --from 'git+https://github.com/github/spec-kit.git@v1.2.6' specify version
    if ($LASTEXITCODE -ne 0) { throw 'Cannot run official CLI; STOP' }

    uvx --from 'git+https://github.com/github/spec-kit.git@v1.2.6' specify init `
        --here --force --non-interactive --integration codex --script py
    if ($LASTEXITCODE -ne 0) { throw 'Native initialization failed; STOP' }

    git status --short
    git diff --name-status
    git diff -- .specify/feature.json .specify/memory/constitution.md AGENTS.md
    Get-ChildItem .specify/scripts, .agents/skills -File -Recurse -ErrorAction SilentlyContinue |
        Select-Object -ExpandProperty FullName

    python .specify/scripts/python/check_prerequisites.py `
        --json --require-spec --require-tasks --include-tasks
    if ($LASTEXITCODE -ne 0) { throw 'Spec Kit prerequisite check failed' }
} finally {
    Pop-Location
}
```

These are **documented commands, NOT executed in this turn**. They do not install a CI workflow, run against a production host or grant B implementation permissions. Keep Windows/OneDrive/junction adversarial testing a separate risk-authorized M1 activity.

## 3. Acceptance record and quality gates

| ID | Required proof | Actual status |
| --- | --- | --- |
| SK3-01 | Clean original HEAD, safe detached worktree and before-state hashes | NOT_RUN |
| SK3-02 | Exact pinned `specify version` observed with OS and Python/runtime deps | BLOCKED — no tool network |
| SK3-03 | `specify init` completes in disposable checkout, complete generated file inventory | NOT_RUN |
| SK3-04 | Exact `feature.json`, Constitution, master AGENTS preserved or reviewed conflicts | NOT_RUN |
| SK3-05 | Official Python scripts, Codex skills, required templates present after init | NOT_RUN |
| SK3-06 | Real upstream prerequisite check correctly resolves this active feature | NOT_RUN |
| SK3-07 | Negative tests for missing/stale/symlinked/out-of-scope inputs and collision | NOT_RUN |
| SK3-08 | Maintainer reviews diff, approved subset and rollback before any PR adoption | NOT_RUN |

**Task mapping:** T006 candidate release provenance **researched but not approved**; T007–T009 native pilot **NOT_RUN**; T010–T015 independent A.1/B/B.1/release gates **NOT_RUN/NOT_AUTHORIZED**. Never mark any task PASS solely on this document.

## 4. Pending decisions and handoff

DEC-SK3-01 owner chooses reviewed release (including security-hardening differences); DEC-SK3-02 chooses real Codex/Codespaces/Windows host; DEC-SK3-03 explicitly permits force merge **inside a throwaway checkout only**; DEC-SK3-04 approves which generated files can be carried into current development branch; DEC-SK3-05 confirms reviewer/owner A.1 and B scope.

STOP state: `SK3_PILOT_BLOCKED_BY_TOOL_NETWORK`. Preserve original git branch, original `.specify/` and all currently unfinished task IDs. On RESUME recheck the exact current SHA, feature pointer, Constitution, applicable AGENTS and latest Google BRD revision. Do not use a fake CLI substitute, fabricated native test output or silent promotion to A1_PASS.


## 5. Actual disposable Git-worktree mechanics smoke test (NOT the native CLI)

A local **synthetic** miniature Git repository was initialized and committed with six representative S2C files: root AGENTS, feature.json, draft Constitution and feature spec/plan/tasks. Git then created one detached worktree at that exact SHA; SHA-256 hashes for all six files matched between original and disposable worktree, both worktrees remained clean, and the branch count stayed **one**. The synthetic temporary directory was automatically disposed when the test completed.

**Observed:** Git checkout isolation mechanism works in this Linux tool environment for ordinary files. **Not observed:** actual S2C checkout, Spec Kit CLI or official scripts, remote network, any Windows/junction/OneDrive attack case, user-host compatibility, A.1/B.1 or authorized code changes. Therefore `SK3-01` remains `NOT_RUN` for the real S2C native pilot. This smoke test cannot be promoted into a native `specify init` PASS.


## PLAN-097 — Mandatory upstream feature environment hygiene (before native pilot)

[Source-verified upstream behavior and new negative tests](specKitUpstreamEnvAudit097.md) show that `SPECIFY_FEATURE_DIRECTORY` may supersede `.specify/feature.json` and trigger `persist_feature_json`, unless `SPECIFY_FEATURE_NO_PERSIST=1` or `no_persist=True`. Upstream `get_feature_paths` also accepts absolute feature directories; `setup_plan.py` can create/write selected feature artifacts **without importing S2C's Path Guard**.

**Amend operator preflight:** In the already verified disposable checkout, clear `SPECIFY_FEATURE_DIRECTORY` and `SPECIFY_FEATURE`, then set `SPECIFY_FEATURE_NO_PERSIST=1` before **read-only** upstream preflight; validate the pointer under S2C's containment policy, hash it and re-hash afterward. In POSIX use `unset SPECIFY_FEATURE_DIRECTORY SPECIFY_FEATURE; export SPECIFY_FEATURE_NO_PERSIST=1`. In PowerShell use `Remove-Item Env:SPECIFY_FEATURE_DIRECTORY, Env:SPECIFY_FEATURE -ErrorAction SilentlyContinue` only when valid in the chosen PowerShell edition, or remove separately; then `$env:SPECIFY_FEATURE_NO_PERSIST='1'`. Existing examples above are historic and **must be followed by this extra preflight**.

**Do not overclaim:** NO_PERSIST prevents automatic pointer writes in the inspected helper, **not arbitrary writes from setup_plan/implement**; neither it nor `git status` validates external path sentinels or Windows junction safety. Add cases `SK97-NEG-01..05` to native acceptance review; all NOT_RUN. No CLI or host tests were executed in PLAN-097.
