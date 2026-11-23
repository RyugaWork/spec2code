# Web v1.0 — RM-001..052 applicability and security-owner review overlay

Date: 2026-11-23; source input `fa2ba44e4a2076cf004160831fdaa7a3f2ec8148` on `docs/plan-089-a1-readiness`. **PROPOSED / OWNER_PENDING** under WEB-004 and WEB-027. This is an overlay, not a replacement for [the canonical risk matrix](../.riskMatrix.md). Existing likelihood, impact, priority, residual, global statuses and risk history remain unchanged. No code/runtime remediation, Web tests, or owner signoff is implied.

## Decision taxonomy and constraints

- `WEB_APPLIES`: direct Markdown, provider, manual checkpoint, planning, evidence, host-document or release exposure; requires scoped controls/tests and risk-owner decision.
- `SPLIT`: underlying runtime attack surface excluded from the proposed Web distribution, but a Web analogue or data/authority/ownership concern still applies; **do not close or reduce the global risk**.
- `RUNTIME_EXCLUDED`: no reachable corresponding machine capability is proposed in Web v1.0; exclusion must be proven by the eventual allowlisted payload and permissioned profile behavior. If an excluded feature becomes reachable, reopen applicability and stop.
- `PENDING_OWNER` for all rows: the author makes only an initial classification. Security/Host Owner must approve scope, supported provider capabilities, any applicability difference and actual source-bound evidence. Until then neither `EXCLUDED` nor `SPLIT` is a security waiver.

Owner codes: SEC=Security/Provider Owner; QA=QA/Independent Reviewer; HOST=Host/Architecture Owner; ARCH=Architecture Owner; PRODUCT=Product Owner. Listed WEB-TC IDs are **designed/not-run negative or functional checks**, not executed evidence. For runtimes that are out of profile, their native security checks retain global NOT_RUN and must not be converted to Web PASS.

## 52-row proposal — no ID replaced or silently closed

