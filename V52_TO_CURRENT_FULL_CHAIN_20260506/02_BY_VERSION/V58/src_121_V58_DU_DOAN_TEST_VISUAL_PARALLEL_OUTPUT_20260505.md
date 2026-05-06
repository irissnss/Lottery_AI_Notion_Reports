# V58 — `/du-doan-test` visual parallel output

**Date:** 2026-05-05 23:20 VN  
**Scope:** UI-only output clarity for `/du-doan-test`  
**Owner concern:** The test page must show the actual test output directly (BT, 3 càng, xiên 2, xiên 3), not just measurement tables.

---

## What changed

Added a prominent top card in `web/frontend/du-doan-test.html`:

**“🎯 Dự đoán Test Song Song — output để anh xem trực quan”**

It displays side-by-side:

- BT
- Lô 3 càng
- Xiên 2
- Xiên 3

For both:

- Test output (`/du-doan-test`)
- Official baseline (`/du-doan`)

It also shows a lock/proof label:

- `PRE_RESULT_LOCKED`: real pre-result test snapshot, counts as natural experiment proof
- `POST_CLOSEOUT_DIAGNOSTIC`: after-result diagnostic snapshot, useful for learning but **not** counted as realtime proof

---

## Important honesty guard

For 2026-05-05, because the work happened after closeout, the page must show:

`POST_CLOSEOUT_DIAGNOSTIC`

This prevents post-result rows from being presented as if they were pre-result predictions.

Tomorrow and later, the goal is:

1. Generate `/du-doan-test` C-16 output before result.
2. Lock it as `PRE_RESULT_LOCKED`.
3. After results, verify it as WIN/LOSE/PARTIAL.
4. Continue rolling measurement.

---

## Deploy/verify

- UI file deployed to VPS.
- `/du-doan-test` remains admin-only (unauth 401).
- `/api/health=200`.
- The UI file contains the new output section and lock labels.

---

## Official mutation

None.

This was UI-only and reads the existing API fields.

