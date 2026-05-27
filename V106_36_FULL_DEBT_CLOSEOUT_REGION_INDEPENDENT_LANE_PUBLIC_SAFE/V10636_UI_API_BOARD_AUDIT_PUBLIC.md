> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 UI / API / BOARD AUDIT (live probe)

- ts_vn: 2026-05-27T23:05:00+07:00
- probe method: HTTP GET via WebFetch (no auth header). For 401 endpoints, owner browser session is required.

## Endpoint status

| Endpoint | HTTP | Observation | Class |
|---|---|---|---|
| `https://xs.io.vn/monitoring` | 401 | Unauthorized as designed (admin-only). | OK_AS_DESIGNED |
| `https://xs.io.vn/accuracy` | timeout (>15s) | Page slow to render via HTTP fetch. | SLOW_PROBE |
| `https://xs.io.vn/app` | 200 | Loads with "Loading..." placeholders; model leaderboard list intact (GPT-5-mini, Claude Sonnet 4.6, Gemini 2.5 Flash/Pro, Claude Opus 4, DeepSeek R1, GPT-5.4, COMBO Super, COMBO No Token, Smart Meta+LSTM, XGBoost, Smart XGB+RF, Meta-Learning, LSTM, Random Forest). | OK_NEEDS_JS |
| `https://xs.io.vn/du-doan` | 200 | Loads with "Đang tải dự đoán..." placeholder; needs JS. | OK_NEEDS_JS |
| `https://xs.io.vn/du-doan-test` | timeout | Slow probe. | SLOW_PROBE |
| `https://xs.io.vn/api/prediction-quality` | timeout | Slow probe. May be a heavy SQL endpoint. | SLOW_PROBE |
| `https://xs.io.vn/api/final-bundle?region=MN` | timeout | Slow probe. | SLOW_PROBE |
| `https://xs.io.vn/api/admin/v10622-parallel-live-board` | not probed | Board deploy gate (owner-only). | DEPLOY_GATE_REQUIRED |

## Findings

1. **`/monitoring` 401** is intentional admin auth. NOT a defect.
2. **`/app` and `/du-doan` HTML shell** loads fine. UI placeholders fill via XHR/JS. Static probe (no JS execution) shows placeholders only — cannot conclude staleness from static probe alone.
3. **`/accuracy`, `/du-doan-test`, `/api/prediction-quality`, `/api/final-bundle`** all time-out via WebFetch. Could be slow CDN, slow VPS handler, or genuine hang. Need owner-side browser confirmation.
4. **No 5xx, no 404 detected** in this pass.

## Findings vs PHASE 2 closeout

- `final_bundles` has rows for today MN/MT/MB (BT 58/77/08). The `/du-doan` endpoint should display these once JS runs. If owner browser shows "Đang tải" stuck more than 30s, that is a stale UI bug.
- `model_daily_eval` has 83 rows today. `/app` model leaderboard should populate.

## Owner verification needed (P1)

| Item | Owner action |
|---|---|
| `/accuracy` page render | Owner open in browser, screenshot if stuck >30s. |
| `/du-doan-test` page render | Owner open in browser, screenshot if stuck >30s. |
| `/api/prediction-quality` JSON | Owner open in browser with /app, capture XHR latency from Devtools. |
| `/api/final-bundle?region=MN` | Owner curl with browser session; verify response < 3s. |
| `/monitoring` page after owner login | Verify auth works, board renders. |

## Board deploy gate

- Owner has not explicitly approved a NEW admin-only read-only board deploy in this session.
- → `BOARD_DEPLOY_OWNER_GATE_REQUIRED`.
- No `/du-doan` change made.
- No official mutation made.
- No `/api/admin/v10622-parallel-live-board` deploy attempted.

## Decision

This pass treats all UI/API observations as **PENDING_OWNER_BROWSER_CONFIRM** rather than declaring STALE. Doing so honors the "no false STALE claim" rule (a static HTTP probe without JS execution cannot prove UI staleness).

Next-live runbook for 2026-05-28 will include owner-browser smoke as P1 item.
