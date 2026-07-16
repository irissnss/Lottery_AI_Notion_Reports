# V10809 — Audit mốc cửa sổ xếp hạng + Shadow A/B 7 ngày live (16-22/07)

Ngày: 2026-07-16. Trigger: owner 10:35 — "xem lại rules xếp hạng mốc 12W, hệ số từng miền còn đúng không; chạy shadow 7 ngày 3 miền 5 model tốt+tệ; sau đó đề xuất hoàn hảo an toàn nhất; ghi nhận lại toàn bộ".

## Kết quả chính
- Config thật: miner 12W/16W chung 3 miền; **8W là của MB** (không phải MN); MN/MT nhấn 12W/16W; KHÔNG có mốc 6W.
- Audit forward 2921 rows: thước PER-SỐ → mốc 12W/16W dự báo TỐT (MN +12.6pp, MT +12.3pp tercile spread; MB +3.7pp, mốc ngắn 4W/6W ÂM ở MB).
- Thước CỤM-any (đang dùng để xếp hạng) hỏng: MN bão hòa ~96%; **MB ĐẢO CHIỀU −6.9..−12.9pp** (xếp theo cụm nóng = chọn ngược).
- Thiên lệch cụm: corr(nhả-nhiều-số, per-số) = **−0.62..−0.83** → ranking hiện tại thưởng nhầm rule rải thảm.
- TRẢ LỜI: mốc 12W/16W GIỮ; cái cần đổi là THƯỚC (cụm-any → per-số) — gói vào CP-L6, chưa đổi production.

## Shadow A/B 7 ngày (ĐANG CHẠY 16-22/07)
- 5 model: opus, qwen (mạnh) + gemini-flash, gpt-5-mini (kém) + deepseek (trung) × 3 miền.
- Arm B = prompt + addendum trỏ-miền/per-số (bản sandbox V10807+V10808 verified); arm A = chính production picks (0 call).
- Cron 04:20/16:48/17:42/19:15; bảng `v10809_shadow_ab_daily` shadow-only; panel 🧪 trong /monitoring.
- Day-1 MN kicked 11:04. Chi phí ~105 call ≈ 3-6 USD.

## Checkpoint (roadmap ACTIVE_ROADMAP_V10809_SHADOW_AB_7D.md — surface đầu mỗi phiên)
- CP-S1 18/07 health · CP-S2 19-20/07 giữa kỳ · **CP-S3 23/07 tổng kết → đề xuất hoàn hảo an toàn nhất** · CP-S4 26/07 gỡ cron.

## An toàn
- Hash 4 bảng official pre=post IDENTICAL; smoke 200/401/401; journal sạch; rollback 1 lệnh.

## Link chi tiết
- GitHub public: `V10809_WINDOW_AUDIT_SHADOW7D_20260716_PUBLIC_SAFE/` (báo cáo + bảng evidence đầy đủ).
