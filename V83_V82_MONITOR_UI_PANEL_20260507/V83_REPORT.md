# V83 — V82 MONITOR UI PANEL (admin-only, read-only)

Owner OK: 2026-05-07 23:14 VN — bật UI admin read-only panel cho V82.

## Mục tiêu

Cho owner (anh) một dashboard nhìn thấy hằng ngày:

- AI herd vs NO_TOKEN herd vs OFFICIAL per region 7 ngày gần nhất
- V82 60d evidence summary (cached)
- V79 cluster-weighted consensus (rank=1)
- V79 AI ↔ NO_TOKEN cross-verify
- V81 provider shadow pilot per-call (deepseek-chat / claude-sonnet-4-6 / gemini-3-flash)
- V67 / V70 / V73 selector traces
- V80 MB regime-shift + MN AI herd vs V67 save
- V77 fast incident monitor

## Hard contract honored

- READ-ONLY backend (`_v82_monitor.py` không có một dòng `INSERT/UPDATE/DELETE` nào)
- Admin-only routes (401 cho unauth)
- KHÔNG có nút promote / rollback / edit / trigger run
- KHÔNG đổi scoring / selector / lane weights / model roster
- KHÔNG đụng official prompt
- KHÔNG đụng final_bundles / predictions / lottery_results / model_daily_eval
- Pre/post hashes 4 official tables UNCHANGED (verified after deploy)

## Routes

- `GET /v82-monitor` (HTML, admin-only, 401 if not admin)
- `GET /api/admin/v82-monitor` (JSON, admin-only, 18-key payload)

## Cách sử dụng

1. Anh đăng nhập `/login` với tài khoản admin.
2. Truy cập `/v82-monitor`.
3. Panel auto-refresh mỗi 5 phút.
4. Anh chỉ xem; KHÔNG có nút nào thay đổi state.

## Verification (2026-05-07 23:20 VN)

- Local compile + lint pass.
- VPS deploy 23:19 VN: `systemctl restart lottery`, active.
- Smoke: `/api/health=200`, `/v82-monitor=401` unauth (admin lock confirmed), `/api/admin/v82-monitor=401` unauth.
- Backend module smoke: 18 payload keys, 7-day MN herd rows, 12 cluster recent rows, 21 V81 pilot rows.
- Pre/post hashes 4 official tables UNCHANGED (`predictions/final_bundles/lottery_results/model_daily_eval`).

## Sections rendered (7)

1. **Per-region last 7 days** — OFFICIAL/AI herd/NO_TOKEN herd với hit pill (HIT/MISS/PENDING).
2. **V82 60d cached summary** — top 5 method per region với verdict pill (PROMOTION_CANDIDATE/DESTRUCTIVE/BASELINE).
3. **V79 cluster-weighted (rank=1)** — selected_tail + score + cluster weights + risk flag.
4. **V79 AI ↔ NO_TOKEN cross-verify** — full picks + confidence + would_save/would_break.
5. **V81 provider pilot** — per-call (date × region × model) với latency + status pill.
6. **V67/V70/V73 traces** — 3-column grid.
7. **V80 MB regime + MN V67 save + V77 fast incident** — 3-column grid.

## Owner-lock notice (in panel)

Panel hiển thị warning: "V82 monitor cố ý không có nút điều khiển. Mọi promotion/rollback đều cần owner OK ở session riêng + dossier."

## What is NOT in this panel

- Không có nút "Promote V67/V73/V79".
- Không có nút "Disable AI model".
- Không có nút "Increase NO_TOKEN floor".
- Không có nút "Trigger cron now".
- Không có nút "Edit official prompt".

→ Owner-lock cho mọi promotion remains intact.

## Files deployed

- `web/backend/_v82_monitor.py` (NEW, ~210 lines, read-only payload builder)
- `web/backend/main.py` (PATCHED, +30 lines for 2 admin routes)
- `web/frontend/v82-monitor.html` (NEW, ~280 lines, display dashboard)

## Hash guard

PRE = POST byte-identical for `predictions/final_bundles/lottery_results/model_daily_eval`.
