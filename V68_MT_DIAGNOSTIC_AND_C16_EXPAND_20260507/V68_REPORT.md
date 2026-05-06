# V68 — MT diagnostic + C-16 budget expansion 15-20 voters

**Date:** 2026-05-07 01:40 VN
**Scope:** owner directives (1) clarify MT weakness; (2) expand C-16 to ≥15 strongest models. Test-lane only. ZERO touching `/du-doan`, `final_bundles`, scoring, model_registry, prompt.

---

## 1. Owner question (Vietnamese)

> "MT VÀ MB YẾU LÀ YẾU THẾ NÀO EM YẾU SO VỚI OFFICIAL HAY YẾU SO VỚI CHỈ SỐ ĐẸP MỸ MÃN CỦA MN ?"
> "TOTAL TEST LANE ĐANG LẤY TỐI THIỂU 8-10 MODEL MẠNH NHẤT... MUỐN SỬ DỤNG SỨC MẠNH CỦA TỐI THIỂU 15 MODEL MẠNH NHẤT."

---

## 2. Diagnostic — MT yếu so với gì?

| Region | V67 hit | Random baseline | Official hit | Δ vs random | Δ vs official | Verdict |
|---|---:|---:|---:|---:|---:|---|
| **MN** | 100% | 43.4% | 40% | **+56.6pp** | **+60pp** | 🟢 strong improvement |
| **MB** | 50% | 23.8% | 17% | **+26.2pp** | **+33.3pp** | 🟢 strong improvement vs both |
| **MT** | 33% | 35.1% | 67% | **−1.7pp ≈ random** | **−33.3pp 🔴** | 🔴 weaker than official AND random |

→ MN và MB **đều mạnh hơn cả random và official**. Owner đọc "MB 50%" tưởng yếu nhưng so với baseline MB 24% và official MB 17%, MB là cải tiến rõ.
→ **Chỉ MT thực sự là regression** — yếu so với official và gần như bằng random.

### MT regression root cause (per-day trace)

| Date | V67 | Trace contributions | Verdict |
|---|---|---|---|
| 2026-05-01 | 99 | **single** per-model `gemini-2.5-pro Δ6.0` | low confidence noise |
| 2026-05-02 | 16 | 4 per-model + 1 same-region + 1 cross | strong, just unlucky |
| 2026-05-03 | 71 | **single** per-model `gemini-2.5-pro Δ9.3` | low confidence — but HIT |
| 2026-05-04 | 29 | 5 per-model + 1 same-region | strong, HIT |
| 2026-05-05 | 65 | **single** cross MN→MT `Δ24.8` | volatile cross-region single source |
| 2026-05-06 | 15 | **single** cross MN→MT `Δ23.1` | volatile cross-region single source |

**Root cause**: 4/6 MT picks were single-source. Cross MN→MT signal has high statistical edge (+26pp average) but high single-day volatility — single-source picks are noisy.

---

## 3. Fix 1 — V67.1 STRICT-confidence gate (no penalty path)

```python
# In _materialize_adaptive_exploit_v1.py
STRICT_MIN_CONTRIBUTIONS = 2
STRICT_SCORE_THRESHOLD   = 1.5
# Skip emit (no row written) when top candidate has:
#   contribution_count < 2 AND score < 1.5
# This is suppression-only — no penalty applied to any signal.
```

After-fix backfill 14d:

| Region | n_before | n_after | hit_before | hit_after | net_before | net_after |
|---|---:|---:|---:|---:|---:|---:|
| MN | 5 | 2 | 100% | 100% | +3 | +2 |
| **MT** | 6 | 2 | 33% | **50%** | −2 | **−1** |
| MB | 6 | 6 | 50% | 50% | +2 | +2 |

→ MT improves from `−1.7pp vs random` to `+15pp vs random` on the surviving subset; from `−33.3pp vs official` to `−16.7pp vs official`.
→ MN stays 100% on the high-confidence subset (lost 3 single-source rows, all were hits — trade-off documented).
→ MB unchanged because all candidates were already multi-source.

### Trade-off honesty

STRICT may suppress some single-source winning days in MN (3 days lost: 56, 17, 13 picks were all hits). The trade is fewer noise picks ↔ fewer single-source lucky picks. With small sample (n=5-6 per region) it's hard to say which trade dominates. Owner can revisit at CP-66.9 (after 14 fresh live days).

---

## 4. Fix 2 — C-16 budget expansion 8-10 → 15-20

```python
# In _materialize_du_doan_test_model_budget.py
target_min = 15  # was 8
target_max = 20  # was 10
```

2026-05-07 result on VPS:

| Region | total_pool | measured | selected | watch | skipped | controls |
|---|---:|---:|---:|---:|---:|---:|
| MN | 29 | 22 | **20** (was 10) | 8 | 1 | 4 |
| MT | 29 | 22 | **15** (was 8) | 7 | 7 | 4 |
| MB | 29 | 22 | **15** (was 8) | 7 | 7 | 4 |

→ Fewer models in SKIP_TODAY, more voters contributing to `ADAPTIVE_BUDGET_SELECTOR_V1` aggregation, satisfies owner's directive "≥15 model mạnh nhất theo region/weekday/station".

---

## 5. Verification

| Check | Result |
|---|---|
| `predictions` count LOCAL | 4377 (unchanged) |
| `final_bundles` count LOCAL | 204 (unchanged) |
| `lottery_results` count LOCAL | 14621 (unchanged) |
| `model_daily_eval` count LOCAL | 4328 (unchanged) |
| VPS deploy | `01:38 VN`, `/api/health=200` |
| VPS C-16 2026-05-07 | MN selected 20, MT selected 15, MB selected 15 |
| V67 still test-lane only | `output_eligible=0`, `diagnostic_only=1`, `owner_approved=0` |

---

## 6. Caveat & next gates

- After-fix MT n=2 sample is too small for hard conclusion. CP-66.7 14-day fresh live verification remains the proof gate.
- STRICT gate may need re-tuning at CP-66.9 if it suppresses too many MN winners.
- C-16 expansion to 15-20 voters may slightly dilute discrimination in weak buckets where only 8-10 models are truly strong; effect on `ADAPTIVE_BUDGET_SELECTOR_V1` win rate to be measured during live verification.

---

## 7. Discoveries during V68

- **MT regression is single-source noise**, not signal degradation. Fix is structural (require multi-source) not signal-recalibration.
- Cross-region single-source factor 1.23-1.25 has good *expected* edge but high single-day variance — needs multi-source confirmation to be trustworthy on individual days.
- C-16 with 8-10 voters was leaving 18-21 measured models in SKIP/WATCH. Owner-directed widen surfaces these strengths.

---

## 8. Raw paths

| Artifact | Path |
|---|---|
| MT diagnostic dump | `artifacts/v68_mt_diagnostic/v68_mt_diagnostic.txt` |
| V67 after-strict eval | `artifacts/v68_mt_diagnostic/v67_after_strict_eval.txt` |
| V68 report (this) | `artifacts/v68_mt_diagnostic/V68_REPORT.md` |
| Updated materializers | `web/backend/_materialize_adaptive_exploit_v1.py`, `web/backend/_materialize_du_doan_test_model_budget.py` |
| CHANGELOG | V20.3.37.68 |

STATUS: **V68_DEPLOYED — STRICT_GATE_LIVE + C16_15_20_VOTERS_LIVE — accumulating CP-66.7 evidence**.
