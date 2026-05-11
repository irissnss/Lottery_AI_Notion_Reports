# TOP2 A/B SHADOW / POLICY RISK — V105.27

## 1. Tables consulted

- `shadow_method_scoreboard=12732` (12732 rows but local schema lacks `date` column query as written — needs different filter approach).
- `shadow_model_promotion_scorecard_daily=542`
- `shadow_daily_comparison=180`
- `shadow_rule_d1_comparison=106`
- `shadow_results=3583`
- `shadow_candidates=3583`

## 2. Recent observation (from scheduler logs 2026-05-11)

- MT closeout 2026-05-11: `[DU-DOAN-TEST-CLOSEOUT] MT evaluated=18 would_save=0 would_break=0`
- MN closeout 2026-05-10: `[CLOSEOUT] MN evaluated_runs=9 would_save_count=2 would_break_count=0 false_promotion_count=0`

| Policy | Region | would_save | would_break | break_ratio | false_promo | Recommendation |
|---|---|---:|---:|---:|---:|---|
| Top2 A/B (lane-test, ADAPTIVE_EXPLOIT / HYBRID) | MN | 2 (2026-05-10 9-run sample) | 0 | 0.000 | 0 | `CONTINUE_MEASURE` — sample still small, target 14d |
| Top2 A/B (lane-test) | MT | 0 | 0 | 0.000 | 0 | `CONTINUE_MEASURE` — but `MT_PROTECT_MODE` means no promote even if would_save grows |
| Top2 A/B (lane-test) | MB | (data per V105.20 mixed) | (per V105.18 lo2 boost MB) | n/a | n/a | `FORENSIC_ONLY` |

## 3. Risk thresholds (carry-over from V105.10/V105.18 doctrine)

- `break_ratio >= 0.20` → HOLD.
- No official promotion unless 14d clean + per-region positive evidence + MT protect preserved.

## 4. Verdicts

- `TOP2_AB_HIGH_BREAK = NO` for current 5-9 run samples.
- `DO_NOT_PROMOTE` until 14d evidence accumulates.
- `MT_PROTECT_PRESERVED` even when MN/MB show benefit.
- Owner decision needed to run a structured 14d Top2 A/B shadow with explicit `entered_top2`, `bundled`, `final_output`, `would_save`, `would_break`, `false_promo` per `region+weekday+station_set` columns.
