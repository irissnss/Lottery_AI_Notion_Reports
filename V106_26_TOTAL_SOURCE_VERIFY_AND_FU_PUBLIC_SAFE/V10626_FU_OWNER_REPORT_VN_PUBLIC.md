# V10626-FU MB DB D-2 Owner Hypothesis Verification & New Findings

> Generated: 2026-05-24T23:34:38
> Locked manifest: `artifacts/live_sync/20260524_221208/manifest.json`
>
> Scope: research-only verification of owner hypothesis "Dich MB D = MB DB D-2" + new findings scan.
> Hard locks active: NO live application, NO official mutation, PRE_REGISTER_ONLY for everything.

## 1. Verify gia thuyet owner: "MB D = MB DB D-2"

Em check theo 2 cach hieu:
- **H1 LOOSE**: 2 so cuoi cua MB DB ngay D-2 co xuat hien o bat ky giai nao cua MB ngay D khong?
- **H2 STRICT**: 2 so cuoi cua MB DB ngay D-2 co bang DUNG 2 so cuoi cua MB DB ngay D khong?

### Ket qua H1 LOOSE

| Window | Days | Hit rate | Baseline | Lift_pp | CI95 | raw_p |
|---|---:|---:|---:|---:|---|---:|
| 30d | 30 | 23.3% | 23.7% | -0.37 | 11.8-40.9% | 0.6033 |
| 60d | 60 | 18.3% | 23.6% | -5.30 | 10.6-29.9% | 0.8683 |
| 90d | 90 | 18.9% | 23.8% | -4.88 | 12.1-28.2% | 0.8870 |
| 180d | 173 | 24.9% | 23.9% | +0.99 | 19.0-31.8% | 0.4139 |
| 365d | 358 | 23.5% | 23.9% | -0.40 | 19.4-28.1% | 0.5941 |

### Ket qua H2 STRICT

| Window | Days | DB-to-DB rate | Baseline | Lift_pp | raw_p |
|---|---:|---:|---:|---:|---:|
| 30d | 30 | 0.00% | 1.00% | -1.00 | 1.0000 |
| 60d | 60 | 0.00% | 1.00% | -1.00 | 1.0000 |
| 90d | 90 | 0.00% | 1.00% | -1.00 | 1.0000 |
| 180d | 173 | 0.58% | 1.00% | -0.42 | 0.8264 |
| 365d | 358 | 1.12% | 1.00% | +0.12 | 0.5169 |

### Ket luan gia thuyet owner

- **H1 LOOSE (LAST2 D-2)**: lift gan zero o 30d/180d/365d (-0.4 -> +1.0 pp), AM nhe o 60d/90d (-5pp). Khong vuot bat ky muc significance nao. raw_p den 0.41 chua tinh BH.
- **H2 STRICT (DB-to-DB D-2)**: 0% match cho 30/60/90d, 0.58% o 180d (baseline 1%), 1.12% o 365d (=baseline). **Khong co tin hieu DB->DB direct.**
- **Ket luan tom tat**: Voi rule chinh xac "MB DB D-2 LAST2 -> MB", **gia thuyet KHONG xac nhan**. Co the case anh nhin la coincidence ngan han.

## 2. Phat hien quan trong khi mo rong sang lag khac va transform khac

### 2.1 Cung LAST2 nhung khac lag (180d, MB self-lag)

| Lag | Days | H1 rate | H1 lift_pp | DB-to-DB | DB lift_pp |
|---|---:|---:|---:|---:|---:|
| 1 | 174 | 21.3% | -2.60 | 0.57% | -0.43 |
| 2 | 173 | 24.9% | +0.99 | 0.58% | -0.42 |
| 3 | 172 | 29.1% | +5.20 | 1.16% | +0.16 |
| 4 | 171 | 22.8% | -1.05 | 0.58% | -0.42 |
| 5 | 171 | 19.3% | -4.55 | 1.17% | +0.17 |
| 6 | 171 | 20.5% | -3.37 | 0.58% | -0.42 |
| 7 | 171 | 25.1% | +1.28 | 0.58% | -0.42 |
| 14 | 171 | 22.2% | -1.65 | 0.58% | -0.42 |
| 21 | 171 | 28.1% | +4.20 | 1.17% | +0.17 |
| 28 | 171 | 30.4% | +6.53 | 1.17% | +0.17 |

