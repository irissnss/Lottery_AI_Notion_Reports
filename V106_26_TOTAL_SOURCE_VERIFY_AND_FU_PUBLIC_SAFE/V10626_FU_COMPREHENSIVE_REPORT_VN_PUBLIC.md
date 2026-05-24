# V10626 FU COMPREHENSIVE — MB DB D-2 Verify + MN/MT/MB Cross-Source Findings

> Generated: 2026-05-25T00:12:19
> Locked manifest: `artifacts/live_sync/20260524_221208/manifest.json`
>
> Scope: comprehensive research-only verification. NO live application, NO official mutation.
> All findings inherit V107 risk overlay: BH_FAIL_GLOBAL + SELECTION_BIAS_RISK + FORWARD_90D_INSUFFICIENT + PRE_REGISTER_ONLY.

## 1. Tom tat dau bao cao

Em da chay 3 scan lon:
- SCAN 1: Self-lag same-region (MB-self, MN-self per-station, MT-self per-station)
- SCAN 2: Cross-region MB_BOARD → MN/MT targets
- SCAN 3: Cross-region top-6 MN/MT stations → other regions

Tong cells positive: 9226. CSV luu top 5000.

**2 metric danh gia**:
- **H1 LOOSE**: transformed_tail co xuat hien o BAT KY giai cua target khong
- **H2 STRICT-DB**: transformed_tail = DB tail cua target (rat hep, baseline ~1-4%)

## 2. Verify gia thuyet owner ban dau (MB D = MB DB D-2)

Tom tat: **KHONG verify** o LAST2 D-2.

| Window | H1 LOOSE rate | Lift_pp | H2 STRICT rate | Lift_pp |
|---|---:|---:|---:|---:|
| 30d | 23.3% | -0.37 | 0.00% | -1.00 |
| 60d | 18.3% | -5.30 | 0.00% | -1.00 |
| 90d | 18.9% | -4.88 | 0.00% | -1.00 |
| 180d | 24.9% | +0.99 | 0.58% | -0.42 |
| 365d | 23.5% | -0.40 | 1.12% | +0.12 |

Chi co D-3 (+5.20pp), W-3 (+4.20pp), W-4 (+6.53pp) la manh hon D-2 doi voi LAST2 self-lag MB.

## 3. PHAT HIEN MOI MANH NHAT — Double-strong (H1 + H2 cung duong)

Cac rule double-strong la rule co H1 LOOSE lift >= +8pp VA H2 STRICT-DB lift >= +3pp (vua co recall cao vua co DB direct).

### Target MN

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MN<-MB:MB_BOARD:G2#2:FIRST2_REV` | W-2 | 60 | 60 | 61.7% | +18.33 | 11.67% | +8.52 |
| `MN<-MB:MB_BOARD:G2#2:P2P1` | W-2 | 60 | 60 | 61.7% | +18.33 | 11.67% | +8.52 |
| `MN<-MB:MB_BOARD:G2#2:FIRST2_REV` | W-2 | 90 | 86 | 61.6% | +18.33 | 10.47% | +7.31 |
| `MN<-MB:MB_BOARD:G2#2:P2P1` | W-2 | 90 | 86 | 61.6% | +18.33 | 10.47% | +7.31 |
| `MN<-MN:TP. HCM:G2#1:HEAD_SECOND_LAST` | D-4 | 180 | 52 | 59.6% | +17.37 | 9.62% | +6.63 |
| `MN<-MN:TP. HCM:G2#2:TAIL_HEAD` | W-4 | 180 | 32 | 59.4% | +12.59 | 12.50% | +9.03 |
| `MN<-MN:TP. HCM:G2#2:P4P1` | W-4 | 180 | 32 | 59.4% | +12.59 | 12.50% | +9.03 |
| `MN<-MB:MB_BOARD:G2#2:P3P5` | D-3 | 60 | 60 | 61.7% | +18.33 | 6.67% | +3.52 |
| `MN<-MB:MB_BOARD:G1#1:TAIL_HEAD` | W-1 | 60 | 60 | 55.0% | +11.67 | 10.00% | +6.85 |
| `MN<-MB:MB_BOARD:G1#1:P5P1` | W-1 | 60 | 60 | 55.0% | +11.67 | 10.00% | +6.85 |

