# Spec2Code — Cross-Technology Version, Structure & User Override Policy

> PLAN-086 • **draft agent-governance specification**, 2026-11-13. Applies equally to **the Spec2Code development codebase** (`.source/scripts/`, `.source/tests/`, `.source/.config/`, tooling and CI) and **every integrated host repository** using the portable S2C skill. Only recommendations/approval design is currently in scope; this document does not execute changes or create a runtime version validator. Host-owned approved AGENTS/security rules cannot be silently replaced.

## 1. Universal default: mature, common, supported, compatible

When the user has **not** specified a version or architecture, the agent MUST choose a **well-adopted, stable, actively supported** baseline and a conventional structure appropriate for that stack, **not simply the newest release**.

This applies to all technology classes, not only .NET: Python and packages/build/test tools; PowerShell and PowerShell modules/scripts; SQL **database engines, server versions, dialects, drivers, ORM and migration tools**; .NET/C#, Java, JavaScript/Node, Go, Rust, containers, IDEs, CI actions and other frameworks/dependencies. `SQL` is a language family, **not a single versioned runtime**: identify PostgreSQL, SQL Server, MySQL, SQLite, etc., their own support policies, actual engine/dialect/version and extension/driver compatibility.

For each new or changed **major/runtime/architecture decision**, record:

1. **Vendor support and maintenance:** stable official release or maintained project; credible security fixes; support/EOL dates when provided, expected project lifespan, update mechanism. Prefer a supported LTS when suitable, but not all products offer LTS. An unsupported popular version is **not** a safe new-project default.
2. **Maturity:** a history of stable servicing, published migration/breaking changes and real ecosystem testing. Prefer a major with roughly a year of production use when available; **age is a flexible risk indicator**, not an automatic ban on all younger releases. Newly GA majors are excluded from the **default** pending evidence or explicit user override. A freshly shipped **security patch** in an approved supported series does not count as an unproven major.
3. **Community / mainstream adoption:** maintained production-relevant ecosystem integrations, vendor docs, common developer tooling and representative usage; verify with independent sources when feasible. Do not invent download numbers, percentage market share or alleged production users.
4. **Structure / maintainability:** documented common folder/module layout, discoverable tests, clear responsibilities, security/secrets ownership, dependency management and manageable onboarding. The **host's already approved architecture is the starting point**; don't restructure it to mimic a new framework template without a separate request.
5. **Compatibility:** existing dependency locks, runtime target, interpreter/PowerShell edition, database dialect, OS, CI, deployed image, build tools and supported deployment requirements. Check any breaking changes and upgrade path.
6. **Security/operations:** known vulnerabilities, patched build, authentication and data handling, rollback, backups, schema migrations and permissions relevant to the stack.
7. **Evidence and decision:** identify exact source/date, candidate and alternative, [technology assessment](technologyAssessmentTemplate.md), `S2C-NFR-008`, risk IDs, reviewer and scope. The agent proposes, while the requester/authorized owner decides within their authority.

**Default outcome:** `RECOMMENDED_FOR_REVIEW`, not `APPROVED_BY_OWNER`. Missing key evidence → `NEEDS_REVIEW`. Unsupported or unreconciled high-risk dependencies → `BLOCKED` for unapproved deployment.

## 2. Scope: S2C source and integrated repositories

| Scope | What is governed | Default behavior and ownership |
| --- | --- | --- |
| **S2C development** | Python interpreter compatibility, stdlib/third-party dependencies, PowerShell helper scripts, database/test tooling if used, CI images/actions, architecture of `.source/`, `.agents/` | Preserve current supported baselines and tested compatibility. A proposed upgrade/structure change requires PLAN/RTM/risk/approval. CI **testing** on a new interpreter is not the same as selecting that interpreter as the deployment minimum. Do not force downgrade/retarget existing Python tests by rule alone |
| **Integrated host repository** | Actual host code, frameworks, PowerShell scripts, SQL engines/migrations, dependencies, containers/CI and module/folder layout | Inspect host `AGENTS.md`, dependency manifests/locks, database/infra versions and contracts first. Avoid changing existing baselines unless requested or needed to meet safety/compatibility requirements, with approval |
| **Shared portable skill** | `.source/SKILL.md` -> installed `.agents/skills/spec-to-code/SKILL.md` | Includes a self-contained summary of this policy. The development repo's `.agents/` files are **not automatically installed into a host**; do not falsely promise that the host has them |

The policy governs **recommendations and future authorized edits** in either scope. In the present A design phase, it is documentation; no Python, SQL, PowerShell, dependency or target-host edits are authorized by writing this policy.

## 3. Stack-specific review questions (no global hardcoded version list)

