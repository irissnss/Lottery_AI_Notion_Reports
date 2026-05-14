# V105.41 Morning Comprehensive Report — 2026-05-14

Generated VN time: 2026-05-14 09:25

## 1. Executive verdict

- Day-control morning audit at the start of the 2026-05-14 live cycle.
- Read-only mode honored: no deploy, no restart, no provider/manual AI call, no trigger change.
- Yesterday 2026-05-13 cycles closed naturally for all three regions. MN/MT/MB final bundles all `status=ACTIVE` with `generation_method=weighted_voting_wr` and `consensus_level=strong`.
- MT 5-model token watch fully recovered in the 16:30 cycle; the morning 04:36 closed-file shadow events did not repeat.
- Today 2026-05-14 MN 04:15 cycle is clean: 15/15 auto_daily models valid, final bundle ACTIVE with strong consensus.
- Closed-file regression persists. The DB-level runtime contract (V105.30d) absorbed every event — official prediction path was not affected. But the regression spans more sites than V105.40 morning believed; details in §6.
- `V105.40 _safe_stdio_ctx expansion patch` is not yet deployed — service has been continuously active since 12 May 19:38:50 VN (uptime 26d 8h, no restart since V105.35 deploy).
- `/api/review-hub/filter` user-facing endpoint still returns HTTP 500 `I/O operation on closed file.` for all three regions — known V105.40b finding from yesterday.

## 2. Yesterday outcome (2026-05-13)

Final bundle verified status:

| Region | id | BT | lo2 | lo3 | xien2 | xien3 | model_count | BT status | lo2 status | lo3 status | xien2 status | xien3 status |
|---|---:|---|---|---|---|---|---:|---|---|---|---|---|
| MN | 301 | 23 | [23, 32] | 523 | [23, 32] | [23, 32, 37] | 15 | LOSE | PARTIAL | LOSE | LOSE | LOSE |
| MT | 302 | 92 | [92, 11] | 192 | [92, 11] | n/a | 15 | WIN | WIN | LOSE | WIN | N/A |
| MB | 303 | 32 | [32, 02] | 432 | [32, 02] | [32, 02, 50] | 13 | LOSE | LOSE | LOSE | LOSE | LOSE |

Lottery actual:

| Region | Station | tail |
|---|---|---|
| MB | Bắc Ninh | 38 |
| MN | Cần Thơ | 04 |
| MN | Sóc Trăng | 51 |
| MN | Đồng Nai | 15 |
| MT | Khánh Hòa | 70 |
| MT | Đà Nẵng | 92 |

Notes:
- MT BT=92 matched Đà Nẵng tail=92 — best outcome of the day.
- MN BT=23 missed; lo2 PARTIAL because 32 appears in the supporting set even though 23 did not draw. The system explicitly flagged Wednesday MN as the weakest weekday in the day's reasoning, so this aligns with risk model expectations.
- MB BT=32 lost. None of the seven MB lane-test challenger experiments diverged from the official BT=32, so the loss was systemic across challengers rather than a missed bet by the publisher.

## 3. MT 5-model token recovery

The five token models that morning of 13/5 failed with closed-file class were:

- `gpt-5-mini`
- `claude-sonnet-4-6`
- `gemini-2.5-flash`
- `claude-opus-4-20250514`
- `deepseek-reasoner`

In the 16:30 MT cycle each model returned exactly one prediction row through `run_source='ai_chain'` with `n_nums=2`. None of the five repeated the closed-file failure. The cascade rerun completed naturally.

Label: `MT_5_MODEL_RECOVERED_AFTERNOON_13_5`.

## 4. MB official vs lane-test forensic

| Experiment | test_bt | official_bt | Outcome (cùng official LOSE) |
|---|---|---|---|
| MB_OFFICIAL_BASELINE_CONTROL | 32 | 32 | cùng LOSE |
| MB_COMPOSITE_CHALLENGER_V2 | 32 | 32 | cùng LOSE |
| MB_TIER_AWARE_BUNDLE_SHADOW_V1 | 32 | 32 | cùng LOSE |
| MB_AI_CHAIN_PRESERVATION_V1 | 32 | 32 | cùng LOSE |
| MB_SPECIALIST_ROSTER_V1 | null | 32 | challenger did not commit |
| MB_PRIOR_REGION_CONTEXT_SAFE_V1 | 32 | 32 | cùng LOSE |
| MB_NO_TOKEN_HERD_REDUCTION_V1 | 32 | 32 | cùng LOSE |

Compared with 12/5 (official 34 WIN, challenger 36 LOSE), today's data shows no challenger divergence — every lane-test simply mirrored the official. `DO_NOT_PROMOTE_MB_CHALLENGER` remains in effect; promotion would not have helped today.

## 5. Today live state (2026-05-14)

### 5.1 MN cycle (04:15)

