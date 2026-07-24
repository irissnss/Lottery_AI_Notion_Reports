# V10844 — Owner duyệt 23:45 24/07: triển khai đo what-if /choi MB + AE theo nguồn (shadow only)

- Owner: "Các vấn đề an toàn, có giá trị nâng cao dự đoán đã xác thực, đo lường rõ ràng thì tiến hành dùm anh đi em."
- **Làm:** (1) bảng shadow `v10844_mb_whatif_daily` so 3 cánh tay MB mỗi ngày — /choi thật · laneV2 · laneV3 — chỉ từ row đã ghi TRƯỚC cutoff 18:00 (anti-lookahead, không gọi model mới); (2) API `/api/admin/mb-whatif` (require_admin, no-store) kèm AE theo nguồn 30d; (3) panel 🔁 `/monitoring` đăng ký 60s; (4) cron 21:10 VN.
- **Không làm:** mở rộng catalog V10829 (cấm sửa giữa cửa sổ đo — skim 28/07); không đụng AE-MT (edge thật 54.5%). **Production /choi MB vẫn chạy AE** — chỉ đo.
- **Ngưỡng viết sẵn:** ≥7 ngày forward (từ 25/07): BT% lane − hit% /choi ≥ **+15pp bền** → trình owner 1 quyết định đổi nguồn /choi MB; dưới ngưỡng giữ AE + gate. Đọc sớm nhất ~01/08.
- Backfill 19–24/07 (tham khảo): /choi **0/4** · AE 0/4 · **laneV2 BT 3/6 (50%)** any 4/6 · laneV3 2/3 — khớp 100% số V10843.
- AE nguồn 30d: MT same_region_lag1 **54.5%** > per_model 44.9%; MB per_model 26.2% · sameday 23.3% ≈ baseline → xác nhận MB không edge.
- Verify: VPS restart OK, health 200, anon 401 (3 endpoint), backfill khớp từng số, cron dòng 98; **hash 4 bảng official pre=post IDENTICAL** (`5adf2f7c/74b1705d/95bf835b/c2f1589e`); backup local + remote.
- Chờ live: 25/07 21:10 row forward đầu; panel verify mắt khi owner mở /monitoring; FU-V10843 = DEPLOYED_PENDING_LIVE_VERIFY.
- Báo cáo đầy đủ: GitHub `Lottery_AI_Notion_Reports/V10844_MB_WHATIF_MEASURE_20260724/`.
