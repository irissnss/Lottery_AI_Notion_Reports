# D-1 / D-2 / D-7 / Wave items reconciliation

| Item | First seen | Purpose | Status | Still relevant? | Next action |
| --- | --- | --- | --- | --- | --- |
| D-1 RULE_MECHANISM_FULL_AUDIT | 2026-05-01 phase_checkpoint D1_RULE_MECHANISM_FULL_AUDIT_20260501.md | Audit toàn bộ rule mechanism (current_week, 12W scan, source-prize) | DOC_COMPLETE → consumed by P0 portfolio rule_phase_evidence_v1 + rule_injection_contract_v1 | YES (subsumed) | No standalone action; tracked via rule_phase_evidence shadow. |
| D-2 OVERREACH_ROLLBACK_AUDIT | 2026-05-01 phase_checkpoint D2_OVERREACH_ROLLBACK_AUDIT_20260501.md | Verify D-1 changes did not overreach into official | DOC_COMPLETE | YES (governance principle still active) | Continue applied as anti-overreach principle for V84+. |
| D-7 ITEMS (ambiguous label) | 2026-04 era references | AMBIGUOUS — appears to refer to 7-day rolling proof requirement, not a specific deliverable | AMBIGUOUS_LABEL — resolved as 7d_proof gate concept, applied per-method in V84 maturity matrix | YES (concept, not standalone) | Use 7d/14d gates in decision_calendar; no standalone D-7 deliverable found. |
| Wave 1 (V20.3.18-20) | FU-026/FU-031/FU-043 in tracker | Wave 1 control surfaces (ai_primary_gate, strongest_candidate_escape, weekday_rule_strength, bundle_readiness_gate, public_bundle_publish_audit, output_eligible_completion, reasoning_layer_penetration, ai_reasoning_contract, source_prize_effectiveness, convergence_cluster_pattern_daily) | DEPLOYED + LIVE_PROVEN since 2026-04-25 | YES (active measurement) | Continuous; cron auto-materializes after closeout. |
| Wave 2 (V20.3.22) | FU-043 | Wave 2 measurement-safe surfaces (PP-1 live watch, verdict_distribution_daily, prompt_section_breakdown) | DEPLOYED + LIVE_PROVEN | YES | Continuous. |
| P0 portfolio 17→18 methods | 2026-04-28 EXECUTION_CLOSEOUT | P0/P0.5/P0.7/P0.8/P0.9 multi-lane shadow scaffold + cohere_rerank bridge | DEPLOYED + 18 methods registered + 8-11 days of cron data | YES | Reach min_days/min_samples per method; see V84 maturity matrix. |
| P0.10 / Tier-A scaffolds (V20.3.37.24) | FU-071 | Tier-A scaffold methods within multi-lane shadow | DEPLOYED + measured | YES | Continuous. |
| M-NOW-1/2/3 measurement writers | FU-058+ | Measurement-only writers triggered post-closeout | DEPLOYED | YES | Continuous. |
