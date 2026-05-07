# V78 — AI Prompt + Region Regime Audit (2026-05-07)

> DB Source: VPS_SYNCED via `artifacts/live_sync/20260507_200323/manifest.json`
> Official safety: no official prompt/scoring/final bundle/model roster changes.

## Executive Summary

V78 confirms V77 as latest public truth and extends it with AI/prompt forensic. MN/MB official cold streak is real. MN has a clear recovery path in test-lane: V67/V73 selected `95` and saved 2026-05-07 while AI/official herd selected `94` and missed. MB is harder: all methods remain cold over the incident window and needs regime-shift monitoring plus uncertainty/diversification shadow prompt, not immediate selector changes.

## V77 Fix Health

- 19:00 and 19:05 cron registered.
- A runtime timezone bug in those jobs and the 23:35→23:50 selector chain was found (`datetime.now(VN_TZ)` while `VN_TZ` is a string) and fixed by using `_today_vn_date_str()` / `_tomorrow_vn_date_str()`.
- VPS `/api/health=200` after deploy.
- V77 materializers smoke PASS after patch.
- V78 prompt shadow audit cron registered at 19:10 VN, no provider calls.

## AI Herd Summary

| date | region | herd_tail | herd_count | herd_hit | official | v67 | v73 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-04 | MN | 65 | 7 | False | 65 | None | 65 |
| 2026-05-04 | MT | 82 | 6 | True | 29 | None | 82 |
| 2026-05-04 | MB | 46 | 6 | True | 09 | None | 09 |
| 2026-05-05 | MN | 52 | 9 | True | 15 | None | 15 |
| 2026-05-05 | MT | 52 | 7 | True | 44 | None | 44 |
| 2026-05-05 | MB | 41 | 10 | False | 83 | None | 41 |
| 2026-05-06 | MN | 95 | 11 | False | 95 | None | 95 |
| 2026-05-06 | MT | 71 | 15 | True | 11 | None | 71 |
| 2026-05-06 | MB | 49 | 7 | False | 79 | None | 32 |
| 2026-05-07 | MN | 94 | 9 | False | 94 | 95 | 95 |
| 2026-05-07 | MT | 40 | 9 | False | 88 | 95 | 88 |
| 2026-05-07 | MB | 37 | 5 | False | 20 | 79 | 79 |

## NO_TOKEN vs AI

| region | class | hits | n | hit_rate |
| --- | --- | --- | --- | --- |
| MB | NO_TOKEN | 7 | 28 | 25.0 |
| MB | TOKEN | 16 | 81 | 19.8 |
| MN | NO_TOKEN | 7 | 28 | 25.0 |
| MN | TOKEN | 20 | 81 | 24.7 |
| MT | NO_TOKEN | 18 | 28 | 64.3 |
| MT | TOKEN | 44 | 81 | 54.3 |

## Prompt Coverage Verdict

| field | prompt | context | trace | fix | note |
| --- | --- | --- | --- | --- | --- |
| previous_official_miss | True | True | False | PARTIAL | self-history exists but not official final_bundle miss context |
| previous_lo2_miss | True | True | False | PARTIAL | not explicitly injected as prior LO2 miss candidate |
| same_region_lag1 | False | False | False | MISSING | not in official prompt; V66/V67 exists in test-lane only |
| same_region_lag2 | False | False | False | MISSING | not in official prompt; V66.1 measures it only |
| cross_region_sameday | True | True | False | PARTIAL | inter-region source data present for MT/MB |
| cross_region_nextday | False | False | False | MISSING | not in official prompt |
| V67_candidate | False | False | False | SHADOW_PROMPT_REQUIRED | not in official prompt |
| V70_consensus_candidate | False | True | False | SHADOW_PROMPT_REQUIRED | not in official prompt |
| V73_candidate/tier | False | True | False | SHADOW_PROMPT_REQUIRED | not in official prompt |
| agreement_count | False | False | False | SHADOW_PROMPT_REQUIRED | not in official prompt |
| no_token_herd_candidate | False | False | False | MISSING | only model ranking, no daily no-token herd candidate |
| ai_herd_candidate | False | False | False | MISSING | post-prediction diversity pass exists, not pre-prompt context |
| official_tail | False | False | False | MISSING | not injected into prompt for same target day |
| recent_model_failure_streak | True | True | True | PARTIAL | self WR exists; model-specific failure streak partial |
| region-specific doctrine | True | True | False | PARTIAL | generic region caution exists; not V78 specialist split |
| anti-herding instruction | True | True | False | PARTIAL | generic anti-herding exists |
| MB volatility warning | True | True | False | PARTIAL | present generic; lacks current cold-streak input |
| MN lag1 exploit instruction | True | True | False | SHADOW_PROMPT_REQUIRED | opposite instruction: avoid yesterday loses |
| MT consensus-first instruction | True | True | False | SHADOW_PROMPT_REQUIRED | not explicit by region |

## Implemented Now

- Created three shadow prompt files:
  - `MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md`
  - `MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md`
  - `MT_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md`
- Created materializer `web/backend/_materialize_ai_region_prompt_shadow_audit.py`.
- Created 6 shadow tables:
  - `ai_prompt_context_audit_shadow`
  - `ai_region_specialist_prompt_shadow_results`
  - `ai_herding_failure_daily`
  - `official_vs_testlane_rescue_daily`
  - `mn_mb_failure_streak_daily`
  - `method_cluster_performance_daily`
- Added scheduler cron 19:10 VN: V78 prompt shadow audit, no provider calls.
- Deployed to VPS and smoke-ran 86 rows with all safety flags valid.

## Not Changed

- `/du-doan`
- `/api/final-bundle`
- official `final_bundles`
- official prompt production
- official scoring/voting
- official model roster
- production cascade
- provider AI calls for shadow prompts

## Next 24h Watch

1. Verify 19:00 V77 post-cascade rerun fires tomorrow.
2. Verify 19:05 fast incident monitor fires tomorrow.
3. Verify 19:10 V78 prompt shadow audit fires tomorrow.
4. Check MN whether V67/V73 continues saving vs official herd.
5. Check MB if all-method cold persists; escalate after 7 additional days if still cold.
