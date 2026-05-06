# DAY GOVERNANCE CRITERIA — Canonical day-tag definitions

> **Created:** 2026-05-02 V20.3.37.36 Phase A
> **Purpose:** Standardize how each closed day is tagged for replay / backtest / measurement
> **Source:** V35 finding (FU-083): 60d window has only 12/60 (20%) fully VALID days

---

## 1. Tag definitions

For each `(date)`, evaluate `min(predictions per region)` where region ∈ {MN, MT, MB} and `run_source IN ('auto_daily','ai_chain','rerun_post_mn','rerun_post_mt','rerun_post_mb','shadow_auto_eval')`.

| Tag | Criteria | Use in metric |
|---|---|---|
| `VALID_LIVE_DAY` | min predictions per region **>= 22** | ✅ Primary metric (clean-day) |
| `DEGRADED_LIVE_DAY` | 15-21 predictions per region | 🟡 Secondary diagnostic only |
| `INCOMPLETE` | 10-14 predictions per region | 🔴 Reference only, do NOT use as primary |
| `EXCLUDE_PRIMARY` | < 10 predictions per region | ❌ Excluded from any aggregate metric |

→ **Why >= 22 for VALID**: roster is 25 active models (15 output + 10 SHADOW_AUTO). Allowing 3-model fallback gives 22 floor. Days with full roster have 25-26 predictions.

---

## 2. Mandatory split in all replay reports

Every replay summary, backtest report, or aggregate metric MUST report:

| Split | Required |
|---|:---:|
| Clean-day primary (VALID only) | ✅ MANDATORY |
| All-day diagnostic (VALID + DEGRADED + INCOMPLETE) | ✅ MANDATORY |
| Per-tag breakdown | ✅ MANDATORY |

Reports that present a single number without this split are **considered overclaim** per `.Antigravityrules.md` governance.

---

## 3. Implementation requirement for CP-2.2 refined replay

When `_materialize_tier2_replay_shadow.py` (or any new replay materializer) launches:

1. ADD `day_tag` column to schema (TEXT, one of the 4 values above)
2. Compute tag for each date BEFORE running policy logic
3. Materialize rows with `day_tag` populated
4. Replay summary script MUST aggregate by `day_tag`
5. Pass-gate criteria apply to **VALID_LIVE_DAY subset only**, not all-day

---

## 4. Current 60d distribution (V35 audit baseline)

Window: 2026-03-04 .. 2026-05-01 (60 closed days)

| Tag | Count | % |
|---|---:|---:|
| VALID_LIVE_DAY | 12 | 20.0% |
| DEGRADED_LIVE_DAY | 18 | 30.0% |
| INCOMPLETE | 21 | 35.0% |
| EXCLUDE_PRIMARY | 9 | 15.0% |

→ **Only 20% of last 60 days are fully valid**. Replay must filter heavily.

---

## 5. Why this matters

V33 CP-2.1 14d replay (2026-04-18..2026-05-01) included 5 DEGRADED days mixed with 9 VALID days. Result was -9.5 to -14.3 pp NET, but the result is **distorted** because degraded days had fewer model predictions, biasing vote concentration.

V35 strict requirement: refined CP-2.2 replay must split metrics by `day_tag` to honestly evaluate policy lift.

---

## 6. Reference files

- Audit script: `artifacts/_audit_v35_controller.py` section 5 (degraded-day hygiene)
- Raw output: `artifacts/_v35_controller_out.txt`
- FU tracker: `FU-083 — Degraded-day hygiene 60d tagging + replay filter`
- Active roadmap: `docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md` CP-X.2

---

*Status: ACTIVE governance criterion. Updated when criteria thresholds change with explicit owner OK.*
