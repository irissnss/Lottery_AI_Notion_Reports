# g5-anomaly · tang=EVIDENCE_COMPLETE · 7 phat hien

## TOM TAT

Ngày 04/09 là một ngày VẬN HÀNH KHẢ QUAN nhưng KHÔNG SẠCH VỀ THIẾT KẾ ĐO: 20/20 phép kiểm đã chạy, 16 phép không thấy bất thường (bundle tái lập 45/45, lo3 tái lập 93/93, 0 output rỗng ở cả ba miền — ngày duy nhất trong 12 ngày, 0 timeout, 0 ERROR scheduler, không có lookahead), nhưng ba khiếm khuyết ĐÃ CHỨNG MINH nằm ở chính bộ bằng chứng V11160 vừa dựng. Thứ nhất, vân tay prompt chỉ băm phần trước khi nối `_ctx_pack`/`REASONING_RULEBOOK`, nên `runtime_prompt_chars=24.435` trong khi chuỗi thật ≥50.670 ký tự — `contam_hits=0` KHÔNG chứng minh prompt cuối sạch. Thứ hai, V11160 vá `regime_prompt_cho_luot` nhưng bỏ sót dòng kề `_shadow_mode = ... or (selected_model in SHADOW_GATE_MODELS)` ở `:6738`, nên `gpt-oss-120b` chạy OFFICIAL vẫn ăn gói ngữ cảnh lane shadow — lệch 88/88 (ngày,miền) trong 30 ngày, và hôm nay nó bỏ phiếu vào bạch thủ công bố của cả MN (53) lẫn MB (86). Thứ ba, câu «bỏ mệnh đề theo-model mất 0 lượt đo» sai: `gpt-oss-120b` không có một lượt `shadow_auto_eval` nào trong 15 ngày, nên cohort prompt ngữ cảnh thuần mất hẳn một model từ 04/09. Về dự đoán, BT 1/3 (MT thắng, MN/MB thua) — n=3, cấm kết luận; MN có cụm 9 model ra cùng bộ {28,53}, vượt p90 nhưng chưa vượt max lịch sử. Không có mutation nào trên production: 10/10 băm tệp khớp Gate 0, NRestarts 0, đếm 4 bảng khoá không đổi.

## TRA LOI CAU HOI

BẤT THƯỜNG HAY KHẢ QUAN — trả lời tách đúng hai lớp:

**A. OPERATIONAL QUALITY = KHẢ QUAN, và là ngày tốt nhất của tuần.** Coverage 81/81 lượt, 0 `main_numbers` rỗng ở cả ba miền — ngày DUY NHẤT đạt 0/0/0 trong 12 ngày gần nhất (03/09 MN=2, 02/09 và 01/09 mỗi miền 1). Parse 60/60, `timeout_or_fallback=False` 60/60, `degraded_flag=False` 60/60, `hard_timeout_models=[]` cả ba bundle. Latency med 55,0s · p90 223,3s · max 300,1s — max THẤP NHẤT trong 10 ngày (nền 275–1084s). Scheduler 1.250 dòng, 18 WARNING, 0 ERROR (nền 7 ngày: 1.151–1.666 dòng, 13–40 non-INFO); warning đều là `SOFT_CONTINUE_90S` + `RULE_QUALITY_ALERT` + `AI_ONCE_DAILY_BLOCK`, tái diễn 6/7 ngày trước. Tái lập tất định: 45/45 bundle (15 ngày × 3 miền) có `bach_thu`=top1, `lo2`=top2, `xien3`=top3 và 0 phiếu sai; 93/93 lo3 tái lập bằng `_v11162_lo3_lineage`. Roster không trôi. NHƯNG hai chỗ KHÔNG được nâng lên «sạch»: vân tay prompt thiếu ~52% chuỗi (G5-F1) và gói ngữ cảnh vẫn rò theo model (G5-F2).

**B. PREDICTIVE QUALITY = TRUNG BÌNH, và MỘT NGÀY KHÔNG NÓI LÊN ĐIỀU GÌ.** BT 1/3 = 33,3% (MT 28 WIN; MN 53 LOSE; MB 86 LOSE) so với nền 30 ngày 26/90 = 28,9% và nền 7 ngày 3/21 = 14,3%. Top-10 trúng lô: MN 4/10 (med nền 4) · MT 7/10 (med 4, tb 3,73, max 8) · MB 3/10 (med 2). `model_daily_eval.bt_hit`: MN 63,0% (nền 39,5%) · MT 59,3% (nền 39,2%) · MB 14,8% (nền 19,6%). Với n=3 bundle và n=27 model/miền trong MỘT ngày, mọi con số trên là EXPLORATORY — không preregistered, không hiệu chỉnh multiple-testing, không dùng z/Fisher/McNemar. CẤM dùng 04/09 để sửa ngưỡng MT; `MT_PREREGISTRATION` giữ nguyên `PROVISIONAL_AGENT_PROPOSED`.

**Có được kết luận «V11160 đã đóng lỗ rò prompt» không?** KHÔNG hoàn toàn. Đúng là 27/27 lượt LEGACY có `contam=4` và 33/33 lượt CONTEXT_ONLY có `contam=0`, và `gpt-oss-120b` hôm nay LEGACY cả ba miền — tức nhánh regime prompt đã vá đúng. Nhưng (a) bộ đếm đó về mặt cấu trúc KHÔNG thể nhìn thấy `_ctx_pack` (10.977–18.427 ký tự) vì nó băm trước khi nối, và (b) chính `_ctx_pack` vẫn định tuyến theo MODEL. Nên verdict đúng tầng là: `PROMPT_LANE_REGIME_FIXED` nhưng `PROMPT_CLEAN_NOT_PROVEN`.

