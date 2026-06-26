# V10753.3 — Song-thủ CÓ ĐIỀU KIỆN (động) + tinh gọn UI

**Thời điểm:** 2026-06-26T20:38:00+07:00 · **Owner:** duyệt khai thác số phụ + "hệ thống quá rối rắm, nhiều cảnh báo, nhiều thông tin quá → tinh gọn".

## Khai thác số phụ (backtest 119 ngày)

- Đánh SP **mỗi ngày** thì LỖ (giá trị biên: MN −81.8M, MB −13.7M; chỉ MT +38.8M).
- **Song-thủ CÓ ĐIỀU KIỆN** (chỉ đánh con thứ 2 khi nhiều model đồng thuận) thắng rõ, xu hướng đơn điệu theo ngưỡng vote:
  - **MB: SP ≥5 model → +37.3M (VƯỢT chơi 1 số +30.4M)**
  - **MT: SP ≥3 model → +108M** (> song-thủ thường +102M)
  - **MN: không ngưỡng nào thắng 1 số → luôn 1 số**
- SP cứu ngày BT-miss: MN 31% · MT 40% · MB 22% — nhưng đánh đại không bù chi phí → phải có điều kiện.

## Đã triển khai (admin-only, KHÔNG đổi số dự đoán)

- **Panel động "🎯 HÔM NAY NÊN: [1 SỐ / SONG-THỦ] → số"** trên /du-doan: tự đọc độ đồng thuận SP hôm nay rồi quyết (ngưỡng MN none / MT 3 / MB 5).
- **Tinh gọn UI:** gộp 3 badge khuyến nghị chồng nhau → 1 panel duy nhất; **ẩn 2 badge trùng lặp** (cường độ đài + sức khỏe đài); bảng kỹ thuật admin vốn đã thu gọn trong `<details>`.

Preview 26/06: MN→1 SỐ 53 · MT→SONG-THỦ 80-91 (SP 5 model) · MB→SONG-THỦ 18-30 (SP 5 model).

## Verify

diff main +50/-9, du-doan +19/-10; compile OK; health 200; admin endpoint unauth=401; /du-doan=200; **4 bảng official IDENTICAL trong deploy** (không regen). Rollback: trả endpoint về tĩnh + bỏ ẩn 2 badge.
