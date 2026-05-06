# V64 Hardening Audit + Safe Deployment Plan

## 1. Yêu cầu đã hiểu

Mục tiêu là làm cho `/du-doan-test` đủ tin cậy để thu thập evidence 14/30 ngày, không phải cải thiện official ngay. Không thêm model mới. Không đụng `/du-doan` official.

## 2. Scope thực hiện

Audit + implementation plan cho:

- C-03 multi-region closeout evaluator
- C-17A idempotency/dedupe guard
- C-17B output lock/readiness gate
- C-05 latency/cost instrumentation
- C-16 explainability audit

## 3. Rules áp dụng

Đã đọc `.Antigravityrules.md`.

Áp dụng:

- HARD PRE-FLIGHT
- NO PARTIAL FIX
- RUNTIME CHANGE = DEPLOY + VERIFY
- NO-STALE-DB EVALUATION
- DB-SOURCE REPORTING
- LIVE DATA PRESERVATION
- DUAL-TABLE EVALUATION
- BẠCH THỦ NORTH STAR
- Notion AI report export/synthesis rule

Đã thỏa:

- Sync live DB/trace trước audit: `artifacts/live_sync/20260506_232706/manifest.json`
- Dùng public V63 mới nhất thay vì V62.
- Không đề xuất đụng official.

Blocked/partial:

- Notion MCP search broad available, but page-content fetch by page-id is blocked by current tool wrapper. Mark: `READ_BLOCKED_PARTIAL_CONTENT`.

## 4. Newest version check

Public report repo có `V63_SAFE_IMPLEMENTATION_20260506`, mới hơn V62. Vì vậy V63 là newest visible report package. Audit không dùng V62 làm nguồn chính.

## 5. Executive verdict

- Official: `OFFICIAL_LOCK_CONFIRMED` by scope; no official mutation proposed.
- `/du-doan-test`: chưa đủ tin để làm official evidence clean 14/30 ngày.
- P0 thật sự hiện tại:
  1. C-17A dedupe/idempotency guard
  2. C-17B output lock/readiness gate
  3. C-03 evaluator natural-hook hardening
  4. C-05 latency live proof after next model calls

Tổng experimental line vẫn đúng hướng, nhưng measurement trust đang bị block bởi duplicate rows, snapshot-type/readiness thiếu, và latency chưa live-proven.

## 6. Evidence summary

### Duplicate audit

