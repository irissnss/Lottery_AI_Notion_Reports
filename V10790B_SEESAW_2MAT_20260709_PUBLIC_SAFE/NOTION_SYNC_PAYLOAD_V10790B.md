# V10790-B — Bập bênh 2 mặt (seesaw): xác minh quan sát owner + panel ⚖ /monitoring (09/07 tối muộn)

**Owner 18:59:** "MB nay lại về? Model trật hết mà /choi trúng; hôm qua model ok mà /choi trượt; 07/07 cũng thế. Có cách nào khống chế cân bằng ổn áp hơn không? Dựa live data tìm được cơ chế nào không?"

## Xác minh — owner ĐÚNG 100%, bập bênh CÓ THẬT (3 probe READ-ONLY)

- MB 3 ngày: 07/07 bể 76% model trúng → /choi AE [16,59]✗ · 08/07 bể 60% → AE [59]✗ · 09/07 bể chỉ 4% → **AE [13,64]✓VỀ** (official 16✗).
- 60d MB (n=36): ngày bể-TRẮNG (<10% model trúng) **AE 67% vs vote-OUTPUT_V1 8%**; ngày bể-NÓNG (≥30%) **vote 86% vs AE 29%** — cặp bù trừ giáo khoa.
- Union ≥1 mặt trúng: **MN 88% / MT 82% / MB 78%**.

## Vì sao KHÔNG làm switch theo ngày

- Regime không tự tương quan (hôm qua TRẮNG → hôm nay TRẮNG chỉ 7/18 ≈ base rate).
- Mọi rule switch causal đã backtest (theo share hôm qua 49%, follow-streak 37%, anti-herd 44%, overlap 42%) đều ≤ always-AE 47% → switch = overfit.
- Số "đồng thuận" 2 mặt cùng chọn KHÔNG mạnh hơn: MT 3/11=27%, MB 0/3.

## Cơ chế ổn áp chính thức (đã ở đúng cấu hình từ hôm nay)

- **Official = mặt VOTE**: K11a MB (live 09/07) + K15 MT (live 10/07) — bắt ngày "thuận bể" (86% khi bể nóng).
- **/choi = mặt ECHO** (AE lock tuần) — bắt ngày "lệch kịch bản" (67% khi bể trắng).
- Panel mới **⚖ BẬP BÊNH 2 MẶT** trên `/monitoring`: bucket TRẮNG/VỪA/NÓNG, hit từng mặt, union, ngày mới nhất — giám sát union giữ ≥75%.

## Deploy

- 19:0x, restart 1 lần guard SAFE; sandbox PASS (số khớp probe); smoke health 200 / admin 401; hash 4 bảng pre/post IDENTICAL. DIAGNOSTIC-ONLY — không đổi số official/lane//choi.

**Chi tiết đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10790B_SEESAW_2MAT_20260709_PUBLIC_SAFE/`