| Field | Value |
|---|---|
| Final bundle | id=304, region=MN, status=ACTIVE |
| Generation method | weighted_voting_wr |
| Consensus level | strong |
| BT | 16 |
| lo2 | [16, 35] |
| lo3 | 616 |
| xien2 | [16, 35] |
| xien3 | [16, 35, 04] |
| model_count | 15 |
| created / updated | 2026-05-14 04:22:11 |

All 15 auto_daily models produced valid 2-number arrays. Several models (claude-opus-4, claude-sonnet-4-6, gemini-2.5-pro, gpt-5-mini) converged on tail 35 supported by an MN(D-1) rule on a single source station; combo-no-token picked 16 instead and prevailed in the weighted bundle vote.

### 5.2 MN shadow lane (cron 04:15)

13 shadow rows persisted: 12 SUCCESS + 1 ERROR (`gpt-oss-120b` at 04:25 VN, latency 85.1s, persisted diagnostic empty). Five shadow models had latency > 300s (within the timeout audit class `LATE_AFTER_HARD_TIMEOUT_SHADOW`) but still persisted SUCCESS — shadow lane only, never feeds official.

### 5.3 MT / MB pending

MT cron 16:30 and MB cron 17:35 have not run. MT 5-model watch is active for today.

## 6. Closed-file regression scope (from yesterday DB)

`scheduler_logs` for 2026-05-13 contains 14 closed-file events spanning **seven** distinct code paths. The full list:

| # | Time VN | Source path | Symptom |
|---|---|---|---|
| 1 | 09:33:34 | Excel update | `Lỗi cập nhật Excel: I/O operation on closed file.` |
| 2 | 09:33:34 | Verify final bundle MN | `Verify final bundle MN error: I/O operation on closed file.` |
| 3 | 09:35:57 | Token AI provider wrapper (claude-sonnet-4-6) | `API invocation wrapper error: I/O operation on closed file. (44.6s)` (caught — retry succeeded) |
| 4 | 09:49:09 | Shadow eval (gpt-5.5 / MT) | wrapper error 89.0s → diagnostic row created |
| 5 | 09:53:48 | Shadow eval (gemini-3-flash / MT) | wrapper error 32.7s → diagnostic row created |
| 6 | 10:30:00 | Excel update | repeat |
| 7 | 10:30:00 | Verify final bundle MT | repeat |
| 8 | 10:50:33 | Shadow eval (kimi-k2.5 / MB) | wrapper error 198.6s → diagnostic row created |
| 9 | 11:31:02 | Excel update | repeat |
| 10 | 11:31:02 | Verify final bundle MB | repeat |
| 11 | 11:31:02 | Pattern Tracker | `Lỗi Pattern Tracker: I/O operation on closed file.` |
| 12 | 11:31:02 | Shadow Daily Comparison | `[SHADOW_DAILY_COMPARISON] Error: I/O operation on closed file.` |
| 13 | 13:20:00 | Shadow Rule D1 (MB measurement) | `[SHADOW_RULE_D1] post-MRE/MDE error: I/O operation on closed file.` |
| 14 | 21:25:26 | Shadow eval (gpt-oss-120b / MN) | wrapper error 85.1s → diagnostic row created |

Important: the diagnostic-row contract from V105.30d / V105.34 absorbed every event. No silent missing row in official output. The hardening still left these specific source paths un-wrapped.

## 7. Endpoint smoke

| Endpoint | HTTP | Time |
|---|---:|---:|
| `/api/health` | 200 | <0.1 s |
| `/api/status` | 200 | <0.1 s |
| `/api/final-bundle?region=MN` | 200 | <0.1 s |
| `/api/final-bundle?region=MT` | 200 | <0.1 s |
| `/api/final-bundle?region=MB` | 200 | <0.1 s |
| `/du-doan` | 200 | 0.2 s |
| `/du-doan-test` | 401 (expected admin lock) | <0.1 s |
| `/filter` (review hub page) | 200 | 0.2 s |
| `/api/mined-rules/overview` | 200 | 0.07 s |
| `/api/so-gan?target_region=MN` | 200 | 0.11 s |
| `/api/review-hub/filter?target_region=MN/MT/MB` | **500** | 0.08 s |
| Public raw `LATEST_REPORT.json` | 200 | — |

`/api/review-hub/filter` 500 is the V105.40b finding: `traceback.print_exc()` in the endpoint's `except` block raises after systemd closed stdio. Page `/filter` overview tab stays stuck on "Đang tải tổng quan…" for users. Until the V105.40 expansion patch deploys, owner workaround is to use `/du-doan`, `/api/mined-rules/overview`, `/api/so-gan` directly.

## 8. Public SSOT vs Drive / Notion

