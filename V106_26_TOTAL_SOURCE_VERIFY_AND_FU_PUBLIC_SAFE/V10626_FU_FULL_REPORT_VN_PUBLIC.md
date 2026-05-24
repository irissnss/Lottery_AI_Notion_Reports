# V10626 FU FULL — Bao Cao Comprehensive Cross-Source MN/MT/MB (Schema-Fixed)

> Generated: 2026-05-25T00:21:10
> Locked manifest: `artifacts/live_sync/20260524_221208/manifest.json`
>
> Scope: research-only verification, schema-safe key-name extractor.
> Hard locks: NO live application, NO official mutation, NO public push.
> V107 risk overlay applies to all: BH_FAIL_GLOBAL + SELECTION_BIAS_RISK + FORWARD_90D_INSUFFICIENT.

## 1. Tom tat dau bao cao

Lan nay em mo rong sang TAT CA giai ic bo so cho ca 3 mien:
- **MB**: DB (5d), G1 (5d), G2#1 (5d), G2#2 (5d)
- **MN**: G8 (2d ⭐), G7 (3d), G5 (4d), G2 (5d), G1 (5d), DB (6d) — moi giai 1 bo duy nhat
- **MT**: G8 (2d ⭐), G7 (3d), G5 (4d), G2 (5d), G1 (5d), DB (6d) — moi giai 1 bo duy nhat

Tong positive rules: 12966. CSV luu 6000 top.

Bug schema da fix: 2 cach order JSON cho MN/MT (G8-first vs DB-first). Truoc khi fix, ~8% rows MN/MT bi label sai. V3 dung key-name lookup tu Vietnamese key → schema-safe.

### Phan bo rule theo prize

| Prize | Total positive rules |
|---|---:|
| G2 | 4728 |
| DB | 3215 |
| G1 | 2991 |
| G5 | 912 |
| G7 | 676 |
| G8 | 444 |

## 2. Verify gia thuyet owner ban dau (MB D = MB DB D-2)

Tom tat: **VAN KHONG verify** o LAST2 D-2 sau khi fix schema MB (MB schema khong bi anh huong vi MB luon DB-first).

| Window | H1 LOOSE rate | Lift_pp | H2 STRICT rate | Lift_pp |
|---|---:|---:|---:|---:|
| 30d | 23.3% | -0.37 | 0.00% | -1.00 |
| 60d | 18.3% | -5.30 | 0.00% | -1.00 |
| 90d | 18.9% | -4.88 | 0.00% | -1.00 |
| 180d | 24.9% | +0.99 | 0.58% | -0.42 |
| 365d | 23.5% | -0.40 | 1.12% | +0.12 |

## 3. PHAT HIEN DOUBLE-STRONG (H1>=+8pp VA H2>=+4pp)

### TARGET MN

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MN<-MB:MB_BOARD:G2#2:FIRST2_REV` | W-2 | 60 | 60 | 61.7% | +18.33 | 11.67% | +8.52 |
| `MN<-MB:MB_BOARD:G2#2:P2P1` | W-2 | 60 | 60 | 61.7% | +18.33 | 11.67% | +8.52 |
| `MN<-MB:MB_BOARD:G2#2:FIRST2_REV` | W-2 | 90 | 86 | 61.6% | +18.33 | 10.47% | +7.31 |
| `MN<-MB:MB_BOARD:G2#2:P2P1` | W-2 | 90 | 86 | 61.6% | +18.33 | 10.47% | +7.31 |
| `MN<-MT:Đà Nẵng:G2#1:TAIL_HEAD` | D-4 | 180 | 52 | 63.5% | +21.50 | 7.69% | +4.75 |
| `MN<-MT:Đà Nẵng:G1#1:SECOND_HEAD_TAIL` | D-2 | 180 | 51 | 52.9% | +10.67 | 15.69% | +12.69 |
| `MN<-MT:Đà Nẵng:G1#1:P2P5` | D-2 | 180 | 51 | 52.9% | +10.67 | 15.69% | +12.69 |
| `MN<-MT:Đà Nẵng:G7#1:TAIL_HEAD` | W-3 | 180 | 52 | 61.5% | +14.88 | 9.62% | +6.17 |
| `MN<-MN:TP. HCM:G7#1:FIRST2_REV` | W-4 | 180 | 51 | 56.9% | +10.10 | 11.76% | +8.29 |
| `MN<-MN:TP. HCM:G7#1:P2P1` | W-4 | 180 | 51 | 56.9% | +10.10 | 11.76% | +8.29 |
| `MN<-MB:MB_BOARD:G1#1:TAIL_HEAD` | W-1 | 60 | 60 | 55.0% | +11.67 | 10.00% | +6.85 |
| `MN<-MB:MB_BOARD:G1#1:P5P1` | W-1 | 60 | 60 | 55.0% | +11.67 | 10.00% | +6.85 |
| `MN<-MT:Khánh Hòa:G7#1:LAST2` | D-5 | 180 | 51 | 51.0% | +8.71 | 11.76% | +8.76 |
| `MN<-MT:Khánh Hòa:G7#1:SECOND_HEAD_TAIL` | D-5 | 180 | 51 | 51.0% | +8.71 | 11.76% | +8.76 |
| `MN<-MN:TP. HCM:G2#1:P4P1` | W-1 | 180 | 51 | 54.9% | +8.14 | 11.76% | +8.29 |

