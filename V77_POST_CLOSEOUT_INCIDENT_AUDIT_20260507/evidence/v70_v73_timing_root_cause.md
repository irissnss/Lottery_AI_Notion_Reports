# V70/V73 Timing Bug — Root Cause Analysis

## What the audit revealed

V70 CONSENSUS and V73 HYBRID rely on `experimental_preview_shadow` rows written by other test methods (C16 BUDGET, AI_CHAIN, SPECIALIST, NO_TOKEN_HERD, STRENGTH_WEIGHTED, PRIOR_REGION, OFFICIAL_BASELINE_CONTROL).

The cron schedule was:

| Time (VN) | Job |
| --------- | --- |
| 23:35 | V66 lag-1 signal materializer |
| 23:40 | V67 ADAPTIVE_EXPLOIT_V1 (writes EXPLOIT row for tomorrow) |
| 23:45 | V70 CONSENSUS_V1 (reads pool for today + tomorrow) |
| 23:48 | V73 HYBRID_V1 (reads pool for today + tomorrow) |
| 23:50 | V76 drift monitor |

But the daily `/du-doan-test` runner (which writes C16, AI_CHAIN, SPECIALIST, NO_TOKEN_HERD, STRENGTH_WEIGHTED, PRIOR, OFFICIAL_BASELINE picks) is dynamic — driven by readiness:

| Region | Test runner approximate time |
| ------ | ---------------------------- |
| MN | ~04:30 VN (after MN cascade ~04:15) |
| MT | ~16:45 VN (after MT cascade ~16:42) |
| MB | ~17:45 VN (after MB cascade ~17:42) |

## The mismatch

V70 cron at 23:45 VN of day D fires for `target_date = D` and `target_date = D+1`:

- For `D+1`: only V67 EXPLOIT has written → `agreement_count = 1` → no consensus emitted.
- For `D`: ALL methods should be written by then (last write at 17:45 VN) → consensus should work.

**But the actual write timestamp `2026-05-07T01:50:31+07:00` shows V70 ran at 01:50 VN of 2026-05-07, NOT 23:45 VN of 2026-05-06.** This is a 1h45min cron delay (likely systemd boot / scheduler startup catch-up).

By 01:50 VN of D+1:

- For `target_date = D+1`: only V67 EXPLOIT written (cron 23:40 fired at 01:23) → agreement_count=1 → no row.
- For `target_date = D` (i.e., yesterday): NOT in cron loop (V70 cron for "today + tomorrow" interpretation depends on system clock).

Result: V70 had **zero useful rows** in `experimental_preview_shadow` for V73 to consume.

## Backfill proof of the fix

Re-running V70 with the FULL pool (after all method picks landed):

| Date | Region | Old V70 agreement | New V70 agreement | Old V70 BT | New V70 BT | Hit? |
| ---- | ------ | ----------------- | ----------------- | ---------- | ---------- | ---- |
| 2026-05-04 | MN | n/a (no row) | 3 | — | 65 | ❌ |
| 2026-05-04 | MT | n/a | 3 | — | 82 | ✅ |
| 2026-05-04 | MB | n/a | 3 | — | 09 | ❌ |
| 2026-05-05 | MN | n/a | 3 | — | 15 | ❌ |
| 2026-05-05 | MT | n/a | 3 | — | 44 | ✅ |
| 2026-05-05 | MB | n/a | 5 | — | 41 | ❌ |
| 2026-05-06 | MN | n/a | 6 | — | 95 | ❌ |
| 2026-05-06 | MT | n/a | 5 | — | 71 | ✅ |
| 2026-05-06 | MB | n/a | 4 | — | 32 | ❌ |
| 2026-05-07 | MN | 1 | 5 | 95 | 94 | ❌ |
| 2026-05-07 | MT | 1 | 3 | 95 | **88** | ✅ |
| 2026-05-07 | MB | 1 | 4 | 79 | 20 | ❌ |

→ When V70 has the proper pool, agreement counts shoot from 1 → 3-6, and MT becomes 4/4 over 4 days.

## V73 today's miss explained

For MT on 2026-05-07, the FULL pool was:

| Method | Pick |
| ------ | ---- |
| C16 BUDGET | 88 ✅ |
| OFFICIAL CONTROL | 88 ✅ |
| STRENGTH_WEIGHTED | 69 |
| AI_CHAIN | 69 |
| SPECIALIST_ROSTER | 88 ✅ |
| NO_TOKEN_HERD | 88 ✅ |
| PRIOR_REGION_CONTEXT | 97 |
| V67 EXPLOIT | 95 |

Vote tally: **88 = 5 votes ✅**, 69 = 2 votes, 97 = 1 vote, 95 = 1 vote.

→ Real consensus for MT today = **88 ✅** with `agreement_count = 5` ≥ 3 gate.

V73 priority for MT = `consensus, exploit, budget`. With consensus=88 available, V73 should pick 88 ✅.

But because V70 ran early at 01:50 VN with only V67 in the pool, V70 emitted no row. V73 then fell to V67=95 ❌.

**This is a TIMING REGRESSION on the upstream input, NOT a flaw in V73's region priority.**

## V77 fix

Add a SECOND cron at 19:00 VN that re-runs V70 + V73 for `target_date=today` AFTER all 3 region runners (latest = MB at 17:45) have completed. Original 23:45/23:48 cron retained for `target_date=tomorrow` prep.

```python
def _run_v77_post_cascade_rerun():
    today = _dt.now(VN_TZ).strftime("%Y-%m-%d")
    for _r in ("MN", "MT", "MB"):
        _mat_v70(today, _r)
    for _r in ("MN", "MT", "MB"):
        _mat_v73(today, _r)

_scheduler.add_job(
    _run_v77_post_cascade_rerun,
    CronTrigger(hour=19, minute=0, timezone=VN_TZ),
    id="v77_post_cascade_rerun",
    ...)
```

## Why not event-driven (post-MB-runner hook)?

That's preferred long-term and is listed as P2-FU-77.4. For incident response we used a simple time-cron which fires safely after the latest known runner. Event-driven would tighten SLA but requires more code changes; we kept V77 minimal.
