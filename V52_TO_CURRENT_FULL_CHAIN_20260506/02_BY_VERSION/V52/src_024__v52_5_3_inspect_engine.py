"""V52.5.3 multi-region engine inspection."""
import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path('data/lottery_ai.db'))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

print('=== Test runs by region (run_label LIKE V52.5.3 only) ===')
for r in cur.execute(
    """
    SELECT region, COUNT(*) AS n, COUNT(DISTINCT run_date) AS days
    FROM du_doan_test_runs
    WHERE run_label LIKE 'du_doan_test_engine_v52_5_3%'
    GROUP BY region
    """
):
    print(' ', dict(r))

print()
print('=== Test results flip stats (V52.5.3 runs, actual_known) ===')
for r in cur.execute(
    """
    SELECT b.region, b.experiment_name,
           COUNT(*) AS n,
           SUM(rs.would_save) AS save,
           SUM(rs.would_break) AS brk,
           SUM(rs.false_promotion) AS fp,
           SUM(CASE WHEN rs.test_bt_status='WIN' THEN 1 ELSE 0 END) AS test_wins,
           SUM(CASE WHEN rs.official_bt_status='WIN' THEN 1 ELSE 0 END) AS official_wins
    FROM du_doan_test_results rs
    JOIN du_doan_test_runs b ON rs.run_id=b.id
    WHERE b.run_label LIKE 'du_doan_test_engine_v52_5_3%'
    GROUP BY b.region, b.experiment_name
    ORDER BY b.region, save DESC
    """
):
    print(' ', dict(r))

print()
print('=== Test bundle examples for 2026-05-03 ===')
for r in cur.execute(
    """
    SELECT region, experiment_name, test_bt, official_bt, test_lo2_json
    FROM du_doan_test_bundles
    WHERE run_date='2026-05-03'
    ORDER BY region, experiment_name
    """
):
    print(' ', dict(r))

conn.close()
