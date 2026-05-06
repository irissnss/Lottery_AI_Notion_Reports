# V54 Owner Next Action Plan

## Next 24h

- Let 2026-05-04 finish naturally.
- No more restarts before 20:00 eval jobs unless outage.
- After closeout, run V52.5.6 runner manually for `--region ALL --mode POST_CLOSEOUT_DIAGNOSTIC_FULL_25`.

## Next 3 Days

- Deploy C-05 per-model latency instrumentation outside live windows.
- Deploy C-07 MT correct-but-dropped UI panel.
- Deploy C-14 strength chips UI.
- Keep C-02 source labels live.

## Next 7 Days

- Extend closeout evaluator to MN/MT/MB (C-03).
- Consider scheduler auto-wire only after 3 clean manual closeouts.
- Surface C-15 blackspot panel in `/du-doan-test`.

## Next 14 Days

- Re-evaluate loz trace after 14 valid days.
- Decide whether any loz method becomes owner-review candidate. Current answer: no.

## Next 30 Days

- Review Wave 1 method candidates (MB Composite V2 / MB StrengthWeighted / MN AI_CHAIN) only if gates met.
- No production deploy without DECISION_LOG owner OK.

## Do Not Do

- Do not prune models before latency/cost data exists.
- Do not promote single-vote rescue.
- Do not change official loz policy.
- Do not claim 2026-05-04 before closeout.