### TARGET MT

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MT<-MT:Huế:DB#1:P4P1` | D-4 | 180 | 31 | 64.5% | +27.55 | 9.68% | +7.19 |
| `MT<-MT:Đà Nẵng:G2#1:LAST2_REV` | W-1 | 180 | 52 | 55.8% | +19.77 | 9.62% | +7.12 |
| `MT<-MT:Đà Nẵng:G2#1:P5P4` | W-1 | 180 | 52 | 55.8% | +19.77 | 9.62% | +7.12 |
| `MT<-MT:Đà Nẵng:G1#1:P3P4` | D-2 | 180 | 51 | 45.1% | +14.69 | 11.76% | +9.80 |
| `MT<-MT:Huế:G5#1:SECOND_HEAD_TAIL` | D-4 | 180 | 31 | 54.8% | +17.87 | 9.68% | +7.19 |
| `MT<-MT:Huế:G1#1:SECOND_HEAD_TAIL` | W-4 | 180 | 36 | 50.0% | +14.14 | 11.11% | +8.58 |
| `MT<-MT:Huế:G1#1:P2P5` | W-4 | 180 | 36 | 50.0% | +14.14 | 11.11% | +8.58 |
| `MT<-MT:Khánh Hòa:DB#1:LAST2` | W-4 | 180 | 52 | 44.2% | +8.75 | 13.46% | +10.96 |
| `MT<-MT:Khánh Hòa:DB#1:P5P6` | W-4 | 180 | 52 | 44.2% | +8.75 | 13.46% | +10.96 |
| `MT<-MB:MB_BOARD:DB#1:P2P3` | D-6 | 60 | 60 | 46.7% | +11.10 | 10.00% | +7.55 |
| `MT<-MT:Đà Nẵng:G8#1:LAST2_REV` | W-4 | 180 | 52 | 50.0% | +14.00 | 7.69% | +5.19 |
| `MT<-MT:Đà Nẵng:G8#1:FIRST2_REV` | W-4 | 180 | 52 | 50.0% | +14.00 | 7.69% | +5.19 |
| `MT<-MT:Đà Nẵng:G8#1:TAIL_HEAD` | W-4 | 180 | 52 | 50.0% | +14.00 | 7.69% | +5.19 |
| `MT<-MT:Đà Nẵng:G8#1:P2P1` | W-4 | 180 | 52 | 50.0% | +14.00 | 7.69% | +5.19 |
| `MT<-MB:MB_BOARD:G1#1:P5P2` | D-1 | 60 | 60 | 45.0% | +9.43 | 10.00% | +7.55 |

### TARGET MB

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MB<-MT:Khánh Hòa:G2#1:P5P2` | D-3 | 180 | 51 | 37.3% | +13.25 | 5.88% | +4.88 |
| `MB<-MT:Đà Nẵng:G2#1:P3P2` | W-3 | 180 | 51 | 33.3% | +9.33 | 5.88% | +4.88 |
| `MB<-MB:MB_BOARD:G2#1:P3P5` | W-4 | 60 | 60 | 31.7% | +8.03 | 6.67% | +5.67 |

## 4. Top 10 H1 LOOSE overall per target

### TARGET MN

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MN<-MT:Đà Nẵng:G1#1:SECOND_HEAD_TAIL` | W-2 | 180 | 52 | 71.2% | +24.50 | 3.85% | +0.40 |
| `MN<-MT:Đà Nẵng:G1#1:P2P5` | W-2 | 180 | 52 | 71.2% | +24.50 | 3.85% | +0.40 |
| `MN<-MT:Đà Nẵng:G2#1:TAIL_HEAD` | D-4 | 180 | 52 | 63.5% | +21.50 | 7.69% | +4.75 |
| `MN<-MT:Đà Nẵng:G2#1:P3P4` | D-6 | 180 | 51 | 62.7% | +20.86 | 1.96% | -1.04 |
| `MN<-MT:Khánh Hòa:DB#1:TAIL_HEAD` | W-3 | 180 | 52 | 61.5% | +19.58 | 5.77% | +2.83 |
| `MN<-MN:TP. HCM:G5#1:LAST2` | D-6 | 180 | 52 | 61.5% | +19.37 | 3.85% | +0.88 |
| `MN<-MN:TP. HCM:G5#1:P3P4` | D-6 | 180 | 52 | 61.5% | +19.37 | 3.85% | +0.88 |
| `MN<-MT:Đà Nẵng:G2#1:P5P4` | D-6 | 180 | 51 | 60.8% | +18.90 | 5.88% | +2.88 |
| `MN<-MT:Đà Nẵng:G2#1:LAST2_REV` | D-6 | 180 | 51 | 60.8% | +18.90 | 5.88% | +2.88 |
| `MN<-MT:Khánh Hòa:DB#1:LAST2_REV` | D-1 | 180 | 51 | 60.8% | +18.80 | 3.92% | +0.92 |

### TARGET MT

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MT<-MT:Huế:DB#1:P4P1` | D-4 | 180 | 31 | 64.5% | +27.55 | 9.68% | +7.19 |
| `MT<-MT:Huế:G1#1:LAST2_REV` | D-3 | 180 | 31 | 58.1% | +23.10 | 6.45% | +4.00 |
| `MT<-MT:Huế:G1#1:P5P4` | D-3 | 180 | 31 | 58.1% | +23.10 | 6.45% | +4.00 |
| `MT<-MT:Huế:G7#1:LAST2_REV` | D-3 | 180 | 31 | 58.1% | +23.10 | 0.00% | -2.45 |
| `MT<-MT:Huế:G7#1:P3P2` | D-3 | 180 | 31 | 58.1% | +23.10 | 0.00% | -2.45 |
| `MT<-MT:Huế:DB#1:P2P3` | D-6 | 180 | 31 | 64.5% | +22.87 | 6.45% | +3.45 |
| `MT<-MT:Khánh Hòa:G2#1:P4P3` | W-3 | 180 | 52 | 57.7% | +22.21 | 1.92% | -0.58 |
| `MT<-MT:Khánh Hòa:G7#1:LAST2` | D-3 | 180 | 52 | 57.7% | +21.69 | 0.00% | -2.50 |
| `MT<-MT:Khánh Hòa:G7#1:SECOND_HEAD_TAIL` | D-3 | 180 | 52 | 57.7% | +21.69 | 0.00% | -2.50 |
| `MT<-MT:Khánh Hòa:G7#1:P2P3` | D-3 | 180 | 52 | 57.7% | +21.69 | 0.00% | -2.50 |

