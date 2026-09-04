# h8-modelmatrix · tang=EVIDENCE_COMPLETE

## TOM TAT

Gate 8 đã dựng MODEL_PROMPT_COMPATIBILITY_MATRIX cho đủ 19 LLM active+shadow (class=TOKEN, role=GENERATOR), mọi trường đọc thẳng từ mã đang serve trên VPS (hash khớp Gate 0) và mọi con số đo trên prediction_trace.jsonl + clone bất biến, không đọc tài liệu provider. Phát hiện nặng nhất: gpt-oss-120b — model OFFICIAL output_eligible — nhận GÓI NGỮ CẢNH SHADOW ở 88/88 lượt official trong 30 ngày, vì V11160 chỉ vá nửa: sửa được regime prompt nhưng để nguyên `_shadow_mode` ở gpt_analyzer.py:6738 cấp cho build_context_pack; gói shadow thêm hai khối mà 7 model official khác không có, trong đó có "PHASE-FIRST REASONING GATE — 8 bước BẮT BUỘC". Trả lời thẳng câu hỏi cắt prompt: hệ KHÔNG cắt đầu vào gì cả — không ưu tiên section, không phiên bản hoá, không ghi section bị bỏ, không băm payload sau cắt (grep 0 dòng), và không model nào có context window khai trong mã nên hệ không thể biết prompt có vừa hay không. Hệ quả đúng như đề bài định nghĩa: ngày 04/09 cả 60 lượt mang cùng nhãn prompt_version=PB-20.1 và cùng prompt_layers, nhưng sinh ra 60 vân tay sha256 khác nhau, hai regime và hai biến gói ngữ cảnh — hai payload khác nhau đang bị gọi là cùng một prompt version, PROVEN_DEFECT. Tool calling KHÔNG bật ở bất kỳ model nào (grep 5 mẫu trên toàn web/backend = 0 dòng), nên mọi mệnh lệnh bảo model "tự truy vấn" đều không thể thi hành. Prompt OFFICIAL vẫn bơm đủ tên model + win_rate + weight kèm mệnh lệnh "AI nên ưu tiên patterns từ models có win_rate cao hơn" (contam_hits=4 ở cả 27 lượt LEGACY_PROMPT, =0 ở cả 33 lượt CONTEXT_ONLY_V2) — trái thẳng mục tiêu thuần-ngữ-cảnh số 5 và số 8 của owner. Không viết vá, không deploy, không restart, không ghi DB: clone bất biến và 8 tệp mã production đều còn nguyên hash, service PID 3370750 NRestarts 0.

## TRA LOI

## 1. "Có model nào nhận nội dung khác model khác cùng miền/regime không? (V11164 tìm ra gpt-oss-120b — tìm xem còn ca nào khác không)"

**CÓ, và đúng MỘT ca duy nhất còn lại chưa được giải thích trước đó — nhưng ca của V11164 thì VẪN CÒN NGUYÊN, chưa được vá.**

**Nhóm OFFICIAL (8 model output_eligible), 89 cặp (ngày,miền) trong 30 ngày:**
- `gpt-oss-120b`: **88/88 lượt LỆCH** (100%). delta TB +2.534,9 ký tự, max +3.269.
- 7 model official còn lại: **0 lượt lệch** trên tổng 89+112+115+95+114+108+88 lượt.
⇒ Ngoài `gpt-oss-120b`, **KHÔNG có ca nào khác** trong nhóm official.

**Nhóm SHADOW (11 model), 89 cặp:** 15 lượt lệch, đã truy hết nguyên nhân:
- **8 lượt** = lượt combo-super của `gemini-3.5-flash` / `gemini-3.6-flash` — hai model này nằm trong `combo_super.AI_MODELS` (9 mục), lượt đó gọi `analyze_and_predict` không kèm `lane_test_shadow_pack` và hai model không thuộc `SHADOW_GATE_MODELS` ⇒ nhận gói **official**. `cpc` trùng **khít** giá trị official. → `EXPECTED_BEHAVIOR`.
- **7 lượt** = `qwen3.7-max` ×4, `gpt-5-mini`, `glm-5.2`, `grok-4.3` — `cpc` **không trùng cả hai** giá trị, nằm giữa; nghi trôi theo thời điểm gọi (chậm hơn cohort 5–10 phút). → `SUSPICIOUS_NEEDS_MORE_EVIDENCE`, **không kết luận**.

