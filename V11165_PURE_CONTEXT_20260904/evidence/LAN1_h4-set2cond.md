# h4-set2cond · tang=EVIDENCE_COMPLETE

## TOM TAT

Đã dump prompt THẬT từ hàm đang serve (RM-14) cho 6 biến (3 miền × 2 regime) trên clone bất biến, bẫy mutation sạch, rồi kiểm kê 35 producer sinh/bơm bộ số. Trả lời thẳng: prompt MN official ngày 04/09 mang 27 khối mốc, 25 khối có số, trong đó khoảng 23 là AGGREGATED_NUMBER_SET (đã xếp hạng/lọc/top-k/chấm điểm) và chỉ 2 là RAW_NUMBER_FACT — tổng cộng bơm 83/100 đuôi của toàn vũ trụ dưới 23 nhãn khác nhau. Lane «ngữ cảnh thuần» (CONTEXT_ONLY_V2) chỉ gỡ 3 khối trong ~30 và THÊM 4 khối; nó vẫn ăn TOP 5 GỢI Ý, GAN CAO, HOT, ĐỀ XUẤT PYTHON, SỐ NÊN TRÁNH, OVERDUE (sắp về), HOT BY GAP, WR của chính model, và ở MB cả bảng xếp hạng model. Bộ 5 dấu ô nhiễm của V11160 báo contam=0 cho lane đó trong khi 12–14 dấu meta-hệ-thống VẪN CÓ trong đúng chuỗi ấy — tức con số «60/60 sạch» của V11164 KHÔNG được đọc thành «prompt sạch». gan/hot/cold chưa hề bị gỡ: V11001/V11007 chỉ gỡ phía gpt_analyzer, còn statistical_analyzer, feature_engineering và metrics_calculator vẫn bơm mỗi lượt. Nặng nhất là P07: prompt đưa sẵn ĐÁP ÁN («ĐỀ XUẤT PYTHON: 02 (score=13), 28 (score=13)» — đúng dạng main+secondary của hợp đồng đầu ra) rồi ra lệnh «ưu tiên Python metrics», cộng với «KHÔNG tự tạo số mới nếu Rule Tails đã có gợi ý mạnh» — model không còn tự chọn. Chỉ 1/35 producer (MINED RULES) có nền tường minh và có đoạn tự phủ định mức bằng chứng; 34 producer còn lại không có nền, không hiệu chỉnh bội, không bằng chứng ngoài mẫu.

## TRA LOI

CÓ BAO NHIÊU AGGREGATED_NUMBER_SET ĐANG ĐƯỢC BƠM VÀO PROMPT HÔM NAY (04/09/2026)?

Đo trên dump thật, MN|OFFICIAL_LEGACY (50.464 ký tự): 27/30 khối mốc có mặt, 25 khối mang số, trong đó ~23 là AGGREGATED_NUMBER_SET và 2 là RAW_NUMBER_FACT (KẾT QUẢ NGÀY TRƯỚC; phần ĐB/G8 của LỊCH SỬ ĐÀI). MN|SHADOW_CONTEXT_ONLY (53.877 ký tự): bỏ đúng 1 bộ có số (SỐ ĐÃ TRÚNG GẦN ĐÂY) và THÊM 2 bộ (PHASE-STATE, LANE-TEST addon) ⇒ ~24 bộ. MB nhiều hơn vì có thêm MB RULE STACK và MB HARD MODE. Tổng kiểm kê mã: 35 producer, 27 bơm bộ số tổng hợp, 2 raw fact.

Hợp lại, các bộ này phủ 83/100 đuôi trong prompt MN official — tức gần trọn vũ trụ được trình như «tín hiệu» dưới 23 nhãn khác nhau, nên bất kỳ số nào model chọn cũng biện minh được.

