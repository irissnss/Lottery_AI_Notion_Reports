# V106.03 Methodology

Source data: live-synced `data/lottery_ai.db` after `artifacts/live_sync/20260521_220205/manifest.json`.

Extraction rule:

1. Read MB `Giai nhi` for source date.
2. Take both values, e.g. `54197`, `29265`.
3. Convert to tails, e.g. `97`, `65`.
4. For each MN target date D, compare source dates D-1, D-2, D-3.
5. Measure any MN prize hit, per-candidate hit rate, any DB day hit, station DB hit rate, and lift over baseline.

Baseline note: with two source tails, any-day probability must be baseline-adjusted because raw any-day naturally rises when source candidates increase from one to two.
