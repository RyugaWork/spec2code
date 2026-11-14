# PLAN-103 — BR-to-test traceability review checkpoint

2026-11-14 Asia/Ho_Chi_Minh. Repository `RyugaWork/spec2code`; existing branch `docs/plan-089-a1-readiness`. **Input Git SHA:** `df95edf040fa417f0af47ebb5776e0db5a1c5daa`; **output SHA:** committing revision containing this handoff, to be retrieved from branch HEAD. Parent [PLAN-103 final authoring handoff](plan-103-documentation-final-handoff.md).

## Evidence-based issue and correction

The master feature group BR-022..027 and existing `F43..F64` scenario table had mutually consistent memberships (6 of 6 BR groups and 22 of 22 features), but RTM Section P still said `NOT_MAPPED_TO_TEST` and the planned `TC-Fxxx-P/N` naming was only implied. Author-side preflight compared all 22 feature rows with all six BR-group feature lists (zero membership conflicts), then explicitly inserted **44 unique candidate case IDs** in the two existing positive/negative columns for `F43..F64`. RTM Section P now enumerates the exact candidate case IDs per BR and says `DESIGN_CASES_LINKED / NOT_RUN / OWNER_APPROVAL_PENDING` instead of the stale no-mapping status. No new requirements or test scenarios were invented, and the 44 planned cases remain unexecuted.

**Changed scope:** `.agents/.workflow/testingAndDelivery.md`, `.agents/.traceMatrix.md`, this checkpoint Markdown. No S2C runtime, Python, CI/config, Google BRD, native Spec Kit, Git branch or PR changes. No local working-tree status/Path Guard or Codex/Gemini host check was performed through this GitHub documentation connector.

## Remaining and resume

This is structural design traceability only. Individual approved BR-specific AC thresholds, fixtures and owner decisions remain pending. `A1_NOT_RUN`, `B_NOT_AUTHORIZED`, `B1_NOT_RUN`, open P0 risks and unchecked Spec Kit T011/T012/T015 remain unchanged. Resume by fetching exact output SHA, verifying the 44 unique new IDs, matching six BR groups and inspecting full Markdown links/anchors, then independently reconcile exact Git and Google BRD revisions. A model's document review is **not** an independent A.1 signature. On stale branch, STOP, preserve this handoff and do not force-update.
