# BÁO CÁO V10794 — TỔNG KẾT CHU KỲ LIVE 09-13/07 + FIX RACE KHÓA COMBO /choi MB

- **Ngày:** 2026-07-13 tối → 2026-07-14 sáng (giờ VN)
- **Yêu cầu owner (13/07 18:43):** "Đã hết chu kỳ live rồi em tiến hành phân tích đánh giá, đào sâu tiếp tục từ kết quả dự đoán của thời gian vừa qua, đề xuất xử lý hợp lý tiếp theo là gì em?" — 14/07 08:48 nhắc tiếp tục hoàn tất.
- **Phạm vi:** đánh giá forward K11a MB / K15 MT / selector shadow / /choi tuần 06-13/07 + verify khóa tuần mới 13-19/07. Phát hiện và fix 1 defect race khóa số /choi MB.
- **Dữ liệu:** DB sync live 2 lần (manifest `artifacts/live_sync/20260713_184528` + `20260714_085208` — sau settle qua đêm). 8 probe READ-ONLY `_v10794_cycle_probe1-8.py`.

## 1. K11a MB — challenger `MB_OUTPUT_V1` vs champion (5 ngày, 09-13/07)

| Ngày | Challenger (áp official) | Champion (shadow) |
|---|---|---|
| 09/07 | 16,74 ✗ −2.7M | 86,23 ✗ −2.7M |
| 10/07 | 86,36 · 1 nháy +2.2M | 98,65 ✗ −2.7M |
| 11/07 | 64,38 ✗ −2.7M | 98✓,65✓ đúp +7.1M |
| 12/07 | 72,17 · 1 nháy +2.2M | 35,64 · 1 nháy +2.2M |
| 13/07 | **89✓ BT WIN** +2.2M | 35,01 · 1 nháy +2.2M |
| **Tổng** | **+1.2M · BT 1/5 · ăn 3/5** | **+6.1M · BT 1/5 · ăn 3/5** |

Champion dẫn P&L **chỉ nhờ đúng 1 ngày đúp** (11/07). Hit-profile hai bên **y hệt** (ăn-ngày 3/5, BT 1/5). Ngày 13/07 challenger cho official MB **BT WIN đầu tiên** (89✓ — bắt đúng bầy 12/25 model; champion 35✗). KHÔNG chạm kill-switch (không có 5 ngày thua liên tục). **Checkpoint ngày-7: 16/07.**

## 2. K15 MT — challenger `MT_OUTPUT_V1` vs champion (4 ngày, 10-13/07)

| Ngày | Challenger | Champion |
|---|---|---|
| 10/07 | 16,85 · 1 nháy +1.3M | 16,64 ✗ −3.6M |
| 11/07 | 61✓ BT,63 −0.5M | 94,61 · 1 nháy −0.5M |
| 12/07 | 64✓ BT,10 · 2 nháy +4.4M | 43,64 · 2 nháy +4.4M |
| 13/07 | 31,97 ✗ −3.6M | 31,97 ✗ −3.6M |
| **Tổng** | **+1.6M · BT 2/4 · ăn 3/4** | **−3.3M · BT 1/4 · ăn 2/4** |

Challenger **≥ champion cả 4/4 ngày**, BT gấp đôi. **Checkpoint ngày-7: 17/07.**

## 3. Selector shadow FORWARD (5 ngày 09-13/07, settle đủ)

| Miền | SEL_BASE | SEL_DEDUP | SEL_RECENCY | Ghi chú |
|---|---|---|---|---|
| MN | −19.0M (BT 0/5) | −9.2M (BT 1/5) | −23.9M (BT 0/5) | **NGƯỢC hẳn backfill** (backfill: RECENCY +2.3M dương duy nhất) |
| MT | −13.6M (BT 2/5) | −8.7M (BT 2/5) | −3.8M (BT 2/5) | lỗ 1-số chỉ −1.9M |
| MB | +6.1M (BT 3/5) | +6.1M (BT 3/5) | +6.1M (BT 3/5) | trio > challenger K11a (+1.2M) — n=5 còn nhỏ |

Bài học: forward-test đã cứu hệ khỏi một quyết định sai — nếu tin backfill thì đã đổi bộ chọn MN và lỗ nặng. **KHÔNG đổi bộ chọn MN.** Tổng kết 14 ngày: **23/07**.

## 4. /choi tuần 06-13/07 + khóa tuần mới

