# s6-be-mat · tang=PARTIAL

## TOM TAT

CỔNG 6 — BỀ MẶT PHỤC VỤ, đo trên production thật (main.py sha 4ed5fd7ebaee8d23, PID 3370750, cổng 8000, DB mode=ro, nginx access.log).

BỨC TRANH MỘT CÂU: hệ chạy đúng bên trong (bundle 831/833/835 có thật, `database.get_final_bundle('2026-09-05', X)` trả đúng MN BT=74 · MT BT=86 · MB BT=37) — nhưng NGƯỜI DÙNG THẤY BA THỨ KHÁC NHAU tuỳ quyền, và hai trong ba là sai.

① Kiểm kê 210 route: 58 PUBLIC · 144 REQUIRE_ADMIN · 7 FAIL_CLOSED_ADMIN · 1 ADMIN_SOFT. **0 route `/api/admin/*` thiếu cổng.**

② `/du-doan` 200 (shell) nhưng JS chuyển hướng `/login` khi chưa đăng nhập · `/du-doan-test` 401 · `/monitoring` 401. **viewer-freeze VẪN kẹp `2026-06-07` — y hệt V11164, nay là 90 ngày**; hằng số khoá cứng `main.py:6337-6338`, không có đường mở ngoài sửa mã.

③ NGƯỜI DÙNG THẤY GÌ:
· **khách vô danh**: `/api/status` trả dự đoán **07/06** (gemma-4-31b 32/16 · deepseek-v4-pro 39/65 · kimi-k2.5 17/85) — KHÔNG khớp 831/833/835, lệch 90 ngày. Nhưng `/api/results/*`, `/api/win-rates`, `/api/model-ranking`, `/api/accuracy/*` cùng lúc trả **05/09 LIVE**. Cùng một khách, hai nửa trang nói hai ngày khác nhau.
· **viewer đăng nhập** (`testviewer`, im 57 ngày): `/api/final-bundle` → 403 (FU-438) → UI hiện **«❌ Lỗi tải dự đoán»**, không thấy số nào.
· **admin**: thấy đúng số hôm nay — nginx 05/09 ghi `/api/final-bundle 200 ×7`, `/api/predictions 200 ×6`, `/du-doan 200 ×8`.

④ Nhãn consensus ba bundle hôm nay: MN `moderate` (3/15 = 20,0%) · MT `strong` (5/13 = 38,5%) · MB `strong` (6/15 = 40,0%). Đối chiếu nguồn độc lập (đếm model trong `predictions`, lọc đúng cửa sổ chọn, bỏ `shadow_auto_eval`) — **hôm nay nhãn KHỚP, không bị thổi phồng**; 0/570 bundle lệch khỏi luật trong mã. Vấn đề là NGỮ NGHĨA: 509/570 (89,3%) mang nhãn «🔥 Đồng thuận cao» với trung vị chỉ **38,5%** model đồng ý, thấp nhất 23,5%.

⑤ `/monitoring`: 75 hàm panel · 78 endpoint · **0 endpoint 404** · **0 lượt 5xx trong toàn bộ nginx log** · 44/75 panel làm mới 60s (31 nạp 1 lần — quyết định V10773 có chủ ý) · **4 panel đọc bảng đã ngừng ghi 58/62/128 ngày + 2 bảng RỖNG**.

⑥ Số đã rút lại: **12 chỗ vẫn khẳng định mệnh đề ĐÃ RÚT** (RL-002/008/009/010/011/014/015) — 7 chỗ trong `docs/FOLLOW_UP_TRACKER.md`, 2 trong `DE_XUAT_MATERIALIZATION_V11163.md`, 1 trong `CURRENT_TRUTH_SSOT.md`, và 3 trong báo cáo CÔNG KHAI (`REPORT_V11054` và `REPORT_V11163` **không có một dấu rút lại nào**). Nghiêm trọng hơn: **chính cổng `_v11085` đang mù hai chỗ**, chứng minh được hai chiều.

