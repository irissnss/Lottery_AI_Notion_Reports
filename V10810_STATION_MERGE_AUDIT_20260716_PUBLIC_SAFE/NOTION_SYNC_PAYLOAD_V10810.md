# V10810 — Audit đài sau sáp nhập tỉnh 1/7 + repair 6 dòng tên đài (16/07/2026)

**Owner hỏi (11:49):** Sau 1/7 sáp nhập tỉnh, đài cũ gộp về tỉnh mới → 1 tuần đài sổ 2 lần khá nhiều? Hệ thống ghi nhận có đúng hiện tại không — đài, tên đài, thứ, kiểm tra lại luôn.

**Kết quả chính:**
- Lịch đài × thứ KHÔNG đổi sau 1/7: phương án gộp 9 đài MN (TP.HCM 4 lần/tuần...) chỉ là DỰ THẢO — Bộ Tài chính chỉ đạo giữ lịch cũ đến khi công ty XS chạy mô hình mới; MT chưa có phương án. Thực chứng 15/07: DB khớp web 100% (ĐB 008402/867898/282199).
- Đài 2 lần/tuần hiện tại (HCM T2+T7, Khánh Hòa T4+CN, Huế T2+CN, Đà Nẵng T4+T7, Hà Nội T2+T5) đã như vậy TỪ 2020 — không phải hiện tượng mới.
- THIẾU SÓT THẬT tìm thấy: 6 dòng kết quả MT ghi MÃ TẮT thay vì tên đài (QB/QT 25/06, GL/NT 03/07, DLK/QNA 07/07 — parser dự phòng xskt) → 8 dòng đánh giá rule bị câm lặng lẽ, gồm 5 rule Ninh Thuận (đài best-spot số 1) và 3 HIT thật bị bỏ lỡ (tail 17, 54, 84).
- Đã sửa 4 tầng: (1) repair 6 dòng — có backup, guard ĐB đối chiếu web từng dòng; (2) backfill 8/8 dòng rule-eval; (3) chuẩn hóa tên đài ngay tại điểm ghi DB (mọi luồng) + 13 alias mã tắt; (4) check-11 mới trong self-check T2 hằng tuần — PASS ngay.
- An toàn: hash predictions/final_bundles/model_daily_eval PRE=POST GIỐNG HỆT; lottery_results delta chủ đích đúng 6 dòng (đã backup); shadow A/B V10809 không ảnh hưởng.
- Việc cần nhớ: khi Bộ TC áp dụng lịch mới THẬT → 1 phiên riêng cập nhật đài kỳ vọng + rule nguồn đài cũ; 2 chuông báo tự la ngày đầu.

**Chi tiết đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10810_STATION_MERGE_AUDIT_20260716_PUBLIC_SAFE/` (báo cáo + evidence raw + conversation context).
