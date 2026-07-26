# ADDENDUM V10858 (26/07 12:47→13:0x) — FIX MOBILE P&L/ACCURACY (regression V10856) + MORNING CHECK CN

Owner: "đầu ngày kiểm tra tổng lực + giao diện P&L và độ chính xác chán quá, chữ 1 nơi card 1 nơi tùm lum trên mobile."

## Root cause (lỗi của phiên V10856 — nhận và sửa)

- `overflow-wrap: anywhere` làm **min-content co về ~1 ký tự** → mobile cột grid/flex bị bóp vụn + chữ gãy giữa từ = đúng "gián chữ nghĩa, card 1 nơi" (P&L có `v2-body`; accuracy dính vì nav-injector runtime thêm class `v2-body`).
- 2 rule quá tay `.card{flex-column}` + `.row{dồn phải}` đè layout riêng pnl/du-doan/index.
- Riêng accuracy: nút ☰ (nav-injector, fixed góc trái) **đè lên tiêu đề** trên mobile.

## Fix (deploy md5 14/14, marker đo lường nguyên)

- `anywhere` → **`break-word`** (không đổi min-content; chỉ gãy token thật dài) · GỠ `.card`/`.row` rules · accuracy `top-bar padding-left 60px ≤900px` (☰ hết đè).
- Sự cố nhỏ trong lúc sửa: lần re-inline đầu chết giữa chừng vì assert quá gắt (rule `anywhere` RIÊNG có từ trước của monitoring/du-doan-test — scoped hẹp, không phải của theme) → live tạm nửa mới nửa cũ ~1 phút, chạy lại đủ 14/14.

## Morning check CN 26/07 — sạch

- Self-check **11/11** (model 0.5d · **optimizer 0.4d — marker 03:14 verified**) · journal 0 · quick_check ok · contract PASS.
- Closeout 25/07: M2s MB 05✓ · **rule-cond B MN 04✓ trong khi official trượt (điều kiện cứu MN lần 2 liên tiếp)** + MB 05✓ · what-if MB day-1 thuận. **M2s−M0 forward 12/21 vs 10/21 = +9.5pp — đọc promote 28/07.**
- Sáng nay: MN 15 official 0-empty (gpt-5-mini/gpt-5.4 hồi ở MN; MT verify 16:4x) · bundle BT **50** [50,14] @04:17 · /choi MN khoá [50] (CN chơi lại sau T7 đúng lock) · V67 target MB 52/65/30/27 + MT 78/17/74 · trace 26/26 PB-18.1.

Git `f7fb84d`. Lịch: 28/07 ĐỌC LỚN (M2s promote + PB-18.1 + rule-cond + lean); ~01/08 what-if MB.
