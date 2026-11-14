# Agent governance configuration

This directory holds **development-governance metadata**, not the Spec2Code runtime policy. Runtime configurations live in `.source/.config/*.json` and must remain adjacent to the packaged `.source/scripts/` directory.

Never store credentials or local machine/session state here. Any future machine-readable governance config must have strict schema validation and no permission to weaken Path Guard or grant execution rights.

## PLAN-107 / S06 — Future governance configuration schema

If machine-readable governance configuration is introduced during an approved B phase, it must be versioned, scoped to the current repository, validated against a closed schema and **unable to authorize itself**. Candidate declarative fields: `policySchemaVersion, repositoryId, proposedAllowedPaths, proposedDeniedPaths, maxTasks, maxRetries, maxDuration, tokenBudget, reviewerProfileIds`. Require an external trusted approval token/reference for actual execution; never store credentials, host absolute secrets or write-capable tokens in this directory.

Reject unknown security-sensitive keys, negative/zero budgets that might disable limits, symlink aliases that resolve outside the root, and mismatched repository/session IDs. Current docs do not deploy that schema or instruct agents to manufacture config values; no config files are changed in this batch.
