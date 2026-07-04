# V10771 + V10772 — /choi RÕ RÀNG + MB giả-thuyết random-forest (SHADOW forward) — 2026-07-04

> Public-safe report. Không chứa secret/API key/DB dump. Nguồn: audit live sync `20260704_212138` + `20260704_222127` (manifest trong repo private).

## BỐI CẢNH (lời owner, tóm tắt)

Owner bức xúc 2 đợt trong ngày:
1. `/choi` "giả tạo": số đầu-live khác cuối-live ("ảo ảo"), verdict "CHƠI" giục chơi bằng số không ổn định — "lúc này lúc kia về cuối toàn thắng thì thôi chứ còn gì nữa, làm thế anh cũng làm được".
2. Chưa trả lời dứt điểm: ML đã đổi MỐC theo từng miền, vậy Model Combo / Model Super khi tổng hợp **có lấy đúng các mốc đó không**? Live 3-4 ngày sau fix chưa được đánh giá. Phải backtest kiểm chứng method/total output sau fix. Luồng deploy GitHub private/public cũng phải nắm rõ.

## PHẦN 1 — V10771: /choi RÕ RÀNG (khóa method tuần + khóa số ngày + thành tích forward)

**Chẩn đoán (đã chứng minh bằng mô phỏng cùng ngày 04/07):**
- `/choi` cũ tự refresh 60s và tính lại từ đầu mỗi lần: bốc "method có P&L quá khứ đẹp nhất" trên lane test. Khi một miền xổ → mốc so sánh trượt 1 ngày → method đảo hạng → song-thủ ĐỔI TRONG NGÀY.
- Ví dụ thật 04/07: MN sáng `59-56` → tối `59-39`; MB sáng `68-17` → tối `26-87` (3 method MB hòa nhau 31.7M — trượt 1 ngày là đổi ngôi).
- Đây là survivorship/in-sample ("về cuối toàn thắng") — đúng như owner chê, vô nghĩa cho tương lai.
- Official `/du-doan` KHÔNG đổi số trong ngày (1 bản/miền/ngày, tạo trước giờ xổ) — luồng tin cậy.

**Fix V10771 (SHADOW/admin-only, không đụng official):**
- KHÓA method theo TUẦN (bảng `money_board_lock`) — mỗi miền 1 method/tuần.
- KHÓA số trong NGÀY (bảng `money_board_daily_lock`) — sáng = tối, hết "lúc này lúc kia".
- Tách bạch: "cơ sở quá khứ" (căn cứ chọn method) vs "THÀNH TÍCH THẬT TỪ KHI KHÓA" (forward W/L + P&L, out-of-sample) — con số trung thực để owner đánh giá.
- UI bỏ khoe P&L quá khứ như thành tích; giữ đối chiếu official.

**Verify:** test local 2 lần gọi liên tiếp giống hệt; deploy VPS health 200, `/choi` 401 (admin-gate); hash-guard 4 bảng official IDENTICAL.

## PHẦN 2 — TRẢ LỜI DỨT ĐIỂM: Combo/Super có lấy đúng MỐC từng miền không?

Có 2 TẦNG khác nhau (đây là chỗ gây hiểu lầm):

| Tầng | Là gì | Mốc |
|---|---|---|
| Model `combo-super` / `combo-no-token` | Dòng tổng hợp trong bảng predictions | LUÔN tổng hợp ML **sameday tươi** tại thời điểm chạy — KHÔNG stale |
| Bundle official `/du-doan` | Số cuối cùng publish | Chấm trọng số tất cả model, riêng MB áp **override mốc** (V10767/V10770) ở bước cuối |

- MN, MT: combo tổng hợp đúng snapshot = mốc official (MT sau V10766 chỉ còn bản 04:00 → combo cũng dựng trên 04:00). KHỚP.
- MB: model combo = số nóng sameday; mốc D-1/điều-kiện nằm ở TẦNG BUNDLE → combo MB hiển thị khác official là ĐÚNG THIẾT KẾ (ví dụ 02/07: combo-no-token `38-29`, combo-super `96-93`, official `56`).
- KẾT LUẬN: KHÔNG có bug "ML đổi mà combo đứng yên". Không có model stale (cả 28 model có bản 04/07).
- Fix hiểu lầm (Q2): thẻ combo/SUPER ở MB nay có nhãn vàng "số nóng tổng hợp trong ngày — official /du-doan (đã áp mốc) mới là số chuẩn để chơi".

## PHẦN 3 — MỐC ML TỪNG MIỀN (verify live, không phải chỉ trên giấy)

| Miền | Mốc | Bản | Live thật từ | Bằng chứng |
|---|---|---|---|---|
| MN | sameday 04:00 (không đổi) | — | — | run_source `auto_daily` |
| MT | khóa 04:00, BỎ re-predict sau MN | V10766 | 02/07 | run_source đổi `rerun_post_mn` → `auto_daily` từ 02/07 |
| MB | đầu tháng (dom≤10) sameday, còn lại D-1 | V10767→V10770 | 02/07 | shadow log basis + bundle khớp mốc từ 03/07 |

