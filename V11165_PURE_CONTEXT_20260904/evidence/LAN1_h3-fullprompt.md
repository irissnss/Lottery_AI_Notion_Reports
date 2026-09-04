# h3-fullprompt · tang=CODED_AND_TESTED_NOT_RUNTIME_PROVEN

## TOM TAT

Đã dump PAYLOAD CUỐI 100% từ hàm ĐANG SERVE (gpt_analyzer.py sha 758c29c13185763f) trên clone bất biến, sandbox chặn hai chiều 6/6 đạt, neo558 production TRƯỚC=SAU, clone không đổi, PID 3370750 NRestarts 0. Chứng minh an toàn tĩnh trước: 19 hàm tiếp cận được trong gpt_analyzer + 23 hàm ngoài module đều KHÔNG có đường ghi DB/tệp/mạng; 36 execute đều SELECT/PRAGMA. Bám được 222 payload (57 đường scheduler = 100% mẫu số 30 ngày · 54 đường combo-super chưa ai đo bao giờ · 111 biến thể retry, trong đó 6 không tới được). Bốn khiếm khuyết ĐƯỢC CHỨNG MINH: (1) rò gói ngữ cảnh shadow vào lane OFFICIAL của gpt-oss-120b VẪN CÒN SỐNG tại :6738 — nó nhận thêm khối «PHASE-FIRST REASONING GATE» 2.979 ký tự mà 7 model official khác không hề nhận, ở CẢ BA miền; (2) vân tay prompt runtime chỉ phủ 39,81–48,07% chuỗi thật, thiếu 26.478–35.315 ký tự mỗi lượt, bắt được 2/11 phép đột biến; (3) bộ 5 dấu ô nhiễm mù cấu trúc — shadow báo 0/5 «sạch» trong khi payload thật vẫn có weight= (33/33), Best MB model (11/33), AI token models 14d WR (11/33); (4) prompt «ngữ cảnh thuần» của shadow VẪN giao rổ số đã chọn sẵn «ĐỀ XUẤT PYTHON: 86 (score=21), 16 (score=21)» + «SỐ NÊN TRÁNH (9 số)» + «AI nên ưu tiên» — 33/33 lượt, y hệt official. Cổng _v11160_test_lane.py mù với nửa ctx_pack (0 lần nhắc build_context_pack/shadow_mode/ctx_pack). Hai bản vá ứng viên là TỆP MỚI trong artifacts/, không đè tệp đang serve, thử chặn hai chiều: patch A xoá lệch ctx official ở cả ba miền, patch B nâng phát hiện đột biến từ 2/11 lên 11/11.

## TRA LOI

**1) Chứng minh an toàn TRƯỚC khi gọi ba hàm sinh prompt — có chứng minh được không?**
CÓ, và không phải viện dẫn niềm tin. Đồ thị gọi AST từ ba điểm vào ra 19 hàm trong `gpt_analyzer.py` và 23 hàm ngoài module; quét đủ bốn lớp (SQL ghi · `.commit()` · `open(w/a/x/+)` · mạng) đều bằng **0**; 36 lệnh `cursor.execute` phân loại được 34 SELECT/PRAGMA, **0 ghi**, 2 «không rõ» mở ra đọc thì đều là SELECT. Vì thế **KHÔNG** phải ghi `BLOCKED_BY_SIDE_EFFECT_UNCERTAINTY` — nhưng tôi vẫn chạy trên clone bất biến với ba lớp chặn (chuyển hướng connect · guard SQL · mode=ro), vì «chứng minh tĩnh» không thay được bẫy mutation. Thử chặn hai chiều 6/6 đạt, trong đó phép quan trọng nhất là **tắt guard rồi thử INSERT vẫn bị chặn** bởi `mode=ro` — chứng minh có lớp thứ hai độc lập. neo558 production TRƯỚC = SAU, clone sha256 không đổi, PID 3370750 NRestarts 0.

**2) FULL_RUNTIME_PAYLOAD_HASH_COVERAGE có bằng 100% không?**
**100% cho đường scheduler** (57/57 tổ hợp miền × regime × model, đúng bằng mẫu số thật lấy từ `predictions` 30 ngày). Cộng thêm 54 payload của **đường combo-super mà chưa phép đo nào trước đây chạm tới**, và 105 biến thể retry/fallback tới được. **Chưa phủ, nói thẳng:** (a) **số token là INDETERMINATE** — VPS không có tokenizer và cấm gọi provider; tôi từ chối ước lượng bằng hệ số mượn (RM-21), chỉ báo ký tự + byte; (b) ba đường `main.py:8769` (endpoint single-AI thủ công), `ensemble_voting.py:192`, `advanced_modes.py:286` — không sinh dòng nào trong 30 ngày nên không nằm trong mẫu số, và tôi **không** dump chúng; (c) 105 biến thể retry là **TÁI LẬP từ mã đang serve, không phải bắt được một lượt retry THẬT** — đây là sự khác biệt về tầng, không được đọc là bằng chứng runtime; (d) header HTTP và khoá API cố ý REDACT.

