# CASCADE / DD TRƯỚC-DD SAU / NO-TOKEN RUNTIME VERIFY — V105.27

## 1. Contract under audit

| Region | 04:00 first pass | After MN verify | After MT verify | After MB verify |
|---|---|---|---|---|
| MN | No-token + AI → DD Sau (D-1/D-2 completed context) | Freeze MN only. No MN no-token rerun. AI not chained again. | n/a | n/a |
| MT | No-token → DD Trước; AI → not yet (chained later) | No-token `rerun_post_mn` → DD Sau. AI `ai_chain` → DD Sau. | Freeze MT only. | n/a |
| MB | No-token → DD Trước; AI → not yet | Optional intermediate no-token `rerun_post_mn` → DD Sau (label rõ). Wait MT. | No-token `rerun_post_mt` → DD Sau. AI `ai_chain` → DD Sau. | Freeze MB / close day. |

## 2. Live evidence — 2026-05-11 (today)

Sources: `predictions` (live-sync 18:05:55), `scheduler_logs` (`log_time` is UTC; +07:00 for VN time).

| Time (VN) | Event | Outcome |
|---|---|---|
| 04:00 | MN/MT/MB no-token first pass | `auto_daily` 7/7/7 rows; AI MN `auto_daily` 8/8 |
| 16:38:52 | MN scrape complete (3 stations, 11 retries) | `[SCRAPE_COMPLETE] MN: 3/3 stations OK` |
| 16:38:53 | MN verify final bundle, WIN '01' | `📊 Xác minh MN: WIN (Trúng: ['01'])`; `🔒 [REGION_FROZEN_H2_ONLY] MN 2026-05-11` |
| 16:38:53 | `_rerun_free_models_after_scrape("MN")` | `🏁 Re-predict hoàn tất: 0 thành công, 14 lỗi (trigger: MN)` — every ML call raised `I/O operation on closed file.` |
| 16:38:55 | AI chain MT triggered | `⏰ AI Predict Job triggered: MT (2026-05-11) [source=ai_chain]` — AI succeeded (8 rows in DB) |
| 17:30:00 | MT scrape complete (2 stations) | `✅ Đã cào MT: 2 đài` |
| 17:30:00 | MT verify final bundle, LOSE | `📊 Xác minh MT: LOSE (Trúng: [])`; `🔒 [REGION_FROZEN_H2_ONLY] MT 2026-05-11` |
| 17:30:05 | `_rerun_free_models_after_scrape("MT")` | `🏁 Re-predict hoàn tất: 7 thành công, 0 lỗi (trigger: MT)` ✅ |
| 17:30:08 | AI chain MB triggered | `⏰ AI Predict Job triggered: MB (2026-05-11) [source=ai_chain]` |
| 17:32-17:38 | MB AI chain runs | 8 `ai_chain` rows persisted |

### 2.1 Resulting prediction shape (`predictions` 2026-05-11)

| target_region | run_source | count | Notes |
|---|---|---:|---|
| MN | auto_daily | 7 no-token + 8 AI = 15 official | DD Sau by contract |
| MT | auto_daily | 7 no-token | **MISSING `rerun_post_mn` rows (closed-file crash) — DD Trước stays the only no-token surface** |
| MT | ai_chain | 8 AI | DD Sau |
| MB | rerun_post_mt | 7 no-token | DD Sau (last-write wins; auto_daily rows replaced by `INSERT OR REPLACE` keyed on date+region+model) |
| MB | ai_chain | 8 AI | DD Sau |

### 2.2 Per-row cascade verdict