MỖI BỘ ĐẾN TỪ ĐÂU — 6 nguồn:
1. `lottery_results` qua statistical_analyzer + feature_engineering (P01–P05, P11, P12, P14, P15, P16, P17, P20) — sự kiện xổ số thật.
2. `source_data` trong bộ nhớ qua metrics_calculator (P07, P08, P09) — sự kiện thật, nhưng bị chấm điểm và chọn sẵn.
> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18). Phiên này **không** tuyên bố
> hiệu quả của luật khai mỏ, nên cả bốn vế — **trong cửa sổ chọn · ngoài cửa sổ chọn · trong mẫu ·
> ngoài mẫu** — đều để trống có chủ ý. Bộ đủ nằm ở **RM-18/V11030** (**+7,5 / +13,8 / +20,7 điểm
> TRONG cửa sổ chọn, ĐÚNG BẰNG 0 ngoài cửa sổ**) và **V11073** (**+9,9% trong mẫu → −1,6% ngoài
> mẫu**). Đo bổ sung của phiên này: **n = 20/miền trên 4 ngày** ⇒ **RM-04, chưa được phép kết
> luận**; KTC95 đều chứa 0. Báo một vế là giấu mất nửa sự thật.
3. `mined_rules` + `mined_rule_effectiveness` qua context pack (P21–P28, P30, P34).
4. `predictions` — DỰ ĐOÁN CỦA CHÍNH HỆ (P10, P13, P30, P31, P32, P35). Đây không phải sự kiện nguồn.
5. TỆP TĨNH `_knowledge_base.json` (P18, P19) — mtime 2026-04-26, đóng băng 131 ngày.
6. `final_bundles` — OUTPUT CÔNG BỐ của chính hệ (P33), chỉ ở lane shadow.

> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18). Phiên này **không** tuyên bố
> hiệu quả của luật khai mỏ, nên cả bốn vế — **trong cửa sổ chọn · ngoài cửa sổ chọn · trong mẫu ·
> ngoài mẫu** — đều để trống có chủ ý. Bộ đủ nằm ở **RM-18/V11030** (**+7,5 / +13,8 / +20,7 điểm
> TRONG cửa sổ chọn, ĐÚNG BẰNG 0 ngoài cửa sổ**) và **V11073** (**+9,9% trong mẫu → −1,6% ngoài
> mẫu**). Đo bổ sung của phiên này: **n = 20/miền trên 4 ngày** ⇒ **RM-04, chưa được phép kết
> luận**; KTC95 đều chứa 0. Báo một vế là giấu mất nửa sự thật.
CÓ BASELINE KHÔNG? 1/35. Chỉ P21 (MINED RULES) có cột `lợi thế/nền` (V11094/FU-404) và kèm đoạn CÁCH ĐỌC tự phủ định («z = −0,33/+0,26 ngang bằng luật giả», «0/105 luật qua cổng đo tiến»). P25 có đoạn tự phủ định nhưng không có nền số. 33 producer còn lại: không nền, không z, không hiệu chỉnh so sánh bội. Nặng nhất: P15 quét 4.950 cặp rồi báo top-5 mà không hiệu chỉnh; P27 in 5 dòng «100.0%» với n=2–5; P23 in «6W: 92%» cho phép đếm hit_any của bộ 3–4 số mà nền đúng phải là 1−(1−b)^k (RM-18).

CÓ CUTOFF KHÔNG? Có và đúng: P01–P05, P07–P09, P11–P17, P20, P23–P29. Thiếu hoặc sai: P10 (không có `date < target_date`, chỉ `ORDER BY date DESC LIMIT 7`), P22 (dùng `date('now','-2 days')` thay vì `date_str`), P32/P35 (dùng `date('now')`), P21/P34 (không có điều kiện thời gian), P18/P19 (tệp tĩnh, không neo ngày nào).

