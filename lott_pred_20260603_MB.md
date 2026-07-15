# 🔵 MIEN BAC — T4 03/06/2026

| | |
|---|---|
| **Dai** | Bắc Ninh |
| **Version** | `post_mb_final` (re-predict post_mt: SP1 14→54, SP2 55→52, Xien3 87-54-67→87-54-14) |
| **Created** | 03/06 16:45 VN |
| **Data tu** | 03/06 (22 ngay lookback + MN fresh data) |
| **Phase** | MIXED (conf: 0.40) |

---

## 🏆 DU DOAN

| | So | Score | Action | Risk |
|---|---|---|---|---|
| **Bach Thu** | **87** | 5.0/10 | ✅ RECOMMEND | MEDIUM |
| So Phu 1 | **14** | — | — | — |
| So Phu 2 | **55** | — | — | — |

### Reasoning chi tiet

**Bach Thu 87:**
- Tang 1 V10667 ⭐ BH-pass: MB:G7#4:D-1 LAST2. MB G7#4 ngay 02/06 (Quang Ninh) = 87. Lift +7.20pp. p=0.0014. Strength STRONG (BH-pass). Weight 5.
- Tang 3: Freq 4x/22d (duoi avg), nhung vua xuat hien 02/06. Mean-reversion potential.
- Co-occur voi 54: 13.6% (3/22), voi 67: 13.6% (3/22) — tot cho Xien.
- Confidence cap 55% (MB V10667 calibration).
- Giu tu morning prediction — BH-pass rule khong thay doi.

**So Phu 1 — 14:**
- Tang 3: Freq HOT #1 MB (10x/22d!). Recent 2x/3d. Wed 1x. Score 7.0/10. Weight 2.
- Markov cascade STRONG: MN 57→14 (3x), MN 34→14 (3x), MN 71→14 (3x). 3 independent MN sources deu chi vao 14. Weight 3.
- Tang 4 Cycle: Wed cycle 2/3 tuan (week_1 + week_2 co 14). Weight 1.
- Multi-tang: Tang 3 + Markov + Cycle = 3 layers. Weighted score 6.0.
- Thay doi tu morning (truoc: SP1=16). Ly do: 14 co Markov cascade cuc manh tu MN fresh data.
- Caution: 14 freq HOT nhung MISS ngay 02/06. Hom nay khac: co Markov + cycle backing.

**So Phu 2 — 55:**
- Tang 3: Freq 8x/22d, recent 3x/3d (hot streak). Score 7.2/10. Weight 2.
- Markov cascade: MN 57 (Soc Trang DB) → MB 55 (3x). Weight 2.
- Thay doi tu morning (truoc: SP2=54). Ly do: 55 recent 3x/3d manh hon 54 (2x).

---

## 🎲 XIEN

| Loai | Bo so | Score | Co-occur | Action |
|---|---|---|---|---|
| Xien 2 | 87-54 | 7.0 | 13.6% (3/22 ngay) | ✅ RECOMMEND |
| Xien 3 | 87-54-67 | 6.3 | 87-54=13.6%, 87-67=13.6%, 54-67=22.7% | ✅ RECOMMEND |
| Xien 4 | 87-54-67-55 | 5.5 | Most pairs >= 9.1% | RECOMMEND_WITH_CAUTION |

### Xien reasoning:
- Xien 2 (87-54): 87 tu BH-pass (weight 5). 54 tu freq 9x + cycle 2/3 (weight 3). Co-occur 13.6% >> baseline 7.1%. Score: avg(5,3)=4 + co-occur +2 + hot +1 = 7.0 → RECOMMEND.
- Xien 3 (87-54-67): 67 tu freq 7x + recent 3x. 54-67 co-occur 22.7% (cao nhat!). 3 sources da dang. Score: avg(5,3,2)=3.3 + co-occur +2 + hot +1 = 6.3 → RECOMMEND.
- Xien 4 (87-54-67-55): Them 55 (Markov cascade + recent hot). 87-55=9.1%, 54-55=18.2%, 55-67=13.6%. Score 5.5 < 7 threshold → RECOMMEND_WITH_CAUTION.
- Note: 54 va 67 duoc chon cho Xien (co-occur cao) khac voi SP1/SP2 (14, 55). Day la chien luoc da dang.

---

## ⚠️ CANH BAO