**Bốn dạng bất đối xứng đề bài liệt kê, đối chiếu từng cái:**

| Dạng | Có xảy ra? | Bằng chứng |
|---|---|---|
| model A nhận thêm candidate list | **KHÔNG** — mọi model cùng regime nhận cùng `create_analysis_prompt` | 7 model official cpc lệch 0 |
| model B **thiếu** condition | **CÓ** — 7 model official thiếu 2 khối mà `gpt-oss-120b` có (`:5059`, `:5849`) | 88/88 lượt |
| model C nhận **model ranking** | **CÓ, nhưng ĐỒNG LOẠT** — cả 8 model official đều nhận `HIỆU SUẤT THEO MODEL` + `win_rate` + `weight` (`:3040-3043`); 11 model shadow đều **không** | contam_hits 4 vs 0, 04/09 |
| model D nhận dữ liệu **sau cutoff** | **KHÔNG ĐO ĐƯỢC ở gate này** — cần dựng lại gói ngữ cảnh, ngoài phạm vi lần sóng 1 | — |

## 2. "Nếu prompt vượt budget: hệ CẮT THẾ NÀO?"

| Câu hỏi | Trả lời | Bằng chứng |
|---|---|---|
| Hệ cắt thế nào? | **KHÔNG CẮT GÌ CẢ** | `grep -rE 'user_prompt\s*\[\s*:'` = 0 · `'system_prompt\s*\[\s*:'` = 0 · `'_ctx_pack\s*\[\s*:'` = 0. Lát cắt duy nhất: `raw_prompt[:500]` (`:973`) là **custom prompt của owner**, `ARCHIVE_ONLY` |
| Có section priority đã phiên bản hoá chưa? | **CHƯA CÓ** | AST: không hằng số `*PRIORITY*` / `*SECTION_ORDER*`; `grep MAX_INPUT\|max_input\|MAX_PROMPT` chỉ trúng `knowledge_weights.py` (trọng số học) |
| Có ghi section nào bị bỏ không? | **KHÔNG** | Trường hợp bỏ duy nhất: bỏ **cả gói ngữ cảnh** khi `len<=500`, chỉ `print('[CONTEXT_PACK] No context data')` (`:6769`). Trace không có trường boolean nào. Đo được **36 lượt** (3 cặp ngày-miền × 12 model, `cpc=64`) |
| Có băm payload SAU khi cắt không? | **KHÔNG** — băm **TRƯỚC** khi nối thêm | `:6723` băm; `ctx_pack` nối `:6755`, `RULEBOOK` nối `:6760`. Độ phủ đo được **44,1%** (n=60, p5 40,1% · p95 48,3%) |

**⇒ Kết luận đúng theo tiêu chí đề bài: `PROVEN_DEFECT`.** Bằng chứng chốt: ngày 04/09 cả **60/60** lượt mang `prompt_version=PB-20.1` + `prompt_layers={SP-4.4, RR-16.5, CTX-18.6, PB-20.1}` **y hệt**, `declared_but_inactive_layers=[]`, nhưng sinh ra **60 vân tay sha256 khác nhau**, **2 regime** (27 vs 33), **2 biến gói ngữ cảnh**, `contam_hits` chia đôi **4 vs 0**. Hai payload khác nhau đang bị gọi là cùng một prompt version.

**Bổ sung quan trọng:** vì **không model nào có context window trong mã**, hệ **không thể** biết prompt sắp vượt. Nếu có vượt, provider trả 400 → rơi vào chuỗi lùi 4 bước → cả 4 hỏng → `MODEL_INCOMPATIBLE` + circuit breaker 600s (`:4222-4230`). Tức lỗi ngân sách đầu vào sẽ **hiện ra dưới lớp nguỵ trang "model không tương thích"**. Prompt lớn nhất quan sát được: **62.419 ký tự** — rủi ro **chưa kích hoạt**, không phải sự cố đang xảy ra.

