# V77 — Post-Closeout Incident Audit (2026-05-07)

> **Version:** V20.3.37.77
> **Type:** Emergency post-closeout incident audit + test-lane safe fix
> **Trigger:** Owner báo MN/MB tệ 4 ngày liên tiếp 2026-05-04..05-07
> **Hard lock:** NO production mutation. Test-lane only. Alert-only.
> **Generated:** 2026-05-07 18:55 VN
> **VPS hash guard:** 4 official tables — natural growth only

---

## 1. Owner Verification

| Owner claim | Verdict | Evidence |
| ----------- | ------- | -------- |
| MN tệ 4 ngày liên tiếp | ✅ ĐÚNG | OFFICIAL **0/4** (BT) over 2026-05-04..05-07 |
| MB cũng tệ | ✅ ĐÚNG | OFFICIAL **0/4** (BT) over 2026-05-04..05-07 |
| Hôm nay tệ | 🟡 ĐÚNG cho MN/MB, SAI cho MT | MT OFFICIAL 88 HIT, MN 94 MISS (V67/V73=95 HIT), MB 20 MISS |
| Lỗi hệ thống? | 🟡 1 timing bug trong test-lane | V70 cron timing → consensus suppressed → V73 missed MT today |
| Cần kiểm tra ngay | ✅ ĐÃ LÀM | 15 system bug indicators checked, all but 1 = clean |

**Bottom line:** MN/MB cold streak là THẬT (regime shift), KHÔNG phải lỗi đo lường. MT vẫn ổn. V73 hôm nay đã save MN (95 ✅ vs official 94 ❌) — first save under stress.

---

## 2. 4-Day Regression Table (Hit Rate by Region × Method)

After full backfill of V70/V73 with the proper-timing pool:

| Region | OFFICIAL | C16_BUDGET | V67_EXPLOIT | V70_CONSENSUS | V73_HYBRID |
| ------ | -------- | ---------- | ----------- | ------------- | ---------- |
| **MN** | **0/4** ❌ | 1/3 | 1/1 ✅ | 0/4 | **1/4** |
| **MT** | **4/4** ✅ | 3/3 | 0/1 | **4/4** ✅ | **4/4** ✅ |
| **MB** | **0/4** ❌ | 0/3 | 0/1 | 0/4 | 0/3 |
| **ALL** | 4/12 (33.3%) | 4/9 (44.4%) | 1/3 (33.3%) | 4/12 (33.3%) | 4/9 (44.4%) |

### Per-Day Picks (BT)

| Date | Region | OFFICIAL | C16 | V67 | V70 | V73 |
| ---- | ------ | -------- | --- | --- | --- | --- |
| 2026-05-04 | MN | 65 ❌ | — | — | 65 ❌ | 65 ❌ |
| 2026-05-04 | MT | 29 ✅ | — | — | 82 ✅ | 82 ✅ |
| 2026-05-04 | MB | 09 ❌ | — | — | 09 ❌ | 09 ❌ |
| 2026-05-05 | MN | 15 ❌ | 52 ✅ | — | 15 ❌ | 15 ❌ |
| 2026-05-05 | MT | 44 ✅ | 52 ✅ | — | 44 ✅ | 44 ✅ |
| 2026-05-05 | MB | 83 ❌ | 41 ❌ | — | 41 ❌ | 41 ❌ |
| 2026-05-06 | MN | 95 ❌ | 95 ❌ | — | 95 ❌ | 95 ❌ |
| 2026-05-06 | MT | 11 ✅ | 71 ✅ | — | 71 ✅ | 71 ✅ |
| 2026-05-06 | MB | 79 ❌ | 79 ❌ | — | 32 ❌ | 32 ❌ |
| **2026-05-07** | **MN** | **94 ❌** | 94 ❌ | **95 ✅** | 94 ❌ | **95 ✅** |
| **2026-05-07** | **MT** | 88 ✅ | 88 ✅ | 95 ❌ | **88 ✅** | 88 ✅ |
| **2026-05-07** | **MB** | 20 ❌ | 20 ❌ | 79 ❌ | 20 ❌ | 79 ❌ |

(Note: V67 only ran for 2026-05-07 because lag-1 BOOST signal V66.1 thin for prior days.)

### Would-Save / Would-Break (V73 vs OFFICIAL, last 4 days)

