# V79 — AI ↔ NO_TOKEN Cross Verification + Cluster-Weighted Consensus

> DB Source: VPS_SYNCED via `artifacts/live_sync/20260507_211721/manifest.json`
> Official safety: no official prompt/scoring/final bundle/model roster changes.

## Executive Summary

Production AI prompt currently has model ranking/self-history but does **not** truly see the daily NO_TOKEN herd, AI herd, V67/V70/V73/C16, or independent cluster count before model output. V79 implements a shadow-only cross-verification materializer and cluster-weighted consensus table. It caps raw AI herd influence, gives NO_TOKEN a protected floor when present, and treats V67/V70/V73/C16 as independent clusters. Official remains diagnostic/control only.

## Current Answer to Owner

| Question | Answer |
| --- | --- |
| AI có soi no-token trước khi chốt không? | **PARTIAL / mostly NO**. It sees broad model rankings, not daily no-token herd candidate. |
| Có daily no-token herd candidate không? | Trước V79: no. V79: yes in `ai_no_token_cross_verification_shadow`. |
| Có AI herd candidate không? | Trước V79: only post-prediction diversity pass, not prompt context. V79: yes. |
| Có independent_cluster_count không? | Trước V79: no. V79: yes. |
| Có so AI vs NO_TOKEN vs V67/V70/V73/C16 không? | Trước V79: no full layer. V79: yes shadow-only. |

## 4-day Shadow Backtest

| target_date | region | ai_herd_tail | no_token_herd_tail | v67_tail | v70_tail | v73_tail | c16_tail | official_tail | cluster_weighted_tail | independent_cluster_count | ai_vs_no_token_relation | would_save | would_break | actual_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-04 | MB | 46 | 38 | None | 09 | 09 | None | 09 | 09 | 4 | MB_ALL_METHOD_COLD | 0 | 0 | LOSE |
| 2026-05-04 | MN | 65 | 32 | None | 65 | 65 | None | 65 | 65 | 5 | AI_DISAGREES_NO_TOKEN | 0 | 0 | LOSE |
| 2026-05-04 | MT | 82 | 29 | None | 82 | 82 | None | 29 | 82 | 4 | AI_DISAGREES_NO_TOKEN | 0 | 0 | WIN |
| 2026-05-05 | MB | 41 | 83 | None | 41 | 41 | 41 | 83 | 41 | 6 | MB_ALL_METHOD_COLD | 0 | 0 | LOSE |
| 2026-05-05 | MN | 52 | 15 | None | 15 | 15 | 52 | 15 | 52 | 4 | V73_CONTRADICTS_AI_HERD | 1 | 0 | WIN |
| 2026-05-05 | MT | 52 | 44 | None | 44 | 44 | 52 | 44 | 44 | 4 | V73_CONTRADICTS_AI_HERD | 0 | 0 | WIN |
| 2026-05-06 | MB | 49 | 92 | None | 32 | 32 | 79 | 79 | 32 | 5 | MB_ALL_METHOD_COLD | 0 | 0 | LOSE |
| 2026-05-06 | MN | 95 | 46 | None | 95 | 95 | 95 | 95 | 95 | 6 | AI_DISAGREES_NO_TOKEN | 0 | 0 | LOSE |
| 2026-05-06 | MT | 71 | 99 | None | 71 | 71 | 71 | 11 | 71 | 5 | AI_DISAGREES_NO_TOKEN | 0 | 0 | WIN |
| 2026-05-07 | MB | 37 | 64 | 79 | 20 | 79 | 20 | 20 | 20 | 4 | MB_ALL_METHOD_COLD | 0 | 0 | LOSE |
| 2026-05-07 | MN | 94 | 76 | 95 | 94 | 95 | 94 | 94 | 95 | 2 | V67_CONTRADICTS_AI_HERD | 1 | 0 | WIN |
| 2026-05-07 | MT | 40 | 88 | 95 | 88 | 88 | 88 | 88 | 88 | 5 | V73_CONTRADICTS_AI_HERD | 0 | 0 | WIN |


## Result

- V79 cluster-weighted shadow saved MN 2026-05-07 by selecting `95` instead of AI/official herd `94`.
- MT remains consensus-first and selects `88` on 2026-05-07.
- MB remains cold; V79 marks MB as all-method cold rather than forcing high confidence.

## Implemented

- New `web/backend/_materialize_ai_no_token_cross_verification_shadow.py`.
- New tables:
  - `ai_no_token_cross_verification_shadow`
  - `cluster_weighted_consensus_shadow`
- New scheduler cron 19:08 VN, shadow-only, no provider calls.

## Not changed

- `/du-doan`, `/api/final-bundle`, official `final_bundles`, official scoring/voting, official prompt, model roster, production cascade.
