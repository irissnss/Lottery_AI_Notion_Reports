# NEXT ACTION

V77 đã handle owner emergency. Next focus: verify cron 19:00 + 19:05 VN tomorrow + monitor MN/MB cold streak.

## Tomorrow 2026-05-08 (post-V77 verification)

1. **19:00 VN** — Verify V77 post-cascade rerun cron fires. V70 should produce CONSENSUS rows with `agreement_count >= 3` for at least MN/MT (MB cold).
2. **19:05 VN** — Verify fast incident monitor cron fires. Should write 15 rows (3 regions × 5 methods).
3. **After closeout** — Re-evaluate 4-day rolling. Confirm V73 ≥ OFFICIAL.
4. Check `journalctl -u lottery -n 100 | grep V77` for both jobs.

## P0 (escalate immediately if MB stays cold ≥7 days)

1. **Regime-shift / Markov detection** — root-cause investigation for MB if OFFICIAL stays 0 for 7+ more days.
2. Forensic: which model class is suddenly weak in MB? AI vs NO_TOKEN? Single weekday or all?
3. Possible mitigation: weekday-specific model rotation in MB.

## P1 (next session)

1. Method interaction trace surface (CROWN/AURA fire log per region per day)
2. C-16 top-20 audit surface (snapshot daily strength rankings)
3. UI dashboard `/du-doan-test` with side-by-side method comparison + tier badges + Wilson CI
4. Per-station + per-weekday consensus when sample reaches 180d
5. Independent cluster consensus metric (count distinct method clusters, not just method count)

## P2 (after 30d data)

1. OFFICIAL_PROMOTION_DOSSIER.md draft (no implementation, owner gate)
2. `official_promotion_readiness_shadow` materializer
3. Region-specific candidate analysis
4. Lo3 / Xien 2-3 axis consensus extension
5. Replace fixed 19:00 cron with event-driven post-MB-runner trigger (P2-FU-77.4)

## P3 (owner-gate decisions)

1. NO_TOKEN local timing (low risk, but touches local ML wrappers)
2. Cohere wide-pool reactivation as anti-stale post-processor
3. Production AI cascade strength-ordering (HIGH risk; needs 14d shadow proof)

## Until next session

- Cron daily fires automatically.
- V77 jobs (19:00 + 19:05) join V66/V67/V70/V73/V76 (23:35-23:50).
- V76 drift alerts activate after 2026-05-21 (n30 ≥ 10 needed).
- V77 fast incident alerts activate immediately (4-day window).
- Owner can review V77_REPORT.md and decide if any P1 items are urgent.