### TARGET MB

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MB<-MT:Đà Nẵng:G2#1:HEAD_SECOND_LAST` | D-1 | 180 | 51 | 43.1% | +19.47 | 3.92% | +2.94 |
| `MB<-MT:Đà Nẵng:G5#1:P4P3` | D-4 | 180 | 51 | 43.1% | +19.24 | 3.92% | +2.92 |
| `MB<-MT:Đà Nẵng:G5#1:LAST2_REV` | D-4 | 180 | 51 | 43.1% | +19.24 | 3.92% | +2.92 |
| `MB<-MT:Đà Nẵng:G1#1:P2P1` | W-1 | 180 | 51 | 41.2% | +17.18 | 1.96% | +0.96 |
| `MB<-MT:Đà Nẵng:G1#1:FIRST2_REV` | W-1 | 180 | 51 | 41.2% | +17.18 | 1.96% | +0.96 |
| `MB<-MT:Khánh Hòa:DB#1:P3P4` | D-3 | 180 | 51 | 41.2% | +17.18 | 1.96% | +0.96 |
| `MB<-MB:MB_BOARD:G2#2:P5P3` | W-2 | 60 | 60 | 40.0% | +16.37 | 5.00% | +4.00 |
| `MB<-MB:MB_BOARD:DB#1:P3P4` | D-2 | 60 | 60 | 40.0% | +16.37 | 0.00% | -1.00 |
| `MB<-MT:Đà Nẵng:DB#1:HEAD_SECOND_LAST` | D-3 | 180 | 50 | 40.0% | +16.14 | 0.00% | -1.00 |
| `MB<-MT:Đà Nẵng:G1#1:P3P2` | D-6 | 180 | 50 | 40.0% | +16.06 | 0.00% | -1.00 |

## 5. Top 10 H2 STRICT-DB overall per target (DB direct match)

### TARGET MN

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MN<-MT:Đà Nẵng:G1#1:SECOND_HEAD_TAIL` | D-2 | 180 | 51 | 52.9% | +10.67 | 15.69% | +12.69 |
| `MN<-MT:Đà Nẵng:G1#1:P2P5` | D-2 | 180 | 51 | 52.9% | +10.67 | 15.69% | +12.69 |
| `MN<-MT:Khánh Hòa:G7#1:HEAD_TAIL` | D-5 | 180 | 51 | 43.1% | +0.86 | 13.73% | +10.73 |
| `MN<-MT:Đà Nẵng:G1#1:P4P3` | D-5 | 180 | 51 | 35.3% | -6.69 | 13.73% | +10.73 |
| `MN<-MT:Đà Nẵng:DB#1:P5P2` | W-1 | 180 | 52 | 48.1% | +1.42 | 13.46% | +10.02 |
| `MN<-MN:TP. HCM:G5#1:TAIL_HEAD` | D-1 | 180 | 51 | 41.2% | -0.41 | 11.76% | +8.80 |
| `MN<-MN:TP. HCM:G5#1:P4P1` | D-1 | 180 | 51 | 41.2% | -0.41 | 11.76% | +8.80 |
| `MN<-MN:TP. HCM:DB#1:P6P4` | D-1 | 180 | 51 | 41.2% | -0.41 | 11.76% | +8.80 |
| `MN<-MT:Khánh Hòa:G7#1:LAST2` | D-5 | 180 | 51 | 51.0% | +8.71 | 11.76% | +8.76 |
| `MN<-MT:Khánh Hòa:G7#1:SECOND_HEAD_TAIL` | D-5 | 180 | 51 | 51.0% | +8.71 | 11.76% | +8.76 |

### TARGET MT

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MT<-MT:Khánh Hòa:DB#1:LAST2` | W-4 | 180 | 52 | 44.2% | +8.75 | 13.46% | +10.96 |
| `MT<-MT:Khánh Hòa:DB#1:P5P6` | W-4 | 180 | 52 | 44.2% | +8.75 | 13.46% | +10.96 |
| `MT<-MT:Huế:DB#1:LAST2_REV` | D-3 | 180 | 31 | 35.5% | +0.52 | 12.90% | +10.45 |
| `MT<-MT:Huế:DB#1:P6P5` | D-3 | 180 | 31 | 35.5% | +0.52 | 12.90% | +10.45 |
| `MT<-MT:Huế:DB#1:P5P2` | D-4 | 180 | 31 | 38.7% | +1.74 | 12.90% | +10.42 |
| `MT<-MT:Huế:G2#1:HEAD_SECOND_LAST` | W-1 | 180 | 31 | 32.3% | -4.13 | 12.90% | +10.35 |
| `MT<-MT:Huế:G2#1:P1P4` | W-1 | 180 | 31 | 32.3% | -4.13 | 12.90% | +10.35 |
| `MT<-MT:Đà Nẵng:G1#1:P3P4` | D-2 | 180 | 51 | 45.1% | +14.69 | 11.76% | +9.80 |
| `MT<-MT:Huế:G5#1:LAST2_REV` | W-3 | 180 | 34 | 38.2% | +2.09 | 11.76% | +9.24 |
| `MT<-MT:Huế:G5#1:P4P3` | W-3 | 180 | 34 | 38.2% | +2.09 | 11.76% | +9.24 |

### TARGET MB

