# Decision calendar — V84

Generated: 2026-05-07T23:33:33+07:00

| Ngày VN | Trigger | Item | Required output | Decision rule |
| --- | --- | --- | --- | --- |
| 2026-05-08 | Cron 19:00-19:14 VN natural execution | V77/V77fast/V79/V78/V80/V81 6 cron jobs | log entries + new shadow rows | Auto-verify next morning. If any cron fails → P0 fix. |
| 2026-05-08 | Closeout 18:30-19:00 VN | Day 1 fresh-live for V79 cluster + V81 pilot | would_save / would_break per region | Append to V82 monitor. No promote. |
| 2026-05-09 | Day 2 fresh-live | V79 + V81 cumulative 2 days | Updated V82 monitor | Auto-update SSOT. No promote. |
| 2026-05-10 | Day 3 fresh-live + sample_count gate for min_samples=3 methods | freshness_readiness_guard / strongest_to_final_preservation / no_token_drift_guard / rule_phase_evidence / output_policy_replay / counterfactual_decision_audit / cohere_rerank min sample 3 reached | V84 monitor refresh | Eligible for evaluation, not promotion. |
| 2026-05-12 | Day 5 fresh-live + min_days=5 methods (rule_aware_adaptive_notoken / phase_aware_rerank) | 5d minimum reached | Stats refresh | Eligible for evaluation, not promotion. |
| 2026-05-14 | Day 7 fresh-live | V79/V80/V81 7d rolling review + MB cold streak check (>=7d cold → P0 forensic) | 7d aggregate per region per method | If MB still 0/7 → escalate P0 MB regime forensic. Else continue. |
| 2026-05-21 | Day 14 fresh-live + min_days=14 methods activate | meta_ranker_ltr_dataset / context_specialist_policy / online_bayesian_weighting reach 14d minimum + V79 + V81 14d rolling + drift monitor V76 starts active alert | 14d aggregate; check MN candidates SPECIALIST_ROSTER / AI_CHAIN_PRESERVATION sustain lift; draft MN_TEST_LANE_VOTER_PROPOSAL dossier (no promote) | If MN candidates still + and MT no break → trình owner dossier (test-lane voter only). |
| 2026-06-06 | Day 30 fresh-live | 30d rolling review for selected methods (V79 cluster, V81 pilot, top P0 methods) | 30d Wilson CI | Method that beats baseline + Wilson_lo > baseline_hi → eligible promotion proposal. |
| 2026-07-06 | Day 60 fresh-live | Full 60d rolling review for all V79/V80/V81 surfaces | 60d Wilson CI per region per method | Promotion gate full check + owner OK required for any official change. |
| ANY 19:14 VN failure | Cron failure detected | Auto-FU entry generated | FOLLOW_UP_TRACKER + AUTOMATION_HISTORY | Re-run / fix / disable per FU entry. |
| Always | Pre/post hash mismatch on official tables | Hash guard violation | Block deployment | STOP + investigate before any further action. |