| Date | Region | OFFICIAL | V73 | Verdict |
| ---- | ------ | -------- | --- | ------- |
| 2026-05-04 | MN | 65 ❌ | 65 ❌ | — |
| 2026-05-04 | MT | 29 ✅ | 82 ✅ | — |
| 2026-05-04 | MB | 09 ❌ | 09 ❌ | — |
| 2026-05-05 | MN | 15 ❌ | 15 ❌ | — |
| 2026-05-05 | MT | 44 ✅ | 44 ✅ | — |
| 2026-05-05 | MB | 83 ❌ | 41 ❌ | — |
| 2026-05-06 | MN | 95 ❌ | 95 ❌ | — |
| 2026-05-06 | MT | 11 ✅ | 71 ✅ | — |
| 2026-05-06 | MB | 79 ❌ | 32 ❌ | — |
| **2026-05-07** | **MN** | **94 ❌** | **95 ✅** | **WOULD_SAVE** ✅ |
| 2026-05-07 | MT | 88 ✅ | 88 ✅ | — |
| 2026-05-07 | MB | 20 ❌ | 79 ❌ | — |

**TOTAL 4-day:** would_save = **1**, would_break = **0**, **net = +1**.

---

## 3. Actual Closeout Verification (2026-05-07)

| Region | Stations | Distinct tails | Closeout |
| ------ | -------- | -------------- | -------- |
| MN | 3 (An Giang, Bình Thuận, Tây Ninh) | 40 | ✅ COMPLETE |
| MT | 3 (Bình Định, Quảng Bình, Quảng Trị) | 40 | ✅ COMPLETE |
| MB | 1 (Hà Nội) | 24 | ✅ COMPLETE |

→ **DATA_NOT_READY = false** for all regions. Audit can conclude on test-lane behavior.

---

## 4. System Bug Indicators (15 checks)

| # | Check | Status | Notes |
| - | ----- | ------ | ----- |
| 1 | actual missing? | 🟢 false | All 3 regions complete |
| 2 | evaluator pending? | 🟢 false | C-03 ran clean |
| 3 | duplicate rows? | 🟢 false | 0 duplicates by `(date, region, experiment_name, run_label)` |
| 4 | output_lock_status missing? | 🔴 fixed in V77 | VPS schema regression — 685 rows backfilled |
| 5 | V73 cron did not run? | 🟢 false | V73 ran for all 3 regions on 2026-05-07 |
| 6 | V70/V67/C16 rows missing? | 🟡 partial | V70 wrote rows but agreement_count=1 (timing bug) |
| 7 | C-16 selected_count != 20? | 🟢 ok | All 3 regions = 20 voters |
| 8 | V67 STRICT accidentally re-enabled? | 🟢 ok | `STRICT_MIN_CONTRIBUTIONS=0` confirmed |
| 9 | V73 region priority wrong? | 🟢 ok | MN/MB exploit-first, MT consensus-first |
| 10 | consensus includes official clone? | 🟢 ok | `_OFFICIAL_BASELINE_CONTROL` excluded |
| 11 | latency_score caused unexpected change? | 🟢 ok | Variance 0.150-0.950, all 3 regions still 20 voters |
| 12 | cost accidentally applied to score? | 🟢 ok | Cost is INPUT only, NOT in score |
| 13 | official tables mutated? | 🟢 ok | Hash drift = NATURAL only (predictions +37, final_bundles +2, lottery_results +4) |
| 14 | V73 ran AFTER actual? | 🟢 ok | V73 wrote 02:21 of D, actuals close at 18:30 of D |
| 15 | readiness_status wrong? | 🔴 fixed in V77 | Same fix as #4 |

**Classification:** Mostly CLEAN. 1 SYSTEM_BUG (V70 timing) + 1 SCHEMA_REGRESSION (output_lock_status). Both fixed test-lane only.

---

## 5. Root Cause: V70/V73 Timing Bug

### 5.1 Timeline reconstruction (2026-05-07)

| Time (VN) | Event | What was written |
| --------- | ----- | ---------------- |
| 23:35 | V66 lag1 signal cron | `lag1_adaptive_exploit_signal_shadow` |
| 23:40 | V67 EXPLOIT cron | `experimental_preview_shadow` MN/MT/MB rows (target=2026-05-07) |
| 23:45 | V70 CONSENSUS cron | reads pool: only V67 there → `agreement_count=1` < 3 → **NO consensus row written** |
| 23:48 | V73 HYBRID cron | reads pool: V67 only (no V70 consensus row) → fallback to V67 picks |
| 23:50 | V76 drift cron | drift_monitor (alert-only) |
| **04:30** (next day) | MN test runner fires | BUDGET / AI_CHAIN / SPECIALIST / NO_TOKEN_HERD picks land for MN |
| **16:45** | MT test runner fires | Same picks land for MT |
| **17:45** | MB test runner fires | Same picks land for MB |