| Rule | Axis | W | Days | H1 hit% | H1 lift | H2 hit% | H2 lift |
|---|---|---:|---:|---:|---:|---:|---:|
| `MB<-MT:Khánh Hòa:DB#1:P3P4` | D-1 | 180 | 49 | 30.6% | +6.98 | 8.16% | +7.18 |
| `MB<-MT:Đà Nẵng:G2#1:TAIL_HEAD` | D-5 | 180 | 49 | 28.6% | +4.94 | 8.16% | +7.18 |
| `MB<-MT:Đà Nẵng:G2#1:P2P1` | D-5 | 180 | 49 | 18.4% | -5.27 | 8.16% | +7.18 |
| `MB<-MT:Đà Nẵng:G2#1:FIRST2_REV` | D-5 | 180 | 49 | 18.4% | -5.27 | 8.16% | +7.18 |
| `MB<-MT:Khánh Hòa:G1#1:P2P1` | W-2 | 180 | 51 | 31.4% | +7.47 | 7.84% | +6.84 |
| `MB<-MT:Khánh Hòa:G1#1:FIRST2_REV` | W-2 | 180 | 51 | 31.4% | +7.47 | 7.84% | +6.84 |
| `MB<-MB:MB_BOARD:G2#1:P3P5` | W-4 | 60 | 60 | 31.7% | +8.03 | 6.67% | +5.67 |
| `MB<-MB:MB_BOARD:G2#1:TAIL_HEAD` | W-4 | 60 | 60 | 26.7% | +3.03 | 6.67% | +5.67 |
| `MB<-MB:MB_BOARD:G2#1:P5P1` | W-4 | 60 | 60 | 26.7% | +3.03 | 6.67% | +5.67 |
| `MB<-MB:MB_BOARD:DB#1:P1P3` | D-1 | 60 | 60 | 25.0% | +1.37 | 6.67% | +5.67 |

## 6. Top 3 rule moi NHAT theo TUNG GIAI (per target)

### TARGET MN

**Prize G8** (giai G8):

Top H1 (recall):
- `MN<-MT:Đà Nẵng:G8#1:FIRST2 W-4 w180` days=52 H1=+14.88pp H2=+2.33pp
- `MN<-MT:Đà Nẵng:G8#1:HEAD_TAIL W-4 w180` days=52 H1=+14.88pp H2=+2.33pp
- `MN<-MT:Đà Nẵng:G8#1:LAST2 W-4 w180` days=52 H1=+14.88pp H2=+2.33pp

Top H2 (DB strict):
- `MN<-MT:Khánh Hòa:G8#1:LAST2_REV D-1 w180` days=51 H1=+7.04pp H2=+4.84pp
- `MN<-MT:Khánh Hòa:G8#1:P2P1 D-1 w180` days=51 H1=+7.04pp H2=+4.84pp
- `MN<-MT:Khánh Hòa:G8#1:FIRST2_REV D-1 w180` days=51 H1=+7.04pp H2=+4.84pp

**Prize G7** (giai G7):

Top H1 (recall):
- `MN<-MN:TP. HCM:G7#1:LAST2_REV W-4 w180` days=51 H1=+15.98pp H2=-3.47pp
- `MN<-MN:TP. HCM:G7#1:P3P2 W-4 w180` days=51 H1=+15.98pp H2=-3.47pp
- `MN<-MT:Đà Nẵng:G7#1:TAIL_HEAD W-3 w180` days=52 H1=+14.88pp H2=+6.17pp

Top H2 (DB strict):
- `MN<-MT:Khánh Hòa:G7#1:HEAD_TAIL D-5 w180` days=51 H1=+0.86pp H2=+10.73pp
- `MN<-MT:Khánh Hòa:G7#1:LAST2 D-5 w180` days=51 H1=+8.71pp H2=+8.76pp
- `MN<-MT:Khánh Hòa:G7#1:SECOND_HEAD_TAIL D-5 w180` days=51 H1=+8.71pp H2=+8.76pp

**Prize G5** (giai G5):

Top H1 (recall):
- `MN<-MN:TP. HCM:G5#1:LAST2 D-6 w180` days=52 H1=+19.37pp H2=+0.88pp
- `MN<-MN:TP. HCM:G5#1:P3P4 D-6 w180` days=52 H1=+19.37pp H2=+0.88pp
- `MN<-MN:TP. HCM:G5#1:FIRST2_REV D-2 w180` days=51 H1=+18.73pp H2=+0.94pp

Top H2 (DB strict):
- `MN<-MN:TP. HCM:G5#1:TAIL_HEAD D-1 w180` days=51 H1=-0.41pp H2=+8.80pp
- `MN<-MN:TP. HCM:G5#1:P4P1 D-1 w180` days=51 H1=-0.41pp H2=+8.80pp
- `MN<-MT:Đà Nẵng:G5#1:P4P3 D-2 w180` days=51 H1=-8.94pp H2=+6.80pp

**Prize G2** (giai G2):

Top H1 (recall):
- `MN<-MT:Đà Nẵng:G2#1:TAIL_HEAD D-4 w180` days=52 H1=+21.50pp H2=+4.75pp
- `MN<-MT:Đà Nẵng:G2#1:P3P4 D-6 w180` days=51 H1=+20.86pp H2=-1.04pp
- `MN<-MT:Đà Nẵng:G2#1:P5P4 D-6 w180` days=51 H1=+18.90pp H2=+2.88pp

Top H2 (DB strict):
- `MN<-MN:TP. HCM:G2#1:P3P5 D-4 w180` days=52 H1=-3.79pp H2=+8.56pp
- `MN<-MB:MB_BOARD:G2#2:FIRST2_REV W-2 w60` days=60 H1=+18.33pp H2=+8.52pp
- `MN<-MB:MB_BOARD:G2#2:P2P1 W-2 w60` days=60 H1=+18.33pp H2=+8.52pp

**Prize G1** (giai G1):