## PHAT HIEN
  - [PROVEN_DEFECT] «Ngữ cảnh thuần» chỉ gỡ 3 khối trong ~30 — 23 bộ số tổng hợp và toàn bộ meta-hệ-thống khác VẪN Ở NGUYÊN
  - [PROVEN_DEFECT] Bộ 5 dấu ô nhiễm của V11160 báo contam=0 cho lane ngữ cảnh thuần trong khi 12–14 dấu meta-hệ-thống vẫn có trong đúng chuỗi đó
  - [PROVEN_DEFECT] gan/hot/cold CHƯA HỀ bị gỡ — V11001/V11007 chỉ gỡ phía gpt_analyzer, ba nguồn khác vẫn bơm mỗi lượt
  - [PROVEN_DEFECT] Prompt đưa sẵn ĐÁP ÁN đúng dạng hợp đồng đầu ra rồi ra lệnh cho model ưu tiên đáp án đó
  - [PROVEN_DEFECT] Nguồn CHẾT vẫn được ĐỌC mỗi lượt: `_knowledge_base.json` đóng băng 131 ngày, và nó mâu thuẫn với khối live trong CÙNG một prompt
  - [PROVEN_DEFECT] Mệnh lệnh trỏ vào khối bằng TÊN và CỬA SỔ không tồn tại — cổng mồ côi hiện có không bắt được
  - [PROVEN_DEFECT] Hai câu ngược nhau về giờ xổ trong cùng một prompt MB, và cả hai đều khác mốc khoá của dự án
  - [PROVEN_DEFECT] Hai dòng LIÊN TIẾP bảo ngược nhau về cùng một phép đo gap
  - [PROVEN_DEFECT] De-herding bỏ sót MB HARD MODE — bảng xếp hạng model vẫn vào cả lane ngữ cảnh thuần
  - [PROVEN_DEFECT] Lane «ngữ cảnh thuần» là lane DUY NHẤT được ăn OUTPUT CÔNG BỐ của chính hệ
  - [PROVEN_DEFECT] `DIGIT SUM (winning)` không phải đặc trưng của kỳ xổ — là đặc trưng của DỰ ĐOÁN THẮNG của chính hệ
  - [PROVEN_DEFECT] MB RULE STACK đang BẬT trên official MB — và suýt bị kết luận nhầm là TẮT vì đo sai nguồn
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] Phase 15 thiếu chặn as-of — khe hở CÓ THẬT trong mã, nhưng 30 ngày qua KHÔNG có lượt production nào bị rò
  - [OPERATIONAL_IMPROVEMENT] Chỉ 1/35 producer có nền tường minh — và khuôn mẫu ĐÚNG đã có sẵn trong chính kho này
  - [PROVEN_DEFECT] Gần trọn vũ trụ 100 đuôi được trình như «tín hiệu» dưới 23 nhãn khác nhau

## DAU VAO LAN SAU

ĐIỀU LÀN SÓNG 2 CẦN BIẾT TỪ GATE NÀY:

A. CON SỐ NEO — dùng thẳng, đã tái lập được
   · prompt thật 04/09: MN 50.464 / MT 51.487 / MB 55.178 (official); MN 53.877 / MT 54.571 / MB 58.124 (context-only)
   · 35 producer · 27 bơm bộ số tổng hợp · 2 raw fact · 1/35 có nền
   · 83/100 đuôi được bơm vào MN official
   · CONTEXT_ONLY_V2 gỡ 3 khối (MN) / 2 khối (MB), THÊM 4 / 2
   · bộ 5 dấu V11160 = 0 trong khi dấu meta thật = 12 (MN) / 11 (MT) / 14 (MB)
   · `_knowledge_base.json` mtime 2026-04-26 (131 ngày)
   · gpt_analyzer.py sha16 = 758c29c13185763f (KHỚP gate 0, không đổi trong suốt phiên)

B. BỐN ĐIỂM VÀO ĐỘC LẬP — đụng một chỗ KHÔNG sửa được ba chỗ kia (§60.2 câu 1)
   1. `create_analysis_prompt` gpt_analyzer.py:2221-3212 — thân prompt (P01..P20, P31, P32)
   2. `build_context_pack` gpt_analyzer.py:4831-5937 — gói ngữ cảnh (P21..P30, P34, P35)
   3. Ba module ngoài: statistical_analyzer.py · metrics_calculator.py · feature_engineering.py
      — ĐÂY LÀ CHỖ V11001/V11007 BỎ SÓT. Mọi lần «gỡ gan/hot/cold» chỉ đụng gpt_analyzer đều sẽ sót lại.
   4. `_build_lane_test_shadow_doctrine_addon` gpt_analyzer.py:6370-6533 — riêng lane shadow

C. THƯỚC ĐANG DÙNG LÀ THƯỚC HỎNG — sửa thước TRƯỚC khi đo lại bất cứ gì
   · `_dau_o_nhiem` (gpt_analyzer.py:6712) chỉ 5 chuỗi, bỏ sót 12-14. Mọi kết luận «lane sạch» dựa trên nó đều vô giá trị.
   · `_V10768_HERD_SECTION_KEYS` (gpt_analyzer.py:4598) chỉ 4 chuỗi, khớp theo header `### ` — bỏ sót `### 🔴 MB HARD MODE`. Đây là lần THỨ HAI cùng họ lỗi (V11106 đã vá ca `  📊 MB MODEL RANKING`). RM: một RM tái phạm hai lần ⇒ phải dựng cổng máy.
   · `_v11107_cong_prompt_mo_coi.py` chỉ khớp khuôn «Khi … có "X"» — không bắt được F6 (tên/cửa sổ sai), F7/F8 (hai câu ngược nhau), F5 (nhãn nói sai về chính nó). Chính tệp đó đã tự khai giới hạn này ở đầu file.
   ⇒ Đề nghị: dựng MỘT cổng đo trên DUMP THẬT thay vì đếm chuỗi trên mã, lấy 35 producer_id của artifact này làm danh sách bắt buộc-có-mặt/bắt-buộc-vắng-mặt theo regime.

