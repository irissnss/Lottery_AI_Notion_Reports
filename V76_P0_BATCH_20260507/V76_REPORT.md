# V76 — P0 BATCH (drift monitor + C-16 latency live + cost tracking)

**Date:** 2026-05-07 15:16 VN
**Owner directive:** Option A — implement all 3 P0 items in this session.
**Hard contract:** test-lane only. ZERO touch official.
- Drift: ALERT only, never auto-rollback.
- Latency: rolling 7d avg score input only, never prunes.
- Cost: tracking only, never auto down-rank.

---

## Summary

| Item | Status | Risk | Owner contract honored |
|---|---|---|---|
| **P0-1 Drift detector** | ✅ DEPLOYED | ZERO | alert-only, `auto_rollback_taken=0` enforced |
| **P0-2 C-16 latency_score live** | ✅ DEPLOYED | ZERO | rolling 7d avg, gentle curve never zeros, cost NOT in score |
| **P0-3 Cost provider table** | ✅ DEPLOYED | ZERO | tracking only, NO score adjustment |
| **VPS deploy** | ✅ 15:16 VN | — | `/api/health=200` |
| **Hash guard 4 official tables** | ✅ UNCHANGED | — | predictions/final_bundles/lottery_results/model_daily_eval same SHA256 pre/post |

---

## P0-1 — Drift detector

**File:** `web/backend/_materialize_drift_monitor.py`
**New shadow table:** `test_lane_signal_drift_monitor` (`output_eligible=0`, `diagnostic_only=1`, `owner_approved=0`, `auto_rollback_taken=0`)
**Cron:** 23:50 VN daily (after V73 23:48)

### Alert classes

| Class | Trigger |
|---|---|
| 🔴 RED | `\|hit_rate_7d − hit_rate_30d\| > 15 pp` (with n7d ≥ 5) |
| 🟡 YELLOW | 3 consecutive miss days in 7d window |
| 🟠 ORANGE | consensus agreement < 3 for ≥5 consecutive days (V70/V73 dependents) |
| 🟢 GREEN | healthy |
| ⚫ GRAY | n30d < 10 (insufficient sample) |

### 2026-05-07 result

12 rows persisted (3 regions × 4 methods). All GRAY because n30d < 10 — natural state for newly-deployed methods. After 14 fresh closed days (target 2026-05-21), alerts will become meaningful.

### What it monitors

- V73_HYBRID, V70_CONSENSUS, V67_EXPLOIT, C16_BUDGET
- 3 regions (MN/MT/MB)

---

## P0-2 — C-16 latency_score live integration

**File patched:** `web/backend/_materialize_du_doan_test_model_budget.py` `_latency_score()`

### Logic

```python
# Read rolling 7-day average latency from model_latency_cost_audit_daily
# (require >=2 valid days; fall back to single-day if only 1 available)
if latency < 30:    score = 0.95
elif latency < 60:  score = 0.80
elif latency < 120: score = 0.55
elif latency < 180: score = 0.30
else:               score = 0.15

# Mild timeout penalty (max 0.20 reduction, floor 0.10) — never zeros model
if timeout_count_7d >= 2:
    score = max(0.10, score - 0.20)

# Cost NOT applied to score (owner-no-prune contract)
```

### 2026-05-07 result (variance proof)

| Metric | Before V76 | After V76 |
|---|---:|---:|
| min latency_score | 0.500 | **0.150** |
| max latency_score | 0.500 | **0.950** |
| avg latency_score | 0.500 | 0.540 |
| distinct values | 1 | **6** |

### Top fast (latency_score = 0.95)

`kimi-k2.5` 11.3s, `qwen3-coder` 6.4s, `grok-4.20-multi-agent` 10.9s

### Top slow (latency_score = 0.15)

`gpt-oss-120b` 190.8s, `glm-5.1` 184.4s, `qwen3.6-plus` 136.8s, `gemma-4-31b` 137.0s

→ Slow models still selected to budget (target_max=20 keeps them in pool), but their **final_budget_score is reduced naturally**, giving them less weight in HYBRID aggregation.

