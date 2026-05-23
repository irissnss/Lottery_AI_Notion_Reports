# V106.05 Methodology

Source: live-synced DB after `artifacts/live_sync/20260523_223517/manifest.json`.

Target: MT D.
Source: MB board only, lag D-1/D-2/D-3.
Allowed source prizes: DB#1, G1#1, G2#1, G2#2.

Transforms tested: LAST2, LAST2_REV, FIRST2, FIRST2_REV, HEAD_TAIL, TAIL_HEAD, SUM_UNIT_PAIR, and exact digit-position transforms P{i}P{j}.

Metrics: hit rate against any MT prize, baseline-adjusted hit lift, DB-day hit rate, DB-day lift, station DB rate, and half-window stability.

Controls: broad selectors such as G3_ALL, LOW_ALL, TOP3_PRIZES, and ALL_PRIZES are excluded from boost conclusions. Scoped rules must match weekday/station-set.
