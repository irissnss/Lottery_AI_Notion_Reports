# P0.1 → P0.6 status matrix

Generated: 2026-05-07T23:05:06+07:00

| P0 | Topic | Implemented | Evidence | 60d | 14d | 7d | Risk | Next action |
|---|---|---|---|---|---|---|---|---|
| P0.1 | Code ↔ Notion reconcile | v80_master_reconcile_matrix=True<br>v80_notion_doc_patch_matrix=True<br>v80_changelog_present=True<br>v80_shadow_materializer_present=True<br>v81_provider_pilot_materializer_present=True<br>ssot_v81_row_present=True<br>fu_147_present=True | artifacts/v80_absolute_closure/master_reconcile_matrix.md; CHANGELOG.md V20.3.37.80 + V20.3.37.81; docs/FOLLOW_UP_TRACKER.md FU-146 + FU-147 | NO | NO | NO | LOW (governance only) | Continuous; new versions must keep this pattern. |
| P0.2 | AI ↔ NO_TOKEN cross-verification | materializer_present=True<br>table_exists=True<br>rows_total=12<br>rows_last_7d=12<br>rows_last_60d=12<br>cron_19_08_registered=True | web/backend/_materialize_ai_no_token_cross_verification_shadow.py; scheduler 19:08 VN cron | NO | NO | NO | LOW shadow only | Wait for 7-14d natural cron rows before promotion proposal. |
| P0.3 | Cluster-weighted consensus | table_exists=True<br>rows_total=130<br>rows_last_60d=130<br>schema_has_independent_cluster_count=True | cluster_weighted_consensus_shadow | NO | NO | NO | LOW shadow only | Use 60d eval in this V82 audit if data permits; otherwise mark LIMITED. |
| P0.4 | Rule-phase synthesis pack | table_exists=True<br>rows_total=12<br>rows_last_7d=12<br>rows_last_60d=12<br>no_token_rule_pack_table=True<br>no_token_rule_pack_rows=12<br>consumed_by_official=False | rule_phase_synthesis_shadow; no_token_rule_aware_pack_shadow | NO | NO | NO | LOW shadow only — not consumed by official prompt | Backfill shadow + observe; no consumer yet (intentional safety). |
| P0.5 | MB regime-shift mode | table_exists=True<br>rows_total=4<br>rows_last_7d=4<br>shadow_only_flags_clean=True | mb_regime_shift_shadow | NO | NO | NO | LOW shadow only | 7d natural watch. |
| P0.6 | Timezone HCM hardening | tzinfo_string_bug_present=True<br>helper_today_present=True<br>helper_tomorrow_present=True<br>cron_chain_19_minutes=[0, 5, 8, 10, 12, 14]<br>vn_tz_constant_typed=True | web/backend/scheduler.py | NO | YES | YES | HIGH if regression — selector chain blocks otherwise | Audit non-scheduler legacy datetime; lock as P1 follow-up. |
