# V52.5 Multi-Region Parallel Test Lane

> Date: 2026-05-03 (built and verified between 22:58 and 23:55 VN)
> Mode: VPS-deployed / measurement + test-lane only / no official mutation
> Live sync: `artifacts/live_sync/20260503_225849/manifest.json`
> VPS backup: `/root/Lottery_AI_Test/backups/v52_5_1_20260503_2300/` (code + 61 MB DB)

## Goal

Owner asked for a real parallel experimental lane mirroring `/du-doan` for MN/MT/MB, applying measurement-driven improvements (region/run_source/weekday-aware strength) without ever mutating official `/du-doan` output. V52.5 delivers that lane end-to-end, strictly admin-only.

## Sub-steps and what landed

### V52.5.1 — Model strength tensor

- File: `web/backend/_compute_model_strength_tensor.py`.
- Table: `model_strength_by_region_weekday_station_daily`.
- Anchor `2026-05-02` (D-1 of 2026-05-03 cycle), 4 windows (7/14/30/60) × 3 grains (region, region+weekday, region+station).
- Rows on VPS: 9052.
- Anti-leakage: anchor strictly D-1 from the requested target date.
- Evidence: `artifacts/phase_checkpoints/V52_5_1_MODEL_STRENGTH_TENSOR_20260503.md`.

### V52.5.2 — Multi-region experimental preview materializer

- File: `web/backend/_materialize_experimental_preview_shadow.py`.
- Table: `experimental_preview_shadow` with region in {MN, MT, MB}.
- 6 experiments per region: OFFICIAL_BASELINE_CONTROL, STRENGTH_WEIGHTED_V52_5_2, AI_CHAIN_PRESERVATION_V1, SPECIALIST_ROSTER_V1, PRIOR_REGION_CONTEXT_SAFE_V1, NO_TOKEN_HERD_REDUCTION_V1.
- Rows on VPS: 1080 across 3 regions × 60 days × 6 experiments.
- Anti-leakage:
  - MN selection inputs: D-1 only.
  - MT selection inputs: D-1 + MN(D) actuals (allowed because MN closes before MT).
  - MB selection inputs: D-1 + MN(D) + MT(D) (allowed because both close before MB).
  - Strength tensor anchor enforced strictly < target date.
