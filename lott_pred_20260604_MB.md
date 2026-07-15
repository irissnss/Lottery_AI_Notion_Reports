# 🔵 MIEN BAC — Thu 04/06/2026

| | |
|---|---|
| **Dai** | Hà Nội |
| **Version** | `morning` |
| **Created** | 03/06 22:50 VN |
| **Data tu** | 03/06 (23 ngay lookback) |
| **Phase** | MIXED (conf: 0.45) |

---

## 🏆 DU DOAN (MB confidence cap 55%)

| | So | Score | Action | Risk |
|---|---|---|---|---|
| **Bach Thu** | **95** | 6.0/10 | ✅ RECOMMEND | MEDIUM |
| So Phu 1 | **53** | 5.5/10 | — | — |
| So Phu 2 | **38** | 5.5/10 | — | — |

### Reasoning chi tiet

**Bach Thu 95:**
- Tang 1 V10667 MODERATE: MN:G2#1:D-1 (Dong Nai G2=87795→95), lift +5.94pp, weight 3
- Tang 2 Mined: co trong mined_candidates, multi-confirm
- Tang 3 Statistical: freq=6/23 above avg (4.9) → warm signal
- BH-pass candidates 79(freq=4<avg) va 53(self-lag hit_rate=0%) kem hon
- BH_PASS_FREQ_GATE: 79 downweighted 5→3 (freq below avg)
- Multi-layer confirm (V10667+Mined+Freq) → 95 la BT tot nhat

**So Phu 1 — 53:**
- Tang 1 V10667 BH-pass: MB:DB#1:D-3 (Ha Noi DB=90353→53), lift +6.25pp, weight 5
- Tang 5 Self-lag: MB→MB rule, nhung layer5 hit_rate=0/2 → caution
- Tang 3: freq=5/23 at avg → neutral
- BH-pass strong nhung single-source + self-lag weakness

**So Phu 2 — 38:**
- Tang 1 V10667 MODERATE: MN:G2#1:D-1 (Can Tho G2=10938→38), lift +5.94pp
- Tang 3: freq=7/23 above avg → hot signal
- Diverse source (MN→MB cross-region)

### Candidates backup:
| So | Source | Freq | Note |
|---|---|---|---|
| 79 | V10667 BH-pass MB:G2#2:D-1 | 4/23 | freq below avg → downweighted |
| 14 | Mined + freq=10 HOTTEST | 10/23 | No V10667 → pure statistical |
| 42 | V10667 MODERATE MN:G3#1:D-3 | 6/23 | Good freq |
| 18 | V10667 MODERATE MN:G3#1:D-3 | 6/23 | Good co-occur with 95 |

---

## 🎲 XIEN

| Loai | Bo so | Score | Co-occur | Action |
|---|---|---|---|---|
| Xien 2 | 14-95 | 6.0 | 13.0% (3/23 ngay) | ✅ RECOMMEND |
| Xien 3 | 14-18-95 | 5.5 | 8.7% (2/23 ngay) | ✅ RECOMMEND |
| Xien 4 | 14-18-53-95 | 3.0 | <3% | ⛔ SKIP |

### Xien reasoning:
- 14-95: co-occur 13.0% vs baseline 7.1% → lift 1.8x. 14=HOTTEST(freq=10)+mined, 95=BT
- 14-18-95: co-occur 8.7% vs baseline 1.8% → lift 4.8x! 18=V10667 MODERATE+freq=6
- 14 dung lam Xien anchor thay vi BT anchor (theo auto_rule XIEN_NO_BT_ANCHOR)
- MB 27 tails → Xien co kha nang cao hon MN/MT

---

## ⚠️ CANH BAO

| Muc | Chi tiet |
|---|---|
| MB cap 55% | V10667 evidence mong hon MN/MT 3-4 lan |
| Self-lag weak | Layer5 hit_rate=0/2 → SP1=53 tu self-lag can than |
| BH-pass filtered | 79 BH-pass downweighted vi freq < avg (W1 lesson) |
| Re-predict | Se duoc re-predict sau MN (16:35) va MT (17:35) voi cascade data |

---

## ✅ VERIFY — Ket qua thuc te

> ⏳ **Cho ket qua xo 18:15 ngay 04/06/2026**

### Ket qua cac dai

| Dai | DB (5 so) | Duoi DB | G7 (4 so) |
|---|---|---|---|
| Hà Nội | _____ | __ | __ __ __ __ |

### Full 27 tails

> ⏳

### Kiem tra Bach Thu + So Phu

| So | Du doan | Trung? | Ghi chu |
|---|---|---|---|
| Bach Thu | 95 | ⏳ | |
| So Phu 1 | 53 | ⏳ | |
| So Phu 2 | 38 | ⏳ | |

### Kiem tra Xien (MB: 1 dai Ha Noi, 27 tails)

| Loai | Bo so | ALL trung? | Ghi chu |
|---|---|---|---|
| Xien 2 | 14-95 | ⏳ | |
| Xien 3 | 14-18-95 | ⏳ | |
| Xien 4 | — | ⛔ SKIP | |

---

## 📝 BAI HOC (ghi sau verify)

> _BH_PASS_FREQ_GATE hieu qua? Multi-confirm BT vs single-source BH-pass? Self-lag layer5?_
