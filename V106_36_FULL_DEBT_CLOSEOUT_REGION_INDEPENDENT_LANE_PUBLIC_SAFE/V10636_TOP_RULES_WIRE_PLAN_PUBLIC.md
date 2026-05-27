> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 TOP RULES WIRE TO LANE-TEST PLAN

- ts_vn: `2026-05-27T23:00:43`

## Region-isolated lanes

### MN — `MN_INDEPENDENT_LANE_V1`
- TIER_A rules to feed in: **26**
- max per-rule rank contribution: 30%
  - must include candidate family: `MB G2 D-2 first/both tails → MN D (owner observation)`
  - must include candidate family: `MB G4#2 → MN`
  - must include candidate family: `TP.HCM W-4 GĐB/low-card`
  - must include candidate family: `MT Đà Nẵng / Khánh Hòa → MN if double-strong`
- `max_candidate_pool`: `8`
- `false_consensus_dampener`: `True`
- `selector_gap_rescue`: `True`

### MT — `MT_CONVERSION_GATE_LANE_V1`
- TIER_A rules to feed in: **18**
- max per-rule rank contribution: 30%
  - must include candidate family: `MT Huế`
  - must include candidate family: `MT Khánh Hòa`
  - must include candidate family: `MT Đà Nẵng G1 D-2 P3P4`
  - must include candidate family: `MB G7 precision → MT`
  - must include candidate family: `91/97 style current support`
- `full_spent_block_in_lane`: `True`
- `boost_dominance_cap`: `True`
- `rerun_post_mn_dominance_cap`: `True`

### MB — `MB_COST_CONTROL_LANE_V1`
- TIER_A rules to feed in: **4**
- max per-rule rank contribution: 30%
  - must include candidate family: `MB G4/G6/G7 self-lag`
  - must include candidate family: `MB G4#3 P2P3 D-6`
  - must include candidate family: `MB G6#2 D-4`
  - must include candidate family: `MT Khánh Hòa / Đà Nẵng → MB`
  - must EXCLUDE: `MB GĐB D-2 LAST2 (V10635 NOT_VALIDATED)`
- `ai_token_branch_freeze_candidate`: `True`
- `no_token_baseline_first`: `True`
- `high_support_miss_suppressor`: `True`
- `ceiling_pct`: `55`
- `require_n_independent_evidence`: `2`

## Safety

- `official_mutation`: `False`
- `lane_promotion`: `False`
- `wallet`: `0`
- `provider_call`: `0`
- `deploy`: `False`
- `cron`: `False`

## How to ingest into lane-tests (V10637+)

1. Pull TIER_A rows from `V10636_RULES_LANE_TEST_READY_BY_REGION.csv`.
2. For each region, build candidate seed list by joining TIER_A rules against `lottery_results` D-1 for the matching prize_keys.
3. Pass to `du_doan_test_bundles` with `experiment_name` per lane (e.g., `MN_INDEPENDENT_LANE_V1`, `MT_CONVERSION_GATE_LANE_V1`, `MB_COST_CONTROL_LANE_V1`).
4. Each rule contributes <=30% rank weight.
5. Materialization scripts: re-use V10629R1 region-isolated materializer pattern.
6. No write to `final_bundles`, `predictions`, `lottery_results`, `mined_rules`.