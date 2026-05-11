# V105.29 — Total Force No-Miss Control + Lose-Carryover Signal Layer + Runtime Stability (2026-05-12 00:55 VN)

Status: **PARTIAL_NOT_PASS** + **SHADOW_ONLY** for V105.29 layer + **DO_NOT_PROMOTE** for all candidate policies.

## Headline

- 20 LANE audit complete; 14 lanes PASS, 2 lanes open (stdio deploy + AI priority).
- V105.29 Lose-Carryover Signal Layer materialized: 3785 signals, 6 backtest aggregates, 40 prompt-context traces, 21 Rule105 vs V101 audits.
- Backtest 30d for all 6 LOSE-carryover paths: **break_ratio 0.93–0.99** → DECISIVE `LOSE_CARRYOVER_DO_NOT_PROMOTE`.
- Local `_safe_stdio_ctx` wide patch ready (smoke 3/3 PASS); VPS deploy pending owner OK.
- 30 mined_rules violate owner prize-source lock (MB:13, MN:6, MT:11) → owner decision needed.
- Official 4 tables pre/post sha256 IDENTICAL. Provider/manual AI call count: 0.
- MT_PROTECT_PRESERVED. D-2 leak MT/MB 7d = 0.
- Public GitHub raw still V105.27; local mirror at V105.28+V105.29 (push pending SSH migration).

## Owner decisions (15 items)

See `evidence/V105_29_LOSE_CARRYOVER_RUNTIME_STABILITY_REPORT.md` Section 25. Format trả lời: `A,A,A,A,A,A,A,A,A,A,A,B,A,A,A` (recommend).

P0 items: **#10 (deploy stdio)** + **#9 (SSH migration)**.

## Files

- `evidence/V105_29_LOSE_CARRYOVER_RUNTIME_STABILITY_REPORT.md` — báo cáo VN 28 sections.
- `evidence/v10529_preflight.json` — pre-hash + env state.
- `evidence/v10529_safe_stdio_smoke.json` — 3/3 PASS.
- `evidence/v10529_master_audit.json` — 20 LANE.
- `evidence/v10529_drilldown.json` — LANE 6/9/14 drill.
- `evidence/v10529_post_hash.json` — official unchanged.
- `evidence/_v10529_DEPLOY_SAFE_STDIO_VPS.md` — deploy + rollback script.

## V105.29 shadow tables (local DB)

| Table | Rows | Purpose |
|---|---:|---|
| v10529_lose_carryover_signal_shadow | 3785 | Per-(target_date, region, signal_path, source_tail) candidates |
| v10529_lose_carryover_backtest | 6 | 30d aggregated per (region, signal_path) |
| v10529_ai_prompt_lose_context_trace | 40 | 7d prompt context trace under profile `LOSE_CARRYOVER_CONTEXT_SHADOW_V10529` |
| v10529_rule105_vs_v101_audit | 21 | Per (region, weekday) separation evidence |
| v10529_runtime_summary | 4 | Lane verdict labels |

All shadow_only=1, output_eligible=0, diagnostic_only=1, owner_approved=0, official_impact=false.

## Hard locks observed

- /du-doan, /api/final-bundle, generate_final_bundle, official scoring/selector/voting, production prompt, model roster, official output eligibility, MT source formula, MB source formula primary — **none changed**.
- Token once/day/region/model contract — preserved.
- Station canonical — owner decision pending; no auto-flip.

## Next step

After owner OK Decision #10 + #9, execute `_v10529_DEPLOY_SAFE_STDIO_VPS.md`, verify live cascade, push public mirror, create Notion V105.29 page.
