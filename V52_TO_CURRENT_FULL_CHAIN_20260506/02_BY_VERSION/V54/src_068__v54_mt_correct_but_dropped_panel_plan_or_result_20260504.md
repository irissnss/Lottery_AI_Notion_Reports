# V54 C-07 — MT Correct-But-Dropped UI Panel Plan

> Status: `READY_FOR_UI_TEST_ONLY_NOT_DEPLOYED`  
> Reason: C-06 backend measurement landed first; UI panel will consume both `mt_model_hit_output_drop_shadow` and new `loz_stage_trace_shadow` after one more closed day.

## Data Sources

- `mt_model_hit_output_drop_shadow` (V52.1/V52.2): rolling 60d.
- `loz_stage_trace_shadow` (V54): stage trace per actual tail.

## Panel Contents

Add to `/du-doan-test` only:

- 7/14/30/60 MT summary:
  - `LOZ_LINE_SELECTION_MISS`
  - `AI_SIGNAL_DROPPED`
  - `NOT_IN_CANDIDATE_UNIVERSE`
  - `CANDIDATE_POOL_MISS`
- Latest closed date detail:
  - actual tail;
  - model(s) that had it;
  - model family;
  - candidate rank/score;
  - official BT/lo2;
  - test method picks;
  - drop stage.

## Owner Labels

- `Model có tín hiệu nhưng final bỏ`
- `Không vào candidate pool`
- `Line loz chọn sai`
- `Test cứu được`
- `Test cũng miss`

## Safety

UI-test-only. No official output change.
