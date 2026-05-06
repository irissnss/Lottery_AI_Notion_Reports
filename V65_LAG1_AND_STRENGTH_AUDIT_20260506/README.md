# V65 Lag-1 leakage + strength priority + test-lane weighting audit

Published: 2026-05-07 00:15 VN (UTC+7).

## Quick links

- Main report: [V65_AUDIT_REPORT.md](V65_AUDIT_REPORT.md)
- Reading index: [00_READING_INDEX.md](00_READING_INDEX.md)
- Manifest: [MANIFEST.json](MANIFEST.json)
- Public raw root: https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V65_LAG1_AND_STRENGTH_AUDIT_20260506/

## Scope

- Q1: BT lose-on-day-N → hit-on-day-(N+1) leakage rate, stratified by NO_TOKEN vs TOKEN class and per-model.
- Q1b: Cohere effectiveness vs lag-1 leakage.
- Q2: Strength priority by region+weekday+station — daily/weekly cycle, freshness, applied to which lanes.
- Q3: /du-doan-test scoring with strength weighting (C-16 adaptive budget selector).

All conclusions are derived from production DB sha256=`893adb19...79347` (synced 2026-05-06 23:46 VN) and prediction_trace sha256=`46efd1b7...e5bb9`.

## Hard contract

- Code, prompts, secrets remain in private `irissnss/Lottery_AI_Test`.
- This repo only carries redacted markdown + JSON evidence.