Top H1 (recall):
- `MN<-MT:Đà Nẵng:G1#1:SECOND_HEAD_TAIL W-2 w180` days=52 H1=+24.50pp H2=+0.40pp
- `MN<-MT:Đà Nẵng:G1#1:P2P5 W-2 w180` days=52 H1=+24.50pp H2=+0.40pp
- `MN<-MT:Khánh Hòa:G1#1:LAST2_REV D-6 w180` days=51 H1=+18.33pp H2=+0.45pp

Top H2 (DB strict):
- `MN<-MT:Đà Nẵng:G1#1:SECOND_HEAD_TAIL D-2 w180` days=51 H1=+10.67pp H2=+12.69pp
- `MN<-MT:Đà Nẵng:G1#1:P2P5 D-2 w180` days=51 H1=+10.67pp H2=+12.69pp
- `MN<-MT:Đà Nẵng:G1#1:P4P3 D-5 w180` days=51 H1=-6.69pp H2=+10.73pp

**Prize DB** (giai DB):

Top H1 (recall):
- `MN<-MT:Khánh Hòa:DB#1:TAIL_HEAD W-3 w180` days=52 H1=+19.58pp H2=+2.83pp
- `MN<-MT:Khánh Hòa:DB#1:LAST2_REV D-1 w180` days=51 H1=+18.80pp H2=+0.92pp
- `MN<-MT:Đà Nẵng:DB#1:P1P2 W-2 w180` days=52 H1=+18.73pp H2=-1.52pp

Top H2 (DB strict):
- `MN<-MT:Đà Nẵng:DB#1:P5P2 W-1 w180` days=52 H1=+1.42pp H2=+10.02pp
- `MN<-MN:TP. HCM:DB#1:P6P4 D-1 w180` days=51 H1=-0.41pp H2=+8.80pp
- `MN<-MT:Đà Nẵng:DB#1:HEAD_TAIL D-5 w180` days=51 H1=+1.16pp H2=+8.76pp

### TARGET MT

**Prize G8** (giai G8):

Top H1 (recall):
- `MT<-MT:Huế:G8#1:LAST2 W-4 w180` days=36 H1=+19.69pp H2=+0.25pp
- `MT<-MT:Huế:G8#1:FIRST2 W-4 w180` days=36 H1=+19.69pp H2=+0.25pp
- `MT<-MT:Huế:G8#1:HEAD_TAIL W-4 w180` days=36 H1=+19.69pp H2=+0.25pp

Top H2 (DB strict):
- `MT<-MT:Đà Nẵng:G8#1:LAST2_REV W-4 w180` days=52 H1=+14.00pp H2=+5.19pp
- `MT<-MT:Đà Nẵng:G8#1:FIRST2_REV W-4 w180` days=52 H1=+14.00pp H2=+5.19pp
- `MT<-MT:Đà Nẵng:G8#1:TAIL_HEAD W-4 w180` days=52 H1=+14.00pp H2=+5.19pp

**Prize G7** (giai G7):

Top H1 (recall):
- `MT<-MT:Huế:G7#1:LAST2_REV D-3 w180` days=31 H1=+23.10pp H2=-2.45pp
- `MT<-MT:Huế:G7#1:P3P2 D-3 w180` days=31 H1=+23.10pp H2=-2.45pp
- `MT<-MT:Khánh Hòa:G7#1:LAST2 D-3 w180` days=52 H1=+21.69pp H2=-2.50pp

Top H2 (DB strict):
- `MT<-MT:Đà Nẵng:G7#1:LAST2_REV D-1 w180` days=52 H1=+4.90pp H2=+6.62pp
- `MT<-MT:Đà Nẵng:G7#1:P3P2 D-1 w180` days=52 H1=+4.90pp H2=+6.62pp
- `MT<-MT:Khánh Hòa:G7#1:LAST2 D-2 w180` days=51 H1=-3.02pp H2=+5.88pp

**Prize G5** (giai G5):

Top H1 (recall):
- `MT<-MT:Huế:G5#1:HEAD_TAIL W-3 w180` days=34 H1=+19.74pp H2=+3.35pp
- `MT<-MT:Huế:G5#1:P1P4 W-3 w180` days=34 H1=+19.74pp H2=+3.35pp
- `MT<-MT:Huế:G5#1:LAST2 D-5 w180` days=31 H1=+18.97pp H2=-2.39pp

Top H2 (DB strict):
- `MT<-MT:Huế:G5#1:LAST2_REV W-3 w180` days=34 H1=+2.09pp H2=+9.24pp
- `MT<-MT:Huế:G5#1:P4P3 W-3 w180` days=34 H1=+2.09pp H2=+9.24pp
- `MT<-MT:Huế:G5#1:FIRST2 W-3 w180` days=34 H1=-0.85pp H2=+9.24pp

**Prize G2** (giai G2):

Top H1 (recall):
- `MT<-MT:Khánh Hòa:G2#1:P4P3 W-3 w180` days=52 H1=+22.21pp H2=-0.58pp
- `MT<-MB:MB_BOARD:G2#2:SECOND_HEAD_TAIL W-1 w60` days=60 H1=+21.10pp H2=+0.88pp
- `MT<-MB:MB_BOARD:G2#2:P2P5 W-1 w60` days=60 H1=+21.10pp H2=+0.88pp

Top H2 (DB strict):
- `MT<-MT:Huế:G2#1:HEAD_SECOND_LAST W-1 w180` days=31 H1=-4.13pp H2=+10.35pp
- `MT<-MT:Huế:G2#1:P1P4 W-1 w180` days=31 H1=-4.13pp H2=+10.35pp
- `MT<-MB:MB_BOARD:G2#1:P5P2 W-1 w60` days=60 H1=+4.43pp H2=+9.22pp

**Prize G1** (giai G1):

