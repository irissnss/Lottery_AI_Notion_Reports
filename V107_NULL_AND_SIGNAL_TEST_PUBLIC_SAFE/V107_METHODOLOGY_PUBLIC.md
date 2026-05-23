# V107 Methodology

Locked live sync: `artifacts/live_sync/20260523_233622/manifest.json`.
DB: `data/lottery_ai.db` (live-synced from VPS).

## Null tests
- **1. Permutation**: shuffle target_date<->target_features within last 365 days, 500x, seed=20260524. Track best_lift across V107 panel of 498 rules.
- **2. Negative control**: 6 deterministic synthetic source features (random_00_99, moon_phase, lunar_day, day_of_year_tail, weekday_month_composite, sine_period_27). Compare best_lift to real panel.
- **3. Multiple-testing correction**: For each of 153228 V106.06 rules, compute exact binomial raw_p, then BH q within transform family + Bonferroni within family + Bonferroni full.
- **4. Sub-sample replication**: Split last 180 days into odd-DOY and even-DOY halves; compute lift on each half; count rules >= +15pp in BOTH halves. Compare to expected under independence.
- **5. Forward 90d audit**: V106.03/05/06 pre-registered rules + 30-day holdout proxy.

## Integrity families
- **A. Within-region positional autocorrelation**: LAST2 self-lag 1/7/14/28/30 days. Mean should be ~0 for clean RNG.
- **D. Reverse causality**: For top 20 V107 panel rules (forward X@d-k -> Y@d), evaluate reverse X@d+k -> Y@d. If forward >> reverse, predictive-like; if forward ~ reverse, contemporaneous.

Stopping criteria (per request):
- Permutation p_empirical > 0.20 -> STOP.
- Negative control synthetic >= real best -> STOP.
- Forward 90d aggregate p >= 0.5 -> STOP.

Lineage rule: every test uses `source_region:source_unit:source_prize#index:transform:lag`. No broad selectors (G3_ALL/LOW_ALL/TOP3/ALL_PRIZES).

Public-safe constraints: no DB, no jsonl, no log, no runtime artifact, no secrets.
