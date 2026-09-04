# gate2 · tang=PARTIAL · 8 phat hien

## TOM TAT

Đã kiểm TOÀN BỘ 84 lượt ngày 04/09 (60 lượt LLM có trace + 24 lượt ML/ensemble không có prompt LLM), không lấy mẫu: định tuyến regime prompt đúng 60/60 — 27 lượt official đều `LEGACY_PROMPT` (contam=4), 33 lượt shadow đều `CONTEXT_ONLY_V2` (contam=0), 60 vân tay sha256 khác nhau, 0 thiếu, 0 trùng; không một model `CONTEXT_ONLY_V2` nào bỏ phiếu vào ba bundle 825/827/829. Bản vá V11160 chứng minh được ở runtime: `gpt-oss-120b` ngày 03/09 ăn `CONTEXT_ONLY_V2` ở hai lượt OFFICIAL (MT 16:41:49, MB 17:32:44), ngày 04/09 cả ba lượt về `LEGACY_PROMPT`. NHƯNG bốn chỗ chưa đóng được: (1) định tuyến theo MODEL **vẫn còn** ở `gpt_analyzer.py:6738` — `gpt-oss-120b` là model official duy nhất nhận gói ngữ cảnh SHADOW-GATE (14142/14536/18427 ký tự, **đúng bằng** gói của lane thí nghiệm) trong khi 7 model official khác nhận 10977/11557/15448, và nó bỏ phiếu top-1 vào bundle 825 và 829; (2) vân tay prompt chỉ băm **40,1–48,4%** chuỗi thật vì băm ở `:6723` TRƯỚC khi nối ctx_pack + RULEBOOK ở `:6755-6762`; (3) `gpt-oss-120b` không có lượt shadow nào ngày 04/09 (lượt cuối 01/08/2026) nên kiểm bắt buộc số 2 là INDETERMINATE_NOT_EXERCISED, và phạm vi đo ngữ cảnh thuần tụt 12 → 11 model — câu «bỏ mệnh đề theo-model mất 0 lượt đo» trong chú thích V11160 **sai**; (4) mọi dòng `print()` ngừng vào journal từ 16:53:48 nên cả cohort MB (19 lượt) không có đối chứng journal. Không có mutation nào trên production: PID 3370750 nguyên, NRestarts 0, neo558 NGUYÊN, bốn bảng khoá y hệt Gate 0.

## TRA LOI CAU HOI

**1) SCHEDULED_LANE_ROUTING_PROVEN ?** → **PROVEN.** 60/60 lượt khớp kỳ vọng. Luật kỳ vọng lấy từ code chứ không đoán: `regime_prompt_cho_luot()` (`gpt_analyzer.py:935-950`) chỉ nhận `lane_test_shadow_pack`, và `lane_test_shadow_pack=True` chỉ được truyền từ `scheduler.py:7690` (đường `shadow_auto_eval`). Đối chiếu `predictions.run_source` × `trace.context_only_regime`: 27 lượt `auto_daily`/`ai_chain` → `LEGACY_PROMPT` (27/27), 33 lượt `shadow_auto_eval` → `CONTEXT_ONLY_V2` (33/33). Không một FAIL, không một INDETERMINATE trong 60 lượt.

**2) SCHEDULED_SHADOW_PROMPT_CLEAN_PROVEN ?** → **PROVEN NHƯNG PHẠM VI HẸP HƠN CÂU CHỮ.** 33/33 lượt `CONTEXT_ONLY_V2` có `runtime_prompt_contam_hits = 0`, và đây là bằng chứng NỘI DUNG (băm chuỗi sắp gửi ở `:6723-6726`), không phải cờ tự khai. Ba giới hạn phải ghi kèm, nếu bỏ là tự nâng tầng: (a) vân tay chỉ phủ **40,1–42,9 %** chuỗi thật, phần ctx_pack + lane addon + RULEBOOK nối SAU khi băm nên nằm ngoài phép đếm; (b) bộ 5 dấu ô nhiễm **không phủ** khối Phase 11 «📊 HIỆU SUẤT GẦN ĐÂY / Win Rate: X%» — chuỗi in ra là `Win Rate` chứ không phải `win_rate`, nên khối đó có lọt vào cũng đếm ra 0; (c) dấu Phase 11 duy nhất trong bộ («SỐ ĐÃ TRÚNG GẦN ĐÂY») ngày 04/09 **không hề được bơm** (journal: `[Phase 11] Injected N recent winning numbers` = **0 dòng**), nên nó không phân biệt được gì trong ngày này. Chốt chặn Phase 11 ở lane shadow vẫn đứng — nhưng đứng bằng **đọc code + 19 dòng journal `[Phase 11][CONTEXT_ONLY_V2] BỎ QUA`**, không phải bằng con số `contam=0`.

