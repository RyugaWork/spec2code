# Spec2Code — Technology & Architecture Approval Assessment

> Use during A/P3 research and A/P5–P6 design. **Blank form; NOT approved.** Never fill PASS/APPROVED without verifiable source and actual external reviewer.

- Assessment ID: `TECH-<unique>`
- Task / approved host scope:
- Technology, type (runtime/framework/library/build tooling), proposed **major/minor**:
- Project structure / architecture proposal:
- Current host baseline and whether NEW project or EXISTING/LEGACY:
- Date checked, official vendor support URL and source version:
- GA/stable release date / elapsed maturity:
- Current support phase, support end date, expected go-live + required maintenance window:
- Servicing/security patch policy and proposed supported patch:
- Adoption evidence source 1 (official ecosystem/tooling or representative production):
- Adoption evidence source 2 (independent, maintained ecosystem integration/usage):
- Dependency/SDK/IDE/CI/container/OS compatibility and known breaking changes:
- Vendor-recommended or widely used structure evidence, and reason this structure fits:
- Alternatives, including older supported LTS and their security status:
- New major/preview/EOL/novel structure vetoes? YES/NO and factual reason:
- Security/operational risk IDs, L×I priority and design mitigation:
- Requirement/AC/feature/RTM links:
- Exception requested? scope, owner, compensating controls, expiry and migration path:
- Agent recommendation: `PROPOSED` / `RECOMMENDED_FOR_REVIEW` / `BLOCKED` / `NEEDS_REVIEW`:
- Owner decision: `NOT_REVIEWED` / `APPROVED_BY_OWNER` (actual decision source and exact version only):
- A.1: `NOT_RUN` / real criterion result and report ID:
- B.1: `NOT_RUN` / real observed runtime validation and report ID:
- Handoff path/ref / `NOT_PERSISTED`:

## Comparison (evidence-based)

| Candidate major/structure | Vendor support current? | Mature since GA? | Adoption evidence | Compatible? | Security/operations | Status/rationale |
| --- | --- | --- | --- | --- | --- | --- |
| <version> | <source/date> | <date> | <2 evidence classes> | <evidence> | <risk> | PROPOSED/NEEDS_REVIEW/BLOCKED |

Remember: **newest ≠ approved**, **popular ≠ supported**, **fresh security patch ≠ new immature major**. Record .NET 8 after EOL only as a legacy exception, not a new-project recommendation; .NET 10 LTS is the conservative 2026-11 candidate; .NET 11 is too newly released for default adoption under this policy.