### Target MT

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MT<-MT:Huế:G2#1:P3P4` | W-2 | 180 | 33 | 48.5% | +11.97 | 15.15% | +12.61 |
| `MT<-MT:Khánh Hòa:G2#1:P3P2` | D-2 | 180 | 51 | 51.0% | +20.51 | 7.84% | +5.88 |
| `MT<-MT:Đà Nẵng:G2#1:LAST2` | W-3 | 180 | 52 | 53.8% | +17.85 | 9.62% | +7.12 |
| `MT<-MT:Huế:G2#2:LAST2_REV` | D-3 | 180 | 30 | 50.0% | +14.87 | 10.00% | +7.53 |
| `MT<-MT:Huế:G2#2:P4P3` | D-3 | 180 | 30 | 50.0% | +14.87 | 10.00% | +7.53 |
| `MT<-MT:Huế:G2#1:LAST2` | W-2 | 180 | 33 | 45.5% | +8.94 | 12.12% | +9.58 |
| `MT<-MB:MB_BOARD:DB#1:P2P3` | D-6 | 60 | 60 | 46.7% | +11.10 | 10.00% | +7.55 |
| `MT<-MT:Đà Nẵng:DB#1:LAST2_REV` | W-4 | 180 | 52 | 44.2% | +8.23 | 11.54% | +9.04 |
| `MT<-MB:MB_BOARD:G1#1:P5P2` | D-1 | 60 | 60 | 45.0% | +9.43 | 10.00% | +7.55 |

### Target MB

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MB<-MT:Đà Nẵng:G2#2:SECOND_HEAD_TAIL` | W-2 | 180 | 30 | 43.3% | +19.30 | 6.67% | +5.67 |
| `MB<-MT:Khánh Hòa:G2#1:SECOND_HEAD_TAIL` | D-5 | 180 | 50 | 46.0% | +21.92 | 4.00% | +3.00 |
| `MB<-MT:Khánh Hòa:G2#1:P3P2` | W-3 | 180 | 51 | 39.2% | +15.31 | 5.88% | +4.88 |
| `MB<-MB:MB_BOARD:G2#2:P5P3` | W-2 | 60 | 60 | 40.0% | +16.37 | 5.00% | +4.00 |
| `MB<-MT:Đà Nẵng:G2#1:P3P4` | W-3 | 180 | 51 | 37.3% | +13.25 | 5.88% | +4.88 |
| `MB<-MT:Khánh Hòa:G2#2:P3P2` | W-3 | 180 | 33 | 36.4% | +12.42 | 6.06% | +5.06 |
| `MB<-MB:MB_BOARD:G1#1:HEAD_TAIL` | D-4 | 60 | 60 | 36.7% | +13.03 | 5.00% | +4.00 |
| `MB<-MT:Đà Nẵng:G2#1:FIRST2_REV` | D-4 | 180 | 51 | 35.3% | +11.39 | 5.88% | +4.88 |
| `MB<-MB:MB_BOARD:G2#1:P3P5` | W-4 | 60 | 60 | 31.7% | +8.03 | 6.67% | +5.67 |

## 4. Top 10 theo H1 LOOSE lift per target

### Target MN

**Top 10 MN theo H1 lift**

