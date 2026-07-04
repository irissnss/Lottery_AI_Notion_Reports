# V10774 — MỐC ML TỪNG MIỀN: kiểm chứng lại + RF-MB đo RIÊNG TỪNG MỐC + vá log-mốc + dọn root — 2026-07-05

## Câu hỏi của owner (nguyên văn, 04-05/07)

> "ML vừa rồi xác định mốc cho từng miền rồi, giờ có cần kiểm chứng lại không? có cần xác định, phân tích lại không? với ML model RF của MB vừa fix thì đang đo lường, xác định là ở mốc nào? đã kiểm chứng, phân tích cho từng mốc chưa hiện đang báo cáo chung chung lắm chưa rõ ràng ah em. Root cũng quá hỗn loạn cũng cần dọn dẹp sạch sẻ tinh gọn bớt đi em"

## Trả lời dứt điểm

### 1. Bản đồ MỐC THẬT (đọc từ dữ liệu, không suy đoán)

- **MB ML có 2 mốc mỗi ngày:**
  - **04:00** (`auto_daily`) — giá trị gốc buổi sáng, được giữ ở cột `pre_result_numbers` (phủ 220/224 bản ghi từ 10/5).
  - **17:30** (`rerun_post_mt`) — dự đoán lại sau khi có KQ miền Trung, là `main_numbers`; vẫn TRƯỚC giờ quay MB 18:15 nên hợp lệ để chơi.
  - **D-1** = mốc 17:30 của NGÀY HÔM QUA (nền của V10767).
- **MT:** đã khóa mốc **04:00** (V10766) — kiểm chứng live: từ 02/07 không còn rerun 16:35, chỉ còn `auto_daily 04:00`. Chạy ĐÚNG.
- **MN:** chỉ có DUY NHẤT 1 mốc 04:00 (224/224 bản ghi từ 10/5) — không có mốc nào khác để so.
- **RF của MB đang đo ở mốc nào?** Shadow V10772 trước giờ **CHỈ đo mốc 17:30** (đối chiếu 3 ngày: số shadow = main_numbers 17:30, không phải 04:00). Đây đúng là chỗ "chung chung" anh bắt — đã sửa ở mục 3.

### 2. Kiểm chứng TỪNG MỐC (56 ngày 10/5→04/07, kinh tế /choi 50đ × 98k × 27k, tie-break khớp số official live 02-04/07)

**RF-MB theo mốc — DƯƠNG Ở CẢ 4 MỐC, đều BỀN 2 nửa:**

| Mốc RF | P&L 56d | Nửa 1 | Nửa 2 | Bền? |
|---|---|---|---|---|
| RF @ điều-kiện (dom≤10→17:30, else D-1) | **+44.8M** | +17.5M | +27.3M | BỀN |
| RF @ 17:30 | +39.9M | +12.6M | +27.3M | BỀN |
| RF @ 04:00 | +25.2M | +2.8M | +22.4M | BỀN |
| RF @ D-1 | +20.3M | +12.6M | +7.7M | BỀN |

→ Giả thuyết RF **không phụ thuộc mốc** — mạnh ở mọi mốc, tốt nhất là mốc điều-kiện.

**Plurality (nền của official) theo mốc:**

| Mốc plurality | P&L 56d | Bền? |
|---|---|---|
| @ điều-kiện V10770 (mốc official ĐANG chạy) | **+30.1M** | **BỀN** |
| @ D-1 | +5.6M | — |
| @ 17:30 | −23.8M | — |
| @ 04:00 | −28.7M | — |

→ **Mốc V10770 kiểm chứng lại VẪN ĐÚNG** (duy nhất dương và bền trong 4 mốc plurality). KHÔNG cần đổi mốc. Vấn đề còn lại: plurality thua RF ở MỌI mốc (−14.7M ngay tại mốc đang chạy) — đây là câu hỏi của checkpoint RF 14/07, không phải câu hỏi mốc.

**Theo THỨ (trục bucket miền+thứ):** RF yếu nhất Thứ 2 (@17:30 −11.8M) nhưng RF@D-1 lại mạnh Thứ 2 (+27.4M); Thứ 5 và Thứ 3 mạnh nhất ở mọi mốc.

**MT RF (so cùng 52 ngày có cả 2 mốc):** mốc 16:35 cũ +62.3M BỀN > mốc 04:00 +42.7M (nửa 1 −0.7M). Lưu ý trung thực: sau V10766, mốc 16:35 KHÔNG còn tồn tại để đo tiếp (đánh đổi đã ghi nhận). Forward mốc 04:00 sau khóa: +10.1M/3 ngày — theo dõi tới 16/07, không đổi gì lúc này.

### 3. Phát hiện forensic + đã vá (V10774)

- **Log mốc từng bị restart-deploy ghi đè** → lịch sử mốc bị sai 2 ngày:
  - 01/07: bundle thật `[56,90]` (aggregate cũ — V10767 deploy tối đó SAU giờ chốt bundle) nhưng log 23:02 ghi "applied D-1" (ảo).
  - 02/07: bundle thật `[56,88]` = **D-1 (V10767)** nhưng log bị restart 20:22 (deploy V10770) đè thành "sameday [38,29]".
  - **Timeline mốc THẬT của official MB: tới 01/07 aggregate cũ → 02/07 D-1 → từ 03/07 mốc điều-kiện V10770** (03/07 `[99,77]`, 04/07 `[29,62]` — log ghi cùng giây với bundle, chuẩn).
- **Vá:** log-guard V10774 — log mốc chỉ được ghi đè khi còn TRƯỚC 18:15 của đúng ngày; sau giờ quay chỉ thêm-nếu-chưa-có. Test pass: log cũ không bị đè khi gọi lại, hành vi chọn số KHÔNG đổi.
- **Shadow V10772 mở rộng 8 → 12 variant**: thêm `RF@04:00`, `RF@D-1`, `RF@điều-kiện`, `plurality@04:00` — từ nay panel 🌲 trên /monitoring đo FORWARD **riêng từng mốc**, mỗi dòng gắn nhãn mốc tường minh, hết chung chung.

### 4. Dọn root

~110 file rời ở thư mục gốc dự án đã gom về đúng chỗ: 60 báo cáo audit cũ (tháng 4-5) → `docs/archive/root_reports_2026H1/`; script/bat/log/zip cũ → `backups/root_archive_20260705/` (trong đó `gpt_analyzer.py` ở root là bản stale 12/04 — bản sống nằm ở `web/backend/`); script tạm của phiên → `backups/`. Root giờ chỉ còn file cấu hình + `CHANGELOG.md`.

### 5. An toàn + verify

- KHÔNG đụng /du-doan, final_bundles writer, selector; chỉ shadow + log-guard + nhãn UI.
- Hash 4 bảng official pre/post deploy **IDENTICAL** (predictions 9268, final_bundles 381, lottery_results 15010, model_daily_eval 9132).
- Smoke: health 200, /du-doan 200, admin API 401, 6 zombie API vẫn 404. VPS live: 12 variant chạy, backfill 96 ngày đủ, log-guard hiện diện trong code live.
- Backup: `backups/v10774_pre/`. Rollback = restore backup + restart.

### 6. Chờ owner (không tự làm)

1. **CP-66.9** adaptive-exploit MN (quá hạn) — promote/đóng.
2. OK/không OK **drop 41 bảng chết**.
3. **Checkpoint RF-MB 14/07**: đọc cột FORWARD theo TỪNG MỐC — nếu RF vẫn dẫn plurality ≥2 tuần forward, đề xuất chuyển official MB sang RF (dự kiến mốc điều-kiện).
