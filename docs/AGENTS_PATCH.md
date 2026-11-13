# Optional target AGENTS.md guidance (review before adding)

This is **a suggested fragment**, not permission to override host repository policies.

> For implementation tasks, start or checkpoint a Spec2Code coding session before reading feature source. Use the local scanner and context router under `.agents/skills/spec-to-code/scripts/` to route only relevant source and generated architecture docs. A target repo may have `src/`, `app/`, `backend/`, `web/`, `.source/`, or any other declared structure; use only observed paths. Where the official GitHub Spec Kit is installed, resolve the current feature using `.specify/feature.json` / `SPECIFY_FEATURE_DIRECTORY` and validate `spec.md`, `plan.md`, `tasks.md` before implementation. Route with `--speckit-stage implement`. Spec2Code does not edit Spec Kit artifacts except through separately authorized work recorded by the active session. Preserve outside-session changes in `visualChange`, explicitly authored changes in `specChange`, and merge only exact verified finished Session IDs. Never bypass the host repository's requirements, security review, authorization rules, or Git approval gates to save tokens.

## PLAN-080 host governance guidance

Optionally describe canonical business/API/security sources and required review authorities in host-owned AGENTS. S2C only locates applicable documents, reports missing/conflicting policy and routes pointers into context; it never overwrites or auto-approves a host requirement.