| Technology | Version choice requires checking | Prefer established structure |
| --- | --- | --- |
| **Python** | CPython official support/security-fix lifecycle, interpreter/platform, pinned library `Requires-Python`, wheel availability, dependency/pytest/lint support; application vs library compatibility requirements | `pyproject.toml`, conventional `src/` layout where suitable or existing proven package layout, isolated tests and virtual env; avoid speculative packaging rewrites |
| **PowerShell** | Microsoft PowerShell 7 lifecycle and LTS when available, `pwsh` vs Windows PowerShell 5.1 edition, OS compatibility, dependency modules, execution policies, supported .NET runtime | Standard `.psm1`/`.psd1` module convention for modules, clear `scripts/` and Pester tests when applicable; preserve existing host conventions |
| **SQL/database** | **Exact engine** and edition (PostgreSQL, SQL Server, MySQL, SQLite...), vendor-supported server versions, driver/ORM, extensions, dialect compatibility, migrations, rollback/backup and production hosting support | Vendor-recommended schema and versioned migrations, consistent naming and environment-independent configuration; don't introduce experimental SQL syntax or engine-specific constructs without declaring them |
| **.NET/C#** | Microsoft SDK/runtime/ASP.NET/EF support phase, installed tooling, existing target frameworks and build/test compatibility | SDK-style projects and common ASP.NET Core layout where appropriate; Clean Architecture, CQRS or microservices only for explicit project needs |
| **Other stacks** | Official stable/support policies, ecosystem adoption, OS/toolchain/lockfile/deployment and versioned migration plan | Vendor-supported or widely adopted minimal structure instead of novelty-driven architecture |

**No global static Python/PowerShell/SQL version recommendation:** support and deployment compatibility change, sometimes quickly; inspect the official vendor lifecycle at the time of **each** concrete proposal. Version choice is **per technology/engine**, not a hardcoded table in Python modules or a universal .config version number.

