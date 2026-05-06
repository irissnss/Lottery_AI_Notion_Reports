"""V52.5.2 inspection: show MN/MT/MB experimental_preview rows for 2026-05-03."""
import sqlite3
import json
from pathlib import Path

conn = sqlite3.connect(Path('data/lottery_ai.db'))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

for region in ('MN', 'MT', 'MB'):
    print(f'=== {region} 2026-05-03 ===')
    rows = cur.execute(
        """
        SELECT experiment_name, candidate_bt, baseline_bt, baseline_bt_status,
               actual_known, candidate_bt_hit, candidate_lo2_status,
               would_flip_baseline_to_win, would_flip_baseline_to_lose,
               selection_basis
        FROM experimental_preview_shadow
        WHERE date='2026-05-03' AND region=?
        ORDER BY id
        """,
        (region,),
    ).fetchall()
    for r in rows:
        d = dict(r)
        d['selection_basis'] = (d['selection_basis'] or '')[:120]
        print(' ', d)
    print()

print('Counts by region/date:')
for r in cur.execute(
    "SELECT date, region, COUNT(*) AS n FROM experimental_preview_shadow "
    "GROUP BY date, region ORDER BY date, region"
):
    print(' ', dict(r))
conn.close()
