# V107 - Null Test & Signal Verification Report

> Phien ban: V107 | Generated: 2026-05-24T06:54:58
> Locked live sync manifest: `artifacts/live_sync/20260523_233622/manifest.json`
> DB last_date: 2026-05-23
>
> Muc dich: Kiem tra framework V106.05 / V106.06 co tin hieu THAT khong, hay dang reward NOISE tu multiple-testing va selection bias.
>
> Hard rule: KHONG fix code, KHONG refactor pipeline, KHONG mine rule moi ngoai panel pre-register, KHONG sua official, KHONG goi provider/manual AI.

## 1. Tom tat 1 trang (BAT BUOC DOC TRUOC)

### 1.1 Verdict tong the

Framework V106.05 / V106.06 **CO MOT PHAN tin hieu vat ly** (chap nhan permutation va negative control), nhung **THAT BAI hai test khac nhau quan trong hon**:

| Null test | Verdict | Y nghia |
|---|---|---|
| 1. Permutation (500 lan) | PASS | Real panel beats random target permutation, p_emp < 0.0001 |
| 2. Negative control (6 synthetic features) | PASS | Real source > all synthetic noise features |
| 3. Multiple-testing correction (BH/Bonferroni) | **FAIL** | **0/153228 rules survive q<0.05 within family** |
| 4. Sub-sample replication odd/even DOY | **FAIL** | rate_both 65.3% < expected 67.4% under independence |
| 5. Forward 90d audit | **INSUFFICIENT** | V106.03 forward 2 ngay fisher_p=0.74 (>= 0.5 threshold), V106.05/06 chua co forward window |

### 1.2 So rule survived sau full test

**0 rule survived multiple-testing correction.** 
Day la phan ung quan trong nhat: dot mining 153,228 hypothesis, **khong rule nao** vuot duoc nguong q<0.05 sau khi correct cho gia thiet boi family.

### 1.3 Recommendation

**Scenario: WEAK SIGNAL / mostly selection bias.**

- Khong promote bat ky V106.05 / V106.06 rule len official, **kha cao** Tier A/B ket qua tu chon mau lieu lon lap nhieu lan voi selection bias da chiet xuat.
- Neu chay shadow tiep, **bat buoc pre-register panel < 50 rule TRUOC khi nhin data** roi forward 90 ngay rieng.
- Ngung mining ban rong (broad scan all transforms/lags) cho den khi co bang chung forward 90d ngoai backtest.
- Khong ket luan "rule nay manh" tu backtest nua.

### 1.4 Forward 90d window thuc te

- V106.03 publish 2026-05-21 -> forward 2 ngay (du lieu da co): aggregate fisher_p = 0.7351 -> stopping criterion >= 0.5 trigger.
- V106.05 publish 2026-05-23 -> forward 0 ngay -> INSUFFICIENT.
- V106.06 publish 2026-05-23 -> forward 0 ngay -> INSUFFICIENT.

Forward 90d audit dung nghia chi co the bat dau tu hom nay. Ket qua 90 ngay sau (uoc tinh 2026-08-21) la bang chung duy nhat valid.

## 2. Bang ket qua null test

### 2.1 Null Test 1 - Permutation

- **Phuong phap**: shuffle target_date <-> all_set/db_unique trong 365 ngay gan nhat, 500 lan, seed=20260524.
- **Real best_lift_pp**: 61.4167
- **Permuted distribution**: min=21.2, p05=24.52, median=31.25, mean=31.7357, p95=41.1667, max=51.25.
- **p_empirical_best_lift**: 0.0 -> **PASS** (criterion: <=0.20).

Ghi chu: pass khong dong nghia framework manh; chi noi panel co lift cao hon random target. Vi panel da duoc selection nen pass o muc nay la can thiet nhung CHUA du.

### 2.2 Null Test 2 - Negative Control

- **Real panel best_lift_pp**: 61.42
- **Synthetic max best_lift_pp**: 34.8846
- **Synthetic mean best_lift_pp across 6 features**: 28.7154
- **Verdict**: **PASS** (criterion: synthetic >= real).

| Synthetic feature | best_overall_lift_pp | top10_mean_lift_pp |
|---|---:|---:|
| random_00_99_seed42 | 31.0385 | 20.533 |
| moon_phase_28day | 27.3462 | 21.277 |
| lunar_day_30 | 34.8846 | 19.311 |
| day_of_year_tail | 32.6 | 21.048 |
| weekday_month_composite | 22.9231 | 19.099 |
| sine_period_27 | 23.5 | 19.742 |

