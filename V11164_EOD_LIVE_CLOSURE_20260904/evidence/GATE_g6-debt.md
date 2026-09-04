# g6-debt · tang=PARTIAL · 13 phat hien

## TOM TAT

Gate 6 đã dựng sổ nợ 32 dòng, mọi dòng map được vào FU-449/FU-450 — không mở FU mới, không có dòng NEEDS_OWNER_MAPPING. Ba tệp điều hướng công khai (LATEST_REPORT.json · NEXT_ACTION.md · REPORT_INDEX.md) lệch 14 ngày: khai V11098 / 376 thư mục trong khi thực tế V11163 / 440 thư mục, và gốc là bộ sinh `_v11083` KHÔNG nối vào hook nào — đúng lỗi nó từng được dựng ra để chữa. Con số «94 mục quá hạn» đang lưu hành trên NEXT_ACTION.md là số đo ngày 21/08 trong cửa sổ [−14,+21]; đo lại hôm nay bằng chính bộ đọc canonical ra 194 treo / 152 quá hạn — hai thước khác nhau nên cấm trừ hai số, nhưng chắc chắn số công bố đã 14 ngày tuổi. Sổ rút lại `docs/SO_RUT_LAI.json` đứng ở 7 mục từ 18/08 trong khi từ đó tới nay có 25 báo cáo chứa chữ «RÚT LẠI» và 5 bản mang chữ đó ngay trong tên thư mục — cổng `_v11085` lấy sổ này làm nguồn duy nhất nên nó đang mù đúng những kết luận vừa bị bác, và bản thân cổng cũng chưa nối vào hook. Đo lại writer scorecard cho thấy phạm vi món nợ bị khai THIẾU: không phải một vị trí `None` mà 3 vị trí ở câu INSERT thứ nhất và 6 vị trí ở câu thứ hai, và đường gọi thật là `scheduler.py:665` chứ không phải crontab. Hai kết quả ngược chiều đáng ghi: «promotion_bucket không có reader» là SAI (có SELECT sống ở `_v11155:135`), còn true missing output ngày 04/09 là 0/81 — nhưng một ngày chỉ là một ngày (RM-04).

## TRA LOI CAU HOI

**«KIỂM tracker thật, đừng tin con số 94»** — đã kiểm, và con số 94 KHÔNG dùng được cho hôm nay. Nguồn của nó là `NEXT_ACTION.md:42` (tệp máy sinh, sinh lúc 2026-08-21 20:57:22), và chính tệp đó khai nó lọc cửa sổ [−14, +21] ngày. Đo lại hôm nay bằng chính bộ đọc canonical `_v10958_fu_reader.treo_items(..., today=2026-09-04)`: 194 treo · **152 quá hạn** · 0 đến hạn hôm nay · 34 không ghi hạn · 6 mồ côi · 3 thiếu mã đọc. Theo RM-21 tôi KHÔNG viết «94 → 152» như một phép biến thiên, vì hai số đo bằng hai thước; điều nói được là số đang lưu hành đã 14 ngày tuổi và số thật hôm nay là 152/194.

**LATEST_REPORT.json / NEXT_ACTION.md / REPORT_INDEX stale** — cả ba đều stale, cùng một lần sinh 2026-08-21 20:57:22, cùng một commit `a8fca05`. Khai V11098 / 376 thư mục; thật là V11163 / 440 thư mục. Gốc không phải quên chạy tay mà là bộ sinh không nối vào hook nào.

**Navigation generation** — tôi CHỈ BÁO CÁO tình trạng, KHÔNG regenerate, đúng luật cứng của gate. Đã chạy nhánh đối chiếu `--thu` (read-only) để lấy verdict chính thức: `✗ 2 mặt LỆCH so với thư mục thật`. Quy trình đóng đúng vẫn là snapshot → dry-run → diff → validation → commit, và phải làm sau audit.

**111 historical cells thiếu registry L3** — xác nhận 111, và tái lập độc lập bằng số học lưới (37 ngày × 3 miền). Đóng được ngay bằng cách ghi hạn chế phạm vi, tuyệt đối không bù dữ liệu (RM-17).

**357 bundle trước boundary thuật toán 3-càng** — xác nhận bằng SQL: 357/567, từ mốc 210. Nhưng phát hiện thêm: V11159 cũng có một con số 357 với nghĩa hoàn toàn khác (ô lưới trước 05/07), và cả hai đều tái lập đúng. Đã ghi thành dòng nợ D-NUM-01 để lần trích sau bắt buộc kèm danh từ.

**Historical as-of / lookahead risk** — có thật và chưa có cổng: mốc đóng băng đổi ba lần (05/07 → 31/07 → 01/08), 357/540 ô nằm trước khi cơ chế freeze ra đời, và bản dựng đầu tiên áp mốc hôm nay ngược 180 ngày đã xoá oan hai ô. Kiến nghị: một hàm tra `moc_dong_bang(ngay, mien)` dùng chung thay cho hardcode.

