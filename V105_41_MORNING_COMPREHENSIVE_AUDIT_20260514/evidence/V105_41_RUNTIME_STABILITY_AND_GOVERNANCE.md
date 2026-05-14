# V105.41 Runtime Stability and Governance — 2026-05-14

This document records the runtime stability story from V105.30d to today, the active follow-up tracker, the governance lock list, and the current owner-decision queue. It is intended to give external analysts the full context for why the system is in `NATURAL_VERIFY_PARTIAL_PASS_NOT_FULL_PASS` and why the V105.40 expansion patch is owner-gated rather than auto-deployed.

## 1. Runtime stability timeline

| Version | Date | Highlight |
|---|---|---|
| V105.15 | earlier | Defined the official soft/hard timeout architecture: 90 s soft continue, 300 s hard timeout, OpenRouter HTTP 300 s. |
| V105.27 | 2026-05-11 | Shadow-wire of MN D-2 ranked top-5 into prompt (shadow only). Production prompt unchanged. |
| V105.28 | 2026-05-11 | Total Force Runtime Contract Verify. Confirmed DD Trước / DD Sau routing, retrain-before-rerun, region-only freeze. Surfaced `CLOSED_FILE_DEPLOY_PENDING`. |
| V105.29 | 2026-05-12 | `_safe_stdio_ctx` wide refactor in scheduler.py around no-token entry points; smoke 3/3 pass. |
| V105.30 | 2026-05-12 | `_safe_stdio_ctx` deployed to VPS. Six endpoints green. Journal post-restart 0 closed-file. Rule105 strict shadow built. |
| V105.30d | 2026-05-12 | Shadow no-missing runtime contract: non-timeout system/provider/parser failures become persisted diagnostic empty rows; backfilled glm-5.1 morning. |
| V105.33 | 2026-05-12 | Natural verify snapshot at 16:00 VN; MN clean, MT/MB pending. |
| V105.34 | 2026-05-12 | Official token result/save handling protected by `_safe_stdio_ctx`; UI labels under-15 baselines as "not on /du-doan". |
| V105.35 | 2026-05-12 | Semantic publish gate fix. Readiness uses `output_eligible_row_count` (15/15 official roster); voting uses `scoreable_model_count` (after WR/BT filter). MB publishes 15/15 + quality warning. |
| V105.36 | 2026-05-12 | Closeout audit only (this wrapper). No live verify pass declared. |
| V105.37 | 2026-05-12 | Model health scoreboard + provider routing A/B draft. Direct-API vs OpenRouter shadow A/B plan. |
| V105.38 | 2026-05-12 | Owner question on raising timeout to 500 s answered with `PROPOSAL_ONLY`; design proves the change is not a single-constant flip. |
| V105.39 | 2026-05-13 | Safe morning control. MN 04:15 clean; 2 shadow closed-file events identified; MT 5-model armed for 16:30. |
| V105.40 (morning) | 2026-05-13 | Day-control read-only. Root cause confirmed: `gpt_analyzer.py` has zero `_safe_stdio_ctx` / `_safe_print` coverage. |
| V105.40b | 2026-05-13 | `/api/review-hub/filter` 500 forensic. Scope extends to `main.py` 16 `traceback.print_exc()` sites. Patch owner-gated for deploy after MB cycle close. |
| V105.41 | 2026-05-14 | Morning comprehensive audit (this release). 14 closed-file sites observed on 13/5; scope extends further to Excel, verify-bundle, Pattern Tracker, Shadow Daily Comparison, Shadow Rule D1. |

## 2. Closed-file regression map

Confirmed source paths emitting `I/O operation on closed file` after systemd closes stdio on the long-running service:

| Category | Symptom path | Evidence (date / count) |
|---|---|---|
| Token AI provider wrapper | `gpt_analyzer.py _call_*` (OpenAI / Anthropic / Gemini / DeepSeek / xAI / OpenRouter) | 13/5: 1 event (claude-sonnet-4-6 sáng) — retry succeeded |
| Shadow eval provider wrapper | scheduler `shadow_auto_eval` worker | 13/5: 5 events (gpt-5.5, gemini-3-flash, kimi-k2.5, gpt-oss-120b 21:25 / 14/5: gpt-oss-120b 04:25) |
| User-facing API endpoints | `main.py` `traceback.print_exc()` in `except` | 13/5 12:30 onward — `/api/review-hub/filter` returns HTTP 500 for all 3 regions |
| Excel update writer | `Lỗi cập nhật Excel: ...` | 13/5: 3 events (09:33, 10:30, 11:31) |
| Verify final bundle | `Verify final bundle <REGION> error: ...` | 13/5: 3 events (one per region after scrape + verify) |
| Pattern Tracker | `Lỗi Pattern Tracker: ...` | 13/5: 1 event (11:31) |
| Shadow Daily Comparison | `[SHADOW_DAILY_COMPARISON] Error: ...` | 13/5: 1 event (11:31) |
| Shadow Rule D1 measurement | `[SHADOW_RULE_D1] post-MRE/MDE error: ...` | 13/5: 1 event (13:20 MB measurement) |

Common root cause:

- The service has been running continuously since 12/5 19:38:50 VN (uptime 26d 8h at time of this report).
- Systemd has closed `sys.stdout` and `sys.stderr` at some point during this long run.
- Any code path that writes to stdout/stderr without going through the existing `_safe_stdio_ctx` or `_safe_print` helpers will throw `ValueError: I/O operation on closed file`.
- In `except` blocks, that throw replaces the original exception and propagates as `HTTPException(detail="I/O operation on closed file.")` to the API caller.

Mitigation already in place (V105.30d / V105.34):

- Diagnostic-row contract for `shadow_auto_eval` and official token save path. No silent missing.
- `_safe_stdio_ctx` wrap on scheduler worker threads for token and no-token entry points.

Mitigation pending (V105.40 expansion):

- Add `_safe_stdio_ctx` + `_safe_print` to `gpt_analyzer.py` provider entry points.
- Add `_safe_print` to `main.py` and replace 16 `traceback.print_exc()` sites.
- Same treatment for Excel writer, verify-final-bundle path, Pattern Tracker, Shadow Daily Comparison, Shadow Rule D1 materializer.
- One service restart to refresh stdio handles.

## 3. Active follow-up tracker (excerpt)

| FU ID | Status | Summary |
|---|---|---|
| `FU-V105-41-CLOSED-FILE-REGRESSION-MULTI-SITE` | OWNER_LOCK | New today. Wider regression scope across 7 source paths; 14 events observed on 13/5. |
| `FU-V105-40-SAFE-STDIO-EXPANSION` | OWNER_LOCK | Patch design for shadow + main user-facing endpoints; deploy gate after MB cycle close. |
| `FU-V105-39-SHADOW-CLOSED-FILE-REGRESSION-P0` | DEPLOYED_PENDING_LIVE_VERIFY | Shadow lane closed-file diagnostic rows persisted; contract held; recurrence today 04:25 with 1 ERROR row. |
| `FU-V105-38-TIMEOUT-EXTENDED-GRACE-PROPOSAL` | OWNER_LOCK | 500 s extended-grace lane proposal only; design proves not a single-constant flip. |
| `FU-V105-35-SEMANTIC-PUBLISH-GATE-LATE-LANE-FORENSIC` | DEPLOYED_PENDING_LIVE_VERIFY | Semantic split deployed; readiness uses output rows, voting uses scoreable rows. |
| `FU-V105-34-OFFICIAL-DIAGNOSTIC-GATE-CLARITY` | DEPLOYED_PENDING_LIVE_VERIFY | Diagnostic rows persisted instead of silent missing; UI label clarity. |
| `FU-V105-32 / V105-33 / V105-31` | DEPLOYED_PENDING_LIVE_VERIFY | Public SSOT wrappers; GLM compact profile proposal owner-gated. |
| `FU-V105-30-SAFE-STDIO-VPS-DEPLOY-AND-RULE105-STRICT-SHADOW` | DEPLOYED_LIVE_VERIFIED_NO_MISSING_EXCEPT_TIMEOUT | Wide `_safe_stdio_ctx` deploy + Rule105 strict shadow; production untouched. |

