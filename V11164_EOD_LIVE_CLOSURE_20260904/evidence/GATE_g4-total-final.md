# gate6 · tang=EVIDENCE_COMPLETE · 16 phat hien

## TOM TAT

Tái lập TOTAL từ RAW MODEL OUTPUT cho cả ba bundle 04/09 (MN 825 · MT 827 · MB 829) khớp TUYỆT ĐỐI: 30/30 hàng top-10 trùng cả số, điểm 4 chữ số thập phân và thứ tự danh sách voter; 81/81 hàng trọng số BT trùng; lô-3-càng 853/228/586 tái lập đúng. So năm tầng (raw → persisted TOTAL → published FINAL → override → UI) cho ĐIỂM LỆCH ĐẦU TIÊN = KHÔNG CÓ: bach_thu luôn là ranked[0], không đòn bẩy override nào kích hoạt, không connector, không lookahead (bundle v2 chốt MN 15:40 · MT 16:55 · MB 17:55 đều TRƯỚC giờ kết quả). Phát hiện nặng nhất không nằm ở số mà ở ĐỘC LẬP CỦA PHIẾU: combo-super GỌI LẠI chính model đã bỏ phiếu (trace bắt được 3 lượt gọi lại đúng giây tạo bundle) còn smart-ensemble/smart-ml DÙNG LẠI đầu ra đã lưu của model cha — MT bạch thủ 28 có 4 voter nhưng chỉ 3 danh tính model, MB số 78 lấy 27% điểm từ hai bộ tổng hợp cùng đếm lại meta-learning. Trần MT-13 loại meta-learning và random-forest nhưng tín hiệu hai model đó quay lại nguyên vẹn qua smart-ensemble/smart-ml, tức trần chỉ cắt lá phiếu chứ không cắt ảnh hưởng. Journald mất toàn bộ dòng print() từ khoảng 17:00 nên KHÔNG có một dấu vết nào về việc sinh bundle MB trong journal — phải dùng scheduler_logs mới dựng lại được, đây là lỗ thủng của chính kênh bằng chứng Gate 0 đã dùng. Không có mutation nào trên production: 4 bảng khoá đếm lại đúng bằng Gate 0, PID 3370750 · NRestarts 0 giữ nguyên.

## TRA LOI CAU HOI

1) TÁI LẬP TOTAL/FINAL/OVERRIDE/3-CÀNG TỪ RAW MODEL OUTPUT — ĐẠT 100%.
Dùng `_v11161_rank_gen.py` (CanhGac chặn oracle bằng cấu trúc) chạy trên DB production mở `mode=ro`, nguồn là bảng `predictions` (đúng thứ `generate_final_bundle` đọc qua `get_prediction_history`), trọng số as-of `date >= D-30 AND date < D`.
· effective_weight · strength/10 · verdict_weight · lane_weight · position_weight: khớp từng thành phần.
· PP-1 ×0,85: MN kích hoạt đúng một lần trên số 53 (0,1280 → 0,1088, 3 voter mang dấu CONV-DOWNGRADE/DIVERSITY); MT factor = 1,0 (TẮT) đúng như `_PP1_DAMPENER_DISABLED_REGIONS={"MT"}`; MB bật nhưng 0 sự kiện.
· PP-5 family bonus: `ENABLE_FAMILY_BONUS=False` → không áp ở cả ba miền.
· Trần voter MT-13: tái lập đúng hai model bị đẩy ra là meta-learning và random-forest, và đúng thứ tự `(bt_rate, win_rate)` giảm dần — hai model đó đứng hạng 14 và 15/15.
· Làm tròn production `round(bt_rate,1)` rồi `round(bt_weight,3)` (database.py:3420-3429): giữ nguyên; đây là điều kiện cần — bỏ nó là lệch thứ tự.
· Tie-break tất định: MB có một ca hoà điểm THẬT — 96 và 82 cùng 0,050800000000 (bằng nhau tuyệt đối, hiệu = 0,0). Bản tái lập ra đúng thứ tự 96 trước 82 vì `sorted` ổn định giữ thứ tự chèn, mà thứ tự chèn đến từ `ORDER BY created_at DESC` của truy vấn nguồn.
· ranked[:10] · lo2 · xien2 · xien3 · lo3: khớp.

2) NĂM TẦNG — ĐIỂM LỆCH ĐẦU TIÊN: KHÔNG CÓ.
(1) raw tái lập = (2) persisted TOTAL = (3) published FINAL = (4) override-adjusted. (5) UI công khai: `/api/final-bundle` sau FU-438 là ADMIN ONLY fail-closed, khách gọi trả HTTP 401 cho cả ba miền, nên tầng 5 KHÔNG phát ra số nào cho người xem — phép so tầng 4↔5 rỗng theo thiết kế owner đã khoá, không phải drift.
Cụ thể vì sao tầng 4 == tầng 3: `_V10767_MB_PREVDAY_ENABLED=False` · `_V10789_MB_LANE_PROMOTE_ENABLED=False` · `_V10790_MT_LANE_PROMOTE_ENABLED=False`; V10640 `OVERRIDE_CONFIG` chỉ MN `enabled:True` (chooser `specialist`) nhưng không đổi số; `generation_method='weighted_voting_wr'` ở cả ba → connector V10883 KHÔNG cắm.