"# Duplicate audit\n\n## Bundles\n| run_date | region | experiment_name | mode | row_count | ids | picks | first_created | last_created |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| 2026-05-04 | MB | MB_AI_CHAIN_PRESERVATION_V1 | POST_CLOSEOUT_DIAGNOSTIC_FULL_25 | 2 | 595,601 | 09,09 | 2026-05-05T00:45:45.530380+07:00 | 2026-05-05T00:45:46+07:00 |\n| 2026-05-04 | MB | MB_NO_TOKEN_HERD_REDUCTION_V1 | POST_CLOSEOUT_DIAGNOSTIC_FULL_25 | 2 | 598,604 | 09,09 | 2026-05-05T00:45:45.536578+07:00 | 2026-05-05T00:45:46+07:00 |\n| 2026-05-04 | MB | MB_OFFICIAL_BASELINE_CONTROL | POST_CLOSEOUT_DIAGNOSTIC_FULL_25 | 2 | 592,599 | 09,09 | 2026-05-05T00:45:45.523196+07:00 | 2026-05-05T00:45:46+07:00 |\n| 2026-05-04 | MB | MB_PRIOR_REGION_CONTEXT_SAFE_V1 | POST_CLOSEOUT_DIAGNOSTIC_FULL_25 | 2 | 597,603 | 19,19 | 2026-05-05T00:45:45.534534+07:00 | 2026-05-05T00:45:46+07:00 |\n| 2026-05-04 | MB | MB_SPECIALIST_ROSTER_V1 | POST_CLOSEOUT_DIAGNOSTIC_FULL_25 | 2 | 596,602 | None | 2026-05-05T00:45:45.532382+07:00 | 2026-05-05T00:45:46+07:00 |\n| 2026-05-05 | MB | MB_AI_CHAIN_PRESERVATION_V1 | POST_CLOSEOUT_DIAGNOSTIC_FULL_25 | 2 | 620,626 | 41,41 | 2026-05-05T20:32:35.321414+07:00 | 2026-05-05T20:32:36+07:00 |\n| 2026-05-05 | MB | MB_NO_TOKEN_HERD_REDUCTION_V1 | POST_CLOSEOUT_DIAGNOSTIC_FULL_25 | 2 | 623,629 | 41,41 | 2026-05-05T20:32:35.328104+07:00 | 2026-05-05T20:32:36+07:00 |\n| 2026-05-05 | MB | MB_OFFICIAL_BASELINE_CONTROL | POST_CLOSEOUT_DIAGNOSTIC_FULL_25 | 2 | 617,624 | 83,83 | 2026-05-05T20:32:35.313464+07:00 | 2026-05-05T20:32:36+07:00 |\n| 2026-05-05 | MB | MB_PRIOR_REGION_CONTEXT_SAFE_V1 | POST_CLOSEOUT_DIAGNOSTIC_FULL_25 | 2 | 622,628 | 98,98 | 2026-05-05T20:32:35.325852+07:00 | 2026-05-05T20:32:36+07:00 |\n| 2026-05-05 | MB | MB_SPECIALIST_ROSTER_V1 | POST_CLOSEOUT_DIAGNOSTIC_FULL_25 | 2 | 621,627 | None | 2026-05-05T20:32:35.323649+07:00 | 2026-05-05T20:32:36+07:00 |\n| 2026-05-06 | MB | MB_AI_CHAIN_PRESERVATION_V1 | REALTIME_AVAILABLE_ONLY | 2 | 650,657 | 32,32 | 2026-05-06T17:40:01.929262+07:00 | 2026-05-06T17:40:03+07:00 |\n| 2026-05-06 | MB | MB_NO_TOKEN_HERD_REDUCTION_V1 | REALTIME_AVAILABLE_ONLY | 2 | 653,660 | 32,32 | 2026-05-06T17:40:01.935834+07:00 | 2026-05-06T17:40:03+07:00 |\n| 2026-05-06 | MB | MB_OFFICIAL_BASELINE_CONTROL | REALTIME_AVAILABLE_ONLY | 2 | 647,655 | 79,79 | 2026-05-06T17:40:01.920956+07:00 | 2026-05-06T17:40:03+07:00 |\n| 2026-05-06 | MB | MB_PRIOR_REGION_CONTEXT_SAFE_V1 | REALTIME_AVAILABLE_ONLY | 2 | 652,659 | 32,32 | 2026-05-06T17:40:01.933632+07:00 | 2026-05-06T17:40:03+07:00 |\n| 2026-05-06 | MB | MB_SPECIALIST_ROSTER_V1 | REALTIME_AVAILABLE_ONLY | 2 | 651,658 | None | 2026-05-06T17:40:01.931519+07:00 | 2026-05-06T17:40:03+07:00 |\n\n## Preview\nNO_ROWS\n\n## Budget\nNO_ROWS\n"

### Pending / timeline audit

"# Timeline / Pending audit\n\n| run_date | region | official_bundle_created_at | first_test_bundle_created_at | actual_result_created_at | test_bundle_rows | pending_bt_rows | pending_lo2_rows | actual_rows_joined |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| 2026-05-04 | MB | 2026-05-04 17:40:09 | 2026-05-05T00:45:45.523196+07:00 | 2026-05-04T18:31:01.727554+07:00 | 13 | 0 | 0 | 13 |\n| 2026-05-04 | MN | 2026-05-04 04:23:51 | 2026-05-05T00:45:40+07:00 | 2026-05-04T16:38:38.654514+07:00 | 6 | 0 | 0 | 18 |\n| 2026-05-04 | MT | 2026-05-04 16:42:00 | 2026-05-05T00:45:43+07:00 | 2026-05-04T17:30:00.634797+07:00 | 6 | 0 | 0 | 12 |\n| 2026-05-05 | MB | 2026-05-05 17:39:20 | 2026-05-05T20:32:35.313464+07:00 | 2026-05-05T18:31:33.177544+07:00 | 14 | 2 | 0 | 14 |\n| 2026-05-05 | MN | 2026-05-05 04:22:20 | 2026-05-05T20:32:30+07:00 | 2026-05-05T16:36:37.083100+07:00 | 7 | 3 | 0 | 21 |\n| 2026-05-05 | MT | 2026-05-05 16:42:00 | 2026-05-05T20:32:32+07:00 | 2026-05-05T17:31:01.653737+07:00 | 7 | 0 | 0 | 14 |\n| 2026-05-06 | MB | 2026-05-06 17:38:59 | 2026-05-06T17:40:01.920956+07:00 | 2026-05-06T18:31:32.933031+07:00 | 14 | 14 | 14 | 14 |\n| 2026-05-06 | MN | 2026-05-06 04:24:20 | 2026-05-06T07:50:54+07:00 | 2026-05-06T16:34:35.829649+07:00 | 7 | 21 | 21 | 21 |\n| 2026-05-06 | MT | 2026-05-06 16:42:00 | 2026-05-06T16:45:01+07:00 | 2026-05-06T17:30:00.663173+07:00 | 7 | 14 | 14 | 14 |\n"

