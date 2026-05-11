# V102 / V103 / V104 SELECTOR / PROMPT PIPELINE — V105.27

## 1. Pipeline trace

```
V102 recurrence (v102_recurrence_stats_shadow) 666 rows
  -> V103 candidate supply (v103_candidate_supply_shadow) 8743 rows
  -> V104 prompt injection (v104_shadow_prompt_candidate_injection) 1823 rows
  -> V104 model decision (v104_shadow_prompt_model_decision) 93 rows
  -> Selector / top2 (in v101_region_source_pool_top5_shadow / final_bundles)
  -> Bundle / UI (final_bundles 219)
```

## 2. Component status (from local DB + recent SSOT)

| Component | Status | Evidence | Blocker | Next action |
|---|---|---|---|---|
| V102 STRONG rows | Present in `v102_candidate_recurrence_context_shadow` (61 rows) | DB | None | continue measurement |
| V102 RELAXED_L1 rows | `v10522_v102_strong_selector_shadow=0` (V105.22 measurement table empty) | DB | Materializer either VPS-only or not running | confirm cron status on VPS |
| V102 RELAXED_L2 rows | 0 reported in V105.18-V105.22 | DB | Same as above | HOLD until V103 supply fix |
| V103 supply WEAK/STRONG/PROMPT_REVIEW classes | `v103_candidate_supply_shadow=8743` total but local schema does not expose `class` column → schema/version mismatch | DB query returns `no such column: class` | V103 supply class backfill `_v10525_v103_supply_class_backfill.py` may not yet be run locally; need owner gate to backfill 14d | `V103_SUPPLY_BOTTLENECK` |
| V104 prompt injection | `v104_shadow_prompt_candidate_injection=1823` | DB | Schema in local DB lacks `injected` column expected by V105.25 queries | Run schema migration check + V104 injection counter |
| V104 model decision | `v104_shadow_prompt_model_decision=93` | DB | Sample small | More days needed |
| Selector top2 entry | `entered_top2` not directly queried — need cross with `final_bundles` | n/a | Need top2 measurement materializer | shadow pipeline measurement only |
| Would_save / would_break / false_promo | tracked via test-lane closeout (e.g. `[DU-DOAN-TEST-CLOSEOUT] MT evaluated=18 would_save=0 would_break=0`) | scheduler_logs | Per-region small samples | accumulate 14d before promotion |

## 3. Rules

- V102 relaxed: HOLD until 14d of V103 supply class data + per-region break_ratio < threshold.
- No promote if sample small or `would_break` > 0.
- Per-region only — no cross-region promote.

## 4. Verdicts

- `V102_RELAXED_HOLD` — keep relaxed selector OFF official path until 14d of clean supply data.
- `V103_SUPPLY_BOTTLENECK` — class column missing locally; needs schema verify on VPS.
- `V104_SHADOW_ACTIVE` — 1823 injection rows + 93 decisions = pipeline alive but small sample.
- No official prompt/selector/roster change in V105.27.
