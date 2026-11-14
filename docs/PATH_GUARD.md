# Path Guard — Spec2Code v0.6.3

## Security boundary

Every Spec2Code CLI entrypoint must first establish a **single, exact, local Git worktree root**. A directory inside a Git repository is not the root; a bare repository, ordinary directory, symlink alias, or directory outside the checkout is not permitted. The guard is implemented by `scripts/path_guard.py` and reused by `session_guard.py`, `scan_infrastructure.py`, `context_router.py`, and `speckit_bridge.py`.

The same validation applies to programmatic session/graph/handoff entrypoints in preparation for future MCP adapters. Only the **explicitly selected checkout** is permitted as a source or destination of Spec2Code file operations. When the skill is installed at `.agents/skills/spec-to-code/`, its `path_guard.py` is additionally **bound to that same checkout**: it cannot target another valid Git repository. Git worktrees are supported; their `.git` administrative pointer may legitimately reference external Git metadata, but Spec2Code does not read/write application files through that pointer.

## Allowed / blocked

| Request | Outcome | Reason |
| --- | --- | --- |
| `--root .` while the current directory is the Git root | ALLOW | Exact working tree root |
| `--root /path/to/checkout` | ALLOW | Canonical exact Git root; must match installed skill checkout when installed |
| Installed skill directed to another valid Git checkout | BLOCK | Installed-skill checkout binding |
| `--root src/` or `--root repo/subdir` | BLOCK | Repository subdirectory is not the Git root |
| `--root /tmp/non-repo` | BLOCK | Not a Git worktree |
| `--root /tmp/alias` where alias is a symlink | BLOCK | Root aliasing/symlink escape |
| Path `../other-repo/file.py`, `C:\\outside`, or UNC path | BLOCK | Traversal, drive, or foreign path |
| Repo-relative path under symlinked `.agents/state`, `.agents/.handoffs`, or `s2c/` generated layer | BLOCK | Read/write may escape checkout |
| Nested Git repository/submodule encountered during source scanning | SKIP | Has its own repository ownership |
| `GIT_DIR`/`GIT_WORK_TREE`/other injected Git variables | IGNORE | Cannot redirect Git validation/attribution |

Invalid paths return a nonzero status and `PATH_GUARD_BLOCKED` with a short reason. **No fallback** to the parent directory, another repository, or the host user's home directory occurs.

## Rules for extensions and MCP

- Call `path_guard.validate_root(root)` **before any state read, external invocation, or write**; never default to a guessed parent directory when validation fails.
- For every user-provided path, generated path, or path loaded from cached JSON, call `path_guard.check_path(root, path)` before opening or publishing it.
- Do not use arbitrary shell tools, remote Git fetch, or repo mutation as a substitute for a failed guard.
- Keep `specs/` and `.specify/` under Spec Kit's ownership. `speckit_bridge` reads them only after both workspace and feature-path validation.
- Source paths must stay repository-relative in the API and context pack; absolute paths are reserved for internal checked filesystem operations.
- Make no changes in an invalid checkout, including `status`, `merge`, `scan`, `bridge`, and `context_router` operations.
- A valid Git checkout is an **execution boundary**, not proof that the user approved code changes or commits.

## Threat-model limits

This is a fail-closed **path containment and repository-targeting guard**, not a kernel filesystem sandbox. It cannot reliably prevent time-of-check/time-of-use races when a separate malicious process concurrently changes directory entries in a writable checkout. Use OS/container permissions or a mount namespace to enforce containment against an untrusted local filesystem adversary. It does not monitor commits in GitHub until an authorized remote fetch has occurred.

## Regression tests

```sh
python -m unittest discover -s tests -p 'test_path_guard.py' -v
python -m unittest discover -s tests -v
```

Tests cover all CLI entrypoints on non-Git roots, nested roots, root/sensitive path symlinks, `..`, Windows drives and UNC paths, injected Git environment, untrusted cache document paths, nested Git checkouts, and legitimate `git worktree` behavior.

## Continuous enforcement (v0.6.3)

See [CONTINUOUS_SCOPE_ENFORCEMENT.md](CONTINUOUS_SCOPE_ENFORCEMENT.md) for checkout/session identity, directory-relative IO, HEAD invalidation, and the MCP fixed-workspace gate. This is event-boundary checking, **not** an always-on watcher.

## Windows path alias correction (v0.7.0)

Windows 8.3 short-name paths and different casing can refer to the same physical Git worktree without being filesystem links. Root verification now detects actual symlink/junction ancestors, while comparing canonical resolved roots when validating the Git worktree and installed skill ownership. Session scope stores a normalized physical root path to avoid false drift between path spellings.

The containment boundary **still blocks** linked/junction ancestors and any path resolving outside the checkout. POSIX anchored file operations and Windows fallback have different TOCTOU guarantees; passing Windows CI does not establish race-free file writes or permission to operate on untrusted paths. Migration of previously persisted session bindings is not automatic.

## PLAN-107 / S01 — Physical path containment acceptance

The trust root is the **operator-approved resolved checkout**, not a string supplied by a model or MCP client. A future write-capable host must resolve and compare paths against this root, including case-folded Windows volumes, drive-relative paths, alternate separators, UNC/network aliases, junctions, symlinks and indirect helper working directories. Apply the policy at the time of each operation; a single prompt preflight is not enforcement.

Required negative fixtures: an outside-root read sentinel, outside-root write sentinel, symlink/junction to each, traversal and renamed path after validation, and a delegated subprocess with an untrusted cwd. Record sentinel hashes before/after, exact executable OS and denial reason. The *planned* result is zero unauthorized reads/writes; an error message alone is insufficient if the sentinel changed. Existing Python tests do not certify OS-level sandbox escape resistance; these fixtures remain `NOT_RUN` until authorized host execution.


## PLAN-111 — Windows reparse preflight hardening, not race acceptance

The new `path_guard._windows_reparse` uses Win32 `GetFileAttributesW` and `FILE_ATTRIBUTE_REPARSE_POINT` to refuse additional reparse types, including cloud placeholders, even where Python's `Path.is_junction` is absent or returns false. Attribute lookup is repeated at path-check boundaries and denies unknown Windows query errors. It does **not** make the existing non-anchored Windows `scope_io` write/read/delete fallback race-safe against a hostile concurrent directory swap. On untrusted or shared Windows worktrees, keep write-capable automation disabled until the owner provides OS-enforced isolation or a security-reviewed handle-anchored implementation and actual negative sentinel evidence. The Windows CI case mocks a reparse marker and does not prove TOCTOU resistance. See [PLAN-111 current risk disposition](../.agents/.riskMatrix.md#plan-111--p0-treatment-evidence-and-return-to-a-risk-decision).
