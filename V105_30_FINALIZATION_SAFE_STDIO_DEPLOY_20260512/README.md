# V105.30 — Total Force Finalization: `_safe_stdio_ctx` VPS Deploy + Rule105 Strict Shadow + SSOT V105.29 Public Live (2026-05-12 01:48 VN)

Status: **`V105_30_STABILITY_PASS_FOR_SAFE_STDIO` + `DEPLOYED_PENDING_NATURAL_VERIFY`** for runtime stability; **`SHADOW_ONLY` + `DO_NOT_PROMOTE`** for all prediction experiment lanes.

## Read First — Status Refresh 2026-05-12 10:08 VN

- GitHub account-level SSH is now verified and `Lottery_AI_Notion_Reports` has been pushed via SSH. Older "deploy key pending" wording below is superseded.
- Rule105 V105.30b correction: prize-source lock is checked by `source_region`, not `target_region`; `v10530_rule105_recheck.json` shows **0 true violations**. The 30 prior flags are audit false positives, not production quarantine items.
- Notion V105.30 is deferred by owner; public SSOT is GitHub raw (`REPORT_INDEX.md`, `LATEST_REPORT.json`, and this folder).

## Headline (5 dòng)

1. `_safe_stdio_ctx` wide patch **DEPLOYED LIVE** to VPS (`scheduler.py` md5 `9c17595d3dd5c0fa323bbaf4bf221f34`); service active; 6/6 endpoints 200; journal 5-min: 0 closed_file, 0 provider call. VPS backup `/root/Lottery_AI_Test/backups/v105_30_safe_stdio_20260512_012511/scheduler.py.bak`.
2. Public GitHub raw advanced through V105.30/V105.30b; quick-read entrypoint is `REPORT_INDEX.md`.
3. **Rule105 strict shadow** built, then corrected by V105.30b: `v10530_rule105_recheck.json` proves 105 active rules, **0 true prize-source violations**.
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
| v10530_rule105_strict_remine_shadow | 105 | Historical examination trace from the first strict-audit pass |
| v10530_rule105_prize_violation_audit | 30 | Historical false-positive rows after V105.30b source_region correction |
| v10530_rule105_old_vs_strict_compare | 21 | Per (region, weekday) coverage delta old vs strict |

All shadow_only=1, output_eligible=0, diagnostic_only=1, owner_approved=0.

## Hard locks observed

- /du-doan, /api/final-bundle, generate_final_bundle, official scoring/selector/voting, production prompt, model roster, official output eligibility, MT source formula — **none changed**.
- Token once/day/region/model contract — preserved.
- D-2 scope — MN only (MT/MB D-2 leak 7d = 0).

## Owner action remaining

- SSH public mirror push is DONE via account-level SSH.
- Notion V105.30 is optional/deferred; if needed later, create a short page that points to GitHub raw.
- No Rule105 production re-mine is needed for prize-source; V105.30b found 0 true violations.
- (Optional) OK cron daily 19:30 VN strength tensor refresh + cron 00:05 VN runtime manifest snapshot.

## Next step

Sync live + re-audit sau natural MN cascade ~16:30 VN today để confirm `rerun_post_mn` 7/7+7/7 + `closed_file_count=0`. Nếu PASS → V105.30 chuyển sang `V105_30_NATURAL_VERIFIED`.

If anything regresses: rollback via `_v10529_DEPLOY_SAFE_STDIO_VPS.md` rollback section (still applies — same backup path).