3) TOP-1 CỦA TOTAL KHÁC FINAL DO OVERRIDE HAY DO WRITER DRIFT? — KHÔNG KHÁC, nên không phải cái nào cả. bach_thu = ranked[0] ở cả ba miền (53 · 28 · 86). Không có writer thay thế, không có bản backfill/late (81/81 dòng `late=0`), không bundle fallback (`is_fallback=0`).

4) HYBRID/ENSEMBLE CÓ DÙNG LẠI CÙNG PARENT OUTPUT KHÔNG? — CÓ, và theo HAI cơ chế KHÁC NHAU, phải gọi tên tách bạch:
· smart-ensemble và smart-ml **DÙNG LẠI ĐẦU RA ĐÃ LƯU** của model cha (không tốn thêm lượt gọi). Chứng minh bằng dữ liệu: mảng `lstm_numbers` của smart-ensemble MN là `["73","10","92","05","17"]` — trùng từng phần tử với `xgboost_numbers` của smart-ml MN.
· combo-super **GỌI LẠI (re-sample) chính model đó lần nữa**, tức THÊM một lượt gọi API mới cho model đã có phiếu. Chứng minh bằng `prediction_trace.jsonl`: MN `gemini-2.5-pro` có hai dòng 05:15:42 → ['28','75'] và 05:21:04 → ['28','53']; MN `claude-opus-4-6` 05:16:01 → ['53','69'] và 05:20:24 → ['98','53']; MT `gemini-2.5-flash` 16:40:49 → ['28','18'] và 16:46:00 → ['28','30']. Giờ của dòng thứ hai trùng ĐÚNG GIÂY tạo bundle/combo-super.
⇒ Trả lời «THÊM nguồn hay THAY THẾ nguồn»: combo-super **THÊM một mẫu mới của cùng model** (nên trông như nguồn độc lập nhưng không phải); smart-ensemble/smart-ml **THAY THẾ bằng bản sao của nguồn cũ**. Cả hai đều làm ảnh hưởng bị nhân đôi ở **cấp candidate**, không chỉ trùng lineage.

5) MODEL_COUNT HIỂN THỊ CÓ ĐÚNG SỐ VOTER THỰC KHÔNG? — ĐÚNG. `final_bundles.model_count` = 15 · 13 · 15 = đúng số model thật sự được chấm điểm (bản tái lập cho cùng con số). Nó cố tình khác `output_eligible_row_count`=15 dùng cho cổng publish (`publish_readiness_semantic='OUTPUT_ELIGIBLE_ROW_COUNT'`, tách từ V105.35), và MT gắn `incomplete_bundle=True` vì 13 < 15. Đây là hành vi đúng thiết kế, không phải nhãn sai.

6) 3-CÀNG — ĐẠT.
`_v11162_lo3_lineage.tinh_lo3_co_ghi_vet` tái lập đúng 853 / 228 / 586. Hai chữ số cuối của lô-3 BẰNG bach_thu của ĐÚNG lane official ở cả ba miền (53/28/86). Cutoff `2026-03-08`, câu lệnh dùng `date >= cutoff AND date < date_str` — chặn trên NGHIÊM NGẶT nên 6 dòng `lottery_results` của chính ngày 04/09 KHÔNG lọt vào: không lookahead, bảo đảm bằng cấu trúc chứ không bằng lời hứa. Ngày 04/09 nằm sau `MOC_THUAT_TOAN=2026-06-27` nên đúng thời kỳ thuật toán hiện hành (RM-21).
Cảnh báo kèm: prefix MB gần như hoà bốn phía — 5(14) · 1(12) · 6(12) · 2(12) — thắng bằng 2 phiếu.

7) KHÔNG triển khai TOTAL_V2 / COMBO_V2 / FINAL_V2. Phép «bỏ điểm của model tổng hợp» chỉ là phân tích ĐỘ NHẠY để định lượng mức nhân đôi, không phải bộ chọn thay thế và không được ghi vào đâu.