⑦ Lộ thông tin nhạy cảm: **KHÔNG**. 13 tệp tĩnh + 20 phản hồi API vô danh + 5 phép gọi sai — sạch. Một cảnh báo duy nhất ở `du-doan.html:1516-1517` là

## VIEC CAN LAM

P0 — CỔNG QUẢN TRỊ ĐANG MÙ, PHẢI VÁ TRƯỚC
1. **Vá `_v11085_cong_rut_lai.py` — hai điểm mù.** Ai chặn: agent (không cần owner, đây là vá cổng không đụng production). Ở đâu: `::quet_van_ban` (thêm so khớp khử dấu NFD cho cả dấu hiệu lẫn văn bản) và `::_trong_ngoac` (BỎ `*` khỏi cặp đối xứng, hoặc chỉ tính `*` khi không phải `**`). **Bắt buộc kèm thử chặn hai chiều theo RM-15** — giả lập vi phạm ⇒ deny, trạng thái sạch ⇒ allow. Không thử thì coi như cổng không tồn tại.
2. **Chuẩn hoá `docs/SO_RUT_LAI.json`.** Ai chặn: agent. Ở đâu: 10 mục RL-007..RL-016 — viết lại `dau_hieu` CÓ DẤU đúng như nó xuất hiện trong tài liệu (hoặc để cổng khử dấu hai chiều, chọn một, đừng làm cả hai nửa vời — §60.1).

P1 — RÚT LẠI ĐÚNG CHỖ ĐÃ CÔNG BỐ (`PRJ-RETRACTION-001`)
3. **Đính chính 7 chỗ trong `docs/FOLLOW_UP_TRACKER.md`** (:150 RL-015 · :154 RL-014 · :210 RL-009 · :221,223 RL-008 · :258 RL-010 · :364 RL-011). Ai chặn: agent. Ghi ngay tại dòng, đủ bốn phần bắt buộc.
4. **Đính chính `docs/DE_XUAT_MATERIALIZATION_V11163.md`:86,:140 và `docs/CURRENT_TRUTH_SSOT.md`:2880.** Ai chặn: agent.
5. **Bổ sung mục RÚT LẠI vào hai báo cáo CÔNG KHAI chưa có dấu nào:** `V11163_DIEN_TAP_MIGRATION_20260904/REPORT_V11163.md` (RL-008) và `V11054_PROMPT11_GD0_GD3_20260809/REPORT_V11054.md` (RL-002). Ai chặn: agent + push kho công khai. Ở đâu: kho `Lottery_AI_Notion_Reports`.
6. **Đánh dấu tại CHỖ GỐC `REPORT_V11164.md`:421** (mục rút lại đã có ở :440+ nhưng chỗ gốc không trỏ tới). Ai chặn: agent.

P1 — BỀ MẶT NGƯỜI DÙNG
7. **Quyết định freeze: mở lại hay đóng cho nhất quán.** Ai chặn: **OWNER** — đây là quyết định của owner ngày 08/06, agent không tự đổi. Ở đâu: `main.py:6337-6338`. Hai lựa chọn phải trình rõ: (a) mở `_VIEWER_FREEZE_ENABLED=False`; (b) giữ đóng nhưng áp freeze NHẤT QUÁN sang `/api/results/*`, `/api/win-rates`, `/api/model-ranking`, `/api/accuracy/*` để bề mặt vô danh không tự mâu thuẫn. **Cấm agent tự chọn.**
8. **Vá `du-doan.html:1377` — kiểm `r.ok` trước `r.json()`**, phân biệt 403 (đã đóng cho quyền viewer) với lỗi thật. Ai chặn: agent, nhưng câu chữ hiển thị cho viewer thì **cần owner duyệt** (đụng thông điệp ra người dùng).
9. **Tách kế toán `wr_gate_filtered` khỏi `max_voters_cap`.** Ai chặn: **OWNER** — chạm `day_governance`, đã có mã theo dõi FU-449, và VA-h12 đã code+test 30/30 nhưng CHƯA deploy. Ở đâu: `main.py:9840` (gộp tập) + `du-doan.html:1438-1444,1451-1456` (câu «model chất lượng thấp»). Đây là mặt người dùng thấy của phát hiện [G] — hôm nay MT đang hiện đúng câu sai đó.
10. **Thống nhất định nghĩa «đủ model».** Ai chặn: agent trình, owner duyệt. Ở đâu: UI dùng `output_eligible_row_count` (15 ⇒ ✅ COMPLETE) trong khi `day_governance` dùng `completed_model_count` (13 ⇒ INCOMPLETE/EXCLUDE_PRIMARY). Phải chọn MỘT hoặc hiện cả hai kèm nhãn rõ.