### C16 audit

"# C16 audit\n\n## Daily\n| run_date | region | total_pool_count | measured_pool_count | selected_count | watch_count | skipped_count | created_at |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n| 2026-05-05 | MB | 29 | 28 | 8 | 10 | 11 | 2026-05-05T23:10:52+07:00 |\n| 2026-05-05 | MN | 29 | 28 | 10 | 16 | 3 | 2026-05-05T23:10:51+07:00 |\n| 2026-05-05 | MT | 29 | 28 | 8 | 14 | 7 | 2026-05-05T23:10:52+07:00 |\n| 2026-05-06 | MB | 29 | 23 | 8 | 10 | 11 | 2026-05-06T17:40:00+07:00 |\n| 2026-05-06 | MN | 29 | 28 | 10 | 18 | 1 | 2026-05-06T07:50:52+07:00 |\n| 2026-05-06 | MT | 29 | 22 | 8 | 10 | 11 | 2026-05-06T16:45:00+07:00 |\n\n## Empty selected picks\n| run_date | region | model_name | selector_role | final_budget_score | pick_for_date_json |\n| --- | --- | --- | --- | --- | --- |\n| 2026-05-06 | MB | qwen3-max-thinking | SELECTED_VOTER | 0.3125 | {} |\n| 2026-05-06 | MB | qwen3.6-plus | CONTROL | 0.3824 | {} |\n| 2026-05-06 | MT | qwen3-coder | SELECTED_VOTER | 0.3431 | {} |\n\n## Role summary\n| run_date | region | selector_role | n | avg_score |\n| --- | --- | --- | --- | --- |\n| 2026-05-05 | MB | CONTROL | 4 | 0.428 |\n| 2026-05-05 | MB | SELECTED_VOTER | 4 | 0.3494 |\n| 2026-05-05 | MB | SKIP_TODAY | 11 | 0.2478 |\n| 2026-05-05 | MB | WATCH_ONLY | 10 | 0.2281 |\n| 2026-05-05 | MN | CONTROL | 4 | 0.4747 |\n| 2026-05-05 | MN | SELECTED_VOTER | 6 | 0.5241 |\n| 2026-05-05 | MN | SKIP_TODAY | 3 | 0.2223 |\n| 2026-05-05 | MN | WATCH_ONLY | 16 | 0.3198 |\n| 2026-05-05 | MT | CONTROL | 4 | 0.4371 |\n| 2026-05-05 | MT | SELECTED_VOTER | 4 | 0.4305 |\n| 2026-05-05 | MT | SKIP_TODAY | 7 | 0.2303 |\n| 2026-05-05 | MT | WATCH_ONLY | 14 | 0.2811 |\n| 2026-05-06 | MB | CONTROL | 4 | 0.3653 |\n| 2026-05-06 | MB | SELECTED_VOTER | 4 | 0.328 |\n| 2026-05-06 | MB | SKIP_TODAY | 11 | 0.2568 |\n| 2026-05-06 | MB | WATCH_ONLY | 10 | 0.1853 |\n| 2026-05-06 | MN | CONTROL | 4 | 0.5532 |\n| 2026-05-06 | MN | SELECTED_VOTER | 6 | 0.54 |\n| 2026-05-06 | MN | SKIP_TODAY | 1 | 0.0935 |\n| 2026-05-06 | MN | WATCH_ONLY | 18 | 0.3958 |\n| 2026-05-06 | MT | CONTROL | 4 | 0.3892 |\n| 2026-05-06 | MT | SELECTED_VOTER | 4 | 0.3345 |\n| 2026-05-06 | MT | SKIP_TODAY | 11 | 0.247 |\n| 2026-05-06 | MT | WATCH_ONLY | 10 | 0.1781 |\n"