## PHAT HIEN (tieu de)
  - [NO_ANOMALY_FOUND] Tái lập TOTAL từ raw model output khớp tuyệt đối 30/30 hàng, ba bundle
  - [NO_ANOMALY_FOUND] Điểm lệch đầu tiên giữa năm tầng: KHÔNG CÓ — tầng 1 = 2 = 3 = 4; tầng 5 là 401 theo thiết kế
  - [PROVEN_DEFECT] combo-super GỌI LẠI chính model đã bỏ phiếu — phiếu bị nhân đôi ở cấp candidate, trúng đúng bạch thủ MT
  - [PROVEN_DEFECT] smart-ensemble / smart-ml dùng lại ĐÚNG mảng đầu ra đã lưu của model cha rồi bỏ phiếu như model riêng
  - [PROVEN_DEFECT] Trần voter MT-13 (V10752) cắt lá phiếu nhưng KHÔNG cắt ảnh hưởng của hai model bị loại
  - [PROVEN_DEFECT] Bundle MT ghi nhãn SAI nguyên nhân loại model: `wr_gate_filtered` nói cổng chất lượng, `gate_diagnostics` nói hai model đó ĐẠT
  - [PROVEN_DEFECT] Nhãn `lstm_numbers` nói dối: nó chứa đầu ra của xgboost (MN) và của random-forest (MB)
  - [PROVEN_DEFECT] Dòng log `models=0` của combo-super là trường CHẾT — luôn bằng 0 bất kể thực tế
  - [PROVEN_DEFECT] Journald mất TOÀN BỘ dòng print() từ khoảng 17:00 — không còn một dấu vết nào về việc sinh bundle MB
  - [PROVEN_DEFECT] xiên-2 và xiên-3 lấy ranked[0..2] chứ không bám bach_thu — mọi lần override kích hoạt sẽ đẻ ra bộ thẻ tự mâu thuẫn
  - [OPERATIONAL_IMPROVEMENT] Hoà điểm THẬT xảy ra hôm nay và được phân giải bằng độ trễ API, không bằng một tie-break theo miền
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] V10640 đang bật cho MN nhưng bản song sinh shadow 37/37 ngày chưa từng đổi số — đòn bẩy coi như vô hiệu
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] MT_ADAPTIVE_EXPLOIT_V1 sinh SAU mốc đóng băng MT và chỉ trước kết quả 1,2 giây
  - [NO_ANOMALY_FOUND] 3-càng: tái lập đúng cả ba, đuôi bằng bạch thủ đúng lane, cutoff chặn trên nghiêm ngặt nên không lookahead
  - [EXPECTED_BEHAVIOR] V11160 giữ vững trên toàn bộ 60 lượt của 04/09 — không lượt CONTEXT_ONLY_V2 nào dính dấu ô nhiễm
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] Lô 6 thí nghiệm materializer bỏ MN 5/7 ngày gần đây — cùng gốc với việc V10640 MN không có dữ liệu

## CHUA TRA LOI DUOC

1. **Nhánh gọi official của V10640 trả về gì trong ngày 04/09** — chưa chứng minh được. `get_override_bt` gọi `_choose_specialist` nhập từ `_materialize_experimental_preview_shadow`, module này có `CREATE TABLE IF NOT EXISTS` và `INSERT OR IGNORE` nên chạy thử sẽ GHI vào production DB. Chỉ chứng minh được HIỆU LỰC bằng không (bach_thu công bố = ranked[0], journal MN 15:40 đầy đủ không có dòng `[V10640-OVERRIDE]` lẫn dòng `skipped`) và bằng chứng gián tiếp mạnh (37/37 ngày bản song sinh shadow không đổi số). Không phân biệt được «không có pick» với «pick trùng 53». `INDETERMINATE` về cơ chế.

2. **Phân loại 5 nhóm cho `prediction_trace`** (scheduled production invocation / post-bundle replay / emission-only / diagnostic / duplicate) — không hoàn thành. Đã liệt kê ĐỦ 63 khoá của toàn bộ 60 dòng ngày 04/09: không có khoá `run_source`, `run_id`, `lane`, `phase_type`, `surface`, `replay`, `duplicate`. Nên phép phân loại không làm được từ chính tệp trace; chỉ suy ra được bằng cách ghép giờ với `predictions`. Kết quả ghép: 60 dòng trace / 81 prediction, chênh đúng 21 = 7 model ML × 3 miền (ML không ghi trace); combo-super 0 dòng trace ở cả ba miền; MN dư 1 dòng và MB thiếu 1 dòng so với số prediction non-ML — đã xác định phần dư là hai lượt gọi lại của combo-super, phần thiếu ở MB chưa truy được.

3. **Vì sao journald ngừng nhận `print()` từ khoảng 17:00** — chưa xác định nguyên nhân. Đã loại trừ thông báo rate-limit tường minh (chuỗi «Suppressed» đếm được 0 lần trong journal ngày). Có thể là đệm khối của stdout, có thể là giới hạn của journald không in thông báo, chưa chứng minh được cái nào. Ghi `INDETERMINATE`; điều CHẮC CHẮN là journal 04/09 KHÔNG đủ để dựng lại việc sinh bundle MB.

4. **Trọng số as-of có trùng tuyệt đối với trọng số production nhìn thấy tại giây chạy hay không** — chứng minh được ở mức mạnh nhưng không tuyệt đối. 27/27 model mỗi miền khớp `bt_rate`/`bt_weight`/`total` với bảng `model_bt` production đã lưu trong bundle, và bản tái lập ra đúng điểm tớ