P2 — NHÃN VÀ PANEL
11. **Đổi ngưỡng consensus từ số TUYỆT ĐỐI sang TỈ LỆ** (hoặc đổi chữ hiển thị). Ai chặn: **OWNER** — đổi chữ ra người dùng. Ở đâu: `main.py:10338-10345` + `du-doan.html:1467-1468`. Số để owner quyết

## PHAT HIEN
  [P0][PROVEN_DEFECT] Cổng chống-trích-lại `_v11085` MÙ hai chỗ — dấu hiệu không dấu (10/16 mục) và `**bold**` bị tính là dấu trích dẫn
  [P1][PROVEN_DEFECT] 12 chỗ trong tài liệu và báo cáo CÔNG KHAI vẫn khẳng định mệnh đề ĐÃ RÚT LẠI — `PRJ_RETRACTION_SILENT`
  [P1][PROVEN_DEFECT] Bề mặt vô danh TỰ MÂU THUẪN: khối dự đoán đóng băng 07/06 nằm cạnh khối kết quả/xếp hạng LIVE 05/09
  [P1][PROVEN_DEFECT] MT hôm nay: UI gọi TRẦN VOTER CỐ Ý của owner là «2 model chất lượng thấp đã lọc»
  [P1][PROVEN_DEFECT] MT hôm nay: huy hiệu UI ✅ COMPLETE trong khi sổ quản trị ghi DEGRADED_LIVE_DAY / INCOMPLETE / EXCLUDE_PRIMARY
  [P1][PROVEN_DEFECT] Viewer đăng nhập nhận 403 nhưng màn hình hiện «❌ Lỗi tải dự đoán» — UI không kiểm `r.ok`
  [P2][PROVEN_DEFECT] «🔥 Đồng thuận cao» gắn cho 89,3% bundle — trung vị chỉ 38,5% model đồng ý, thấp nhất 23,5%
  [P2][OPERATIONAL_IMPROVEMENT] 4 panel /monitoring đọc bảng đã ngừng ghi 58-128 ngày, trong đó 2 bảng RỖNG hoàn toàn
  [P2][OPERATIONAL_IMPROVEMENT] REPORT_INDEX.md (tài liệu sinh tự động) trễ 67 bản / 15 ngày — liệt kê tới V11098 trong khi kho đang ở V11165
  [P3][NO_ANOMALY_FOUND] Không có bề mặt nào lộ khoá / token / đường dẫn nội bộ — quét 13 tệp tĩnh + 20 phản hồi API vô danh + 5 phép gọi sai
  [P2][EXPECTED_BEHAVIOR] viewer-freeze vẫn kẹp 2026-06-07 — y hệt V11164, nay tròn 90 ngày; không có đường mở ngoài sửa mã
  [P3][EXPECTED_BEHAVIOR] 31/75 panel /monitoring không đăng ký làm mới 60s — có chú thích quyết định V10773, không phải bỏ sót
  [P3][INDETERMINATE] Nội dung từng panel /monitoring khi admin mở — KHÔNG ĐO ĐƯỢC trong phiên này