| Muc | Chi tiet |
|---|---|
| MB confidence cap | 55% max — evidence MB mong hon MN/MT 3-4 lan |
| 87 freq thap | Chi 4x/22d (duoi avg 5.9). BH-pass la signal chinh, freq khong ho tro |
| T4 chi 1 BH-pass | Chi MB:G7#4:D-1. Cac ngay khac (T2, T3) cung co 1 BH-pass. Khong dac biet |
| 14 miss hom truoc | 14 freq HOT nhung MISS 02/06. Hom nay co Markov cascade backing nhung van rui ro |

---

## ✅ VERIFY — Ket qua thuc te

> ✅ **Da xo 18:15 ngay 03/06/2026**

### Ket qua dai

| Dai | DB (5 so) | Duoi DB | G7 (4 so) | Duoi G7 |
|---|---|---|---|---|
| Bắc Ninh | 02636 | 36 | 52 90 77 34 | 52 90 77 34 |

**27 tails:** 36 66 30 79 70 58 13 38 35 69 23 22 51 98 76 95 71 98 48 18 74 13 55 52 90 77 34

### Kiem tra Bach Thu + So Phu (post_mt version)

| So | Du doan | Trung? | Ghi chu |
|---|---|---|---|
| Bach Thu | 87 | ❌ | 87 KHONG co trong 27 tails. 87 xuat hien o MT (Da Nang + Khanh Hoa) nhung MISS MB |
| So Phu 1 | 54 (post_mt) | ❌ | 54 MISS. Markov cascade 5 MT sources → 54 nhung khong trung MB |
| So Phu 2 | 52 (post_mt) | ✅ | 52 = G7#1 Bac Ninh. V10667+mined confirm |
| (post_mn SP1) | 14 | ❌ | 14 MISS — freq HOT nhung lai MISS 2 ngay lien tiep |
| (post_mn SP2) | 55 | ✅ | 55 = G6#3 Bac Ninh. Giu lai tu post_mn cung da trung |

### Kiem tra Xien (MB: 1 dai, check 27 tails)

| Loai | Bo so | ALL trung cung dai? | Ghi chu |
|---|---|---|---|
| Xien 2 | 87-54 | ❌ | 87 MISS → Xien MISS |
| Xien 3 | 87-54-14 (post_mt) | ❌ | 87 MISS |
| Xien 4 | 87-54-14-67 | ❌ | 87 MISS |
| (post_mn X3) | 87-54-67 | ❌ | 87 MISS |
| (post_mn X4) | 87-54-67-55 | ❌ | 87 MISS. Note: 55+67 ca 2 deu co nhung 87 block |

**Note:** Neu BT la 52 thay vi 87, Xien2 (52-55) da WIN (ca 2 co trong tails).

---

## 📝 BAI HOC

**Manh:**
- SP2=52 HIT (V10667 STRONG + mined, post_mt). Cung chinh la G7#1.
- 55 (post_mn SP2) cung HIT (G6#3). Chung to freq + Markov voi recent hot streak la signal tot cho SP.
- 95 xuat hien trong MB tails (G5#2) — cung la SP1 MT (HIT). Cross-region correlation.

**Yeu:**
- BT=87 BH-pass MISS. G7#4:D-1 rule lai MISS. MB BH-pass rules can them confirmation tu Tang 3 Statistical (87 chi 4x/22d, duoi avg).
- Markov cascade SP1=54 MISS: 5 MT sources deu chi vao 54 nhung result khong trung. Markov cascade from MT→MB khong reliable bang MT→MT.
- 14 freq HOT MISS 2 ngay lien tiep — freq alone khong du, ke ca co Markov backing.

**Dieu chinh:**
- MB BH-pass: Them filter — BT candidate phai co freq >= avg (5.9x/22d) MOI cho BH-pass weight 5. Neu freq < avg, giam weight xuong 3.
- Markov cascade: MT→MB reliability thap hon MN→MT. Giam weight MT→MB cascade tu 3 xuong 2.
- SP2 strategy thanh cong: V10667 MODERATE/STRONG cho SP2 voi freq support → giu nguyen.
- Xien MB: Khi BT chi dua vao 1 BH-pass rule ma khong co multi-tang confirm, khong nen dat BT lam anchor Xien. Chon SP lam anchor thay the.