- Flip stats (60d, vs official baseline):
  - **MB SPECIALIST_ROSTER**: fw=5, fl=0 (5 free wins).
  - **MN AI_CHAIN_PRESERVATION**: fw=4, fl=1, hits 32 vs official 29.
  - **MN SPECIALIST_ROSTER**: fw=3, fl=0.
  - **MB STRENGTH_WEIGHTED V52.5.2**: fw=8, fl=7, hits 19 vs official 18.
  - **MT AI_CHAIN_PRESERVATION**: fw=8, fl=12 (destructive, matches owner's MT herding observation).

### V52.5.3 — Multi-region test engine

- File: `web/backend/_du_doan_test_engine.py`.
- Reads from `experimental_preview_shadow`, writes to `du_doan_test_*`.
- 30-day backfill on VPS for 3 regions: 540 runs/bundles/results, 12800 candidates, 12800 contributions.
- All `official_output=false`, `output_impact=false`, `test_only=1`.

### V52.5.4 — Experiment registry extended to MN/MT/MB

- File: `web/backend/_du_doan_test_schema.py` (`EXPERIMENTS` list extended).
- 20 experiments registered (7 MB legacy + 6 MN + 6 MT + STRENGTH_WEIGHTED_V52_5_2 for each of 3 regions; MN/MT receive 6 each, MB has 7 since `MB_TIER_AWARE_BUNDLE_SHADOW_V1` and `MB_COMPOSITE_CHALLENGER_V2` remain).

### V52.5.5 — UI/API render `test_bundle` for MN/MT

- File: `web/backend/main.py` `api_du_doan_test_region` extended.
- File: `web/frontend/du-doan-test.html` version label `v52.5`.
- File: `web/frontend/du-doan.html` cache buster `?v=20260503-v52-5-live-parallel`.
- Mode flips from `MN_MT_TEST_LANE_DESIGN_ONLY` to `MN_MT_TEST_LANE_LIVE_PARALLEL_V52_5` when a primary challenger exists.
- In-process API smoke confirms full axes for 2026-05-03:
  - MN: STRENGTH_WEIGHTED test_bt 79 WIN, lo3 579 WIN, xien3 WIN.
  - MT: STRENGTH_WEIGHTED test_bt 29 LOSE, xien3 PARTIAL via 18.
  - MB: COMPOSITE_CHALLENGER_V2 test_bt 48 WIN, lo3 148 WIN.

### V52.5.6 — Multi-region daily runner

- File: `web/backend/_du_doan_test_daily_runner.py`.
- Supports `--region MN | MT | MB | ALL` and `--mode REALTIME_AVAILABLE_ONLY | POST_CLOSEOUT_DIAGNOSTIC_FULL_25`.
- VPS POST_CLOSEOUT smoke for 2026-05-03 ALL: 6 runs/bundles per region, official_tables_touched=False everywhere.
- For MB the runner writes to both `mb_experimental_preview_shadow` (legacy) and `experimental_preview_shadow` (multi-region) so the legacy MB UI/API keeps working.

### V52.5.7 — Final hash guard

Pre (V52.5.1 start of session): `artifacts/_v52_5_1_pre_hash_20260503.txt`
Post (V52.5.7 end of session): `artifacts/_v52_5_7_post_hash_20260503.txt`

| Table | Pre | Post | Hash same |
|---|---:|---:|---|
| predictions | 4134 | 4134 | YES |
| final_bundles | 195 | 195 | YES |
| lottery_results | 14603 | 14603 | YES |
| model_daily_eval | 4089 | 4089 | YES |
| scheduler_logs | 113162 | 113208 | NO (+46 from `lottery` restart + `[DU-DOAN-TEST-*]` markers) |
| mt_model_hit_output_drop_shadow | 301 | 301 | YES |
| loz_selector_shadow | 3273 | 3273 | YES |
| model_latency_cost_audit_daily | 3273 | 3273 | YES |

scheduler_logs growth is expected from 1 service restart + multi-region V52.5.6 test markers; no production scheduler run was triggered.

| Test-lane table | Pre | Post |
|---|---:|---:|
| model_strength_by_region_weekday_station_daily | 0 | 9052 |
| experimental_preview_shadow | new | 1098 |
| mb_experimental_preview_shadow | new (pre-existing 14) | 21 |
| du_doan_test_runs | new | 579 |
| du_doan_test_bundles | new | 579 |
| du_doan_test_results | new | 579 |
| du_doan_test_candidates | new | 13405 |
| du_doan_test_model_contribution | new | 13405 |
| du_doan_test_experiments | new | 20 |
| du_doan_test_audit_log | new | 192 |

## Hard-lock guarantees still in force

- `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`: hash UNCHANGED.
- No call to `generate_final_bundle()`.
- No write to production prompts, model roster, scoring, bundle voting, lane weights, or scheduler.
- All test-lane rows carry `official_output=false`, `output_impact=false`, `test_only=1`, `output_eligible=0`, `diagnostic_only=1` (or 0 only for the OFFICIAL_BASELINE_CONTROL row, which is a read-only mirror with `output_eligible=0` retained).

## Verdict

V52.5 delivers a real multi-region parallel experimental lane. Owner can now compare official `/du-doan` against `/du-doan-test` for MN/MT/MB on the same axes (BT, lo2, lo3, xien2, xien3) using strength-weighted, AI-chain-preservation, prior-region-safe, specialist-roster, no-token-herd-reduction methods. None of these touch official output. Promising challengers (MB SPECIALIST_ROSTER, MN AI_CHAIN_PRESERVATION) accumulate measurement-only evidence; owner-unlock for production remains gated by FU-073 / FU-114 thresholds.
