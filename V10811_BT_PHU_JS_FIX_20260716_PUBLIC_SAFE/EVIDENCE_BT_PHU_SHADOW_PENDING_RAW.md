# EVIDENCE RAW V10811 — BT vs SỐ PHỤ + SHADOW DAY-1 + PENDING VERIFY (16/07/2026)

Nguồn: probe read-only trên VPS (`_v10811_bt_phu_probe.py`, `_v10811_promote_scoreboard.py`, `_v10811_cron_verify.py`, `_v10811_pending2.py`). Chấm bao-lô toàn miền.

## A. HÔM NAY 16/07 — BT vs PHỤ TỪNG MODEL

### MN (45 đuôi về) — official BT=72 WIN, lô2 [72,96] WIN
- TỔNG 26 model: BT trúng=14, phụ trúng=13, cả hai=6
- AI-OFF n=7: BT=6 phụ=5 · AI-SHD n=11: BT=5 phụ=5 · ML n=7: BT=2 phụ=2 · COMBO n=1: BT=1 phụ=1
- BT trúng: claude-opus(72+17), claude-sonnet(72+17), combo-super(72+17), gemini-flash(96+72), gemini-pro(96+73), gemini-3.5-flash(72+17), glm-5.1(72), gpt-5-mini(96), gpt-5.4(96), grok(72), kimi(72), lstm(45), qwen3.7(72), smart-ensemble(45)
- Chỉ phụ: deepseek-reasoner(72; BT 02 trượt), deepseek-v4-pro-real(72), gemma-4-31b(17), glm-5.2(17), gpt-5.5(72), meta-learning(19), random-forest(04)

### MT (41 đuôi về) — official BT=40 LOSE cả bộ
- TỔNG 25 model: BT trúng=3, phụ trúng=12, cả hai=0
- AI-OFF n=7: BT=0 phụ=2 · AI-SHD n=10: BT=2 phụ=5 · ML n=7: BT=0 phụ=5 · COMBO n=1: BT=1 phụ=0
- BT trúng: combo-super(72), deepseek-v4-pro-real(72), qwen3.7-max(54)
- Chỉ phụ (12): opus(82), gemini-3.5-flash(19), gemma(72), glm-5.1(16), glm-5.2(72), gpt-5.4(34), gpt-oss(72), meta-learning(72), random-forest(72), smart-ensemble(89), smart-ml(89), xgboost(89)

### MB (22 đuôi về) — official BT=69 LOSE cả bộ
- TỔNG 25 model: BT trúng=3, phụ trúng=6, cả hai=1
- AI-OFF n=7: BT=0 phụ=0 (TRẮNG) · AI-SHD n=10: BT=3 phụ=4 · ML n=7: BT=0 phụ=2
- BT trúng: gemini-3.5-flash(16), glm-5.2(16), qwen3-max(46+16)
- Chỉ phụ: deepseek-v4-pro-real(16), gemma(16), grok(16), lstm(63), meta-learning(56)

## B. TREND 14 NGÀY (02–15/07, model_daily_eval)

```
MN  AI-OFF n=98  BT 44 (44.9%) | PHỤ 49 (50.0%)
MN  AI-SHD n=136 BT 70 (51.5%) | PHỤ 58 (42.6%)
MN  ML     n=98  BT 44 (44.9%) | PHỤ 43 (43.9%)
MN  COMBO  n=14  BT  5 (35.7%) | PHỤ  8 (57.1%)
MT  AI-OFF n=98  BT 36 (36.7%) | PHỤ 30 (30.6%)
MT  AI-SHD n=137 BT 40 (29.2%) | PHỤ 52 (38.0%)   << nghiêng PHỤ
MT  ML     n=98  BT 28 (28.6%) | PHỤ 31 (31.6%)   << nghiêng PHỤ
MT  COMBO  n=14  BT  5 (35.7%) | PHỤ  6 (42.9%)
MB  AI-OFF n=98  BT 28 (28.6%) | PHỤ 28 (28.6%)
MB  AI-SHD n=127 BT 37 (29.1%) | PHỤ 27 (21.3%)   << nghiêng BT (ngược MT)
MB  ML     n=98  BT 16 (16.3%) | PHỤ 17 (17.3%)
MB  COMBO  n=14  BT  6 (42.9%) | PHỤ  4 (28.6%)
```