Ghi chu: synthetic feature da co the dat lift +35pp don thuan vi selection across ~1000 (target x lag x scope x window) combinations. Real source dat +61pp tren ~970 source-identities x ~1000 combinations = ~1M tests, nen so sanh truc tiep la GAN-FAIR (real co them ~1000x se selection power).

### 2.3 Null Test 3 - Bonferroni + BH q-value

- **Total hypotheses**: 153228
- **Survivors q<0.05 (BH within family)**: 0
- **Survivors q<0.01 (BH within family)**: 0
- **Survivors p<0.05 Bonferroni within family**: 0
- **Survivors p<0.05 Bonferroni full (153k)**: 0
- **Verdict**: **FAIL_NO_SURVIVORS**

| Family | n_total | n_q05 | n_q01 | n_bonferroni |
|---|---:|---:|---:|---:|
| adjacent_pair | 31651 | 0 | 0 | 0 |
| digit_sum | 11720 | 0 | 0 | 0 |
| head | 23770 | 0 | 0 | 0 |
| head_secondlast_cross | 4688 | 0 | 0 | 0 |
| head_tail_cross | 23770 | 0 | 0 | 0 |
| position_pair | 33859 | 0 | 0 | 0 |
| tail | 23770 | 0 | 0 | 0 |

**Day la phat hien P0 cua V107.** Khong rule nao trong V106.06 du strong de song qua multiple-testing correction. Top rule co raw_p ~ 1.7e-5 nhung BH q ~ 0.40. De sống qua q<0.05 voi family_n=23770, can raw_p < 2.1e-6, ie evidence cuc cao.

### 2.4 Null Test 4 - Sub-sample replication odd/even DOY

- **Lift threshold**: +15.0 pp
- **n_panel_evaluated**: 389
- **rate_odd_pass15**: 85.09%
- **rate_even_pass15**: 79.18%
- **rate_both_observed**: 65.30%
- **rate_both_expected_under_independence**: 67.37%
- **replication_excess_pp**: -2.08
- **Verdict**: **FAIL_REPLICATION_BELOW_INDEPENDENCE**

Y nghia: rule THUC SU manh phai lap o ca odd va even DOY voi rate cao hon expected duoi gia thuyet doc lap. Quan sat thuc te o duoi nguong doc lap -> rule khong replicate on dinh, lift cao trong full window phan lon do tap trung few days.

### 2.5 Null Test 5 - Forward 90d audit

| Report | Forward window | n_rules | fisher_p | Status |
|---|---|---:|---:|---|
| V106.03 | 2 ngay | 3 | 0.7351 | FAIL_STOPPING_CRITERION |
| V106.05 | 0 ngay | 0 | N/A | INSUFFICIENT_DATA |
| V106.06 | 0 ngay | 0 | N/A | INSUFFICIENT_DATA |

Bo sung 30-day holdout proxy (CO data leak, chi mang tinh tham khao):

- Train window: 2025-11-25 -> 2026-04-23 (150 ngay)
- Holdout window: 2026-04-24 -> 2026-05-23 (30 ngay)
- Rules evaluated: 119
- Mean holdout lift_pp: 24.233
- rate_lift_positive: 90.8%
- rate_lift_significant_p05: 14.3%
- fisher_combined_p: 5.308403844765045e-10
- Verdict (CAVEAT: panel duoc select tu data co holdout) : PASS_PRELIMINARY

Quan trong: panel duoc select tu V106.06 mining su dung windows den 2026-05-23 (bao gom holdout). Day la **leakage**, khong phai true forward test. So lieu chi co tinh tham khao, KHONG phai bang chung forward.

## 3. Bang 7 family A-G

| Family | Status | Ket qua chinh |
|---|---|---|
| A. Within-region positional autocorrelation | RUN | mean_lift_pp = -0.855, max = 27.192, min = -28.84 -> verdict NORMAL_RNG |
| B. Mutual information cross-region | NOT RUN | Stopping spirit trigger; computing MI on selected pairs would inherit selection bias |
| C. Cross-prize within-day correlation | NOT RUN | Same as B; no value before forward 90d |
| D. Reverse causality | RUN | forward_lift = 41.349, reverse_lift = 2.597, diff = -36.367 -> verdict PREDICTIVE_LIKE |
| E. Multi-lag conjunction | NOT RUN | 100-200 combinations would inflate hypothesis count further; chua co bang chung tin hieu de combine |
| F. Calendar effects | NOT RUN | Da phan tich weekday/station-set qua scope |
| G. Streak / clustering | NOT RUN | Family A da test self-correlation; dac biet voi mean ~0 cho thay khong co RNG bias ro rang |

