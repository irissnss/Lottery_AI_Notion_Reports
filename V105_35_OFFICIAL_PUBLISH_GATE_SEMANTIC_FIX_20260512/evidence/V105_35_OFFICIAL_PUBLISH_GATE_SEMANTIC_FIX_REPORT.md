# V105.35 — Official Publish Gate Semantic Fix Report

Generated: 2026-05-12T19:35:00+07:00

## Executive Verdict

V105.35 is deployed. The root cause of MB blank `/du-doan` was semantic, not missing official rows: MB had `15/15` official output rows, but WR/BT quality filter removed two contributors from voting, so `bundle.model_count=13`. Old `/api/final-bundle` blocked publication by using that scoreable count as readiness.

The fix separates:

- `output_eligible_row_count`: readiness/completion metadata.
- `scoreable_model_count`: voting/scoring quality metadata after WR/BT filter.

## Region Matrix

| Region | Output rows | Scoreable | Quality filtered | Publish ready | UI |
|---|---:|---:|---|---|---|
| MN | 15/15 | 15/15 | none | true | visible |
| MT | 10/15 | 9/15 | one non-scoreable / still missing token rows | false | blocked with reason |
| MB | 15/15 | 13/15 | `claude-opus-4-20250514`, `smart-ensemble` | true | visible with quality warning |

## What Changed

- `web/backend/main.py`: API metadata + publish gate semantic fix.
- `web/frontend/du-doan.html`: readiness and quality warning badges.
- `web/frontend/du-doan-test.html`: baseline label now trusts `publish_ready`, not just `model_count`.

## What Did Not Change

- Production prompt unchanged.
- Scoring formula unchanged.
- Selector unchanged.
- Bundle voting logic unchanged.
- WR/BT filter preserved.
- Official 15 roster preserved.
- No shadow backfill into official.
- No provider/manual AI call.
- Official reserve-fill remains HOLD.

## Evidence

- Live sync before DB claims: `artifacts/live_sync/20260512_191601/manifest.json`.
- Gate audit: `artifacts/v105_35_semantic_gate/v10535_gate_semantic_audit.json`.
- Before: `api_before_MB.json` blocked because observed count was `13/15`.
- After: `api_after_MB.json` publishes with `output_eligible_row_count=15`, `scoreable_model_count=13`, `publish_gate_reason=OUTPUT_ELIGIBLE_ROWS_READY_WITH_QUALITY_WARNING`.
- VPS backup: `/root/Lottery_AI_Test/backups/v105_35_semantic_gate_20260512_192616`.
- Post deploy smoke: `/api/health=200`, `/api/status=200`, `/du-doan=200`, `/api/final-bundle` MN/MT/MB=200.
- Post-deploy sync: `artifacts/live_sync/20260512_192722/manifest.json`.

## Forensic Notes

MB official won with BT `34`; lane-test challenger rows that chose `36` did not win. Lane-test stays `SHADOW_ONLY` and is not promoted.

MT remains a runtime/model-output pending case: five token models have no official row for the day, while no-token and a subset of token/combo rows exist. No fake readiness is granted.

## Late-Result Assimilation

The deployed API now refreshes publish readiness from current predictions rows on read. Metadata exposes late_result_assimilation with late_result_assimilated, late_models, undle_built_at, latest_output_row_at, seconds_after_bundle, within_hard_window, provider_recalled=false, metadata_refreshed=true, and official_output_mutated=false. This is metadata/readiness refresh only; it does not recall providers and does not fabricate output.

## Final Labels

`V105_35_SEMANTIC_GATE_FIX_DEPLOYED`
`PUBLIC_SSOT_UPDATED`
`MB_OUTPUT_ROWS_READY_PUBLISH_OK_WITH_QUALITY_WARNING`
`MT_OUTPUT_ROWS_PENDING`
`PROVIDER_MANUAL_CALL_0`
`OFFICIAL_SCORING_UNCHANGED`
`WR_BT_FILTER_PRESERVED`
`OFFICIAL_ROSTER_PRESERVED`
`LANE_TEST_RESERVE_ONLY`
`OFFICIAL_RESERVE_HOLD`
`NATURAL_VERIFY_PENDING`