D. THỨ TỰ ƯU TIÊN ĐỀ NGHỊ (nặng → nhẹ), tất cả đều là ứng viên vá TRONG artifacts/, chưa deploy
   1. P07 BLOCK_ORACLE — gỡ `ĐỀ XUẤT PYTHON` + hai mệnh lệnh «ưu tiên Python metrics». Đây là chỗ duy nhất prompt đưa thẳng đáp án đúng dạng hợp đồng đầu ra.
   2. RULEBOOK §11 «KHÔNG tự tạo số mới nếu Rule Tails đã có gợi ý mạnh» (gpt_analyzer.py:639) — câu này một mình đóng cửa mục tiêu owner #2.
   3. P02/P03/P08/P11/P12 DROP_UNSUPPORTED — họ gan/hot/cold, đã có bằng chứng đo 6,5 năm là không hơn nền.
   4. P10/P13/P35 DROP_MODEL_META — meta của chính hệ còn trong lane «ngữ cảnh thuần».
   5. P18/P19 BLOCK_AMBIGUOUS 

## CHUA TRA LOI

1. PROVIDER ADAPTER — chưa quét mảnh prompt ẩn trong retry/fallback của `_call_openai` (3215-3387), `_call_anthropic` (3390-3515), `_call_gemini` (3518-3629), `_call_deepseek` (3632-3721), `_call_xai` (3724-3782), `_call_openrouter` (3949-4324). Gate yêu cầu nhóm này; phiên sau phải đọc từng nhánh retry.

2. BA NHÁNH TẮT — chưa đo nội dung vì không kích hoạt được mà không đụng production:
   · `PHASE_FIRST_JSON_CONTRACT` (gpt_analyzer.py:1052) — chỉ bơm khi `selected_model in PHASE_FIRST_CONTRACT_MODELS`; đo được tập này = [] rỗng trên service đang chạy.
   · `MNMT_DOCTRINE_SHADOW_RUNNER` — không có trong .env, không có trong /proc/PID/environ, và khối MN/MT layered vắng trong dump ⇒ TẮT (đối chiếu hai nguồn).
   · `OPUS_SYSTEM_PROMPT` (nhánh `rule_brave_mode=1`) — chưa đo.

3. PHASE 20 LEGACY PATTERN RULES (gpt_analyzer.py:2756-2865) — `get_pattern_rules` trả rỗng cho cả ba bucket ngày 04/09 nên khối không xuất hiện. Nó có `suggested_numbers` (rổ số tường minh, cap 10 luật) + `_build_rule_cross_reference` (1917-2218) sinh dữ liệu 4 tuần kèm dấu 🔥HỘI TỤ / ⚡CHỐT GẤP. Chưa đo khi có dữ liệu — đây là bộ số tiềm năng lớn còn ngoài bảng.

4. LANE `/du-doan-test` (`_v11160_test_lane.py`, `_du_doan_test_engine.py`) — chưa đo. Doctrine MB nói MANUAL «có thể DRIVE ở /du-doan-test», tức lane đó có luật chọn số khác.

5. GIÁ TRỊ CỤ THỂ CỦA TỪNG BỘ SỐ — dump chạy ~23:20 chứ không phải giờ dự đoán thật (ai_chain 09:36-10:45 · auto_daily 22:00 · shadow_auto_eval 09:41-22:45, đo từ `predictions.created_at`). Mọi khối dùng `date('now')` hoặc thiếu chặn as-of (P10, P22, P32, P35, các mục context pack `-14 days`) thấy NHIỀU dữ liệu hơn lượt thật. CẤU TRÚC không bị ảnh hưởng (khối nào tồn tại, xếp hạng ra sao, có nền không) — nhưng CẤM trích các giá trị như «bộ số model đã nhận lúc 09:36». Xem DC-02.

6. SỐ ĐUÔI ĐẾM ĐƯỢC TỪ DUMP — bản trích regex đầu SAI (bỏ sót số có dấu phẩy ngay sau: `🔥 HOT: 11, 16, 23, ...` đếm thành 1 thay vì 8); bản sau đã dọn nhiễu trước nhưng có thể DỌN QUÁ TA