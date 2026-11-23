# Spec2Code — Technology & Architecture Assessment (all stacks)

> Use for **S2C development code** or **any integrated host repository** during A/P3–P6. Not a grant to modify either repo. An explicit user selection can replace a conservative default under the [override protocol](technologyVersionPolicy.md#4-user-override--explicit-user-preference-takes-precedence-over-conservative-defaults).

- Assessment ID: `TECH-<unique>`
- Scope: `S2C_SOURCE` / `HOST_REPOSITORY` / `BOTH`; exact repository/branch/ref:
- New project / existing project / legacy migration:
- Tech category: Python interpreter/package | PowerShell runtime/module | SQL database engine/driver/dialect/migration | .NET | Other:
- Exact technology product and **major/minor/edition/dialect**:
- Project structure and owner (existing / proposed):
- Explicit user preference or default candidate: `DEFAULT` / `USER_OVERRIDE`:
- Linked override `OVR-ID` (if any):
- Official vendor support/release URL + checked date and evidence:
- GA release, servicing history, latest supported security patch, EOL or maintenance horizon:
- Evidence of production-relevant adoption/tooling and source dates:
- Dependency matrix: compiler/interpreter/PS edition, SQL engine+driver, OS, CI, containers and deployment:
- Official/common structure references, alternatives and complexity justification:
- Security, migration/backups, compatibility, rollback and version pin/update strategy:
- Scope and impact: actual S2C code/config/tests or host paths **to be proposed, not edited**:
- Existing baseline to preserve and migration/rollout costs:
- Risk IDs, L×I, potential residual and responsible owner:
- Requirement/AC/RTM and plan IDs:
- Proposal status: `PROPOSED` / `RECOMMENDED_FOR_REVIEW` / `NEEDS_REVIEW` / `BLOCKED`:
- User owner instruction source and real review decision, if any:
- A.1 evidence/result: `NOT_RUN` or observed report ID:
- B.1 evidence/result: `NOT_RUN` or observed report ID:
- Handoff and provenance:
 
## Candidate comparison

| Candidate/structure | Current support & patch | Adoption/maturity evidence | Target compatibility | Risk and migration | Requested by user? | Review state |
| --- | --- | --- | --- | --- | --- | --- |
| <actual engine/runtime version> | <vendor/date> | <dated evidence> | <real target> | <impact> | DEFAULT / OVR-ID | PROPOSED / BLOCKED |

Rules: Do not hardcode a single default for every stack; `SQL` must name an engine and dialect. Support and adoption evidence must be current. New security patch ≠ new major. Popular old EOL ≠ secure. A user-requested stable newly GA version may bypass the **default maturity preference** with a documented override, not safety permissions or independent host review.

## PLAN-110 / Z08 — Reproducible technology assessment

For each candidate maintain a comparable decision row: `candidate/version, maintainerURL, checkedDate, supportEndDateIfKnown, hostCompatibility, dependencyMatrix, languageStyleAuthority, securityPatchAvailability, migrationCost, rollbackPlan, requiredTests, ownerDecision, evidenceRef`. Rank **only candidates that satisfy mandatory security and compatibility conditions**. Unknown support lifetime or unverified native installation is `NEEDS_RESEARCH`, not a numeric zero or an approved choice.

The reviewer should document why the recommended conservative baseline is preferable to a newer stable or host-requested override and which tests could falsify the decision. A requested override requires a real OVR-ID/owner record; this blank assessment does not authorize altering build files, package lock, SQL schema or CI on the host.
