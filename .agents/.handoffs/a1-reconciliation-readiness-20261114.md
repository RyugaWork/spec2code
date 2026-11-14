# A.1 design-readiness checkpoint — candidate acceptance and stakeholder Draft alignment

**Work date:** 2026-11-14 Asia/Ho_Chi_Minh. **Author evidence only:** ChatGPT using GitHub + Google Docs connectors, not Codex CLI, independent A.1 or host negative tests. **Git input:** `fc81e26c850da75c9cee194b66ada8235226e26f` on `docs/plan-089-a1-readiness`. **Git output:** the commit containing this handoff; re-fetch branch HEAD. **Google Draft:** doc `1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4`, tab `t.0`, revised to `AHj4eMTAw3s3g2hRmmpvE3EnGWU8NTjzT3VSfebORixtFnk9xk3LYwintxxZQ3TnFuRiYQTo5cLt45_7Sjzz9o5_y9bUNiK0CvYdruUZww`.

## What materially changed

1. The canonical SRS now has **six BR-022..027 candidate acceptance envelopes** with visible positive and adverse oracles, input/denominator questions, accountable business/host roles, and no invented approved threshold or executed case.
2. The Google BRD Section-16 paragraphs BR-003, BR-017 and BR-019 were updated in place to clarify seven business vs nine task vs five machine stages, n=1 not plural reviewer independence, and synthesis not a formal independent A.1 signature.
3. Existing governance, RTM and validation procedures link those changes and distinguish author correction from actual owner-accepted business equivalence. False direct quote was corrected in the prior source-pair pass; APP-01..06 remain author-scoped interpretations of the user's broad `duyệt hết đi`.
4. One consolidated documentation commit, no runtime/config/CI and no new feature/AC/test IDs. Historical PLAN-106..110 handoffs remain unchanged.

## Outstanding hard gates

- Product/document owner: accept or revise exact source pair, BR-003/017/019 semantics, and each BR-022..027 measurable AC/threshold/scope/exception.
- Architecture/tool owner: choose actual ADR-102-01..08, provider/runtime versions and interaction contracts.
- Host/security owner: accept a tested threat model/mitigation plan for open P0, sandbox permissions, negative fixtures; actual residual remains `UNKNOWN` until verified.
- Independent A.1 reviewer (not the author): sign A1-VAL-01..09 against final Git SHA and Google revision, retaining dissent and owner evidence.
- Separate Phase-B authorization and later B.1 are required even after any true A1_PASS.

**STOP/readiness state:** `AUTHOR_DRAFT_RECONCILED / INDEPENDENT_A1_NOT_RUN / P0_OPEN / B_NOT_AUTHORIZED`. PR #10 is expected to stay Draft. No native Spec Kit/CLI, Gemini MCP, Linux/Windows Path Guard, local dirty worktree or build regression was observed. On resumption, re-check current branch SHA, Google revision, and user-owned local state before any mutating task.

## Follow-up A.1 author checkpoint — mirror parity and source-linked static checks (2026-11-14)

**Git inspected before commit:** `003297ff1253e661414350483b53a76f9afdaa67` on the same existing `docs/plan-089-a1-readiness` branch. **Google stakeholder Draft before:** `AHj4eMTAw3s3g2hRmmpvE3EnGWU8NTjzT3VSfebORixtFnk9xk3LYwintxxZQ3TnFuRiYQTo5cLt45_7Sjzz9o5_y9bUNiK0CvYdruUZww`; **after revision-guarded Section-36.5 append and read-back:** `AHj4eMTpTE_OFxAkB4X-3MXvcz0WSTl4b6D-UptJB7WLJq2Xkac8kDoGH7gDEkqWIJfGQV9wVuMrfbmWlJAdFueAU_exvNrOc-0t5BIIZA`. Output Git SHA is the commit that appends this checkpoint; recheck HEAD. This is **one author model**, `independentReviewerCount=0`.

| Author-only inspection | Observed evidence | Not established |
| --- | --- | --- |
| BR source identity | Git SRS has BR-001..027, Google now explicitly has BR-001..027; previously Google had exact tokens only BR-001..022 | Requirement-by-requirement semantic signoff |
| Markdown navigation | 17 core documents, 538 internal relative path targets checked, none missing | All repository links, anchors, remote URLs |
| BR acceptance catalogue | 42 distinct `TC-S2C-BR001..021-P/N` IDs | Any executed/PASS testcase |
| Candidate feature catalogue | 44 distinct `TC-F043..064-P/N` IDs | Approved AC or real positive/negative run |
| Codex/Gemini interface catalogue | 12 distinct `MM-TC-01..12` IDs | Working provider/CLI, MCP sandbox evidence |
| Historic author batches | Five distinct PLAN-106..110 handoffs, each with exactly 10 unique R/S/K/M/Z task IDs | 50 implemented runtime features or independent workers |
| Validation check catalogues | Nine A1-VAL-01..09 and nine B1-VAL-01..09 IDs | Any formal gate run or signoff |
| Source-based P0 observations | `workflow_guard.py` `close` constructs a scope-free evaluate request; VERIFY and HANDOFF_REVIEW policy uses `implement`; policy snapshot omits source/spec hashes | A reproducible local regression run or a corrected runtime |
| Repo PR | PR #10 observed Draft and unmerged, based on PLAN-088 | Permission to merge or release |

**Stage record:** DISCOVER=Git/Google source identity read; PLAN=limited A.1 drift review; RISK MANAGEMENT=RM-001..005 and related P0 remain OPEN; IMPLEMENT=Google Draft Section 36.5 + existing governance/handoff Markdown only; TEST=static path/identifier checks; VERIFY=Google revision read-back, Git final fast-forward/read-back pending this checkpoint; OPTIMIZE=existing canonical documents reused, no new BRD/SRS; HANDOFF=this record; DOCUMENT=existing document-governance record updated. No Python/JSON/CI changes or host commands were performed.

**Decision and safety state:** `AUTHOR_STATIC_CHECKS_COMPLETE / GOOGLE_BR_IDS_RECONCILED / A1_NOT_RUN / P0_OPEN / B_NOT_AUTHORIZED / B1_NOT_RUN`. Actual stakeholders must decide AC and revision authority; an authorized independent reviewer must execute A.1; later B authorization, Windows/Linux Path Guard/Workflow Guard negative tests and B.1 must remain distinct. STOP at this external boundary rather than self-authorizing unsafe execution.