## C. SHADOW A/B V10809 DAY-1 (16/07) — A=production, B=addendum

```
MN  opus     A [72,17] hit 72,17 | B [17,29] hit 17
MN  deepseek A [02,72] hit 72    | B [02,57] -
MN  gem-fl   A [96,72] hit cả 2  | B [96,17] hit cả 2
MN  mini     A [96,57] hit 96    | B [96,02] hit 96
MN  qwen     A [72,57] hit 72    | B [57,29] -
MT  opus     A [40,82] hit 82    | B [34,93] hit CẢ ĐÔI
MT  deepseek A [57,32] -         | B [57,00] hit 00
MT  gem-fl   A [05,26] -         | B [57,40] -
MT  mini     A [57,32] -         | B [57,82] hit 82
MT  qwen     A [54,40] hit 54    | B [00,00] hit 00 (PICK TRÙNG — SE3)
MB  opus     A [69,57] -         | B [69,57] -
MB  deepseek A [69,96] -         | B [57,69] -
MB  gem-fl   A [75,69] -         | B [32,57] -
MB  mini     A [72,32] -         | B [46,64] hit 46
MB  qwen     A [75,32] -         | B [57,69] -
Scorer 19:15: "updated 15 rows | B any-hit 8 vs PROD 7"  (MN 3-5, MT 4-2, MB 1-0)
```

## D. K11a MB / K15 MT PROMOTE — CHAMPION vs CHALLENGER (chấm bao-lô)

```
K11a MB (8 ngày applied 09-16/07):
 09/07 champ 86 L | chal 16 L
 10/07 champ 98 L | chal 86 L (lô2 chal W)
 11/07 champ 98 W | chal 64 L   << champion đúng, promote làm hỏng
 12/07 champ 35 L | chal 72 L (lô2 cả 2 W)
 13/07 champ 35 L | chal 89 W   << promote CỨU
 14/07 champ 67 L | chal 51 L
 15/07 champ 57 W | chal 64 L   << champion đúng, promote làm hỏng
 16/07 champ 16 W | chal 69 L   << champion đúng, promote làm hỏng
 TỔNG: champion BT 3/8, lô2 5/8 | official-sau-promote BT 1/8, lô2 4/8
K15 MT (7 ngày applied 10-16/07):
 TỔNG: champion BT 1/7, lô2 2/7 | official-sau-promote BT 2/7, lô2 3/7 (promote nhỉnh)
```

## E. PENDING VERIFY 16/07

```
[T10_CHOT] 15:45 MN BT=72 v2 · 16:54 MT BT=40 v2 · 17:54 MB BT=69 v2
bundle created: MN 04:18 / MT 16:44 / MB 17:35 · model_count 15/13/15
watchdog t10 alert giả: 0 (kỳ vọng 0 sau vá V10799)
budget_catchup MB: "selected=20 (bundles đã có từ lane khác, chỉ bù C16+ABS)" → C16 CLOSED
cron tối: 19:05 ml-mark-ab +8 row · 19:10 chase-bias +3 row · 19:15 shadow scorer 15/15 scored
self-check: 10/11 PASS (FAIL check-3 retrain_OK_in_8d — bệnh cũ, chờ CN 19/07)
MRE 20:15 theo lịch (0 row lúc 18:47 = đúng nhịp)
```

## F. BUG /monitoring — BẰNG CHỨNG

```
node --check inline script (4578 dòng):
  TRƯỚC FIX: SyntaxError: Identifier 'SS' has already been declared (js dòng 2710 = html L5094)
  L5029: const SS = ((data.signal_supply || {})[rg]) || null;   (V10787-F, 08/07)
  L5094: const SS = ((data.seesaw || {})[rg]) || null;          (V10790-B, 09/07 — thủ phạm)
  SAU FIX (SS→SW): script#0 OK
VPS grep -c "const SS" monitoring.html: 1
Deploy: restart active · health 200 · admin anon 401
Hash 4 bảng PRE=POST IDENTICAL: predictions 10200/d2732c81 · final_bundles 417/761958a3 · lottery_results 15088/b43f6694 · model_daily_eval 9986/aaa91dc6
View bt_phu live: MN {n:390, bt:184, phu:179, phu_only:103} · MT {n:390, bt:119, phu:140, phu_only:90} · MB {n:380, bt:92, phu:83, phu_only:52}
```