**3) OFFICIAL_CONTROL_COHORT_CLEAN_ON_04_09 ?** → **SẠCH VỀ REGIME, KHÔNG ĐỒNG NHẤT VỀ NỘI DUNG.** 27/27 lượt official đều `LEGACY_PROMPT`, `is_shadow_lane=False`, `contam=4` giống hệt nhau — không lượt official nào ăn prompt thí nghiệm. Nhưng cohort này **không dùng làm đối chứng đồng nhất được**: `gpt-oss-120b` nhận gói ngữ cảnh SHADOW-GATE 14142/14536/18427 ký tự, **đúng bằng gói của lane thí nghiệm**, trong khi 7 model official cùng miền nhận 10977/11557/15448 — chênh **+2.979 … +3.165 ký tự**. Nguyên nhân là `gpt_analyzer.py:6738` còn `_shadow_mode = lane_test_shadow_pack or (selected_model in SHADOW_GATE_MODELS)`, tức vẫn định tuyến **theo MODEL**.

**4) Có model nào nhận SAI prompt nhưng VẪN bỏ phiếu không ?** → **KHÔNG, theo nghĩa regime.** 0/3 bundle có voter thuộc nhóm `CONTEXT_ONLY_V2`; cả ba bundle chỉ có đúng 8 voter LLM và cả 8 đều là lượt `LEGACY_PROMPT`. **NHƯNG** phải nói tiếp cho đủ: `gpt-oss-120b` — model nhận gói ngữ cảnh khác 7 model official còn lại — **có bỏ phiếu ở cả ba miền**, và là voter của **top-1** ở bundle 825 (`53`) và bundle 829 (`86`, chính là bạch thủ MB công bố). Nên câu trả lời đúng là: *không có model nào nhận sai REGIME mà vẫn bỏ phiếu; nhưng có đúng một model bỏ phiếu với NGỮ CẢNH khác hẳn phần còn lại của cohort official.*

**5) Có trace thiếu vân tay hoặc dùng vân tay stale không ?** → **KHÔNG.** 60/60 dòng có `runtime_prompt_sha256`, `runtime_prompt_chars`, `runtime_prompt_contam_hits` đầy đủ; **60 giá trị sha256 khác nhau hoàn toàn**, 0 trùng lặp, 0 rỗng; journal có **0 dòng** `[PROMPT_FINGERPRINT]` (nhánh bắt lỗi băm) và **0 dòng** `[CONTEXT_PACK][VO]`. Ghi thêm cho trung thực: vì ngữ cảnh đổi theo thời gian nên sha khác nhau là điều **dễ đạt**, phép kiểm này chứng minh «không stale», **không** chứng minh «vân tay đủ mạnh» — cái đó bị giới hạn phạm vi 40–48 % ở câu 2.

---

**NĂM KIỂM BẮT BUỘC CHO `gpt-oss-120b`** (model duy nhất ở giao `SHADOW_GATE_MODELS × output_eligible`, đã kiểm lại bằng code chứ không trích báo cáo cũ):

| # | nội dung | kết quả | bằng chứng |
|---|---|---|---|
| 1 | Official phải dùng legacy/official prompt | **PASS** | 3/3 lượt (MN 05:18:24 · MT 16:42:25 · MB 17:33:20) `LEGACY_PROMPT`, `is_shadow_lane=False`, `contam=4`; journal 2 dòng `[CONTEXT_ONLY_V2][V11160] … lượt NÀY là OFFICIAL → GIỮ prompt cũ` |
| 2 | Shadow phải dùng `CONTEXT_ONLY_V2` | **INDETERMINATE_NOT_EXERCISED** | 0 lượt `shadow_auto_eval` ngày 04/09; lượt shadow gần nhất `2026-08-01T05:20:52`. **Không tự nâng thành PASS** |
| 3 | Không còn routing dựa sai vào model membership | **FAIL** | `gpt_analyzer.py:6738` còn `or (selected_model in SHADOW_GATE_MODELS)`; hệ quả đo được ở Bảng 3 |
| 4 | Mọi lượt `CONTEXT_ONLY_V2` phải có `contam = 0` | **PASS** | 33/33 = 0 |
| 5 | Vân tay phải đến từ prompt runtime THẬT | **PARTIAL** | băm chuỗi thật (`system_prompt + "\n<<<USER>>>\n" + prompt`) chứ không phải cờ tự khai, nhưng băm ở `:6723` TRƯỚC khi nối ctx_pack/RULEBOOK ở `:6755-6762` ⇒ phủ 40–48 % |