Ly do bo qua B/C/E/F/G: stopping criteria trigger sau Null 3 + Null 4 + Null 5; bat ky test bo sung nao tren panel da duoc selection deu se mang theo selection bias. Test moi co y nghia phai chay tren panel pre-registered TRUOC khi nhin data. Family A va D chay vi cheap va tra loi cau hoi integrity (RNG sane khong, rule co dia ho dao chieu khong).

## 4. So sanh V106.05 vs V107

| Tieu chi | V106.05 / V106.06 ket luan | V107 ket luan |
|---|---|---|
| So rule "manh" cho MN/MT/MB | Hang nghin Tier A/B | 0 rule survive multiple-testing correction |
| Best lift Tier A | +35 pp scoped, +18 pp global | Real lift co that, nhung 0 rule individually significant |
| Replication odd/even DOY | Khong test | Below independence (FAIL) |
| Forward verify | Khuyen nghi shadow 14d | Test nay mang tinh hinh thuc; forward 90d chua chay |
| Negative control | Khong test | PASS - real > synthetic, nhung gap nho hon ky vong |
| Recommendation | Tao shadow modules | KHONG promote, can pre-register + forward 90d that |

## 5. Verdict forward 90d (truth bang)

Forward 90d theo dung nghia: **CHUA THE CHAY**. Locked DB last_date = 2026-05-23, V106.03 publish 2026-05-21 -> chi co 2 ngay forward thuc te. 

So lieu chinh thuc tren 2 ngay forward V106.03:

| Rule | Forward days | Forward lift_pp | Forward DB lift_pp | Forward raw_p |
|---|---:|---:|---:|---:|
| `MB:MB_BOARD:G2#1:LAST2 D-2` -> MN | 2 | +52.00 | -3.50 | 0.2304 |
| `MB:MB_BOARD:G2#2:LAST2 D-2` -> MN | 2 | -48.00 | -3.50 | 1.0000 |
| `MB:MB_BOARD:G2#1:LAST2 D-1` -> MN | 2 | +2.00 | -3.50 | 0.7296 |

Aggregate fisher_combined_p = 0.7351 >= 0.5 -> stopping criterion triggered. Tuy nhien sample 2 ngay khong cho phep ket luan vung chac.

## 6. Verdict negative control

| Source | best_overall_lift_pp | Status vs real |
|---|---:|---|
| **Real panel V106.06** | 61.42 | reference |
| random_00_99_seed42 | 31.0385 | -30.38 pp (BELOW) |
| moon_phase_28day | 27.3462 | -34.07 pp (BELOW) |
| lunar_day_30 | 34.8846 | -26.54 pp (BELOW) |
| day_of_year_tail | 32.6 | -28.82 pp (BELOW) |
| weekday_month_composite | 22.9231 | -38.50 pp (BELOW) |
| sine_period_27 | 23.5 | -37.92 pp (BELOW) |

Tat ca 6 synthetic feature deu cho lift duoi real panel. Khoang cach ~26 pp giua real va synthetic max. Tuy nhien luu y: real panel co ~1000x selection power so voi synthetic, nen gap chi 26 pp goi y signal yeu hon ky vong neu real co tin hieu manh.

## 7. Chi tiet Family A va D (integrity check)

### 7.1 Family A - Within-region autocorrelation

- n_tests = 240
- mean_lift_pp = -0.855
- median_lift_pp = 0.109
- max = +27.192 pp, min = -28.84 pp
- pct_lift_positive = 50.0%
- pct_lift_above_5pp = 22.1%
- Verdict: **NORMAL_RNG**

Ket luan: tu lich su 180d, autocorrelation noi region tren LAST2 transform tap trung quanh 0 (mean -0.86 pp). Co +27 pp max va -29 pp min nhung balanced. Day la nhip nhung "noise" the framework co kha nang nham la "rule manh". Day la goc re sample-bias ma V106.06 chi nhan thay.

### 7.2 Family D - Reverse causality

- n_rules = 20 (top 20 V107 panel)
- mean_forward_lift_pp = 41.349
- mean_reverse_lift_pp = 2.597
- mean (reverse - forward) = -36.367 pp
- Verdict: **PREDICTIVE_LIKE**

Ket luan: forward >> reverse, gap = -36 pp. Co the giai thich 2 cach: (a) tin hieu THAT co dia ho di chuyen; (b) selection bias chon panel co forward lift cao, reverse la fresh evaluation tren 20 rule chon ngau nhien -> reverse mean nho la binh thuong. Khong giai thich duoc rieng tu test nay.

## 8. Limitations

