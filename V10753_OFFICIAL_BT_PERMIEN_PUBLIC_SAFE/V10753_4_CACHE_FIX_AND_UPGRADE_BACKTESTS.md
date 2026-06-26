# V10753.4 — Vá cache /du-doan + backtest nâng cấp (a)(b): đều KHÔNG hơn

**Thời điểm:** 2026-06-26T21:04:00+07:00 · **Bối cảnh:** owner báo "không thấy panel" + duyệt (a) gộp model eval vào official, (b) khôi phục strength tensor.

## Vá cache (gốc rễ "không thấy panel")

`/du-doan` thiếu header no-cache → trình duyệt cache HTML cũ (file trên VPS đã đúng V10753.3). Đã thêm `Cache-Control: no-store/no-cache/must-revalidate` + Pragma + Expires; verify GET nội bộ + ngoài `https://xs.io.vn/du-doan` đều trả no-store → hết kẹt cache.

## (a) Gộp model eval vào official — backtest 119 ngày: TỆ HƠN cả 3 miền

| Miền | LIVE | OE-only | +ALL eval | +eval mạnh (BT≥40%) |
|---|---|---|---|---|
| MN | +45.6M | +1.5M | −3.4M | −13.2M |
| MT | +63.3M | +58.4M | +38.8M | +38.8M |
| MB | +30.4M | +1.1M | −13.7M | +6.0M |

→ Nhiều model = nhiều nhiễu, loãng tín hiệu OE mạnh (khớp bài học "ít model thắng"). **KHÔNG gộp.** Model eval = chi phí token monitoring, không đóng góp official.

## (b) Khôi phục strength tensor

Tensor stale từ 05/05, nhưng bộ chọn đang chạy KHÔNG dùng tensor → khôi phục chỉ là diagnostic, không tăng P&L. Hạ ưu tiên.

## Kết luận trung thực

Đã thử hết hướng nâng cấp DỰ ĐOÁN (follow đám đông / gộp eval / tensor) — **tất cả không hơn bộ chọn hiện tại**. Hệ thống đã tối ưu gần hết phần ăn được (+45M/+102M/+30M trên 119 ngày). Phần edge còn lại là **quản lý vốn + song-thủ có điều kiện** (đã làm), không phải dự đoán thêm. Ngày BT trật cả 3 miền hôm nay = **xui 1 ngày**, không phải lỗi bỏ sót có hệ thống.
