# OWNER DECISION REGISTER — V105.27

> 10 explicit decisions awaiting owner confirmation. No action taken without owner OK.

| # | Decision | Context | Options | Risk | Recommendation | Owner confirmation needed |
|---:|---|---|---|---|---|---|
| 1 | Publish V105.24 / V105.25 / V105.25b / V105.26 / V105.27 reports to Drive + Notion + public GitHub mirror? | Local `CHANGELOG.md` jumps V105.20 → V105.22 → V105.25b; V105.21/23/24/26 not surfaced locally. Public-facing root files (`LATEST_REPORT.json`, `REPORT_INDEX.md`, `CHANGELOG_PUBLIC.md`, `DELTA_INDEX.md`, `00_PUBLIC_RAW_LINKS.md`, `OPEN_ISSUES.md`, `NEXT_ACTION.md`) are missing from workspace. | A) Publish all in one batch after redacted scan. B) Publish only V105.27 (this report). C) Wait. | LOW if redacted scan passes; MEDIUM if PAT remediation not done first | A after PAT/SSH migration (Decision #9), otherwise B for V105.27 only | YES |
| 2 | Confirm station alias fixup accepted when regression_count = 0? | `station_identity_runtime_audit=69` shows `unexpected_count=0` for `lottery_results.station`. Huế canonical = `Thừa Thiên Huế` (current) vs `Huế` (mission target). | A) Keep `Thừa Thiên Huế` (current live). B) Flip to `Huế` short form. | A: LOW. B: MEDIUM — changes UI/pnl/rule labels across V105.9 surfaces | A — keep current; treat mission "Huế" as shorthand | YES |
| 3 | Continue MN D-2 prompt wire natural-run tracking 7/14d? | Statistical depth already includes D-2 implicitly; explicit MN_D2 priority card not in prompt. | A) Add shadow-only `mn_d2_shadow_v1` MN profile, no MT/MB injection. B) Continue current (D-2 implicit only). | A: LOW (shadow-only, no provider call). | A | YES |
| 4 | Run Top2 A/B shadow 14d? | Current 5-9 run samples too small; would_save_count=2 (MN 2026-05-10) but break_ratio not yet stable per region+weekday. | A) Run structured shadow 14d on MN+MB; MT measurement only (PROTECT). B) Continue ad-hoc. | A: LOW (shadow-only) | A | YES |
| 5 | Run MB_D_v2 shadow 14d — define scope. | 4 sub-options (A-D in MB_FORENSIC_OPTIONS.md). | A) Wide D-2 (HOLD). B) Relax TOP30 cap. C) Source-prize strong class. D) Same-day MN/MT weighting. Owner pick one or multiple subsets. | A: HIGH. B: MEDIUM. C–D: LOW | C and/or D first; defer A | YES — owner must define exact scope |
| 6 | Keep V102 relaxed HOLD until V103 supply class backfill + 14d clean? | `v10522_v102_strong_selector_shadow=0`, `v103_candidate_supply_shadow.class` column missing locally → likely VPS migration. Sample too small. | A) HOLD. B) Allow shadow promote on a per-region weekday basis. | A: LOW. B: MEDIUM (per-region) | A — HOLD | YES |
| 7 | Keep manual AI/provider cuốn chiếu blocked? | V105.22b token-cost guard active. | A) Keep blocked (current). B) Add owner-only override flag `OWNER_MANUAL_PROVIDER_CALLS_ENABLED=true` for emergency. | A: LOW. B: MEDIUM (provider cost risk) | A — keep blocked | YES |
| 8 | MB `rerun_post_mn` intermediate display allowed or only after MN+MT? | When MN cascade succeeds, MB also gets a `rerun_post_mn` row before MT cascade runs. UI today shows it as DD Sau if it exists. | A) Show intermediate `rerun_post_mn` for MB as DD Sau (current). B) Suppress in UI until MT verify also done; show only `rerun_post_mt`. | A: LOW — informative. B: LOW — cleaner | A — keep, label `(stage=rerun_post_mn)` for clarity | YES |
| 9 | Confirm old PAT revoked + new PAT rotated + SSH deploy key migration approved? | `ghp_cvoSP***` and newly-pasted PAT both flagged in V105 security report. SSH deploy key not yet generated. | A) Revoke both PATs, generate SSH deploy key on VPS, swap remote to SSH. B) Continue PAT remote. | A: LOW once executed. B: HIGH ongoing | A | YES — P0 |
| 10 | Approve VPS deploy of `_safe_stdio_ctx` scheduler patch? | Today 2026-05-11 16:38:53 MN cascade crashed `0 thành công, 14 lỗi` due to `I/O operation on closed file`. Local fix wraps `_run_free_model_prediction` and `_rerun_free_models_after_scrape` in `_safe_stdio_ctx()`. Selector/scoring/prompt/roster unchanged. | A) Deploy with backup + restart `lottery.service`. B) Wait. | A: LOW (stdio safety only). B: HIGH — cascade keeps failing intermittently | A | YES |

## Notes

- Decision #2: keeping `Thừa Thiên Huế` matches V105.9 + V105.19 deployed canonical SSOT. If owner truly wants the short form, plan a coordinated rename across `station_identity.py`, `/pnl-tracker`, V101 shadows, prompt labels, V52 MT surfaces — minimum 2-day prep.
- Decision #9: P0. Other decisions can wait until #9 is resolved if public-push is part of the plan.
- Decision #10: P0 for cascade stability. Without it, MN-trigger cascade keeps degrading whenever systemd thread inherits a closed stdio.

## Provider call count

0 provider calls executed for any decision proposal.
