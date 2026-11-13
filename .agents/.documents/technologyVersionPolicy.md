# Spec2Code — Technology, Version & Project Structure Approval Policy

> **PLAN-086 • proposed system/Agent governance • 2026-11-13**. Applies to S2C's design recommendations and approval evidence in **A Planning & Specification / A.1 Validation**, and is a proposed check for later B/B.1. It does **not** auto-modify dependencies or approve host deployments. A product/domain owner still needs to accept an exact design. Root/nested host AGENTS and applicable security policies remain authoritative; the agent must flag conflicts and never treat an obsolete/unpatched major as secure merely because it is popular.

## 1. Objective and default rule

**Agents MUST prioritize widely adopted, actively maintained, compatible, proven structures and versions, not the newest release.**

To mark a technology/version/architecture `RECOMMENDED_FOR_REVIEW`, document all of:

1. **Official lifecycle:** current stable GA, vendor or credible maintainer support with security fixes, a clearly documented end-of-support date (when applicable), no announced imminent EOL during the target deployment/support window. For long-lived systems, prefer a supported **LTS** with at least ~12 months of remaining vendor support at intended go-live (a **design default**, not a universal legal rule).
2. **Maturity:** major platform/runtime/framework versions should generally have **12 months since stable GA**, more than one real maintenance/patch cycle, known migration notes and observed compatibility. For low-blast-radius libraries with clear ecosystem proof, a **6-month** floor can be proposed with risk review; no floor ever overrides missing security support or known critical issues. Age is a **necessary screening signal**, not sufficient proof.
3. **Real adoption:** verifiable usage in maintained applications, mature ecosystem integrations/plugins, actively maintained dependencies and public official/community documentation. **At least two independent evidence classes** (for example, vendor documentation and representative maintained ecosystem tooling/adoption evidence), without fabricating download counts, stars, survey percentages or production deployments.
4. **Architecture convention:** favor a vendor-documented, commonly used repository layout/project organization with clear module boundaries, deployment/testing/migration patterns and onboarding documentation. Adopt the **simplest appropriate proven pattern**, not a novel pattern merely because it is fashionable. A complex pattern (microservices, CQRS/event sourcing, new scaffolding convention) needs scale/operational justification and evidence; do not impose it by default.
5. **Compatibility/operability:** build tools, supported SDK/IDE/CI, target operating systems/container images, libraries, API versions, observability and rollback plan are compatible. Do not mix unsupported new and old framework targets to mask a dependency gap.
6. **Security/maintenance:** version has security patch channel, known vulnerabilities and update strategy assessed. Do not freeze an obsolete patch to avoid newness; use tested/current security **patch** releases within the approved supported major, subject to compatibility checks.
7. **Traceable decision:** technology, version, supported time window, source/ref checked date, alternatives and rejection rationale, AC/RTM/risk IDs, owner/reviewer and explicit status recorded in the [technology assessment template](technologyAssessmentTemplate.md). Never infer approval from recommendations or a successful local build.

An agent may label a choice `PROPOSED`, `RECOMMENDED_FOR_REVIEW`, `NEEDS_REVIEW`, `BLOCKED` or `APPROVED_BY_OWNER` **only with actual reviewer evidence**. The agent cannot self-issue `APPROVED_BY_OWNER` or claim that a technology is broadly used on the basis of release age alone.

## 2. Version selection precedence and veto conditions

1. **Prefer:** established **supported LTS** major with proven target compatibility and vendor-recommended structure.
2. **Allow review:** mature supported non-LTS/STS only if it passes support/maturity/adoption/compatibility requirements and a specific business reason justifies it; LTS remains normal default.
3. **BLOCK by default:** fresh major, preview, alpha, beta, release candidate, nightly, unsupported/EOL major, experimental architecture, plugin without maintenance, or stack with unknown security/operational support. New vendor releases and official project templates are **not automatically approved**.
4. **Special case — security patch:** newly released security/servicing **patch** for an otherwise approved supported major is **not the same as a fresh major**. Prefer promptly applying vendor patches after a bounded regression/compatibility check; don't delay critical fixes solely to meet an age threshold.
5. **Legacy systems:** a deployed project can have an unsupported historical major **identified as existing state**, never upgraded to a new-project recommendation. Retaining it needs documented business/security owner exception, compensating controls, supported isolation where available, target upgrade version/date and migration tests. If risk is unacceptable, mark `BLOCKED`. No indefinite exception.
6. **New-major exception:** if no supported mature alternative exists and a new major is genuinely required, only a named external architecture/security owner may approve an **exception after evidence**, with reproducible compatibility/security tests, rollback, version pin and risk expiry. Never 'approve' by changing this file or by agent assertion alone.

**Design gate:** if support dates, maturity evidence, current compatibility, adoption or owner decision are unknown, report `NEEDS_REVIEW` rather than selecting the newest or silently falling back to an insecure EOL release.

## 3. Worked example — .NET on 2026-11-13