## 3. "Cấm giả định mọi model xử lý prompt giống nhau"

Đã đo, **không giả định**. Khác biệt THẬT giữa các model, đọc từ mã đang serve:
- **Trần đầu ra chênh 24 lần**: 16.384 (claude/gpt-5.4/gpt-5-mini) → 65.536 (gemini) → 393.216 (deepseek-v4-pro-real).
- **`_MODEL_MAX_TOKENS` chỉ có tác dụng với OpenRouter** (dùng đúng 1 chỗ, `:4019`). Ba provider trực tiếp hard-code: `:3347`, `:3403`, `:3546`.
- **JSON có cấu trúc**: Anthropic **KHÔNG** có cơ chế nào, chỉ nối câu chữ "trả về ĐÚNG JSON" (`:3443`). DeepSeek thinking cũng không. OpenAI/OpenRouter dùng `json_object`. Gemini dùng `response_mime_type`.
- **Vai trò system**: DeepSeek thinking **GỘP** system+user thành một message user (`:3660`). Gemini dùng `system_instruction=`. Anthropic dùng `system=`. OpenAI/OpenRouter dùng `role:system`.
- **Reasoning**: `effort:high` cho gpt-5.5/grok-4.3/qwen3.7-max; `exclude:True` cho qwen3-max-thinking; `thinking:enabled` cho deepseek; động cho gemini; không gửi gì cho phần còn lại.
- **Retry/circuit breaker**: chỉ OpenRouter có circuit breaker (600s / 90s cho 429) và chuỗi lùi 4 bước. Anthropic/DeepSeek/OpenAI không có.
- **Timeout HTTP**: chỉ OpenRouter đặt (`300.0`, `:4089`). Bốn wrapper còn lại **không đặt** → rơi về mặc định SDK.
- **Parser và Unicode**: **dùng chung 100%**, không nhánh riêng — đây là chỗ **không** có bất đối xứng.

## PHAT HIEN
  - [PROVEN_DEFECT] gpt-oss-120b (OFFICIAL) nhận gói ngữ cảnh SHADOW ở 88/88 lượt — V11160 mới vá một nửa
  - [PROVEN_DEFECT] Hai payload khác hẳn nhau mang cùng một nhãn prompt_version — đúng định nghĩa PROVEN_DEFECT của đề bài
  - [PROVEN_DEFECT] KHÔNG có bất kỳ cơ chế cắt prompt đầu vào nào — và cũng không có context window để biết khi nào cần cắt
  - [PROVEN_DEFECT] Vân tay runtime_prompt_sha256 chỉ phủ 44,1% chuỗi thật — băm trước khi nối ctx_pack và RULEBOOK
  - [PROVEN_DEFECT] Prompt OFFICIAL vẫn bơm tên model + win_rate + weight + mệnh lệnh bắt chước nhau — trái mục tiêu thuần-ngữ-cảnh #5 và #8
  - [PROVEN_DEFECT] Prompt shadow đe doạ suông: 'OUTPUT KHÔNG HỢP LỆ nếu thiếu bất kỳ field nào' trong khi bộ kiểm đã tắt hẳn
  - [PROVEN_DEFECT] SHADOW_GATE_MODELS 75% là mục chết, nhưng vẫn là thứ duy nhất điều khiển _shadow_mode
  - [PROVEN_DEFECT] deepseek-v4-pro-real: trần max_tokens 393.216 với hard_timeout 300s — trần cao gấp ~4 lần mức với tới được, 12/89 lượt timeout
  - [PROVEN_DEFECT] Gói ngữ cảnh bị bỏ nguyên gói 36 lượt trong 30 ngày mà trace không có cờ nào đánh dấu
  - [EXPECTED_BEHAVIOR] Tool calling KHÔNG bật ở bất kỳ model nào — mọi mệnh lệnh 'tự truy vấn' trong prompt là không thi hành được
  - [OPERATIONAL_IMPROVEMENT] Trần đầu ra per-model KHÔNG lấy từ _MODEL_MAX_TOKENS cho ba provider trực tiếp — ba con số cứng nằm rải trong ba hàm
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] Hai model shadow_only đang nằm trong pool bỏ phiếu của combo-super (output_eligible)
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] gemini-2.5-flash (official) và gemini-3.5-flash: có lượt reasoning ăn 96,0% trần đầu ra, chỉ còn ~2.600 token cho JSON
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] Lượt gọi OpenRouter THÀNH CÔNG dài hơn hẳn httpx timeout=300s — chưa tách được cơ chế
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] 7 lượt lệch còn lại trong nhóm shadow — nghi trôi theo thời điểm gọi, chưa chứng minh được
  - [NO_ANOMALY_FOUND] Parser và xử lý Unicode dùng chung 100% — không có nhánh riêng theo model