Top H1 (recall):
- `MT<-MT:Huế:G1#1:LAST2_REV D-3 w180` days=31 H1=+23.10pp H2=+4.00pp
- `MT<-MT:Huế:G1#1:P5P4 D-3 w180` days=31 H1=+23.10pp H2=+4.00pp
- `MT<-MT:Huế:G1#1:SECOND_HEAD_TAIL D-4 w180` days=31 H1=+21.10pp H2=+3.97pp

Top H2 (DB strict):
- `MT<-MT:Đà Nẵng:G1#1:P3P4 D-2 w180` days=51 H1=+14.69pp H2=+9.80pp
- `MT<-MT:Huế:G1#1:SECOND_HEAD_TAIL W-4 w180` days=36 H1=+14.14pp H2=+8.58pp
- `MT<-MT:Huế:G1#1:P2P5 W-4 w180` days=36 H1=+14.14pp H2=+8.58pp

**Prize DB** (giai DB):

Top H1 (recall):
- `MT<-MT:Huế:DB#1:P4P1 D-4 w180` days=31 H1=+27.55pp H2=+7.19pp
- `MT<-MT:Huế:DB#1:P2P3 D-6 w180` days=31 H1=+22.87pp H2=+3.45pp
- `MT<-MT:Khánh Hòa:DB#1:P3P2 D-1 w180` days=51 H1=+20.82pp H2=+1.41pp

Top H2 (DB strict):
- `MT<-MT:Khánh Hòa:DB#1:LAST2 W-4 w180` days=52 H1=+8.75pp H2=+10.96pp
- `MT<-MT:Khánh Hòa:DB#1:P5P6 W-4 w180` days=52 H1=+8.75pp H2=+10.96pp
- `MT<-MT:Huế:DB#1:LAST2_REV D-3 w180` days=31 H1=+0.52pp H2=+10.45pp

### TARGET MB

**Prize G8** (giai G8):

Top H1 (recall):
- `MB<-MT:Đà Nẵng:G8#1:FIRST2 D-5 w180` days=49 H1=+13.10pp H2=-0.98pp
- `MB<-MT:Đà Nẵng:G8#1:HEAD_TAIL D-5 w180` days=49 H1=+13.10pp H2=-0.98pp
- `MB<-MT:Đà Nẵng:G8#1:LAST2 D-5 w180` days=49 H1=+13.10pp H2=-0.98pp

Top H2 (DB strict):
- `MB<-MT:Khánh Hòa:G8#1:LAST2_REV D-1 w180` days=49 H1=-1.18pp H2=+1.06pp
- `MB<-MT:Khánh Hòa:G8#1:P2P1 D-1 w180` days=49 H1=-1.18pp H2=+1.06pp
- `MB<-MT:Khánh Hòa:G8#1:FIRST2_REV D-1 w180` days=49 H1=-1.18pp H2=+1.06pp

**Prize G7** (giai G7):

Top H1 (recall):
- `MB<-MT:Đà Nẵng:G7#1:TAIL_HEAD D-2 w180` days=50 H1=+11.92pp H2=-1.00pp
- `MB<-MT:Khánh Hòa:G7#1:P2P1 W-1 w180` days=51 H1=+11.39pp H2=-1.00pp
- `MB<-MT:Khánh Hòa:G7#1:FIRST2_REV W-1 w180` days=51 H1=+11.39pp H2=-1.00pp

Top H2 (DB strict):
- `MB<-MT:Đà Nẵng:G7#1:HEAD_SECOND_LAST D-3 w180` days=50 H1=+6.14pp H2=+3.00pp
- `MB<-MT:Đà Nẵng:G7#1:FIRST2 D-3 w180` days=50 H1=+6.14pp H2=+3.00pp
- `MB<-MT:Đà Nẵng:G7#1:P1P2 D-3 w180` days=50 H1=+6.14pp H2=+3.00pp

**Prize G5** (giai G5):

Top H1 (recall):
- `MB<-MT:Đà Nẵng:G5#1:P4P3 D-4 w180` days=51 H1=+19.24pp H2=+2.92pp
- `MB<-MT:Đà Nẵng:G5#1:LAST2_REV D-4 w180` days=51 H1=+19.24pp H2=+2.92pp
- `MB<-MT:Đà Nẵng:G5#1:HEAD_TAIL D-1 w180` days=51 H1=+13.59pp H2=-0.98pp

Top H2 (DB strict):
- `MB<-MT:Đà Nẵng:G5#1:HEAD_SECOND_LAST D-2 w180` days=50 H1=-4.08pp H2=+5.00pp
- `MB<-MT:Khánh Hòa:G5#1:HEAD_SECOND_LAST D-4 w180` days=51 H1=+3.78pp H2=+4.90pp
- `MB<-MT:Khánh Hòa:G5#1:HEAD_SECOND_LAST D-1 w180` days=49 H1=+9.02pp H2=+3.10pp

**Prize G2** (giai G2):

Top H1 (recall):
- `MB<-MT:Đà Nẵng:G2#1:HEAD_SECOND_LAST D-1 w180` days=51 H1=+19.47pp H2=+2.94pp
- `MB<-MB:MB_BOARD:G2#2:P5P3 W-2 w60` days=60 H1=+16.37pp H2=+4.00pp
- `MB<-MT:Khánh Hòa:G2#1:FIRST2 W-4 w180` days=51 H1=+15.31pp H2=+0.96pp

Top H2 (DB strict):
- `MB<-MT:Đà Nẵng:G2#1:TAIL_HEAD D-5 w180` days=49 H1=+4.94pp H2=+7.18pp
- `MB<-MT:Đà Nẵng:G2#1:P2P1 D-5 w180` days=49 H1=-5.27pp H2=+7.18pp
- `MB<-MT:Đà Nẵng:G2#1:FIRST2_REV D-5 w180` days=49 H1=-5.27pp H2=+7.18pp

**Prize G1** (giai G1):

