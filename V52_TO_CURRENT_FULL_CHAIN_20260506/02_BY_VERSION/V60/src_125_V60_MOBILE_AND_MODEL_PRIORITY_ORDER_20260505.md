# V60 — Mobile two-column UI + model priority ordering

**Date:** 2026-05-05 23:42 VN  
**Scope:** `/du-doan-test` UI readability + shadow model execution order  
**Official impact:** none

---

## Owner request

1. Mobile `/du-doan-test` must stay visually understandable with 2 columns: official vs test.
2. With many models, fast/no-token lanes should run first, then AI/shadow models should run sequentially by strength for the region/weekday/station bucket.
3. Strong models must be prioritized so useful test output is available before weak long-tail models finish.

---

## Changes

### Mobile UI

`web/frontend/du-doan-test.html`

- Mobile `compare-grid` now keeps 2 columns: official/test.
- Reduced card padding, font sizes, icons, badges, and gaps for small screens.
- Removed the previous 1-column/so-le stacking behavior for compare cards.

### Shadow model order

`web/backend/scheduler.py`

Added `_order_shadow_models_for_region(models, region, date_str)`.

Order source:

1. Prefer C-16 `du_doan_test_selected_voters` rows for the date/region:
   - `CONTROL`
   - `SELECTED_VOTER`
   - `WATCH_ONLY`
   - then skipped/remaining
2. If no C-16 rows exist yet, fallback to latest `model_strength_by_region_weekday_station_daily` helpful/BT strength.
3. If lookup fails, fallback to registry order and logs `[SHADOW_ORDER_ERR]`.

No-token models already run in the earlier `04:00_all_regions` batch, before AI/shadow token calls. This patch affects only `shadow_auto_eval` sequencing.

---

## Verified order for 2026-05-05

### MN

```text
gpt-oss-120b, glm-5.1, qwen3.6-plus, kimi-k2.5,
grok-4.20-multi-agent, qwen3-coder, qwen3-max-thinking,
deepseek-v4-pro, gpt-5.5, deepseek-v4-flash,
gemini-3.1-pro, gemini-3-flash, gemma-4-31b
```

### MT

```text
gpt-oss-120b, grok-4.20-multi-agent, qwen3-coder, glm-5.1,
kimi-k2.5, qwen3-max-thinking, qwen3.6-plus, gpt-5.5,
deepseek-v4-flash, deepseek-v4-pro,
gemini-3.1-pro, gemini-3-flash, gemma-4-31b
```

### MB

```text
qwen3.6-plus, qwen3-coder, glm-5.1, qwen3-max-thinking,
grok-4.20-multi-agent, kimi-k2.5, gpt-oss-120b, gpt-5.5,
deepseek-v4-flash, deepseek-v4-pro,
gemini-3-flash, gemini-3.1-pro, gemma-4-31b
```

---

## Verification

```text
systemctl is-active lottery = active
/api/health = 200
```

Scheduler import/compile passed.

---

## Notes

- This does not yet enforce a hard deadline cutoff; it only prioritizes execution order.
- C-05 latency instrumentation is still needed to turn the order into a true time/cost optimizer.
- Future C-16 v2 should mark a test output as `MODEL_BUDGET_COMPLETE` only after selected voter rows have completed, or `PARTIAL_BUDGET_LOCKED` if deadline forces lock before all selected voters finish.

