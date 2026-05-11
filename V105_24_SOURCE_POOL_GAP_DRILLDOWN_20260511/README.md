# V105.24 — SOURCE_POOL_GAP_DRILLDOWN + V102_RELAXED_SHADOW + TOKEN_LOCK + RUNTIME_MANIFEST

Published: 2026-05-11 VN.
Status: **PARTIAL** — official-locked, shadow surfaces wired, but station alias residue and V102 RELAXED L2 = 0 deferred to V105.25.

## What this folder contains

| File | Purpose |
|---|---|
| `evidence/V105_24_FINAL_REPORT.md` | Vietnamese final report (10 sections). |
| `evidence/v10524_local_audit_latest.json` | End-to-end local audit run, including pre/post SHA256 for the four official tables. |
| `evidence/v10524_station_code_audit.json` | Code-axis station identity audit. |
| `evidence/DEPLOYED_RUNTIME_MANIFEST.json` | Snapshot of the runtime manifest (no secrets, fingerprinted). |

## Hard contracts

- `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval` are **never** written by V105.24 modules.
- No provider/manual AI calls were issued.
- Manual `POST /api/predict/{region}` is now token-gated with `HTTP 423` for provider/token-consuming models.

## Read order

1. `evidence/V105_24_FINAL_REPORT.md`
2. `evidence/v10524_local_audit_latest.json` (look for `official_unchanged: true`)
3. `evidence/v10524_station_code_audit.json` (`alias_unexpected_count = 62` — fixed in V105.25)
4. `evidence/DEPLOYED_RUNTIME_MANIFEST.json`

V105.25 follow-up is published at `V105_25_STATION_ALIAS_FIXUP_20260511/`.
