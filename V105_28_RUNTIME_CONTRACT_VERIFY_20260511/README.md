# V105.28 — Total Force Runtime Contract Verify (2026-05-11 23:35 VN)

Read this first. PARTIAL status — not PASS.

## What

V105.28 audit verifies owner's latest runtime contract:

- DD Trước / DD Sau routing per region × run_source × time
- No-token retrain/reload-before-rerun order around verify
- AI strongest-first ordering by region + weekday
- 90s soft / 300s hard timeout orchestration
- Official 15 / lane-test 20 model count gate
- Region-only freeze (no global)
- `_safe_stdio_ctx` deploy / closed-file regression
- Token / manual provider guard
- GitHub PAT revoke + secret scan + SSH key
- 105 Rules / no-token / 12–16W prompt consistency
- LO1/LO2 mixing scope (lane-test only)
- MT protect regression

## Headline findings

- **OFFICIAL 4 TABLES UNCHANGED** — pre/post sha256 identical for `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`.
- **NO PROVIDER / MANUAL AI** call in session.
- **MT_PROTECT_PRESERVED** absolutely. No D-2 leak. No source formula or selector touched.
- **DD_TRUOC_DD_SAU_MATCH** per `DD_COLUMN_POLICY`.
- **SOFT_90S_CONFIRMED** with 66 live events; HARD_300S not observed in 14d lookback (no model hung beyond 300s).
- **OFFICIAL_15_GATE_CONFIRMED** + **LANE_TEST_20_GATE_CONFIRMED** + **BELOW_BUDGET_LABEL_OK**.
- **REGION_FREEZE_OK** — `save_prediction` LOCK guard is per-row, not global.
- **CLOSED_FILE_DEPLOY_PENDING** — 86 closed_file errors today + 25 yesterday in MB no-token rerun. Local code has `_SafeNullWriter` only inside `_start_timed_model_call` for AI token; no-token path needs the same wrap. Owner OK from V105.27 Decision #10 still applies; deploy still pending.
- **AI_PRIORITY_ORDER_GAP** — scheduler iterates static `AUTO_AI_MODELS`; no region+weekday strongest-first reorder. Strength tensor exists but is not consumed; tensor anchor stale at 2026-05-05.
- **OWNER_CONFIRMED_PAT_REVOKED** = true. Local `web/backend/.env` has real API keys but is gitignored; public/docs scan clean. **SSH_DEPLOY_KEY_PENDING** — owner must set up SSH before next push.

## Files

- `evidence/V105_28_RUNTIME_CONTRACT_REPORT.md` — full Vietnamese report (17 sections).
- `evidence/v10528_preflight.json` — pre-hash + git state + env flags + live sync manifest.
- `evidence/v10528_runtime_contract_audit.json` — 11 lanes audit data.
- `evidence/v10528_deep_probes.json` — closed_file detail + final_bundles below-15 + DD distribution + tensor ranking + manual block log.
- `evidence/v10528_security_and_rules.json` — secret scan + git remote + station identity + 105 rules window consistency + hooks/governance state.
- `evidence/v10528_post_hash.json` — post-hash proof identical to pre-hash for 4 official tables.

## Public shadow tables created locally

- `v10528_dd_truoc_dd_sau_audit` (64 rows)
- `v10528_retrain_order_lineage` (24 rows)
- `v10528_ai_priority_order_proposal` (24 rows)
- `v10528_timeout_event_log_audit` (3 rows)
- `v10528_model_count_gate_audit` (288 rows)
- `v10528_freeze_scope_audit` (24 rows)
- `v10528_safe_stdio_event_audit` (4 rows)
- `v10528_token_manual_guard_audit` (7 rows)
- `v10528_mt_protect_regression_audit` (12 rows)
- `v10528_runtime_contract_summary` (15 rows)

All tables: `shadow_only=1`, `output_eligible=0`, `diagnostic_only=1`, `owner_approved=0`.

## Owner decisions pending

1. Deploy `_safe_stdio_ctx` to the full no-token rerun path (P0 stability).
2. Enable scheduler region+weekday strongest-first reorder (P1 quality).
3. Wire daily strength tensor refresh cron 19:30 VN.
4. Migrate git remote to SSH (HTTPS will fail after PAT revoke).
5. V102 relaxed / Top2 A/B / MB_D_v2 promotion remain blocked.

## Status

**PARTIAL — not PASS.** Official lock proven. MT protect proven. Two gaps need owner OK before next session can claim PASS.
