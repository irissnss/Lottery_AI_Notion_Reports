# V56 — `/du-doan-test` Experience Lane

**Date:** 2026-05-05 21:41 VN  
**Scope:** Admin/test UI + read-only API response enrichment only  
**Owner intent:** Stop waiting forever for 14/30/60-day official-proof before the owner can *experience* new methods. Keep official hard locks intact.

---

## What changed

### Backend

Added `_build_du_doan_test_experience_summary(region, date_str)` in `web/backend/main.py`.

The helper is **read-only** and only SELECTs from:

- `final_bundles`
- `lottery_results`
- `du_doan_test_bundles`
- `du_doan_test_results`
- `predictions` (V55 Google shadow models only)

The helper returns an `experience` object in both:

- `/api/du-doan-test/mb`
- `/api/du-doan-test/{region}`

### Frontend

Added a new top section in `web/frontend/du-doan-test.html`:

**“🚀 Trải nghiệm hôm nay (EXPERIENCE MODE)”**

It shows:

- method true rescues
- method harmful / false-promotion count
- V55 Google shadow hits
- method table with `cứu official miss`, `phá / false promo`, `đồng thuận`, `baseline clone`
- V55 Google shadow picks (`gemini-3.1-pro`, `gemini-3-flash`, `gemma-4-31b`)

### Governance flags

Every response carries:

- `official_output=false`
- `output_impact=false`
- `test_only=true`
- `admin_only=true`
- `output_eligible=false`
- `promotion_allowed=false`

---

## VPS verification

Route smoke:

```text
/api/health=200
/du-doan=200
/du-doan-test=401
/api/du-doan-test/mn unauth=401
/api/final-bundle?region=MB=200
```

Direct helper verification for `2026-05-05`:

### MN

- official BT: 15 LOSE
- experience: `MN_AI_CHAIN_PRESERVATION_V1` picked 52 WIN
- `true_rescues=1`
- `gemini-3-flash` PARTIAL with `[13,52]`

### MT

- official BT: 44 WIN
- no true rescue needed
- no harmful highlight in this view
- V55 Google shadow models all LOSE for MT today

### MB

- official BT: 83 LOSE
- experience: `MB_PRIOR_REGION_CONTEXT_SAFE_V1` picked 98 WIN
- `gemini-3-flash` WIN with `[91,14]`
- `gemini-3.1-pro` PARTIAL with `[90,14]`
- `true_rescues=1`, `shadow_helpful=2`

---

## Important correction vs earlier V55 final

After the scheduler preflight fix and subsequent shadow/catch-up activity, `gemma-4-31b` now has helper-visible rows for 2026-05-05. Earlier V55 correctly reported the first natural shadow run skipped it because it was mis-routed to OpenRouter. V56 verifies the route is now fixed and the experience helper surfaces current rows.

---

## Official mutation proof

No official output path changed:

- no call to `generate_final_bundle()`
- no write to `final_bundles`
- no write to official `predictions`
- no change to scoring/voting/lane weights
- no official roster change

This is a view/API enrichment only for admin `/du-doan-test`.

---

## Backup

VPS backup:

`/root/Lottery_AI_Test/backups/v56_experience_lane_20260505_2133/`

Contains:

- `main.py.bak`
- `du-doan-test.html.bak`

---

## Verdict

`EXPERIENCE_MODE_READY`

The owner can now see and compare new methods daily in `/du-doan-test` without waiting for official-promotion proof and without affecting user-facing `/du-doan`.