**Sự cố phát hiện (02/07):** V10770 deploy 20:00 — SAU giờ tạo bundle MB 17:34 → bundle hôm đó vẫn theo code cũ chọn `56` (LOSE) trong khi code mới chọn sameday `38` (**38 VỀ**). Lỡ cú trúng vì up code trễ ~2 tiếng.
→ **Fix Q1 (V10772b):** guard lúc khởi động service — nếu deploy sau khi bundle MB hôm nay đã tạo nhưng TRƯỚC 18h và CHƯA có kết quả MB, và số bundle ≠ số code mới → tự tính lại bundle + alert. Anti-lookahead tuyệt đối (có kết quả/đã verify → không đụng).

## PHẦN 4 — BACKTEST MB 96 NGÀY (31/03→04/07) — con số cụ thể

Đơn vị khớp /choi: song-thủ 2 số, MB 1 đài, 50 điểm/số (mỗi nháy +4.9M, chi phí 2.7M/ngày). Cách chấm lô validate **1707/1707 khớp** với cột bt_hit của hệ thống.

| Cách chọn số MB | BT trúng | Lô-2 trúng | P&L 96d | Nửa 1 | Nửa 2 | Bền? |
|---|---|---|---|---|---|---|
| **random-forest (1 mình)** | 26% | **57%** | **+59.3M** | +22.3 | +37.0 | ✅ BỀN 2 NỬA |
| lstm | 27% | 44% | +20.1M | +37.0 | −16.9 | ❌ |
| V10770 (mốc đang chạy) | 22% | 38% | +5.4M | −26.7 | +32.1 | ❌ |
| meta-learning | 19% | 41% | +5.4M | +22.3 | −16.9 | ❌ |
| official /du-doan | 17% | 39% | **−9.3M** | −7.1 | −2.2 | ❌ lỗ cả 2 nửa |
| xgboost | 22% | 45% | −9.3M | +17.4 | −26.7 | ❌ |
| D-1 plurality | 21% | 37% | −14.2M | −21.8 | +7.6 | ❌ |
| sameday plurality | 16% | 40% | −19.1M | −2.2 | −16.9 | ❌ |
| **combo-super** | 19% | 32% | **−68.1M** | −31.6 | −36.5 | ❌ TỆ NHẤT |

**4 sự thật:**
1. Official MB đang publish LỖ −9.3M/96 ngày, âm cả 2 nửa.
2. random-forest MỘT MÌNH +59.3M, lời CẢ 2 NỬA — không phải may cuối kỳ.
3. combo-super tệ nhất MB (−68M) mà vẫn là 1 lá phiếu trong bundle → kéo official xuống.
4. Tổng hợp nhiều model đang HẠI MB — mọi cách trộn (plurality/combo/official) đều thua model đơn RF.

## PHẦN 5 — QUYẾT ĐỊNH OWNER + TRIỂN KHAI (V10772)

Owner chọn 4 điểm:
- **Q1** guard deploy-trễ MB: ✅ deployed (`_v10772_mb_deploy_guard.py`, log skip `past_cutoff` đúng).
- **Q2** nhãn combo MB "số nóng vs official chuẩn": ✅ deployed (`app.js`).
- **Q3** public report + Notion: ✅ tài liệu này.
- **Q4** hướng MB: chọn **SHADOW-FIRST random-forest** (an toàn, không đổi official ngay): ✅ deployed — bảng `v10772_mb_rf_shadow` (shadow_only=1, output_eligible=0) đo 8 cách chọn số MB mỗi ngày, cột **FORWARD từ 05/07**; API admin `/api/admin/mb-rf-shadow`; panel `/monitoring` "MB — GIẢ THUYẾT random-forest" auto-refresh 60s.

**Checkpoint:** 2026-07-14 (~9 ngày forward) — nếu RF dẫn P&L forward → đề xuất chuyển official MB sang RF; nếu không → giữ V10770 và đánh giá lại.

## PHẦN 6 — VERIFY DEPLOY (bằng chứng)

- Deploy 6 file (2 module mới + scheduler + main + monitoring + app.js), service restart OK.
- Smoke: `/api/health` 200 · `/api/admin/mb-rf-shadow` 401 (admin-gate đúng) · `/du-doan` 200.
- Hash-guard 4 bảng official PRE = POST **IDENTICAL** (predictions=9268, final_bundles=381, lottery_results=15010, model_daily_eval=9132).
- Guard log trên VPS: `[V10772B-GUARD] skip: past_cutoff_23:10` (đúng thiết kế — sau 18h không đụng gì).
- RF shadow backfill trên VPS: 96 ngày, khớp audit local (RF +59.3M robust=True; official −9.3M; V10770 +5.4M).
- Rollback: flag `_V10772_MB_DEPLOY_GUARD_ENABLED=False` / drop bảng `v10772_mb_rf_shadow` / restore `backups/v10772_mb_shadow_20260704/`.

## LUỒNG GITHUB (trả lời câu owner "deploy github pri và public như nào")

- **Private `Lottery_AI_Test`**: toàn bộ code + docs quản trị (CHANGELOG, SSOT, FOLLOW_UP_TRACKER, AUTOMATION_STATE) + script deploy. Mỗi VxxxYYY: commit + push `origin master`.
- **Public `Lottery_AI_Notion_Reports`**: CHỈ report public-safe (payload Notion + context hội thoại + báo cáo kỹ thuật đã lược secret). Mỗi VxxxYYY có thư mục riêng như tài liệu này.
- **Notion**: sub-page dưới trang canonical `Lottery_AI_Test`, mirror 1:1 payload này; page-id ghi vào `AUTOMATION_STATE.json`.