## DAU VAO LAN SAU

## Điều làn sóng 2 CẦN biết từ gate này

**A. MỘT DÒNG VÁ, ĐÃ ĐỦ BẰNG CHỨNG, CHƯA VIẾT VÁ**
`gpt_analyzer.py:6738` — `_shadow_mode = lane_test_shadow_pack or (selected_model in SHADOW_GATE_MODELS)`. V11160 đã sửa đúng mẫu này ở `:6682` (`_la_shadow_prompt = bool(lane_test_shadow_pack)`) nhưng bỏ sót dòng `:6738`. Vá đúng chuẩn = bỏ mệnh đề theo-model, giống hệt cách V11160 đã làm. **Phải đo trước khi sửa để chắc không mất phạm vi đo** (đúng nếp V11160 đã dùng: ngày 03/09 đo thấy 10/12 model đã đi bằng `lane_test_shadow_pack` sẵn nên bỏ mệnh đề theo-model **mất 0 lượt đo**). Sau vá: `gpt-oss-120b` official phải có `cpc` **bằng** 7 model official cùng ngày/miền.

**B. VÁ NÀY LÀM ĐỨT MỘT CHUỖI ĐO ĐANG CHẠY — phải xử lý §60.2**
`gpt-oss-120b` đã chạy **88 lượt official với gói shadow**. Mọi so sánh chất lượng của model này với 7 model official khác trong 30 ngày qua là **so hai chế độ prompt khác nhau**. Trước khi vá phải quyết: (a) cắt mốc và bắt đầu lại chuỗi đo, hay (b) đánh dấu 88 lượt cũ là `PROMPT_REGIME_KHAC` trong bảng chấm. **Không được vá im lặng rồi tiếp tục cộng dồn số.**

**C. BA THỨ PHẢI VÁ CÙNG LÚC, KHÔNG ĐƯỢC LÀM LẺ (§60.1 — bỏ nửa chừng tệ hơn không làm)**
1. `:6738` mệnh đề theo-model.
2. `SHADOW_GATE_MODELS` — dọn 6 mục RETIRED; sau khi vá `:6738` thì danh sách này chỉ còn dùng cho `_la_shadow` (nhãn), cần rà lại nó còn nghĩa gì không.
3. Chú thích `:985-988` mô tả `SHADOW_GATE_MODELS` là "measurement-only lanes... không đổi `/du-doan` output" — **SAI so với thực tế đo được**, phải sửa hoặc gỡ, nếu không nó sẽ dạy lại chính lối nghĩ đã gây lỗi.

**D. VÁ VÂN TAY PROMPT — nếu không thì mọi cổng "prompt sạch" sau này vẫn nói dối**
Chuyển băm từ `:6723` xuống **sau** `:6762` (sau khi nối đủ `ctx_pack` + `RULEBOOK` + contract). Hiện tại phủ 44,1%. Đồng thời `runtime_prompt_contam_hits` cũng đang đếm trên chuỗi thiếu hơn nửa — con số 4 và 0 hiện tại **chỉ nói về base prompt**, chưa nói gì về gói ngữ cảnh.