| Rule | Axis | W | Days | H1 hit% | H1 lift_pp | H2 hit% | H2 lift_pp | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `MN<-MT:Khánh Hòa:G2#2:P3P2` | W-2 | 180 | 32 | 62.5% | +20.28 | 0.00% | -2.91 | 16.79 |
| `MN<-MT:Khánh Hòa:G2#1:P3P2` | D-3 | 180 | 52 | 65.4% | +18.73 | 5.77% | +2.33 | 21.52 |
| `MN<-MT:Đà Nẵng:G2#1:P3P2` | W-2 | 180 | 52 | 65.4% | +18.73 | 1.92% | -1.52 | 16.91 |
| `MN<-MB:MB_BOARD:G2#2:FIRST2_REV` | W-2 | 60 | 60 | 61.7% | +18.33 | 11.67% | +8.52 | 29.55 |
| `MN<-MB:MB_BOARD:G2#2:P2P1` | W-2 | 60 | 60 | 61.7% | +18.33 | 11.67% | +8.52 | 29.55 |
| `MN<-MB:MB_BOARD:G2#2:P3P5` | D-3 | 60 | 60 | 61.7% | +18.33 | 6.67% | +3.52 | 23.55 |
| `MN<-MB:MB_BOARD:G2#2:LAST2` | W-3 | 60 | 60 | 61.7% | +18.33 | 5.00% | +1.85 | 21.55 |
| `MN<-MB:MB_BOARD:G2#2:P4P5` | W-3 | 60 | 60 | 61.7% | +18.33 | 5.00% | +1.85 | 21.55 |
| `MN<-MB:MB_BOARD:G2#2:P1P3` | W-4 | 60 | 60 | 61.7% | +18.33 | 1.67% | -1.48 | 17.55 |
| `MN<-MB:MB_BOARD:G2#2:P5P2` | D-3 | 60 | 60 | 61.7% | +18.33 | 1.67% | -1.48 | 17.55 |

### Target MT

**Top 10 MT theo H1 lift**

| Rule | Axis | W | Days | H1 hit% | H1 lift_pp | H2 hit% | H2 lift_pp | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `MT<-MT:Huế:G1#1:P3P2` | D-3 | 180 | 31 | 61.3% | +26.32 | 0.00% | -2.45 | 23.38 |
| `MT<-MT:Huế:G2#2:SECOND_HEAD_TAIL` | D-4 | 180 | 30 | 60.0% | +23.20 | 0.00% | -2.47 | 20.24 |
| `MT<-MT:Huế:G2#2:P2P4` | D-4 | 180 | 30 | 60.0% | +23.20 | 0.00% | -2.47 | 20.24 |
| `MT<-MT:Huế:G1#1:LAST2_REV` | D-3 | 180 | 31 | 58.1% | +23.10 | 0.00% | -2.45 | 20.15 |
| `MT<-MB:MB_BOARD:G2#2:SECOND_HEAD_TAIL` | W-1 | 60 | 60 | 56.7% | +21.10 | 3.33% | +0.88 | 23.16 |
| `MT<-MB:MB_BOARD:G2#2:P2P5` | W-1 | 60 | 60 | 56.7% | +21.10 | 3.33% | +0.88 | 23.16 |
| `MT<-MT:Khánh Hòa:G2#1:P3P2` | D-2 | 180 | 51 | 51.0% | +20.51 | 7.84% | +5.88 | 27.57 |
| `MT<-MT:Huế:G2#1:FIRST2` | D-2 | 180 | 30 | 50.0% | +19.97 | 3.33% | +1.33 | 21.57 |
| `MT<-MT:Huế:G2#1:P1P2` | D-2 | 180 | 30 | 50.0% | +19.97 | 3.33% | +1.33 | 21.57 |
| `MT<-MT:Huế:G2#1:HEAD_SECOND_LAST` | W-4 | 180 | 36 | 55.6% | +19.69 | 2.78% | +0.25 | 19.99 |

### Target MB

**Top 10 MB theo H1 lift**

