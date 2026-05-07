# CONTINUOUS MEASUREMENT DOCTRINE

> **Created:** V20.3.37.74 (2026-05-07)
> **Owner:** anh
> **Authority:** binding for all test-lane work; this is the canonical reference for "khi nào dừng đo lường"
> **Short answer:** **NEVER**.

---

## 1. Core principle

Lottery has drift. Owner explicitly directed: **measurement does not stop at 7/14/30/60/90/180 days. Those are review checkpoints, not stop points.** Long-term measurement is mandatory because:

- prize density per region/weekday/station drifts
- model strength rotates per weekday
- shadow models age in/out
- test-lane methods accumulate evidence against fresh draws
- hidden regimes (e.g. weekday blackspot) appear/disappear
- structural regression in any region must be detected within days, not weeks

→ **Continuous measurement is on by default. There is no scheduled "end of monitoring".**

---

## 2. Window contract

| Window | Use |
|---|---|
| **1d** | Sanity smoke (today's pick exists, evaluator ran, hashes unchanged) |
| **3d** | Daily anomaly check (drift detector) |
| **7d** | Weekly review checkpoint (per-region per-method) |
| **14d** | Fresh-live verification gate for any new test-lane method |
| **30d** | Stability gate before any TIER 3 review |
| **60d** | Robustness gate (region × weekday) |
| **90d** | Cross-window consistency check |
| **180d** | Per-weekday × per-station gate (need ≥30 closed days per weekday cell) |
| **continuous** | **always_on** — no end date |

→ A method that "passes 30d" still must continue to be measured at 60/90/180/continuous.

---

## 3. Mandatory tracking surfaces

For every active test-lane method:

| Surface | Required |
|---|---|
| Daily evidence pack `artifacts/daily_evidence_pack/<DATE>/` | YES |
| `scoreboard.md` + `scoreboard.json` (Wilson 95% CI) | YES |
| `hash_guard.txt` for 4 official tables | YES |
| `open_issues.md` per day | YES |
| Rolling windows 1/3/7/14/30/60/90/180/lifetime | YES |
| Drift detector signal | YES (P1 to be implemented next session) |

For every active method registered in `TEST_LANE_METHOD_REGISTRY.md`:
- per-region, per-weekday, per-station, per-model_class, per-flow_type, per-tier breakdown
- profit proxy with payout multipliers (70x MB, 80x MN/MT)
- `would_save` / `would_break` / `false_promotion`
- `correct_but_dropped` / `wrong_boosted`

---

## 4. What we never drop

We **never** stop measuring a metric just because it looks "đẹp" or because a method was promoted. Reasons:

1. Lottery numbers rotate — a model strong this week can degrade next week.
2. Today's hit rate has wide CI; long-term tracking is the only honest measurement.
3. Owner needs evidence after promotion to monitor regression.
4. Drift can be detected only by continuous comparison against rolling baselines.
5. The system is meant to learn forever, not just until a test passes.

→ Any drop of a metric requires explicit owner OK + DECISION_LOG entry + governance update.

---

## 5. Review cadence

| Cadence | Action |
|---|---|
| Daily 23:35 → 23:48 VN cron | V66 / V67 / V70 / V73 materializers; daily evidence pack auto-generated |
| Daily after closeout | C-03 evaluator; PENDING ≤ 5 in MN closed-day rows |
| Weekly | Roll forward best-method per region; check 7d / 14d gates |
| Monthly | 30d stability review; potential proposal for TIER 3 review (CP-66.9) |
| Quarterly | 90d robustness review; per-weekday gate readiness |
| Half-yearly | 180d per-weekday × per-station review; calibrate strength tensor weights |
| Continuous | drift detector, alerts, regression signals |

---

## 6. Promotion gate (no early promotion)

A test-lane method MUST satisfy ALL of:

- ≥14 fresh closed days at the current configuration
- 30d preferred for full stability
- 60d for robustness
- per-region lift vs OFFICIAL Wilson lower bound > OFFICIAL Wilson lower bound
- Profit/ROI greater than OFFICIAL across rolling 30d
- `would_save` ≥ `would_break` over 30d
- `false_promotion` rate below 10%
- No region degradation
- Not dependent on a single volatile signal source
- Rollback plan documented in `OFFICIAL_PROMOTION_DOSSIER.md`
- Owner explicit OK in `DECISION_LOG.md`

→ **Backfill alone is never sufficient.** Fresh live data is mandatory.

---

## 7. Drift detection (P1, planned)

Next session must implement:

- `test_lane_signal_drift_monitor` table
- Rolling 7d hit rate vs rolling 30d hit rate per method per region
- Alert when |Δ| > 15 pp
- Alert when method falls below random baseline for ≥3 consecutive days
- Alert when consensus agreement count drops below 3 across 5 consecutive days

---

## 8. Override authority

Only **owner** can:
- Drop a method from monitoring
- Lower review cadence
- Promote a method to official lane
- Disable continuous measurement

Agent must NEVER:
- Stop materializers without owner OK
- Cut sample size to fit a narrative
- Hide PENDING / duplicate / readiness issues
- Drop a metric just because it underperforms

---

STATUS: **ACTIVE — continuous measurement locked**.