**E. BA TRƯỜNG TRACE CẦN THÊM — rẻ, và mở khoá đúng những thứ gate này không đo được**
| Trường | Mở khoá điều gì |
|---|---|
| `prompt_tokens` (lấy từ `response.usage.prompt_tokens`, cả 5 wrapper đều có sẵn) | đếm token đầu vào thật → tính được biên an toàn |
| `context_pack_dropped` (bool) + `context_pack_error` | 36 lượt chạy không ngữ cảnh hiện phải tự suy từ `cpc<=500` |
| `retry_count` + `attempt_latencies` | tách được câu hỏi F: latency 1.429s là một lượt gọi hay một chuỗi retry |

**F. NHÃN PHIÊN BẢN PROMPT PHẢI PHẢN ÁNH REGIME**
`prompt_version=PB-20.1` hiện gắn cho cả hai regime. Đề nghị: `PB-20.1/LEGACY` vs `PB-20.1/CTXONLY`, hoặc t

## CHUA TRA LOI

**1. Đếm token đầu vào THẬT cho từng model — KHÔNG LÀM ĐƯỢC.** `import tiktoken` trên VPS → `ModuleNotFoundError`. Và không tách được `input` khỏi `total_tokens` vì trace chỉ ghi `token_count` tổng. Mọi con số prompt trong gate này là **KÝ TỰ**, không phải token. **Cấm** quy đổi bằng hằng số ước lượng (RM-21).

**2. Context window từng model — INDETERMINATE, không phải "chưa tra".** Nó **không tồn tại trong mã**. Số trong chú thích (`ctx 1M`, `ctx 1.05M`, `max_out 131.072`) là **tài liệu**, RM-14 cấm dùng làm runtime truth. Vì thế cột "ACTUAL usable input budget" và "safety margin đầu vào" của ma trận **để trống có lý do**, không bịa.

**3. NỘI DUNG chính xác của hai gói ngữ cảnh (official vs shadow).** Gate này chứng minh được **cấu trúc** (đúng 2 nhánh `if shadow_mode` sinh nội dung) và **kích thước** (đo thật 88/88 lượt), nhưng **chưa dump** nội dung. Muốn dump phải gọi `build_context_pack` — luật cứng đòi trước đó phải đọc dependency graph, chứng minh không có đường ghi DB/tệp/mạng, chạy trên clone bất biến, monkeypatch chặn mọi hàm ghi, cài bẫy mutation. Chưa làm ⇒ ghi `BLOCKED_BY_SIDE_EFFECT_UNCERTAINTY` cho phần nội dung.

**4. 7 lượt lệch còn lại trong nhóm shadow.** Giả thuyết trôi-theo-thời-điểm hợp lý nhưng **chưa chứng minh** — kiểm chứng đòi dựng lại gói ngữ cảnh ở đúng thời điểm đó. Ghi `SUSPICIOUS_NEEDS_MORE_EVIDENCE`, **không** nâng lên `EXPECTED_BEHAVIOR`.

**5. Tỉ lệ lượt reasoning ăn hết trần đầu ra.** `n=1` cho mỗi model (gemini-2.5-flash, gemini-3.5-flash) ⇒ RM-04: **chưa được phép kết luận** về tỉ lệ. Cơ chế thì tái lập được từ số đo.

**6. Cơ chế thật sau `latency > 300s` mà lượt gọi OpenRouter vẫn THÀNH CÔNG.** `httpx timeout=300.0` (`:4089`) nhưng glm-5.1 có lượt `stop` dài 561,9s (p95) và 1.429,5s (max). Hai khả năng — (a) OpenRouter gửi byte giữ sống làm read-timeout reset; (b) `latency_seconds` gộp cả các lần retry — **không tách được** từ dữ liệu hiện có. Hệ quả: các con số "TB 516s / max 796s" từng dùng để đặt hạn riêng 840s/900s **khôn