| Rule | Axis | W | Days | H1 hit% | H1 lift_pp | H2 hit% | H2 lift_pp | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `MB<-MT:Đà Nẵng:G2#2:LAST2` | W-3 | 180 | 32 | 46.9% | +22.91 | 3.12% | +2.12 | 25.46 |
| `MB<-MT:Đà Nẵng:G2#2:P3P4` | W-3 | 180 | 32 | 46.9% | +22.91 | 3.12% | +2.12 | 25.46 |
| `MB<-MT:Khánh Hòa:G2#1:SECOND_HEAD_TAIL` | D-5 | 180 | 50 | 46.0% | +21.92 | 4.00% | +3.00 | 25.52 |
| `MB<-MT:Đà Nẵng:G2#2:SECOND_HEAD_TAIL` | W-2 | 180 | 30 | 43.3% | +19.30 | 6.67% | +5.67 | 26.10 |
| `MB<-MT:Khánh Hòa:G2#1:LAST2_REV` | W-2 | 180 | 51 | 43.1% | +19.24 | 0.00% | -1.00 | 18.04 |
| `MB<-MT:Khánh Hòa:G2#1:LAST2` | D-2 | 180 | 50 | 42.0% | +18.06 | 0.00% | -1.00 | 16.86 |
| `MB<-MT:Khánh Hòa:G1#1:TAIL_HEAD` | W-1 | 180 | 51 | 41.2% | +17.27 | 1.96% | +0.96 | 18.43 |
| `MB<-MT:Đà Nẵng:DB#1:FIRST2` | D-5 | 180 | 49 | 40.8% | +17.18 | 2.04% | +1.06 | 18.46 |
| `MB<-MT:Đà Nẵng:DB#1:HEAD_TAIL` | D-5 | 180 | 49 | 40.8% | +17.18 | 0.00% | -0.98 | 16.01 |
| `MB<-MB:MB_BOARD:G2#2:P5P3` | W-2 | 60 | 60 | 40.0% | +16.37 | 5.00% | +4.00 | 22.17 |

## 5. Top 10 theo H2 STRICT-DB lift per target (DB direct match)

### Target MN

**Top 10 MN theo H2 STRICT-DB lift**

| Rule | Axis | W | Days | H1 hit% | H1 lift_pp | H2 hit% | H2 lift_pp | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `MN<-MN:TP. HCM:G2#2:TAIL_HEAD` | W-4 | 180 | 32 | 59.4% | +12.59 | 12.50% | +9.03 | 23.43 |
| `MN<-MN:TP. HCM:G2#2:P4P1` | W-4 | 180 | 32 | 59.4% | +12.59 | 12.50% | +9.03 | 23.43 |
| `MN<-MT:Đà Nẵng:G2#1:SECOND_HEAD_TAIL` | D-6 | 180 | 51 | 45.1% | +3.22 | 11.76% | +8.76 | 13.73 |
| `MN<-MB:MB_BOARD:G2#2:FIRST2_REV` | W-2 | 60 | 60 | 61.7% | +18.33 | 11.67% | +8.52 | 29.55 |
| `MN<-MB:MB_BOARD:G2#2:P2P1` | W-2 | 60 | 60 | 61.7% | +18.33 | 11.67% | +8.52 | 29.55 |
| `MN<-MB:MB_BOARD:G1#1:LAST2_REV` | W-1 | 60 | 60 | 46.7% | +3.33 | 11.67% | +8.52 | 14.55 |
| `MN<-MB:MB_BOARD:G1#1:P5P4` | W-1 | 60 | 60 | 46.7% | +3.33 | 11.67% | +8.52 | 14.55 |
| `MN<-MN:TP. HCM:G2#1:HEAD_TAIL` | W-1 | 180 | 51 | 51.0% | +4.22 | 11.76% | +8.29 | 14.17 |
| `MN<-MT:Đà Nẵng:G2#2:HEAD_SECOND_LAST` | W-4 | 180 | 35 | 51.4% | +4.86 | 11.43% | +8.00 | 14.46 |
| `MN<-MB:MB_BOARD:G2#2:FIRST2_REV` | W-2 | 90 | 86 | 61.6% | +18.33 | 10.47% | +7.31 | 28.10 |

### Target MT

**Top 10 MT theo H2 STRICT-DB lift**