**Role-at-time classification debt** — bản vá ĐÃ vào production ở V11158 (+4.114 lượt được phân loại, +46,5%; hồi quy 19/19 · 37/37 · 13/13), còn 11 ô lệch (2,04%) chưa giải. Nhãn đúng là PARTIALLY_CLOSED.

**Pre-existence coverage gaps** — nhãn đúng là ĐÓNG_CÓ_ĐIỀU_KIỆN, phạm vi «đầu vào output_eligible của `_v11155` trong cửa sổ 60 ngày», KHÔNG phải «VPS == git». Ba phản biện đứng vững (nhân chứng mù với `status`; 93/93 là một ảnh git lặp 93 lần = một bậc tự do; bắc cầu VPS==local + local==git không suy ra VPS==git). Chặn dứt điểm cần `registry_sha256` trong bundle → chạm writer → cần owner ký.

**True missing output** — 0/81 ngày 04/09, đo theo RM-09. Không có lượt nào ra rỗng.

**Telemetry asymmetry** — đo lại được và rất rõ: 11 model shadow n=92 đều nhau, ba model official n=6/3/2, vì lane official chỉ ghi khi hỏng. Mọi so sánh độ tin cậy hai lane hiện không có nền cho vế official.

**Trace không 1:1 với predictions · replay/emission duplication** — 81 predictions / 60 dòng trace / 57 cặp; 24 cặp thiếu trace ĐÚNG BẰNG 8 model no-token × 3 miền; 57+24=81. Chiều thiếu là expected; chiều thừa (3 dòng lặp cặp hôm nay, 6 cặp hôm 03/09) là nợ thật vì dòng trace không tự khai nó thuộc loại nào.

**Promotion bucket không có reader** — mệnh đề này SAI. Có SELECT sống ở `_v11155_vai_tro_theo_thoi_diem.py:135`, thêm `_materialize_multi_lane_shadow_p0.py:3038` và index `idx_smps_bucket`. Mệnh đề không-reader chỉ đúng cho `output_counterfactual_rank` (7 dòng mã sống, 0 SELECT).

**Counterfactual artifact/column semantics + writer hardcode None vị trí 17/34** — cột nằm ở vị trí 18/35 của BẢNG và 17/34 của tuple INSERT (bảng có cột `id` đứng đầu) — hai cách đếm, cùng một cột, không mâu thuẫn. Nhưng phạm vi món nợ bị khai thiếu: 3 vị trí `None` ở câu INSERT thứ nhất, 6 vị trí ở câu thứ hai. Và caller thật là `scheduler.py:665`, không phải crontab.

**Latent `_safe_stdio_ctx` concern** — 28 vị trí trong `scheduler.py`, 0 dòng lỗi I/O đo được nên nhánh nguy hiểm chưa từng chạy. Giữ nguyên quyết định chủ động không sửa của V11163, xếp P3.

**Stale/retracted claims trong report và generated UI** — 76 bảng im ≥7 ngày, 31 trong đó có điểm ĐỌC sống (8 trên /monitoring, 11 trên /du-doan-test, 6 chỉ qua API, 6 chỉ mã nội bộ). Kèm cảnh báo tái lập: số dòng RM-20 ghi trong CLAUDE.md đã trôi ~360 (nay là :12244 :12281 :15390 :15402) — mọi báo cáo phải dẫn số dòng đo lại.

**Model aliases/routes/lifecycle · prompt regime documentation · TOTAL formula/rounding/cap/override · ranked adapter · all-model arena · TOTAL_V2 · COMBO_V2 · FINAL_V2 · official cutover packet** — cả chín đều đã vào sổ (D-MODEL-01, D-PROMPT-01, D-TOTAL-01, D-RANK-01, D-ARENA-01, D-V2-01/02/03, D-CUT-01) với đủ 12 trường. Ba điểm đáng nêu: TOTAL đang có BỐN tài liệu cùng mô tả nó ở bốn thời điểm khác nhau và công thức cũ đã bị rút lại ở V11154 mà chưa có bản canonical thay thế; prompt regime đã RUNTIME_PROVEN ở V11160 nhưng ai đo mà không nạp env của service sẽ đọc ra `LLM_CONTEXT_ONLY_V2_LANE=off` và kết luận ngược (RM-13); cutover vẫn HOLD vì «không miền nào đổi có ý nghĩa».

**CẤM tạo FU mới** — tuân thủ. 32/32 dòng map vào FU-449 hoặc FU-450 (một dòng ghi thêm «trùng FU-349/FU-245» vì đó là mục đã tồn tại, không phải mục mới). Không có dòng NEEDS_OWNER_MAPPING.


