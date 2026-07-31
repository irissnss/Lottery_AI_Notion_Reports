# V10892 + V10893 — MN được soi riêng, và mốc chốt cuối ba miền

**31/07/2026** · Owner nhắc *"MN thế nào nãy giờ xoáy vào MT và MB MN không xem luôn ah em"*, rồi chốt *"Chốt cuối total output MN 15h45 / MT 16h53 / 17h53"*.

## MN soi riêng — chuỗi giờ lành mạnh, hai nghi vấn được gỡ oan

| Mắt xích | Giờ đo thật (9 ngày) |
|---|---|
| Official chốt | 04:17 – 04:19 |
| Lane sáng | 04:25 – 05:10 |
| Lane chiều | 15:47 – 15:56 (trước khi dời) |
| Khoá `/choi` | trần 16:00 |
| Xổ | 16:34 – 16:39 |

**Nghi vấn 1 — gỡ oan.** `MN_FULL_POOL` và `MN_TOPK22` ghi dòng MN lúc 17:00, sau giờ xổ MN. Nhưng chữ `lottery_results` trong code nằm trong **cam kết cứng ở docstring** ("KHÔNG đụng lottery_results") — bộ dò từ khoá dính bẫy chú thích lần thứ ba trong hai ngày. Chấm thực nghiệm 60 ngày: FULL_POOL trúng BT 45%, **thấp hơn bản Nghiệm Thu 49%** — không dấu vết lookahead. Bản chất là lane gộp một lần chạy cho cả ba miền nên dòng MN rơi muộn theo thiết kế.

**Nghi vấn 2 — sự cố lịch sử.** Khoá `/choi` MN lúc 22:14 là ngày 04/07, trước khi hệ đóng băng V10834 ra đời. 27 ngày gần nhất trần 16:00.

## Mốc chốt cuối — owner ký

MT và MB đã đúng sẵn từ lịch dời buổi sáng. Chỉ MN phải siết: bốn lane 15:47–15:56 và khoá 16:00 đều sau mốc 15:45.

Kiểm trước khi dời: bốn lane MN chỉ đọc `final_bundles` (chốt 04:17), `predictions` (xong 04:34), `lottery_results`, `mined_rules` — không cần chờ chiều. Bằng chứng mạnh nhất: `MN_DEHERD_V1` ngày 29/07 đã chạy lúc **13:01** ra số bình thường.

| Mốc | MN | MT | MB |
|---|---|---|---|
| Lane chạy | 15:36–15:39 | 16:44–16:49 | 17:38–17:44 |
| **Lane phải xong** | **15:41** | **16:50** | **17:50** |
| **CHỐT CUỐI = khoá `/choi`** | **15:45** | **16:53** | **17:53** |
| Người chơi còn thấy tới | xổ ~16:34 | 16:55 | 17:55 |

Hai job ở 16:55/17:55 (`slice_recommendation`, `output_final_lab_shadow`) đã soi và xác nhận **không tính vào chốt** — chỉ ghi bảng đo lường riêng, không chạm `final_bundles`, khoá `/choi`, hay lane.

## Chốt chặn siết theo mốc mới

Hồi tố 30/07 với thước mới: mục trễ **33 → 37** — đúng kỳ vọng vì bắt thêm 3 lane MN và khoá MT lúc 16:55.

Hash 4 bảng official pre/post IDENTICAL. Rollback bằng một lệnh nạp lại crontab đã sao lưu.
