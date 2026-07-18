# CONVERSATION CONTEXT — V10822 (2026-07-18, phiên 21:00)

## Owner message (verbatim, 21:00)

> Có 2 vấn đề anh cần em tìm hiểu kỹ.
> 1/ Rules có được tổng hợp phân tích xếp hạng hàng ngày hàng tuần không em?
> 2/ Nếu /choi , offical không can thiệp được để vì sẽ phá đo lường không đo được, thế lane test có xử lý được không . anh cũng muốn 1 luồng output mới để chơi 10 ngày tới chứ nhi

## Bối cảnh liền trước

- V10820 (17/07 23:33, owner ký): RULES-FIRST vào prompt production PB-18.1, live trial 18→28/07.
- V10821 (18/07 19:39, owner flag): ngày-1 bundle BT 0/3 dù model any 15/21 → Total-V2 shadow (M0/M1/M2s/M4) live, backtest 165d M2s thắng bundle +5.7→+11.6pp BT.
- Phiên này (21:00): owner muốn (1) xác nhận đường ống phân tích rules, (2) một luồng output MỚI có thể CHƠI ngay trong 10 ngày tới mà không phá các phép đo đang chạy.

## Việc đã làm trong phiên

1. Probe đường ống rules trên VPS (cron + scheduler + DB): xác nhận MRE daily 20:15 (2.978 rows/205 ngày), re-rank MB 20:30 + MN/MT 04:40 & 20:35 (lifecycle + rank 1..35, snapshot daily), weekly miner T2 00:30 (v2026W29, 105 rules, 21 đợt mine).
2. Probe hạ tầng lane: evaluator chấm generic, scoreboard 7/14/30d, /choi chỉ nhận method đủ 24-30 ngày vào khóa tuần → lane mới an toàn tuyệt đối cho 10 ngày.
3. Viết + deploy lane `TOTAL_V2_RULES_V1` (3 miền): M2s coverage-rules, union rules tính LIVE (hàm mới `live_rules_union` dùng chung emission helpers với MRE), cron MN 15:47 / MT 16:56 / MB 17:56, đăng ký 3 experiment ACTIVE_TEST, khối 🚏 trong panel 🧮.
4. Phát hiện + vá bug V10821: cron shadow 19:14 chạy trước MRE 20:15 → rules_active luôn 0 ở ngày mới; dời 20:50 + re-chấm 18/07 (MT bộ2 [41,97]→[41,46] 46✓; M2s any ngày-1 2/3). Preview pre-draw cũng chuyển sang union live.
5. Chuỗi §52 đầy đủ: backup 2 đầu, sha khớp, compile + node --check, restart lottery.service, health 200/admin 401, journal sạch, hash 4 bảng official IDENTICAL, CHANGELOG/SSOT/FU/STATE/HISTORY/PLAYBOOK/SO_TAY, Notion + 2 push.

## Owner message thứ 2 (verbatim, 21:44)

> Luồng mới cũng dùng để đo để so sánh luôn được mà em đúng không? vấn đề là em thao tác đã backup chưa luồng lane test mặc dù phụ nhưng đừng quên nó nhé em. Chú ý tất cả phải được backup ghi nhận cụ thể tránh không quay đầu được nha em. Ghi nhận tất cả dùm anh nhé , nếu theo luồn mới thì dự đoán hôm nay là bao nhiu em cũng nên total lại luôn để có lịch sử từ đây luôn em. Code fix xong cập nhật ghi nhận tổng lực toàn bộ tránh quên lang , tất cả phải được tuy duy , logic , liên quan , tương thích ,liền mạch nhất quán tránh rơi rớt bỏ sót bất kỳ vấn đề gì nha em

## Việc bổ sung sau message 21:44 (V10822b)

1. Xác nhận lane = kênh ĐO chính thức (tự chấm + scoreboard 7/14/30d vs 34 lane + baseline control; đọc chốt 28/07); caveat union live vs MRE ghi thành train/serve gap đo được.
2. Vá thiếu sót backup lượt đầu: crontab pre/post tái dựng + lane script deployed + snapshot JSON (registry + ngày-0 + pre-fix values row shadow 18/07) — cả VPS lẫn local.
3. Viết `_v10822_rollback.py` (dry-run mặc định, --confirm mới chạy): gỡ cron/file/DB lane + restart + verify; mặc định giữ cron 20:50.
4. Ghi NGÀY-0 18/07 vào lane (run_id 8253-8255, mode RETRO_POST_DRAW_BASELINE, đánh dấu rõ): MN [31,38]✗ · MT [41,46] 46✓phụ · MB [93,86] 86✓phụ = any 2/3 — /choi tự loại (cutoff giờ), scoreboard không tính, chỉ hiện khối 🚏 làm mốc lịch sử.
5. Hash 4 bảng official IDENTICAL lần 2; cập nhật CHANGELOG mục 5 / SSOT row / FU / STATE / HISTORY V10822b / PLAYBOOK / SO_TAY + Notion patch + 2 push.

## Trạng thái sau phiên

- Ngày-0 (18/07) đã nằm trong lane (retro, không tính forward); lane ghi số FORWARD đầu tiên: 19/07 (MN 15:47 · MT 16:56 · MB 17:56) — owner lấy số ở khối 🚏 panel 🧮 /monitoring.
- Đọc chốt 28/07 cùng V10820/V10821; lane đủ điều kiện ứng viên khóa tuần /choi ~12-17/08.
- Rollback trọn gói: `_v10822_rollback.py` + backup 2 đầu.