1. **Forward 90d chua co data thuc te.** Locked DB ngay 2026-05-23 trung voi ngay publish V106.05/06 -> 0 ngay forward. V106.03 chi co 2 ngay forward.
2. **Permutation panel = 498 rules**, khong phai re-mine 153,228 rule moi permutation. Day la trade-off de chay duoc 500 perms trong 2 giay; gia thuyet la max(panel) da capture phan lon best_lift cua mining gốc.
3. **Negative control feature** khong gom gold/USD/BTC tail vi rule "no provider call" cua governance. 6 deterministic synthetic features la proxy hop ly.
4. **30d holdout proxy** co data leakage vi panel da duoc select tu V106.06 mining tren ca 180d window. So lieu chi nen tham khao, khong phai bang chung independent.
5. **Family B (MI), C (cross-prize correlation), E (multi-lag conjunction), F (calendar), G (streak)** khong chay vi stopping criteria spirit trigger sau Null 3 + Null 4. Chay them tren panel da selection se mang selection bias chuyen tiep.
6. **Family A LAST2 only** - khong test full transform space cho autocorrelation. Day la integrity check, khong phai exhaustive RNG audit.
7. **Stopping criteria forward p>=0.5** trigger boi V106.03 fisher_p=0.74 tren 2 ngay - sample qua nho de ket luan vung chac. Phai cho 90 ngay that.

## 9. Recommendation - 1 trong 3 scenario

Theo evidence aggregate, scenario thich hop nhat:

### Scenario WEAK SIGNAL CHO PHEP PRE-REGISTER PANEL NHO

**Hanh dong cu the:**

1. **DUNG mining ban rong** them rule moi cho den khi co bang chung forward 90d.
2. **Pre-register** mot panel < 50 rule **TRUOC** khi nhin them data, gồm:
   - Top 5 V106.06 Tier A global cho MN, MT, MB (15 rule)
   - Top 5 V106.06 Tier A scoped cho MN, MT, MB (15 rule)
   - 10 rule Family A tu lift cao nhat (control khong co tin hieu)
   - 5 rule synthetic negative control (control)
   - 5 rule random tu V106.06 rejected pool (control)
3. **Khoa panel** vao file pre-register, public-safe push GitHub voi ngay publish ro rang.
4. **Doi 90 ngay** thuc te cho den ~ 2026-08-21.
5. **Audit forward 90d that** voi BH correction tren chinh xac panel pre-registered.
6. **Chi promote** rule co aggregate fisher_p < 0.05 sau correction.

Khong su dung V106.05/V106.06 lam scoring boost trong giai doan nay.

## 10. Lineage rule kiem tra

Rule lineage bat buoc trong V107:
`source_region:source_unit:source_prize#index:transform:lag` 
Vi du:
- `MB:MB_BOARD:G2#1:LAST2:D-2`
- `MB:MB_BOARD:DB#1:P2P4:D-1`
- `MN:Soc Trang:G2#1:FIRST2_REV:W-2`

Trong toan bo V107: KHONG broad selector (G3_ALL/LOW_ALL/TOP3/ALL_PRIZES) duoc dua vao test. Tat ca 153,228 hypothesis kiem soat lineage day du.

## 11. Output artifacts

Trong `artifacts/v107_null_and_signal_test/`:
- `machine_readable/V107_NULL1_PERMUTATION.json`
- `machine_readable/V107_NULL2_NEGATIVE_CONTROL.json`
- `machine_readable/V107_NULL3_CORRECTION.json`
- `machine_readable/V107_NULL3_RULES.csv`
- `machine_readable/V107_NULL4_SUBSAMPLE.json`
- `machine_readable/V107_NULL4_RULES.csv`
- `machine_readable/V107_NULL5_FORWARD_AUDIT.json`
- `machine_readable/V107_FAMILY_A_AUTOCORR.json`
- `machine_readable/V107_FAMILY_D_REVERSE_CAUSALITY.json`
- `machine_readable/V107_RULE_PANEL.json`
- `scripts/_v107_lib.py`
- `scripts/01_null_permutation.py`
- `scripts/02_null_negative_control.py`
- `scripts/03_null_retroactive_correction.py`
- `scripts/04_null_subsample_replication.py`
- `scripts/05_null_forward_audit.py`
- `scripts/06_family_A_and_D.py`
- `scripts/99_build_report.py`

Hard safety:
- KHONG sua official, KHONG goi provider/manual AI, KHONG promote rule.
- KHONG dua DB / jsonl / log / secret len public.
- 4 official tables hash unchanged truoc/sau toan bo V107 pass.

---

**Locked manifest**: `artifacts/live_sync/20260523_233622/manifest.json`. **DB last_date**: 2026-05-23. **Generated**: 2026-05-24T06:54:58.