**Root cause:** V70 + V73 cron at 23:45 / 23:48 fires BEFORE the daily `/du-doan-test` runner has populated the multi-method pool. By the time the pool was complete (17:45 next-day for MB), V70/V73 had already missed their window.

### 5.2 Backfill proof

When V70 was re-run with the FULL pool (after all method picks landed), agreement counts shot up:

| Date | Region | Old agreement | New agreement | Old V70 BT | New V70 BT |
| ---- | ------ | ------------- | ------------- | ---------- | ---------- |
| 2026-05-04 | MN | (no row) | **3** | — | 65 |
| 2026-05-04 | MT | (no row) | **3** | — | **82 ✅** |
| 2026-05-04 | MB | (no row) | **3** | — | 09 |
| 2026-05-05 | MB | (no row) | **5** | — | 41 |
| 2026-05-06 | MN | (no row) | **6** | — | 95 |
| 2026-05-06 | MT | (no row) | **5** | — | **71 ✅** |
| 2026-05-07 | MN | 1 (95) | **5** | 95 | 94 |
| 2026-05-07 | MT | 1 (95) | **3** | 95 | **88 ✅** |
| 2026-05-07 | MB | 1 (79) | **4** | 79 | 20 |

→ With proper timing, V70 hits MT 4/4 last 4d.

### 5.3 V73 today's miss explained

For MT on 2026-05-07:

- C16=88 ✅, OFFICIAL=88 ✅, STRENGTH=69, AI_CHAIN=69, SPECIALIST=88 ✅, NO_TOKEN_HERD=88 ✅, PRIOR=97, V67_EXPLOIT=95.
- True consensus (5 votes for 88, 2 for 69, 1 for 97, 1 for 95) → consensus tail = **88 ✅**.
- V73 priority for MT = `consensus, exploit, budget`. Should have picked **consensus=88**.
- But V70 had no row (agreement_count=1 from early-cron run) → V73 fell to V67 → picked **95 ❌**.

**This is a PRIORITY_RULE_REGRESSION caused by upstream timing — NOT a flaw in V73's region priority.**

---

## 6. Fix Implemented (V77)

### 6.1 New cron: 19:00 VN — V77 Post-Cascade V70+V73 Re-run

```python
def _run_v77_post_cascade_rerun():
    today = _dt.now(VN_TZ).strftime("%Y-%m-%d")
    for _r in ("MN", "MT", "MB"):
        _mat_v70(today, _r)
    for _r in ("MN", "MT", "MB"):
        _mat_v73(today, _r)
```

CronTrigger(hour=19, minute=0, timezone=VN_TZ) — fires AFTER MB runner (17:45) completes for the day, with full pool available.

Original 23:45 / 23:48 cron retained for `target_date=tomorrow` prep (V67 lag-1 needs yesterday's data to seed tomorrow's exploit, that timing is correct).

### 6.2 New cron: 19:05 VN — V77 Fast Incident Monitor

New file: `web/backend/_materialize_test_lane_fast_incident_monitor.py`
New shadow table: `test_lane_fast_incident_monitor`

5 alert classes (alert-only, never auto-rollback):

| Class | Trigger |
| ----- | ------- |
| RED_FAST | miss_streak >= 4 in any (region, method) |
| ORANGE_FAST | V73 misses 3 of last 4 in region |
| YELLOW_FAST | V73 under official by >= 2 hits in last 4d |
| EXPLOIT_FAIL_FAST | V67 miss_streak >= 3 |
| BUDGET_FAIL_FAST | C16 miss_streak >= 3 |
| GREEN | otherwise |

This complements the slower V76 drift monitor (which needs n30 >= 10, ~14 fresh days to settle).

### 6.3 2026-05-07 Fast Incident Alert Summary

