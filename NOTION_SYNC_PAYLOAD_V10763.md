# V10763 — Pattern-Reasoning Shadow Eval (MB G4 + Evidence Ledger)

**Date:** 2026-06-30  
**Scope:** SHADOW / INFO-only / ZERO official-wallet impact  
**FU:** FU-V10763-PATTERN-REASONING

## Owner Intent

Owner clarified that rules/patterns must not be treated as direct picks. AI/eval must reason over multiple layers: rule, pattern, model votes, agreement, disagreement, hot/cold/gan, and causal validity. A number should be promoted only when independent evidence converges and negative gates do not dominate.

## Implemented

- `_v10763_pattern_reasoning_shadow.py`
  - Reads `MB_G4_Pattern_Tracking.xlsx` as cached pattern metadata.
  - Rebuilds causal MB G4 D-1 candidates from DB.
  - Builds per-tail evidence ledger:
    - AI votes
    - ML/no-token votes
    - combo/smart votes
    - official / money_board
    - cau forward
    - gan
    - MB G4 D-1 transforms
  - Emits ACCEPT / HOLD / REJECT with positive and negative weights.
- `PATTERN_REASONING_RUBRIC_SHADOW_V10763.md`
  - Rule/pattern is evidence, not a command.
  - Pattern-only and gan-only are rejected.
  - ACCEPT requires at least two independent layers and model support.
- `/api/admin/pattern-reasoning`
  - Admin-only, no-store, readout API.
- `/monitoring`
  - New panel: PATTERN REASONING.
  - INFO-only, no staking recommendation.
- Scheduler closeout hook
  - Snapshots V10763 shadow tables after closeout.

## Backfill Result

45-day MB backfill:

| Method | P&L | Hit-days |
|---|---:|---:|
| Pattern reasoning | +1.0M | 16 |
| Official | +5.9M | 17 |

Conclusion: Pattern reasoning is useful as a control/explanation layer, but does not currently beat official. It remains INFO-only and must not be used for staking or official promotion.

## Safety

- Writes only `v10763_pattern_reasoning_shadow` and `v10763_pattern_reasoning_daily`.
- `diagnostic_only=1`, `shadow_only=1`, `output_eligible=0`, `owner_approved=0`.
- No mutation of `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`, wallet, official prompts, or selectors.
- VPS deploy verified: compile OK, backfill OK, health 200, admin endpoint 401, `/monitoring` 401.
- Hash guard: 4 official tables IDENTICAL pre/post.