**3) Kiểm bắt buộc gpt-oss-120b — bốn câu, trả lời từng câu:**
- *«official không được nhận shadow ctx_pack chỉ vì nằm trong SHADOW_GATE_MODELS»* → **ĐANG VI PHẠM, vẫn sống**. `:6738` còn nguyên `or (selected_model in SHADOW_GATE_MODELS)`. Ba miền đều lệch, chênh 3.075–3.208 ký tự, trong đó có nguyên khối hợp đồng suy luận 8 bước 2.979 ký tự.
- *«shadow behavior chỉ phụ thuộc per-run regime»* → **ĐÚNG cho nhánh PROMPT** (V11160 đã sửa `regime_prompt_cho_luot`), **SAI cho nhánh CONTEXT PACK**. Đúng một nửa.
- *«selected_model KHÔNG được quyết định content regime»* → **ĐANG QUYẾT ĐỊNH**. `selected_model` là biến duy nhất khiến `_shadow_mode` bật lên ở lượt official.
- *«cấm ép model này lại vào shadow roster để làm đẹp phép kiểm»* → **KHÔNG ép**. Tôi giữ nguyên roster thật: `gpt-oss-120b ∈ TOKEN_MODELS` = True, `∈ SHADOW_AUTO_EVAL_MODELS` = **False**. Nó có **168 lượt shadow THẬT** (06/06 → 01/08, MN 57 · MT 56 · MB 55) rồi **dừng hẳn từ 2026-08-01** khi được nâng lên official. Nên: **lane shadow của gpt-oss-120b = NOT_EXERCISED từ 2026-08-01**; toàn bộ 103 lượt của nó trong 35 ngày kế tiếp (MB ai_chain 35 · MT ai_chain 33 · MN auto_daily 34 · MT fallback 1) đều là official-và-nhiễm.

**4) Có dùng thứ gì làm ĐẠI DIỆN cho final payload không?**
Không. Tôi dựng đủ tám phần theo đúng thứ tự nối của mã đang serve, rồi bọc thêm wrapper của từng provider (5 tuyến), rồi mới băm. Cả `final_system_sha256`, `final_user_sha256` lẫn `final_payload_sha256` đều tính trên chuỗi/dict **sau** mọi bước, không phải trên context pack rời hay prompt trước de-herding.

**5) Bản vá ứng viên có chứng minh được nâng độ phủ lên 100% không?**
Chứng minh bằng **phát hiện đột biến**, không bằng lời khai. Trạng thái sạch: hai lần chạy giống hệt (allow). 11 phép đột biến trải đủ năm vùng (system · base · ctx_pack · rulebook · tham số/route): vân tay hiện tại bắt **2/11**, vân tay ứng viên bắt **11/11** — bao gồm chính phép «rò ctx shadow vào official» mà bản hiện tại mù. Patch A: trước vá official có **2 bản ctx** ở cả ba miền, sau vá còn **1 bản**. Cả hai là **tệp MỚI trong `artifacts/`**, không đè tệp đang serve, không deploy, không restart. Tầng cao nhất được phép ghi: `CODED_AND_TESTED_NOT_RUNTIME_PROVEN`.

**6) Câu quan trọng nhất — prompt shadow đã là PURE CONTEXT theo định nghĩa owner chưa?**
**CHƯA, và không gần.** `context_only` chỉ gác **6/171 = 3,51%** điểm bơm chuỗi; `build_context_pack` (141 điểm) và `REASONING_RULEBOOK` không bị gác lấy một điểm. Hệ quả đo được trên 33/33 lượt shadow: prompt vẫn giao **rổ số đã chọn sẵn** (`ĐỀ XUẤT PYTHON: 86 (score=21), 16 (score=21)` · `Tổng candidates: 17` · `SỐ NÊN TRÁNH (9 số)`), vẫn **biến điều kiện thành mệnh lệnh** (`→ AI KHÔNG NÊN chọn các số trên`, `AI nên ưu tiên nhưng có thể điều chỉnh`), vẫn chở **trọng số** (`weight=` ×5) và **tên model kèm win-rate** (`🏆 Best MB model: gemini-2.5-flash (20.0%)`). Cái đã gỡ được đúng một thứ: bảng `🏆 HIỆU SUẤT THEO MODEL` 21 dòng (24/24 official → 0/33 shadow). Vì thế mọi câu nói «shadow đang chạy prompt thuần ngữ cảnh» phải đọc là **«shadow đã gỡ bảng xếp hạng model ở base prompt»** — không hơn.

