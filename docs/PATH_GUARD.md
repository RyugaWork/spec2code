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