| Risk | Initial Web scope disposition | Scoped failure / explicit exclusion to assess | Decision owner | Related planned WEB-TC | Review status |
| --- | --- | --- | --- | --- | --- |
| RM-001 | SPLIT | Local Windows Path Guard/race excluded; enforce no local runtime in Web bundle | SEC | WEB-TC-08, WEB-TC-13 | PENDING_OWNER |
| RM-002 | SPLIT | Machine VERIFY/HANDOFF operation excluded; manual policy/gate mapping still applies | ARCH | WEB-TC-08, WEB-TC-09 | PENDING_OWNER |
| RM-003 | WEB_APPLIES | Source/spec drift invalidates Web claims and prior review evidence | QA | WEB-TC-11 | PENDING_OWNER |
| RM-004 | SPLIT | Runtime CLOSE excluded; manual STOP must not silently close or authorize | QA | WEB-TC-10 | PENDING_OWNER |
| RM-005 | WEB_APPLIES | Host file ownership, destructive migration and evidence loss | HOST | WEB-TC-02, WEB-TC-12, WEB-TC-15 | PENDING_OWNER |
| RM-006 | WEB_APPLIES | AI authoring falsely described as business/security approval | PRODUCT | WEB-TC-08, WEB-TC-09 | PENDING_OWNER |
| RM-007 | WEB_APPLIES | Web STOP/resume accidentally claims persistent runtime state | QA | WEB-TC-10, WEB-TC-11 | PENDING_OWNER |
| RM-008 | WEB_APPLIES | Version mismatch and active legacy-state upgrade safety | HOST | WEB-TC-12, WEB-TC-15 | PENDING_OWNER |
| RM-009 | WEB_APPLIES | Host AGENTS and upstream Spec Kit ownership precedence | HOST | WEB-TC-02, WEB-TC-07 | PENDING_OWNER |
| RM-010 | WEB_APPLIES | Handoff falsely PERSISTED or leaks private context | SEC | WEB-TC-10, WEB-TC-14 | PENDING_OWNER |
| RM-011 | WEB_APPLIES | Product coding or commit starts without approved Phase B | PRODUCT | WEB-TC-08 | PENDING_OWNER |
| RM-012 | WEB_APPLIES | Manual Spec Kit syntax/feature pointer misapplied | ARCH | WEB-TC-07 | PENDING_OWNER |
| RM-013 | WEB_APPLIES | Historical build/test evidence treated as fresh PASS | QA | WEB-TC-09, WEB-TC-11 | PENDING_OWNER |
| RM-014 | WEB_APPLIES | Missing per-iteration risk re-evaluation and evidence | SEC | WEB-TC-05, WEB-TC-09 | PENDING_OWNER |
| RM-015 | WEB_APPLIES | Missing independently authorized source/AC/RTM A.1 signoff | PRODUCT | WEB-TC-08, WEB-TC-09 | PENDING_OWNER |
| RM-016 | SPLIT | Host adversarial OS tests deferred; Web-specific B.1 security remains mandatory | SEC | WEB-TC-13, WEB-TC-14 | PENDING_OWNER |
| RM-017 | WEB_APPLIES | A.1/B/B.1/release gates collapsed or bypassed | PRODUCT | WEB-TC-08 | PENDING_OWNER |
| RM-018 | WEB_APPLIES | Unreviewed newly released technology recommended as supported default | ARCH | WEB-TC-04 | PENDING_OWNER |
| RM-019 | SPLIT | Runtime EOL install excluded; inaccurate host/tool version guidance remains | ARCH | WEB-TC-04, WEB-TC-07 | PENDING_OWNER |
| RM-020 | WEB_APPLIES | Novel host document structure disrupts established ownership | HOST | WEB-TC-02 | PENDING_OWNER |
| RM-021 | WEB_APPLIES | Stale vendor support facts or version facts become source authority | ARCH | WEB-TC-04 | PENDING_OWNER |
| RM-022 | WEB_APPLIES | Requester override bypasses applicable host/security rules | SEC | WEB-TC-05, WEB-TC-08 | PENDING_OWNER |
| RM-023 | WEB_APPLIES | Version/structure override treated as implicit source edit permission | HOST | WEB-TC-08, WEB-TC-12 | PENDING_OWNER |
| RM-024 | WEB_APPLIES | Conservative default silently hides explicit safe user choice | PRODUCT | WEB-TC-04, WEB-TC-05 | PENDING_OWNER |
| RM-025 | WEB_APPLIES | Sequential model perspectives misrepresented as independent votes | QA | WEB-TC-09 | PENDING_OWNER |
| RM-026 | SPLIT | Automated worker coverage excluded; human independent coverage still required | QA | WEB-TC-09 | PENDING_OWNER |
| RM-027 | RUNTIME_EXCLUDED | Worker weight/persona algorithm not in Markdown Web profile; prohibit false runtime claim | ARCH | WEB-TC-08 | PENDING_OWNER |
| RM-028 | WEB_APPLIES | Citations, files, test outputs or evidence fabricated by Web author | QA | WEB-TC-03, WEB-TC-09 | PENDING_OWNER |
| RM-029 | SPLIT | Cross-worker orchestration excluded; permitted Web provider/context data boundary remains | SEC | WEB-TC-14 | PENDING_OWNER |
| RM-030 | WEB_APPLIES | Risk/approval dissent suppressed in summary or synthesis | SEC | WEB-TC-08, WEB-TC-09 | PENDING_OWNER |
| RM-031 | WEB_APPLIES | Untrusted Markdown prompt injection and sensitive disclosure | SEC | WEB-TC-13, WEB-TC-14 | PENDING_OWNER |
| RM-032 | WEB_APPLIES | Resume loses policy/source/review identity after drift | QA | WEB-TC-10, WEB-TC-11 | PENDING_OWNER |
| RM-033 | WEB_APPLIES | Token/context limits result in missing mandatory policy or unfounded quality claim | QA | WEB-TC-06, WEB-TC-09 | PENDING_OWNER |
| RM-034 | RUNTIME_EXCLUDED | Autonomous self-evolution/config execution excluded from package; verify capability negative | SEC | WEB-TC-08 | PENDING_OWNER |
| RM-035 | RUNTIME_EXCLUDED | Generated-code execution with CI credentials excluded from Web release | SEC | WEB-TC-08, WEB-TC-14 | PENDING_OWNER |
| RM-036 | WEB_APPLIES | Cleanup/upgrade overwrites historical or host-owned artifacts | HOST | WEB-TC-02, WEB-TC-12, WEB-TC-15 | PENDING_OWNER |
| RM-037 | WEB_APPLIES | Source summarization omits business or security authority | QA | WEB-TC-03, WEB-TC-05 | PENDING_OWNER |
| RM-038 | RUNTIME_EXCLUDED | Automated DBA/lint/mutation repair loop is future runtime work | ARCH | WEB-TC-08 | PENDING_OWNER |
| RM-039 | WEB_APPLIES | Context/token optimization loses mandatory policy coverage | QA | WEB-TC-06 | PENDING_OWNER |
| RM-040 | SPLIT | Automated retry/release feature disabled; manual upgrade interruption remains | HOST | WEB-TC-12, WEB-TC-15 | PENDING_OWNER |
| RM-041 | WEB_APPLIES | Same-model check described as external independent acceptance | QA | WEB-TC-08, WEB-TC-09 | PENDING_OWNER |
| RM-042 | RUNTIME_EXCLUDED | Multiworker overlapping code patches excluded; Web cannot auto-commit | SEC | WEB-TC-08 | PENDING_OWNER |
| RM-043 | SPLIT | OS process containment excluded; connector/host authorization still bounded | SEC | WEB-TC-13, WEB-TC-14 | PENDING_OWNER |
| RM-044 | SPLIT | Concurrent worker lease excluded; manual STOP and bounded handoff still required | QA | WEB-TC-10 | PENDING_OWNER |
| RM-045 | WEB_APPLIES | Same-model review and unmeasured quality/cost claims | QA | WEB-TC-06, WEB-TC-09 | PENDING_OWNER |
| RM-046 | WEB_APPLIES | Interface/version/evidence mismatch triggers false READY claim | QA | WEB-TC-09, WEB-TC-11 | PENDING_OWNER |
| RM-047 | SPLIT | MCP server excluded; untrusted-source injection still relevant to Web | SEC | WEB-TC-13 | PENDING_OWNER |
| RM-048 | WEB_APPLIES | Remote source/context sharing or redaction leaks credentials | SEC | WEB-TC-14 | PENDING_OWNER |
| RM-049 | SPLIT | CLI/state DB failures excluded; unavailable Web capability must be stated | QA | WEB-TC-03, WEB-TC-09 | PENDING_OWNER |
| RM-050 | WEB_APPLIES | Git branch/source movement invalidates a later documentation/release action | HOST | WEB-TC-11, WEB-TC-12 | PENDING_OWNER |
| RM-051 | WEB_APPLIES | Stale Git/BRD pair and role lenses treated as independent A.1 | QA | WEB-TC-08, WEB-TC-11 | PENDING_OWNER |
| RM-052 | WEB_APPLIES | Chat interruption or resume loses tasks, policy and provenance | QA | WEB-TC-10, WEB-TC-11 | PENDING_OWNER |