## PHAT HIEN
  - [PROVEN_DEFECT] RÒ GÓI NGỮ CẢNH SHADOW VÀO LANE OFFICIAL — nửa còn lại của V11160 VẪN CHƯA VÁ
  - [PROVEN_DEFECT] VÂN TAY PROMPT RUNTIME CHỈ PHỦ 39,81–48,07% — bắt được 2/11 phép đột biến
  - [PROVEN_DEFECT] BỘ 5 DẤU Ô NHIỄM MÙ CẤU TRÚC — shadow báo «0/5 sạch» trong khi payload thật vẫn chở win-rate, trọng số và TÊN MODEL
  - [PROVEN_DEFECT] PROMPT «NGỮ CẢNH THUẦN» VẪN GIAO RỔ SỐ ĐÃ CHỌN SẴN KÈM MỆNH LỆNH — 33/33 lượt shadow, y hệt official
  - [PROVEN_DEFECT] CỔNG `_v11160_test_lane.py` MÙ VỚI NỬA CONTEXT PACK — cùng họ lỗi «thước không thể thấy» của V11157/V11158
  - [PROVEN_DEFECT] ĐƯỜNG COMBO-SUPER DÙNG SOURCE_DATA KHÁC HẲN ĐƯỜNG SCHEDULER — cùng model, cùng ngày, cùng miền nhưng HAI prompt khác nhau (chưa ai đo bao giờ)
  - [NO_ANOMALY_FOUND] KHÔNG CÓ ĐƯỜNG GHI NÀO trong toàn bộ đồ thị gọi của ba hàm sinh prompt — an toàn được chứng minh trước khi gọi
  - [EXPECTED_BEHAVIOR] Route deepseek GỘP system vào user ⇒ final_system_chars = 0; mọi phép kiểm bám riêng «system prompt» của deepseek đang bám chuỗi RỖNG
  - [OPERATIONAL_IMPROVEMENT] Nhánh repair-retry PHASE-FIRST không bao giờ chạy (PHASE_FIRST_CONTRACT_MODELS rỗng) — và 6/111 biến thể retry không tới được
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] gemini-3.5-flash và gemini-3.6-flash chạy CẢ HAI regime prompt trong CÙNG MỘT NGÀY — nguy cơ cho mọi phép so shadow vs official
  - [INDETERMINATE] SỐ TOKEN không đo được — chỉ có ký tự và byte
  - [OPERATIONAL_IMPROVEMENT] HAI BẢN VÁ ỨNG VIÊN — tệp MỚI trong artifacts/, thử chặn hai chiều ĐẠT, chưa deploy

## DAU VAO LAN SAU

