# MN Recovery Deep Dive — V78

## Key Finding

MN official cold streak is real: OFFICIAL 0/4 from 2026-05-04 to 2026-05-07.
On 2026-05-07, V67/V73 recovered MN:

| Signal | Tail | Hit? |
| --- | --- | --- |
| OFFICIAL | 94 | False |
| AI/all herd | 94 (9 models) | False |
| C16 | 94 | False |
| V67 | 95 | True |
| V70 | 94 | False |
| V73 | 95 | True |

## Root Cause Hypothesis

MN AI herd and official path over-weighted the same tail `94`, while V67 exploited the previous official miss / lag-1 edge and selected `95`, which hit. The current production prompt contains a generic warning to avoid repeating numbers that lost continuously. That conflicts with the V66/V67 finding: some previous losers become positive-edge lag-1 candidates and should be evaluated, not automatically discarded.

## Prompt Gap

- `V67_candidate`: missing from production prompt.
- `V73_candidate/tier`: missing from production prompt.
- `agreement_count`: missing.
- `same_region_lag1/lag2`: measured by V66/V67 but not present in prompt.
- Existing self-learning text says: “Tránh lặp lại các số đã LOSE liên tục”, which is harmful when V66/V67 edge is positive.

## Safe Recovery Plan

1. Keep official locked.
2. Use `MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1` in dry-run/shadow only.
3. Tomorrow, compare shadow BT vs OFFICIAL/V67/V70/V73.
4. Do not promote until ≥14 fresh closed days and official promotion gates pass.
