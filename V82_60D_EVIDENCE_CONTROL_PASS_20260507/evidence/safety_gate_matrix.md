# V82 — Safety classification matrix

Phân loại an toàn cho từng đề xuất, dựa trên 60d evidence ở trên.

| Item | 60d n | Evidence | Verdict |
|---|---|---|---|
| OFFICIAL prediction path | 180 | MN 45.0% / MT 50.0% / MB 25.0% baseline | OFFICIAL_LOCKED |
| AI_HERD as voter | 180 | MN +3.3pp (n=60); MT -6.7pp (12 breaks); MB +1.7pp | DO_NOT_PROMOTE (MT destructive) |
| NO_TOKEN_HERD as voter | 180 | MN +6.7pp (10/14 saves); MT +1.7pp (6 breaks); MB -1.7pp | REGION_SPECIFIC_ONLY (MN only) |
| MN_SPECIALIST_ROSTER_V1 | 60 | MN +6.7pp / 4 saves / 0 breaks | PROMOTION_CANDIDATE_AFTER_DOSSIER |
| MN_AI_CHAIN_PRESERVATION_V1 | 59 | MN +7.5pp / 5 saves / 1 break | PROMOTION_CANDIDATE_AFTER_DOSSIER |
| MT_AI_CHAIN_PRESERVATION_V1 | 60 | MT -8.3pp / 7 saves / 12 breaks | DO_NOT_PROMOTE_MT_DESTRUCTIVE |
| MT_PRIOR_REGION_CONTEXT_SAFE_V1 | 60 | MT -8.3pp / 4 saves / 9 breaks | DO_NOT_PROMOTE_MT_DESTRUCTIVE |
| MB_SPECIALIST_ROSTER_V1 | 41 | MB +11.6pp / 5 saves / 0 breaks (n<60) | WAIT_60D_BACKFILL_MORE_DATA |
| V67_EXPLOIT selector | 1 | Only 1 emit row (2026-05-07) | WAIT_14D_LIVE |
| V70_CONSENSUS selector | 4 | MN 3/4 + MT 4/4 + MB 1/4 (n=12 total, all post-fix) | WAIT_14D_LIVE |
| V73_HYBRID selector | 4 | Trace 15d but emit only 4d | WAIT_14D_LIVE |
| V79 cluster-weighted | 4 | MT 4/4 + MN 2/4 + MB 0/4 (n=12) + 2 breaks MT | WAIT_14D_LIVE_with_cluster_break_watch |
| V79 AI/NO_TOKEN cross-verify | 4 | Same as cluster | WAIT_14D_LIVE |
| V80 rule_phase_synthesis | 4 | Shadow only, no consumer | KEEP_MONITORING_NO_CONSUMER |
| V80 no_token_rule_pack | 4 | Shadow only, no consumer | KEEP_MONITORING_NO_CONSUMER |
| V80 mb_regime_shift | 4 | Diagnostic flag only | KEEP_MONITORING |
| V80 mn_ai_herd_vs_v67_save_daily | 4 | Diagnostic monitor only | KEEP_MONITORING |
| V81 provider shadow pilot | 2 | 18/18 OK, 1 save per model on MN, 0 breaks across 18 calls | WAIT_7D_LIVE_THEN_14D_LIVE |
| Selector promotion (any) | — | Owner-locked | OWNER_GATE_REQUIRED |
| Official prompt change | — | Owner-locked | OFFICIAL_LOCKED |
| Production model swap | — | Owner-locked | OFFICIAL_LOCKED |
| UI panel admin AI/NO_TOKEN/V67/cluster | — | DATA_READY (V79+V80 tables) | DATA_READY_UI_PENDING |

Verdict legend:
- `OFFICIAL_LOCKED` = không bao giờ tự thay đổi.
- `OWNER_GATE_REQUIRED` = cần anh OK + dossier.
- `PROMOTION_CANDIDATE_AFTER_DOSSIER` = đủ 60d evidence, cần dossier để xét test-lane voter (chưa official).
- `WAIT_14D_LIVE` = mới 4d, cần đủ 14d natural live trước khi xét.
- `WAIT_7D_LIVE_THEN_14D_LIVE` = V81 pilot, 7d trước rồi 14d trước khi xét test-lane voter.
- `DO_NOT_PROMOTE` = đã chứng minh xấu hơn / nhiều break hơn save.
- `DATA_READY_UI_PENDING` = backend sẵn, chỉ thiếu UI cho anh quan sát.
- `KEEP_MONITORING_NO_CONSUMER` = shadow chạy nhưng chưa có consumer; an toàn tuyệt đối.