Top H1 (recall):
- `MB<-MT:Đà Nẵng:G1#1:P2P1 W-1 w180` days=51 H1=+17.18pp H2=+0.96pp
- `MB<-MT:Đà Nẵng:G1#1:FIRST2_REV W-1 w180` days=51 H1=+17.18pp H2=+0.96pp
- `MB<-MT:Đà Nẵng:G1#1:P3P2 D-6 w180` days=50 H1=+16.06pp H2=-1.00pp

Top H2 (DB strict):
- `MB<-MT:Khánh Hòa:G1#1:P2P1 W-2 w180` days=51 H1=+7.47pp H2=+6.84pp
- `MB<-MT:Khánh Hòa:G1#1:FIRST2_REV W-2 w180` days=51 H1=+7.47pp H2=+6.84pp
- `MB<-MT:Đà Nẵng:G1#1:TAIL_HEAD W-3 w180` days=51 H1=+3.45pp H2=+4.88pp

**Prize DB** (giai DB):

Top H1 (recall):
- `MB<-MT:Khánh Hòa:DB#1:P3P4 D-3 w180` days=51 H1=+17.18pp H2=+0.96pp
- `MB<-MB:MB_BOARD:DB#1:P3P4 D-2 w60` days=60 H1=+16.37pp H2=-1.00pp
- `MB<-MT:Đà Nẵng:DB#1:HEAD_SECOND_LAST D-3 w180` days=50 H1=+16.14pp H2=-1.00pp

Top H2 (DB strict):
- `MB<-MT:Khánh Hòa:DB#1:P3P4 D-1 w180` days=49 H1=+6.98pp H2=+7.18pp
- `MB<-MB:MB_BOARD:DB#1:P1P3 D-1 w60` days=60 H1=+1.37pp H2=+5.67pp
- `MB<-MT:Khánh Hòa:DB#1:TAIL_HEAD D-2 w180` days=50 H1=-1.94pp H2=+5.00pp

## 7. Pattern lon — Tong hop phat hien

### 7.1 MT-Huế va MT-Khánh Hòa la HAI source manh nhat overall

- **MT<-MT:Huế:G7#1:LAST2_REV:D-3** H1 +23.1pp (31d) — gia mien Trung Hue lag 3 ngay dao 2 so cuoi
- **MT<-MT:Khánh Hòa:G7#1:LAST2:D-3** H1 +21.7pp (52d)
- **MT<-MT:Khánh Hòa:DB#1:LAST2:W-4** H1 +8.8pp + **H2 +10.96pp** — DB-to-DB rat manh
- **MT<-MT:Huế:DB#1:LAST2_REV:D-3** H2 +10.45pp — DB-to-DB lag 3 ngay dao
- **MT<-MT:Huế:G8#1:LAST2:W-4** H1 +19.7pp — G8 chu ky 4 tuan

### 7.2 TP.HCM (MN) W-4 chu ky chinh xac cho DB

- **MN<-MN:TP. HCM:G7#1:FIRST2_REV:W-4** H1 +10.1pp + H2 +8.29pp
- **MN<-MN:TP. HCM:G2#1:P4P1:W-1** H2 +8.29pp
- **MN<-MN:TP. HCM:G5#1:TAIL_HEAD:D-1** H2 +8.80pp
- **MN<-MN:TP. HCM:DB#1:P6P4:D-1** H2 +8.80pp

### 7.3 MT Đà Nẵng G1 D-2 P3P4 — DOUBLE STRONG cho ca MN va MT

- **MN<-MT:Đà Nẵng:G1#1:SECOND_HEAD_TAIL:D-2** H1 +10.7pp + **H2 +12.69pp** ★★ (51d)
- **MT<-MT:Đà Nẵng:G1#1:P3P4:D-2** H1 +14.7pp + **H2 +9.80pp** ★★ (51d)

→ Day la rule manh nhat lan cho MN va MT, cung source MT Đà Nẵng G1 D-2.

### 7.4 G8 (2 chu so) precision phong phu

G8 chi co 2 chu so → transform LAST2/FIRST2/HEAD_TAIL/P1P2 deu = G8 chinh. Chi 2 candidate distinct moi ngay (G8 va G8 reversed).
- **MT<-MT:Huế:G8#1:LAST2:W-4** H1 +19.7pp (36d) — recall manh
- **MT<-MT:Đà Nẵng:G8#1:LAST2_REV:W-4** H2 +5.19pp
- **MN<-MT:Đà Nẵng:G8#1:LAST2:W-4** H1 +14.9pp
- **MN<-MT:Khánh Hòa:G8#1:LAST2_REV:D-1** H2 +4.84pp

### 7.5 MB DB W-3 chu ky

- **MB<-MB:MB_BOARD:DB#1:HEAD_TAIL:W-3** H2 +4.00pp
- **MB<-MB:MB_BOARD:DB#1:P1P3:D-1** H2 +5.67pp
- **MB<-MT:Khánh Hòa:DB#1:P3P4:D-1** H1 +7.0pp + H2 +7.18pp

### 7.6 MT-Hue G1 SECOND_HEAD_TAIL W-4 H2

- **MT<-MT:Huế:G1#1:SECOND_HEAD_TAIL:W-4** H1 +14.1pp + H2 +8.58pp (36d)
- **MT<-MT:Huế:G1#1:P2P5:W-4** (cung gia tri) H1 +14.1pp + H2 +8.58pp

### 7.7 G7 cua MT-Khanh Hoa la "vang" cho DB strict

- **MN<-MT:Khánh Hòa:G7#1:HEAD_TAIL:D-5** H2 +10.73pp
- **MN<-MT:Khánh Hòa:G7#1:LAST2:D-5** H2 +8.76pp
- **MT<-MT:Khánh Hòa:G7#1:P3P4:W-2** H2 +9.97pp (H1 -7.6 → DB-only)

## 8. So sanh voi tat ca pass truoc

