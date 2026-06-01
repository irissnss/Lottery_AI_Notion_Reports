# V10664 — MT AI LIMIT Planner + Cleanse 4 MT RECOVERING Models from Blocked List

Public-safe report. No private endpoints, no IP, no internal paths.

## 1. Context

Owner asked whether the 4 MT recovering models flagged in V10663 had actually been removed from the blocked list, or just noted for the future.

Investigation showed: although `model_progress` had auto-tagged them RECOVERING, they were still present in `slice_policy.MT.blocked_models_json`. The policy row had `enabled=0` (surface only, not wired into voting), so there was no immediate impact today, but if/when the owner approves wiring later, those 4 recovering models would have been blocked by mistake and the recovery gains would be lost.

Owner chose "both A and B": manual cleanse now for immediate safety, and an auto code fix so the same situation cannot reoccur.

## 2. Action A — Manual cleanse (immediate safety)

Backup the entire `slice_policy.MT` row as a BEFORE snapshot. Removed the 4 RECOVERING models from the blocked list (8 entries → 4 remaining). The 4 remaining are all REDUCED_WATCHING with edge_pp at -4.1 or worse — they correctly belong in the blocked list. Saved an AFTER snapshot for paper trail. The 4 official prediction tables had identical sha256 pre/post, confirming zero impact on official prediction logic. `slice_policy.MT.enabled=0` preserved.

## 3. Action B — Auto code fix (long-term)

Added a new MT-side planner that mirrors the existing MB pattern: it reads `model_progress` for MT, classifies each AI-token model as one of LIMIT (edge_pp ≤ -3 with sufficient sample), RELEASE (RECOVERING or edge_pp ≥ 0), KEEP (status KEEP), or THIN (insufficient sample), and writes the result into a new tracking table. Then it auto-refreshes `slice_policy.MT.blocked_models_json` to contain ONLY the current LIMIT models — RECOVERING/RELEASE/KEEP are now excluded by construction.

Scheduled to run daily at 09:31, immediately after the MB pattern at 09:30. `slice_policy.MT.enabled=0` is preserved by the script, so the surface remains advisory only until the owner approves wiring.

## 4. First Run Output (today)

35 MT AI-token models tracked:

- **7 LIMIT** — deepseek-v4-pro -4.1pp, gemini-3-flash -3.1pp, gemini-3.1-pro -5.5pp, gemma-4-31b -7.1pp, grok-4.20-multi-agent -4.1pp, kimi-k2.5 -9.2pp, qwen3.6-plus -21.8pp
- **12 RELEASE** — includes all 4 RECOVERING (gpt-5.5 +2.8pp, gpt-oss-120b +1.6pp, gpt-5-mini +9.7pp, qwen3-coder +0.6pp) plus 8 KEEP healthy
- **1 KEEP** — deepseek-v4-flash (borderline -1.8 WATCH, kept full weight)
- **15 THIN** — insufficient sample, no decision yet

The auto refresh actually improved on the manual cleanse by detecting 3 new WATCH edge-negative models that the manual list had not included (gemini-3-flash, gemini-3.1-pro, gemma-4-31b). This confirms data-driven detection is more accurate than a static manual list.

Final state of `slice_policy.MT.blocked_models_json`: 7 models (all REDUCED_WATCHING or WATCH with edge_pp clearly negative), 0 RECOVERING. enabled=0.

## 5. Why This Pattern Is Safe

- No code change in any official prediction path. The planner only reads from `model_progress` and writes to its own `mt_ai_limit_plan` table plus refreshes the advisory `slice_policy.MT` row.
- `slice_policy.MT.enabled=0` means the blocked list is not consulted during official voting today.
- Manual cleanse backup snapshots taken before and after the row was updated.
- 4 official prediction tables have identical sha256 pre and post the change.
- The auto planner self-heals: if a model improves into RECOVERING tomorrow, the next 09:31 run automatically removes it from the blocked list.

## 6. Watch Plan

Daily auto refresh now self-maintains. After 7-14 days of stable plan (LIMIT list stable, no false-positive recoveries triggering churn), the owner can decide whether to wire `slice_policy.MT.enabled=1`. Same pattern can later be extended to MN if needed.

## 7. STATUS

PUBLIC_SAFE — no IP / no internal paths / no provider keys / no DB DDL exposure / no private repo references.
