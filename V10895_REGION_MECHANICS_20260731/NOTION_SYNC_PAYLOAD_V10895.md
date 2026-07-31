# V10895 — `/nghiem-thu` trống + ba miền ba cơ chế dự đoán khác nhau

**31/07/2026** · commit `a2a3bbd` · hash 4 bảng IDENTICAL

## Vì sao `/nghiem-thu` trống
Hai nguyên nhân chồng nhau:
1. Cron 04:25/04:35 MN **mới thêm lúc 11h sáng nay** nên chưa từng chạy — log sửa lần cuối 30/07 21:16. Số MN hôm nay do chạy tay 09:25.
2. `_today_cards` `continue` qua miền chưa có số → khối "Hôm nay — 3 miền" **chỉ hiện 1 miền**, không phân biệt được hỏng với chưa tới giờ. Khối lại nằm dưới bảng đối chứng 25 dòng.

Đã sửa: luôn đủ 3 miền, miền chưa tới giờ hiện thẻ nét đứt "Có số lúc 16:44 · final 16:53", tiêu đề đếm "1/3 đã có số", khối hôm nay lên đầu trang.

## Ba miền ba cơ chế
- **MN**: số 04:00–04:19 (15 model) là **bản cuối, không bao giờ re-predict**. Không nạp same-day vì xổ đầu tiên.
- **MT**: số ML 04:00 **giữ nguyên cả ngày** — V10766 đo re-predict là **có hại** (bản-sau +1,6tr vs bản-trước +16,3tr/45 ngày). Same-day chỉ vào qua chuỗi AI chiều 16:35–16:43.
- **MB**: số ML 04:00 **bị XOÁ** (`DELETE FROM predictions`), làm lại 17:30 `rerun_post_mt` với MN+MT cùng ngày. Đo 12 ngày chỉ 31/07 còn `auto_daily` vì MT chưa xổ.

## Điều kiện re-predict
MN cào xong → chỉ MB · MT cào xong → chỉ MB · MB cào xong → không gọi. Cổng verify chỉ chạy khi bộ đài ĐỦ, thiếu thì hoãn sang lượt cào lại T+20p (`force_reverify=True`); cổng chỉ hoãn verify, re-predict và AI vẫn chạy.

## Bẫy thời gian
`training_history` lưu **giờ UTC**: ghi `25/07 19:02` nhưng `lstm_MN.pt` đổi `26/07 02:01` — lệch 7 tiếng. Retrain thật chạy **CN 02:00 giờ VN**. Kiểm 12 lượt liên tiếp đều khớp.

## MN sau 5h sáng
Đo: **không việc nào chạy sau 04:19 mà MN đọc** — rule ranker 04:40 không ghi bảng nào; champion selector 06:00 chỉ ghi bảng shadow; retrain guard 06:30 chỉ ghi log. Retrain CN 02:00, optimizer CN 03:00, đào rule T2 00:30, mn_ai_limit 03:50 đều xong trước 04:00.

Nên về dữ liệu dời không thêm gì, nhưng nguyên tắc vẫn đúng về an toàn vận hành. **Đã dời lane Nghiệm Thu MN 04:25→05:05 và 04:35→05:15.** Chuỗi dự đoán MN chính giữ nguyên — chờ owner quyết.

## Tài liệu chống quên
`docs/CO_CHE_DU_DOAN_TUNG_MIEN.md` — bảng đối chiếu 3 miền, re-predict, same-day, mốc học tập từng giờ, bẫy UTC, thủ tục bắt buộc khi thêm/đổi luồng.

## Xác minh
Hash 4 bảng IDENTICAL · `/api/health` 200 · `/du-doan` 200 · `/nghiem-thu` 401 · md5 KHỚP 6/6 dấu hiệu · Playwright 390/1440px sạch · chạy thử lane MN trả `ĐÃ CHỐT TRƯỚC ĐÓ · 09`.

Rollback: `crontab .local_backup_v10895_crontab_20260731_141740.txt`

Báo cáo đầy đủ: `V10895_REGION_MECHANICS_20260731/REPORT_V10895.md`
