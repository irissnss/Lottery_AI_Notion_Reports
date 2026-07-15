# 🔴 MIEN NAM — Thu 04/06/2026

| | |
|---|---|
| **Dai** | Tây Ninh · An Giang · Bình Thuận |
| **Version** | `morning` |
| **Created** | 03/06 22:50 VN |
| **Data tu** | 03/06 (23 ngay lookback) |
| **Phase** | MIXED (conf: 0.45) |

---

## 🏆 DU DOAN

| | So | Score | Action | Risk |
|---|---|---|---|---|
| **Bach Thu** | **75** | 6.5/10 | ✅ RECOMMEND | MEDIUM |
| So Phu 1 | **34** | 4.0/10 | — | — |
| So Phu 2 | **14** | 6.0/10 | — | — |

### Reasoning chi tiet

**Bach Thu 75:**
- Tang 1 V10667 BH-pass: MT:DB#1:D-1 (Da Nang DB=725175 → LAST2=75), lift +8.18pp, weight 5
- Tang 2 Mined: Nguon Da Nang MT, tier READY_WITH_CAUTION, hit_rate_365=73.6%
- Tang 3 Statistical: freq=3/29 (below avg 4.1) — cold nhung multi-confirm across 2 layers
- Multi-confirm V10667+Mined → weighted_score 7.0 → giam 0.5 (freq concern) → 6.5

**So Phu 1 — 34:**
- Tang 1B MN-01: MB G7#4=34, cross-region weight 3
- Tang 3: freq=6/29 (above avg) → warm signal
- No V10667 support → lower confidence

**So Phu 2 — 14:**
- Tang 1 V10667 BH-pass: MT:DB#1:D-1 (Khanh Hoa DB=863914 → LAST2=14), lift +8.18pp
- Tang 2 Mined: co trong mined_candidates
- Tang 3: freq=2/29 — very cold → risk cao

---

## 🎲 XIEN

| Loai | Bo so | Score | Co-occur | Action |
|---|---|---|---|---|
| Xien 2 | 34-40 | 5.0 | 10.3% (3/29 ngay) | ✅ RECOMMEND |
| Xien 3 | 34-40-95 | 4.5 | 6.9% (2/29 ngay) | ✅ RECOMMEND |
| Xien 4 | 34-40-71-95 | 3.0 | <3.5% | ⛔ SKIP |

### Xien reasoning:
- 34: MN-01 cross-region (MB G7#4) + freq=6 warm
- 40: Mined candidate + freq=8 HOTTEST in MN
- 95: Mined candidate + freq=5 above avg
- Co-occur 34-40: 10.3% vs baseline ~3.2% per station → lift 3.2x
- Co-occur 34-40-95: 6.9% vs baseline ~0.6% → lift 11.5x

---

## ⚠️ CANH BAO

| Muc | Chi tiet |
|---|---|
| Non-hot day | MN T5 chi co 1 BH-pass rule — tin hieu V10667 yeu |
| Freq concern | BT=75 freq below avg (3 vs 4.1) |
| No prior data | MN T5 chua co data trong learning_matrix |
| Re-predict | Se duoc re-predict sau khi MN xo (16:35) |

---

## ✅ VERIFY — Ket qua thuc te

> ⏳ **Cho ket qua xo 16:15 ngay 04/06/2026**

### Ket qua cac dai

| Dai | DB (6 so) | Duoi DB | G8 | Duoi G8 |
|---|---|---|---|---|
| Tây Ninh | ______ | __ | __ | __ |
| An Giang | ______ | __ | __ | __ |
| Bình Thuận | ______ | __ | __ | __ |

### Kiem tra Bach Thu + So Phu

| So | Du doan | Trung? | Ghi chu |
|---|---|---|---|
| Bach Thu | 75 | ⏳ | |
| So Phu 1 | 34 | ⏳ | |
| So Phu 2 | 14 | ⏳ | |

### Kiem tra Xien (MN: check tung dai rieng)

| Loai | Bo so | ALL trung cung dai? | Ghi chu |
|---|---|---|---|
| Xien 2 | 34-40 | ⏳ | |
| Xien 3 | 34-40-95 | ⏳ | |
| Xien 4 | — | ⛔ SKIP | |

---

## 📝 BAI HOC (ghi sau verify)

> _Method nao dung/sai? Xien trung/truot? Dieu chinh gi?_