| Date | Region | Expected stage | Actual run_source/count | UI column | Status | Root cause |
|---|---|---|---|---|---|---|
| 2026-05-11 | MN | auto_daily 7 (no-token) + auto_daily 8 (AI) | 7 + 8 | DD Sau | `CONTRACT_MATCH` | by design |
| 2026-05-11 | MT | auto_daily 7 + rerun_post_mn 7 + ai_chain 8 | auto_daily 7 + **rerun_post_mn 0** + ai_chain 8 | DD Trước (no-token), DD Sau (AI) | `NO_TOKEN_CASCADE_FAIL` | closed-file at 16:38:53; intermittent |
| 2026-05-11 | MB | auto_daily 7 + rerun_post_mn 7 (intermediate) + rerun_post_mt 7 + ai_chain 8 | rerun_post_mt 7 (overwrites auto_daily) + ai_chain 8; **rerun_post_mn skipped/crashed at 16:38:53** | DD Sau via rerun_post_mt | `PARTIAL_CASCADE_OK` | MT cascade succeeded once stdio became usable again |
| 2026-05-10 | MT | rerun_post_mn 7 | 7 ✓ | DD Sau | `CONTRACT_MATCH` | |
| 2026-05-10 | MB | rerun_post_mn 7 + rerun_post_mt 7 | 7 + 7 ✓ | DD Sau | `CONTRACT_MATCH` | |
| 2026-05-09 | MT | rerun_post_mn 7 | 7 ✓ | DD Sau | `CONTRACT_MATCH` | |
| 2026-05-09 | MB | rerun_post_mt 7 | 7 ✓ | DD Sau | `CONTRACT_MATCH` | |
| 2026-05-08 | MT/MB | 7/7 | 7/7 ✓ | DD Sau | `CONTRACT_MATCH` | |
| 2026-05-07 | MT/MB | 7/7 | 7/7 ✓ | DD Sau | `CONTRACT_MATCH` | |

## 3. Closed-file regression status

| Window (VN) | Region/job | Event count | Verdict |
|---|---|---|---|
| 2026-05-11 02:00:33 .. 02:30:48 | MN shadow_auto_eval token catch-up | ~24 `I/O operation on closed file` lines | Side-effect of overnight catch-up bucket (token already once-daily) |
| 2026-05-11 16:38:53 .. 16:38:54 | MN cascade ML rerun + verify_final_bundle + Excel update | 40+ lines including `Re-predict MT/MB ...: I/O operation on closed file` | **Primary cascade failure of the day** |
| 2026-05-11 17:30:05 .. now | MT cascade ML rerun | 0 lines | Recovered (stdio usable) |
| 2026-05-10 ... | mixed | 45 lines | Same intermittent pattern |

Conclusion: closed-stdio is **intermittent**. Sometimes systemd thread inherits a usable stdout, sometimes not. The `_safe_stdio_ctx` wrapper in V105.25b is the correct mitigation but is **NOT yet deployed to VPS**.

## 4. `_safe_stdio_ctx` deploy status

- Code: present in `web/backend/scheduler.py` (module-level `_SafeNullWriter`, `_safe_stdio_ctx`, refactored `_run_free_model_prediction` and `_rerun_free_models_after_scrape` with public wrapper + `_inner` body).
- Local smoke: `artifacts/v105_25_cascade_audit/_smoke_ctx_only.py` PASS (closed stdout/stderr absorbed; intended exceptions still surface).
- VPS deploy: NOT DONE this session. `FU-V105-25B-CASCADE-CONTRACT-MT-PROTECT.next_action` requires owner gate.

## 5. Provider call count

Provider calls executed by this audit session: **0**.

## 6. Verdicts

- `CASCADE_VERIFY_PENDING` for 2026-05-11 MT/MB no-token `rerun_post_mn` (failed today).
- `CLOSED_FILE_FIXED_PENDING_LIVE` — code is in repo; needs VPS deploy + 7/14 day natural-run verify to flip to `LIVE_VERIFIED`.
- `MT_PROTECT_PRESERVED` — no MT selector/scoring/prompt/source-pool change.
- `MB_FORENSIC_ONLY` — MB AI chain happens once after MT verify per contract; no MB_D_v2 active.
- `NATURAL_LIVE_VERIFY_PENDING` — after stdio harden deploy, expect `Re-predict hoàn tất: N thành công, 0 lỗi` and 7/7 `rerun_post_mn` rows for both MT and MB on the next MN verify cycle.
