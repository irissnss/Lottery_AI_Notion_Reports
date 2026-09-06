# s7-chat-luong · tang=EVIDENCE_COMPLETE

## TOM TAT

Ngày 05/09 chạy SẠCH về vận hành: 3/3 miền đủ bundle, 27 lượt/miền (16 official + 11 shadow), 0 lượt rỗng, 0 late, 0 timeout (bằng chứng NỘI DUNG: trace 60/60 `timeout_or_fallback=False`, `degraded_flag=False`, finish_reason chỉ stop/STOP/end_turn), 0 dòng ERROR, 21 WARNING. MB trúng bạch thủ 37; lo2 chỉ PARTIAL (37 trúng, 64 trượt) — KHÔNG phải «lo2 trúng» như bản chụp ghi. MN và MT trượt cả BT lẫn lo2.

Nhưng lớp BẰNG CHỨNG hỏng ở hai chỗ nặng, cả hai đều làm sai kết luận của phiên trước và của chính đề bài Cổng 2:

① `final_bundles.created_at` KHÔNG phải mốc chốt. `save_final_bundle` UPSERT (database.py:4658-4679) không cập nhật `created_at`, nên cột đó là giờ GHI LẦN ĐẦU. Nội dung công bố do job `t10_chot` ghi lần cuối: MN 15:40 · MT 16:55 · MB 17:55 (`_v10782_freeze.T_CHOT_MARKS`, log `job_name=t10_chot` ngày 05/09 ghi đúng BT=74/86/37 «(v2)»). MN lệch **10 giờ 21 phút**. Vì vậy tiền đề «12 lượt MT chạy SAU khi bundle chốt 16:51:30» là đọc nhầm cột: lượt combo-super 16:52:10 chạy TRƯỚC lần ghi nội dung 16:55 và **có vào bundle** — chứng minh bằng `output_eligible_row_count=15`, con số KHÔNG thể có lúc 16:51:30 (khi đó chỉ 14 model output-eligible có dòng).

② stdout của tiến trình production CHẾT từ 04/09 16:53:48, đã 28 giờ. Toàn bộ chẩn đoán `print()` — `[FINAL-BUNDLE]`, `[V10752]`, `[API]`, `[TRACE]`, `[CONTEXT_PACK]`, `[COST]`, `[ANTI-TRAP]`, `[FREEZE-55]` — mất trắng; stderr vẫn chảy đều 32 dòng/giờ. Cơ chế V10545 safe-stdio nuốt lỗi nên KHÔNG có triệu chứng. Đây chính là loại bằng chứng mà Cổng 1 V11164 đã dùng để kết luận; nay không lấy lại được.

Ba lỗi cũ tái hiện SỐNG hôm nay: gpt-oss-120b (OFFICIAL, là voter cả ba bundle) nhận gói ngữ cảnh SHADOW ở 3/3 miền; MT bị gắn EXCLUDE_PRIMARY vì cap CỐ Ý bị đọc ngược thành «Thiếu 2 model (13/15)» (29/30 ngày MT EXCLUDE_PRIMARY, 1 ngày EXCLUDE_ALL — KHÔNG ngày nào INCLUDE); và cơ chế DIVERSITY của combo-no-token đo được là LÀM MẤT nhiều hơn LÀM ĐƯỢC (139 vs 91 cặp lệch, McNemar z=3,099; khử trùng z=2,616; một-ca-mỗi-ngày-miền z=2,802).

Hai cảnh báo bị nghi ngờ trong đề bài thì SẠCH: DUPLICATE_CONCENTRATION không hơn nền (102/430 trúng vs kỳ vọng 115,1; z=−1,44) và không gắn cổng nào; kiểm oracle/lookahead cho MB hôm nay KHÔNG có dấu hiệu nào.

## VIEC CAN LAM