**PHAT HIEN MOI**: Khong phai D-2 ma **D-3 (+5.20pp)** va **D-28 = W-4 (+6.53pp)** moi la lag manh nhat cho LAST2 self-lag MB. D-21 = W-3 cung +4.20pp. Day la chu ky 3 tuan / 4 tuan, khong phai 2 ngay.

### 2.2 Cung D-2 nhung doi transform (top 8 theo H1 lift)

| Transform | Days | H1 rate | H1 lift_pp | DB-to-DB | DB lift_pp |
|---|---:|---:|---:|---:|---:|
| SECOND_HEAD_TAIL | 173 | 30.6% | +6.77 | 1.73% | +0.73 |
| P2P5 | 173 | 30.6% | +6.77 | 1.73% | +0.73 |
| P3P5 | 173 | 30.1% | +6.20 | 0.58% | -0.42 |
| P2P3 | 173 | 28.9% | +5.04 | 1.16% | +0.16 |
| HEAD_TAIL | 173 | 28.3% | +4.46 | 1.73% | +0.73 |
| P1P5 | 173 | 28.3% | +4.46 | 1.73% | +0.73 |
| HEAD_SECOND_LAST | 173 | 27.7% | +3.88 | 2.31% | +1.31 |
| P1P4 | 173 | 27.7% | +3.88 | 2.31% | +1.31 |

**PHAT HIEN MOI**: O D-2 thi:
- `SECOND_HEAD_TAIL` (cs2 + cs cuoi) va `P2P5` (cs2 + cs5) deu **+6.77pp**.
- `HEAD_SECOND_LAST` (cs1 + cs ap cuoi) va `P1P4` (cs1 + cs4) cung **+3.88pp** va co DB-to-DB lift **+1.31pp** (manh nhat o DB).

## 3. Lap V10606 gap: MN-self / MT-self DB#1 (V10606 mining khong cover)

Top 10 rule moi theo H1 lift:

| Target | Source | Transform | Lag | Days | H1 rate | H1 lift_pp |
|---|---|---|---:|---:|---:|---:|
| MN | MN-self | P3P4 | 4 | 92 | 51.1% | +7.89 |
| MN | MN-self | TAIL_HEAD | 1 | 180 | 48.9% | +5.60 |
| MT | MT-self | P3P4 | 2 | 82 | 40.2% | +5.24 |
| MN | MN-self | FIRST2 | 2 | 180 | 47.8% | +4.49 |
| MN | MN-self | LAST2 | 7 | 180 | 47.2% | +3.93 |
| MN | MN-self | FIRST2 | 14 | 180 | 46.7% | +3.38 |
| MT | MT-self | LAST2 | 14 | 180 | 38.3% | +3.17 |
| MN | MN-self | TAIL_HEAD | 2 | 180 | 46.1% | +2.82 |
| MN | MN-self | HEAD_TAIL | 7 | 180 | 46.1% | +2.82 |
| MN | MN-self | HEAD_TAIL | 2 | 180 | 45.6% | +2.27 |

**PHAT HIEN MOI**: MN-self/MT-self co tin hieu tot, dac biet:
- `MN<-self P3P4 D-4`: **51.1%** hit, lift **+7.89pp** (92 ngay).
- `MN<-self TAIL_HEAD D-1`: **48.9%** hit, lift **+5.60pp** (180 ngay).
- `MT<-self P3P4 D-2`: **40.2%** hit, lift **+5.24pp** (82 ngay).
- `MN<-self FIRST2 D-2`: **47.8%** hit, lift **+4.49pp**.

Day la nhung rule HOAN TOAN MOI ma V10606 mining khong cover (do V10606 khong include cross-region self-lag MN/MT). Bay gio em fill xong, can them shadow.

## 4. Cross-region DB-to-MB (vat lieu moi de tham khao)

Top 10 theo H1 lift:

| Target | Source | Transform | Lag | Days | H1 rate | H1 lift_pp | DB-to-DB | DB lift_pp |
|---|---|---|---:|---:|---:|---:|---:|---:|
| MB | MT | FIRST2_REV | 4 | 176 | 33.0% | +9.09 | 0.00% | -1.00 |
| MB | MT | FIRST2_REV | 2 | 176 | 29.5% | +5.68 | 0.00% | -1.00 |
| MB | MN | LAST2 | 2 | 176 | 28.4% | +4.54 | 0.00% | -1.00 |
| MB | MN | LAST2 | 1 | 176 | 27.8% | +3.97 | 0.00% | -1.00 |
| MB | MN | HEAD_TAIL | 3 | 176 | 27.8% | +3.97 | 0.00% | -1.00 |
| MB | MT | LAST2 | 3 | 176 | 27.8% | +3.97 | 0.57% | -0.43 |
| MB | MT | FIRST2_REV | 3 | 176 | 27.8% | +3.97 | 1.14% | +0.14 |
| MB | MN | TAIL_HEAD | 3 | 176 | 27.3% | +3.40 | 1.14% | +0.14 |
| MB | MT | HEAD_TAIL | 3 | 176 | 27.3% | +3.40 | 1.14% | +0.14 |
| MB | MT | TAIL_HEAD | 4 | 176 | 27.3% | +3.40 | 1.14% | +0.14 |

**PHAT HIEN MOI MANH NHAT**: `MB <- MT:DB#1:FIRST2_REV:D-4` lift **+9.09pp** (176 ngay). Day la rule **chuyen MT DB ngay D-4 dao 2 chu so dau** ra MB ngay D.

Vi du:
- MT DB#1 D-4 = `12345`
- 2 so dau = `12` -> dao = `21`
- Soi xem `21` co ve giai nao cua MB ngay D khong

## 5. V107 risk overlay (ap dung cho TAT CA findings tren)

- `BH_FAIL_GLOBAL`
- `SELECTION_BIAS_RISK`
- `FORWARD_90D_INSUFFICIENT`
- `PRE_REGISTER_ONLY`

live_eligible = `False` cho moi rule. Status: PRE_REGISTER_ONLY.

## 6. De xuat thuc hien (DOI ANH XAC NHAN)

### A. Ve gia thuyet owner ban dau
- LAST2 D-2 MB DB -> MB **KHONG nen dua vao panel**. Ket qua am nhe / zero.
- Anh co the chi viec `D-3 thay D-2`, hoac doi sang transform `SECOND_HEAD_TAIL`/`P2P5` o D-2 neu muon giu spirit nguyen ban.

### B. Phat hien moi co the bo sung panel PRE_REGISTER (KHONG live, doi anh OK)
1. `MB<-MB:DB#1:LAST2:D-3` (lift +5.20pp, 172 ngay) — chu ky 3 ngay thay vi 2.
2. `MB<-MB:DB#1:LAST2:W-4` (lift +6.53pp, 171 ngay) — chu ky 4 tuan.
3. `MB<-MB:DB#1:SECOND_HEAD_TAIL:D-2` (lift +6.77pp) — giu lag 2 nhung doi transform.
4. `MB<-MB:DB#1:HEAD_SECOND_LAST:D-2` (lift +3.88pp, DB-to-DB +1.31pp) — manh nhat DB direct.
5. `MB<-MT:DB#1:FIRST2_REV:D-4` (lift +9.09pp) — cross-region moi, manh nhat trong lot.
6. `MN<-MN:DB#1:P3P4:D-4` (lift +7.89pp) — fill V10606 gap MN-self.
7. `MN<-MN:DB#1:TAIL_HEAD:D-1` (lift +5.60pp) — fill V10606 gap.
8. `MT<-MT:DB#1:P3P4:D-2` (lift +5.24pp) — fill V10606 gap MT-self.

Cap them rules nay vao **PRE_REGISTER panel MB/MN/MT** (chua quyet) thi:
- MB hien tai 15 entries -> dat 18-20 (van trong cap 15+5 buffer? Hoac mo cap len 20).
- MN hien tai 15 -> dat 17 voi 2 self-lag moi.
- MT hien tai 20 (max) -> can swap, khong them.

### C. Phai gi truoc khi xet apply
1. Anh **xac nhan** muon them rules moi vao pre-register panel.
2. **Khoa panel** vao file co timestamp.
3. **Doi 90 ngay forward thuc te** (uoc tinh ~2026-08-22).
4. Lam BH correction tren chinh xac panel da khoa, post-correction p<0.05 moi xet apply.
5. Khong promote, khong tin hieu nay tuyet doi.

## 7. Hard safety summary

| Item | Value |
|---|---|
| Official mutation | 0 |
| Provider/manual AI call | 0 |
| Wallet | 0 |
| Lane promotion | 0 |
| Public push | NO (default) |
| Live application | 0 |
| Broad selector used | 0 |