**Coverage:** SPLIT=12; WEB_APPLIES=35; RUNTIME_EXCLUDED=5; total 52 distinct risk IDs. This table intentionally contains **no changed L/I/E or CLOSED state**.

## Risk-owner disposition protocol (required for DEC-WEB-01/04)

For each RM ID on the **exact final source** record: existing L/I/E + provenance; Web-applicable scenario and exposure; rationale for runtime exclusion if any; actual provider permissions and data policy; selected control; owner/role; linked applicable positive and negative AC/test; observed outcome or NOT_RUN; expected residual (explicit estimate); verified residual only with independent evidence; ACCEPT/REVISE/BLOCKED and date. All applicable P0s must be treated and independently accepted/verified by the applicable policy before release. No unsupported test or review can be accepted as a substitute.

Special blocker RM-001: globally P0/20 OPEN residual UNKNOWN; local Windows race remains for later runtime even if Web v1 distribution excludes scripts. If Web can invoke a local tool despite the proposed boundary, stop the Web-only release, revise the scope and complete applicable OS/adversarial testing.

Cases WEB-TC-02/08/10/11/12/13/14/15 form priority owner safety checks, but **none has been run**. [Proposed acceptance crosswalk](webV1AcceptanceAndTraceability.md) and [A.1 packet](webV1A1DesignReviewPacket.md) are separate, non-approval artifacts.

