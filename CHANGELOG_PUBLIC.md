## V84 — MASTER CONTROL BOARD (2026-05-07 23:30 VN)

- 24-row master control board covering ALL families V63 → V83.
- 18-method P0 portfolio maturity matrix: 14 READY_TO_EVALUATE, 4 WAIT 5 days (until 2026-05-12).
- 14d region split: 2 POTENTIAL_LIFT (strongest_to_final_preservation, counterfactual_decision_audit), 3 DESTRUCTIVE_BIAS.
- 60d evidence availability map per family.
- Decision calendar 11 specific VN dates 2026-05-08 → 2026-07-06.
- Owner-gate queue 9 items with trigger dates.
- D-1/D-2 subsumed; D-7 ambiguous resolved as 7d gate concept.
- UI master board spec proposed (owner OK pending).
- 4 official tables hash UNCHANGED.

## V83 — V82 MONITOR UI PANEL (admin-only, read-only) (2026-05-07 23:20 VN)

- New backend module `web/backend/_v82_monitor.py` (read-only payload, 18 keys).
- 2 new admin-required routes: `GET /v82-monitor` (HTML) + `GET /api/admin/v82-monitor` (JSON).
- New frontend `web/frontend/v82-monitor.html` — 7-section dashboard, auto-refresh 5min.
- Hard contract honored: NO promote/rollback/edit/trigger button, NO DB write, NO scoring/selector change.
- Pre/post hashes 4 official tables UNCHANGED.

## V82 — 60D EVIDENCE CONTROL PASS (2026-05-07 23:05 VN)

- 307 audit cells (method × region × window {60, 30, 14, 7, 4}).
- 60D real evidence: OFFICIAL/AI_HERD/NO_TOKEN_HERD + 6 V52.5 methods.
- MN: 2 promotion candidates clean lift — SPECIALIST_ROSTER +6.7pp (save=4 break=0); AI_CHAIN_PRESERVATION +7.5pp (save=5 break=1).
- MT: consensus-first doctrine confirmed (AI_HERD -6.7pp with 12 breaks).
- MB: cold confirmed; all methods within ±5pp.
- V67/V70/V73/V79 max 4-15d; V81 2d → RETRO_LIMITED, no promotion.
- NO_TOKEN vs AI: region-specific (MN +3.4pp, MT +8.3pp, MB -3.3pp); no global floor change.
- Hash guard: 4 official tables UNCHANGED.

## V81 — PROVIDER SHADOW PILOT (owner-approved) (2026-05-07 22:18 VN)

- 3 models × 3 regions × 2 days = 18 provider calls. 18/18 parse_status=OK. 0 contract violations.
- Each model: hits=3/6, would_save=1, would_break=0 (n=6).
- MN 2026-05-07: all 3 models converge on V67/V73 tail 95 vs OFFICIAL 94 (would_save).
- MT: stable consensus. MB: honest LOW conf + herd warnings.
- New cron 19:14 VN. Cron now 6 jobs daily.
- Hard contract: shadow_only=1, output_eligible=0, output_impact='false'. Official tables UNCHANGED.

## V80 — ABSOLUTE CLOSURE PASS (2026-05-07 21:55 VN)

- Notion MCP doctrine pages reconciled with code (7 key pages patched).
- New shadow tables: rule_phase_synthesis_shadow / no_token_rule_aware_pack_shadow / mb_regime_shift_shadow / mn_ai_herd_vs_v67_save_daily.
- New cron 19:12 VN. Official tables UNCHANGED.

## V79 — AI↔NO_TOKEN CROSS-VERIFICATION + CLUSTER-WEIGHTED CONSENSUS (2026-05-07 19:08 VN)

- Cluster-weighted consensus shadow + AI/NO_TOKEN cross-verification.
- Region policies: MN V67/V73 boost, MB cold treatment, MT consensus-first.
- New cron 19:08 VN. Official tables UNCHANGED.

## V78 — AI PROMPT/CONTEXT FORENSIC + REGION-SPECIALIST SHADOW PROMPTS (2026-05-07 19:10 VN)

- Region-specialist shadow prompts MN/MT/MB authored and audited (no provider call yet at V78).
- Scheduler tzinfo bug fixed (V77 selector chain).
- New cron 19:10 VN. Official tables UNCHANGED.

# CHANGELOG_PUBLIC

## V80
- Notion/code/runtime sync closure.
- Shadow completion surfaces.
- Official unchanged.

## V79
- AI↔NO_TOKEN cross verification.
