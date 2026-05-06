# V71 — HYBRID_V1 + C-16 score-gate fix

Published: 2026-05-07 02:05 VN.

## Highlights

- C-16 0.42 score gate dropped (was MN-biased). MN/MT/MB all reach target_max=20 voters.
- V71 HYBRID combines CONSENSUS+EXPLOIT+BUDGET into CROWN/HIGH/MEDIUM/LOW/SKIP tiers.
- 14d backfill ALL-region n=42:
  - HYBRID 45.2% [31.2-60.1] vs OFFICIAL 42.9% [29.1-57.8] = +2.3pp
  - **MT TIED OFFICIAL 57.1%** (was -14.2pp under with C-16 alone) - RESCUED
  - **MB +7.1pp vs OFFICIAL** - RESCUED
- HYBRID covers all 42 days (no SKIP).

## Hard contract

Test-lane only. ZERO touching `/du-doan`/`final_bundles`/scoring/model_registry/prompt.
