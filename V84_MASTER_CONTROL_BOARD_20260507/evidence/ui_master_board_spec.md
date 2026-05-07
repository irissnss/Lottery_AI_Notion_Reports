# Master Experiment Control Board — UI/API spec (proposal)

Status: SPEC ONLY. Owner OK pending. KHÔNG build until owner OK.

## Mục đích

Kế thừa V83 `/v82-monitor`, mở rộng thành **Master Experiment Control Board** để owner xem 1 màn hình:

1. Today's risk
2. Method maturity (14/18 READY_TO_EVALUATE; 4 WAIT 5 ngày)
3. Due decisions calendar
4. MN/MB/MT status snapshot
5. AI herd vs NO_TOKEN herd 7d
6. V67/V70/V73 conflict
7. V81 provider pilot per call
8. 7/14/30/60d gates progress
9. Owner-gate queue
10. Hard-lock list (do-not-touch)

## API contract (read-only)

`GET /api/admin/master-board` (admin only)

Returns JSON with sections:
- `today_risk`: ai_herd_severe_count, mb_cold_streak_days, mn_v67_save_signal, mt_consensus_status
- `method_maturity`: from 18-method matrix (READY/WAIT)
- `decision_calendar`: next 14 events with date + trigger + decision rule
- `regions`: MN/MT/MB current status snapshot
- `ai_no_token_7d`: per-region herd compare
- `v67_v70_v73_conflict`: today's tail conflicts
- `v81_pilot`: latest 3 days × 3 models
- `windows`: 7/14/30/60d progress per method
- `owner_gate_queue`: items waiting owner OK
- `do_not_touch`: hard locks list

NO write endpoints. NO promote/rollback/edit/trigger.

## UI sections (proposal)

Block 1 — Today's risk
- 3 traffic lights: MN risk / MT risk / MB risk
- AI herd severity per region (severe/moderate/light count last 7d)
- MB cold streak counter (auto-escalate at 7d)
- MN V67 save signal (sticky on/off)

Block 2 — Method maturity
- Stack 18-method portfolio with progress bars
- Per method: days observed / min_days, samples / min_samples
- READY/WAIT pill

Block 3 — Decision calendar
- Next 14 due dates with item + trigger + decision rule
- Highlight today + tomorrow

Block 4 — Region snapshot (MN/MT/MB cards)
- Per region: OFFICIAL hit rate 60d/30d/14d/7d
- AI/NO_TOKEN/V67/V73/cluster table latest 7d
- 60d candidates list (PROMOTION_CANDIDATE pill)

Block 5 — Owner gate queue
- 3 queue: Now / Soon / Owner-locked
- Each item: trigger date + blocker + owner_action

Block 6 — Hard-lock list
- Visible permanent panel listing things that MUST NOT be auto-changed.

## Build effort estimate

- Backend module `_v84_master_board.py` ~250 lines (read-only payload).
- Route `GET /api/admin/master-board` + `GET /master-board` (~20 lines main.py).
- Frontend `master-board.html` ~400 lines (display only).
- Total: 1 session work; no DB write; no schema change; no scoring change.

## Owner OK required

Anh OK thì em build. Nếu chưa cần thì giữ V83 `/v82-monitor` đủ dùng.