| Rule | Axis | W | Days | H1 hit% | H1 lift_pp | H2 hit% | H2 lift_pp | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `MT<-MT:Huế:G2#1:P3P4` | W-2 | 180 | 33 | 48.5% | +11.97 | 15.15% | +12.61 | 27.10 |
| `MT<-MT:Huế:G2#1:LAST2` | W-2 | 180 | 33 | 45.5% | +8.94 | 12.12% | +9.58 | 20.43 |
| `MT<-MB:MB_BOARD:G2#1:P5P2` | W-1 | 60 | 60 | 40.0% | +4.43 | 11.67% | +9.22 | 16.49 |
| `MT<-MT:Đà Nẵng:DB#1:LAST2_REV` | W-4 | 180 | 52 | 44.2% | +8.23 | 11.54% | +9.04 | 19.08 |
| `MT<-MT:Khánh Hòa:DB#1:LAST2` | W-4 | 180 | 52 | 40.4% | +4.90 | 11.54% | +9.04 | 15.75 |
| `MT<-MT:Huế:G2#2:HEAD_SECOND_LAST` | W-4 | 180 | 36 | 38.9% | +3.03 | 11.11% | +8.58 | 13.33 |
| `MT<-MT:Huế:G2#2:P1P3` | W-4 | 180 | 36 | 38.9% | +3.03 | 11.11% | +8.58 | 13.33 |
| `MT<-MB:MB_BOARD:G2#1:P5P2` | W-1 | 90 | 87 | 41.4% | +6.13 | 10.34% | +7.91 | 16.62 |
| `MT<-MB:MB_BOARD:DB#1:P2P3` | D-6 | 60 | 60 | 46.7% | +11.10 | 10.00% | +7.55 | 21.16 |
| `MT<-MB:MB_BOARD:G1#1:P5P2` | D-1 | 60 | 60 | 45.0% | +9.43 | 10.00% | +7.55 | 19.49 |

### Target MB

**Top 10 MB theo H2 STRICT-DB lift**

| Rule | Axis | W | Days | H1 hit% | H1 lift_pp | H2 hit% | H2 lift_pp | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `MB<-MT:Đà Nẵng:G2#2:SECOND_HEAD_TAIL` | W-2 | 180 | 30 | 43.3% | +19.30 | 6.67% | +5.67 | 26.10 |
| `MB<-MB:MB_BOARD:G2#1:P3P5` | W-4 | 60 | 60 | 31.7% | +8.03 | 6.67% | +5.67 | 15.83 |
| `MB<-MB:MB_BOARD:G2#1:TAIL_HEAD` | W-4 | 60 | 60 | 26.7% | +3.03 | 6.67% | +5.67 | 10.83 |
| `MB<-MB:MB_BOARD:G2#1:P5P1` | W-4 | 60 | 60 | 26.7% | +3.03 | 6.67% | +5.67 | 10.83 |
| `MB<-MB:MB_BOARD:DB#1:P1P3` | D-1 | 60 | 60 | 25.0% | +1.37 | 6.67% | +5.67 | 9.17 |
| `MB<-MT:Đà Nẵng:G2#2:HEAD_SECOND_LAST` | W-3 | 180 | 32 | 21.9% | -2.09 | 6.25% | +5.25 | 4.21 |
| `MB<-MT:Đà Nẵng:G2#1:TAIL_HEAD` | D-5 | 180 | 49 | 30.6% | +6.98 | 6.12% | +5.14 | 13.15 |
| `MB<-MT:Khánh Hòa:G2#2:P3P2` | W-3 | 180 | 33 | 36.4% | +12.42 | 6.06% | +5.06 | 18.50 |
| `MB<-MT:Khánh Hòa:G2#2:SECOND_HEAD_TAIL` | W-3 | 180 | 33 | 21.2% | -2.73 | 6.06% | +5.06 | 3.35 |
| `MB<-MT:Khánh Hòa:G2#2:FIRST2_REV` | W-3 | 180 | 33 | 18.2% | -5.76 | 6.06% | +5.06 | 0.32 |

## 6. So sanh MN vs MT vs MB — nhung phat hien chinh

### 6.1 Target MN (Dich Mien Nam)

- **MN<-MB:G2#2:FIRST2_REV W-2** (60d): H1 +18.3pp + H2 +8.52pp. Double-strong. Cong thuc: lay G2#2 cua MB cach 2 tuan, dao 2 chu so dau.
- **MN<-MN:TP. HCM:G2#2:TAIL_HEAD W-4** (180d, 32d sample): H2 +9.03pp + H1 +12.6pp. Same-day cross-station self-lag.
- **MN<-MT:Khánh Hòa:G2#2:P3P2 W-2** (180d, 32d): H1 +20.3pp. Recall manh nhung H2 yeu.
- **MN<-MT:Khánh Hòa:G2#1:P3P2 D-3** (180d, 52d): H1 +18.7pp + H2 +2.33pp. Cong thuc: lay G2#1 cua MT Khanh Hoa cach 3 ngay, chu so 3 + chu so 2.