**A. Ba hằng số phải mang sang, đừng đo lại:**
- Mã đang serve: `gpt_analyzer.py` sha16 `758c29c13185763f` · `main.py` `4ed5fd7ebaee8d23`. Bản local `E:\Lottery_AI_Test\web\backend\` **trùng byte** với VPS cho hai tệp này (đã kiểm) ⇒ đọc mã tĩnh ở local là hợp lệ, **nhưng DUMP thì vẫn phải chạy trên VPS** (RM-14).
- Clone bất biến `/root/Lottery_AI_Test/artifacts/v11165_immutable.db` sha `c3c2f568…b6efebb6e2` còn nguyên, `chattr +i` còn giữ. Dùng lại, đừng tạo clone mới.
- neo558 = `a82c508d3569abda47041ad625cca93fdec2227fbe389c395dc7f139893a0e5f` (n=558). Công thức: `SELECT id,date,region,bach_thu,model_count,created_at FROM final_bundles ORDER BY id LIMIT 558`, nối bằng `|`, mỗi dòng thêm `\n`.

**B. Ba con số PHẢI dùng, không được suy lại:**
- Vân tay prompt hiện tại phủ **39,81–48,07%** (tb 43,59%), thiếu **26.478–35.315** ký tự/lượt, bắt **2/11** đột biến. Mọi câu «prompt sạch» dựa trên `runtime_prompt_sha256` đều **KHÔNG có giá trị chứng minh** cho ctx_pack / rulebook / wrapper.
- `context_only` gác **6/171 điểm bơm = 3,51%**. `build_context_pack` (141 điểm) bị gác **0**.
- Rò shadow ctx vào official: **+3.208 / +3.075 / +3.097** ký tự (MN/MT/MB), khối lớn nhất là `PHASE-FIRST REASONING GATE` **2.979** ký tự.

**C. Việc lượt sau nên làm trước tiên (theo thứ tự lợi nhất):**
1. **Trình owner Patch A** — nó là vết nửa còn lại của V11160, một dòng, đã có thử chặn hai chiều. Cho tới khi vá, **mọi phép so official-vs-shadow đều có một model official ăn prompt thí nghiệm**, nên nhánh official không phải đối chứng sạch (chạm `PRJ-SELECTION-WINDOW-001`).
2. **Dựng lại cổng `_v11160_test_lane.py`** cho nó soi CẢ `build_context_pack(shadow_mode=…)`, không chỉ `regime_prompt_cho_luot`. Hiện nó có 0 lần nhắc `build_context_pack` / `shadow_mode` / `ctx_pack` ⇒ mù đúng chỗ nó nhận trách nhiệm canh.
3. **Trả lời owner câu «thuần ngữ cảnh»** bằng bảng B4, đừng bằng chữ. Muốn đạt PURE CONTEXT thì phải gỡ tiếp ba thứ nằm NGOÀI phạm vi `context_only` hiện tại: (a) khối `ĐỀ XUẤT PYTHON` + `SỐ NÊN TRÁNH` + hai câu mệnh lệnh kèm theo trong `create_analysis_prompt`; (b) ba dòng `AI token models 14d` / `ML/ensemble models 14d` / `🏆 Best MB model: <tên>` tại `gpt_analyzer.py:5579-5583`; (c) các hằng WR theo miền trong `REASONING_RULEBOOK` (`MN ~57% · MT ~61% · MB ~47%`).
4. **Đường combo-super phải vào phạm vi đo.** Nó dùng `source_data` khác hẳn (MT −1.526, MB −1.815 ký tự) và có thêm `herding_warning`; 54 payload đã bám sẵn trong `v11165_h3_combo_super.json` — dùng lại, đừng dựng lại.

**D. Ba cái bẫy đã sập trong phiên này, đừng sập lại:**
- Vá `io.open` bằng hàm Python 

## CHUA TRA LOI

**1. SỐ TOKEN — INDETERMINATE, không phải «chưa làm».** VPS không có tokenizer (`import tiktoken` → `No module named 'tiktoken'`) và luật cứng cấm gọi provider thật nên không lấy được `usage`. Tôi **từ chối** ước lượng bằng hệ số chia ký tự: prompt là tiếng Việt dày dấu, mọi hệ số mượn từ thước tiếng Anh rơi đúng vào `RM-21` (hằng số chỉ đúng cho thước đã đo nó), và con số ước lượng sai chiều sẽ đẻ ra kết luận sai về chi phí/cắt ngữ cảnh. Đã thay bằng ký tự + byte UTF-8, đo được và tái lập được cho cả 57 combo. Muốn có token thật thì hoặc cài tokenizer trên VPS, hoặc đọc `tokens_used` từ `predictions`/trace của lượt đã chạy.

**2. Ba đường gọi `analyze_and_predict` KHÔNG được dump:** `main.py:8769` (endpoint single-AI thủ công), `ensemble_voting.py:192`, `advanced_modes.py:286`. Lý do: cả ba không sinh dòng nào trong `predictions` 30 ngày nên không nằm trong mẫu số production; nhưng chúng **có thể** dựng `source_data` theo công thức riêng như combo-super đã cho thấy. Chưa chứng minh được chúng trùng hay khác đường scheduler ⇒ ghi **NOT DUMPED**, không suy đoán.

**3. 105 biến thể retry/fallback là TÁI LẬP, không phải QUAN SÁT.** Tôi dựng chúng từ mã đang serve (`_do_call` attempt 1..4, fallback `max_tokens`, fallback bỏ `temperature`, `temperature=1` của anthropic, đường thoát 503 của gemini) và bám hash — nhưng **không bắt được một lượt retry THẬT nào** trong phiên (không gọi provider). Tầng đúng là `CODE_REPRODUCED`, **không phải** `RUNTIME_PROVEN`. Muốn nâng tầng thì phải bắt log/trace của một lượt retry thật.

**4. Không đo được TÁC ĐỘNG của rò shadow-ctx lên chất lượng dự đoán.** Tôi chứng minh được prompt KHÁC (hash, độ dài, khối nội dung), và chứng minh được model đó ra số công bố thật; nhưng **KHÔNG** đo «prompt khác ⇒ trúng nhiều/ít hơn». Làm phép đó cần nền đúng cho từng vế (`RM-18`), VIF đo lại cho chính thước bạch thủ (`RM-21`, **cấm mượn 2,92**), tách TRONG/NGOÀI cửa sổ chọn (`PRJ-SELECTION-WINDOW-001`), và đăng ký ngưỡng TRƯỚC ngày chốt (`RM-03`). Chưa