"""V52.5.1 strength tensor inspection helper (read-only)."""
import sqlite3
from pathlib import Path

DB = Path('data/lottery_ai.db')
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def show(family: str) -> None:
    print(f'--- {family} top-5 helpful_signal_strength per region (window=30, grain=region) ---')
    for region in ('MN', 'MT', 'MB'):
        print(f'region {region}')
        rows = cur.execute(
            """
            SELECT model_name, run_source, predictions_count, bt_hit_count,
                   loz1_rate, loz2_rate, helpful_signal_strength
            FROM model_strength_by_region_weekday_station_daily
            WHERE grain='region' AND model_family=? AND window_days=30 AND region=?
            ORDER BY helpful_signal_strength DESC NULLS LAST
            LIMIT 5
            """,
            (family, region),
        ).fetchall()
        for r in rows:
            print(' ', dict(r))


show('TOKEN')
show('NO_TOKEN')
show('SHADOW')

print('--- Counts by grain/window ---')
for r in cur.execute(
    "SELECT grain, window_days, COUNT(*) AS n FROM model_strength_by_region_weekday_station_daily "
    "GROUP BY grain, window_days ORDER BY grain, window_days"
):
    print(dict(r))

conn.close()
