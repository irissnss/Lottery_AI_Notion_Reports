"""V52.5.2 VPS inspection: counts and flip stats."""
import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path('data/lottery_ai.db'))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

print('=== Total rows by region ===')
for r in cur.execute(
    "SELECT region, COUNT(*) AS n, COUNT(DISTINCT date) AS d FROM experimental_preview_shadow GROUP BY region"
):
    print(' ', dict(r))

print()
print('=== Last 5 dates per region ===')
for region in ('MN', 'MT', 'MB'):
    rows = cur.execute(
        "SELECT date, COUNT(*) AS n FROM experimental_preview_shadow WHERE region=? GROUP BY date ORDER BY date DESC LIMIT 5",
        (region,),
    ).fetchall()
    for r in rows:
        print(' ', region, dict(r))

print()
print('=== Flip stats (actual_known=1 only) ===')
for r in cur.execute(
    """
    SELECT region, experiment_name,
           SUM(would_flip_baseline_to_win) AS fw,
           SUM(would_flip_baseline_to_lose) AS fl,
           SUM(false_promotion) AS fp,
           SUM(actual_known) AS ak,
           SUM(CASE WHEN candidate_bt_hit=1 THEN 1 ELSE 0 END) AS hits,
           COUNT(*) AS n
    FROM experimental_preview_shadow
    GROUP BY region, experiment_name
    ORDER BY region, fw DESC, hits DESC
    """
):
    print(' ', dict(r))

conn.close()