**P0 — `final_bundles.created_at` bị đọc nhầm thành mốc chốt.** Ai chặn: owner (quyết định sửa cột hay chỉ sửa cách đọc). Ở đâu: `database.py:4658-4679` (UPSERT không đụng `created_at`) và mọi script forensic dùng cột này. Việc: ① thêm cột hoặc trường ghi rõ `content_written_at` / ghi `notes` mang giờ t10_chot, HOẶC ② nếu không sửa schema thì ghi luật thành văn vào đủ sáu mặt: «mốc chốt = `_v10782_freeze.T_CHOT_MARKS`, KHÔNG phải `final_bundles.created_at`», kèm dòng cảnh báo trong `docs/CURRENT_TRUTH_SSOT.md` §mốc giờ. Bắt buộc kèm bản RÚT LẠI theo PRJ-RETRACTION-001 cho hai câu của V11164 g1 («MT bundle 827 tạo 16:46:00 · sớm 12 phút» và «MN bundle 825 tạo 05:21:04»). **Phiên này CẤM sửa** (phiên soi).

**P0 — stdout production chết 28 giờ.** Ai chặn: owner (việc khôi phục cần **restart service** — phiên này cấm restart). Ở đâu: PID 3370750; mã nuốt lỗi `main.py:60-80`, `scheduler.py:235-260`, `gpt_analyzer.py:43-66`. Việc: ① owner quyết có restart để lấy lại quan sát không; ② dựng CỔNG MÁY canh «stdout còn sống» — cổng phải tự chứng minh chặn được theo RM-15 (giả lập stdout hỏng ⇒ thoát ≠ 0); ③ sửa `_safe_print`: khi phải hạ xuống null-writer thì bắt buộc ghi MỘT dòng vào `scheduler_logs` (kênh DB vẫn sống) — hiện tại nó im lặng tuyệt đối; ④ tái hiện nguyên nhân gốc trên bản sao ngoài production (60+ tệp `_v*` dùng khuôn `io.TextIOWrapper(sys.stdout.buffer)`).

**P1 — gpt-oss-120b official ăn ngữ cảnh shadow.** Ai chặn: owner (đây là [B] của V11165, đã biết, chưa có quyết định vá). Ở đâu: `gpt_analyzer.py:6738` (điểm neo V11165) — tái hiện 3/3 miền ngày 05/09. Việc: quyết vá hay đóng băng; trước khi vá phải chốt: mọi phép so official-vs-shadow đã chạy có model này đều phải đánh dấu nhiễm.

**P1 — MT bị EXCLUDE_PRIMARY vì cap cố ý (0/30 ngày INCLUDE).** Ai chặn: owner (bản vá **VA-h12** đã code + 30/30 test, replay đổi 45 dòng, **chưa deploy** — chờ quyết định deploy). Ở đâu: `main.py:9816-9847` (cap), `database.py:5087` (chuỗi «Thiếu N model»), `wr_gate_filtered` dán nhãn sai ở `main.py:10511`. Việc: deploy VA-h12 hay ghi rõ lý do hoãn; đồng thời tách nhãn `max_voters_cap` khỏi `wr_gate_filtered`.

**P1 — DIVERSITY của combo-no-token làm mất nhiều hơn làm được.** Ai chặn: owner (đổi hành vi sinh số ⇒ phải có quyết định). Ở đâu: `scheduler.py:3651-3678`. Việc: đăng ký ngưỡng TRƯỚC rồi dựng đo shadow tắt/bật (RM-03), KHÔNG tắt thẳng trên production. Lưu ý giảm nhẹ: combo-no-token không output-eligible nên không đổi số công bố — mức ưu tiên là P1 vì nó bóp méo hồ sơ đo, không phải vì nó hại người dùng.

> ⚠️ **Cố ý trích MỘT cửa sổ cho bộ k số** (`PRJ-SELECTION-WINDOW-001` · RM-18). Bản này **không**
> tuyên bố hiệu quả của lô2 / bộ k đuôi, nên **30 / 90 / 180 ngày** đều để trống có chủ ý. Bộ đủ
> nằm ở **V11086**, đo trên nền đúng `1 − (1−b)^k` (**không** phải nền 1 số): **30 ngày −3,96pp ·
> 90 ngày −5,15pp · 180 ngày −0,35pp** — cả ba đều **âm**.
**P2 — Rút lại hai câu của bản chụp đầu phiên** (PRJ-RETRACTION-001, đủ bốn phần). Ai chặn: agent phiên này ghi, owner duyệt. Ở đâu: bản chụp V11166 và mọi báo cáo dùng lại nó. Hai câu: ① «04/09 là ngày DUY NHẤT đạt 0/0/0 rỗng trong 12 ngày» → thật ra 8/12 ngày đạt, 05/09 cũng đạt; ② «MB BT=37 TRÚNG, lo2 TRÚNG» → `lo2_status=PARTIAL` (64 trượt).

