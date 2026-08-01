# V10917 — Tắt 5 lớp ghi đè bạch thủ (01/08/2026)

**Kết quả chính:** 37% số ngày, bạch thủ công bố **không phải** số thắng phiếu bầu của các
model. 5 lớp ghi đè chạy sau khi cộng phiếu đã vứt đi những số tốt. Đã tắt 5 lớp, giữ 1 lớp.

**Con số:** 28,9% → **35,6%** trúng · −96,5tr → **−23,0tr** trên 60 ngày (đỡ **73,5 triệu**).
Miền Bắc từ lỗ 27,1tr thành **lãi 12,1tr**.

**Đo tiến 60 ngày live, từng lớp:**
- V10640·MN specialist: **+14,7tr** → GIỮ
- V10640·MT nt_consensus: −24,5tr → tắt
- V10640·MB prior_region: −29,4tr → tắt
- V10767·MB hôm trước: ±0 → tắt
- V10789·MB luồng test: −4,9tr → tắt
- V10790·MT luồng test: −9,8tr → tắt

**Chắc chắn:** mô phỏng chuỗi qua cổng kiểm 180/180 · McNemar p=0,0075 · bootstrap 20k thắng
99,9% · chia đôi thời gian cùng chiều cả hai nửa.

**Owner quyết:** *"Xử lý an toàn, cải tiến, cải thiện, tinh gọn, sạch sẽ cho cả 3 miền nha em."*

**Nói thẳng:** vẫn lỗ −23tr/60 ngày — đây là bớt chảy máu, chưa phải hệ có lãi. Lớp MN giữ lại
**chưa đạt chuẩn chắc chắn** (p=0,754), đã ghi ngưỡng: rà 31/08, âm tiền thì tắt nốt.

**Bài học:** V10655→V10672→V10677→V10753→V10789→V10790, lần nào cũng có backtest hứa +7 đến
+22pp rồi rữa. Luật mới ghi vào code: đừng bật lại bằng backtest, chỉ bằng đo tiến.

**Đã dựng:** panel `/monitoring` + `/api/admin/override-watch` đối chiếu phiếu bầu vs số công bố
mỗi ngày — lỗ hổng khiến lỗi này âm ỉ nhiều tháng.

**Deploy:** service `lottery`, PID 503462→547740, health 200, hash 4 bảng khoá giữ nguyên.
Gỡ về: `_v10917_deploy.py --rollback`.

**Theo dõi:** FU-183 (ngưỡng MN 31/08) · FU-184 (xác minh MT/MB 02/08) · FU-185 (tinh gọn lane).

**Báo cáo đầy đủ + bằng chứng:**
https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/master/V10917_OVERRIDE_LAYERS_20260801