**So sánh với 7 ngày trước cutover:** so được ở coverage/latency/scheduler/reproduction (cùng roster 27 model/miền, cùng 3 miền). KHÔNG so trực tiếp được ở hai trường vân tay prompt `runtime_prompt_*` — chúng chỉ tồn tại từ 03/09 (03/09 còn 20/62 dòng rỗng), nên nền cho ba trường đó chỉ có 1 ngày.

**Trạng thái bắt buộc giữ nguyên — đã giữ:** `MATERIALIZATION_DECISION=DEFERRED_PENDING_EOD_AUDIT` · `OUTPUT_COUNTERFACTUAL_RANK_PRODUCTION_WRITE=FORBIDDEN` · `MT_PREREGISTRATION=PROVISIONAL_AGENT_PROPOSED` · `POOL_VERDICT=HOLD` · `MODEL_ACTION=BLOCKED` · `PROMPT_43_R1=PARTIAL`. Kết quả kiểm 18/19 củng cố khuyến nghị V11163 «DỪNG ĐO `output_counterfactual_rank`»: cột vẫn 0/17.121 non-NULL kể cả 81 dòng ghi hôm nay, writer hàng giờ vẫn chạm nó qua danh sách INSERT ở `_materialize_shadow_promotion_scorecard.py:408/:500`, và 0 reader.


## PHAT HIEN (tieu de)
  - [PROVEN_DEFECT] Vân tay prompt V11160 chỉ băm ~48% chuỗi thật gửi đi — gói ngữ cảnh, RULEBOOK và contract được nối vào SAU khi băm
  - [PROVEN_DEFECT] V11160 vá một trong hai chỗ dùng `_la_shadow` — gói ngữ cảnh VẪN định tuyến theo MODEL, gpt-oss-120b chạy official vẫn ăn context pack lane shadow và bỏ phiếu vào bạch thủ công bố
  - [PROVEN_DEFECT] Câu «Bỏ mệnh đề theo-model mất 0 lượt đo» của V11160 SAI với gpt-oss-120b — cohort prompt ngữ cảnh thuần mất hẳn một model từ 04/09
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] MN 04/09: chín model ra CÙNG bộ số {28,53}, vượt p90 nhưng chưa vượt max lịch sử
  - [OPERATIONAL_IMPROVEMENT] Ba lượt gọi LLM không có dòng predictions tương ứng — prediction_trace không có trường phân loại lượt
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] Một dòng official có phase_type RỖNG vẫn bỏ phiếu vào bạch thủ MB công bố
  - [EXPLORATORY_PREDICTIVE_SIGNAL] 04/09 khả quan về vận hành, trung bình về dự đoán — và một ngày không nói lên điều gì

## CHUA TRA LOI DUOC

1. **Gói ngữ cảnh (`_ctx_pack`) có chứa dấu ô nhiễm thật hay không — INDETERMINATE.** Đã chứng minh vân tay không phủ nó (G5-F1), nhưng CHƯA đo được nội dung. Muốn đo phải gọi `build_context_pack(target_region, date_str, shadow_mode=...)` trên hàm đang serve rồi grep năm dấu — tôi KHÔNG chạy vì chưa chứng minh được hàm đó hoàn toàn không ghi DB, mà luật cứng của phiên cấm mọi khả năng ghi lên production. Đây là việc phải làm trước khi bất kỳ ai nâng `PROMPT_43_R1` khỏi `PARTIAL`.

2. **Vì sao ba lượt gọi LLM lặp thêm tồn tại — INDETERMINATE.** Đã chứng minh chúng có thật, không có dòng `predictions`, và hai trong ba trùng đúng giây tạo bundle. CHƯA truy được hàm gọi (giả thuyết `run_combo_super()` gọi lại model đã chọn là SUY LUẬN, chưa quét ra bằng grep — RM-10 cấm kết luận theo tên đoán). MB hôm nay không có lượt lặp nào trong khi combo-super vẫn bỏ phiếu — mâu thuẫn với giả thuyết đó, càng phải quét mã thật.

3. **Vì sao `phase_type` rỗng — INDETERMINATE.** Chưa quét được writer gán nhãn này, nên không nói được đó là lỗi ghi, lỗi đường dẫn, hay nhánh hợp lệ.

4. **Vì sao prompt lệch 100–230 ký tự giữa các model trong cùng (miền, regime) — INDETERMINATE** (phép kiểm #10). Vân tay không chuẩn hoá và lại thiếu 52% chuỗi nên phép so này mất nghĩa cho tới khi G5-F1 được sửa.

5. **Cụm 9 model MN có phải xu hướng không — CHƯA ĐƯỢC PHÉP KẾT LUẬN.** n = 1 ngày, nằm trong dải lịch sử (max 11 ngày 30/08). Cần tối thiểu 10–14 ngày đo trên ĐÚNG thước này (cùng miền, cùng roster 27 model, cùng định nghĩa cặp trùng), đăng ký ngưỡng TRƯỚC, và đo lại hệ số cụm cho chính thước này chứ không mượn VIF 2,92 hay 0,889 của thước khác (RM-21).

6. **Ảnh hưởng ĐỊNH LƯỢNG của G5-F2 lên chất lượng output — CHƯA ĐO.** Đã chứng minh `gpt-oss-120b` ăn gói ngữ cảnh khác và đã bỏ phiếu vào bạch thủ công bố của MN và MB hôm nay. CHƯA đo bundle sẽ ra số gì nếu bỏ phiếu của nó — muốn đo phải tái lập weighted_voting_wr có/không voter đó trên 88 cặp (ngày, miền), và phải tách TRONG/NGOÀI cửa sổ ch