**P2 — Lệch `model_count` vs `score_breakdown`.** Ai chặn: không ai — cần một phiên ĐO riêng. Ở đâu: `

## PHAT HIEN
  [P0][PROVEN_DEFECT] `final_bundles.created_at` KHÔNG phải mốc chốt — nội dung công bố do job t10_chot ghi sau đó, MN lệch 10 giờ 21 phút
  [P0][PROVEN_DEFECT] stdout của tiến trình production chết từ 04/09 16:53:48 — mất toàn bộ chẩn đoán print(), 28 giờ, KHÔNG triệu chứng
  [P1][PROVEN_DEFECT] gpt-oss-120b (OFFICIAL, voter cả ba bundle) chạy trên GÓI NGỮ CẢNH SHADOW — tái hiện sống 3/3 miền ngày 05/09
  [P1][PROVEN_DEFECT] MT bị EXCLUDE_PRIMARY vì cap CỐ Ý bị đọc ngược thành «Thiếu 2 model» — 29/30 ngày, KHÔNG ngày nào INCLUDE
  [P1][PROVEN_DEFECT] Cơ chế DIVERSITY của combo-no-token LÀM MẤT nhiều hơn LÀM ĐƯỢC — 139 vs 91 cặp lệch, ba thước đều khác 0
> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18 · RM-21). Đoạn dưới đo **NỀN**
> cho thước bạch thủ và báo kết quả **trên toàn bộ 479 bundle LIVE**, không tuyên bố hiệu quả theo
> một cửa sổ riêng. Bộ đủ **14 / 30 / 90 / 180 ngày** nằm ở **V11084 + V11086**, và ở đó **dấu ĐỔI**:
> 30 ngày **+4,07pp** · 90 ngày **−3,18pp** · 180 ngày **+0,91pp** (CI95 [−3,2 ; +5,0]).
> Bản này có nêu 5 cửa sổ 7/30/60/90/160 ở bảng 20 ô — con số trích riêng ở đây chỉ là **tóm tắt**
> của bảng đó, không phải một cửa sổ được chọn cho khớp kết quả.
  [P2][NO_ANOMALY_FOUND] MB trúng bạch thủ 37 ngày 05/09 — KHÔNG có dấu hiệu oracle/lookahead nào
  [P2][EXPECTED_BEHAVIOR] 12 lượt MT sau 16:51:30: 11 shadow bị chặn theo thiết kế + 1 combo-super ĐÃ vào bundle — bình thường, không bất thường
  [P2][NO_ANOMALY_FOUND] Cảnh báo [DUPLICATE_CONCENTRATION] không hơn nền và không gắn cổng nào — 430 ca, z = −1,44
  [P2][PROVEN_DEFECT] «04/09 là ngày DUY NHẤT đạt 0/0/0 rỗng trong 12 ngày» — không tái lập được; 8/12 ngày đạt, và 05/09 cũng đạt
  [P3][OPERATIONAL_IMPROVEMENT] db_env_drift: khoá Google trong .env khác khoá trong DB, DB thắng — 828 dòng / 140 ngày, không gây hỏng nhưng .env là override chết
  [P2][SUSPICIOUS_NEEDS_MORE_EVIDENCE] `model_count` đếm DÒNG qua cổng, không đếm model THỰC SỰ bỏ phiếu — MT 13 vs 12 model trong breakdown, chưa tách bạch được
  [P3][EXPLORATORY_PREDICTIVE_SIGNAL] MB chuyển từ INCOMPLETE kinh niên sang COMPLETE 6/7 ngày gần nhất — chưa được phép kết luận