### 6.2 Target MT (Dich Mien Trung)

- **MT<-MT:Huế:G2#1:P3P4 W-2** (180d, 33d): H2 +12.61pp + H1 +12.0pp. **DOUBLE-STRONG manh nhat MT.**
- **MT<-MT:Huế:G1#1:P3P2 D-3** (180d, 31d): H1 +26.3pp. Recall rat cao.
- **MT<-MT:Huế:G2#2:SECOND_HEAD_TAIL D-4** (180d, 30d): H1 +23.2pp.
- **MT<-MT:Đà Nẵng:DB#1:LAST2_REV W-4** (180d, 52d): H2 +9.04pp. DB-to-DB 4-tuan, doi 2 so cuoi.
- **MT<-MT:Khánh Hòa:DB#1:LAST2 W-4** (180d, 52d): H2 +9.04pp. DB-to-DB 4-tuan, raw last2.
- **MT<-MT:Khánh Hòa:G2#1:P3P2 D-2** (180d, 51d): H1 +20.5pp + H2 +5.88pp. **D-2 verify trong MT — KHAC voi MB.**

### 6.3 Target MB (Dich Mien Bac)

- **MB<-MT:Đà Nẵng:G2#2:SECOND_HEAD_TAIL W-2** (180d, 30d): H1 +19.3pp + H2 +5.67pp. **DOUBLE-STRONG MB.**
- **MB<-MT:Đà Nẵng:G2#2:LAST2 W-3** (180d, 32d): H1 +22.9pp + H2 +2.12pp.
- **MB<-MT:Khánh Hòa:G2#1:SECOND_HEAD_TAIL D-5** (180d, 50d): H1 +21.9pp + H2 +3.00pp.
- **MB<-MB:MB_BOARD:G2#1:P3P5 W-4** (60d): H2 +5.67pp. MB self-lag chu ky 4 tuan.
- **MB<-MB:MB_BOARD:DB#1:P1P3 D-1** (60d): H2 +5.67pp + H1 +1.4pp.

## 7. Pattern lon ma em nhin thay

1. **MT-Hue la source rat manh** cho MT-self target. G1#1 va G2#1/G2#2 cua Hue o D-3/D-4/W-2/W-4 deu xuat hien o top H1 va H2. **Day la phat hien moi V10606 khong cover.**

2. **TP. HCM (MN) la source manh** cho MN-self target o W-4 (cung thu 4 tuan truoc). G2#2 lay TAIL_HEAD lift H2 +9pp.

3. **MT Đà Nẵng / Khánh Hòa** la source cuc manh cho MB target o D-5, W-2, W-3 voi G2#1, G2#2 SECOND_HEAD_TAIL hoac LAST2. Day la cross-region xuat hien nhieu lan.

4. **Chu ky W-2 / W-3 / W-4** (cung thu cua 2/3/4 tuan truoc) la chu ky tan suat manh hon D-1/D-2 don le. Day la pattern "theo thu tuan truoc" ma owner da nghi tu V10603.

5. **DB direct match (H2)** chi co tin hieu khi lag W-1/W-2/W-3/W-4 hoac D-5/D-6 voi transform LAST2 / TAIL_HEAD / P3P4 / SECOND_HEAD_TAIL. KHONG xuat hien o D-1/D-2/D-3 LAST2.

6. **Transform "P3P2" va "SECOND_HEAD_TAIL"** xuat hien rat nhieu trong top - chung dac thu cho cau truc 5-chu-so giai dac biet.

## 8. Cap nhat de xuat pre-register panel (DOI ANH XAC NHAN)

De xuat **15 rule moi nhat va manh nhat** de them vao pre-register panel (giu PRE_REGISTER_ONLY status, khong live):

