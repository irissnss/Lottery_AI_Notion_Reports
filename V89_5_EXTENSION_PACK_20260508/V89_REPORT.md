# V89 — 5-extension pack: Migrations + Live Cron + FU Audit + Phase Findings + Decision Log + Governance Ledger

Ngày: 2026-05-08 00:55 VN
Trạng thái: SHADOW ONLY + UI EXTENSION — Không touch official.

## 0. Owner directive

"Tiến hành các đề xuất 1,2,3,4,5 luôn cho sạch sẽ đầy đủ trong tối nay đi khuya rồi."

## 1. Em đã làm gì

V89 mở rộng V87 Master Index từ 18 → **24 tabs** trong `/monitoring`, thêm 6 tabs mới (em tách Decision Log + Governance Ledger thành 2 tabs riêng — đề xuất 5 thực ra cần 2 surfaces):

| # | Tab mới | Source | Findings |
|---|---|---|---|
| 19 | 🛠️ **Migrations** | parse `web/backend/migration_*.py` | **3 migration files** với docstring + tables CREATE/ALTER |
| 20 | 🔴 **Live Cron** (next_run) | APScheduler runtime + `scheduler_logs` last-run hints | jobs realtime với "in 5m 30s" badge color-coded (đỏ <0, cam <10p, vàng <1h, xanh) |
| 21 | 🔎 **FU Audit** (stale) | re-verify 152 FU items vs CHANGELOG | **72/152 FU stale flag** với rule (DEPLOYED/DONE but 0 mention) hoặc (WAIT but ≥3 mentions) |
| 22 | 🔬 **Phase Findings** | extract first paragraph từ 116 phase_checkpoint files | 116 với title + finding |
| 23 | ⚖️ **Decision Log** | parse `docs/DECISION_LOG.md` | **22 DEC owner decisions** với finality pill (FINAL/PROVISIONAL/SUPERSEDED) |
| 24 | 📓 **Governance Ledger** | parse `docs/CHANGELOG_GOVERNANCE_LEDGER.md` | **96 entries** date + title + summary |

## 2. Finding giá trị: 72/152 FU items STALE

Audit rules:
- Stale nếu status `DEPLOYED/DONE/LIVE_PROVEN` nhưng FU-NNN **không xuất hiện trong CHANGELOG**
- Stale nếu status `WAIT` nhưng FU-NNN có **≥3 CHANGELOG mentions** (likely đã advanced nhưng quên update tracker)

→ 72 FU cần re-verify. V90 candidate nếu owner OK = audit từng FU.

## 3. Verification

- Local compile + smoke: 31 keys (was 25), migrations=3, fu_audit=152 (72 stale), phase_findings=116, decision_log=22, governance_ledger=96.
- VPS deploy 00:53 VN, `systemctl restart lottery`, active.
- `/api/health=200`, `/api/admin/master-board=401` unauth.
- 4 official tables hash byte-identical.
- monitoring.html: 201 KB → 209 KB (+8 KB).

## 4. Hard contract honored

- READ-ONLY backend (zero write SQL trong 6 blocks mới).
- 24 tabs READ-ONLY display.
- NO promote/rollback/edit/trigger button.
- NO scoring/selector/output mutation.
- ai_keys vẫn redacted (V88 anti-leak).
- Pre/post hashes 4 official tables byte-identical.

## 5. Total inventory after V89

**~1019 distinct items reconciled** across V85 + V86 + V87 + V88 + V89:

- V85 deep: 41 models / 129 DB / 26 cron / 8 prompts + 5 PFG / 27 metrics / 59 shadow methods
- V86 forensic: 132 API / 12 frontend / 142 FU summary / 224 CHANGELOG / 116 phase
- V87 UI: 12 tabs
- V88 deep: 252 settings / 28 history / 151 FU full / 116 phase / 31 backups / 15 Notion
- **V89 extras**: 3 migrations / live_cron jobs / 152 FU audit / 116 phase findings / 22 decision_log / 96 governance_ledger

## 6. Owner can now

- Truy cập `/monitoring` → cuộn xuống V87 Master Index → click bất kỳ trong **24 tabs**.
- Tab `🔎 FU Audit` cho biết **72 FU stale** cần re-verify.
- Tab `🔴 Live Cron` xem next_run của 26 cron jobs realtime.
- Tab `⚖️ Decision Log` xem 22 owner decisions.
- Tab `🔬 Phase Findings` lướt nhanh first paragraph của 116 audit reports.

## 7. Agent IDE

- 1 endpoint `/api/admin/master-board` schema `v89_master_board_v3` với 31 keys.

## 8. Official UNTOUCHED ✅

- 4 official tables hash byte-identical V77 → V89.
- Backend chỉ thêm 6 helper blocks vào module hiện tại.
- monitoring.html chỉ thêm 6 region-tab buttons + 6 render branches.
- KHÔNG đổi scoring / selector / output / model roster.

## 9. V90 candidate (nếu owner OK)

- Audit từng FU stale (72/152) → fix status hoặc closeout.
- Hợp nhất duplicate FU (nếu có).
- Per-decision-log audit: track FINAL vs PROVISIONAL.
