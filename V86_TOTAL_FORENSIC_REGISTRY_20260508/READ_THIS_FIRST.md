# V86 — read this first

Owner: V85 chưa đủ + /monitoring đã có sẵn em quên + /v82-monitor không có nút dễ quên → gộp.

## What's new

- **TOTAL_PUBLIC_REGISTRY.md** — 1 bảng duy nhất Notion AI tra cứu (10 sections, 26 KB).
- **`/monitoring`** giờ có thêm section `V82 Master Control Board` (cuộn xuống dưới Parallel Shadow Proof).
- `/v82-monitor` standalone vẫn giữ.

## Inventory bổ sung V85→V86

- 132 API endpoints (24 ADMIN + 86 PUBLIC + 22 PAGE; 90 admin-only).
- 12 frontend pages (V85 sót `viewer.html`).
- 142 FU items đầy đủ (V85 chỉ count nhẹ).
- 224 CHANGELOG versions từ V6.8 → V20.3.37.85.
- 116 phase_checkpoints qua 14 distinct dates.
- 26 AUTOMATION_HISTORY entries.

## Hard locks

- 4 official tables hash UNCHANGED.
- monitoring.html chỉ thêm 1 read-only section + 1 load function + 2 init lines.
- KHÔNG đổi scoring / selector / output path.
- KHÔNG có nút promote/rollback.

Main: [V86_REPORT.md](V86_REPORT.md)
Notion AI lookup: [TOTAL_PUBLIC_REGISTRY.md](TOTAL_PUBLIC_REGISTRY.md)
Source of truth: [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