## PHAT HIEN (tieu de)
  - [PROVEN_DEFECT] Ba tệp điều hướng công khai lệch 14 ngày — và bộ sinh chữa lỗi này KHÔNG nối vào hook nào
  - [PROVEN_DEFECT] «94 mục quá hạn» đang lưu hành là số của 21/08; đo lại hôm nay ra 194 treo / 152 quá hạn — nhưng KHÁC THƯỚC, cấm trừ
  - [PROVEN_DEFECT] Sổ rút lại đứng ở 7 mục từ 18/08 — cổng PRJ-RETRACTION-001 đang mù đúng những kết luận vừa bị bác
  - [PROVEN_DEFECT] Nợ báo cáo §57 không giảm mà TĂNG: 38/232 (đo 02/09) → 40/240 (đo hôm nay), 23 bản thiếu hẳn
  - [PROVEN_DEFECT] Món nợ writer `None` bị khai THIẾU PHẠM VI: không phải 1 vị trí mà 3 và 6; và đường gọi thật không phải crontab
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] HAI con số «357» khác nghĩa nằm trong hai báo cáo liên tiếp — cả hai đều tái lập đúng
  - [PROVEN_DEFECT] Bất đối xứng telemetry đo lại được: 11 model shadow có n=92, ba model official có n=6/3/2 — vế official KHÔNG CÓ MẪU SỐ
  - [EXPECTED_BEHAVIOR] Trace ≠ predictions — nhưng cộng số khớp tuyệt đối: 57 + 24 = 81, và 24 đúng bằng 8 model no-token × 3 miền
  - [NO_ANOMALY_FOUND] «promotion bucket không có reader» là SAI — có SELECT sống; mệnh đề không-reader chỉ đúng cho output_counterfactual_rank
  - [NO_ANOMALY_FOUND] True missing output ngày 04/09 = 0/81 — đo theo RM-09, không đếm chuỗi thô
  - [PROVEN_DEFECT] Briefing đầu phiên đứng im 19 ngày — nguồn gốc của thói quen trích số cũ
  - [OPERATIONAL_IMPROVEMENT] Ba món nợ khác nhau cùng bị chặn bởi MỘT cánh cửa: §52 mục 13 cấm động writer `final_bundles`
  - [PROVEN_DEFECT] 111/540 ô lưới role-at-time không có lớp L3 — đóng được bằng cách GHI HẠN CHẾ, không được bù dữ liệu

## CHUA TRA LOI DUOC

**① Không đóng được dòng nợ nào bằng hành động** — luật cứng của gate cấm ghi tài liệu, cấm regenerate điều hướng, cấm git. Năm dòng đánh dấu «CÓ thể đóng ngay» (D-NUM-01, D-ROLE-01, D-LO3-01, D-SCORE-01, D-TRACE-01) chỉ cần một lần ghi tài liệu, nhưng phải làm ở phiên sau. Vì vậy verdict là PARTIAL chứ không phải EVIDENCE_COMPLETE.

**② Bốn con số trong sổ là TRÍCH TỪ BÁO CÁO TRƯỚC, tôi không đo lại trong phiên này** — và tôi ghi rõ để không ai tưởng chúng vừa được xác minh: role-at-time «8.853 → 12.967 (+46,5%)» và «11 ô lệch 2,04%» (V11155/V11158); arena «94/94 lượt shadow_auto_eval, 0/273 bundle» (V11151); ranked adapter «tự kiểm 13/13, DEGRADED 4/7» (V11157); stale reader «76 bảng im, 31 có điểm đọc sống» (V11157). Bốn nhóm này ở tầng REPORT_PROVEN theo báo cáo gốc, không phải RUNTIME_PROVEN từ phép đo hôm nay (RM-12).

**③ Con số «writer chạy 16:00·17:00·18:00·20:00» không tái lập được** và tôi không tìm ra nguồn của nó. `crontab -l` không có dòng nào cho scorecard; caller là `scheduler.py:665`. Tôi KHÔNG đọc định nghĩa job trong scheduler để xác định giờ thật — nên câu đúng hiện giờ là «writer còn sống, ghi lần cuối 04/09 18:31:35», còn tần suất chính xác là INDETERMINATE.

**④ 11 ô lệch (2,04%) của đối chiếu L1∩L3 vs L2 chưa có nguyên nhân** — giả thuyết là cùng gốc với 2 ô ngày 01/08 (độ phân giải NGÀY của registry commit) nhưng chưa đo, nên không được viết như đã giải.

**⑤ 3 dòng trace lặp cặp ngày 04/09 chưa phân loại được** thành scheduled / post-bundle replay / emission-only / diagnostic / duplicate. V11162 phân loại được 6 cặp của ngày 03/09 bằng cách so thời điểm với lúc ráp bundle; tôi không lặp phép đó cho 04/09. Đây chính là lý do dòng nợ D-TRACE-02 tồn tại: dữ liệu không tự khai loại.

**⑥ Chưa xác minh «5 ca rút lại chưa vào sổ» là con số ĐẦY ĐỦ.** Tôi đếm được 25 báo cáo chứa chuỗi «RÚT LẠI» và đối chiếu thủ công ra ít nhất 4–5 ca chưa có mục trong `SO_RUT_LAI.json`. Chưa chạy phép đối chiếu máy từng ca ↔ từng mục, nên con số đúng có thể lớn h