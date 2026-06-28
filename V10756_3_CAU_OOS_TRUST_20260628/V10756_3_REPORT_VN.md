# V10756.3 — Trọng số OOS walk-forward HONEST + bác bỏ chu kỳ tuần (2026-06-28)

> SHADOW thuần, ZERO official impact. Hash-guard 4 bảng official IDENTICAL.

## Bối cảnh
Owner phản biện đúng: cầu D-1 nguồn có sẵn; cầu D xổ theo thứ tự MN<MT<MB → **backtest lịch sử KHÔNG leak**, KHÔNG cần chờ live mới ra trọng số. + hỏi chu kỳ tuần W-1/W-4 và rule có lặp không.

## 1. Trọng số OOS walk-forward (honest, không leak)
Mỗi cutoff hằng tuần: mine top-5 trên 240 ngày TRƯỚC, chấm 7 ngày SAU; gộp 84 ngày → oos_rate per (miền, rank). Lưu bảng `cau_oos`. `_trust` ưu tiên forward live, chưa đủ thì dùng OOS lịch sử (≥40 mẫu) — bỏ "đang đo" mù.

| Miền | OOS rank1-3 | Nền | Lift |
|---|---|---|---|
| MN | 46.7% (n=255) | 43.1% | **+3.6pp** (rank3 +8.7pp 🟢) |
| MT | 36.1% (n=255) | 35.2% | +0.9pp (~hòa) |
| MB | 21.6% (n=255) | 23.7% | −2.1pp (🔴) |

- Thứ hạng in-sample KHÔNG giữ OOS (MB rank4-5 > rank1-3) → con số rank nhiễu.
- Trọng số live: MN #3 🟢 NÊN; phần lớn MT 🟡; MB toàn 🔴.

## 2. Bác bỏ chu kỳ tuần (W-1/W-4)
- **Weekly echo** (lô cùng thứ N tuần trước về lại) W-1..W-5 = +0.0→0.6pp ≈ nền → **KHÔNG có chu kỳ tuần**. Đừng đoán theo "tuần trước".
- **Rule churn**: top-3/slot xoay **~50%/tuần**; tuần 1 vs tuần 6 chỉ trùng **22%** → **KHÔNG lặp lại, không thành chu kỳ**.
- ⇒ Cầu CỤ THỂ phần lớn là nhiễu; chỉ **HỆ THỐNG** (chọn top mỗi tuần theo miền) mới có edge nhẹ, và chỉ rõ ở **MN**.

## 3. Kết luận
- Có thể gán trọng số trung thực NGAY từ lịch sử (đúng như owner nói).
- MN cầu có edge thật nhẹ (+3.6pp OOS); MT trung tính; MB nên bỏ.
- Không khai thác được chu kỳ tuần.

private 0bfc6e2.