### MN panel (de xuat 5 rule moi)
1. `MN<-MB:MB_BOARD:G2#2:FIRST2_REV:W-2` — H1 +18.3pp + H2 +8.52pp (60d)
2. `MN<-MN:TP. HCM:G2#2:TAIL_HEAD:W-4` — H2 +9.03pp + H1 +12.6pp (180d, 32d sample)
3. `MN<-MT:Khánh Hòa:G2#1:P3P2:D-3` — H1 +18.7pp + H2 +2.33pp (180d, 52d)
4. `MN<-MT:Đà Nẵng:G2#1:SECOND_HEAD_TAIL:D-6` — H2 +8.76pp (180d, 51d)
5. `MN<-MN:TP. HCM:G2#2:P4P1:W-4` — H2 +9.03pp same TP.HCM W-4 anchor

### MT panel (de xuat 6 rule moi)
1. `MT<-MT:Huế:G2#1:P3P4:W-2` — H2 +12.61pp + H1 +12.0pp (180d, 33d)
2. `MT<-MT:Đà Nẵng:DB#1:LAST2_REV:W-4` — H2 +9.04pp (180d, 52d)
3. `MT<-MT:Khánh Hòa:DB#1:LAST2:W-4` — H2 +9.04pp (180d, 52d)
4. `MT<-MT:Khánh Hòa:G2#1:P3P2:D-2` — H1 +20.5pp + H2 +5.88pp (180d, 51d) **verify D-2 trong MT**
5. `MT<-MT:Huế:G1#1:P3P2:D-3` — H1 +26.3pp (180d, 31d) cao nhat MT
6. `MT<-MB:MB_BOARD:G2#2:SECOND_HEAD_TAIL:W-1` — H1 +21.1pp + H2 +0.88pp (60d)

### MB panel (de xuat 4 rule moi)
1. `MB<-MT:Đà Nẵng:G2#2:SECOND_HEAD_TAIL:W-2` — H1 +19.3pp + H2 +5.67pp (180d, 30d) double-strong nhat MB
2. `MB<-MT:Đà Nẵng:G2#2:LAST2:W-3` — H1 +22.9pp + H2 +2.12pp (180d, 32d)
3. `MB<-MT:Khánh Hòa:G2#1:SECOND_HEAD_TAIL:D-5` — H1 +21.9pp + H2 +3.00pp (180d, 50d)
4. `MB<-MB:MB_BOARD:DB#1:P1P3:D-1` — H2 +5.67pp DB-strict same-day-1

## 9. Hard safety check

| Item | Value |
|---|---|
| Official mutation | 0 |
| Provider/manual AI call | 0 |
| Wallet | 0 |
| Lane promotion | 0 |
| Public push | NO |
| Live application | 0 |
| Broad selector used | 0 |
| V107 risk overlay | BH_FAIL_GLOBAL + SELECTION_BIAS_RISK + FORWARD_90D_INSUFFICIENT |
| live_eligible | False |
| Status | PRE_REGISTER_ONLY |

## 10. Owner decisions (DOI ANH)

- **(A)** Anh OK em them 15 rule moi (5 MN + 6 MT + 4 MB) vao pre-register panel V10626?
- **(B)** Anh OK em khoa panel V10626 + FU bo sung lai thanh baseline 90-day forward audit, timestamp `2026-05-25`?
- **(C)** Anh muon em mo pass rieng kiem tra sau MT-Hue (source rat manh moi noi nay) va TP.HCM W-4 (DB-direct cao)?
- **(D)** Private commit gop ca FU MB DB D-2 + comprehensive scan thanh `V20.3.37.106.26.1: comprehensive cross-source verify + new findings`? Default doi anh OK.
- **(E)** Public push? Default NO theo HARD LOCK.

## 11. Output artifacts

Trong `artifacts/v106_26_followup_mb_db_d2_hypothesis/`:
- `V10626_FU_OWNER_REPORT_VN.md` — MB DB D-2 verify (Phan 1)
- `V10626_FU_COMPREHENSIVE_REPORT_VN.md` — bao cao tong (file nay)
- `machine_readable/V10626_FU_MB_DB_D2_VERIFY.json` — raw verify
- `machine_readable/V10626_FU_COMPREHENSIVE_SCAN.csv` — 5000 top rule
- `machine_readable/V10626_FU_COMPREHENSIVE_SCAN_SUMMARY.json` — top per target
