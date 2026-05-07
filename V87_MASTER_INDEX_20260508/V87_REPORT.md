# V87 — Master Index in /monitoring (12-tab unified dashboard)

Ngày: 2026-05-08 00:25 VN
Trạng thái: SHADOW ONLY + UI EXTENSION — Không touch official.

## 0. Owner directive

"/monitoring là nơi tổng hợp toàn bộ về đo lường — phải triger, realtime, trực quan, tránh quên lãng, hỗ trợ Agent IDE khi cần thiết nhìn là nhớ ngay."

## 1. Em đã làm gì

- **Backend module mới**: `web/backend/_v87_master_board.py` (370 lines, READ-ONLY).
- **Route mới**: `GET /api/admin/master-board` (admin-only). Single endpoint trả 12 categories.
- **Section mới**: `sectionV87MasterIndex` trong `monitoring.html` (đặt **trước** `sectionV82MasterControl`).
- **12 tabs** dùng existing `region-tabs` UI pattern:
  1. 🧬 **Models** — 41 (15 ACTIVE / 13 SHADOW / 8 REMOVED) với status pill, provider, region, slot, WR.
  2. 💬 **Prompts** — 5 production stack (SP-4.0 / CP-7.9 archive / RR-16.4 / CTX-16.4 / PB-18.0) + 3 region-specialist shadow (V78) + 5 PFG cohorts (PFG-A → E active 2026-05-05) + 3 V81 pilot models.
  3. 📐 **Rules** — mined_rules / mined_effectiveness / verified_bucket counts + 12W/16W rolling windows + PB-18 phase fields chip + 4 rule-shadow methods + custom_prompt mode ARCHIVE_ONLY.
  4. ⚙️ **Mechanisms** — production cascade timeline 8 steps + 9 bundle gate surfaces + strongest-to-final POTENTIAL_LIFT + V59 strict (BT/LO2/LO3/Xien) + V77 post-cascade + 5 fast incident classes + anti-herding 5 layers + cohere rerank + 6 provider keys + timezone HCM helpers + hash guard 4 official tables sha256.
  5. 📊 **Metrics** — 8 C-XX với row counts + 3 PB/PP layers + 16 flip/risk/health/cost chips.
  6. 🌒 **Shadow Methods** — 18 P0 portfolio (method_key + group + state + min_days/min_samples) + 30 V52.5 era chips + 11 selectors (V67/V70/V73/V79/V80/V81 + table + rows + status).
  7. 🗄️ **DB Tables** — 129 với family pill (OFFICIAL/TEST_LANE/SHADOW/WAVE_1_2/INFRA/SUPPORT) + rows + max_date.
  8. ⏰ **Cron** — 26 jobs với time + lane pill + purpose.
  9. 🎨 **Frontend** — 12 pages với clickable URL + purpose.
  10. 🔌 **API** — 132 endpoints (24 ADMIN + 86 PUBLIC + 22 PAGE) collapsible sub-tables.
  11. 📅 **Decision Calendar** — 11 mốc với T+/T- badge (TODAY màu cam, T+N màu xanh, T-N màu xám).
  12. 🔒 **Owner Gate** — 9 items với trigger_date + blocker + owner_action + official_impact pill.
- Tab switcher: render từ cached payload (no re-fetch khi đổi tab).
- Auto-refresh 60s cùng các section khác.

## 2. Verification

- Local compile + lint pass.
- Backend smoke: 41 models / 59 shadow methods / 129 DB tables / 26 cron / 132 API / 12 frontend.
- VPS deploy 00:24 VN, `systemctl restart lottery`, active.
- `/api/health=200`, `/api/admin/master-board=401` unauth (admin lock OK), `/monitoring=401` unauth.
- 4 official tables hash UNCHANGED (predictions/final_bundles/lottery_results/model_daily_eval byte-identical).
- monitoring.html size: **162KB → 196KB** (+34KB cho section mới + JS render).

## 3. Hard contract honored

- READ-ONLY backend (zero write SQL trong `_v87_master_board.py`).
- 12 tabs READ-ONLY display.
- NO promote/rollback/edit/trigger button anywhere.
- NO scoring/selector/output mutation.
- Pre/post hashes 4 official tables byte-identical.

## 4. Owner can now

- Đăng nhập admin và truy cập **`https://xs.io.vn/monitoring`**.
- Cuộn xuống section "📚 V87 Master Index — toàn bộ hệ thống ở 1 chỗ (12 tab)" (đặt trước Parallel Shadow Proof + V82 Master Control).
- Click 12 tabs để xem từng category.
- Auto-refresh 60s — không cần F5.

## 5. Agent IDE có thể

- Gọi `GET /api/admin/master-board` (admin auth) để có 1 payload đầy đủ chứa toàn bộ inventory.
- Schema: `v87_master_board_v1`.
- Không cần parse nhiều endpoint khác — 1 lần là đủ.

## 6. Section ordering trong /monitoring (sau V87)

```
... (existing 20 sections)
sectionPromptGateCohort
sectionParallelShadowProof
↓
sectionV87MasterIndex ← V87 mới (12 tabs)
↓
sectionV82MasterControl ← V86 merge (V82 monitor)
↓
sectionRanking + sectionTrail + sectionGap + ... (other existing)
```

## 7. Những gì còn có thể thêm (V88+ nếu owner OK)

1. Live cron job last_run timestamps (gọi APScheduler runtime).
2. Settings DB tab (config keys + values).
3. Migration history tab.
4. VPS backup timeline tab.
5. Full FU history tab (FU-001 → FU-153).
6. Notion docs sync tab (titles + last updated).

## 8. Official UNTOUCHED ✅

- monitoring.html chỉ thêm 1 section + 1 load function + 1 switcher + 1 init/setInterval line.
- Backend chỉ thêm 1 module + 1 route admin-only READ-ONLY.
- KHÔNG đổi scoring / selector / output path / model roster.
- Pre/post hashes 4 official tables byte-identical.

## 9. Links + commits sẽ update sau push
