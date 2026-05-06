# V59 — Strict LO3 / Xien verification fix for `/du-doan-test`

**Date:** 2026-05-05 23:25 VN  
**Trigger:** Owner correctly challenged that 3-càng was being shown as WIN when it only matched the 2-digit tail.  
**Scope:** API verification semantics for `/du-doan-test` output axes. No official output mutation.

---

## Root cause

`/du-doan-test` API had reintroduced an old bug that official verifier had already fixed:

```text
lo3="446" -> tail "46" -> false WIN if any 2-digit actual tail is 46
```

The wrong logic existed in:

- MB API path around `test_lo3_status`
- MN/MT multi-region API path around `test_lo3_status`

It used:

```python
tail_of_lo3 = str(test_lo3)[-2:]
test_lo3_status = "WIN" if tail_of_lo3 in actual_tail_set else "LOSE"
```

That is wrong for 3-càng.

---

## Correct definition applied

### LO3 / 3-càng

`WIN` only if the full 3-digit number matches a full 3-digit suffix from actual prize values.

Example:

- test lo3 `452`
- actual 2D tail contains `52`
- but no actual 3D suffix `452`
- result = `LOSE`, not WIN

### Xiên 2 / Xiên 3

`WIN` only if all selected 2D tails appear in the same station when station rows exist, matching official verifier semantics.

---

## Code changes

`web/backend/main.py`

Added strict helpers:

- `_du_doan_test_actual_axis_sets(region, date_str)`
- `_du_doan_test_lo3_status(lo3_value, actual_axis_sets)`
- `_du_doan_test_xien_status(values, actual_axis_sets, required_count)`

Replaced both old 2D-tail LO3 verification paths:

- `/api/du-doan-test/mb`
- `/api/du-doan-test/{MN,MT}`

Also made MB endpoint include `MB_ADAPTIVE_BUDGET_SELECTOR_V1` from `experimental_preview_shadow`, so MB test primary now correctly uses C-16 adaptive output.

---

## VPS verification after fix

Internal API bundle verify for 2026-05-05:

```text
MN ADAPTIVE:
  BT=52 WIN
  lo3=452 LOSE
  xien2=[52,13] LOSE
  xien3=[52,13,56] LOSE

MT ADAPTIVE:
  BT=52 WIN
  lo3=752 LOSE
  xien2=[52,46] LOSE
  xien3=[52,46,44] LOSE

MB ADAPTIVE:
  BT=41 LOSE
  lo3=341 LOSE
  xien2=[41,98] LOSE
  xien3=[41,98,19] LOSE
```

This is the honest result. No beautification.

---

## Important correction

Any earlier `/du-doan-test` display/report claiming LO3 WIN based only on the last 2 digits is invalid and must be treated as a UI/API verification bug, not a real test win.

From V59 onward:

- LO3 status is full 3-digit only.
- Xiên status is same-station when station data exists.
- BT/lo2 remain 2-digit-tail based.

---

## Route smoke

```text
systemctl is-active lottery = active
/api/health = 200
```

---

## Official mutation

None.

This only changes how `/du-doan-test` verifies and displays test-axis status.

