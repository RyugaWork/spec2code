# PLAN-097 — Native upstream environment boundary source audit handoff

> 2026-11-13 Asia/Ho_Chi_Minh. **Source before this grouped commit:** `da7531bb029dbd3bad05bdd6a8d28808ac4b97eb`, existing branch `docs/plan-089-a1-readiness` / Draft PR #10. Creating this commit advances HEAD; re-fetch current SHA before relying on it. No additional branch, runtime code edit, CI or merge.

## Actual verified evidence

- Compared official `github/spec-kit` `v1.2.6` and `v1.4.0` source: `common.py` selects `SPECIFY_FEATURE_DIRECTORY` before pointer file, allows absolute feature directories, and can persist `feature.json` unless `SPECIFY_FEATURE_NO_PERSIST=1`. `setup_plan.py` writes template files under the selected feature directory. The upstream source did **not** import S2C's Path Guard; no real host execution or exploit was demonstrated.
- [Source audit](../.documents/specKitUpstreamEnvAudit097.md) includes upstream line references, two candidate risks (`SK-R10/11`), five new `SK97-NEG-01..05` real-host acceptance designs, and explicitly scoped Linux/Windows operator examples. These examples are **NOT executed**.
- Updated [native pilot](../.documents/specKitNativePilot.md), [native execution gate](../.workflow/specKitNativeExecutionGate.md), [Web workflow](../.workflow/specKitWebWorkflow.md), [feature contract](../../specs/001-s2c-speckit-integration/contracts/web-native-interface.md), [acceptance catalogue](../../specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md), [RTM](../.traceMatrix.md), [risk](../.riskMatrix.md), [plans](../.plans.md), [root AGENTS](../../AGENTS.md), [feature plan](../../specs/001-s2c-speckit-integration/plan.md) and [master SRS](../.spec.md).
- Google stakeholder BRD Draft v1.5 Section 30 PLAN-097 write acknowledged at revision `AHj4eMT7O0eSAtsgZ2Y5o26Z9ybkc7NTFV09Vw9oDwHVJ_NQTwcoRtgiR2IUo58E5QHIQNpXKxvK9crptuqk-Pd1yoVTvIJoPzKgHYABVA`. This is not independent stakeholder approval or a Git SHA.
- **Scope and task counts:** unchanged six documentary tasks T001–T005/T010; original 24 feature cases remain exactly 4 bounded GitHub Web/static PASS, 20 NOT_RUN; PLAN-096 4 negatives + PLAN-097 5 negatives all NOT_RUN. A.1 NOT_RUN, B NOT_AUTHORIZED, B.1 NOT_RUN.

## Safe continuation / decision queue

1. Approve/reject strict native pointer/override environment handling; default recommendation: no inherited overrides for readonly checks, `SPECIFY_FEATURE_NO_PERSIST=1`, validate feature under actual S2C host Path Guard and detect byte-level pointer/drift before/after.
2. Obtain actual independent A.1 with current Git SHA and owner authority. No reviewer was delegated here, and role-lens analysis is not independent.
3. On an authorized network-enabled disposable checkout, choose a security-reviewed official tag, install native CLI, run `SK97-NEG-01..05` with real guard and sentinel paths, gather stdout/stderr/exit/OS/hashes; compare with existing `SK96-NEG-01..04` and seven bridge tests.
4. Only with A.1 and separately approved B scope implement any adapter/interception code; later B.1/release decision remains independent. Do not use `specify init --force` in the active branch and do not enable automatic new feature branches.

**STOP/PERSISTENCE:** docs committed on the existing Git branch and Google write acknowledged; **official native CLI/source host tests still NOT_RUN** because container DNS cannot reach GitHub. No coding-agent native guard hook was deployed. Update this handoff with final exact commit SHA on next resume, do not treat the source inspection as executed safety tests.