---

## P0-3 — Cost provider table

**File:** `web/backend/_provider_pricing_table.py` (configurable by owner)
**Patched:** `_materialize_v52_measurement_surfaces.py` to derive `cost_estimate = (token_count/1000) × price_per_1k` when API trace doesn't natively provide cost.

### 2026-05-07 cost capture (MN region)

| Model | latency | tokens | cost |
|---|---:|---:|---:|
| claude-opus-4-20250514 | 41.6s | 27,955 | **$0.42** |
| gpt-5.4 | 25.0s | 21,219 | $0.11 |
| gpt-5.5 | 71.6s | 21,131 | $0.11 |
| claude-sonnet-4-6 | 47.7s | 29,158 | $0.087 |
| deepseek-reasoner | 134.4s | 32,817 | $0.046 |
| grok-4.20-multi-agent | 10.9s | 20,618 | $0.041 |
| deepseek-v4-pro | 115.2s | 29,058 | $0.041 |
| gemini-2.5-pro | 33.9s | 25,303 | $0.032 |
| gemini-3.1-pro | 48.6s | 23,870 | $0.030 |
| gpt-5-mini | 87.7s | 25,730 | $0.026 |
| qwen3.6-plus | 136.8s | 23,567 | $0.024 |
| gemini-2.5-flash | 39.2s | 29,216 | $0.022 |
| qwen3-max-thinking | 25.4s | 21,700 | $0.022 |
| kimi-k2.5 | 11.3s | 25,883 | $0.021 |
| gpt-oss-120b | 190.8s | 19,594 | $0.020 |
| gemini-3-flash | 21.9s | 21,241 | $0.016 |
| deepseek-v4-flash | 22.4s | 20,957 | $0.015 |
| glm-5.1 | 184.4s | 24,076 | $0.014 |
| qwen3-coder | 6.4s | 21,544 | $0.013 |
| **gemma-4-31b** | 137.0s | 22,028 | **$0.000** (free tier) |
| **TOTAL MN** | — | 486,665 | **~$1.10** |

→ Cost is **tracked**, NOT applied to C-16 score. Owner can later decide cost-based pruning at a separate gate.

---

## Cron schedule (now 5 jobs daily VN)

```
23:35 VN — V66 lag-1 adaptive exploit signal
23:40 VN — V67 ADAPTIVE_EXPLOIT_V1
23:45 VN — V70 CONSENSUS_V1
23:48 VN — V73 HYBRID_V1 (region-adaptive)
23:50 VN — V76 drift monitor (alert-only)  ← NEW
```

Plus:
- 5-min — `/du-doan-test` pre-result trigger
- 23:30 VN — daily eval backup

---

## Hash guard

| Table | sha256[:16] | count | verdict |
|---|---|---:|---|
| predictions | `189facdf5ffbadfb` | 4419 | UNCHANGED |
| final_bundles | `21c339f493db2d72` | 205 | UNCHANGED |
| lottery_results | `b730399a81f6f754` | 14621 | UNCHANGED |
| model_daily_eval | `a557c5819263a019` | 4328 | UNCHANGED |

Pre/post identical on LOCAL+VPS.

---

## Open items after V76

- ✅ P0 list COMPLETE (3/3)
- ⏳ P1: method interaction trace, C-16 top-20 audit surface, UI dashboard, per-station consensus
- 🟡 P2: OFFICIAL_PROMOTION_DOSSIER draft, region-specific candidates analysis, Lo3/Xien consensus
- 🔴 P3: NO_TOKEN local timing, Cohere wide-pool, production cascade strength-ordering (owner gate)

---

## Next session

Cron daily 23:35-23:50 VN sẽ accumulate 14 fresh closed days. Drift monitor alerts sẽ active sau 2026-05-21. Em chờ owner OK proposal P1 hoặc cứ để cron tự chạy.

STATUS: **V76_P0_BATCH_COMPLETE — all 3 P0 items deployed test-lane only, official untouched, hash guard PASS**.
