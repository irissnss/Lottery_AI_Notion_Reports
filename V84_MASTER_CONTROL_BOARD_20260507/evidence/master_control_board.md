# V84 — Master Control Board

Generated: 2026-05-07T23:33:33+07:00

Một bảng duy nhất gom toàn bộ method/issue/family/wave từ V63→V83. Mỗi dòng = một item, có ngày trigger, decision_date, pass/fail, owner_gate.

| Family | Method/Issue | Current state | Evidence | 60d? | Live proof | Next trigger | Decision date | Pass condition | Fail condition | Owner gate? | Official impact | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OFFICIAL | OFFICIAL_BASELINE | PRODUCTION_LIVE | 60d Wilson MN 45% / MT 50% / MB 25% | YES | PRODUCTION | Always | — | Continue | Cold streak alert | Yes for change | — | DO NOT TOUCH |
| V52.5 | MN_SPECIALIST_ROSTER_V1 | 60D_PROVEN | n=60 hit=51.7% save=4 break=0 | YES | 60D | 14d fresh-live (2026-05-21) | 2026-05-21 | win_flip > lose_flip + Wilson > OFFICIAL | Lift loss or MT break | YES for test-lane voter | Test-lane only | Draft dossier 2026-05-21 |
| V52.5 | MN_AI_CHAIN_PRESERVATION_V1 | 60D_PROVEN | n=59 hit=52.5% save=5 break=1 | YES | 60D | 14d fresh-live | 2026-05-21 | Sustain lift | Lift loss | YES for test-lane voter | Test-lane only | Draft dossier 2026-05-21 |
| V52.5 | MT_AI_CHAIN_PRESERVATION_V1 | 60D_DESTRUCTIVE_PROVEN | n=60 hit=41.7% break=12 | YES | 60D | — | — | — | Already failed for MT | — | — | DO_NOT_PROMOTE_MT |
| V52.5 | MB_SPECIALIST_ROSTER_V1 | PROMISING_LIMITED | n=41 hit=36.6% save=5 break=0 | PARTIAL | 41D | 60d gate (2026-07-06) | 2026-07-06 | Reach n=60 + sustain lift | Lift loss with full sample | YES | Test-lane only | Wait + monitor |
| V67_EXPLOIT | ADAPTIVE_EXPLOIT_V1 (MN/MT/MB) | DEPLOYED_EAGER + 1D_EMIT_FRESH | 12 trace + 3 emit rows | NO | 1D | Cron 23:40 VN daily | 14d (2026-05-21) | win_flip > lose_flip 14d + MT no break | Single-source destructive | YES for promotion | Test-lane only | Wait natural cron |
| V70_CONSENSUS | CONSENSUS_V1 | DEPLOYED + 4D_EMIT_FRESH | 12 emit rows post-fix | NO | 4D | Cron 23:45 VN + V77 19:00 rerun | 14d (2026-05-21) | agreement_count >= 3 sustained + lift > OFFICIAL | Coverage drop | YES | Test-lane only | Wait natural cron |
| V73_HYBRID | HYBRID_V1 region-adaptive | DEPLOYED + 4D_EMIT | 45 trace + 12 emit rows | NO | 4-15D | Cron 23:48 VN | 14d (2026-05-21) | Per-region tier + lift | Region break | YES | Test-lane only | Wait natural cron |
| V76 | drift / latency / cost | DEPLOYED ALERT_ONLY | 12 GRAY rows (n30<10) | NO (need 14d fresh) | ALERT_ONLY | Active alert after 2026-05-21 | 2026-05-21 | RED/ORANGE/YELLOW alerts triage | Auto-rollback (forbidden) | — | — | Wait 14d fresh + auto activate |
| V77 | fast incident + post-cascade rerun | DEPLOYED + cron 19:00 + 19:05 | 5 RED_FAST + 1 BUDGET_FAIL_FAST + 9 GREEN @ 2026-05-07 | NO | 1D | Cron 19:00/19:05 daily | Continuous | Alert triage | — | — | — | Continue |
| V78 | AI prompt region-specialist shadow audit | DEPLOYED + cron 19:10 (no provider call) | 86 shadow rows + 3 region prompt files | NO | 1D | Cron 19:10 daily | — | Audit only | — | — | — | Continue |
| V79 | AI↔NO_TOKEN cross-verify + cluster-weighted | DEPLOYED + cron 19:08 + 4D | 12 cross + 130 cluster rows | NO | 4D | Cron 19:08 daily | 14d (2026-05-21) | Cluster lift > OFFICIAL Wilson upper | MT cluster break | YES for promotion | Test-lane only | Wait 14d natural |
| V80 | rule_phase_synthesis + no_token_rule_pack + mb_regime + mn_v67_save | DEPLOYED + cron 19:12 + 4D + NO CONSUMER | 32 rows across 4 tables | NO | 4D | Cron 19:12 daily | Continuous monitor | Surface consumer when promoted | — | YES for consumer | — | Continue monitoring |
| V81 | Provider shadow pilot 3 models | DEPLOYED + cron 19:14 + 2D | 18 calls 18 OK 0 break | NO | 2D | Cron 19:14 daily | 14d (2026-05-21) | would_save > would_break per model + region | Provider error rate >10% or break > save | YES for promotion | Shadow only | Continue + GPT-5-mini key fix |
| V82 | 60d evidence control pass | DELIVERED + AUDIT_DONE | 307 audit cells | YES (where data exists) | AUDIT_ONLY | — | — | — | — | — | — | Refer to V82 report |
| V83 | V82 monitor UI panel | DEPLOYED + admin-only | /v82-monitor 401 unauth, 200 admin | — | LIVE_API | Owner login + view | Owner verify any time | Display correct | Layout broken | OK to extend if needed | — | Owner verify |
| P0 portfolio | 18 multi-lane shadow methods | DEPLOYED + 8-11D | 504-516 scoreboard rows per method, 14d shadow_results region split | PARTIAL (need 49+ days) | 8-11D | Continuous post-closeout cron | Per method min_days/min_samples (3-14d) | Per-method maturity gate | DESTRUCTIVE_BIAS (lose_flip > win_flip) | YES for any promotion | Shadow only | Per-method maturity matrix; see 17_methods_status.md |
| Wave 1 | Wave 1 control surfaces (9 tables) | DEPLOYED + LIVE_PROVEN | FU-031 + FU-026 backfill | PARTIAL (since 2026-04-25) | 12+D | Continuous | — | — | — | — | — | Continue |
| Wave 2 | PP-1 + verdict_dist + prompt_section_breakdown | DEPLOYED + LIVE_PROVEN | FU-043 | PARTIAL | 12+D | Continuous | — | — | — | — | — | Continue |
| D items | D-1 / D-2 audits | DOC_COMPLETE_SUBSUMED | Phase checkpoint files 2026-05-01 | — | DOC | — | — | — | — | — | — | Subsumed by P0 portfolio |
| D items | D-7 (ambiguous) | AMBIGUOUS_LABEL_RESOLVED | No standalone deliverable found | — | — | — | — | — | — | — | — | Treat as 7d gate concept (decision_calendar) |
| Timezone HCM | P0.6 helpers + cron VN | BUG_CONTAINED_BY_HELPERS | _today_vn_date_str / _tomorrow_vn_date_str | — | PROVEN since V78 fix | — | — | — | Regression check | — | — | Continuous + P1 audit legacy datetime |
| Hash guard | 4 official tables sha256 | ACTIVE | predictions=25d1a3db, final_bundles=999d42cb, lottery_results=937407fe, model_daily_eval=07a53a97 | — | PROVEN every session | Pre + post each deploy | Always | PRE = POST | STOP + investigate | — | GUARD | Continuous |
