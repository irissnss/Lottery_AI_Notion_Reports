# V91 — Decision Calendar (hardened)

Generated 2026-05-08T01:19:20+07:00

Mỗi mốc có pass/fail condition + owner_action + auto_report path.

| Date VN | Trigger | Item | Pass condition | Fail condition | Owner action | Auto-report path |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-05-08 | Cron 19:00-19:14 VN natural | 6 cron job natural proof | All 6 jobs log success | Any cron error → P0 fix | None (auto) | scheduler_logs |
| 2026-05-08 | Closeout 18:30 VN | Day 1 fresh-live V79 cluster + V81 pilot | would_save/break tracked | Provider error rate >10% | None | ai_no_token_cross_verification_shadow + ai_region_specialist_provider_shadow_results |
| 2026-05-12 | Day 5 + min_days=14 methods reach 14d | 4 P0 methods (meta_ranker_ltr_dataset / context_specialist_policy / online_bayesian_weighting + 1) reach 14d minimum | Days observed >= 14 | Methods drop coverage | Eligible for evaluation, not promotion | shadow_method_scoreboard |
| 2026-05-14 | Day 7 fresh-live | V79/V80/V81 7d rolling + MB cold-streak escalation gate | MN/MT V81 saves > 0; MB cold streak < 7 | MB OFFICIAL 0/7 → P0 forensic auto-trigger | Read MB forensic dossier if escalated | mb_regime_shift_shadow + V81 pilot rolling |
| 2026-05-21 | Day 14 + min_days=14 methods activate | 14d full review + MN dossier draft + drift V76 active | MN candidates sustain lift + MT no break | MN lift loss or MT break | Read MN_TEST_LANE_VOTER_PROPOSAL dossier (em sẽ chuẩn bị trước) | MN_TEST_LANE_VOTER_PROPOSAL.md |
| 2026-06-06 | Day 30 fresh-live | 30d rolling for V79/V80/V81 + top P0 methods | Method beats baseline + Wilson_lo > baseline_hi | Lift loss with full sample | Owner OK before any promotion proposal | V92_30D_AUDIT_PASS_20260606.md (proposed) |
| 2026-07-06 | Day 60 fresh-live | Full 60d rolling V79/V80/V81 + MB SPECIALIST_ROSTER | 60d Wilson CI > baseline + zero MT break | Below baseline or MT break detected | Owner explicit OK + dossier review | V93_60D_FULL_AUDIT_20260706.md (proposed) |
| ANY 19:14 VN failure | Cron failure detected | Auto-FU entry + scheduler_logs alert | — | — | Read FU + decide | FOLLOW_UP_TRACKER auto-append |
| Always | Pre/post hash mismatch | Hash guard violation on official tables | PRE = POST byte-identical | STOP + investigate before any further action | Confirm rollback if needed | _v74_write_pre_hash.py output |
| V91 today | Stale FU reconciliation | 74/154 stale FU items reviewed | All flagged with classification | — | None (V91 done) | FU_STALE_RECONCILIATION_MATRIX.md |