## AGENTS.md AI-executed integration — design change impact (2026-11-23)

[AGM-01..17 matrix](webV1AgentsIntegrationMatrix.md) adds an optional **authorized host AGENTS write** surface to Web v1, which must be explicitly reviewed rather than treated as a general Web capability. Reassess at minimum RM-005 (unowned data loss), RM-006/015/017 (false approval and phase bypass), RM-009 (host AGENTS/Spec Kit precedence), RM-010/032/052 (STOP/hand-off/drift), RM-022/023 (override versus authorization), RM-031/047/048 (prompt injection and credential disclosure), RM-036/050 (conflict/cleanup and concurrent updates), and RM-041/051 (invalid independent approval). Each remains PENDING_OWNER at its original global score/status. Planned negative cases WEB-TC-19 and WEB-TC-21 cannot PASS without real denied-write and readback evidence. This scope change requires reapproval of DEC-WEB-01/02/04/06 and revised A.1; no claim that the OS runtime risk RM-001 is repaired.

## RM-001 applicability clarification required by Gemini review (owner decision pending)

The existing RM-001 `SPLIT` row is **not a blanket exception** for the agent-executed AGENTS write feature. The [mode-specific matrix](webV1GeminiReviewDisposition20261123.md#7-security-owner-decision-matrix-for-rm-001) distinguishes (a) Web uploaded/pasted source without local execution, (b) permissioned remote GitHub AGENTS modification with real remote-only execution, (c) Codex/local Windows agent execution (RM-001 remains applicable and blocked absent independently verified OS containment), and (d) other local agents needing separate host security analysis. All are owner-pending; global risk remains P0, 4×5=20, residual UNKNOWN. A test fixture without a real host operation cannot certify non-applicability. The Security Owner must sign supported-provider scope and adversarial evidence before Phase B/B.1; unresolved applicable P0 vetoes release.

## A-Closure final owner mode/attack-surface question (2026-11-23)

[Owner approval D-02 and mode-specific host requirements](webV1AClosureApprovalPacket20261123.md#d-02--rm-001-release-applicability-blocker) require evidence-based **supported-mode selection**, not automatic P0 exemption: Web read/upload and remote GitHub API-only AGENTS writes may exclude local Windows OS race when verified; Codex/local Windows write requires actual independent OS isolation evidence. Every RM-001..052 profile row still `PENDING_OWNER`; 35 WEB_APPLIES / 12 SPLIT / 5 RUNTIME_EXCLUDED remain unchanged, global P0/20 OPEN.

## U-05 — requester-approved Web product modes, NOT risk-owner closure (2026-11-23)

[Explicit requester environment decision](webV1RequesterConditionalDecisions20261123.md#6-u-05--scope-approved-execution-modes-security-risks-still-pending) limits proposed V1.0 to (1) uploaded/pasted ZIP/Markdown read-only in ChatGPT Web and (2) real, separately authorized **remote GitHub API** AGENTS create/adopt/upgrade. Local Codex/agent host writes on Windows, Linux or macOS are excluded. This updates the **product-mode applicability boundary only**. All 52 `RM-` row dispositions remain `PENDING_OWNER` until named Security/Host Owner approves evidence and tests. `RM-001` stays `SPLIT` for remote-only profile and global `P0 OPEN, 4×5=20`; no claim of local TOCTOU mitigation or risk closure. Real connector authorization/path/expected-SHA/readback still required, and no remote provider capability has been security-validated.