### Measurement audit

"# Measurement surfaces\n\n## Latency\n| date | region | rows | latency_available | missing |\n| --- | --- | --- | --- | --- |\n| 2026-05-04 | MB | 25 | 0 | NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT |\n| 2026-05-04 | MN | 25 | 0 | NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT |\n| 2026-05-04 | MT | 25 | 0 | NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT |\n| 2026-05-05 | MB | 27 | 0 | NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT |\n| 2026-05-05 | MN | 27 | 0 | NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT |\n| 2026-05-05 | MT | 27 | 0 | NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT |\n| 2026-05-06 | MB | 28 | 0 | NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT |\n| 2026-05-06 | MN | 28 | 0 | NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT |\n| 2026-05-06 | MT | 27 | 0 | NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT |\n\n## Loz stage\n| date | region | rows | top1 | top2 | top10 | loz_miss | pool_miss |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n| 2026-05-04 | MB | 22 | 3 | 3 | 3 | 2 | 1 |\n| 2026-05-04 | MN | 39 | 2 | 3 | 3 | 2 | 0 |\n| 2026-05-04 | MT | 27 | 3 | 6 | 6 | 1 | 3 |\n| 2026-05-05 | MB | 22 | 5 | 5 | 5 | 2 | 3 |\n| 2026-05-05 | MN | 42 | 3 | 5 | 5 | 3 | 2 |\n| 2026-05-05 | MT | 30 | 6 | 6 | 6 | 5 | 0 |\n\n## MT drop\n| date | region | rows | ai_drop | notoken_drop |\n| --- | --- | --- | --- | --- |\n| 2026-05-04 | MT | 5 | 2 | 0 |\n| 2026-05-05 | MT | 5 | 4 | 3 |\n| 2026-05-06 | MT | 4 | 2 | 2 |\n"

## 7. Finding table

| ID | Category | Evidence | Impact | Root cause hypothesis | Proposed action | Risk | Owner confirmation needed? |
|---|---|---|---|---|---|---|---|
| F-01 | DUPLICATE_RISK / HIGH_IMPACT_ON_MEASUREMENT | 15 duplicate `du_doan_test_bundles` groups, all MB 04/05-06/05 | corrupts UI/evaluator/would_save counts | legacy MB engine + multi-region engine both write same logical methods | C-17A dedupe canonical view + unique snapshot key | Low if test-only | YES before migration |
| F-02 | PENDING_AFTER_ACTUAL / HIGH_IMPACT_ON_MEASUREMENT | 06/05 MN/MT/MB have PENDING rows despite actual joined | evidence cannot be trusted silently | evaluator not automatically hooked after actual/result closeout | C-03 natural post-closeout hook + failed-state labels | Low | YES |
| F-03 | READINESS_GAP / HIGH_IMPACT_ON_UI_TRUST | no snapshot_type/readiness fields in bundle rows | PRE_RESULT vs diagnostic ambiguous | current mode string is insufficient | C-17B output lock table/fields | Medium schema change, test-only | YES |
| F-04 | C05_DEPLOYED_PENDING_NEXT_MODEL_CALL | latency rows 06/05 still 0 | cannot prune/cost optimize | model calls occurred before instrumentation deploy | verify 07/05 trace then materialize | Low | NO for verify |
| F-05 | C16_EXPLAINABILITY_GAP | 3 selected voters empty pick | selected voters may be incomplete | C-16 selected by score even no same-day pick | C-16 daily explainability audit + readiness excludes empty selected voters | Low | YES for gating change |
| F-06 | OFFICIAL_LOCKED | hard locks intact | official safe | n/a | no official change | n/a | YES for any official change |

## 8. P0 implementation plan

### P0-A C-17A idempotency/dedupe

Files likely touched:

