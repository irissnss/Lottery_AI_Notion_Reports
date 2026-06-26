# V10753.5 — CONFIDENCE GATE: NÊN CHƠI / CÂN NHẮC / NÊN BỎ (khai thác mới)

**Thời điểm:** 2026-06-26T21:32:00+07:00 · **Owner:** "không còn khai thác nào tốt hơn sao?" + muốn phân tích MT/MB.

## MT & MB hôm nay (26/06)
- MT: đề 73, BT 80 trật, SP 91 trật. 7/28 model trúng rải rác (69/90/03/57/16). Đề không ai bắt.
- MB: đề 04, BT 18 trật, SP 30 trật. `45` có 3 model (gpt-5.4, lstm, qwen3.6-plus) nhưng official lấy 18. Đề không ai bắt.
→ Cả 3 miền bad-day đồng loạt + đề không đoán nổi = xui.

## Khai thác MỚI: chọn ngày theo độ ĐỒNG THUẬN của BT (staking, robust 2 nửa)

| Miền | YẾU (<3 vote) | TB (3-4 vote) | MẠNH (≥5 vote) |
|---|---|---|---|
| MN | (1d) | **70% · +56.9M** | 47% · **−13.5M** (bẫy hội tụ) |
| MT | 12% · **−11.3M** | +19.2M | **+55.4M** |
| MB | 14% · **−4.5M** | **+27.4M** | +7.5M |

Verify robustness (2 nửa): MT/MB ngày YẾU âm ở cả 2 nửa; MN TB ~70% vs MẠNH ~47% net-âm cả 2 nửa. **Cả 2 phát hiện ROBUST.**

**2 quy tắc:**
1. **BT <3 vote → NÊN BỎ/đánh nhẹ** (MT/MB lịch sử âm; bỏ-yếu MT +11.3M, MB +4.6M).
2. **MN ≥5 vote = BẪY HỘI TỤ** (~47%, kéo lỗ) → CÂN NHẮC; vùng 3-4 vote ~70% mới là vùng vàng.

## Đã triển khai (admin-only, KHÔNG đổi số dự đoán)
Panel /du-doan hiện verdict **✅ NÊN CHƠI / ⚠️ CÂN NHẮC / ⛔ NÊN BỎ** + lý do, theo độ đồng thuận BT hôm nay.
Preview 26/06: MN ⚠️ CÂN NHẮC (BT 5 vote bẫy hội tụ — 53 đã trật) · MT ✅ song-thủ 80-91 · MB ✅ song-thủ 18-30.

Verify: compile OK, health 200, admin endpoint 401, /du-doan 200, 4 bảng official IDENTICAL. Rollback sẵn.

## Ghi chú: các hướng KHÔNG hiệu quả (đã loại)
Follow đám đông / gộp model eval vào official / khôi phục tensor — backtest đều KHÔNG hơn bộ chọn hiện tại. Phần dự đoán đã tối ưu gần hết; edge thật nằm ở **staking (gate này) + song-thủ có điều kiện**.
