# PROMPT INJECTION GAP / MN D-2 — V105.27

## 1. V105.26 claims under audit

| Claim | Verified? | Evidence |
|---|---|---|
| `mn_d2_rows` exist as shadow data | NOT confirmed locally — no dedicated `mn_d2_*` table | `db_tables.json` has no `mn_d2_*` |
| `mn_d2_top5_rows` exist | NOT confirmed locally | same |
| MT D-2 leak = 0 | YES — `d2_leak_in_predictions` query returned 0 rows | `proxy_evidence.json:d2_leak_in_predictions` |
| MB D-2 leak = 0 | YES — same query | same |
| MN D-2 prompt seen | NO — `_attach_owner_priority_meta` for MN does not include `MN_D2/MT_D2/MB_D2` keys | `web/backend/scheduler.py:2406-2441` |
| `REAL_PROMPT_NOT_INJECTED` count | Cannot quantify locally without V105.26 source query | n/a |

## 2. Where MN D-2 currently lives in the system

- Statistical analyzer (`meta_predict.run_full_analysis` with `statistical_depth=30`) reaches back 30 days, so D-2 is included in the *statistical* feature set for no-token models.
- AI prompt priority layer (`_attach_owner_priority_meta`) injects only `*_D1` and same-day cross-region for MT/MB.
- Result: MN no-token models implicitly use D-2 via statistical depth, but the AI provider prompt does not explicitly highlight `MN_D2 / MT_D2 / MB_D2` cards.

## 3. Stages and proposed shadow scope

| Stage | Count source | Gap | Region | Next action |
|---|---|---|---|---|
| Source pool includes MN D-2 | `meta_predict.run_full_analysis(days=30)` | implicit only, no explicit `MN_D2` key | MN | Materialize MN-only shadow profile `mn_d2_shadow_v1` adding `MN_D2 / MT_D2 / MB_D2` as priority entries (shadow-only) |
| Prompt explicitly cites MN D-2 | not implemented | gap | MN | Shadow prompt copy in `gpt_analyzer` with `mn_d2_shadow_v1` profile only |
| MT/MB D-2 prompt | 0 | preserved | MT/MB | DO NOT ADD |
| Provider call | 0 | preserved | all | Track natural-run rows only |

## 4. Rules

- Production prompt locked.
- Shadow prompt only.
- No provider calls.
- Do not expand V104 prompt without owner scope.
- Natural-run tracking required (no manual provider invocation) — 7d small-window, 14d statistical window.

## 5. Recommended owner decision

`Continue MN D-2 prompt wire natural-run tracking 7/14 days?` — Recommended YES, shadow-only, MN-only profile, no MT/MB injection, no provider call. Decision item registered in `OWNER_DECISION_REGISTER.md`.

## 6. Verdicts

- `PROMPT_INJECTION_GAP` for MN D-2 explicit injection (low risk; statistical depth already covers D-2 for no-token).
- `D2_MN_ONLY` enforced at runtime (no leakage to MT/MB priority).
- `OWNER_DECISION_PENDING` for whether to wire MN D-2 explicit shadow prompt.
