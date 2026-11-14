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
