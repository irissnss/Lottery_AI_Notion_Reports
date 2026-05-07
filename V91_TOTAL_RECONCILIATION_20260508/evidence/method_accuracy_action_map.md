# V91 — Method Accuracy Action Map

Generated 2026-05-08T01:19:20+07:00

Per-region 60d Wilson CI from V82 audit + V81 pilot data.

| Method | Region | n | Hit rate | Wilson 95% CI | Save | Break | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OFFICIAL | MN | 60 | 45.0% | [33.1, 57.5] |  |  | BASELINE |
| OFFICIAL | MT | 60 | 50.0% | [37.7, 62.3] |  |  | BASELINE_STRONG |
| OFFICIAL | MB | 60 | 25.0% | [15.8, 37.2] |  |  | BASELINE_WEAK |
| AI_HERD | MN | 60 | 48.3% | [36.2, 60.7] | 6 | 4 | PARITY+ |
| AI_HERD | MT | 60 | 43.3% | [31.6, 55.9] | 8 | 12 | DESTRUCTIVE_-6.7pp |
| AI_HERD | MB | 60 | 26.7% | [17.1, 39.0] | 12 | 11 | NOISY |
| NO_TOKEN_HERD | MN | 60 | 51.7% | [39.3, 63.8] | 14 | 10 | PARITY (region-specific) |
| NO_TOKEN_HERD | MT | 60 | 51.7% | [39.3, 63.8] | 7 | 6 | PARITY |
| NO_TOKEN_HERD | MB | 60 | 23.3% | [14.4, 35.4] | 5 | 6 | PARITY- |
| MN_SPECIALIST_ROSTER_V1 | MN | 60 | 51.7% | [39.3, 63.8] | 4 |  | PROMOTION_CANDIDATE_CLEAN |
| MN_AI_CHAIN_PRESERVATION_V1 | MN | 59 | 52.5% | [40.0, 64.7] | 5 | 1 | PROMOTION_CANDIDATE |
| MT_AI_CHAIN_PRESERVATION_V1 | MT | 60 | 41.7% | [30.1, 54.3] | 7 | 12 | DESTRUCTIVE_PROVEN_60D |
| MT_PRIOR_REGION_CONTEXT_SAFE_V1 | MT | 60 | 41.7% | [30.1, 54.3] | 4 | 9 | DESTRUCTIVE_PROVEN_60D |
| MB_SPECIALIST_ROSTER_V1 | MB | 41 | 36.6% | [23.6, 51.9] | 5 |  | PROMISING_LIMITED_SAMPLE_n41 |
| V67_EXPLOIT (MN) | MN | 1 | 100% | [20.7, 100] | 1 |  | INSUFFICIENT_SAMPLE_RECENT |
| V70_CONSENSUS | MT | 4 | 100% | [51, 100] |  |  | INSUFFICIENT_SAMPLE_4D |
| V73_HYBRID | MT | 4 | 100% | [51, 100] |  |  | INSUFFICIENT_SAMPLE_4D |
| V79 cluster_weighted | MT | 4 | 25% | [5, 70] |  | 2 | INSUFFICIENT_4D_2_BREAKS_MT |
| V81 deepseek-chat | MN | 2 | 50% | [9, 91] | 1 |  | INSUFFICIENT_2D |
| V81 claude-sonnet-4-6 | MN | 2 | 50% | [9, 91] | 1 |  | INSUFFICIENT_2D |
| V81 gemini-3-flash | MN | 2 | 50% | [9, 91] | 1 |  | INSUFFICIENT_2D |