## PHAT HIEN (tieu de)
  - [EXPECTED_BEHAVIOR] Định tuyến regime prompt theo LƯỢT đúng 60/60 — bản vá V11160 chứng minh được ở runtime, không phải bằng cờ tự khai
  - [PROVEN_DEFECT] Định tuyến THEO MODEL vẫn chưa gỡ hết: `gpt-oss-120b` là model official DUY NHẤT nhận gói ngữ cảnh SHADOW-GATE, và nó bỏ phiếu top-1 vào hai bundle
  - [PROVEN_DEFECT] Vân tay prompt runtime chỉ băm 40,1–48,4 % chuỗi thật — `contam_hits = 0` KHÔNG chứng minh cả prompt sạch
  - [PROVEN_DEFECT] Bộ 5 dấu ô nhiễm có điểm mù: khối Phase 11 «Win Rate» KHÔNG bị bộ dấu nào bắt, và dấu Phase 11 duy nhất trong bộ thì ngày 04/09 không hề xuất hiện
  - [PROVEN_DEFECT] Câu biện minh của V11160 «bỏ mệnh đề theo-model mất 0 lượt đo» SAI — mất đúng 1 model, và model đó không có đường quay lại
  - [PROVEN_DEFECT] Mọi dòng `print()` ngừng vào journal từ 16:53:48 — cả cohort MB (19 lượt) không có đối chứng journal, chỉ còn trace
  - [OPERATIONAL_IMPROVEMENT] `SHADOW_GATE_MODELS` là danh sách đã chết 6/8 — nhưng vẫn đang lái nội dung prompt của đường official
  - [INDETERMINATE] 60 lượt gọi LLM nhưng chỉ 57 dòng `predictions` — ba lượt gọi lại trong cùng lane official, chưa chứng minh được cơ chế

## CHUA TRA LOI DUOC

**1. Kiểm bắt buộc số 2 cho `gpt-oss-120b` («shadow run phải dùng CONTEXT_ONLY_V2») — INDETERMINATE_NOT_EXERCISED, không phải PASS.** Ngày 04/09 model này không có một lượt `shadow_auto_eval` nào (lượt cuối 2026-08-01T05:20:52) nên sự kiện cần kiểm **không xảy ra**. Không có raw runtime evidence ⇒ theo đúng luật gate, ghi INDETERMINATE. Và vì nó không nằm trong `SHADOW_AUTO_EVAL_MODELS`, sự kiện này sẽ **không tự xảy ra** ở các ngày sau — muốn đóng thì phải có quyết định owner đưa nó vào roster shadow, tôi không mở việc đó.

**2. Ảnh hưởng của gói ngữ cảnh SHADOW-GATE lên con số dự đoán của `gpt-oss-120b` — CHƯA ĐO.** Tôi chứng minh được prompt khác (+2.979…+3.165 ký tự) và chứng minh được nó bỏ phiếu top-1 vào bundle 825 và 829. Tôi **không** chứng minh được lá phiếu đó khác đi vì gói ngữ cảnh khác. Muốn kết luận phải chạy đối chứng — mà đối chứng nào cũng cần gọi lại model, tức chạm production; và làm sau khi đã biết kết quả 04/09 là vi phạm luật cấm ORACLE. Ghi NOT PROVEN, không suy luận lấp chỗ trống.

**3. Nội dung ctx_pack có chứa dấu ô nhiễm hay không — CHƯA ĐO TRỰC TIẾP.** Đây là phần lớn nhất nằm NGOÀI vùng băm vân tay (10.977–18.427 ký tự, tức 20–32 % chuỗi thật). Tôi cố ý **không** gọi `build_context_pack()` vì không chứng minh trước được nó chỉ đọc, mà luật cứng là production read-only tuyệt đối. Hai khối còn lại nối sau khi băm thì đã kiểm tĩnh và sạch (`REASONING_RULEBOOK` 15.256 ký tự → 0 dấu, `PHASE_FIRST_JSON_CONTRACT` 1.343 → 0 dấu). Riêng ctx_pack: chỉ biết `_deherd_strip_ranking()` đã gỡ khối xếp hạng WR/BT khỏi nó (journal 38 dòng `[V10768-DEHERD]`, ví dụ MN `12135→10977`), **không biết** phần còn lại có dấu nào không.

**4. Nguyên nhân gốc của việc `print()` ngừng vào journal lúc 16:53:48 — CHƯA TÌM RA.** Triệu chứng PROVEN (0 dòng print từ 16:53:48 đến 20:50, xác nhận trên journal SỐNG, đã loại trừ rate-limit). Nghi `_safe_print` / `_safe_stdio_ctx` (`gpt_analyzer.py:43-66`) nhưng chưa tái lập được, và tái lập sẽ phải chạm tiến trình service 