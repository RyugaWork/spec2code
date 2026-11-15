# PLAN-112 security continuation

Baseline `3227fa51eca5a41634ae563ffa7af539d33ee851`, verified against GitHub and a clean detached copy. Scope is targeted A.1 remediation. Prior PLAN-111/112 handoffs and both Codex summaries remain historical evidence.

| Task | Baseline file/line | CWE | Expected | Observed before edits | Risk |
| --- | --- | --- | --- | --- | --- |
| T112-05/06/07 | .source/scripts/scope_io.py:19–37; .source/scripts/workflow_guard.py:360–378 | 367, 59 | Unsupported hosts deny managed I/O; hostile cases require an independently protected evaluator | Scope IO checks anchors, but the workflow lock uses raw path-based creation; Windows isolation and ACL are unverified | RM-001 P0 |
| A1-SEC-08 | .source/scripts/workflow_guard.py:129–175 | 200 | Sensitive config contributes metadata only; excluded names contribute no file observation | Union of scope and routed paths reads and hashes every regular file | RM-003/032 |
| A1-SEC-09 | .source/scripts/workflow_guard.py:179–285, 360–401 | 345, 732 | Validate replay and protected state; reject rewriting or truncation relative to the cached head | Public digest chain and replay accept some recomputed changes; cache mismatch is treated as repairable | RM-004/006/032 |
| A1-SEC-10 | .source/scripts/architecture_tree.py:420–433 | 703 | Bounded recovery after an interrupted initial publish or update | Initial retry tested; only first document stages outside the output tree, and later interruption can leave temp files visible | RM-005/032 |
| A1-SEC-11 | .github/workflows/tests.yml:1–27 | — | Separate pinned static checks and per-rule triage | Unit CI only; prior Ruff/Bandit counts were observations on an earlier revision | RM-032 |

Concurrency control uses a separate detached clone and a fast-forward push to the existing branch. Rollback is a reviewed revert of scoped commits. Hostile Windows tests require proven isolation, separate ACLs and synthetic canaries. No protected host targets are used. Review count is zero.

## Disposition and handoff

| Task | Local disposition | Remaining |
| --- | --- | --- |
| T112-05 | BLOCKED_HOST. Windows build 10.0.26200.0. WindowsSandbox.exe was absent from command discovery. No isolated Windows evaluator identity, ACL segregation or outside-root canary controls were independently demonstrated. | Security Owner supplies an isolated disposable Windows guest and verifies evaluator/test-process permissions before hostile execution. |
| T112-06 | NOT_RUN | Execute bounded interleavings, junction/reparse, outside-root read/write and concurrent cases only after T112-05. Canary ledger and hostile-host verdict are absent. |
| T112-07 | PARTIAL. Reviewed the baseline Scope IO deny path and routed the Workflow Guard lock through anchored directory locking. | RM-001 OPEN, score 20, residual UNKNOWN. Windows support decision requires hostile-host evidence. |
| A1-SEC-08 | DONE for the scoped source and regression | Sensitive config size and mtime are evidence. Identical metadata can hide a content change. |
| A1-SEC-09 | PARTIAL. Private POSIX state, atomically replaced bounded journal, validated replay and cache anchor, with explicit one-event recovery. | Independent append authenticity and isolation against a same-UID writer remain open. The local checkpoint cannot disambiguate a plausible forged extension from an interrupted cache write. |
| A1-SEC-10 | DONE for retry recovery | Readers can observe mixed generations during interruption. Retry the same inputs once after resolving the failing condition, or preserve the partial output for owner inspection. Staging requires the state and output destinations on the same filesystem. |
| A1-SEC-11 | DONE for selective CI and reproducible triage, partial against historical Ruff count | Obtain the historical Ruff configuration and raw report for item-level reconciliation. Observe Actions independently of local analyzer results. |
| T112-08/09 | BLOCKED_OWNER / NOT_RUN | Security Owner reviews host evidence. Independent reviewer then evaluates A1-VAL-01..09 against the final Git/Google source pair once the owner gates are met. |

A.1 disposition is NO-GO with RM-001 open. Reviewer count is zero and A1-VAL-01..09 are NOT_RUN. General Phase B and delivery are outside this authorization. No changes in the OneDrive checkout were needed. Rollback by reviewed reversion of the scoped source and evidence commits. Preserve the prior PLAN-111/112 handoffs and existing user state.

## Static analysis

Commands below ran on Windows build 10.0.26200.0 with Python 3.12.14. Baseline source was extracted from Git without user state. Candidate source SHA is `9a49f6bf361f83864f341fe7dbf4bb32d04b418b`.

- Ruff 0.11.13, `ruff check --no-cache --statistics .source/scripts .source/tests` baseline and `python -m ruff check --no-cache --statistics .source/scripts .source/tests` candidate, each exit 1 and 67 diagnostics. E701 (4), E702 (21), E402 (19), E731 (7), E741 (8) and F401 (8) are layout/import/readability findings. Script-only default yielded 21 at baseline. Adding `--select E,F` on scripts and tests yielded 628, with 561 from E501. The historical 151 cannot be reproduced from the available command/config evidence. No style churn was applied.
- Ruff baseline `ruff check --no-cache --select S --statistics .source/scripts` yielded S603 (5) and S607 (4), exit 1. Candidate `python -m ruff check --no-cache --select S --ignore S603,S607 .source/scripts` yielded zero, exit 0. The separate CI job uses this selection and a five-minute limit. S603/S607 are outside the CI gate and remain review items.
- Bandit 1.8.3, `python -m bandit -q -r .source/scripts -f json -o <report>`, exit 1 on both revisions, each with 12 low findings. B404 imports (3) are in path_guard.py, scan_infrastructure.py and session_guard.py. B603 fixed/list-argument subprocess calls (5) occur at baseline path_guard.py:118/140, scan_infrastructure.py:162/457 and session_guard.py:48. B607 flags four Git lookups at those lines except the opt-in version probe at scan_infrastructure.py:457. The calls do not request shell execution. Executable resolution still trusts the process search path for Git, and the opt-in version probe relies on the host's executable lookup as well. No severity upgrade was reproduced in this scoped review.

These scanners do not establish Windows containment, private-state authenticity or independent approval.


## Dynamic regression evidence

Source and tests at `9a49f6bf361f83864f341fe7dbf4bb32d04b418b`. Both suites used existing temporary repositories with synthetic inputs. The added cases configure a synthetic application settings file, alter or truncate a fixture journal, exercise private filesystem modes and hard links, inject an interrupted cache write, and fault architecture publication before committing new state.

| Environment | Command from exact checkout | Exit | Observed |
| --- | --- | ---: | --- |
| Ubuntu on WSL2, Linux 6.18.58.1, Python 3.14.4 | `timeout 180s python3 -B -m unittest discover -s .source/tests -v` | 0 | 146 collected, 141 passed, 5 platform skips, 82.439s. New security cases and both publisher-recovery cases passed. |
| Native Windows build 10.0.26200.0, bundled Python 3.12.14 | `python.exe -B -m unittest discover -s .source/tests -v` | 0 | 146 collected, 43 passed, 103 platform skips, 45.833s. Both explicit unanchored-I/O and session-start denial tests passed. |

Windows run was ordinary regression coverage. Hostile isolation/ACL/canary evidence and independent approval remain NOT_RUN. The source commit and this documentation evidence may have distinct SHAs. GitHub CI should be evaluated at the published branch HEAD.