Current official source entrypoints:
- [Python developer status-of-versions](https://devguide.python.org/versions/)
- [PowerShell support lifecycle](https://learn.microsoft.com/en-us/powershell/scripting/install/powershell-support-lifecycle)
- [PostgreSQL versioning/support](https://www.postgresql.org/support/versioning/)
- [Microsoft SQL Server lifecycle](https://learn.microsoft.com/en-us/lifecycle/products/?products=sql-server) (select actual product/edition)
- [MySQL release model](https://dev.mysql.com/doc/refman/en/mysql-releases.html)
- [SQLite releases](https://sqlite.org/changes.html)
- [Microsoft .NET support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core)

These are **research pointers**, not blanket evidence that a specific host version is approved. Recheck source and target environment before choosing.

## 4. User Override — explicit user preference takes precedence over conservative defaults

**Override is a requested choice, not an automatic privilege escalation.** When the user explicitly asks for a particular technology version, tool, layout or experimental stack, the agent MUST respect that preference as the target **if it is within the user's authority and can be handled safely**. Do **not** silently substitute a mature default. Instead:

1. Detect a **clear explicit request** (`use Python X`, `use .NET 11`, `keep this PowerShell edition`, `choose PostgreSQL Y`, `use this architecture`, `override the default`) and define the exact affected **S2C development** or **host repository** scope.
2. Inspect the official current support/maturity/compatibility, dependencies and security implications. Explain any fresh-major, preview, deprecated/EOL or unproven-structure risk. Distinguish normal **newly GA supported** release from a **known insecure/EOL** version.
3. Record an `OVR-ID` in the [override record template](technologyOverrideTemplate.md): requester instruction, requested version/structure, exact repository/path scope, rationale, support evidence/date, compatible alternatives, risk and mitigation, affected requirement/AC, required tests and rollback, expiry/review trigger, and any outstanding independent authorization.
4. **For a supported stable new major:** explicit user choice can bypass the *conservative maturity/adoption default* (e.g., the user asks for freshly GA .NET 11) with documented risks and validation design. User instruction **is the preference approval** within their control; additional independent signoff only when required by the host's existing policy or security constraints.
5. **For EOL/preview/high-risk versions or experimental architecture:** do not treat the user's preference as proof of security. Flag `OVERRIDE_REVIEW_REQUIRED`, document compensating controls, isolation/migration plan and responsible authorized risk acceptance where needed. Existing host security, data protection, permissions, statutory requirements and Path Guard are **not overrideable via this mechanism**. If unacceptable, remain `BLOCKED` while offering a supported option.
6. In A/A.1, record and review the exception as **design input**. In future B/B.1, check the actual implementation against that exact version/architecture and current risks after **separate coding authorization**. Do not perform Git commits, migrations, deployments, database changes or host overrides merely because a version was requested.

**Priority rule:** system safety/security and verified host policy > actual owner permissions and explicit constraints > **explicit user-selected stack/version** > this policy's **conservative default recommendation**. Where constraints conflict, do not choose secretly; record conflict and ask the relevant authorized owner.

Override outcomes: `REQUESTED`, `ASSESSING`, `ACCEPTED_FOR_DESIGN`, `OVERRIDE_REVIEW_REQUIRED`, `BLOCKED`, `IMPLEMENTED_VERIFIED` (only future evidence). `ACCEPTED_FOR_DESIGN` is not permission to modify files.

## 5. Worked examples as of 2026-11-13 — illustrative, not universal

| Stack | Conservative default example | With explicit user override |
| --- | --- | --- |
| **.NET** | .NET 10 is supported LTS (released 2025-11-11), suitable candidate for a new project if dependencies compatible. .NET 11 (released 2026-11-10) is **supported STS but too newly GA** for automatic selection; .NET 8 reached EOL 2026-11-10 and is **not** a secure new-project default | If a user explicitly requests `.NET 11`, document maturity/compatibility risk and adopt as **design target** under override; for `.NET 8` flag unsupported/EOL and require a legacy/temporary exception, compensating controls and upgrade plan before unsafe deployment |
| **Python** | Choose a currently security-supported mature interpreter meeting real dependency/platform needs, not necessarily the highest new CPython feature version | If user selects a newer interpreter, record compatibility/wheel/test evidence; no automatic rejection solely for recency |
| **PowerShell** | Select a supported mainstream PowerShell version/edition appropriate to Windows/Linux and enterprise module compatibility; on 2026-11-13 PowerShell **7.6 LTS** is listed supported by Microsoft, while 7.4/7.5 reached support end in Nov 2026 | Honor an explicit edition/version request only with its true support status, module compatibility and any needed exception; don't silently replace Windows PowerShell 5.1 scripts |
| **SQL/database** | Choose a supported mature version of the **named database engine**, not a fabricated `SQL 2026` version; use stable migrations and dialect | If user requires a new PostgreSQL/SQL Server/MySQL major or engine-specific feature, document compatibility/schema/rollback and validate the exact engine, not generic SQL syntax |

Official sources checked for **dated examples**: [Microsoft .NET support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) (last updated 2026-11-10), [Microsoft .NET 8/9 EOL notice](https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support/), [PowerShell lifecycle](https://learn.microsoft.com/en-us/powershell/scripting/install/powershell-support-lifecycle). Actual support depends on the day and platform; revalidate before real implementation. Do not retarget an existing host automatically.

## 6. Integration into A → A.1 → B → B.1

- **A/P3:** collect dated `TECH-ID` evidence for S2C source **and/or** host, including official support, community/tool maturity, alternatives and any `OVR-ID`.
- **A/P5/P6:** define supported default structure/version, or explicitly requested override, with compatibility and architecture alternatives. Link `S2C-NFR-008` and impacted feature requirements.
- **A/P7/P8:** risk assessment covers fresh major churn, EOL vulnerabilities, edition/dialect mismatch, migration/data loss, and experimental structure; document the **highest-priority unresolved risk** and its mitigation in design.
- **A.1:** review under `A1-VAL-01/05/07` for current support, ordinary default or evidence-backed override, architecture compatibility and outstanding approvals; missing critical safety evidence `FAIL/BLOCKED`.
- **B:** implementation only if separately authorized; respect exact approved/overridden target, no unrequested SDK or database upgrade, and apply current supported security patches as appropriate.
- **B.1:** `B1-VAL-01/03/04/06` verifies **effective** compiler/interpreter/runtime/DB/PowerShell editions, package versions, CI and schema against the approved `TECH-ID`/`OVR-ID`, tests and risk signoffs.
- **Handoff:** record chosen default or override, official support checked date, actual approval state, exception/expiry and pending migration. Never rewrite previous approval or claim validation run before it did.

## 7. Trace and limitation

`S2C-NFR-008`/`S2C-NAC-008`: **any new technology/major-version/project-structure recommendation for S2C or a host** must be supported by maturity, community adoption, maintenance, compatibility, permission and documented alternative/override evidence. The **explicit user override** can replace the conservative default, but not bypass host security/authority.

This is a **Markdown-based agent contract**, not automatic version scanning or a configured runtime veto: `workflow_guard.py`, `policy_resolver.py` and `config_loader.py` currently do not implement this choice logic. Only a separately approved B-phase implementation could add code-level enforcement. RTM: [system matrix](../.traceMatrix.md); risk: [scored matrix](../.riskMatrix.md); reviews: [validation specification](../.workflow/validationSpecification.md).

## DOC-B03 — Verifiable support and version decision method

For every proposed Python, PowerShell, SQL engine/driver/dialect, .NET, JS/TS runtime, framework, SDK or OS, collect the **official maintainer lifecycle reference**, exact major/minor/patch, checked date, supported platform matrix, maintained security patch stream, compatibility with dependencies and test runner, and migration/rollback effort. Distinguish (a) safe patch within a selected supported major, (b) a newly GA but unproven major, (c) preview/RC, and (d) EOL. Never hardcode a universal preferred version or reuse an old source citation as present support evidence.

Conservative default means proven, supported and commonly adopted **at the task date**; an explicit user `OVR-ID` may select a newer stable or nonstandard structure within their scope. Unsupported/EOL or incompatible targets remain BLOCKED until risk-owner decisions and applicable verification, even if requested; no override waives path confinement, data safety, independent A.1/B.1 or observed regression tests. This document only governs recommendations until separately implemented and tested.
