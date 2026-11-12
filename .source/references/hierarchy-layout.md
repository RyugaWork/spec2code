# Spec2Code Hierarchical Architecture and Handoff Contract (v0.6.1)

## Owner-defined paths

```text
./s2c/.summerize.md                            # root layer pathing matrix and graph
./s2c/Present/.summerize.md                    # layer definition; controller/feature matrix
./s2c/Present/MemberPage/.summerize.md         # component/controller-level index
./s2c/Present/MemberPage/.MemberPage.Render.md # indexed function, version, source path, last change
./s2c/API/.summerize.md                        # same model for API layer
./s2c/API/MemberController/.summerize.md
./s2c/API/MemberController/.MemberController.GetMember.md
# ... Application, DataAccess, Persistence, Security, Integrations,
#     Delivery, Quality, Governance have their own .summerize.md
./.agents/.handoffs/.details/.visualChange.{SessionID}.md
./.agents/.handoffs/.details/.specChange.{SessionID}.md
./.agents/.handoffs/.buildnotes.handoff.md
```

`Controller#1`/`Function#1` in the request are placeholders: replace with *observed* source symbols. Never invent controller/function stubs for an empty scaffold. `Present` refers to the frontend, and its child nodes can be components/pages rather than .NET controllers.

## Index and graph

- `./s2c/.summerize.md`: all layers, source statuses, static layer dependencies, pathing matrix D/T/- and Mermaid graph. Source of traversal, not technical implementation truth.
- `./s2c/<Layer>/.summerize.md`: layer definition, list of controllers/components, adjacent layers, bounded component link matrix.
- `./s2c/<Layer>/<Component>/.summerize.md`: exact source path, source fingerprint, list of indexed function declarations, observed relative imports to peer components.
- `./s2c/<Layer>/<Component>/.<Component>.<Function>.md`: function symbol, source line, revision `rN`, last file-fingerprint change summary; semantic behavior not automatically invented.
- `.agents/state/infrastructure.json`, `.agents/state/system-graph.json`, `.agents/state/architecture-docs.json`, `.agents/state/symbol-cache.json`: machine-only inventories.

The static declaration parser indexes conventional C#, Python, TypeScript and JavaScript declaration patterns; it is not a full semantic compiler. A missing edge/function is **unknown**, not proof of no dependency. C# project references are observed static layer links. Frontend relative imports establish same-layer component links. There are no built-in assumed cross-layer edges. Other dependencies remain unobserved until evidence exists.

Generated documents carry `<!-- spec2code:managed-architecture v1 -->`; script refuses to overwrite a hand-written collision. The tool never removes source or hand-written docs, and does not remove orphaned generated docs silently. Current root index is authoritative for active components; review stale files before manual cleanup.

## Pending and merged handoff protocol

1. `start`: compare local Git HEAD and eligible file fingerprints to the last session checkpoint. External changes go to the new session ID's pending visual log; baseline does not create a change event.
2. `record`: register specific authored source changes in the same session's pending spec log.
3. `checkpoint`: discover commits with no matching `Spec2Code-Session:` trailer; append external events in that session's visual log.
4. `finish`: verify every in-session changed source path is either registered or attributed to an outside commit, then write FINISH event.
5. `merge --session-id <EXACT-ID>`: verify FINISH, validate pending file header/type/session and SHA-256; append actual pending content to buildnotes ledger with `SPEC2CODE-MERGED` marker; verify persisted content before `unlink` on each exact file.
6. If the process crashes after ledger write but before deletion, retrying the same session recognizes the existing marker, verifies content and removes the pending file without appending a duplicate.
7. If a pending file changed after the ledger write, it is not deleted unless its new content is safely archived and re-verified.

`./.agents/.handoffs/.buildnotes.handoff.md` begins with a small `Quick handoff` table. Detailed merged records are retained below the marker for forensic traceability, but the agent should read only the quick summary and relevant session subsection. No wildcard deletion, `rmtree`, Git cleaning or remote operations.

## Token costs and correctness

- Enumerate eligible filenames/metadata locally without sending contents to the model.
- Hash permitted changed files (cache based on size and mtime); sensitive `.env*` excluded, sensitive configurations metadata only.
- Read selected small source files locally for **declaration indexing** only when fingerprint changes. Content stays in local process; only symbol name/line and evidence are written.
- Output at most a dozen path-change lines per checkpoint. Layer and component summaries limit matrices and indexed rows.
- If needed, run `checkpoint --verify` to rehash all safe eligible files when metadata is untrustworthy.
- Checking Git HEAD locally **does not detect un-fetched remote commits**. Never claim live remote status.
