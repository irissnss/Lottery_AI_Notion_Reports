# g1-region-ledger · tang=EVIDENCE_COMPLETE · 11 phat hien

## TOM TAT

Ngày 04/09 chạy SẠCH về vận hành: 3/3 miền có bundle đúng hạn, 24/24 lượt AI official trả kết quả, 0 dòng ERROR, 0 timeout cứng, 0 parse lỗi, 0 output rỗng, 0 late. Nhưng lớp ĐO LƯỜNG thì hỏng: cap V10752 (cố ý bỏ 2 model yếu nhất của MT) bị đọc ngược thành «bundle thiếu model» — day_governance ghi nguyên văn «Thiếu 2 model (13/15)» trong khi cả hai model đều chạy xong và đều PASS gate, khiến MT bị gắn DEGRADED_LIVE_DAY + EXCLUDE_PRIMARY và bị loại khỏi rolling WR/TOP1; 90 ngày qua MT bị loại 72/90 lượt (80,0%) so với MN 10/91 (11,0%). Kèm theo là ba lỗi nhãn/khoá tái lập được: `wr_gate_filtered` chứa model bị cap dù `gate_diagnostics` ghi pass=true (70/144 ngày), combo-super luôn in `models=0` vì `scheduler.py:3977` đọc khoá `models_used` mà `combo_super.py` không bao giờ trả, và 100% dòng lane `rerun_post_mt` của MB mang run_id tiền tố `MT_`. Điểm sáng: V11160 kín — 33/33 lượt shadow có `runtime_prompt_contam_hits=0` và 0/24 lượt official chạy prompt CONTEXT_ONLY_V2, đây là bằng chứng NỘI DUNG chứ không phải cờ tự khai. MT thắng bạch thủ 28 (BT/lo2/xiên2 WIN), MN và MB trượt bạch thủ — một ngày, cấm suy ra model tốt/xấu.

## TRA LOI CAU HOI

**Giờ chạy THẬT (lấy từ scheduler_logs naive-UTC +7, journal, và predictions.created_at — không lấy từ tài liệu):**
- MN: free_predict 05:00:09→05:00:13 (run_id MN_2026-09-04_965ccff1) · ai_chain CASCADE_STAGE_START 05:15:00 → END 05:21:04 (363,7s, run_id MN_2026-09-04_7fda2f5a) · bundle 825 tạo 05:21:04 · mốc đóng băng 15:45 → sớm 10h24
- MT: free_predict 05:00:00→05:00:09 (MT_..._c5e5a2a4) · ai_chain 16:40:11 → 16:46:00 (349,0s, MT_..._ade66018) · bundle 827 tạo 16:46:00 · mốc 16:58 → sớm 12 phút
- MB: ai_chain 17:30:33 → 17:33:41 (188,0s, MB_..._971b6db2) · bundle 829 tạo 17:33:41 · mốc 17:58 → sớm 24 phút. MB **không có dòng predictions nào tạo trước 17:00** dù journal ghi free_predict MB chạy 05:00:13–05:00:17 và POST_BATCH xác nhận 21/21 dòng no-token lúc 05:00:17.

**Phân loại prediction_trace (60 dòng ngày 04/09, KHÔNG 1:1 với 81 dòng predictions):**
| loại | n | ghi chú |
|---|---|---|
| scheduled production invocation | 24 | 8 model AI × 3 miền |
| post-bundle replay | 0 | không có dòng nào sau mốc bundle mà thuộc lượt official |
| emission-only (không có dòng DB) | 0 | |
| diagnostic (shadow_auto_eval) | 33 | 11 × 3 miền |
| duplicate | 3 | MN gemini-2.5-pro 05:21:04 · MN claude-opus-4-6 05:20:24 · MT gemini-2.5-flash 16:46:00 — trùng đúng giờ combo-super, là lượt gọi NỘI BỘ của combo-super ghi dưới tên model thành viên |

Đối chiếu: 24+33+3 = 60 = tổng dòng trace ✓. 24 cặp (miền,model) có trong predictions mà KHÔNG có trace — toàn bộ là 7 model ML no-token + combo-super mỗi miền (chúng không gọi provider nên không sinh trace) ✓.

**Reconciliation các số tổng:** 81 dòng predictions = 48 official (16/miền) + 33 shadow. 16 official/miền = 15 roster output-eligible + combo-no-token (KHÔNG nằm trong roster, `model_registry.get_output_eligible_ids()` trả đúng 15 id, không có combo-no-token) ⇒ `output_eligible_row_count=15` khớp cả ba miền. MN/MB: scoreable = 15 = model_count bundle ✓. MT: scoreable = 13, chênh **2** — giải thích HOÀN TOÀN bởi cap V10752 (`(15−13) == 2 dòng max_voters_cap`), không phải lỗi.

**empty (RM-09, đọc JSON ra list rỗng chứ không đếm chuỗi):** 0/48 dòng official. Mọi dòng parse ra list và khớp `pick_count`. **timeout cứng:** 0 — bằng chứng: 0 dòng ERROR trong scheduler_logs, trace `timeout_or_fallback=False` 60/60, `finish_reason` chỉ có stop/FinishReason.STOP/end_turn, không có 'length'. ⚠️ **KHÔNG dùng `bundle.hard_timeout_models` làm bằng chứng** — nó là hằng số `[]` viết cứng ở `main.py:10504`. **truncated / malformed JSON:** 0, suy từ `finish_reason` không có giá trị cắt và 0 dòng parse_err. **late:** 0/81 (`predictions.late` toàn 0). 9 lần `SOFT_CONTINUE_90S` là chờ mềm, không phải timeout — cả 9 model đều về sau đó với status `OK_AFTER_SOFT_CONTINUE_90S`.


