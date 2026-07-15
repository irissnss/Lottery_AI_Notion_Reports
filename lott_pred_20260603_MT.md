# 🟡 MIEN TRUNG — T4 03/06/2026

| | |
|---|---|
| **Dai** | Đà Nẵng · Khánh Hòa |
| **Version** | `post_mn` |
| **Created** | 03/06 16:45 VN |
| **Data tu** | 03/06 (22 ngay lookback + MN fresh data) |
| **Phase** | MIXED (conf: 0.35) |

---

## 🏆 DU DOAN

| | So | Score | Action | Risk |
|---|---|---|---|---|
| **Bach Thu** | **59** | 7.0/10 | ✅ RECOMMEND | LOW |
| So Phu 1 | **95** | — | — | — |
| So Phu 2 | **75** | — | — | — |

### Reasoning chi tiet

**Bach Thu 59:**
- Tang 1B (Cross-Region): MB G7#2 ngay 02/06 (Quang Ninh) = 59. Rule MT-01 → MT hom nay. Weight 3.
- Tang 3 (Statistical): Freq 7x/22d, recent 3x/3d, wed 1x/3wed. Score 6.8/10.
- Markov cascade (MN fresh): MN 57 (Soc Trang DB) → MT 59 (3x). MN 25 (hot all 3 dai) → MT 59 (3x). 2 independent MN sources.
- Multi-tang: Tang 1B + Tang 3 + Markov = 3 layers xac nhan. Weighted score 7.0.

**So Phu 1 — 95:**
- Tang 3: Freq HOT #1 (8x/22d), recent 4x/3d (!). Score 7.0/10.
- Markov: MN 71 (hot 2x today) → MT 95 (2x transition).
- Co-occur voi 59: 18.2% (4/22 ngay) — SIGNIFICANT (> 6% baseline MT 2 dai).

**So Phu 2 — 75:**
- Tang 3: Freq 8x/22d, recent 3x/3d. Score 6.2/10.
- Markov cascade STRONG: MN 57 → MT 75 (3x), MN 71 → MT 75 (3x). 2 independent sources.
- Co-occur voi 59: 13.6% (3/22). Co-occur voi 95: 18.2% (4/22).
- Thay doi tu morning (truoc: SP2=23). Ly do: Markov cascade tu MN fresh data cho 75 manh hon 23.

---

## 🎲 XIEN

| Loai | Bo so | Score | Co-occur | Action |
|---|---|---|---|---|
| Xien 2 | 59-95 | 6.0 | 18.2% (4/22 ngay) | ✅ RECOMMEND |
| Xien 3 | 59-95-75 | 5.5 | 59-95=18.2%, 59-75=13.6%, 75-95=18.2% | ✅ RECOMMEND |
| Xien 4 | — | — | — | SKIP |

### Xien reasoning:
- Xien 2 (59-95): 59 tu Tang 1B + Markov, 95 tu freq HOT + Markov. Da dang source. Co-occur 18.2% >> baseline 6%.
- Xien 3 (59-95-75): ALL 3 pairs co-occur >= 13.6%. ALL hot (last 3d). 3 sources khac nhau.
- Xien 4: SKIP — MT 18 tails/dai, baseline 0.07%/dai qua thap. Khong du 4 candidates manh.

---

## ⚠️ CANH BAO

| Muc | Chi tiet |
|---|---|
| V10667 empty | MT T4 co 0 BH-pass, 0 MODERATE+ rules. Hoan toan phu thuoc Tang 1B/2/3 |
| T4 khong phai hot day | MT hot days = T5 (85 BH-pass), T7 (90 BH-pass). T4 signal yeu |
| Phase MIXED | Phase conf 0.35 — khong ro MIRROR/CROSS |
| Baseline per dai | MT chi 18 tails/dai. Xien kho trung hon MB (27 tails) |

---

## ✅ VERIFY — Ket qua thuc te

> ✅ **Da xo 17:15 ngay 03/06/2026**

### Ket qua cac dai

| Dai | DB (6 so) | Duoi DB | G8 | Duoi G8 |
|---|---|---|---|---|
| Đà Nẵng | 725175 | 75 | 95 | 95 |
| Khánh Hòa | 863914 | 14 | 71 | 71 |

### Kiem tra Bach Thu + So Phu

| So | Du doan | Trung? | Ghi chu |
|---|---|---|---|
| Bach Thu | 59 | ✅ HIT | Da Nang: G3_2=85559 (duoi 59). Khanh Hoa: MISS |
| So Phu 1 | 95 | ✅ HIT | Da Nang: G8=95. Khanh Hoa: MISS |
| So Phu 2 | 75 | ✅ HIT | Da Nang: DB=725175 (duoi 75) + G4_7=54375 (duoi 75). Khanh Hoa: MISS |

### Kiem tra Xien (MT: check tung dai rieng)

| Loai | Bo so | ALL trung cung dai? | Ghi chu |
|---|---|---|---|
| Xien 2 | 59-95 | ✅ WIN (Da Nang) | 59 (G3_2) + 95 (G8) ca 2 co o Da Nang |
| Xien 3 | 59-95-75 | ✅ WIN (Da Nang) | 59 + 95 + 75 (DB tail + G4_7) ALL co o Da Nang |

**Da Nang all tails:** 95 87 35 18 17 22 23 46 11 58 35 81 75 68 59 50 46 75
**Khanh Hoa all tails:** 71 87 11 57 49 94 54 68 38 93 06 14 06 52 60 89 60 14

---

## 📝 BAI HOC

**Manh:**
- **MT-01 cross-region rule WIN ngay thu 3 lien tiep.** MB G7#2 02/06 = 59. Rule MT-01: MB G7#2 → MT D+1. Da Nang co 59 trong tails. PERFECT.
- **Markov cascade 57→59 chinh xac.** MN Soc Trang DB=57 → Markov → 59 (MT). Confirmed.
- **Markov cascade 57→75 chinh xac.** 57 → 75 transition HIT. Da Nang DB tail = 75.
- **ALL 3 so HIT tai cung 1 dai (Da Nang)** → Xien 2 + Xien 3 deu WIN. Day la ngay perfect cho MT.
- **SP1=95 HIT G8** — freq analysis + cross-region backing deu chinh xac.

**Yeu:**
- Khanh Hoa MISS tat ca — chi Da Nang trung. Multi-dai coverage can cai thien.
- Note: 87 xuat hien o CA 2 dai MT (Da Nang + Khanh Hoa) nhung khong duoc predict. Co the la signal cho cross-region.

**Dieu chinh:**
- MT-01 rule: 3 ngay WIN lien tiep → tang weight tu 3 len 4 (tam thoi, theo doi tiep).
- Markov cascade MN→MT: confirmed reliable. Giu weight 3.
- SP strategy tai MT: freq + Markov combination rat manh. Giu nguyen approach.