- `_du_doan_test_schema.py`
- `_du_doan_test_engine.py`
- `_du_doan_test_mb_engine.py`
- `_du_doan_test_daily_runner.py`
- `main.py` API read layer

Tables:

- add/derive canonical fields in `du_doan_test_runs/bundles/results`
- possible new table `du_doan_test_snapshot_registry`

Safety:

- test-only tables only
- mark duplicates as `DUPLICATE_NON_CANONICAL`, do not delete blindly

Verification:

```sql
SELECT run_date, region, experiment_name, snapshot_type, COUNT(*)
FROM du_doan_test_bundles
GROUP BY run_date, region, experiment_name, snapshot_type
HAVING COUNT(*) > 1;
```

Rollback:

- revert schema additions if only additive
- keep duplicate rows historical but UI filters canonical only

### P0-B C-17B output lock/readiness

Add explicit fields/status:

- snapshot_type
- trigger_source
- input_cutoff_time
- output_created_at
- actual_available_at_creation
- created_before_result
- selected_voter_count_expected/done
- selected_voter_missing_json
- lock_status
- readiness_status
- dedupe_key

Statuses:

- READY_PRE_RESULT_LOCKED
- PARTIAL_BUDGET_LOCKED
- ACTUAL_ALREADY_EXISTS_BLOCKED
- POST_CLOSEOUT_DIAGNOSTIC_ONLY
- DUPLICATE_BLOCKED
- EVALUATOR_PENDING
- EVALUATOR_FAILED

### P0-C C-03 evaluator hook

Current evaluator works manually for all regions after V63, but natural hook is not yet proven.

Plan:

- run after actual scrape/verify per region
- update all eligible rows from PENDING to WIN/LOSE/PARTIAL/N/A/EVALUATOR_FAILED
- write evaluator timestamp/status

Verification:

```sql
SELECT run_date, region, COUNT(*)
FROM du_doan_test_results
WHERE test_bt_status='PENDING'
  AND run_date IN (SELECT date FROM lottery_results)
GROUP BY run_date, region;
```

### P0-D C-05 latency proof

Instrumentation is deployed, but not live-proven until next model call.

Plan:

- after 07/05 model calls, re-run materializer
- require `latency_available > 0`
- only then feed C-16 latency score

## 9. P1/P2 plan

P1:

- C-16 daily explainability audit
- C-04 auto-wire after C-17A/B + C-03 clean 3-5 closeouts
- C-07 MT correct-but-dropped UI

P2:

- C-14 strength chips
- C-15 MB blackspot UI
- V55 Google 14-day evidence pack

## 10. Do-not-do list

- Do not change official `/du-doan`.
- Do not change official final bundle generation.
- Do not prune models before C-05 live proof.
- Do not promote C-16 official.
- Do not promote MT AI-chain.
- Do not treat POST_CLOSEOUT_DIAGNOSTIC as realtime proof.
- Do not count duplicate MB rows as independent evidence.

## 11. Decision gates

Before 14/30-day evidence collection can be trusted:

1. Dedupe canonical rows must pass.
2. Readiness/snapshot fields must exist.
3. Evaluator must clear PENDING after actuals.
4. Latency must become available for new model calls.
5. C-16 selected voters must not include empty-pick rows as complete.

## 12. Open owner questions

No blocker question for audit. Implementation of C-17A/B schema changes needs owner approval.

## 13. Final recommendation

Next safest deployment batch:

1. C-17A idempotency/dedupe guard
2. C-17B output lock/readiness gate
3. C-03 evaluator natural hook
4. C-16 daily explainability audit
5. C-05 verify on next model calls (already deployed, do not change again until proof)

This is more urgent than UI expansion because evidence trust is currently blocked by duplicate and readiness/evaluator states.

## Final owner-facing answers

1. Total experimental line remains the correct direction.
2. It is blocked by duplicate MB rows, missing snapshot/readiness contract, evaluator pending states, and latency not live-proven.
3. Fix first: C-17A + C-17B + C-03 natural hook.
4. Must not touch official output, prompt, roster, voting, pruning.
5. More deep report is not needed before implementation; the blockers are clear.
6. Safest next deployment batch is C-17A/C-17B/C-03 hook, then verify C-05 on next model calls.
