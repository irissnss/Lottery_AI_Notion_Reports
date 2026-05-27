> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 RULE105 DAMPENER PLAN

- ts_vn: `2026-05-27T22:58:52`

## Per-region dampeners (lane-test only, no official mutation)

### MN
- `threshold`: `50`
- `ceiling`: `0.7`
- `confirm_only_share`: `30`
- `ready_strong_share`: `3`
- `false_consensus_dampener`: `True`
- `selector_gap_rescue`: `True`
- `max_candidate_pool`: `8`

### MT
- `threshold`: `60`
- `ceiling`: `0.7`
- `weak_buckets_suppress_weekdays`: `[0, 1, 2, 3, 4, 6]`
- `boost_dominance_cap`: `True`
- `rerun_post_mn_dominance_cap`: `True`
- `ninetyone_ninety_seven_current_support_required`: `True`

### MB
- `threshold`: `50`
- `ceiling`: `0.55`
- `require_n_evidence`: `2`
- `no_single_rule_overclaim`: `True`
- `no_token_baseline_first`: `True`
- `high_support_miss_suppressor`: `True`
- `ai_token_branch_freeze_candidate`: `True`