## PHAT HIEN (tieu de)
  - [PROVEN_DEFECT] Cap V10752 cố ý bị đọc ngược thành «bundle thiếu model» — MT bị loại khỏi đo lường chính 80% số ngày
  - [PROVEN_DEFECT] Trường `wr_gate_filtered` dán nhãn sai: chứa model bị CAP trong khi `gate_diagnostics` ghi pass=true
  - [PROVEN_DEFECT] combo-super luôn ghi `models=0` vì lệch TÊN KHOÁ giữa combo_super.py và scheduler.py
  - [PROVEN_DEFECT] run_id sai tiền tố miền cho TOÀN BỘ lane rerun_post_mt của MB
  - [PROVEN_DEFECT] `bundle.hard_timeout_models` là hằng số rỗng viết cứng — không dùng được làm bằng chứng «không có timeout»
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] MB: journal xác nhận 21/21 dòng no-token lúc 05:00 nhưng DB không còn dòng MB nào tạo trước 17:00
  - [NO_ANOMALY_FOUND] V11160 KÍN — lần đầu có bằng chứng NỘI DUNG (không phải cờ tự khai) rằng lane shadow sạch và official không ăn prompt thí nghiệm
  - [OPERATIONAL_IMPROVEMENT] Hai bẫy đọc log: `[MODEL_CALL_START]` in sai giờ khi bể song song bật, và `strength` trong log là giá trị TRƯỚC hình phạt DIVERSITY
  - [OPERATIONAL_IMPROVEMENT] combo-super gọi model nội bộ nhưng prediction_trace ghi dưới TÊN MODEL THÀNH VIÊN, không có dòng nào tên combo-super
  - [EXPLORATORY_PREDICTIVE_SIGNAL] Cả ba miền: số «strongest candidate» nằm trong tập đuôi kết quả, còn bạch thủ công bố chỉ trúng 1/3 — MỘT NGÀY, CHƯA ĐƯỢC PHÉP KẾT LUẬN
  - [EXPECTED_BEHAVIOR] combo-no-token không vào bundle và `min_strength_for_voting=3.0` không thi hành — cả hai ĐÚNG THIẾT KẾ, không phải lỗi

## CHUA TRA LOI DUOC

**1. Cột «scheduler expected time» chỉ suy được từ giờ chạy thật, chưa đọc thẳng cấu hình lịch.** Tôi lấy mốc kỳ vọng từ hành vi quan sát (free_predict 05:00, ai_chain MN 05:15 / MT 16:40 / MB 17:30) và mốc đóng băng từ hằng số đã khoá (MN 15:45 · MT 16:58 · MB 17:58). Chưa dump bảng job của APScheduler trong tiến trình đang chạy để đối chiếu từng job một. Vì vậy không kết luận được «có job nào lệch lịch không» — chỉ khẳng định được là mọi bundle đều hoàn thành TRƯỚC mốc đóng băng của miền đó.

**2. Chưa chứng minh được các dòng MB lúc 05:00 bị XOÁ.** Khe id 29361-29373 trống và không còn dòng MB nào trước 17:00 là bằng chứng gián tiếp mạnh, nhưng tôi không quan sát trực tiếp lệnh DELETE (production read-only, và journal không ghi dòng xoá). Còn hai khe khác (29394-29410, 29431-29442) chưa quy được về nguyên nhân nào. Cần soi writer của lane `rerun_post_mt` và kiểm tra khe id trên nhiều ngày mới nâng được lên PROVEN.

**3. Chưa đo được cap V10752 làm lệch con số WR/TOP1 bao nhiêu.** Tôi chứng minh được lệch THÀNH PHẦN MẪU (MN 81 ngày vs MT 18 ngày vs MB 17 ngày trong rolling metrics) và 46/72 ngày MT bị loại là do cap chứ không do hỏng. Nhưng tính lại WR/TOP1 khi bỏ điều kiện `EXCLUDE_PRIMARY` là một phép đo mới, cần nền riêng cho từng vế và đăng ký ngưỡng TRƯỚC — RM-03 cấm ghi «thắng/thua» khi thiếu. Ngoài ra hằng số hiệu chỉnh nào dùng cho phép đo đó phải đo lại cho chính thước đó (RM-21), không mượn VIF 2,92 hay 0,889 của thước cũ.

**4. Chưa xác định vì sao MB có `bt_gate_threshold=12 / wr_gate_threshold=26` trong khi MN là 15/30 và MT là 14/28.** Ngưỡng khác nhau theo miền và có vẻ suy từ cỡ mẫu (`total` 28-30 trong `model_bt`), nhưng tôi chưa quét ra đoạn code tính `min_bt_for_region` / `min_wr_for_region`. Chưa đủ để nói ngưỡng đúng hay sai.

**5. Chưa lý giải hết vì sao strength của MB co cụm bất thường.** MB ai_chain chỉ có 4 giá trị phân biệt trên 9 model (0,1 · 3,5 · 5,0 · 6,0) trong khi MT ai_chain có 9/9 phân biệt. Một phần đã giải thích được (trần MB,