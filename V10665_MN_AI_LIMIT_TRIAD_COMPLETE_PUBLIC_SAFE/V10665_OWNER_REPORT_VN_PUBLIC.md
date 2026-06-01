# V10665 — MN AI LIMIT Planner Completes 3-Region Triad (MB + MT + MN)

Public-safe report. No private endpoints, no IP, no internal paths.

## 1. Context

After seeing the MT auto-cron pattern (V10664), the owner approved extending the same auto cron to MN and MB: "MN va MB cung tuong tu giong MT auto cron tot hon, mem deo linh hoat hop ly hon" (the same auto cron pattern for MN and MB is also good — flexible and reasonable).

Verified MB already had its planner running automatically at 09:30 daily since V10662 (blocked list 12 models, all REDUCED_WATCHING with edge_pp ≤ -3.1, 0 RECOVERING — exactly as designed). Then added the missing MN planner to complete the 3-region triad.

## 2. New MN Planner

`_v10665_mn_ai_limit.py` mirrors the MB and MT pattern for region MN. Same logic: read `model_progress` for MN, classify AI-token models as LIMIT (edge_pp ≤ -3 with sample size ≥ 20), RELEASE (RECOVERING or edge_pp ≥ 0), KEEP (status KEEP), or THIN. Writes its own `mn_ai_limit_plan` table; auto-refreshes `slice_policy.MN.blocked_models_json` daily; `slice_policy.MN.enabled=0` preserved.

Scheduled at 09:32 (right after MB 09:30 and MT 09:31).

Note: MN currently uses a separate specialist override, so `slice_policy.MN.enabled=0` means the blocked list is advisory only — it does not block MN voting today. If the owner ever rolls back the override or wires the policy later, the RECOVERING models will already be auto-excluded by construction.

## 3. First Run Output

33 MN AI-token models tracked:

- **5 LIMIT** — gpt-5-mini -3.3pp (REDUCED_WATCHING), gpt-5.4 -6.6pp (WATCH_CUT), grok-4.20-multi-agent -3.3pp (WATCH_CUT), kimi-k2.5 -4.0pp (WATCH_CUT), qwen3-max-thinking -5.3pp (WATCH_CUT)
- **12 RELEASE** — includes all healthy KEEP models (gpt-5.5 +13.4pp, qwen3.6-plus +13.4pp, claude-opus-4-20250514 +6.7pp, gemini-2.5-flash +6.7pp, claude-sonnet-4-6 +3.4pp, gemini-2.5-pro +3.4pp, gemini-3-flash +4.9pp, gemini-3.1-pro +4.9pp, gpt-oss-120b +3.2pp, gemma-4-31b +0.7pp, deepseek-v4-pro +0.1pp, deepseek-v4-flash +0.1pp)
- **3 KEEP** — deepseek-reasoner -1.9pp, glm-5.1 -1.0pp, qwen3-coder -0.4pp (borderline WATCH_CUT, kept full weight)
- **13 THIN** — insufficient sample, no decision

`slice_policy.MN.blocked_models_json` went from 1 model (manual single-entry from earlier) to 5 models (data-driven auto-detect). All 5 are confirmed edge-negative with the correct status. 0 RECOVERING in the blocked list, as designed. `enabled=0` preserved.

## 4. 3-Region Triad Now Complete

| Region | Planner | Cron | First-run blocked | enabled |
|---|---|---|---|---|
| MB | V10662 | 09:30 daily | 12 (all REDUCED_WATCHING) | 0 |
| MT | V10664 | 09:31 daily | 7 (all REDUCED_WATCHING / WATCH) | 0 |
| MN | V10665 | 09:32 daily | 5 (REDUCED_WATCHING + WATCH_CUT) | 0 |

Per-region independence preserved per owner directive: 3 separate planner files, 3 separate cron lines, 3 separate plan tables. Any region can be rolled back, paused, or tuned independently without affecting the others.

## 5. Safety

- No code change in any official prediction path.
- No DB table dropped or modified beyond `mn_ai_limit_plan` (new) and `slice_policy.MN` row update.
- The 4 official prediction tables had identical sha256 pre and post the change.
- `slice_policy.MN.enabled=0` preserved → no impact on MN voting today.
- Backup snapshots BEFORE and AFTER of `slice_policy.MN` row saved.
- Crontab backup saved before the cron line was added.
- py_compile PASS on local and VPS. Service active. /login HTTP 200.

## 6. Watch Plan

Daily auto refresh now self-maintains. After ~14 days of stable plans across the 3 regions (LIMIT lists stable, no false-positive recoveries), the owner can decide whether to wire `slice_policy.<region>.enabled=1` for any region. MN-specific note: as long as the specialist override is the primary MN strategy, the MN advisory list is informational only.

## 7. STATUS

PUBLIC_SAFE — no IP / no internal paths / no provider keys / no DB DDL exposure / no private repo references.
