# ARCHIVE — Gemini-era Google BRD full content imported to Git

> **HISTORICAL_SOURCE / NON_NORMATIVE / SUPERSEDED_BY_GIT**. Imported upon explicit requester decision D01 (2026-11-23). This is the **complete text** from the native [BRD_Spec2Code](https://docs.google.com/document/d/1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4/edit) at exact Google document revision `AHj4eMTQo-4II6DrQF5kSGoY8OxDNISChHco-PFSx_OgzuUuEWu4R2qAsiNmlioUDwDF-cYLmUq__B8TxyeB5iOzSa8tL5uDM_9Rqh0Npw`, converted from native headings/lists and two tables to Markdown; **not** a second current BRD. Future changes and authority belong solely to [Git master SRS](../.spec.md) plus its approved technical matrices. Never use the old Google document to override current Git, accept stale requirements, or silently rewrite current BR/AC definitions.

## Import manifest and fidelity

- Google title: `BRD_Spec2Code`; document ID: `1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4`; tab count: 1.
- Exact source revision: `AHj4eMTQo-4II6DrQF5kSGoY8OxDNISChHco-PFSx_OgzuUuEWu4R2qAsiNmlioUDwDF-cYLmUq__B8TxyeB5iOzSa8tL5uDM_9Rqh0Npw`; acquired for D01 on 2026-11-23.
- Native extraction: **475/475 paragraphs**, **2 tables**, **11 table rows**, **51 table cells**, **220 bullet paragraphs**. All 475 native paragraph texts were matched 1:1, in original document order, against an independent Google Docs text read. Text run content is preserved; formatting, numbered list glyph styles and native tab attributes are normalized for Markdown rendering.
- The historical source is not a signed authoritative requirement or accepted technical baseline. For each divergence, the newer Git specification and explicit current requester decisions govern. Use this archive only for historical traceability.

---

## Original archived content (in native order)

## Source tab: Tab 1

### TÀI LIỆU YÊU CẦU NGHIỆP VỤ & KẾ HOẠCH TRIỂN KHAI — S2C | DRAFT v1.5 • PLAN-087–097

### 1. GIỚI THIỆU (INTRODUCTION)

Spec2Code (S2C) là một Universal AI Agent Skill phục vụ phát triển phần mềm theo đặc tả, với các tài liệu Markdown, trạng thái session, Path Guard và cơ chế quản trị trên Git repository. S2C phối hợp ChatGPT/Codex và có thể đọc artifact của GitHub Spec Kit; một Orchestrator/API độc lập chỉ là khả năng mở rộng trong tương lai, không phải thành phần đã triển khai hoặc bắt buộc cho MVP.

S2C chuyển yêu cầu đã được chấp thuận thành thiết kế, task, bản sửa đổi trong phạm vi cho phép và test evidence có truy vết. Hệ thống giảm nguy cơ suy diễn thiếu căn cứ nhưng không bảo đảm xóa hoàn toàn hallucination; mọi khẳng định về mã nguồn và kết quả kiểm thử phải có bằng chứng. Cơ chế handoff hỗ trợ tiếp tục công việc giữa các phiên.

S2C hỗ trợ các AI coding assistants phù hợp, trước hết là ChatGPT/Codex, theo quyền và khả năng thực tế của môi trường chạy. Không khóa cứng vào GPT-4o, một mô hình cụ thể, API hay hình thức truy cập repo không được cấp phép.

### 2. KIẾN TRÚC & LỰA CHỌN CÔNG NGHỆ (TECH STACK)

Chính sách công nghệ áp dụng cho cả S2C và code của repository được tích hợp: ưu tiên stable, được hỗ trợ, phổ biến và có hệ sinh thái kiểm chứng; ưu tiên LTS nếu có lợi cho vòng đời vận hành. Tránh preview/beta, phiên bản vừa phát hành chưa đủ kiểm chứng hoặc đã hết hỗ trợ. Người dùng có thể yêu cầu override một phiên bản có lý do, phải ghi rõ phạm vi, compatibility evidence và risk acceptance; override không vô hiệu hóa security invariants.

- Backend Orchestrator (tương lai, chưa lựa chọn): không bắt buộc ASP.NET Core 8 hoặc .NET trong MVP. Nếu cần dịch vụ tập trung, kiến trúc và framework sẽ được quyết định bằng ADR, nhu cầu thực tế, vòng đời hỗ trợ, benchmark và security review.

- Database & Vector Search (tương lai, tùy chọn): phiên bản Markdown-first sử dụng file state/handoff/index có quản trị phiên bản. PostgreSQL, pgvector và database server chỉ bổ sung khi có nhu cầu đã chứng minh, kèm chính sách lưu trữ, migration và rollback. Không xem PostgreSQL 16 là lựa chọn bắt buộc.

- AI CLI/Agent Scripting: S2C hiện dùng Python, JSON configuration, scripts và unit tests trên nhiều hệ điều hành. Version policy phải dựa vào metadata, dependency/CI support của release cụ thể, không tuyên bố Python 3.12 là chuẩn duy nhất cho mọi dự án.

- LLM Integration: trọng tâm là vận hành agent skill trong cuộc hội thoại được người dùng điều khiển; API/MCP adapter là tùy chọn. Mọi output cần dẫn về source artifact, revision, test hoặc evidence; không sử dụng suy luận ẩn của mô hình làm bằng chứng nghiệm thu.

### 3. TÍNH NĂNG HỌC THUẬT: TRUY XUẤT DỮ LIỆU NHANH GỌN (FAST CONTEXT RETRIEVAL)

Fast Context Retrieval giúp giảm context thừa nhưng vẫn phải đọc đủ chính sách bắt buộc. S2C hiện có scanner tĩnh/lexical, architecture index và Context Router minimal/balanced/deep; các phương pháp retrieval từ bài báo là hướng nghiên cứu cần benchmark độc lập trước khi tuyên bố tích hợp hoặc có cải thiện hiệu suất.

#### 3.1. Dependency-Aware Retrieval (hướng nghiên cứu, cần kiểm chứng)

- Vấn đề cần kiểm chứng: một số chiến lược truy xuất có thể đưa context thừa hoặc bỏ sót dependency; không khái quát rằng mọi RAG đều quét toàn bộ code base. Phải so sánh với baseline lexical của S2C.

- Hướng nghiên cứu: Retrieval dựa trên dependency, phân lớp repository/file/symbol/source line và phân tích AST khi cần. Chưa được mặc định tuyên bố S2C đang dùng Tree-sitter hoặc đã tăng tốc 7,4 lần/giảm 80% token; chỉ công bố số liệu được đo, lặp lại và kiểm chứng trên benchmark S2C.

#### 3.2. Selective Retrieval (hướng nghiên cứu, cần kiểm chứng)

- Selective Retrieval: lựa chọn context theo task scope, cấu trúc thực tế, mức rủi ro và độ sâu cần thiết; không được bỏ qua host AGENTS, approved requirements, mandatory policies hoặc security evidence chỉ để giảm token. Mọi giả định thiếu chứng cứ phải giữ trạng thái UNKNOWN hoặc NEEDS_REVIEW.

#### 3.3. Iterative Retrieval (hướng nghiên cứu, cần kiểm chứng)

- Iterative Retrieval: trong tác vụ phức tạp, Agent điều chỉnh các truy vấn ngữ cảnh theo symbols/contracts hiện có và kiểm tra dependency sau mỗi vòng. Mọi kết luận phải gắn source path hoặc artifact; không cam kết tái sử dụng hoàn hảo code chỉ nhờ truy xuất.

### 4. TÍNH NĂNG CỐT LÕI & NGUYÊN TẮC HOẠT ĐỘNG (CORE FEATURES)

#### 4.1. Traceability (Khả năng Truy ngược)

- Traceability phải dựa vào Requirements Traceability Matrix (RTM) và provenance có ID ổn định; không bắt buộc chèn comment vào mọi đoạn code. Comment tham chiếu chỉ dùng khi thực sự cần và phù hợp coding conventions của host.

- Ví dụ một trace record: REQ-014 -> DES-005 -> TASK-014 -> RISK-003 -> src/component.py -> TC-014 -> EV-014.

- RTM phải ánh xạ Requirement -> Design -> Task -> Risk -> Source Change -> Test Case -> Evidence; lưu dưới dạng artifact được version-control trước khi cân nhắc database.

#### 4.2. Session Continuity (Handoff - Tính liên tục của phiên)

- Sử dụng session guard, state files, checkpoint, fingerprint và handoff trong .agents/state/ và .agents/.handoffs/ của repository host. Handoff ghi task, stage, code paths, thay đổi có bằng chứng, kiểm thử, risk còn mở, người phê duyệt và bước kế tiếp.

- Khi resume, Agent phải đối chiếu Session ID, Git checkout identity, HEAD, AGENTS/policy snapshot, affected paths và hashes. Nếu phát hiện drift, legacy session không tương thích hoặc thiếu approval thì dừng để REVIEW, không tự nối tiếp như thể điều kiện vẫn giữ nguyên.

#### 4.3. Universal & Config-Driven (Đa dụng & Điều khiển bằng cấu hình)

- Universal: không gán cứng business domain, ngôn ngữ, framework hoặc thư mục riêng của host. Scanner mang tính tĩnh/lexical, không thay thế semantic analyzer cho mọi ngôn ngữ; dependency không quan sát được phải báo UNKNOWN.

- Config-Driven: Tham số điều chỉnh được lưu trong .source/.config/*.json và policy/config host được xác nhận. Security invariants, quyền và Path Guard phải được enforce bởi code/host, không bị vô hiệu bởi file config.

#### 4.4. Cơ chế chống quá tải và Phân phối Worker (Anti-Overload & Worker Delegation)

- Chia nhỏ Task: Để tránh tình trạng tràn bộ nhớ ngữ cảnh (token exhaustion) và timeout, S2C không xử lý toàn bộ spec lớn trong một luồng duy nhất.

- Phân công: chia task thành phần có đầu vào, đầu ra, phạm vi và gate rõ ràng; một agent có thể làm tuần tự. Worker độc lập chỉ dùng khi môi trường hỗ trợ và được phép. Orchestrator/worker fleet chưa triển khai; không cam kết giảm thời gian/token khi chưa đo.

#### 4.5. Thống nhất và Dọn dẹp Tài liệu (Document Unification & Cleanup)

- Nguồn quản trị: .agents/.spec.md là baseline tổng BRD–kiến trúc–kế hoạch; Google BRD là bề mặt review cùng phiên bản/BR ID. RTM, risk và workflow là tài liệu chi tiết liên kết về baseline. Không chuyển tài liệu vào .specify/ hoặc specs/ vì đây là vùng sở hữu của Spec Kit.

- Dọn dẹp có kiểm soát: đánh dấu tài liệu bị thay thế và dẫn tới bản hiện hành; giữ ID, lịch sử, bằng chứng và session đang hoạt động. Chỉ xóa artifact đã xác minh chủ sở hữu/hash trong phạm vi được cho phép, có khả năng khôi phục; không có cleanup định kỳ tự trị.

#### 4.6. Động cơ thao tác mã bằng AST (AST-Based Code Manipulation)

- Nguyên lý: S2C không xử lý code như văn bản thuần túy (plain text) mà sử dụng Abstract Syntax Tree (AST) (thông qua Tree-sitter hoặc các parser tương đương).

- Mục tiêu: Cho phép AI chèn, sửa đổi hoặc xóa các node cụ thể (class, function) một cách chính xác tuyệt đối mà không làm hỏng cú pháp hoặc ghi đè nhầm mã nguồn của developer khác. Tiết kiệm token bằng cách chỉ xuất ra phần code thay đổi.

#### 4.7. Định tuyến & Tỉa ngữ cảnh động (Dynamic Context Routing & Pruning)

- Nguyên lý: S2C nội suy các file phụ thuộc dựa vào task hiện tại.

- Mục tiêu: Tự động "móc" (retrieve) phần code liên quan nạp vào context và "tỉa" (prune) các file không còn dùng tới ra khỏi bộ nhớ phiên làm việc. Đảm bảo AI không bị tràn token và giảm thiểu ảo giác (hallucination) trong các dự án quy mô lớn.

#### 4.8. Tường lửa ngữ cảnh & Quyền hạn AI (AI Firewall & RBAC)

- Nguyên lý: Áp dụng Role-Based Access Control (RBAC) cho AI Agent thông qua file cấu hình .s2crc.

- Mục tiêu: Chặn đứng các hành vi prompt injection. Giới hạn nghiêm ngặt quyền (READ/WRITE/DENY) trên từng thư mục hoặc file cụ thể (như .env, appsettings.json), chặn các output vi phạm ngay tại lớp Middleware trước khi ghi xuống ổ cứng.

#### 4.9. Phát hiện sai lệch Spec-Code (Drift Detection Engine)

- Nguyên lý: Động cơ quét chạy ngầm hoặc thông qua Git Hooks để so sánh mã nguồn thực tế với yêu cầu trong spec.md và tasks.md.

- Mục tiêu: Phát hiện sự sai lệch (Drift) khi developer sửa code thủ công mà quên cập nhật tài liệu. Hệ thống sẽ cảnh báo "Code Drift Detected" và yêu cầu AI hoặc con người đồng bộ hóa lại (cập nhật spec theo code hoặc sửa code theo spec).

#### 4.10. Vòng lặp Đồng thuận Đa Tác tử (Multi-Agent Consensus Loop)

- Nguyên lý: Phân tách nhiệm vụ cho các AI Agent độc lập: Coder Agent (viết code), Reviewer Agent (đối chiếu spec.md), và Tester Agent (sinh test case).

- Mục tiêu: Một Task chỉ được đánh dấu hoàn thành (Done) khi cả 3 Agent đạt được sự đồng thuận (Consensus). Ngăn chặn tình trạng một Agent tự sinh code rồi tự "lấp liếm" lỗi của chính mình.

#### 4.11. Multi-Agent Document Review (Weighted Expert & Personality Review)

### S2C bổ sung cơ chế review tài liệu theo yêu cầu với n worker được cấu hình. Orchestrator phân loại tài liệu/hệ thống, xác định chuyên môn bắt buộc, chọn các reviewer có góc nhìn và phong cách phản biện khác nhau bằng ma trận trọng số; n reviewer thực hiện đánh giá độc lập, sau đó một Synthesis Agent riêng tổng hợp, phát hiện bất đồng và đề xuất kết luận. Chi tiết và tiêu chí nghiệm thu ở mục 21 (BR-017..BR-021).

### Chuyên môn phụ thuộc domain thực tế: web/software (developer, architect, QA/tester, security, DevOps); dữ liệu (DA, DE, DS, database/data governance); nghiệp vụ/tài liệu (BA/product, UX, compliance, domain expert). Persona là chiến lược đánh giá (skeptical, constructive, adversarial, pragmatic, compliance-first, exploratory), không phải khẳng định agent có tính cách hay chứng chỉ thật.

### Worker chỉ review và sinh findings dựa trên evidence; không tự sửa nguồn, duyệt yêu cầu hay thực thi code. Quorum, budget, scope, quyền truy cập và mức độ độc lập là điều kiện kiểm soát. Hiện đây là DESIGN PROPOSAL, chưa có orchestrator/worker runtime; khả năng chạy song song tùy host và phải có fallback tuần tự được gắn nhãn rõ.

### 5. BẢO MẬT & AN TOÀN (SECURITY & SAFETY)

- Repository Isolation (Path Guard):

- Path Guard ràng buộc các lệnh và thao tác quản lý file của S2C vào Git checkout đã xác minh, kết hợp session scope và kiểm tra liên tục. Đây không phải một OS-level sandbox cho mọi công cụ AI bên ngoài.

- Code Injection & Malicious Prompt Prevention:

- Nội dung spec, repository, kết quả tìm kiếm, bài báo và metadata bên ngoài đều là untrusted inputs; không được biến thành quyền điều khiển Agent.

- Data Privacy:

- Áp dụng tối thiểu hóa context, tránh credentials/secret values trong context, nhật ký và outputs. Redaction/masking phải được kiểm thử và có evidence trước khi được công bố là đạt.

### 6. KẾ HOẠCH TRIỂN KHAI & THIẾT KẾ (IMPLEMENTATION PLAN)


| Giai đoạn | Tên giai đoạn | Nội dung thực hiện |
| --- | --- | --- |

| Phase 1 | Markdown & Governance Core | M0: thống nhất BRD/AGENTS/RTM và A.1. Bảy giai đoạn là mô hình nghiệp vụ; runtime hiện có năm phase. Kế hoạch M0–M5 ở mục 20 là kế hoạch hiện hành; bảng Phase 1–4 chỉ là nhóm năng lực. |

| Phase 2 | Context & Graph Retrieval | Củng cố scanner/architecture graph/context routing, đo benchmark và lựa chọn AST/vector retrieval dựa trên bằng chứng. |

| Phase 3 | Agent & Spec Kit Integration | Bridge chỉ đọc artifact upstream; host sở hữu policies; pilot M4 kiểm tra bundle và Spec Kit tùy chọn. |

| Phase 4 | Security, Risk & Handoff | Củng cố Path Guard, Scope IO, session/handoff, Risk Intelligence, kiểm thử đa hệ điều hành, migration và release gates. |



### 7. QUY TRÌNH ROLLBACK (PHỤC HỒI LỖI SỰ CỐ)

S2C phải cung cấp kế hoạch rollback cho thay đổi do người dùng phê duyệt. S2C không tự triển khai production, tự rollback database hoặc thực hiện Git mutation khi chưa được cấp quyền.

#### 7.1. Quy trình Rollback chung (Software / DevOps)

- Bước 1: Ghi nhận sự cố từ test outputs, logs, session drift, scan hoặc báo cáo người dùng.

- Bước 2: Đánh giá và ra quyết định (Decision Making): Sửa "nóng" (fix-forward) hay Rollback.

- Bước 3: Thông báo và chuẩn bị (Notification & Preparation).

- Bước 4: Thực thi phương án đã được phê duyệt (revert patch/restore backup/feature flag) trong phạm vi cho phép.

- Bước 5: Kiểm tra và xác minh (Verification): Chạy smoke test đảm bảo hệ thống ổn định.

- Bước 6: Tổng kết và rút kinh nghiệm (Post-mortem).

#### 7.2. Quy trình Rollback Cơ sở dữ liệu (SQL / Database)

- Xác định transaction lỗi: Gây treo hệ thống hoặc sai lệch dữ liệu.

- Đánh giá: Xác định các transaction liên quan bị phụ thuộc hoặc ảnh hưởng dây chuyền.

- Hoàn tác: SQL ROLLBACK chỉ áp dụng giao dịch chưa commit. Với thay đổi đã commit/migration, phải có backup, restore hoặc forward compensation được kiểm thử và cấp quyền theo phạm vi.

- Kiểm tra: Kiểm tra tính toàn vẹn dữ liệu.

### 8. CƠ CHẾ KHÓA PHIÊN BẢN (VERSION LOCK) & QUY TRÌNH NÂNG CẤP CÔNG NGHỆ

#### S2C áp dụng Version Lock dựa trên manifest và policy thực tế, hạn chế chọn API/dependency không tương thích.

#### 8.1. Cơ chế khóa phiên bản (Version Lock)

- Ranh giới công nghệ (Tech Boundary): Phiên bản runtime, language, framework, package và tooling phải được xác định từ manifest/lockfiles/policies thật của host.

#### 8.2. Quy trình nâng cấp công nghệ (Tech Stack Upgrade Workflow)

Khi có yêu cầu nâng cấp từ phiên bản hiện hành sang phiên bản đích đã xác minh hỗ trợ, S2C thực hiện năm bước:

- Đánh giá rủi ro và Vùng ảnh hưởng (Risk & Impact Assessment): Đánh dấu các phần phụ thuộc bị ảnh hưởng.

- Phân tích điểm khác biệt (Diff Analysis): Phân tích các Breaking Changes, API bị loại bỏ (Deprecated).

- Lập kế hoạch nâng cấp (Upgrade Planning): Lên chi tiết cấu hình, logic, thư viện cần nâng cấp.

- Xét duyệt Kế hoạch (Review Plan): Bản kế hoạch bắt buộc phải qua vòng đánh giá (Review).

- Thực thi và Review Code (Execution & Code Review): Thực hiện thay đổi có phạm vi và rollback rõ ràng, cập nhật RTM.

### 9. PHẠM VI, NGUYÊN TẮC VÀ TRẠNG THÁI TRIỂN KHAI

- Trạng thái: BRD revision 1.3 / PLAN-087+088 (13/11/2026). DRAFT FOR REVIEW; A.1/B.1 NOT_RUN. Baseline Git: c2b57a3a2dedebce0014b0cd6896b86a4a2494dc; nội dung thống nhất nằm ở .agents/.spec.md.

- Mục tiêu nghiệp vụ: Chuẩn hóa quy trình Spec -> Design -> Task -> Code -> Test -> Evidence; giới hạn phạm vi AI Agent; phát hiện rủi ro; khôi phục công việc qua handoff.

- In scope: AGENTS/policy routing, Spec Kit read-only bridge, RTM, 7-stage Workflow Guard, risk discovery & treatment, handoff.

- Out of scope: Autonomous deployment, auto merge/push/delete, thay đổi business requirements khi chưa duyệt, release tự động.

### 10. WORKFLOW 7 GIAI ĐOẠN VÀ VALIDATION GATES

- Stage 1 - DISCOVER: Xác minh checkout, approved requirements, architecture, session, boundaries. Output: Discovery Snapshot.

- Stage 2 - RISK_DISCOVER: Quét risks từ code, cấu hình, dependency, session. Output: Initial Risk Register.

- Stage 3 - SPECIFY_PLAN: chuẩn bị goals, RTM, thiết kế, task và test strategy. A.1 chỉ diễn ra sau toàn bộ A, bao gồm Risk Management và design handoff.

- Stage 4 - RISK_MANAGEMENT: Xác minh nguyên nhân gốc, gộp risk, áp dụng scoring/blocking. Output: Approved Risk Treatment Plan.

- Stage 5 - IMPLEMENT: Chỉ thực hiện approved tasks trong checkout được Path Guard bảo vệ.

- Stage 6 - VERIFY: kiểm chứng nội bộ trên revision thực tế; sau đó B.1 kiểm định hệ thống/host, bảo mật và stakeholder. Không dùng unit-test PASS thay B.1.

- Stage 7 - HANDOFF_REVIEW: Ghi session snapshot, before/after risk matrix, test approvals. Output: Handoff + Release/Continue Decision.

### 11. RISK CLASSIFICATION VÀ RISK ASSESSMENT MATRIX

- Risk taxonomy tối thiểu: Security, Path & Scope, Data Integrity, Requirements, Architecture, Dependencies, Implementation, Compatibility, Testing, Workflow, Privacy, Performance.

- Scoring matrix 5x5: Likelihood (Rare 1 -> Almost certain 5); Impact (Negligible 1 -> Severe 5). Score = L x I.

- Mandatory blocking gates: Path escape, unauthorized access, secret exposure, sai phạm approval sẽ bị block độc lập với điểm số.

### 12. RISK AGGREGATION, ROOT-CAUSE GRAPH VÀ JOINT TREATMENT

- BR-RISK-GROUP: Liên kết risk theo duplicate, shared verified root cause, causal chain, shared control, affected component.

- Risk Graph: Gồm các node Risk, Root Cause, Component, Requirement, Control, Patch, Test và Evidence.

- Joint treatment: Phải có test cho từng risk thành viên lẫn tests cho tương tác.

### 13. ACADEMIC EVIDENCE ENGINE (RESEARCH-DRIVEN REMEDIATION)

- Rapid evidence review: Tìm kiếm peer-reviewed papers, official standards.

- Research workflow: Hình thành câu hỏi nghiên cứu -> Lập query -> Tìm kiếm -> Trích xuất finding/DOI -> So sánh -> Thử nghiệm -> Lưu quyết định.

- Không được bịa bài báo, DOI, kết quả benchmark.

### 14. RISK-DRIVEN PATCHING & CONTINUOUS REASSESSMENT

- Chu trình: đọc register → phát hiện/gộp risk có bằng chứng → BEFORE → chọn risk cao nhất trong phạm vi → treatment/task → thực hiện theo quyền hiện có → review/tests → AFTER. Trong A chỉ sửa thiết kế; không tự vá runtime. AFTER kỳ vọng phải tách residual đã được kiểm chứng.

- KPI nghiệp vụ: Số risks open theo severity, verified root causes, patches verified, residual Critical, RTM test coverage. Không dùng KPI 'số patch'.

### 15. REQUIREMENTS TRACEABILITY, GOVERNANCE VÀ HANDOFF

- RTM: REQ -> DES -> TASK -> RISK -> CODE -> TC -> EVIDENCE. Một requirement có thể có nhiều tests và risks.

- STOP conditions: Phạm vi repo không hợp lệ, symlink/junction/path escape, thiếu mandatory docs, nguồn thẩm quyền xung đột.

- Handoff: Ghi lại task ID, phase, timestamp, branch/HEAD, approved scope, risk matrix.

- Integration với Spec Kit: Chỉ bridge/đọc artifacts trong phạm vi.

### 16. FUNCTIONAL REQUIREMENTS (BRD REGISTER)

- BR-001: ràng buộc exact authorized checkout. AC: root hợp lệ hoạt động; traversal/foreign root/symlink/junction escape bị chặn; sentinel ngoài phạm vi không đổi. M1.

- BR-002: giữ quyền sở hữu host policies/requirements. AC: đọc đúng AGENTS áp dụng; thiếu tài liệu bắt buộc hoặc xung đột thẩm quyền chặn thao tác liên quan. M1.

- BR-003: phân biệt ba lớp: quy trình nghiệp vụ bảy giai đoạn (mô tả cấp cao), vòng thực thi từng task chín bước DISCOVER→PLAN→RISK MANAGEMENT→IMPLEMENT→TEST→VERIFY→OPTIMIZE→HANDOFF→DOCUMENT và năm phase runtime hiện có của Workflow Guard. Đây không phải ba state machine khác nhau và không tự thêm phase vào code; owner còn cần chấp thuận cách diễn đạt.

- BR-004: A.1/B.1 là vòng kiểm định riêng. AC: mỗi tiêu chí có kết quả, revision, bằng chứng và reviewer; không tự nâng trạng thái khi thiếu quyết định. M0/M4.

- BR-005: RTM hai chiều với ID ổn định. AC: mỗi BR nối AC/design/task/risk/source/test/evidence hoặc ghi rõ NOT_MAPPED; giữ S2C-REQ-001..037 và NFR-001..009. M0/M2.

- BR-006: khám phá và chấm risk mỗi vòng thay đổi. AC: scenario, loại, nguyên nhân, evidence, L/I, owner, BEFORE/AFTER đầy đủ. M2.

- BR-007: gộp risk có căn cứ. AC: giữ ID thành viên; không gộp vì cùng component mà thiếu bằng chứng; kiểm tra từng thành viên và tương tác; không che blocker. M2.

- BR-008: dùng nghiên cứu cho mitigation khó. AC: nguồn/phiên bản/định danh xác minh được, giới hạn áp dụng, phương án thay thế và thử nghiệm; không bịa DOI. M3.

- BR-009: ưu tiên xử lý risk trong phạm vi được phép. AC: chọn risk cao nhất liên quan hoặc ghi lý do; design-only không sửa code; patch có task và regression evidence. M1/M2.

- BR-010: STOP/handoff/resume an toàn. AC: ghi trạng thái thực và PERSISTED/NOT_PERSISTED; resume kiểm tra lại scope/policy/source; STOP không ngầm CLOSE. Native pause/resume chưa có. M2.

- BR-011: context có giới hạn và bảo vệ dữ liệu. AC: minimal không bỏ policy bắt buộc; loại dữ liệu nhạy cảm; từ chối context cũ. M1/M3.

- BR-012: Spec Kit tùy chọn, bridge chỉ đọc. AC: standalone không bắt buộc Spec Kit; feature phải trong repo; thiếu spec/plan/tasks chặn bridge implement. M4.

- BR-013: công nghệ ổn định và override có phạm vi. AC: TECH có support/compatibility evidence; OVR ghi lựa chọn người dùng/risk; không tự đổi code hoặc nới security. M0/M4.

- BR-014: thống nhất tài liệu và cleanup khôi phục được. AC: mỗi chủ đề có chủ quản; link đúng; tài liệu cũ đánh dấu thay thế; không xóa dữ liệu chưa rõ chủ sở hữu. M0/M2.

- BR-015: kiểm chứng bundle/host/recovery. AC: bundle copy chạy độc lập; các ca Linux/Windows, collision, legacy và recovery có kết quả riêng. M4.

- BR-016: hồ sơ release có truy vết. AC: revision/manifest/tests/skips/risk/rollback/owner đầy đủ; CI không tự cấp quyền release. M5.

BR-017: Weighted Review Workforce. Cho phép n worker (1..maxWorkers theo policy), chọn tự động hoặc explicit, vai trò theo domain/risk và trọng số có cấu hình. AC: manifest ghi source revision, n yêu cầu/thực tế, role/persona, trọng số, coverage, quyền/budget; thiếu chuyên môn/quota phải BLOCK/REVIEW. n=1 chỉ là một lượt nhận xét, KHÔNG được tự báo cáo nhiều reviewer độc lập; lựa chọn mức independence/coverage vẫn cần owner duyệt. Proposed, owner/ETA UNKNOWN.

BR-018: Independent Evidence-Based Review. Mỗi worker nhận phạm vi và snapshot thống nhất nhưng nhận xét độc lập; finding có vị trí nguồn, claim, evidence, severity, confidence, suggested action và trace ID. AC: không có finding chỉ dựa trên persona; không đưa dữ liệu ngoài scope/secret vào report; unsupported claim ghi UNVERIFIED; failure/timeout giữ PARTIAL. Proposed.

BR-019: Synthesis & Dissent Preservation. Vai trò Synthesis tách chức năng tổng hợp khỏi reviewer workers, gộp duplicate theo nguồn, đánh giá coverage/chứng cứ, giữ dissent và lỗi chưa giải quyết. AC: conflict nêu rõ nguồn và worker; blocker không bị xóa vì đa số; kết luận chỉ PROPOSED/NEEDS_REVIEW. Synthesis riêng về vai trò KHÔNG chứng minh reviewer A.1 độc lập hoặc cấp quyền APPROVED. Proposed.

BR-020: Review Traceability, Safety & Handoff. Review có Review ID, source fingerprint, policy/config version, per-worker outputs, synthesis, RTM/risk links, audit trail và resume checkpoint. AC: source drift invalidates affected findings; Path Guard/connector authorization giữ nguyên; STOP ghi trạng thái và đối chiếu lại khi resume. Proposed.

BR-021: Review Validation & Acceptance. Thiết lập ca kiểm thử domain-role matching, quorum/budget, independence, fake consensus, P0 blocker, conflicting findings, injection, stale revision, interruption và approval. AC: A.1 duyệt thiết kế/contract; B.1 chỉ chạy trên host/runtime thật sau khi được phép triển khai; không dùng self-scored review làm nghiệm thu. Proposed.

### 17. ROADMAP, ACCEPTANCE VÀ RELEASE GATES

- M0: BRD/governance/RTM alignment và review A.1; T087-01/02.

- M1: sửa safety/workflow scope/operation/freshness trước pilot; T087-03/04.

- M2: risk/trace contracts và STOP/recovery; T087-05/06.

- M3: research/retrieval benchmark và mitigation evidence; T087-07.

- M4: host/platform pilot và B.1; T087-08/09.

- M5: release dossier và quyết định phát hành riêng; T087-10.

- Hồ sơ nghiệm thu: Requirement ID, owner, design/task refs, implementation status, evidence, tests, human approval.

### 18. TÀI LIỆU THAM KHẢO VÀ CHANGE CONTROL

- [1] NIST, Guide for Conducting Risk Assessments, SP 800-30 Rev. 1, 2012.

- [2] NIST, Secure Software Development Framework (SSDF), SP 800-218 v1.1.

- [5] GitHub, Spec Kit — Spec-Driven Development.

- [6] RyugaWork, Spec2Code repository.

- Change control: Chỉ stakeholder có thẩm quyền mới phê duyệt requirement, ngoại lệ version hoặc chấp nhận residual Critical risk.

### 19. PHỤ LỤC: MA TRẬN RỦI RO 5x5 (RISK SCORING REFERENCE)

- 


| I \ L | 1 (Rare) | 2 (Unlikely) | 3 (Possible) | 4 (Likely) | 5 (Almost certain) |
| --- | --- | --- | --- | --- | --- |

| 5 (Severe) | 5 | 10 | 15 | 20 | 25 |

| 4 (Major) | 4 | 8 | 12 | 16 | 20 |

| 3 (Moderate) | 3 | 6 | 9 | 12 | 15 |

| 2 (Minor) | 2 | 4 | 6 | 8 | 10 |

| 1 (Negligible) | 1 | 2 | 3 | 4 | 5 |



- 

### 20. BASELINE THỐNG NHẤT: CẤU TRÚC, CHỨC NĂNG VÀ TRIỂN KHAI

#### 20.1. Điểm đọc duy nhất và kiểm soát thay đổi

- Bản triển khai đầy đủ trên Git: https://github.com/RyugaWork/spec2code/blob/ed81320cbd54196334050506eaf087f59ba62993/.agents/.spec.md

- Revision này chứa BR-001..021, tiêu chí nghiệm thu, component contracts, lifecycle mapping, M0–M5 và T087-01..10. Google BRD là bản review nghiệp vụ của cùng baseline v1.3/PLAN-087+088. Trước khi code phải đối chiếu hai bên theo revision và BR ID; không lấy một bản chỉnh chưa đối chiếu để tự ghi đè quyết định đã duyệt.

- .agents/.spec.md sở hữu yêu cầu tổng, kiến trúc và kế hoạch; .traceMatrix.md sở hữu mapping hai chiều; .features.md ghi hiện trạng tính năng; .plans.md ghi tiến độ task; .risk.md giữ lịch sử/nội dung risk, .riskMatrix.md giữ điểm và treatment; .workflow/ và .documents/ là chi tiết hỗ trợ; AGENTS.md là điểm điều hướng quy tắc thao tác; handoff là lịch sử liên tục, không thay BRD. Không tạo thêm BRD/SRS độc lập hoặc bản sao từng phiên.

- Mỗi thay đổi phải cập nhật đồng bộ requirement/AC → design/task → risk → source/test/evidence và handoff liên quan. Giữ ID cũ, ghi nguồn/revision/owner/approval; owner chưa xác định ghi UNKNOWN. Không nâng trạng thái phê duyệt bằng nội dung do agent tự viết.

#### 20.2. Kiến trúc theo mã nguồn hiện có

- Policy: policy_resolver.py và governance_schema.py nhận task/paths/host policies, trả danh sách tham chiếu và lý do gate. Metadata không cấp quyền.

- Context: scan_infrastructure.py, architecture_tree.py, context_router.py nhận source được giới hạn, tạo inventory/graph/context minimal–balanced–deep. Scanner lexical không bảo đảm hiểu ngữ nghĩa mọi ngôn ngữ; dependency chưa rõ phải ghi UNKNOWN.

- Safety/IO: path_guard.py, scope_io.py xác minh exact checkout và target tương đối, cho phép managed IO hoặc từ chối. Đây không phải OS sandbox; Windows race/OneDrive cần nghiệm thu riêng.

- Session/evidence: session_guard.py, handoff_store.py quản lý checkpoint, attribution, visualChange/specChange và handoff đúng session. Native pause/resume chưa triển khai.

- Workflow: workflow_guard.py quản lý năm phase và journal. CLOSE mất task scope, mapping VERIFY/HANDOFF và fingerprint source/Spec Kit là các lỗi còn mở quan sát trong baseline; sửa tài liệu không sửa các lỗi này.

- Integration/config: speckit_bridge.py chỉ kiểm kê artifact upstream có giới hạn; mcp_boundary.py là thư viện, chưa có server; config_loader.py và JSON cấu hình không được vô hiệu security invariants.

- Toàn bộ script trên nằm trong .source/scripts/. Giữ CLI/JSON/schema/bundle hiện có tới khi có migration được review. Risk graph/research engine tự động là đề xuất; trước mắt dùng Markdown có ID và evidence.

#### 20.3. Cấu trúc S2C và host

- Repo phát triển: root AGENTS/README; .agents/ quản trị; .source/ skill/scripts/tests/references/config; docs/ hướng dẫn sử dụng.

- Host: .agents/skills/spec-to-code/ chứa bundle; .agents/state/ chứa state; .agents/.handoffs/ chứa log và ledger; s2c/ chứa architecture index. Host sở hữu AGENTS/requirements; Spec Kit sở hữu .specify/ và specs/. Không sao chép AGENTS của repo phát triển để thay policy host.

#### 20.4. Một lifecycle, ba mức mô tả

- Lifecycle tổng: A → A.1 → B → B.1 → quyết định phát hành.

- A gồm P1 scope, P2 spec plan, P3 nghiên cứu, P4 requirement/RTM, P5 feature design, P6 architecture/workflow, P7 Risk Discovery, P8 Risk Management, P9 design handoff. A.1 kiểm định trọn bộ A; thiếu approval không được suy thành quyền triển khai.

- B có năm phase runtime hiện tại: DISCOVER → SPECIFY_PLAN → IMPLEMENT → VERIFY → HANDOFF_REVIEW. Bảy giai đoạn nghiệp vụ ở mục 10 bổ sung Risk Discovery/Risk Management dưới dạng hoạt động quản trị, không phải thêm hai giá trị vào JSON runtime.

- B.1 diễn ra sau kiểm chứng nội bộ, bao gồm host/security/stakeholder acceptance. A.1 FAIL quay lại P tương ứng; B.1 FAIL do code quay B, do thay requirement quay A/A.1. Drift làm mất hiệu lực bằng chứng liên quan, không xóa lịch sử.

- STOP ở mọi giai đoạn: dừng mutation mới; ghi thao tác đang chưa rõ kết quả; chụp task/session/ref/paths/approval/evidence/risk/next action; giữ session hoạt động; xác minh đã ghi trước khi nói PERSISTED. Resume cần yêu cầu tiếp tục và đối chiếu scope/policy/source mới. Không dùng CLOSE/finish thay STOP.

#### 20.5. Dữ liệu và hợp đồng bằng chứng

- Requirement có ID/source/owner/revision/AC/priority/approval. Design/task có dependency, affected paths, owner role, AC và rollback. Risk có scenario/cause confidence/evidence/L/I/blocker/group edges/treatment/residual. Evidence có exact revision, command hoặc procedure, môi trường, thời gian, kết quả, skip/giới hạn, location/reviewer. Handoff giữ trạng thái thực, thay đổi self/external, risk và bước kế tiếp.

- Đây là hợp đồng logic cho Markdown, không khẳng định toàn bộ field đã có trong JSON. Mọi schema runtime mới cần version, validation, compatibility, migration và rollback test riêng. Truy cập repo qua connector không chứng minh local Path Guard/test đã chạy.

#### 20.6. Risk grouping và tiêu chí chất lượng

- Giữ thang hiện có: P0=16–25, P1=10–15, P2=5–9, P3=1–4 theo L×I. Path escape/unauthorized access/secret exposure/approval violation chặn độc lập với score. Nhóm risk chỉ dùng duplicate, nguyên nhân chung đã kiểm chứng, causal chain, control hoặc component; cùng component chưa đủ chứng minh chung nguyên nhân. Priority nhóm không thấp hơn blocker/thành viên cao nhất; không cộng điểm tương quan để tạo độ chính xác giả.

- Mỗi vòng chọn risk cao nhất liên quan hoặc ghi lý do khác; BEFORE/action/AFTER có evidence. Trong A, residual kỳ vọng tách residual thực đã kiểm chứng; viết mitigation không đóng risk. Giữ RM-001..024 cùng điểm hiện có cho tới khi có bằng chứng mới.

- Mục tiêu đề xuất: 100% BR đang hoạt động có AC và trace hoặc gap hiển thị; mọi kết quả xác minh có revision/môi trường; không bỏ mandatory security gate; đủ ca host/platform trước stable release. Không hứa tỷ lệ giảm token/latency trước benchmark.

#### 20.7. Roadmap hiện hành và công việc cụ thể

- M0 — T087-01 thống nhất baseline, T087-02 review A.1. Owner role: product/architecture reviewer. Đầu ra: BRD/AGENTS/RTM/risk/lifecycle đồng bộ. T087-01 đã soạn; A.1 chưa chạy. Rollback: revert bản tài liệu có phạm vi.

- M1 — T087-03 sửa phase/scope, T087-04 freshness/boundary. Phụ thuộc M0 và quyền code. Owner role: runtime/security engineer. Giữ task/paths khi CLOSE; map policy operation đúng; invalidate evidence khi source/spec/plan/tasks đổi; xử lý status read-only. Gate: regression âm/dương, review độc lập, xử lý blocker phù hợp. Rollback: revert code có phạm vi và bảo toàn state/evidence.

- M2 — T087-05 hợp đồng risk/RTM, T087-06 STOP/recovery. Phụ thuộc M1 và quyết định schema. Owner role: workflow/data owner. Bắt đầu bằng Markdown; thiết kế native resume/migration trước khi code. Gate: trace đầy đủ, ca interrupted/stale/corrupt state và recovery; rollback bằng backup đã xác minh, không xóa file không rõ ownership.

- M3 — T087-07 nghiên cứu retrieval/mitigation. Phụ thuộc M1; owner role: context/research owner. Benchmark lexical baseline trên tập task cố định, đánh giá relevance, thiếu mandatory policy, latency, context size; chọn hoặc bác AST/vector bằng số liệu. Giữ retrieval hiện tại làm fallback. Chỉ làm song song nếu phạm vi và môi trường cho phép.

- M4 — T087-08 host/platform pilot, T087-09 B.1. Phụ thuộc M1/M2 và M3 nếu áp dụng. Owner role: host/security/QA. Kiểm tra bundle copy độc lập, host mới/cũ, Spec Kit tùy chọn, OS được hỗ trợ, privacy/collision/legacy/rollback. Gate: B1-VAL-01..09 áp dụng có bằng chứng thật; rollback bundle/state tương thích từ bản backup.

- M5 — T087-10 release dossier. Phụ thuộc M4 và quyền phát hành riêng. Owner role: release owner. Đầu ra: version/manifest/exact-source tests/skips/compatibility/residual risk/recovery. Gate: quyết định phát hành của người có thẩm quyền; giữ artifact trước đã kiểm chứng để rollback.

- Không tự gán tên người hoặc ngày hoàn thành. Các role và lịch được chốt tại A.1. M1 ưu tiên rủi ro an toàn cao nhất; môi trường chưa chứng minh containment phải giới hạn hỗ trợ hoặc BLOCK, không gọi là certified.

#### 20.8. Kiểm chứng, adoption và quyết định còn mở

- Kiểm chứng tài liệu: ID/link/source/test symbol đúng, không mâu thuẫn phase, current/historical tách rõ. Việc này không thay A.1.

- Ca runtime cần có: scoped CLOSE; policy theo phase; source/Spec Kit drift; journal corruption/replay; unsafe path; session/collision preservation; retry handoff idempotent; không lộ secret sentinel. Chạy test trên checkout thực và exact-head CI theo từng OS; kết quả lịch sử không được coi là kết quả phiên này.

- Adoption: inventory ownership/version → review collision/legacy → backup/hash → thử trên host disposable → cài đặt đúng phạm vi → smoke/acceptance → handoff. Không auto-migrate session đang hoạt động.

- Quyết định còn mở: người review A.1; owner milestone/security/host; schema native pause/resume và legacy migration; host/OS support matrix; bộ benchmark/budget và chỉ tiêu hiệu năng trước khi chọn kỹ thuật.

- Trạng thái kết thúc bản kế hoạch: M0 documentation prepared; A DESIGN_IN_PROGRESS; A.1 NOT_RUN; M1–M5 PLANNED; B.1 NOT_RUN. Chưa sửa runtime, chưa nghiệm thu host, chưa merge/release. Tài liệu này dùng đồng thời làm BRD sản phẩm và kế hoạch triển khai có truy vết.

### 21. ĐẶC TẢ ĐỀ XUẤT: WEIGHTED MULTI-AGENT DOCUMENT REVIEW

Trạng thái: CHANGE REQUEST / DESIGN PROPOSAL, 13/11/2026. Yêu cầu BR-017..BR-021 bổ sung vào BRD; chưa được A.1 phê duyệt, chưa code hoặc chạy agent fleet. Cần đồng bộ về .agents/.spec.md, .traceMatrix.md, risk/workflow và AGENTS.md ở một thay đổi Git riêng trước implementation. Baseline M0–M5/T087-01..10 không tự động đổi trạng thái.

#### 21.1. Mục đích và phạm vi

Đầu vào: tài liệu BRD/SRS/spec/design, source code hoặc bộ test có quyền truy cập; task review, source revision/hash, domain/system context, n, mode minimal|balanced|deep, budget, rubric và reviewer constraints. Đầu ra: n báo cáo độc lập, bản tổng hợp phản biện và danh mục finding có truy vết. Reviewer không có quyền thực hiện mutation; sửa tài liệu/code cần task, approval và gate riêng.

#### 21.2. Phân loại domain và role catalog

Domain classifier dựa vào evidence trong phạm vi được phép (đường dẫn, nội dung và taxonomy/config), có thể nhận nhiều domain. Với web/software: architect, backend/frontend/full-stack developer, QA/tester, application security, DevOps/SRE; với DA/DE/DS: analyst, ETL/pipeline engineer, database/data quality specialist, ML/DS reviewer, governance/privacy; với tài liệu nghiệp vụ: BA/product, stakeholder/domain expert, UX/accessibility, compliance. Không tạo role giả định khi thiếu domain evidence; lập danh sách UNKNOWN cần xác nhận.

Mỗi role có skill tags, phạm vi kiểm, finding rubric và mức ưu tiên theo artifact. Ví dụ code security-sensitive yêu cầu security+tester; data pipeline yêu cầu DE+data quality; acceptance criteria cần BA+QA. Mandatory coverage do policy/task quyết định, không thể được thay bằng số phiếu của persona khác.

#### 21.3. Persona review và cơ chế chọn n worker

Persona là profile hành vi kiểm tra, được cấu hình và tránh lặp góc nhìn: Skeptical (tìm giả định thiếu), Adversarial (negative cases/abuse), Constructive (khả thi/cải tiến), Pragmatic (chi phí/triển khai), Compliance-first (policy, trace, quy định), Exploratory (tình huống ít gặp). Mỗi worker có đúng một primary role, một primary persona và optional secondary traits. Không dùng nhãn persona làm thước đo độ đúng/sai.

Role-fit score đề xuất S=0.35·E_domain+0.25·E_task+0.15·P_viewpoint+0.15·D_coverage+0.10·A_budget; các thành phần được chuẩn hóa 0..1, trọng số tổng 1.00, cấu hình có version. E_domain: độ phù hợp chuyên môn; E_task: khớp artifact/risk; P_viewpoint: góc nhìn cần bổ sung; D_coverage: lợi ích phủ role/persona còn thiếu; A_budget: khả thi theo token/time/quota. Đây là heuristic thiết kế phải kiểm nghiệm, không phải xác suất tin cậy.

Chọn n bằng bài toán constrained assignment: ưu tiên phủ bắt buộc và độ đa dạng trước tối đa hóa tổng score; hạn chế reviewer trùng vai trò/góc nhìn khi có lựa chọn khác. n do người dùng chọn hoặc auto theo complexity/risk/budget trong config, luôn báo số requested/selected/executed. n=1 gắn LOW_INDEPENDENCE; high-impact review cần độc lập bổ sung hoặc human gate. Nếu không có worker đủ chuyên môn, quyền hoặc budget: GAP/BLOCK, yêu cầu quyết định; không tự giả lập đã có reviewer chuyên gia.

#### 21.4. Workflow orchestration và tính độc lập

R0 REQUEST → R1 SNAPSHOT (scope, policy, owner, source revision/hash) → R2 DOMAIN/RISK CLASSIFY → R3 PLAN (n, role, persona, weight, coverage, cost) → R4 INDEPENDENT REVIEW → R5 SYNTHESIS → R6 INDEPENDENT VALIDATION/HUMAN DECISION → R7 TRACE & HANDOFF. Worker nhận cùng source snapshot, scope có giới hạn, rubric/ID riêng; không xem report worker khác trước khi nộp. Agent tổng hợp không được sửa bằng chứng gốc.

R4 chỉ song song khi host thực sự hỗ trợ nhiều worker và có quyền; nếu không, thực hiện review tuần tự với context isolation khả thi, ghi executionMode=SEQUENTIAL, không tuyên bố là parallel hoặc independent model instance nếu không chứng minh được. Mỗi vòng có timeout, retry policy và partial-result policy. Source drift/policy drift trước R5/R6 buộc kiểm tra và đánh dấu stale những nhận xét liên quan.

#### 21.5. Báo cáo, scoring, tổng hợp và xử lý bất đồng

Worker finding tối thiểu: findingId, reviewId, workerId/role/persona, source locator (section/path/line/revision), claim, evidence quote/ref, category, likelihood 1..5, impact 1..5, severity=L×I, confidence label+reason, reproduction/verification, recommendation, requirement/risk link, limitation. Không đưa suy đoán chưa kiểm tra thành lỗi xác nhận.

Synthesis Agent hợp nhất duplicate theo finding/evidence, liên kết common verified root cause với risk graph, lập agreement/disagreement matrix và đề xuất ưu tiên. Weighted support index (tùy chọn) sử dụng trọng số relevance và evidence quality của từng worker; không lấy persona weight làm lá phiếu thẩm quyền, không coi consensus là ground truth. Giữ nguyên các finding đơn lẻ có chứng cứ, dissent/minority report và unresolved conflicts. Critical blocker theo security/approval được escalate độc lập với support index.

Kết quả synthesis gồm: executive summary; domain coverage; issue register theo priority P0–P3 phù hợp Risk Matrix hiện tại; agreement/conflict ledger; evidence gaps; suggested corrections; RTM impact; residual risks; recommendation PASS_WITH_NOTES / REVISE / BLOCK / INCONCLUSIVE. Đây là recommendation, còn approval do authorized human reviewer; không tự ghi APPROVED.

#### 21.6. Artifact contracts, config và bảo mật

Bộ artifact đề xuất (đường dẫn phải duyệt tại A.1): .agents/.reviews/<review-id>/manifest.md; workers/<worker-id>.md; synthesis.md; issues.md; decision.md. Manifest lưu source fingerprint, role/persona assignment, weights, rubric version, execution mode, costs/budget, status, timestamps và links sang risk/RTM/handoff; reports immutable theo revision, sửa bằng version mới. Handoff giữ Review ID, stage, nguồn, finding unresolved và hành động kế tiếp.

Config đề xuất trong .source/.config/ (schema/version cần thiết kế): review.enabled, review.workerCount, review.maxWorkers, review.selectionWeights, review.roleCatalog, review.personaCatalog, review.mandatoryCoverage, review.budget, review.timeout, review.retry, review.quorum, review.evidenceRules. Không hardcode taxonomy/domain hay weights trong script. User override được phép nếu policy cho phép và lưu lý do; không được tắt Path Guard, mandatory reviewer/gates, redaction hoặc giới hạn quyền.

Đối với file trong repo, Path Guard và Scope IO ràng buộc mọi read/write. Đối với Google Docs qua connector, tuân theo authorization và file scope của connector; Path Guard không được diễn giải thành sandbox bảo vệ mọi thao tác ngoài repo. Nội dung tài liệu, comment và kết quả web/retrieval là dữ liệu không tin cậy, không được biến thành lệnh cho worker. Mỗi worker thấy tối thiểu dữ liệu cần thiết; secret masking, access audit và output redaction phải được kiểm chứng.

#### 21.7. Test strategy, acceptance và risk

AC-REV-01: chọn role đúng theo artifact hỗn hợp (web, data, BRD) và ghi mandatory coverage/gap. AC-REV-02: cấu hình trọng số tổng 1 hoặc reject, cùng snapshot/config cho kết quả phân vai tái lập ở mức assignment (không hứa output LLM deterministic). AC-REV-03: n explicit, budget, quota và n=1 có trạng thái phù hợp. AC-REV-04: n independent reviews có ID, evidence và source locator; missing evidence → UNVERIFIED. AC-REV-05: dedup, minority dissent, conflicting verdict và P0 blocker không bị majority vote xóa.

AC-REV-06: source drift, policy drift, timeout, 1 worker fail, STOP/resume và retry không làm mất provenance, giữ PARTIAL/STALE rõ ràng. AC-REV-07: prompt injection, secret leakage, out-of-repo access và connector access sai phải bị chặn/escalate. AC-REV-08: human reviewer có quyết định riêng với revision/evidence; A.1/B.1 không được tự PASS. AC-REV-09: báo cáo budget/tokens/latency và đo quality/coverage trên benchmark trước khi tuyên bố cải thiện.

Risk mới cần register riêng: false consensus; persona-induced bias; hallucinated evidence; role mismatch; shared-source correlation; cross-worker leakage; stale revision; cost explosion; malicious document instruction; critical finding suppression. Risk scoring theo L×I 5x5 và mandatory blockers ở mục 11/20.6; nhóm root cause có bằng chứng, không xóa ID gốc khi hợp nhất. Việc chưa có runtime là implementation gap, không phải test PASS.

#### 21.8. Tích hợp lifecycle và điều kiện triển khai

Tại A (P3–P8), dùng review để phản biện requirement/design, trace và risk; tại A.1 kiểm tra chất lượng đầu ra và phê duyệt thiết kế. Tại B/VERIFY, review code/test evidence như một lớp bổ trợ, không thay CI/test thực tế; B.1 yêu cầu host pilot, security và stakeholder acceptance. STOP viết checkpoint ở mọi giai đoạn; resume tái xác minh source/config/approval. Mốc triển khai cho BR-017..021 là PROPOSED/TBD, cần task ID, owner, RTM, acceptance plan và risk treatment được phê duyệt trước khi thay code.

### 22. PLAN-088 — KIẾN TRÚC, CHỨC NĂNG VÀ KẾ HOẠCH TRIỂN KHAI S2C THỐNG NHẤT

Trạng thái: DRAFT FOR REVIEW v1.3 (13/11/2026). Baseline phát triển trên Git: nhánh feat/agent-governance-v0.8.0, review thay đổi tại docs/plan-088-unified-s2c. Chưa A.1, chưa triển khai engine Multi-Agent, chưa chạy kiểm chứng B.1, chưa merge hay phát hành. PLAN-088 mở rộng PLAN-087 chứ không tạo thêm một roadmap độc lập.

#### 22.1. Một hệ tài liệu có phân quyền sở hữu

.agents/.spec.md là bản gốc quản trị phát triển, đồng thời là BRD, kiến trúc, hợp đồng chức năng và kế hoạch M0–M5. Google BRD này là bản stakeholder review cùng BR ID và version. .agents/.traceMatrix.md giữ ánh xạ BR/REQ/AC/DES/TASK/RISK/SOURCE/TEST/EVIDENCE; .features.md chỉ giữ trạng thái; .plans.md chỉ giữ progress/historical; .risk.md và .riskMatrix.md giữ lịch sử/risk score; .workflow/ hướng dẫn quy trình, .documents/ chứa thiết kế nghiên cứu chi tiết; AGENTS.md chỉ là luật hướng dẫn AI. Handoff chứa snapshot, không làm tài liệu yêu cầu mới.

Mỗi thay đổi yêu cầu gồm: source/revision/owner → BR/Acceptance Criteria → design/task → risk → source/test/evidence → quyết định và handoff. Nếu Git và Google Docs khác nhau, ghi DRIFT và yêu cầu owner xác nhận; không tự chọn bản mới hơn làm thẩm quyền. Giữ lại tài liệu/handoff cũ, dùng superseded link thay vì xóa dữ liệu khi chưa được cho phép.

#### 22.2. Hợp nhất các chức năng thành một vòng điều khiển

Authorized Intent + host policy → Path Guard/Scope + Discovery/Context → BRD/RTM + Architecture/Feature Design + Technology Policy → Risk Discovery/Research + Risk Management → Optional Multi-Agent Review/Synthesis → A.1 Validation → B Implementation/Verify → Optional Code/Test Review → B.1 Host Acceptance → Handoff/Release decision. Review là một dịch vụ dùng chung, không được thay thế security guard, unit/integration test, approval hoặc quyết định merge/deploy.

Cơ sở đang có: path_guard.py, scope_io.py, policy_resolver.py, scan_infrastructure.py, architecture_tree.py, context_router.py, session_guard.py, handoff_store.py, workflow_guard.py, speckit_bridge.py và mcp_boundary.py. Giữ workflow_guard.py ở 5 runtime phases; 7 business stages và P1–P9 planning đều thuộc lifecycle A→A.1→B→B.1. Chưa có orchestrator multi-agent, native STOP/RESUME hay MCP server; không ghi là đã hoàn thành.

#### 22.3. Thiết kế n reviewer và synthesis (BR-017..021)

R0 yêu cầu → R1 frozen snapshot/scope → R2 phân domain & risk → R3 chọn n roles/personas/weights/budget → R4 independent review → R5 synthesis và dissent ledger → R6 independent validation/human decision → R7 trace/handoff. Role theo domain: software developer/architect/QA/security/DevOps; DA/DE/DS/DB/data quality; BA/product/UX/compliance/domain expert. Persona chọn skeptical/adversarial/constructive/pragmatic/compliance-first/exploratory, chỉ định hướng kiểm tra, không cấp thêm thẩm quyền.

Weight đề xuất: 35% phù hợp domain, 25% nhiệm vụ/artifact, 15% góc nhìn, 15% tăng coverage, 10% ngân sách. Các giá trị được cấu hình và kiểm nghiệm; điều kiện bắt buộc về reviewer phù hợp, quyền truy cập, scope, bảo mật và quota phải được đáp ứng trước khi tối ưu trọng số. n=1 phải báo LOW_INDEPENDENCE. Không có khả năng chạy nhiều worker thì ghi SEQUENTIAL, không bịa n reviewer độc lập.

Mỗi finding có Review ID, worker role/persona, source revision/section, claim, evidence, confidence, risk L×I, links BR/REQ/risk và trạng thái. Agent tổng hợp gộp trùng có chứng cứ, giữ minority dissent, xử lý conflict và không được xóa P0/security/approval blocker theo số phiếu. PASS_WITH_NOTES, REVISE, BLOCK, INCONCLUSIVE chỉ là review recommendation, không phải A.1/B.1 hay human approval.

#### 22.4. Triển khai theo M0–M5 và phụ thuộc

M0 (T088-01/02/03): thống nhất hai bản BRD, AGENTS, RTM, risk/feature, kiến trúc, contract phân vai và A.1 package; chỉ tài liệu và thiết kế. M1 (T087-03/04): ưu tiên sửa Path Guard, phase/scope, source fingerprint và workflow correctness sau khi có quyền code; đây là điều kiện an toàn trước khi triển khai worker engine.

M2 (T087-05/06, T088-04): thống nhất logical review manifest, source fingerprint, risk/trace, STOP/resume and recovery contract, host artifact collision/migration; schema phải có version, test và rollback nếu sau này thay runtime. M3 (T087-07, T088-05/06/07): nếu được phép triển khai, tạo planner theo config, reviewer adapter, synthesis, RTM/risk/handoff integration; so benchmark hiệu quả thực tế, lưu fallback.

M4 (T087-08/09, T088-08/09): pilot host có thực trên software, data và BRD; test negative, security, injection, isolation, budget, drift, Windows/OS, connector access, partial failures và independent B.1 acceptance. M5 (T087-10, T088-10): release dossier theo exact commit/manifest/version/CI/test/skips/risk/residual/rollback, chỉ phát hành khi owner cho phép.

#### 22.5. Kế hoạch kiểm chứng, risk và rollback

A.1 trước code: kiểm tra source authority, tính đo được của AC-REV-01..09, domain-role coverage, cost budget, RTM hai chiều, version policy, threat model, evidence và thiết kế STOP/handoff. B.1 sau code: xác minh bằng test/host thực tế, reviewer độc lập và người có quyền duyệt; thiếu bằng chứng = NOT_RUN/BLOCKED. Risk mới RM-025..033 gồm false consensus, thiếu coverage, sai weight, bịa evidence, leak giữa workers, bỏ dissent/P0, prompt injection, stale/STOP và cost explosion. Giữ nguyên RM-001..024 và chấm theo L×I 5×5; không hạ residual bằng văn bản.

Rollback: bản tài liệu → revert commit có phạm vi; bản runtime tương lai → giữ artifact/bundle trước, backup hash, thử khôi phục trên host disposable, không ghi đè host policy/active session/legacy data. A.1 FAIL quay lại P tương ứng; B.1 FAIL do code quay B, do đổi yêu cầu quay A/A.1; STOP không đóng session hoặc tự triển khai cleanup.

#### 22.6. Quyết định cần chủ sở hữu và trạng thái thực tế

Cần phê duyệt: owner/stakeholder BR-017..021; reviewer A.1/B.1; giới hạn n/maxWorkers và budget; catalog role/persona theo domain; contract/collision cho .agents/.reviews/; schema compatibility; host/OS support; tiêu chí benchmark; phương án hợp nhánh governance với spec2code/InitialVersion_v0. `main` hiện là README-only và các nhánh phát triển phân kỳ, không auto-merge. AGENTS và tài liệu đã được cập nhật trên nhánh docs/plan-088-unified-s2c; review tại https://github.com/RyugaWork/spec2code/pull/9 (DRAFT, chưa merge); runtime và acceptance chưa được thực hiện.

### 23. PLAN-089 — HOÀN THIỆN SRS, INTERFACE CONTRACTS, RTM VÀ HỒ SƠ A.1

Trạng thái: DRAFT v1.4, đang chuẩn bị đánh giá A.1, không phải A.1 PASS hay phê duyệt triển khai B. Nguồn chuẩn trên Git: .agents/.spec.md (mục 15–17) thuộc nhánh docs/plan-089-a1-readiness, kế thừa PLAN-088 và các mốc M0–M5. Google BRD giữ bản stakeholder-facing; tài liệu chuyên trách lưu tình trạng và bằng chứng, không tạo BRD/SRS độc lập.

#### 23.1. A0 → A1: Thống nhất nguồn, đặc tả SRS-01..12

SRS-01 Purpose & scope: S2C là portable Markdown-guided agent skill, hỗ trợ phát triển S2C và repo host dưới giới hạn quyền. Không mặc định yêu cầu MCP, API, database, tự commit/merge/deploy hay thay host AGENTS.

SRS-02 Authority & actors: requester định nghĩa nhu cầu/scope; host owner nắm chính sách host; maintainer sở hữu kế hoạch S2C; technical author viết; QA/security review theo chứng cứ; release owner phát hành. Reviewer persona không tự cấp thẩm quyền. Danh tính người phê duyệt và phạm vi ủy quyền còn UNKNOWN.

SRS-03 Use cases & failures: UC-01 DISCOVER; UC-02 SPECIFY; UC-03 multi-agent REVIEW; UC-04 IMPLEMENT; UC-05 VERIFY/ACCEPT; UC-06 STOP/RESUME; UC-07 Spec Kit tùy chọn; UC-08 HOST INSTALL/RECOVER. Mỗi use case quy định precondition, happy path, error path, authorization boundary và kết quả có thể đánh giá.

SRS-04 FR & states: BR-001..021 là bộ yêu cầu nghiệp vụ hiện tại; F01..37 có trạng thái nguồn riêng, F38..42 là PROPOSED. Review recommendation PASS_WITH_NOTES/REVISE/BLOCK/INCONCLUSIVE không đồng nghĩa A.1/B.1 PASS hoặc được duyệt.

SRS-05 NFR: exact repo scope, security/secret protection, privacy, auditability, source freshness, portability, Windows/OS safety, configurable budget, technology maturity và explicit override. Target định lượng latency/cost/capacity và host support matrix cần owner chốt; không suy đoán SLO.

SRS-06 Interfaces: phân biệt nguồn local Python, connector Google/GitHub, cấu hình, state, trace và review. Đề xuất versioned ReviewManifest, ReviewFinding, ReviewSynthesis; các object này chưa tồn tại trong runtime, không thêm JSON config hoặc thư mục host nếu chưa được duyệt.

SRS-07 Architecture: dùng lại Policy Resolver, Path Guard/Scope IO, Repository/Context Router, RTM, Risk/Research, Session/Workflow/Handoff, Spec Kit Bridge; thêm Review Planner/Worker Adapter/Synthesis khi có quyền. Hạn chế thêm dịch vụ/MCP/database nếu chưa có bằng chứng cần thiết.

SRS-08 Lifecycle: A/P1–P9 → A.1 independent design validation + owner authorization → B five-phase runtime → B.1 host/stakeholder acceptance → release decision. RISK, REVIEW và STOP là cross-cutting; không lén thêm phase vào workflow_guard.py.

SRS-09 Risk/recovery: phân loại L×I 1..5, P0..P3, mandatory security blockers; giữ member risk, nhóm shared cause có bằng chứng, không tự hạ verified residual. STOP ghi thật trạng thái, persistence, source drift và next safe action; native PAUSE/RESUME chưa có.

SRS-10 Verification: test catalogue 42 scenario IDs cho 21 BR (mỗi BR có positive/negative) được thiết kế trong .agents/.workflow/testingAndDelivery.md; RTM Section J ánh xạ hai chiều. Chúng chưa được chạy; kiểm thử thực tế phải ghi SHA, môi trường, log, owner, outcome.

SRS-11 Migration/rollout: host backup/hash, kiểm tra collision/legacy/active sessions, disposable install, platform/adversarial verification và rollback tương thích. Không ghi đè host state, không tự xóa. Windows junction/OneDrive/TOCTOU vẫn cần chứng cứ kiểm nghiệm.

SRS-12 Decisions: thống nhất master và Google BRD, bảo toàn Spec Kit/host ownership, worker review là lựa chọn không tự phê duyệt. Còn chờ owner, review budget, n/maxWorkers, quorum, schema compatibility, host support, exact branch integration, A.1 signoff.

#### 23.2. A2: Hợp đồng module và dữ liệu

Luồng giao tiếp thống nhất: Request → Policy & Scope → Context Snapshot → Requirements/RTM/Architecture/Risk → Optional Review Planner → Worker Findings → Synthesis → Risk/RTM/Handoff → A.1/B.1 Human Gate. Các interface cần input provenance, source/config fingerprint, output owner, negative result và migration strategy. Mọi review chạy trên source snapshot; worker không đọc bản nháp của worker khác nếu tuyên bố độc lập; mọi dissent và P0 blocker được bảo toàn.

Contract đề xuất: ReviewManifest gồm reviewId, schemaVersion, sourceFingerprint, policy/configFingerprint, requestedN, effectiveN, executionMode, coverage/weights, budget, worker IDs và status; ReviewFinding gồm role/persona, locator, sourceRevision, claim, evidence, confidence, risk/requirement refs; ReviewSynthesis gồm raw-finding mapping, conflict/dissent ledger, mandatory blockers và humanDecisionRef (có thể null). Tất cả chỉ là schema thiết kế chờ duyệt.

#### 23.3. A3: Traceability, test specification và acceptance

21 BR đã được gắn với 42 test scenario dự kiến: TC-S2C-BR001-P/N đến TC-S2C-BR021-P/N. Từng scenario có positive/negative, precondition, expected decision/evidence và milestone. Đây là test design, không phải 42 test script hoặc 42 PASS. Riêng BR-017..021 phải bao phủ normalized weights, thiếu expert/role, n=1, quota, evidence hallucination, prompt injection, partial worker, minority dissent P0, STOP/retry, source/policy drift và independent approval.

#### 23.4. A4 → P9: Risk, handoff và điều kiện A.1

Giữ nguyên RM-001..024 và RM-025..033, R74..82 mới. Không giảm điểm residual vì viết tài liệu. P089-00..05 lần lượt: nguồn chuẩn → SRS 12 phần → interface contract → test/RTM → risk/handoff → hồ sơ đánh giá A.1. A.1 gồm A1-VAL-01..09, cần reviewer độc lập và owner thật; tự đánh giá consistency chỉ là PREFLIGHT_ONLY. Với các yêu cầu còn UNKNOWN/OWNER_MISSING hoặc critical risk chưa phê duyệt, ghi BLOCKED/NEEDS_REVIEW và không khởi động B.

#### 23.5. Các mốc B/M1–M5 và điều kiện dừng

M0: tài liệu, RTM, governance và A.1 package. M1: vá scope/Path Guard/workflow correctness và chạy regression khi được phép. M2: data trace, sessions, STOP/resume contract, risk. M3: code planner, worker adapter, synthesis và đo benchmark (chỉ sau M1/M2 + A.1 + quyền B). M4: pilot host thực tế, security, OS, connector, B.1. M5: release dossier/rollback và release owner decision. Không được tự merge PR, sửa runtime hoặc tự ghi PASS chỉ vì tài liệu đã soạn.

Bản Git cho nội dung chi tiết: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.spec.md ; Planned test catalogue: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.workflow/testingAndDelivery.md ; RTM: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.traceMatrix.md . PR giai đoạn: https://github.com/RyugaWork/spec2code/pull/10 (DRAFT; chưa merge). Handoff: .agents/.handoffs/plan-089-a1-readiness-handoff.md. Trạng thái A.1: NOT_RUN, B: NOT_AUTHORIZED.

### 24. PLAN-091 — REMEDIATION SAU REVIEW A.1 (BẢN THIẾT KẾ)

PLAN-091 xử lý 10 findings REV-090-01..10 từ PLAN-090 technical preflight. Nguồn review gốc giữ nguyên tại Git commit 1dae9338f4d38518e897212cdf80ba47239a7671 (PR #10 trước sửa). Review 6 góc nhìn do một mô hình thực hiện tuần tự; không có 6 agent độc lập, không có human independent signoff và không được xem là A.1 PASS. Nhánh thực hiện sửa tài liệu: docs/plan-089-a1-readiness. Giữ một nguồn chuẩn .agents/.spec.md, không mở BRD/SRS song song.

#### 24.1. R1 — Sửa định dạng và mã tham chiếu đặc tả

Đã chuẩn hóa A1-VAL-01..09 trong SRS-10 và loại bỏ 160 ký tự escape backtick sai tại phần SRS-01..12 / interface. Đây là SOURCE_TEXT_REPAIRED, không có nghĩa cả tài liệu được nghiệm thu hoặc code đã chạy.

#### 24.2. R2 — Đặc tả acceptance và requirements traceability

Cả 42 test case kế hoạch TC-S2C-BR001-P/N đến TC-S2C-BR021-P/N nay có preconditions/partitions, thao tác, expected observable result, evidence và giai đoạn. Tất cả DESIGNED/NOT_RUN, chưa có test fixture được phê duyệt, chưa chạy trên host. RTM Section K liên kết REV-090-01..10 với BR, TC, risk và quyết định DEC-091. Không gán PASS dựa trên độ đầy đủ câu chữ.

#### 24.3. R3 — ReviewManifest, WorkerFinding, Synthesis, STOP & Recovery

Master BRD SRS Section 18 xác định contract logic (chưa phải JSON runtime) cho ReviewRequest, SourceSnapshot, ReviewManifest, WorkerAssignment, ReviewFinding, ReviewSynthesis; tách executionMode thực sự (host-native isolated workers) khỏi SINGLE_MODEL_SEQUENTIAL. Các trạng thái PARTIAL/STALE/BLOCKED/STOPPED_NOT_PERSISTED và quy tắc giữ nguyên minority P0, secret redaction, source/config/policy fingerprint, provenance và hard constraints được định nghĩa. Worker không thể tự cấp quyền, tự nhận independent approval hoặc làm thay A.1/B.1. Quorum, n tối đa, budget/token/time và output namespace còn cần người sở hữu chốt.

#### 24.4. R4 — Decision register, risk và dependency

DEC-091-01..10 yêu cầu chủ thể phê duyệt: BR/AC owners, host/security/policy scope, hỗ trợ Windows/OS, domain role/quorum, benchmark token/cost/latency, privacy và vị trí lưu output, fixture/QA acceptance, merge baseline, độc lập A.1, B/B.1/release. Mỗi ô UNKNOWN là việc phải xác nhận bằng bằng chứng, không được tự đặt mức định lượng tùy ý. RM-001..033 giữ nguyên mức rủi ro và verified residual UNKNOWN; M1 Path Guard và workflow safety vẫn phải xử lý bằng source/tests sau A.1 và explicit B authority, trước M3 worker runtime.

#### 24.5. Trạng thái và nguồn tra cứu

Technical remediation: DOCUMENTATION_UPDATED, pending review of exact new Git+Google revision. Formal A.1: NOT_RUN; B: NOT_AUTHORIZED; B.1: NOT_RUN; host tests/worker runtime: NOT_RUN/NOT_IMPLEMENTED. PLAN-090 review report remains immutable and pinned to pre-fix commit. Các tài liệu chính: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.spec.md ; Test catalogue: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.workflow/testingAndDelivery.md ; RTM: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.traceMatrix.md ; Technical review: https://github.com/RyugaWork/spec2code/pull/11 ; Source update PR: https://github.com/RyugaWork/spec2code/pull/10 .

### 25. PLAN-092 — TÍCH HỢP GITHUB SPEC KIT ĐỂ PHÁT TRIỂN CHÍNH S2C

Phiên bản DRAFT v1.5. Mục tiêu: sử dụng Spec Kit làm quy trình đặc tả theo feature của S2C; ChatGPT Web có thể cập nhật Markdown qua GitHub và coding agent trong Codespaces/Codex có thể chạy CLI/skill chính thức sau khi cài đặt và kiểm chứng. Không thay thế S2C Governance, Path Guard, Requirements Traceability, Risk Management hoặc A.1/B.1.

#### 25.1. Phạm vi tích hợp và nguồn tài liệu chuẩn

Đã thêm .specify/memory/constitution.md (DRAFT, chưa RATIFIED), .specify/feature.json (feature_directory = specs/001-s2c-speckit-integration), cùng spec.md, plan.md, tasks.md và checklist của feature đầu tiên. Root AGENTS.md và .agents/.spec.md vẫn là nguồn quản trị/yêu cầu S2C; Constitution chỉ bổ trợ workflow feature. Không sao chép BRD/SRS vào feature, không tự ghi đè AGENTS host. Một branch Git có thể làm nhiều feature; feature hiện hành được xác định bởi feature.json chứ không phải tên branch.

#### 25.2. Chế độ Web/GitHub

ChatGPT Web đọc và sửa tài liệu Spec Kit qua GitHub connector trong phạm vi đã cho phép: đọc AGENTS, master BRD/SRS, Constitution, active feature; phân tích, Clarify, Specify, Plan, Tasks và review bằng nội dung Markdown. Kết quả ghi exact branch SHA, nguồn và trạng thái. Không thể coi việc viết tài liệu trên GitHub là đã chạy CLI, script Python, Codex skill hoặc đa-agent độc lập. Có thể thực hiện STOP/handoff mà không đóng machine Workflow Guard session.

#### 25.3. Chế độ native CLI và coding-agent

Cài chính thức specify-cli trong Codespaces/Codex hoặc môi trường đã cấp quyền ở bản checkout dùng thử có backup; chọn phiên bản phát hành ổn định sau đánh giá maturity/compatibility (không mặc định chọn phiên bản vừa GA). Theo quy trình existing project: dùng specify init --here --force --non-interactive --integration <approved-key> --script py, kiểm tra trước các đường dẫn bị ghi đè và diff tạo ra. Chỉ công nhận native CLI/skill khi có specify version, file scripts/skills và bằng chứng chạy thực tế. Các tệp được khởi tạo trong lần này là native-compatible Markdown bootstrap; chưa chạy specify init và chưa cài upstream scripts/templates/agent skills.

#### 25.4. Tích hợp S2C bridge, RTM, risk và bảo mật

speckit_bridge.py và .source/.config/speckit.json hiện có vẫn là read-only adapter: nhận feature pointer, kiểm tra sự tồn tại/kích thước/hashes của spec.md/plan.md/tasks.md và trả số lượng task IDs, không trích xuất nội dung hoặc tự cấp quyền triển khai. Đã ánh xạ SKI-FR-001..012 tới BR-003/004/005/010/012/014/015 và S2C-REQ/NFR qua RTM Section L. Risk SK-R01..06 đề cập ghi đè init --force, sai feature pointer, vượt quyền, phiên bản, drift và false independence; các rủi ro P0 cũ giữ nguyên.

#### 25.5. Kiểm tra hiện trạng và gate

SK-01/02: đã tạo native-compatible feature artifacts và liên kết với AGENTS/BRD/RTM/risk. Static GitHub preflight tại commit ebdbd03f027a8e65ce5cde8ddc5ea0af5a1cad14: feature.json hợp lệ, đủ spec.md/plan.md/tasks.md, T001..T015 không trùng và 171 link Markdown nội bộ được kiểm tra không thiếu. Sau đó đánh dấu T001..T005 là công việc bootstrap tài liệu đã xong. Đây không phải chạy Python/CLI hay kiểm thử host. SK-03 native installation NOT_RUN; A.1 NOT_RUN, B NOT_AUTHORIZED, B.1 NOT_RUN. Không merge/deploy/CI trong giai đoạn này.

GitHub nguồn chuẩn: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.spec.md ; Hướng dẫn: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.specify/README.md ; Feature: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/specs/001-s2c-speckit-integration/spec.md ; Tasks: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/specs/001-s2c-speckit-integration/tasks.md .

### 26. PLAN-093 — SK-03: KIỂM TRA VÀ CHUẨN BỊ CÀI SPEC KIT NATIVE

Giai đoạn này tiếp nối PLAN-092, nhằm đưa Spec Kit chính thức vào môi trường chạy lệnh Codex/Codespaces với đầy đủ bảo toàn tài liệu S2C. Trạng thái hiện tại PILOT_PREPARED / NATIVE_NOT_RUN. Không tự tạo Git branch, không sửa Python runtime, không CI/CD và không coi đây là A.1 hoặc B.1.

#### 26.1. Đối chiếu phiên bản upstream và yêu cầu vận hành

Đã kiểm tra release GitHub Spec Kit v1.2.6 phát hành 02/11/2026 làm ứng viên chạy thử trong bản checkout tạm; bản v1.4.0 phát hành 10/11/2026 có thay đổi bảo mật file/URL mới cần đánh giá trước khi chọn phiên bản triển khai chính thức. v1.2.6 yêu cầu Python >=3.11, hỗ trợ --here, --force, --non-interactive, --integration codex và --script py; Constitution hiện có được nhánh xử lý khởi tạo của upstream giữ nguyên theo source, nhưng các file quản lý khác có thể bị ghi đè. Đây là kiểm tra mã nguồn và release metadata, chưa phải kiểm chứng thực thi.

#### 26.2. Kết quả thử nghiệm môi trường

Môi trường terminal có Git 2.47.3, Python 3.13.5 và uv, nhưng không cài specify-cli và không phân giải tên miền GitHub/PyPI. Lệnh uvx --offline --from git+https://github.com/github/spec-kit.git@v1.2.6 specify version thất bại exit code 1 do không thể lấy Git dependency. Vì vậy KHÔNG có kết quả specify version, specify init, scripts/skills Codex hay acceptance test native. Không nâng trạng thái T007..T009 lên Pass.

#### 26.3. Quy trình cài đặt thử an toàn

Đã ghi runbook GitHub riêng cho Linux/Codespaces và PowerShell: kiểm tra clean Git HEAD; tạo detached worktree trong thư mục dùng thử; ghi hash feature.json, Constitution và AGENTS; cài/chạy CLI được ghim phiên bản sau khi có môi trường và quyền phù hợp; so sánh toàn bộ git status/diff và liệt kê generated files; chạy official check_prerequisites.py đối với feature hiện hành; chỉ đưa file được chủ sở hữu duyệt trở lại nhánh S2C. Tuyệt đối không chạy specify init --force trên nhánh phát triển hoặc tự xóa worktree nếu có dữ liệu chưa xác minh.

#### 26.4. Quyết định và gate tiếp theo

T006: đã nghiên cứu phiên bản ứng viên, chưa được chủ sở hữu phê duyệt. T007–T009: BLOCKED_BY_RUNNER_NETWORK/NOT_RUN. T010–T015: chưa có A.1 độc lập, quyền B, test host và B.1. Giữ các rủi ro Path Guard, workflow và file collision chưa được giảm mức. Tài liệu kỹ thuật: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.documents/specKitNativePilot.md ; feature tasks: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/specs/001-s2c-speckit-integration/tasks.md .

### 27. PLAN-094 — HOÀN THIỆN SPEC KIT FEATURE VÀ KIỂM TRA TĨNH

PLAN-094 tiếp tục SK-03 trong phạm vi không cần thay đổi Python runtime hay cài CLI chính thức. Đây là phần hoàn thiện feature artifacts và đối chiếu tài liệu đang ở trạng thái DRAFT / A.1 NOT_RUN, không phải đã nghiệm thu hay triển khai mã nguồn.

#### 27.1. Hoàn chỉnh feature-level Spec Kit artifacts

Đã bổ sung research.md (nguồn upstream/phiên bản và lựa chọn kiến trúc), data-model.md (logic source/feature/task/evidence và trạng thái), quickstart.md (chế độ ChatGPT Web và Native Codex/Codespaces), contracts/web-native-interface.md (quyền, dữ liệu vào/ra, STOP/RESUME) và checklists/integrationAcceptance.md (24 planned cases). Không tạo database, JSON runtime mới, daemon, CI hoặc thêm branch.

#### 27.2. Tuân thủ template và requirements trace

Feature spec.md có thêm Success Criteria, Assumptions, Key Entities, User Scenarios & Testing; plan.md có Technical Context, Constitution Check, Project Structure và Complexity Tracking. RTM Section L đã thay mã shorthand bằng 12 hàng SKI-FR-001..012 riêng biệt; từng yêu cầu ánh xạ hai testcase SKI-TC-xxx-P và SKI-TC-xxx-N. Test case hiện chỉ ở trạng thái DESIGNED/NOT_RUN.

#### 27.3. Kết quả static repository inspection

Kiểm tra nguồn GitHub tại commit a45c7db2162ef8e6683b20bb1d9b8e97918f019d: feature pointer JSON hợp lệ và chỉ đúng thư mục trong repo; 12 unique SKI-FR, 12 RTM rows, 24 test case IDs không trùng, 15 task IDs không trùng, 137 liên kết Markdown nội bộ trong 13 file được kiểm tra có 0 liên kết thiếu. Các mục Success Criteria/Assumptions, Technical Context/Constitution Check/Project Structure/Complexity Tracking hiện diện. Đây không phải chạy speckit CLI, S2C Python test suite hay an ninh host.

#### 27.4. Giới hạn, risk và bước tiếp theo

Native CLI vẫn bị chặn bởi terminal không có specify-cli và không có DNS/Internet để tải từ GitHub. Ứng viên v1.2.6 chỉ phù hợp để thử trong checkout dùng thử sau khi được chấp thuận; v1.4.0 có các hardening mới cần xét. RM-001..005, risk ghi đè --force, quyền A.1, phê duyệt B và B.1 chưa được đóng. Tiếp theo cần host Codespaces/Codex có mạng, owner-approved version, detached-worktree pilot và evidence exit/hash/diff; không tự merge hay quảng bá kết quả thành PASS. Source: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/specs/001-s2c-speckit-integration/ ; RTM: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.traceMatrix.md .

### 28. PLAN-095 — WEB MODE KIỂM CHỨNG THỰC TẾ & CHẶN NATIVE IMPLEMENT

PLAN-095 tiếp tục tích hợp Spec Kit mà không thay mã nguồn runtime/CI và không tạo nhánh Git mới. Nhánh đang làm việc: docs/plan-089-a1-readiness, PR #10 Draft. Nội dung vừa bổ sung quy tắc an toàn cho native agent, vừa thực thi những ca kiểm thử có thể kiểm chứng trực tiếp trên GitHub Web Connector.

#### 28.1. Phát hiện giới hạn của upstream Spec Kit

Từ template commands/implement.md tại tag GitHub Spec Kit v1.2.6: khi checklist chưa đủ, implement có thể dừng và hỏi người dùng có muốn tiếp tục không. Phản hồi đồng ý ở bước đó không được coi là A.1 độc lập, quyền B sửa mã nguồn, an toàn Path Guard hay B.1 của S2C. Các task T011 (phê duyệt A.1), T012 (phê duyệt B) và T015 (B.1/release) không được coding agent tự đánh dấu hoàn thành. T001..T015 đã gắn user story [US1]..[US4] mà không đổi mã ID.

#### 28.2. Quy trình Web Mode và nguồn quản trị

Đã có tài liệu .agents/.workflow/specKitWebWorkflow.md cho tiến trình Constitution, Specify, Clarify, Checklist, Plan, Tasks, Analyze theo các thao tác Markdown/GitHub connector có cấp quyền và ghi commit SHA. Nhiều lần update_file qua GitHub không phải transaction nguyên tử, nên nếu lỗi giữa chừng phải ghi PARTIAL_PERSISTENCE và bàn giao lại. .agents/.workflow/specKitNativeExecutionGate.md xác định gate native: chỉ được Implement/Converge khi có phê duyệt A.1, B theo từng phạm vi và bằng chứng host thực. Đây là quy tắc tài liệu, chưa có hook runtime chặn tool call.

#### 28.3. Kết quả thực thi Web/Static trên GitHub

Có 4/24 ca đạt PASS trong phạm vi GitHub Web/Static, 20 ca NOT_RUN. SKI-TC-001-P: feature.json hợp lệ; SKI-TC-003-P: có đủ artifact và 15 task ID khác nhau tương thích với regex nguồn S2C; SKI-TC-004-P: đã cập nhật một file quickstart.md qua GitHub và kiểm tra lại đúng 1 commit/1 file/blob SHA/HEAD; SKI-TC-006-P: 12 yêu cầu feature khớp 12 RTM mapping và 24 case IDs không trùng. Nguồn kiểm tra được ghim tại Git SHA 916ed6aa769e1fb9c25d9bd988277275613ae695; phép sửa file đi từ commit 1709037a6975b846478e80151d129fb486a. Bằng chứng: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.documents/specKitWebModeEvidence095.md . Các ca PASS không chứng minh an toàn host, native CLI hoặc phê duyệt A.1/B.1.

#### 28.4. Trạng thái và tồn đọng

A.1 vẫn NOT_RUN, B NOT_AUTHORIZED, B.1 NOT_RUN, Spec Kit native CLI/skills chưa cài, các phép thử chặn checklist, symlink/junction và path guard vẫn NOT_RUN. 8 tình huống kiểm thử SK95-GATE-01..08 chỉ ở trạng thái DESIGNED. RM-001..005 và rủi ro native checklist bypass vẫn OPEN, chưa hạ mức. Tiếp theo cần review độc lập trên Git SHA mới nhất và host Codex/Codespaces có mạng để thực hiện đúng các kiểm tra native/OS, trước mọi yêu cầu merge hoặc phát hành.

Tham chiếu: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.workflow/specKitNativeExecutionGate.md ; https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.workflow/specKitWebWorkflow.md ; https://github.com/RyugaWork/spec2code/pull/10 .

### 29. PLAN-096 — ĐỐI CHIẾU MÃ NGUỒN SPEC KIT BRIDGE VÀ THIẾT KẾ NEGATIVE TEST

Đây là lượt kiểm tra tĩnh trên mã nguồn thật của S2C từ GitHub commit 72920032a892b8a60c74fbdf2b62847fb5fa771d. Đã commit một đợt cập nhật gồm 8 file Markdown tại 663d0440db321ea99942711f6bcba9a64d1583fa trên nhánh docs/plan-089-a1-readiness. Không sửa Python, JSON hoặc CI; không mở branch mới, không merge. Dự án vẫn Draft, A.1 NOT_RUN, B NOT_AUTHORIZED và B.1 NOT_RUN.

#### 29.1. Bốn điểm không đồng nhất giữa source và requirement

SK96-01: hàm _feature_path() kiểm tra giới hạn nằm trong repo nhưng không bắt buộc thư mục nằm trong specs/<feature-id>; cần quyết định hợp đồng đối với override. SK96-02: json.loads cho feature.json không bật cơ chế từ chối duplicate keys. SK96-03: các file bắt buộc có kích thước 0 vẫn được nhận là tồn tại theo điều kiện is_file/exists. SK96-04: task ID được trích xuất và đếm nhưng không kiểm tra trùng lặp. Đây là phát hiện từ mã nguồn, chưa phải lỗi runtime hay security exploit đã tái hiện.

#### 29.2. Bằng chứng hỗ trợ và negative cases

Có thử nghiệm riêng bằng thư viện chuẩn Python trên thư mục tạm: JSON trùng khóa dùng giá trị xuất hiện cuối; file 0 byte vẫn is_file() bằng True; regex task nhận hai lần T001. Đây chỉ là thử nghiệm ngữ nghĩa Python chứ không chạy S2C bridge. Đã lập SK96-NEG-01..04, ánh xạ từng trường hợp vào SKI-FR, RTM Section N và risk SK-R08/09. Cả bốn negative cases vẫn NOT_RUN. Bộ 24 feature test case trước đó giữ nguyên 4 PASS giới hạn Web/static và 20 NOT_RUN; không cộng nhầm bốn negative mới vào số case đã PASS.

#### 29.3. Hướng xử lý và điều kiện nghiệm thu

Cần chủ sở hữu quyết định policy cho thư mục specs/ và override, quy tắc duplicate JSON keys, file rỗng/whitespace và task ID trùng trước khi sửa guard. Sau A.1 độc lập và B cụ thể, mới được sửa Python/config/test theo scope, chạy bảy unit test có sẵn cùng bốn negative tests mới trong checkout thật với module Path Guard và Scope IO nguyên bản. Trên Windows/OneDrive/junction cần kiểm tra riêng, ghi SHA, OS, kết quả thực tế, stdout/stderr, exit code và hash sentinel. Không dùng mock guard thay cho security test.

#### 29.4. Nguồn kiểm tra và trạng thái còn mở

Audit source: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.documents/specKitBridgeSourceAudit096.md ; Feature acceptance: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md ; Handoff: https://github.com/RyugaWork/spec2code/blob/docs/plan-089-a1-readiness/.agents/.handoffs/plan-096-bridge-source-audit-handoff.md . Native Spec Kit CLI chưa cài/chạy do thiếu kết nối mạng trong terminal. RM-001..005 và các risk liên quan chưa được nghiệm thu giảm thiểu.

### 30. PLAN-097 — KIỂM SOÁT BIẾN MÔI TRƯỜNG KHI CHẠY SPEC KIT NATIVE

Đối chiếu mã nguồn chính thức GitHub Spec Kit v1.2.6 và v1.4.0 cho thấy upstream dùng cùng cơ chế tìm feature từ .specify/feature.json hoặc SPECIFY_FEATURE_DIRECTORY. Khi đặt biến override mà không đặt SPECIFY_FEATURE_NO_PERSIST=1, common.py có thể ghi lại .specify/feature.json. Đây là tác dụng phụ có thật trong đường đi mã nguồn, nên không được tự gọi là thao tác đọc thuần túy.

#### 30.1. Phân biệt Path Guard của S2C và upstream Spec Kit

Hàm get_feature_paths trong upstream cho phép giá trị SPECIFY_FEATURE_DIRECTORY là đường dẫn tuyệt đối, không thực hiện kiểm tra phạm vi repo như S2C path_guard.py. setup_plan.py dùng feature_dir.mkdir và impl_plan.write_bytes; khi có override trỏ ra ngoài repo, hành vi có nguy cơ tạo hoặc ghi file ngoài checkout. Đây là rủi ro thiết kế xác nhận qua source, chưa được tái hiện bằng bài test trên một host native.

#### 30.2. Quy tắc tích hợp an toàn và vận hành thử

Trong mọi lần preflight đọc/kiểm tra, xóa SPECIFY_FEATURE và SPECIFY_FEATURE_DIRECTORY khỏi môi trường tiến trình, đặt SPECIFY_FEATURE_NO_PERSIST=1, kiểm tra feature.json bằng chính sách S2C (giới hạn specs/<id>, không path traversal, symlink/junction, kiểm tra quyền và nguồn). Chỉ chạy các lệnh upstream có khả năng ghi như setup_plan, init, tasks hay implement trong detached worktree được cấp quyền với hash trước/sau, diff và allowlist file. SPECIFY_FEATURE_NO_PERSIST chỉ ngăn ghi con trỏ feature, không phải sandbox đường dẫn cho tất cả script.

#### 30.3. Test plan và trạng thái nghiệm thu

Các ca mới đề xuất SK97-NEG-01: override trỏ ngoài repo bị từ chối trước khi chạy; SK97-NEG-02: biến override hợp lệ có no-persist không làm thay đổi hash pointer; SK97-NEG-03: không dùng no-persist thì nhận diện tác dụng phụ và không chấp nhận chạy trong read-only mode; SK97-NEG-04: từ chối symlink/junction và không ghi sentinel ngoài repo; SK97-NEG-05: setup_plan chỉ được thử trên detached worktree, phát hiện diff/generator collision. Tất cả NOT_RUN; chúng là ca bổ sung, không thay đổi tổng số 24 case feature (4 PASS giới hạn Web/static, 20 NOT_RUN).

#### 30.4. Quyết định còn mở

Rủi ro mới SK-R10 là rò rỉ phạm vi thực thi do upstream native không kế thừa Path Guard của S2C. Cần lựa chọn phiên bản, môi trường thử, chính sách override và phê duyệt A.1/B theo đúng thẩm quyền. Chưa cài Spec Kit CLI, chưa gọi upstream script trên host thật, chưa sửa Python/JSON/CI và chưa merge PR. Mã nguồn đối chiếu: https://github.com/github/spec-kit/blob/v1.2.6/scripts/python/common.py và https://github.com/github/spec-kit/blob/v1.2.6/scripts/python/setup_plan.py .

### 31. PLAN-098 — TÍCH HỢP CHỨC NĂNG VÀ KIẾN TRÚC TÁI SỬ DỤNG

- Bổ sung bản tóm tắt stakeholder cho thiết kế trên GitHub: F01–F42 là danh mục hiện trạng/đã đề xuất trước đó; F43–F64 gồm 22 mã thiết kế mới và quan hệ tới các module governance, source graph, context routing, Path Guard, workflow, Spec Kit, quality và multi-agent review. Nguyên tắc là mở rộng module hiện có, không tạo hệ thống thực thi trùng lặp. F43–F64 ở trạng thái DESIGN_PROPOSED, chưa phải tính năng đã code hoặc được nghiệm thu.

- Phạm vi tài liệu chuẩn: .agents/.spec.md là BRD/SRS/architecture cơ sở; .agents/.documents/featureDesign.md giữ design matrix; .agents/.traceMatrix.md giữ đối chiếu; .agents/.riskMatrix.md giữ điểm rủi ro; .agents/.workflow/testingAndDelivery.md quản lý ca kiểm tra. Google BRD này là bản tóm tắt cho stakeholder, không phải một bộ SRS thứ hai.

### 32. PLAN-099 — TRÌNH TỰ XÂY DỰNG VÀ ĐIỀU PHỐI AGENT

- Kiến trúc theo lớp L0–L7: khảo sát/tài liệu → A.1 độc lập → nền tảng an toàn Path Guard và Workflow Guard → truy vết/provenance → Spec Kit/provider integration → multi-agent review → nghiệm thu host → triển khai. Mỗi task ghi nhận 9 công đoạn DISCOVER, PLAN, RISK MANAGEMENT, IMPLEMENT, TEST, VERIFY, OPTIMIZE, HANDOFF, DOCUMENT. Runtime hiện tại chỉ có 5 machine phases; không tự ý thêm trạng thái PAUSE/RESUME vào code. Mọi hoạt động thực thi có giới hạn số vòng, thời gian, quyền và chi phí.

- Nguyên tắc đồng thời: chỉ một integrator được ghi mã và commit vào source chuẩn; worker review có thể chạy độc lập khi thật sự tồn tại môi trường tách biệt. Nếu dùng một mô hình xem xét qua nhiều góc nhìn, phải gọi là sequential analytical lenses, không được giả định đó là nhiều reviewer độc lập. Handoff phải tồn tại trước khi đổi task; cấm xóa các bản lịch sử hoặc file thuộc host.

### 33. PLAN-100 — ĐIỀU KIỆN SẴN SÀNG ĐỂ CODE

- PLAN-100 đã tạo blueprint từ L0 đến L7, test thiết kế L1-WF01..04 và L1-SC01..03 cho lỗi workflow/Path Guard. Kết quả thiết kế F43–F64 gồm 44 ca dự kiến, toàn bộ DESIGNED / NOT_RUN. Rủi ro critical gồm Path Guard Windows, workflow phase/scope/freshness, dữ liệu, quyền owner và an toàn gọi tool. Rủi ro không tự giảm vì cập nhật tài liệu.

- Cổng A.1 độc lập chưa chạy, B chưa có ủy quyền riêng và B.1 chưa chạy. Các nhiệm vụ native Spec Kit T011, T012, T015 để nguyên chưa đánh dấu. Lịch sử thử Codex 0.169.0-alpha.11.1 trên Windows: tùy chọn codex exec --full-auto --sandbox workspace-write bị CLI từ chối với exit 2; một read-only probe khác lỗi khởi tạo state DB/app-server exit 1. Không có bằng chứng thực thi thành công Codex, Gemini MCP, Spec Kit native hoặc sandbox host từ các lần thử này.

### 34. PLAN-101 — CỘNG TÁC CODEX VÀ GEMINI/ANTIGRAVITY QUA MCP

- Thiết kế dùng Codex làm người thực hiện ghi code/tài liệu và build/test trong giới hạn đã duyệt; Gemini/Antigravity là nguồn phân tích ngữ cảnh và review read-only tùy chọn. S2C kiểm soát thứ tự task, phạm vi, ngân sách và kết quả handoff. MCP là kênh truyền tool, không tự đảm bảo an toàn; việc xác minh package, tài khoản, tool list, quyền đọc/ghi, secret redaction và OS sandbox là bắt buộc trước khi có tác vụ thực tế.

- Đã đưa 12 yêu cầu kỹ thuật dự thảo MM-REQ-001..012, 12 ca dự kiến MM-TC-01..12 (toàn bộ NOT_RUN), và sáu rủi ro đề xuất RM-047..052 mức P0 vào tài liệu GitHub. Chế độ Manual/Safe Auto có thể được đặc tả ở Phase A; Sandbox Auto và Full Auto cần phê duyệt bảo mật/host riêng, giới hạn loop, timeout, token, process, quota, checkpoint và không sử dụng YOLO ngoài sandbox. Các cổng này không được một agent tự phê duyệt.

### 35. PLAN-102 — HOÀN TẤT BẢN THẢO TÀI LIỆU VÀ HỒ SƠ A.1

- PLAN-102 tập hợp các quyết định kiến trúc ADR-102-01..08 (đều đang PROPOSED), liên kết thành một architecture/requirements/workflow/risk/test package, bổ sung fixture cho L1-WF/SC và giao thức review A1-VAL-01..09. Hồ sơ A.1 ghi bằng chứng hiện có và các giới hạn, không phải A1_PASS. Bản thiết kế có thể ở mức AUTHORING_COMPLETE_CANDIDATE sau khi kiểm tra đường dẫn và bàn giao.

- Hành động còn bắt buộc từ owner: (1) chốt những BR/AC áp dụng, gồm BR-022..027 hiện còn candidate; (2) xem khác biệt giữa nguồn Git và bản mirror Google rồi chấp thuận revision phù hợp; (3) quyết định P0 risk, phạm vi chia sẻ dữ liệu, host Windows/Linux, budget và quyền; (4) chỉ định reviewer A.1 thực sự độc lập trên đúng cặp revision; (5) cấp ủy quyền B riêng cho code sau A.1; (6) nghiệm thu B.1 sau có kết quả thực thi. Mọi nội dung này chưa được coi là đã ký duyệt.

- Nguồn Git bản thảo tại thời điểm bổ sung: https://github.com/RyugaWork/spec2code/blob/cc99d97a249fc29242fd0d876463b86b5b4afa10/.agents/.spec.md . Nhánh docs/plan-089-a1-readiness, PR #10 Draft. Đây là mirror summary mang trạng thái DRAFT / OWNER REVIEW REQUIRED, không tự động hợp nhất hoặc thay thế tài liệu Git và không làm thay đổi quyền A.1/B/B.1.

### 36. PLAN-103 — KIỂM TRA KỸ THUẬT TÀI LIỆU VÀ KHẮC PHỤC MÂU THUẪN

- Đã thực hiện review kỹ thuật theo sáu góc nhìn (business, architecture, QA, security, traceability và operations) nhưng do một mô hình đánh giá tuần tự; không có sáu worker độc lập hoặc chữ ký nghiệm thu A.1. Phạm vi review Git tại https://github.com/RyugaWork/spec2code/tree/docs/plan-089-a1-readiness và bộ tài liệu PLAN-085/098/100/102.

- REV-103-01 (P1): bảng nghiệm thu A1-VAL-04..07 trong PLAN-102 sử dụng tên/ý nghĩa khác bảng chuẩn PLAN-085. Đã sửa tài liệu Git để thống nhất: 04 Feature Design; 05 Architecture & Workflow; 06 Risk Discovery; 07 Risk Management. Các case A1-VAL-01..09 vẫn NOT_RUN và cần reviewer độc lập xác nhận.

- REV-103-02 (P1): F56 là DBA Guard/Reviewer nhưng testcase cũ quá tập trung migration và rollback. Đã mở rộng dự thảo kiểm tra N+1 query, index, transaction boundary, SQL dialect, ownership và bằng chứng EXPLAIN khi thực sự có. Không tự chạy DDL/DML; mọi test chưa được thực thi.

- REV-103-03/04/05 còn mở: người có quyền phê duyệt BR/AC, risk P0 và host chưa được xác nhận; bản Google BRD là stakeholder mirror Draft, chưa có signoff tương đương nội dung; Codex --full-auto/Gemini MCP/Spec Kit native/Path Guard OS chưa kiểm chứng thành công. Chưa chuyển sang coding B, A.1 vẫn NOT_RUN và B.1 vẫn NOT_RUN.

- Bản tổng hợp trên Git: .agents/.workflow/validationSpecification.md mục PLAN-103, RTM mục U và .agents/.handoffs/plan-103-documentation-review-handoff.md. Đây là bản tóm tắt DRAFT, không thay đổi thứ tự quyền hoặc thay thế yêu cầu chuẩn trên Git.

- PLAN-103 supplemental review: F50 and F63

- Đối chiếu tiếp chức năng F50 Lightweight CI/SLM và F63 AI FinOps Profiler với test catalogue cho thấy cần làm rõ: F50 phải kiểm tra cả báo cáo static/CI, đầu ra SLM có provenance và fallback tất định khi model không khả dụng; F63 phải kiểm tra định lượng usage, vùng/loại model, bảng giá có thời điểm, đơn vị tính và phân biệt ước tính với số đo. Đã bổ sung các tiêu chí dự kiến trong tài liệu Git; không phát sinh test ID mới và chưa chạy test. Nội dung review này do một mô hình thực hiện, không phải đánh giá A.1 độc lập. Các finding chủ sở hữu, P0, CLI và các điều kiện triển khai vẫn chặn giai đoạn B.

#### 36.1. Kết quả đối chiếu BR–Feature–Test và tài liệu lưu trữ

- Trên GitHub nhánh docs/plan-089-a1-readiness, sáu nhóm yêu cầu đề xuất BR-022..027 đã được đối chiếu với 22 feature F43..F64. Test Catalogue hiện ghi cụ thể 44 mã test positive/negative TC-F043-P/N tới TC-F064-P/N và RTM Section P ánh xạ ngược từng nhóm BR sang các test đó. Đây là các ca THIẾT KẾ / CHƯA CHẠY; không phải yêu cầu nghiệp vụ đã được owner phê duyệt hoặc test thực thi thành công.

- Audit đường dẫn Markdown tại commit 352df6a9aa6b27ebb972a29c7711615e607af3cf kiểm tra 99 tài liệu và 868 tham chiếu tương đối: 11 liên kết cũ chỉ tồn tại trong ba file handoff lưu trữ v0.6.4, được ánh xạ sang tên file hiện hành trong Document Governance mà không sửa nội dung lịch sử. Bảng điều hướng README, structure và workflow index đã cập nhật tới PLAN-103 trên GitHub. Kiểm tra này không bao gồm mọi anchor nội bộ, URL bên ngoài hoặc kiểm chứng runtime.

- Trạng thái: AUTHORING_COMPLETE_CANDIDATE / OWNER_REVIEW_REQUIRED; A1_NOT_RUN, B_NOT_AUTHORIZED, B1_NOT_RUN và P0 vẫn mở. Reviewer A.1 phải đối chiếu chính xác revision Git đầu ra với revision Google BRD mới nhất; Google BRD là bản stakeholder Draft chứ không phải bản nghiệm thu độc lập.

#### 36.2. Hai đợt hoàn thiện tài liệu, mỗi đợt 10 task

- Đợt A — DOC-A01..A10: quy tắc ưu tiên nguồn yêu cầu; hồ sơ quyết định owner; ý nghĩa traceability; bằng chứng kiểm thử; ưu tiên nhóm rủi ro P0; tiêu chí A.1 độc lập; hợp đồng giữa các module; chọn reviewer có weight và kiểm soát tương quan; kiểm tra Codex CLI/sandbox; giới hạn thao tác native Spec Kit. Đợt A đã có commit 048333cf815c320239ed9a5958c1aeb958dba073 và handoff riêng trên nhánh docs/plan-089-a1-readiness.

- Đợt B — DOC-B01..B10: chuẩn hóa STOP/RESUME; phân biệt 9 bước vận hành và 5 trạng thái runtime; bằng chứng phiên bản công nghệ; hồ sơ user override; giải quyết drift Git/Google; validation report cho người phê duyệt; trạng thái feature; thứ tự nghiệm thu/triển khai; giới hạn Spec Kit Web so với native; cập nhật điều hướng README. Các hạng mục này thuộc phạm vi bản thảo và được kiểm tra/bàn giao theo SHA xuất bản trong Git, không đồng nghĩa có tính năng runtime mới.

- Quy tắc nghiệm thu thống nhất: một mô hình thực hiện nhiều lượt review theo vai trò chỉ được tính là author-side review, không phải reviewer độc lập A.1. Các testcase F43..64 và Codex-Gemini MCP vẫn NOT_RUN; không tự phê duyệt BRD, P0, A.1, B hay B.1. Google BRD là stakeholder Draft, cần owner đối chiếu đúng Git output SHA với Google revision rồi ra quyết định có chữ ký.

- Chỉ các thay đổi trong tài liệu hiện hữu và hai handoff Git được chấp nhận ở giai đoạn này; không tạo BRD/SRS thứ hai, không sửa code/runtime, không tự động merge PR hoặc làm sạch dữ liệu ngoài phạm vi.

#### 36.3. Bổ sung 5 đợt review tài liệu, mỗi đợt 10 task

- Đây là phần cập nhật Draft mang tính bàn giao stakeholder. Chuỗi năm đợt PLAN-106..110 tập trung review và hoàn thiện tài liệu hiện có thay vì tạo BRD/SRS thứ hai. Mỗi đợt gồm mười thay đổi có ID riêng trong mười tệp Markdown, một commit gộp và một handoff GitHub. Việc ghi nội dung đề xuất không cho phép tự kết luận A.1 PASS hoặc Implementation Ready.

- PLAN-106: 10 task về thứ tự nguồn yêu cầu, acceptance trạng thái, RTM hai chiều, rủi ro P0, kế hoạch coding có cổng, quyền BRD và độc lập reviewer. Git 83e894b58de866cb72f6044b00b034784a8067cb.

- PLAN-107: 10 task về Path Guard và Windows alias, chặn ngoài root liên tục, config/AGENTS host, policy routing, sandbox/CLI, STOP và rủi ro host. Git 967a6539fd799a06925a39173e85457e4df247f3.

- PLAN-108: 10 task về Spec Kit feature spec, plan/tasks, nghiên cứu upstream, model và contract Web/native, acceptance checklist và môi trường native. Git 44324800b02a0d1a79de1be5127d9369cd4ac1a3.

- PLAN-109: 10 task về Portable Skill, Codex-Gemini/Antigravity MCP tùy chọn, quality gates, session/traceability, giới hạn token, AST graph và implementation template. Git 64684a29fcec463a6915bb233a6b550dbff01107.

- PLAN-110: 10 task kết thúc review tài liệu, cải thiện navigation, feature statuses, checklist, version assessment, validation report và kế hoạch bàn giao. Git commit 09434e5239a360cf59c1492343df9a641e1c5c13 và handoff .agents/.handoffs/plan-110-10task-batch-5.md đã được xuất bản; đây là bằng chứng soạn thảo, không phải kết quả A.1 độc lập hoặc kiểm thử host.

- Những việc cần người thật/host: business owner chấp thuận BR/AC, architecture/security owner quyết định P0, reviewer A.1 độc lập xem đúng cặp Git SHA và Google revision, rồi mới xin ủy quyền B riêng. Các ca test thiết kế vẫn NOT_RUN; Codex --full-auto bản thử trước không được CLI hỗ trợ và Gemini MCP chưa được chứng minh có quyền truy cập.

#### 36.4. Chủ dự án chấp thuận APP-01..APP-06 ở mức thiết kế

- Ngày 14/11/2026, người yêu cầu viết nguyên văn “duyệt hết đi” sau khi trợ lý liệt kê bốn nhóm cần phê duyệt. Các mục APP-01..APP-06 là cách tác giả phân rã và giới hạn an toàn việc ghi nhận ý định đó, KHÔNG phải sáu câu phê duyệt riêng biệt hoặc chữ ký được xác thực. Đây là chấp thuận định hướng thiết kế; các AC chi tiết, rủi ro P0, quyền thực thi host và A.1 độc lập còn cần quyết định hoặc bằng chứng riêng. Google BRD tiếp tục là Draft stakeholder mirror.

- APP-01 — Chấp thuận phạm vi thiết kế BRD hiện có, gồm nhóm đề xuất BR-022..027 và các chức năng F43..64; chưa chấp thuận Acceptance Criteria chi tiết, giá trị ngưỡng, các trường hợp test như kết quả chạy thực tế hay nội dung Git–Google tương đương từng dòng.

- APP-02 — Chấp thuận định hướng kiến trúc S2C hiện có, tích hợp Spec Kit và adapter Codex/Gemini/Antigravity; chưa phê duyệt từng ADR/host/provider/vị trí triển khai, không xác nhận thực thi native thành công.

- APP-03 — Chấp thuận nguyên tắc Manual/Safe Auto mặc định, Sandbox Auto có quyền và Full Auto chỉ trong sandbox được chấp thuận rõ ràng; không cấp quyền thao tác thực tế, không cho phép YOLO toàn máy.

- APP-04 — Chấp thuận chính sách nhận diện, ưu tiên và xử lý P0 trước các thao tác nguy hiểm; mọi P0 vẫn OPEN/UNKNOWN RESIDUAL cho đến khi có bằng chứng kiểm thử và quyết định chấp nhận riêng.

- APP-05 — Chấp thuận mô hình A → A.1 → B → B.1, STOP/RESUME, handoff, review đa agent và RTM; không coi chấp thuận quy trình là A.1 PASS hay ủy quyền B.

- APP-06 — Chấp thuận chọn công nghệ ổn định, phổ biến, còn hỗ trợ, tuân thủ tài liệu chính thức và cho phép user override có kiểm soát; không phê duyệt một phiên bản cụ thể hoặc một migration chưa kiểm chứng.

- Trạng thái chung: DESIGN_POLICY_APPROVED_BY_REQUESTER / EXTERNAL_IDENTITY_NOT_VERIFIED; A1_NOT_RUN; P0_OPEN; B_NOT_AUTHORIZED; B1_NOT_RUN. Reviewer A.1 phải dùng đúng Git HEAD sau commit ghi nhận và revision Google hiện tại, đối chiếu các yêu cầu/AC chi tiết; không được tự tạo chữ ký hoặc nâng trạng thái.

#### 

#### 36.5. Đối chiếu sáu BR đề xuất với nguồn Git — DRAFT, chưa duyệt AC

- Đối chiếu nguồn: nhánh docs/plan-089-a1-readiness, Git HEAD 003297ff1253e661414350483b53a76f9afdaa67, .agents/.spec.md v1.5 mục PLAN-A1-AC. Đây là bản tóm tắt cho stakeholder, không thay thế nguồn Git hoặc biên bản nghiệm thu A.1.

- BR-022 — Source/impact/contract: khi nguồn được ghim và phạm vi được chấp thuận, báo cáo ID nguồn, tác động trực tiếp/gián tiếp và gợi ý test; từ chối sửa khi nguồn lỗi thời, phụ thuộc chưa rõ hoặc ngoài repo. Owner phải chốt tập nguồn/đồ thị tham chiếu và thước đo kết quả.

- BR-023 — Permission/Path Guard/cleanup: thao tác được phép phải có danh tính, phạm vi và audit; traversal, junction/reparse, MCP vượt quyền hoặc dọn dữ liệu được bảo vệ phải bị chặn, hash sentinel bên ngoài không đổi. Owner host/security phải chốt OS và fixture.

- BR-024 — Quality/DBA/review: phát hiện lỗi có thể tái lập kèm nguồn/quy tắc/độ bao phủ, giữ ý kiến bất đồng; thiếu dialect, thiếu oracle hoặc reviewer lỗi không được ghi PASS. Owner QA/DBA/architecture chốt ngôn ngữ, độ phủ và tiêu chí lỗi.

- BR-025 — Context/SLM/budgets: định tuyến minimal/balanced/deep giữ mọi chính sách bắt buộc, ghi chi phí/thời gian và nguồn; context cũ, thiếu policy, rò rỉ secret hoặc vượt budget phải từ chối/fallback có ghi nhận. Owner chốt benchmark, ngân sách và mẫu nhạy cảm.

- BR-026 — Trace/multi-source/rollback: một thay đổi được duyệt liên kết source→spec→schema→API/code, có owner, manifest và rollback thử được khi có quyền; xung đột schema, giá cloud không rõ hoặc rollback thất bại phải chặn. Owner kiến trúc/DB/cloud chốt dữ liệu và tiêu chí khôi phục.

- BR-027 — Protected Core/self-evolution: bắt buộc kiểm chứng phạm vi Z0/Z1, các AC thiết yếu và reviewer độc lập; sửa protected bytes, tự ký duyệt hoặc còn P0 phải ngăn promotion. Các mốc 100% mandatory AC và >95% coverage hiện chỉ là đề xuất, chưa duyệt mẫu số/phạm vi.

- Trạng thái của BR-022..027: CANDIDATE / BUSINESS_AC_PENDING / TEST_NOT_RUN. Các test TC-F043..064-P/N (44 mã) vẫn chỉ ở trạng thái DESIGNED/NOT_RUN. Cần chữ ký owner theo đúng cặp revision Git–Google và review độc lập A1-VAL-01..09; không được tự nâng A1_PASS, B_AUTHORIZED hoặc B1_PASS.

- 

#### 36.6. PLAN-111 — Kết quả sửa P0 và quay lại giai đoạn A (chưa nghiệm thu A.1)

- Nguồn Git mới: nhánh docs/plan-089-a1-readiness, commit 78c65b278fbd2ec384301c88abfdf6c84d388a29 và commit cf8c595b2e4dd5ee2178087bf370b4d36b12213b. Bản sửa có thay đổi mã nguồn và regression test đúng phạm vi requester yêu cầu; không mở branch mới và PR #10 vẫn Draft.

- Workflow Guard: truyền đúng task/paths qua CLOSE; kiểm tra policy VERIFY và HANDOFF bằng operation tương ứng; ràng buộc freshness của file source, chính sách, active Spec Kit spec/plan/tasks; từ chối xác nhận freshness đối với thư mục không xác định và status không đủ scope. Lỗi tương thích status rỗng được sửa sau khi CI đầu tiên phát hiện.

- Path Guard: mở rộng kiểm tra Windows GetFileAttributesW để nhận diện mọi reparse-point flag, kể cả loại không phải junction. Đây chỉ là ngăn chặn ở thời điểm kiểm tra, không phải bảo đảm chống race TOCTOU. Windows/untrusted filesystem cần sandbox hoặc IO dựa trên handle đã được đánh giá bảo mật và kiểm chứng sentinel ngoài repo.

- Bằng chứng CI tại cf8c595b2e4dd5ee2178087bf370b4d36b12213b: sáu job Ubuntu (Python 3.10, 3.11, 3.13 trên hai workflow) đã PASS khi kiểm tra; Windows 3.14 cũng PASS (132 test, không skip); mỗi job Ubuntu 3.10/3.11/3.13 PASS 132 test (4 skip). Cả hai workflow thành công tại SHA đã nêu. Không chuyển trạng thái testcase chưa chạy sang PASS.

- Vòng đánh giá: A1-VAL-01..09 chỉ được author preflight, chưa có reviewer độc lập có thẩm quyền; A1_NOT_RUN. Quyết định P0 Windows, BR-022..027 AC/threshold, ADR và phê duyệt nguồn Git/Google vẫn cần chủ sở hữu xác nhận. Không có A1_PASS, quyền B tổng quát, B1_PASS hoặc release.

- Quay lại A: P4 chốt yêu cầu và AC, P6 thiết kế OS/sandbox bảo vệ Path Guard, P7/P8 đánh giá và xử lý rủi ro RM-001..005, P9 bàn giao cho reviewer A.1 độc lập. Nguồn hồ sơ chính: .agents/.handoffs/plan-111-a1-p0-return-to-a.md; đây là tóm tắt Draft cho stakeholder, không thay thế Git master SRS.

- 

