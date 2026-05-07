# Open issues — as of V84 (2026-05-07)

## Resolved this session (V84)

1. Master Control Board built — 24 family rows reconciling V63 → V83.
2. 18-method P0 portfolio maturity matrix completed.
3. 14d region split flips computed (POTENTIAL_LIFT / PARITY / DESTRUCTIVE_BIAS verdict per method).
4. 60d evidence availability map per family.
5. Decision calendar 11 VN dates with pass/fail conditions.
6. Owner-gate queue 9 items with trigger dates.
7. Region master queues (MN/MT/MB).
8. D-1/D-2 subsumed; D-7 ambiguous resolved.
9. UI master board spec proposed (owner OK pending to build).

## Active automated triggers (no manual action required)

1. **2026-05-08**: 6-cron 19:00-19:14 VN natural proof (auto).
2. **2026-05-12**: 4 P0 methods reach 14d minimum (auto evaluate).
3. **2026-05-14**: V79/V80/V81 7d rolling + MB cold-streak escalation gate.
4. **2026-05-21**: 14d full review + MN dossier draft + drift V76 active.
5. **2026-06-06**: 30d full sweep.
6. **2026-07-06**: 60d full V79/V80/V81.

## Owner-gate queue (9 items, see V84 evidence)

1. MN_TEST_LANE_VOTER_PROPOSAL dossier (2026-05-21).
2. Provider invoice update (anytime).
3. MB regime forensic deep dive (auto-trigger 2026-05-14).
4. GPT-5-mini API key validation (anytime).
5. V82 monitor UI feedback (anytime).
6. Selector promotion (60d gate + dossier).
7. Official prompt change (LOCKED).
8. Production model swap (LOCKED).
9. Global NO_TOKEN floor change (LOCKED).

## Owner-locked

- Selector promotion (any).
- Official prompt change.
- Production model swap.
- Global NO_TOKEN floor change.
- UI Master Board build (proposal only).
