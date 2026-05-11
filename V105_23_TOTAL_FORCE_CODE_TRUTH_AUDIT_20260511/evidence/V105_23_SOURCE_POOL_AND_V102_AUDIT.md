# V105.23 Source-Pool Gap + V102 Audit

Status: **read-only / shadow-only / no official mutation**.

## Implemented Source-Pool Formulas

The region formulas are implemented in `_v101_shadow_pilot.py` and mirrored in `_v10522_live_prep.py` profile metadata.

- MN: `MN_D = (MN+MT+MB) D-1 + (MN+MT+MB) D-2`.
- MT: `MT_D = (MN+MT+MB) D-1 + MN D`.
- MB: `MB_D = (MN+MT+MB) D-1 + MN D + MT D`.

Implementation truth:

- `_v101_shadow_pilot.SOURCE_POOL_POLICY_TEXT` stores policy text.
- `_source_steps(region, target_date)` encodes MN all-regions D-1/D-2, MT all-regions D-1 + MN same-day, MB all-regions D-1 + MN/MT same-day.
- `_collect_region_source_candidates()` executes those steps against `lottery_results`.
- `_materialize_region_source_pool()` writes candidates to `v101_region_source_pool_shadow` and provenance to `v101_region_source_pool_evidence_shadow`.

V105.23 check:

- `MT d2_rows=0`.
- `MB d2_rows=0`.
- `MN d2_rows=3080`.

Therefore D-2 is isolated to MN and does not leak to MT/MB in the current shadow source-pool table.

## SOURCE_POOL_MISS Current State

Current tables:

- `bundle_universe_coverage_daily=3076`.
- `source_prize_strong_coverage=3076`.
- `rule_injection_contract=3076`.
- `candidate_drop_stage_daily=102`.

Observed blind spot:

- MN: `SOURCE_POOL_MISS` invisible `28/28`, `PROMPT_NOT_INJECTED=1212`.
- MT: `SOURCE_POOL_MISS` invisible `24/29`, `PROMPT_NOT_INJECTED=994`.
- MB: `SOURCE_POOL_MISS` invisible `14/18`, `PROMPT_NOT_INJECTED=671`.

Interpretation:

- `SOURCE_POOL_MISS` is still a P0 measurement gap before prompt/rank/bundle.
- The current V105.22 coverage table can show per-tail misses, but it does not yet explain the miss at full V105.23 depth.

## Current Drilldown Surfaces

`bundle_universe_coverage_daily` has:

- `target_date`, `region`, `weekday`, `station`, `actual_tail`.
- flags: `in_candidate_universe`, `in_source_pool`, `injected_to_prompt`, `ranked`, `top5`, `top2`, `bundled`, `final_output`.
- `drop_stage`, `drop_reason`, `source_prize`, `method_id`, `rule_family`, `model_id`.

Weakness:

- `station` is often null in current insert path.
- `source_prize` is inserted as null for current coverage rows.
- `candidate_drop_stage_daily` is aggregate/dominant-stage, not full tail-level drilldown.
- There is no join from `SOURCE_POOL_MISS` to `v101_region_source_pool_evidence_shadow`.
- V101 pool is top-30 materialized; a tail below top-30 may look like a formula miss unless the full unranked evidence is compared.

## Why V102 Strong Selector Shadow Is 0 Rows

`v10522_v102_strong_selector_shadow=0`.

Code truth:

- `_v10522_live_prep._materialize_v102_shadow()` exits if `v103_candidate_supply_shadow` does not exist.
- It selects only rows where `v102_recurrence_class='STRONG'` or `v102_recommendation='PROMPT_REVIEW_STRONG'`.
- `_v102_recurrence_tracker.py` classifies STRONG only when `recurrence_score >= 20`.
- `_materialize_v102_shadow()` materializes the single target date, not a rolling 30d backfill.

DB truth from V105.23 probe:

- Latest `v103_candidate_supply_shadow` max date: `2026-05-09`.
- MN supply rows: 100, `v102_strong_or_prompt=0`.
- MT supply rows: 100, `v102_strong_or_prompt=0`.
- MB supply rows: 100, `v102_strong_or_prompt=0`.
- Strict current: 0 all regions.
- Diagnostic relaxed level 1: 0 all regions.
- Diagnostic relaxed level 2: 0 all regions.

Conclusion:

V102 0 rows means upstream recurrence context had no STRONG/PROMPT_REVIEW_STRONG seed rows for the materialized date. It does not mean selector quality is resolved.

## Owner Tail Cases: 68 / 78 / 02 / 82

The tails appear in candidate-supply history, but sampled rows have `v102_recurrence_score=0` or null `v102_recurrence_class` / `v102_recommendation`. Some have other source layers or non-gan core, but they are not passing V102 recurrence.

V105.23 follow-up must preserve these fields:

- `candidate_tail`, `region`, `target_date`, `weekday`, `station_set`.
- `v102_strength`, `source_layers`, `gan_present`, `non_gan_core_present`.
- `lose_only_pass`, `strict_gate_pass`, `relaxed_gate_pass`.
- `selector_rank_before`, `selector_rank_after`, `entered_top2`.
- `would_save`, `would_break`, `reason_if_not_selected`.

## Lose-Only Gate

Implemented in `_materialize_adaptive_exploit_v1.py`:

- D-1 per-model lag-1 skips if yesterday BT hit actuals.
- Cross-region next-day skips if source region D-1 BT hit.
- Cross-region same-day requires source actuals known and skips if source BT hit.
- Unknown same-day source actuals are skipped.

Audit rollup in `lane_test_lose_only_audit_daily`:

- `pass_gate=1` only when `recycled_from_win_count=0` and `source_actual_unknown_used=0`.
- V105.23 result: all MN/MT/MB have recycled winner = 0 and source unknown used = 0.

Gap:

- `_v10522_live_prep._materialize_v102_shadow()` sets `lose_only_pass=True` without re-enforcing the V67 lose-only doctrine. V105.23 relaxed V102 shadow should align this.

## Required V105.23 Fix Surface

Add shadow/admin-only:

- `v10523_source_pool_gap_drilldown`.
- `v10523_candidate_flow_trace`.
- `v10523_v102_relaxed_selector_shadow`.

No official selector, scoring, prompt, bundle, or final output mutation.