| Version | Official status on 2026-11-13 | S2C design default | Rationale and condition |
| --- | --- | --- | --- |
| **.NET 10** | **LTS, actively supported** (released 2025-11-11; support through 2028-11-14) | **PREFERRED for new .NET projects**, subject to actual host needs | >12 months from GA, mature servicing channel and compatible mainstream ecosystem should still be verified; use an up-to-date .NET 10 patch rather than pinning a stale one |
| **.NET 8** | **LTS historically, now EOL** (support ended 2026-11-10) | **NOT approved for new production projects**; only existing legacy support under an explicit reviewed exception | Popularity does not restore security patches. Record upgrade path to .NET 10, risk owner and migration deadline; don't recommend as secure default |
| **.NET 11** | **STS**, newly GA 2026-11-10 (only ~3 days old) | **NOT APPROVED as a default recommendation** | Supported by Microsoft but fails S2C's conservative major-version maturity policy; do not use merely because it is newest |

Sources checked 2026-11-13:
- [Official .NET support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core), updated 2026-11-10.
- [Microsoft .NET 8/9 end-of-support announcement](https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support/), published 2026-06-29.
- [Microsoft .NET 11 announcement](https://devblogs.microsoft.com/dotnet/announcing-dotnet-11/), published 2026-11-10.

The dates above are **time-bound research**, not eternal hardcoded rules. Recheck official lifecycle/patch information at every new technology decision or A.1 review. **.NET 10** is a representative safe-major candidate, not a requirement to use .NET for all hosts. Do not retarget an existing project from .NET 8/11 to .NET 10 without authorization and migration planning.

## 4. Proven project structure (separate approval from version)

A structure proposal must cite the **actual hosting language/framework**, vendor-recommended defaults and representative maintained project examples. Separate **required architectural constraints** from arbitrary folder aesthetics. Assess clear ownership, modularity, test discoverability, dependency direction, configuration/secrets outside source, portability, upgrade strategy and whether a new contributor can follow it.

For .NET, mainstream ASP.NET Core / SDK-style projects, conventional solution/project organization and standard DI/test infrastructure are **candidates**; a particular Clean Architecture layering, CQRS scheme or microservice split is **not mandatory** without project-specific requirements and evidence. For another stack (Python, Java, Node, etc.), apply the same criteria rather than copying a .NET solution layout.

**Reject** novelty-driven changes: adopting a newly introduced project template or build tool without support/adoption proof, adding abstraction layers with no requirement, using internal/unofficial SDK APIs or changing an existing host's approved architecture solely to use new features.

## 5. Integration with A → A.1 → B → B.1

- **A/P3 Research:** collect `TECH-ID`, candidate version/structure, official release/support link, GA date, current patch policy, ecosystem evidence and a comparison of alternatives. Record unknowns and possible host constraints; don't invent popularity statistics.
- **A/P5–P6 Design:** apply the seven checks, select a mature supported baseline and mainstream structure; document rejected fresh versions, EOL conflicts, migration paths and approval owner. Link requirements/ACs and risk entries.
- **A/P7–P8 Risk:** explicitly score newest-version churn, EOL security, immature architecture and stale evidence; design mitigation for the highest unresolved risk. A mitigation document does not prove the risk is fixed.
- **A.1 Validation:** require a completed evidence assessment and independent review under `A1-VAL-05` (architecture compatibility), `A1-VAL-01` (authority), `A1-VAL-07` (risk). If a selected major is unsupported or fresh without an approved exception, `FAIL/BLOCKED` and return to A.
- **B Implementation:** only after separate approval; pin or bound the permitted major and review current secure servicing patches. Avoid unrequested upgrades when coding.
- **B.1 Validation:** under `B1-VAL-01` and `B1-VAL-03/04/06`, verify the **actual** effective SDK/runtime/container/library versions, support status, representative tests and architecture contract against A.1-approved decisions. Unexpected major-version drift `BLOCKED` pending redesign/review.
- **Handoff:** record approval state, official lifecycle checked date, exception scope/expiry, remaining upgrade path, actual chosen major and `NOT_RUN` checks.

No runtime enforcement is added by this policy; `policy_resolver.py` and `workflow_guard.py` do **not** automatically check adoption/maturity. This document is a **human-directed agent gate** until separate code tests and implementation are approved.

## 6. Acceptance and traceability

- `S2C-NFR-008` / `S2C-NAC-008`: every **new recommended** framework/runtime major and project structure must demonstrate current support, maturity, adoption, compatibility and explicit owner approval; fresh new majors and EOL versions are blocked by default, with narrow evidence-based exception governance. Cross-references: F32/F34/F36 (agent governance and independent approval), [RTM](../.traceMatrix.md), [Risk Matrix](../.riskMatrix.md), R67–R70.
- Related validation checks: `A1-VAL-01/05/07`, `B1-VAL-01/03/04/06`. No executed policy acceptance test exists merely because a Markdown criterion was defined.