- Tổng stake-adjusted theo verdict (nghỉ=0, cân nhắc=nửa): **+23.4M** — MT +16.4M (động cơ chính) · MB +7.9M · MN −1.2M.
- Khóa tuần MỚI 13-19/07 tự chọn **đúng hạn** (13/07 15:46, trước mọi cutoff):
  - MB = `MB_OUTPUT_V1 + MB_ADAPTIVE_EXPLOIT_V1` (gộp 2 — **lần đầu m1 là lane promote**)
  - MT = `MT_HYBRID_V1 + MT_STRENGTH_WEIGHTED_V52_5_2` (AE MT rớt khỏi lock theo P&L 60d)
  - MN = `MN_BT1_OFFICIAL_V1` (E5 owner ký, giữ nguyên)
- Item "verify weekly lock 13/07" của V10791: **ĐÓNG**.
- Ngày 13/07: MB CHƠI 41,31 → +2.2M ✓ · MT CHƠI 39,31 → +1.3M ✓ · MN NGHỈ (94 trượt — né đúng, đỡ −2.7M).

## 5. 🐛 DEFECT phát hiện + FIX (code change duy nhất)

**Race khóa số ngày /choi MB:** daily lock freeze 17:36 khi combo mới có leg AE (bundle 17:35) còn `MB_OUTPUT_V1` sinh 17:55 **chưa tồn tại** → 13/07 lock `[41,31]` (thuần AE) dưới nhãn combo, đáng lẽ `[89,41]` (89 = BT WIN của official). 9/10 ngày gần nhất lock MB nổ trước 17:55 → tuần trước vô hại (lock AE-đơn) nhưng **tuần này combo → hỏng hệ thống nếu không fix**. May mắn 13/07 P&L hai cặp bằng nhau (+2.2M, đều 1 nháy).

**Fix (`_v10759_money_board.py`):** mode "gộp 2 method" chỉ freeze khi **đủ cả 2 leg**, hoặc **đã qua cutoff** (leg trễ coi như bỏ — chốt record). Test replay 5 case trên COPY DB: PASS toàn bộ (17:36 thiếu m1 → hiển thị nhưng không freeze · 17:56 đủ 2 leg → freeze `89,41` đúng · qua cutoff thiếu m1 → freeze 1-leg cho record · MT `39,31` không regression · MN BT1 nguyên trạng).

**Deploy:** backup 2 đầu (`backups/v10794_pre/` + VPS `/root/backups/v10794_pre/`); restart 14/07 09:11 (ngoài cửa sổ live); health 200 · /choi 401 (auth đúng) · journal 0 lỗi; **hash 4 bảng pre/post IDENTICAL** (predictions 10006 `921eeaea` · final_bundles 409 `4d9e8098` · lottery_results 15069 `4cc74635` · model_daily_eval 9830 `3da3f94a`). Ghi chú vận hành: MB scrape-fail 18:30 (3 nguồn) hôm 13/07 **tự phục hồi 18:30:31** — row đủ 27 lô, không mất dữ liệu.

## 6. Đề xuất xử lý tiếp theo (chờ owner)

1. **K11a MB: GIỮ NGUYÊN đến 16/07** — hit-profile ngang champion, đã có BT win; khác biệt P&L chỉ là 1 ngày đúp.
2. **K15 MT: GIỮ, đang thắng tuyệt đối** — chốt 17/07.
3. **MN: không đổi gì** — selector forward âm sâu xác nhận vote hiện tại đúng.
4. **CP-L6 (lean roster, hạn 14/07): đề xuất DỜI sang 19/07** gộp cùng CP-R4 — không cắt model giữa cửa sổ đo K11a/K15 (selector dùng top-8/10 strength kể cả shadow = cắt lúc này là trộn biến). Anh chưa OK CP-L6, em đang chờ quyết định: (a) dời 19/07 · (b) làm ngay · (c) huỷ.
5. **23/07: tổng kết selector 14 ngày** — nếu trio MB vẫn > official mới, trình phương án đổi bộ chọn MB.
6. **41 bảng chết CP-L3** vẫn chờ owner OK drop.

## 7. Governance

- CHANGELOG V10794 + SSOT block + `FU-V10794-CYCLE-REVIEW` (DEPLOYED_PENDING_LIVE_VERIFY — verify 14/07 tối ~17:56 lock MB ghi đủ 2 leg).
- `docs/AUTOMATION_STATE.json` seq 255 + `AUTOMATION_HISTORY.jsonl` append.
- Roadmap LEAN_HARVEST: CP-L6 → AWAITING_OWNER_OK (đề xuất dời 19/07).
- Hard safety: official `/du-doan` untouched; zero shadow backfill; runtime artifacts không vào Git.
