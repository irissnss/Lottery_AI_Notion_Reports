# V105.30 — Total Force Finalization: `_safe_stdio_ctx` VPS Deploy + Rule105 Strict Shadow + SSOT V105.29 Public Live (2026-05-12 01:48 VN)

Status: **`V105_30_STABILITY_PASS_FOR_SAFE_STDIO` + `DEPLOYED_PENDING_NATURAL_VERIFY`** for runtime stability; **`SHADOW_ONLY` + `DO_NOT_PROMOTE`** for all prediction experiment lanes.

## Headline (5 dòng)

1. `_safe_stdio_ctx` wide patch **DEPLOYED LIVE** to VPS (`scheduler.py` md5 `9c17595d3dd5c0fa323bbaf4bf221f34`); service active; 6/6 endpoints 200; journal 5-min: 0 closed_file, 0 provider call. VPS backup `/root/Lottery_AI_Test/backups/v105_30_safe_stdio_20260512_012511/scheduler.py.bak`.
2. Public GitHub raw advanced **V105.27 → V105.29** (commit `18ddf38`, 27 files, 9933 insertions). Local mirror at V105.30 staged.
3. **Rule105 strict shadow** built (`v10530_rule105_strict_remine_shadow` 105 rows = 75 kept + 30 quarantine-recommended; 0 bucket collapsed; 19/21 buckets top5_incomplete). `QUARANTINE_INVALID_RECOMMENDED` + `PRODUCTION_REPLACE_NOT_ALLOWED_YET`.
4. `docs/SIGNAL_LAYER_REGISTRY.md` created with 13 canonical layers.
5. Official 4-table row counts identical pre/post; provider call 0; MT protect preserved.

## Files

- `evidence/V105_30_FINALIZATION_REPORT.md` — 25-section Vietnamese report.
- `evidence/v10530_preflight.json` — pre-hash + env state.
- `evidence/v10530_master_audit.json` — 12-lane audit.
- `evidence/v10530_hash_double_check.json` — hash determinism proof on static DB.

## V105.30 shadow tables (local DB)

| Table | Rows | Purpose |
|---|---:|---|
| v10530_rule105_strict_remine_shadow | 105 | Per active mined_rule: kept_strict or quarantine_reason |
| v10530_rule105_prize_violation_audit | 30 | One row per active rule using prize_keys outside owner lock |
| v10530_rule105_old_vs_strict_compare | 21 | Per (region, weekday) coverage delta old vs strict |

All shadow_only=1, output_eligible=0, diagnostic_only=1, owner_approved=0.

## Hard locks observed

- /du-doan, /api/final-bundle, generate_final_bundle, official scoring/selector/voting, production prompt, model roster, official output eligibility, MT source formula — **none changed**.
- Token once/day/region/model contract — preserved.
- D-2 scope — MN only (MT/MB D-2 leak 7d = 0).

## Owner action remaining

- Add SSH public key (`ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIgOYWncuh8DIID0vHOhOuiY0Kx7sVjtYF5hAXKXIAnw admin@lottery-ai`) vào GitHub UI Deploy Keys cho 2 repos: `Lottery_AI_Test` + `Lottery_AI_Notion_Reports` (allow write).
- Manual upload V105.29 + V105.30 packages to Google Drive.
- (Optional) OK riêng để re-mine production `mined_rules` strict (hiện chỉ quarantine recommendation).
- (Optional) OK cron daily 19:30 VN strength tensor refresh + cron 00:05 VN runtime manifest snapshot.

## Next step

Sync live + re-audit sau natural MN cascade ~16:30 VN today để confirm `rerun_post_mn` 7/7+7/7 + `closed_file_count=0`. Nếu PASS → V105.30 chuyển sang `V105_30_NATURAL_VERIFIED`.

If anything regresses: rollback via `_v10529_DEPLOY_SAFE_STDIO_VPS.md` rollback section (still applies — same backup path).
