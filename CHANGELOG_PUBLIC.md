# CHANGELOG (public-side)

## V74 — TOTAL FORCE AUDIT (2026-05-07)
- Runtime verified V73; PASS on A/B/C/D/E/F/I.
- Fixed: C-16 2026-05-07 → 20 voters; CONSENSUS_V1 re-backfilled; C-03 PENDING 37→9; C-17B output_lock_status column added.
- Governance: CONTINUOUS_MEASUREMENT_DOCTRINE / METRIC_DICTIONARY / OFFICIAL_PROMOTION_GATE / TEST_LANE_METHOD_REGISTRY (4 new docs).
- GitHub metadata: LATEST_REPORT.json / REPORT_INDEX.md / CHANGELOG_PUBLIC.md / OPEN_ISSUES.md / NEXT_ACTION.md / DELTA_INDEX.md.
- README rewritten (was stale at V62).
- Open issues: C-05 latency live capture STILL BROKEN (0/83 rows latency_available); flagged P0 for next session.

## V73 — Region-adaptive HYBRID (2026-05-07)
- Per-region priority: MN/MB exploit-first; MT consensus-first; CROWN if exploit==consensus.
- 14d backfill ALL-region n=42: HYBRID 57.1% [42.2-70.9] +1808u vs OFFICIAL 42.9% +1358u (+14.2pp / +450u).
- MN 64.3% (+21.4pp), MT 57.1% (tied), MB 50.0% (+21.4pp).

## V72 — V67 STRICT reverted to eager (2026-05-07)
- STRICT_MIN_CONTRIBUTIONS=0; STRICT_SCORE_THRESHOLD=0.0.
- V67 sample restored 10→17 picks; profit +440u→+753u.
- CONSENSUS agreement counts increased.

## V71 — HYBRID_V1 + C-16 score-gate fix (2026-05-07)
- Removed 0.42 absolute score gate (was MN-biased) so MN/MT/MB all reach target_max=20.
- HYBRID 5-tier (CROWN/HIGH/MEDIUM/LOW/SKIP) initial.

## V69/V70 — metrics + CONSENSUS_V1 (2026-05-07)
- Discovery: 3+ method agreement → 64.3% hit rate vs 28.9% single-method.
- CONSENSUS_V1 selector deployed (gate ≥3).

## V68 — MT diagnostic + C-16 expand 8-10→15-20 (2026-05-07)
- C-16 budget widened.

## V67 — ADAPTIVE_EXPLOIT_V1 deployed (2026-05-07)
- Per-V66.1 BOOST signals exploit selector test-lane only.

## V66 / V66.1 — lag-1 + cross-region adaptive exploit measurement (2026-05-07)
- 11 flow_types signal materializer.

## V65 — lag-1 leakage + strength priority + test-lane weighting audit (2026-05-06)
- Detected MN final_bundle BT lose-then-hit pattern; cross-region MN→MT next-day +26 pp.

## V64 — hardening audit (2026-05-06)
## V63 — C-05 latency instrumentation + C-03 multi-region evaluator (2026-05-06)
## V62 — Notion AI logical synthesis + report export rule sync (2026-05-06)
