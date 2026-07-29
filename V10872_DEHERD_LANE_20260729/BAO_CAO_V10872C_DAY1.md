# V10872c — First live day after the changes, 29 July

Owner: *"Xong ngày live đầu tiên sau điền chỉnh em kiểm tra toàn diện dùm anh nha em"*

Source: paired live sync `artifacts/live_sync/20260729_195004/manifest.json`.

## Results

Miền Bắc, Bắc Ninh, special tail 83. Miền Nam, Cần Thơ 77, Sóc Trăng 65, Đồng Nai 20. Miền Trung,
Khánh Hòa 55, Đà Nẵng 40. Distinct tails on the board: 39 in the South, 32 in the Centre, 21 in the
North — the random baseline for a single number.

## Official: 1 of 3

| Region | Pick | Outcome | Models | Note |
|---|---|---|---|---|
| Miền Nam | `96` | **hit** | 15 / 15 | complete |
| Miền Trung | `15` | miss | 13 | `gpt-5.4` and `meta-learning` dropped by `max_voters_cap` top-13 |
| Miền Bắc | `00` | miss | 14 | `gpt-5-mini` dropped by `bt_gate bt<12` |

Both shortfalls are deliberate quality gates, not failures.

## De-herd lane, day 1: tie everywhere

| Region | Lane | Official | Outcome |
|---|---|---|---|
| Miền Nam | `96` | `96` | both hit |
| Miền Trung | `46` | `15` | both miss |
| Miền Bắc | `00` | `00` | both miss |

Zero wins, zero losses. The lane picked exactly what official picked in two regions and diverged
only in Miền Trung, where neither number landed. A neutral first day, which is unremarkable given
that the backfill showed the arms agree on most days and diverge on roughly half.

The cron fired precisely on schedule: 15:51 for the South, 17:00:01 for the Centre, 18:00:01 for
the North, all pre-draw.

Cumulative across 270 region-days: official 29.3%, lane 37.0%, wins 38, losses 17. Forward counter
now **1 of 21**, decision date 19 August.

## `/choi` hit in all three regions

| Region | Numbers | Result | Method used today |
|---|---|---|---|
| Miền Nam | `[96]` | hit | `MN_BT1_OFFICIAL_V1` |
| Miền Trung | `[20, 32]` | 32 hit | `MT_PRIOR_REGION_CONTEXT_SAFE_V1 + MT_AI_CHAIN` |
| Miền Bắc | `[00, 12]` | 12 hit | `MB_STRENGTH_WEIGHTED_V52_5_2` |

## The agent's play advice was wrong, and why

At 13:41 the recommendation was to play Miền Trung only and skip the other two. All three hit, so
that advice cost two winning days.

The cause is a real flaw in how the advice was built. `/choi` **switches method from day to day**,
but the recommendation used a 30-day average for the whole region. Miền Bắc today ran
`MB_STRENGTH_WEIGHTED_V52_5_2`, which has only 0 of 2 historically, not the
`MB_ADAPTIVE_EXPLOIT_V1` at 7 of 21 whose numbers were quoted. Different method, different odds.

What this does not change: one day cannot overturn a 30-day base rate, and Miền Bắc at 15.5% per
number against a 23% baseline remains a genuine warning.

What it does change: play advice has to read the method actually selected that day from
`method_label` in `v10861_choi_display_output` and look up that method's own record, instead of
averaging the region. Filed as `FU-V10872-CHOI-ADVICE-METHOD-LEVEL`.

## The three fixes, verified on live data

**`deepseek-reasoner`** returned numbers in all three regions — `[12,00]` North, `[00,63]` South,
`[32,20]` Centre — with no `finish_reason=length`. The `max_tokens` raise to 32,768 works.

**`grok-4.3`** returned `CHOT_HA` with numbers in all three regions — `[40,13]`, `[00]`, `[15,32]`
— with no contract void. Completing V10750 works.

**The two retired models** each show exactly one row today, at 04:31:50 and 04:33:20, both before
the roughly 12:00 deployment. The proof the cut is live: the South's shadow pass ran pre-deploy with
12 models while the Centre and North ran post-deploy with 10.

**The two premium models** produced zero rows, correct under `first_run_date` 2026-07-30.

## Sync incident, closed

The first sync attempt at 18:39 failed with a hash mismatch. Cause was the 18:30 Miền Bắc scrape
job writing to the database mid-copy, not corruption: two hashes taken six seconds apart matched
and `PRAGMA quick_check` returned ok. Re-synced successfully at 18:41, and again at 19:50 after the
settle wrote the scoreboard.

## Infrastructure

Service active, health 200, `/du-doan` 200, cross-module contract PASS with `last_bundle` at 29
July, journal errors 0, scheduler errors 0, official roster 15, shadow roster 12.

Evidence: `artifacts/v10872_day1/V10872_DAY1_2026-07-29.json`.
