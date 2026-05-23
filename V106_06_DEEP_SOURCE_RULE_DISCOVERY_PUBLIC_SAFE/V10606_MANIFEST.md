# V106.06 MANIFEST

Live snapshot manifest: `artifacts/live_sync/20260523_230610/manifest.json`
DB path (local-after-sync): `data/lottery_ai.db`
Script: `artifacts/v106_06_deep_source_rule_discovery/scripts/v10606_deep_mine.py`
Run timestamp (local): 2026-05-23T23:12:29

## Data scope
- date range: 2020-01-01 -> 2026-05-23
- target dates indexed: 6897
- source identities (>=30 occurrences): 3486

## Hypothesis space
- transform families: ['adjacent_pair', 'digit_sum', 'head', 'head_secondlast_cross', 'head_tail_cross', 'position_pair', 'tail']
- lag axes: ['D-1', 'D-2', 'D-3', 'D-4', 'D-5', 'D-6', 'D-7', 'W-1', 'W-2', 'W-3', 'W-4']
- windows: [30, 60, 90, 180]
- targets: ['MN', 'MT', 'MB']
- weekday scopes: T2..CN
- top station-sets included: {"MB": 6, "MN": 7, "MT": 8}

## Output
- rules accepted: 54924
- rules rejected: 98304
- agreement events region rows: 3

## Files
- deep_source_rule_candidates.csv
- top_rules_by_target_region.json
- rejected_rules.csv
- station_set_rules.csv
- weekday_rules.csv
- agreement_rules.csv
- agreement_rules.json
- overfit_warning_report.md
- FINAL_OWNER_REPORT_VN.md

## Hard safety
- No official mutation. No /du-doan touched. No provider/manual AI call.
- No DB / jsonl / log committed. Public package will exclude all runtime artifacts.
