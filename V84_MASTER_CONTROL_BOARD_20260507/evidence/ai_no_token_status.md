# AI ↔ NO_TOKEN cross-check status (V79)

## Implementation

- Materializer: `web/backend/_materialize_ai_no_token_cross_verification_shadow.py`
- Tables: `ai_no_token_cross_verification_shadow` (12 rows, 4d), `cluster_weighted_consensus_shadow` (130 rows, 4d × 3 regions × candidates)
- Cron: 19:08 VN daily (registered V79)
- Schema includes: ai_herd_tail, no_token_herd_tail, v67_tail, v70_tail, v73_tail, c16_tail, official_tail, cluster_weighted_tail, independent_cluster_count, ai_vs_no_token_relation, ai_no_token_agree, herd_risk_flag, would_save, would_break, false_promotion, actual_status, created_before_result.

## 4d backfill result (per V79 report)

| Region | OFFICIAL | AI herd | NO_TOKEN | Cluster | Save | Break |
|---|---|---|---|---|---|---|
| MN | 0/4 | 0/4 | 0/4 | 0/4 | 0 | 0 |
| MT | 3/4 | 0/4 | 2/4 | 1/4 | 0 | 2 |
| MB | 0/4 | 1/4 | 1/4 | 0/4 | 0 | 0 |

## Maturity gate

- 4d/14d → INSUFFICIENT_SAMPLE.
- Need 7d (2026-05-14) for first rolling proof.
- Need 14d (2026-05-21) for promotion proposal eligibility.

## Region-specific 60d (from V82, computed independently)

| Region | NO_TOKEN | AI | Δ | Recommendation |
|---|---|---|---|---|
| MN | 51.7% | 48.3% | +3.4pp | KEEP_BALANCED |
| MT | 51.7% | 43.3% | +8.3pp | AI_CAP_DECREASE (region-specific) |
| MB | 23.3% | 26.7% | -3.3pp | REGION_SPECIFIC_ONLY (do not raise NO_TOKEN MB) |

## Status

- DEPLOYED + 4d shadow data + 60d AI/NO_TOKEN baseline known
- WAIT_7D + WAIT_14D gates
- KHÔNG được raise NO_TOKEN floor toàn cục (region delta khác)
- KHÔNG được promote cluster_weighted vào official trước 14d natural live + dossier