- Public GitHub raw root was at V105.35 throughout 12-14/5. This V105.41 wrapper is the next public-safe push after that.
- V105.36, V105.38, V105.39, V105.40 evidence existed locally / in Notion but the public mirror had a long-standing dirty working tree (line-ending reverts) that blocked safe pushes. V105.41 publishes alongside V105.36 CLOSEOUT_AUDIT_ONLY wrapper to clear the backlog in one consistent step.
- Notion FINAL TRUTH page remains the secondary SSOT and was updated at every step from V105.35 → V105.41.

## 9. Provider / manual / trigger proof

- `manual_provider` count for 13/5 + 14/5 in `scheduler_logs`: 0.
- `traceback` text in journal since 12/5 22:54: 0 (journal text grep is not reliable — closed-file events are absorbed before journal write).
- Trigger / cron unchanged: MN auto cron fired at 04:15 on both 12/5, 13/5, 14/5. Verified-bundle cron at 18:30 MB ran on 13/5 with first-source-success retry — final bundle MB had `verified_at` populated.
- Service uptime 26d 8h. No restart since 12/5 19:38:50 VN.

## 10. Remaining blockers

1. `FU-V105-41-CLOSED-FILE-REGRESSION-MULTI-SITE` (new). 14 sites observed in one day.
2. `FU-V105-40-SAFE-STDIO-EXPANSION`. Owner gate pending — Option A from yesterday (deploy + restart after MB cycle close ~19:00 VN) was not authorized last night, so the patch did not ship.
3. `MN_SHADOW_CLOSED_FILE_RECURRED_2026_05_14_GPT_OSS_120B`. One ERROR row this morning.
4. `MN_SHADOW_LATE_RESULT_OVER_HARD_TIMEOUT_SEVERAL_MODELS`. Shadow-only; never feeds official.
5. `MB_OFFICIAL_AND_LANE_TEST_BOTH_LOSE_2026_05_13`. Investigation pending — model decision quality, not gate semantics.
6. `BLOCKED_BY_DIRTY_PUBLIC_MIRROR`. Cleared in this V105.41 push.
7. `EXCEL_WRITER_CLOSED_FILE_3X_DAILY` + `VERIFY_FINAL_BUNDLE_CLOSED_FILE_3X_DAILY`. Operational, not data-integrity — bundle hits still verified.

## 11. Owner decisions needed

1. OK V105.40 deploy + service restart after MB 17:35 close today (~19:00 VN).
2. OK extended V105.40 scope to cover Excel writer, verify-final-bundle path, Pattern Tracker, Shadow Daily Comparison, Shadow Rule D1 materializer.
3. Day-control hard lock preserved through MT 16:30 and MB 17:35 cycles.
4. Public mirror cleanup pushed in this release alongside V105.36 + V105.41 wrappers (V105.38/V105.39 evidence is staged via Notion + private artifacts; not pushed today to keep this release small and reviewable).
5. Timeout `90/300` preserved; V105.38 `500` remains proposal only.
6. Source-pool / prompt / top-2 tuning held until V105.40 patch deploys and the next 24h cycle is clean.

## 12. Final labels

`V105_41_MORNING_COMPREHENSIVE_AUDIT` · `NATURAL_VERIFY_PARTIAL_PASS_NOT_FULL_PASS` · `V105_40_PATCH_NOT_DEPLOYED_OWNER_GATE_PENDING` · `V105_40_SCOPE_FURTHER_EXTENDED_EXCEL_VERIFY_PATTERNTRACKER_SHADOWCOMPARE_RULED1` · `MN_2026_05_13_BT_LOSE_LO2_PARTIAL_T4_AS_PREDICTED` · `MT_2026_05_13_BT_92_WIN_LO2_WIN_XIEN2_WIN` · `MB_2026_05_13_BT_32_LOSE_ALL_LANES_NO_CHALLENGER_DIVERGENCE` · `MT_5_MODEL_RECOVERED_AFTERNOON_13_5` · `MN_2026_05_14_BT_16_FINAL_BUNDLE_ID_304_ACTIVE_STRONG` · `MN_SHADOW_CLOSED_FILE_RECURRED_2026_05_14_GPT_OSS_120B` · `CLOSED_FILE_REGRESSION_14_SITES_2026_05_13` · `OFFICIAL_PUBLISH_PATH_UNAFFECTED` · `PROVIDER_MANUAL_CALL_0` · `TRIGGERS_UNCHANGED` · `OFFICIAL_SCORING_UNCHANGED` · `OFFICIAL_PROMPT_UNCHANGED` · `OFFICIAL_SELECTOR_UNCHANGED` · `OFFICIAL_ROSTER_PRESERVED` · `WR_BT_FILTER_PRESERVED` · `LANE_TEST_RESERVE_ONLY` · `OFFICIAL_RESERVE_HOLD` · `TIMEOUT_90_300_PRESERVED` · `V105_38_TIMEOUT_500_PROPOSAL_ONLY` · `MT_5_MODEL_WATCH_ACTIVE_FOR_2026_05_14_CRON_16_30` · `MB_CYCLE_PENDING_FOR_2026_05_14_CRON_17_35`.
