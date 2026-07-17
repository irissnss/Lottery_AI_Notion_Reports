# CONVERSATION CONTEXT — V10817 (2026-07-17 20:30)

## Owner message (verbatim)

> "để nâng tỷ lệ trên nền em phải phối ghép điều kiện nữa mới được anh nghĩ vậy? ví dụ như số đảo đó có xổ ở miền trước như miền nam hoặc miền trung đặt biệt là rơi vào các giải đáng chú ý dùng để soi cầu đó em, hoặc số đảo đó nó nằm trong tóp số nóng lạnh rơi hoặc gan gì đó phối các điều kiện vào nữa để có thể nâng tỷ lệ cao lên và loại bỏ thêm các % ngoài nền ah em. Xem kỹ dùm anh. Rules và partern chắc chắn có lý của nó nhưng thiếu điều kiện em thử bổ sung thêm các điều kiện vào xem có tăng tỷ lệ cao hơn không nào em?"

## Bối cảnh

- Tiếp nối V10816 cùng tối (owner flag rule GĐB MB đảo 2 số đầu → lô D+1, ví dụ 16/07 GĐB 96763 → 69 về 17/07; backtest 6.5 năm không edge toàn kỳ 24.2% vs 23.8% nhưng 30d cuối 40% = trần lịch sử; panel 🔄 forward-proof đã live 20:1x).
- Owner đề xuất đúng phương pháp conditional filtering: phối điều kiện phụ để nâng hit-rate trên nền và loại nhiễu.

## Kết quả phiên

- Test 31 điều kiện (4 lớp: miền-trước ngày D / soi-cùng-ngày D+1 / nóng-lạnh-rơi-gan MB / combo) trên 2331 cặp; top E2 (lô MT ngày D ∧ gan 3-9) 30.7% +6.5pp z=+2.69 nhưng placebo 2 lớp cho thấy nằm trong nhiễu chọn-lọc (median best-z +2.23 trên 20 biến thể, owner-variant hạng 3/20).
- A6 (ĐB/G1/G7/G8 MT ngày D) 28.4% ổn 2 nửa = ứng viên bền nhất; MN ngày D hơi âm; soi-cùng-ngày = nền.
- Deploy bảng 🧩 PHỐI ĐIỀU KIỆN + tín-hiệu-tối-mai vào panel; forward đo cùng rule gốc; không vào official.