## 4. Governance lock list (still active)

These locks have been honored continuously since the baseline and remain unchanged:

1. Official `/du-doan` publishes only the fixed 15/15 output-eligible roster.
2. Production prompt content is untouched. Any prompt changes are shadow only.
3. Production scoring formula is untouched.
4. Production selector logic is untouched.
5. Production bundle voting logic is untouched.
6. Production model roster is untouched.
7. WR / BT quality filter remains in place.
8. Timeout values remain `AI_MODEL_SOFT_CONTINUE_SEC=90` and `AI_MODEL_HARD_TIMEOUT_SEC=300`. V105.38 500 s extended-grace is proposal only.
9. Cron timings are unchanged: 04:00 ML, 04:15 MN AI, 16:30 MT AI, 17:35 MB AI, 18:30 MB scrape + verify, plus 5-minute readiness sweep for `/du-doan-test`.
10. No silent missing rows. Every non-timeout failure persists a `[PERSISTED_DIAGNOSTIC_EMPTY]` row.
11. No shadow / lane-test row may backfill official.
12. Official reserve-fill is HOLD. Lane-test reserve-fill is test-only.
13. No manual provider / AI call.
14. No force-publish of MT or MB if output rows fall below 15.
15. Rule105 prize-source lock is per `source_region`, not `target_region`. Production mined-rules table is untouched.

## 5. Owner decision queue (pending today)

| # | Decision | Recommendation |
|---|---|---|
| 1 | Authorize V105.40 expansion patch + service restart after MB 17:35 cycle close (~19:00 VN). | YES |
| 2 | Confirm extended scope: gpt_analyzer.py + main.py 16 sites + Excel writer + verify-final-bundle + Pattern Tracker + Shadow Daily Comparison + Shadow Rule D1 materializer. | YES |
| 3 | Maintain day-control hard lock until both MT 16:30 and MB 17:35 cycles complete naturally. | YES |
| 4 | Public mirror cleanup pushed in this release alongside V105.36 + V105.41. V105.37/38/39 evidence remains private + Notion-mirrored. | YES |
| 5 | Timeout 90/300 preserved. V105.38 500 s remains proposal only. | YES |
| 6 | Direct-API vs OpenRouter shadow A/B continue accumulating; no official route migration. | YES |
| 7 | Source-pool / prompt / top-2 tuning remains held until V105.40 deploys and 24h cycle is clean. | YES |
| 8 | MB lo2 weight A/B (0.95 / 0.75 / 0.55) shadow-only continue. No promote. | YES |
| 9 | Model health scoreboard continue accumulating; no roster change. | YES |

## 6. Stop-loss list

Stop and report to owner if any of these conditions appear:

- An official endpoint returns HTTP 500 outside the known V105.40b path.
- Service status becomes unstable (repeated restart loop).
- Live DB sync hash mismatch repeats more than once.
- Closed-file error appears in the official `auto_daily` path (not just shadow).
- Cron trigger schedule is unexpectedly changed.
- Provider key environment is abnormal (e.g., missing or rotated unexpectedly).
- A patch requires broad rewrite to apply safely.
- Public mirror is dirty in a way that would overwrite remote state on push.
- The owner request requires a manual provider call.
- A request asks to force-publish MT when output rows are below 15.

Default action: `NO_UNSAFE_RECOVERY` · `PENDING_PRESERVED` · `NO_SYSTEM_DAMAGE`.

## 7. Public-safe assertions

- No prediction numbers from pending cycles are disclosed here.
- No credentials, IPs, keys, VPS paths are exposed.
- All metrics derive from the read-only forensic snapshot at 2026-05-14 09:25 VN.
- The official `/du-doan` publish lock is intact and untouched in this release.
