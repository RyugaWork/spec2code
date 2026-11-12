# Spec2Code change workflow v0.7.0

1. **Requirement:** update `../.spec.md` as required and set the feature's status in `../.features.md`.
2. **Plan first:** record scope, owner, changed files, rollback, acceptance tests in `../.plans.md`.
3. **Threat model:** classify security/data/cross-OS effects in `../.risk.md`; block unsafe writes.
4. **Session:** start/restore an exact Git checkout session via the installed skill's `session_guard.py`; never treat a source-repository document as host-local runtime session.
5. **Code:** implement only approved changes and keep code/config in `../../.source/`.
6. **Tests:** execute `python -m unittest discover -s .source/tests -v`, plus platform and installation checks; update `../.checklist.md` with evidence.
7. **Handoff:** add a dated file in `../.handoffs/` summarizing feature IDs, commits, changed files, tests, risks, rollback and pending work.
8. **Review/merge:** no force push. Merge only after explicit review and required CI results; update changelog and statuses.

All test claims must distinguish PASS, FAIL, SKIPPED, BLOCKED and NOT RUN.