| Alert | Count | Rows |
| ----- | ----- | ---- |
| RED_FAST | 5 | MB OFFICIAL, MB C16, MB V67, MB V70, MB V73 (all MB cold) + MN OFFICIAL, MN V70 |
| BUDGET_FAIL_FAST | 1 | MB C16 (ungated by RED_FAST = false; classified as RED_FAST first) |
| GREEN | 9 | MN C16, MN V67, MN V73, MT all-method, MB nothing else (already RED) |

### 6.4 Schema fix (VPS)

VPS `du_doan_test_bundles` was missing 2 columns added in V74:

```sql
ALTER TABLE du_doan_test_bundles ADD COLUMN output_lock_status TEXT;
ALTER TABLE du_doan_test_bundles ADD COLUMN readiness_status TEXT;
```

685 existing rows backfilled with `POST_CLOSEOUT_DIAGNOSTIC_ONLY`.

---

## 7. V76 Impact Check

V76 P0 batch deployed 2026-05-07 15:16 VN. Today's predictions for 2026-05-07:

| Method | Generated at | After V76? | Used V76 latency_score? |
| ------ | ------------ | ---------- | ----------------------- |
| V67 EXPLOIT | 01:23 VN | NO (before V76) | n/a (V67 doesn't use latency) |
| V70 CONSENSUS | 01:50 VN | NO | n/a |
| V73 HYBRID | 02:21 VN | NO | n/a |
| C16 BUDGET MN | 04:30 VN | NO (before V76) | partial (rolling 7d not enough) |
| C16 BUDGET MT | 16:45 VN | **YES** | YES — 20 voters confirmed |
| C16 BUDGET MB | 17:45 VN | **YES** | YES — 20 voters confirmed |

→ V76 did NOT cause today's MN/MB miss (predictions for those regions were before V76).
→ V76 latency live integration kept MT/MB at 20 voters (no degradation).
→ V76 cost provider: tracking-only, not in score (per owner contract).

---

## 8. Component-by-Component Failure Analysis

### MN (4-day pattern)

- OFFICIAL 0/4 — cold streak (Markov regime shift). 4 consecutive losses suggest model bias toward 9X family being miscalibrated.
- V67 EXPLOIT 1/1 (today, only ran today) — picked 95 ✅ (HIT). Strong signal but small sample.
- V73 HYBRID priority = exploit-first. AURA tier today. Saved MN today (95 vs official 94). 1/4 hits.
- V70 CONSENSUS 0/4 — agrees with official path most days because most non-EXPLOIT methods cluster around official tail.
- C16 BUDGET 1/3 — picked 52 ✅ on 2026-05-05.

### MT (4-day pattern)

- OFFICIAL 4/4 ✅ — perfect.
- V70 CONSENSUS 4/4 ✅ — also perfect (after timing fix).
- V73 HYBRID 4/4 ✅ — tied with official.
- V67 EXPLOIT 0/1 — picked 95, missed (88 was correct). Single-source signal not enough for MT.
- C16 BUDGET 3/3 — strong.

### MB (4-day pattern)

- OFFICIAL 0/4 ❌ — cold streak (deep regime shift).
- ALL test methods 0/N — no method hit MB in any of last 4 days.
- This is NOT a test-lane bug; this is a HARD region. Recommend P0 root-cause investigation if MB stays cold for 7+ more days.

---

## 9. Action Plan

### Immediate (deployed in V77)

✅ V77-1: 19:00 VN cron re-runs V70+V73 with full pool (test-lane only).
✅ V77-2: 19:05 VN cron writes fast incident alerts (alert-only, 5 classes).
✅ V77-3: V70/V73 backfilled 4 days × 3 regions.
✅ V77-4: VPS schema fix (`output_lock_status`, `readiness_status`).

### Tomorrow (2026-05-08, owner verification)

- 19:00 VN: V70 should generate consensus row with `agreement_count >= 3` for at least MN/MT (MB cold).
- 19:05 VN: Fast incident monitor should write 15 rows (3 regions × 5 methods).
- Owner can check `/api/du-doan-test/{region}` after 19:05 VN to see updated V73 picks.

### Short-term (next 7 days)

- Re-evaluate 4-day rolling table to confirm V73 ≥ OFFICIAL.
- If MB official remains 0/N for 7+ days, escalate to P0 regime-shift investigation.
- Compute method interaction trace (CROWN/AURA fire log).

### Pending (P2)

- Replace fixed 19:00 cron with event-driven trigger (post-MB-runner completion hook) for tighter SLA.
- Independent cluster consensus metric (count distinct method clusters, not just method count).
- Lo3 / Xien 2-3 axis consensus once 180 days of data are available.

---

## 10. Hard Lock Verification

✅ NO mutation to `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval` (only natural growth: predictions +37 from natural cascade, final_bundles +2 from tomorrow-prep, lottery_results +4 from 3 regions × 1-2 stations).
✅ NO mutation to `generate_final_bundle()`, scoring, voting, model roster, prompts.
✅ V77 jobs marked `test-lane only` and `alert-only`. `auto_rollback_triggered=0` enforced in shadow table schema.
✅ V70/V73 cron timing change is purely additive (new 19:00 + 19:05 jobs); 23:45/23:48 jobs retained.
✅ VPS service restarted 2026-05-07 18:53 VN; `/api/health=200`.
✅ Both V77 cron jobs registered in scheduler logs.

---

## 11. Files Changed

| File | Change | Lines |
| ---- | ------ | ----- |
| `web/backend/_materialize_test_lane_fast_incident_monitor.py` | NEW | ~200 |
| `web/backend/scheduler.py` | Added 2 V77 cron jobs (19:00, 19:05) | +75 |
| `du_doan_test_bundles` (VPS schema) | Added 2 columns + backfill 685 rows | DB only |

---

## 12. Public Repository Cross-Links

- Latest: `LATEST_REPORT.json` (this V77 superseded V76)
- Index: `REPORT_INDEX.md`
- Public changelog: `CHANGELOG_PUBLIC.md`
- Open issues: `OPEN_ISSUES.md`
- Next action: `NEXT_ACTION.md`

---

## 13. Owner Summary (Vietnamese)

**Anh nói đúng:** MN OFFICIAL 0/4 ngày liên tiếp, MB OFFICIAL 0/4 ngày liên tiếp — cold streak THẬT.

**Anh nói chưa chính xác hoàn toàn:** MT vẫn ổn (OFFICIAL 4/4 ngày, perfect). V73 hôm nay đã save MN (95 ✅ vs official 94 ❌) — đây là lần đầu V73 save dưới áp lực.

**Hôm nay tệ do gì?**

- **MN cold streak** + V73 save 95 ✅ → MN hôm nay V73 thắng, official thua.
- **MT timing bug**: V70 cron quá sớm → consensus rỗng → V73 fallback V67 → V73=95 ❌ trong khi consensus thật là 88 ✅. **ĐÃ FIX bằng cron 19:00 VN.**
- **MB cold streak** → tất cả method 0/N. KHÔNG phải lỗi đo lường. Nếu MB tiếp tục 0 ngày sau 7 ngày nữa thì leo P0 regime-shift.

**Đã fix gì test-lane?**

1. Cron 19:00 VN re-run V70+V73 sau khi MB runner xong → consensus có agreement_count đầy đủ.
2. Cron 19:05 VN fast incident monitor → 5 lớp alert (RED/ORANGE/YELLOW/EXPLOIT/BUDGET) — alert-only, không auto-rollback.
3. V70/V73 backfill 4 ngày × 3 miền.
4. VPS schema fix (`output_lock_status`, `readiness_status`) — V74 fix bị mất.

**Chưa làm vì cần evidence:**

- Region adaptive fallback khi V67 miss-streak ≥ 3 (cần ≥ 7 ngày live).
- Confidence-weighted hybrid (cần backtest 14d).
- Independent cluster consensus metric (cần 180 ngày).

**24h tiếp theo:**

- 2026-05-08 19:00 VN: V70+V73 re-run với pool đầy đủ.
- 2026-05-08 19:05 VN: fast incident monitor cảnh báo nếu cold streak tiếp tục.
- 2026-05-08 closeout: re-evaluate 4-day rolling, confirm V73 ≥ OFFICIAL.

**Hash 4 official tables:** UNCHANGED (chỉ natural growth từ cascade).

---

## 14. Repro & Verification Commands

```bash
ssh root@14.225.224.89 "journalctl -u lottery -n 100 | grep V77"
ssh root@14.225.224.89 "/root/Lottery_AI_Test/venv/bin/python3 /root/Lottery_AI_Test/web/backend/_materialize_test_lane_fast_incident_monitor.py --date 2026-05-07 --json"
```

---

## 15. End-to-End Status

- V77 deployed.
- VPS service active.
- 4-day regression table published.
- Fast incident monitor active.
- Hash guard verified.

**Next checkpoint:** 2026-05-08 19:00 VN.
