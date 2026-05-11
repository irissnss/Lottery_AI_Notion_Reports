# NEXT ACTION (V105.27 — 2026-05-11 21:30 VN)

10 owner-gated decisions awaiting explicit OK. See `V105_27_TOTAL_FORCE_CONTROL_20260511/evidence/OWNER_DECISION_REGISTER.md` for full detail.

## P0 — Stability (must clear first)

1. Decision #10 — VPS deploy `_safe_stdio_ctx` patch (scheduler.py). Without this, every `rerun_post_mn` MT no-token batch silently fails with `I/O operation on closed file` and DD Sau MT defaults to D-1 fallback values. Local patch ready, hash captured in `preflight.json`.
2. Decision #9 — Revoke any PAT ever pasted in chat/history; approve SSH deploy-key migration to remove HTTPS+PAT from VPS remote URL. Independent of #10 but must clear before next public push round.

## P1 — Prediction quality (after stability)

3. Decision #1 — Publish V105.24/25/25b/26/27 to Drive + Notion + public mirror (this push window completes part of it).
4. Decision #2 — Approve station alias fixup direction (Huế canonical vs. Thừa Thiên Huế canonical).
5. Decision #3 — Approve MN D-2 prompt wire shadow profile `mn_d2_shadow_v1` (14d shadow, no official promote).
6. Decision #5 — Pick MB_D_v2 shadow option (1) relax TOP30 cap, (2) add source-prize strong class, (3) same-day MN/MT weighting, or (4) add D-2.
7. Decision #4 — Run Top2 A/B shadow 14d for MN+MB (MT measurement-only).
8. Decision #6 — Keep V102 RELAXED HOLD until V103 supply class backfill 14d clean.
9. Decision #8 — Clarify MB `rerun_post_mn` intermediate display label vs. suppress until MT verify.
10. Decision #7 — Keep manual AI/provider "cuốn chiếu" blocked (formal owner confirmation).

## Watch / live verify

- 24h: natural cascade after #10 deploy must show 7/7 MT rerun_post_mn + 7/7 MB rerun_post_mn/mt with 0 closed-file errors.
- 7d: MN D-2 shadow vs no-D-2 shadow delta on entered_top2 / would_save / would_break.
- 14d: V102 RELAXED watch, Top2 A/B shadow, MB_D_v2 shadow scoreboard.