| Pass | Scope | Top H1 lift | Top H2 lift | Note |
|---|---|---:|---:|---|
| V10605 | MT<-MB only, G2/DB/G1 4 prize | ~ +14pp | N/A | Original MB→MT |
| V10606 | All targets x MB/MN/MT, MB/G1/G2#1/G2#2 | +61.4pp | N/A | Deep mining |
| V10626 FU1 | MB DB D-2 verify | -5 → +1pp | -0.4pp | Owner hypothesis FAILED |
| V10626 FU2 | Comprehensive cross-source (incorrect G8 schema) | +26pp | +12pp | Some labels wrong |
| **V10626 FU3** | **Full + key-name fix + G8/G7/G5** | **+23.1pp** | **+12.69pp** | **Schema-safe, broader prize coverage** |

## 9. Cap nhat de xuat panel PRE_REGISTER (DOI ANH XAC NHAN)

### MN panel — them 6 rule moi
1. `MN<-MT:Đà Nẵng:G1#1:SECOND_HEAD_TAIL:D-2` — H1 +10.7 + H2 +12.69 ★★ (51d)
2. `MN<-MT:Đà Nẵng:G1#1:P2P5:D-2` — same value as above
3. `MN<-MN:TP. HCM:G7#1:FIRST2_REV:W-4` — H1 +10.1 + H2 +8.29 (51d)
4. `MN<-MT:Khánh Hòa:G7#1:LAST2:D-5` — H2 +8.76 + H1 +8.7 (51d)
5. `MN<-MT:Đà Nẵng:DB#1:P5P2:W-1` — H2 +10.02 (52d)
6. `MN<-MN:TP. HCM:G5#1:TAIL_HEAD:D-1` — H2 +8.80 (51d)

### MT panel — them 8 rule moi
1. `MT<-MT:Khánh Hòa:DB#1:LAST2:W-4` — H1 +8.8 + H2 +10.96 ★ (52d)
2. `MT<-MT:Đà Nẵng:G1#1:P3P4:D-2` — H1 +14.7 + H2 +9.80 ★★ (51d)
3. `MT<-MT:Huế:G7#1:LAST2_REV:D-3` — H1 +23.1 (31d) cao nhat MT
4. `MT<-MT:Huế:DB#1:LAST2_REV:D-3` — H2 +10.45 (31d)
5. `MT<-MT:Huế:G1#1:SECOND_HEAD_TAIL:W-4` — H1 +14.1 + H2 +8.58 (36d)
6. `MT<-MT:Huế:G8#1:LAST2:W-4` — H1 +19.7 (36d)
7. `MT<-MT:Đà Nẵng:G8#1:LAST2_REV:W-4` — H1 +14.0 + H2 +5.19 (52d)
8. `MT<-MT:Khánh Hòa:G7#1:LAST2:D-3` — H1 +21.7 (52d)

### MB panel — them 5 rule moi
1. `MB<-MT:Khánh Hòa:DB#1:P3P4:D-1` — H1 +7.0 + H2 +7.18 (49d)
2. `MB<-MT:Đà Nẵng:G2#1:TAIL_HEAD:D-5` — H1 +4.9 + H2 +7.18 (49d)
3. `MB<-MT:Khánh Hòa:G1#1:P2P1:W-2` — H1 +7.5 + H2 +6.84 (51d)
4. `MB<-MB:MB_BOARD:DB#1:P1P3:D-1` — H2 +5.67 (60d)
5. `MB<-MB:MB_BOARD:G2#1:P3P5:W-4` — H1 +8.0 + H2 +5.67 (60d)

## 10. Hard safety

| Item | Value |
|---|---|
| Official mutation | 0 |
| Provider/manual AI call | 0 |
| Wallet | 0 |
| Lane promotion | 0 |
| Public push | NO |
| Live application | 0 |
| Broad selector | 0 |
| V107 risk overlay | active |
| live_eligible | False |
| Status | PRE_REGISTER_ONLY |

## 11. Owner decisions (DOI ANH)

- **(A)** Em them 19 rule moi (6 MN + 8 MT + 5 MB) vao pre-register panel? PRE_REGISTER_ONLY, khong live.
- **(B)** Khoa panel timestamp `2026-05-25` lam baseline 90-day forward audit?
- **(C)** Mo pass rieng kiem tra:
  - MT-Huế va MT-Khánh Hòa la 2 source manh nhat — co the dao sau theo weekday/thu trong tuan
  - TP.HCM W-4 chu ky DB-precision cao
  - MT-Đà Nẵng G1 D-2 P3P4 — rule manh nhat cho ca MN va MT, can verify forward
- **(D)** Private commit `V20.3.37.106.26.2: FU full key-name fix + comprehensive low-prize findings`? Default doi anh OK.
- **(E)** Public push? Default NO.

## 12. Output artifacts

Trong `artifacts/v106_26_followup_mb_db_d2_hypothesis/`:
- `V10626_FU_OWNER_REPORT_VN.md` — FU1 MB DB D-2 verify
- `V10626_FU_COMPREHENSIVE_REPORT_VN.md` — FU2 broader (schema not fixed)
- `V10626_FU_FULL_REPORT_VN.md` — FU3 (file nay, schema-fixed full coverage)
- `machine_readable/V10626_FU_MB_DB_D2_VERIFY.json`
- `machine_readable/V10626_FU_COMPREHENSIVE_SCAN.csv` (FU2 5000)
- `machine_readable/V10626_FU3_KEYNAME_LOW_PRIZE_SCAN.csv` (FU3 6000)
- `machine_readable/V10626_FU3_KEYNAME_LOW_PRIZE_SUMMARY.json`

---

Live snapshot: `artifacts/live_sync/20260524_221208/manifest.json`. Manifest locked. DB read-only. Generated: 2026-05-25T00:21:10.
