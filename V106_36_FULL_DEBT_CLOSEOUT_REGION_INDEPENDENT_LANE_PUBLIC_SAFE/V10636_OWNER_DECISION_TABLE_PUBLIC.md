> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 OWNER DECISION TABLE

- ts_vn: `2026-05-27T23:08:36`

| Issue | Severity | Status | Decision needed | Default if no decision |
|---|---|---|---|---|
| `MT-CONVERSION-GATE` | P0 | SHADOW_ONLY_NEGATIVE_BACKTEST | Lane net-effect >= 0 over 7 days with conversion gate active. | artifact-only; no production change |
| `MB-COST-WASTE-AI-TOKEN` | P0 | COST_WASTE_CANDIDATE_OWNER_GATE | Owner OK to limit MB AI-token in lane/shadow; no production change. | artifact-only; no production change |
| `FU-V10622-PARALLEL-LIVE-BOARD` | P1 | DEPLOY_GATE_REQUIRED | Owner explicitly approves admin-only read-only deploy. | artifact-only; no production change |
| `FU-V10628R1-NOT-RUN` | P1 | NOT_RUN_BY_DESIGN | Owner explicit approve OR design abandons V10628R1 path. | artifact-only; no production change |
| `MT-FULL-SPENT-BOOST` | P1 | DOMINANCE_OBSERVED | Cap reduces wrong_boosted to <= 3 per region per day in 7d window. | artifact-only; no production change |
| `COHERE-VALUE-UNKNOWN-NOW-PROVEN-ZERO` | P1 | ZERO_VALUE_PROOF_30D_ALL_REGIONS | Owner decision: diagnostic_only OK in lane; production removal requires explicit OK. | artifact-only; no production change |
| `FU-71-PRE-REGISTER-RULES` | P2 | PRE_REGISTER_ONLY_PENDING_90D_FORWARD | Filter survivors with H2-lift >= +3pp after 2026-08-23; only then owner-gated COMMIT_ELIGIBLE_SHADOW. | artifact-only; no production change |
| `FU-105-RULES-INDEPENDENT-QUERY` | P0_THIS_PASS_NOW_RESOLVED_BY_V10636 | QUERY_V2_DESIGNED_LANE_HELPERS_PLANNED | Lane helpers + safety tests pass; 7-day lane-test net-effect > 0 → owner-gated next-step. | artifact-only; no production change |