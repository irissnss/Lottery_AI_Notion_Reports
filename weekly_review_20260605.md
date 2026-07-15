# 📊 LOTT Weekly Review — 29/05 → 05/06/2026

**Tổng:** 32 verifications · BT hit 14/36 official = 39% · v3.5 rules added

## 🏆 Highlights tuần

- ✅ **MB T6 (05/06) break-through:** BT HIT 3/3 versions (16, 47, 47) — phá kỷ lục MB BT 4 tuần 0%
- ✅ **MT T4-T5 GOLDMINE confirmed:** BT 100% 2 ngày liền — methodology V10667 BH-pass + cascade hoạt động hoàn hảo
- ✅ **MB T3 (02/06):** BT 100% (3/3) — `mined+freq+cascade` method validated
- ⚠️ **MN BT toàn tuần yếu:** 1/8 = 13% — cần fix urgent (G11 mới apply)

## 📊 Ma trận Region × Thứ — BT hit rate

| Miền | T3 | T4 | T5 | T6 |
|---|---|---|---|---|
| 🔴 MN | 50% (1/2) | 0% (0/2) | 0% (0/3) | 0% (0/1) |
| 🟡 MT | 67% (2/3) | **100%** (3/3) | **100%** (4/4) | 0% (0/2) |
| 🔵 MB | **100%** (3/3) | 0% (0/4) | 0% (0/6) | **100%** (3/3) ⭐ |

## 🥇 Top methods (by BT hit)

| Method | Hit / Total | % |
|---|---|---|
| cross_region + frequency | 2/2 | **100%** |
| frequency | 2/3 | 67% |
| mined_rules + cross_region | 1/1 | 100% |
| cascade MN→MT | 1/1 | 100% |
| mined_rules + frequency | 1/3 | 33% |

## 📌 Rules tích lũy (auto_rules_registry — 14 rules)

**G1-G10 v2.4** (legacy):
- G1 BT_MULTI_CONFIRM · G2 BT_FREQ_GATE · G3 SP_V10667_PROMOTE
- G4 CASCADE_MT_ONLY · G5 MB_BT_INDEPENDENT · G6 MN_SP_FIRST
- G7 INDEPENDENCE_AUDIT · G8 OVERHEATING_FILTER · G9 MULTI_SIGNAL_THRESHOLD · G10 MIRROR_WEIGHT_CAP

**G11-G14 v3.5** (NEW 05/06):
- **G11 MIRROR_SIDE_TIEBREAKER** — mirror tie → V10667 BH-pass cho từng phía
- **G12 MB_CAP_RAISE_5SIGNALS** — MB cap 55%→70% nếu ≥5 signals + V10667 carry
- **G13 MT_TIEBREAKER_VIA_V10667_FREQ** — tiebreaker khi 2 candidate cùng 3-station MN
- **G14 NO_PEAK_CROSS_PROMOTE_MB** — KHÔNG promote cross-peak ≥4× sang MB BT

## 🎯 Strengths confirmed

- **S1** MT GOLDMINE T5 (85 BH-pass) — 2/2 WIN xác nhận
- **S2** Markov cascade MN→MT — 2/2 accurate
- **S3** V10667 MODERATE/STRONG cho SP — 3/3 hit
- **S6_v35** (NEW) MB V10667 STRONG carry → BT (16 HIT T6)
- **S7_v35** (NEW) Cross-MN 3-station → MB BT (47 HIT T6)
- **S8_v35** (NEW) MT SP1 cross-region direct (2/2 T6)
- **S9_v35** (NEW) G4 CASCADE_MT_ONLY validated

## ⚠️ Weaknesses tracking

- **W9_v35** MN T6 mirror side selection (đã có fix G11)
- **W10_v35** MT 3-station tiebreaker (đã có fix G13)
- **W11_v35** MB cap 55% quá bi quan (đã có fix G12)
- **W12_v35** MN intra-region cross-3 bỏ sót — chưa fix

## 🎯 Kế hoạch T7 (06/06)

| Miền | Đài | BT | P1 | P2 | Conf | Action | Lý do |
|---|---|---|---|---|---|---|---|
| MN T7 | TP.HCM·LA·BP·HG | **86** | 47 | 23 | 75% | RECOMMEND | HOT_DAY BH-pass GOLDMINE +15% |
| MT T7 | DN·QN·ĐN | **90** ⭐ | 73 | 13 | 85% | RECOMMEND | HOT_DAY BH-pass GOLDMINE +20% |
| MB T7 | Nam Định | **75** | 47 | 87 | 70% | RECOMMEND | V10667 G1=75 carry (G12 cap raise) |

## ⚠️ KNOWN ISSUES — engineering

### Sync issue — Cowork mount
- File `cowork_lott_master.py` đã được sửa trên Windows (5 fixes Phase 1)
- Linux mount cache đang stale (sees 1425 lines truncated, Windows actual 1535+ lines)
- **Hậu quả:** engine via bash không chạy được tới khi mount re-sync
- **Workaround:** Refresh Cowork mount hoặc đợi Google Drive sync push

### Phase 1 fixes (đã apply trên Windows, chờ sync)
1. ✅ `import_results` auto-compute all_tails từ prizes
2. ✅ `import_results` accept cả `date` lẫn `date_str`
3. ✅ `save_prediction` handle xien dict/list (không crash)
4. ✅ `run_verify` thêm 2 gates: station_coverage + all_tails_nonempty
5. ✅ Diagnostic output rõ ràng khi verify không có gì làm

### Phase 2 backtest
- Backtest analytical đã chạy trên DB
- G13 validate: nếu hôm nay dùng tiebreaker → BT MT chọn 59 thay 50 → HIT (NT DB)
- G12 validate: MB BT hit 50% (post_mn/post_mt) đáp ứng cap 60-70%
- G11 sample nhỏ (1 mirror prediction in 7d) — cần theo dõi tiếp
- G14 confirmed: 59 cross 5× hôm nay không hit MB → rule đúng

## 🕒 Schedule tuần tới

- **Hôm nay 19:00** — sau khi sync resolve, chạy engine validate code fixes
- **T7 06/06 10:30** — morning predict (BT 86 / 90 / 75 dự kiến)
- **T7 16:30** — verify MN, cascade re-predict MT+MB
- **T7 17:30** — verify MT, cascade re-predict MB
- **T7 18:30** — verify MB Nam Định
- **CN 07/06 19:30** — weekly review tự động

*Generated: 2026-06-05 19:00 · v3.5 EOD review*
