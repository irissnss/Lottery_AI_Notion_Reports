# V89 — read this first

Owner OK 5 đề xuất V88. Done tonight.

## What's new

- 6 new tabs trong /monitoring V87 Master Index → tổng **24 tabs**:
  - 🛠️ Migrations (3 files)
  - 🔴 Live Cron (next_run realtime + last-run hints)
  - 🔎 FU Audit (152 items, **72 stale flagged**)
  - 🔬 Phase Findings (116 first paragraph)
  - ⚖️ Decision Log (22 DEC entries)
  - 📓 Governance Ledger (96 entries)
- Schema v88_v2 → v89_v3 (31 keys).

## Finding giá trị

**72/152 FU items STALE** — claim DEPLOYED/DONE nhưng không có CHANGELOG mention, hoặc claim WAIT nhưng có ≥3 mentions. Cần re-verify trong V90.

## Hard locks

- 4 official tables hash byte-identical.
- READ-ONLY backend.
- NO promote/rollback button.
- ai_keys redacted.

Main: [V89_REPORT.md](V89_REPORT.md)
