"""V52.5.8/V53 reality check: confirm where /du-doan-test numbers come from."""
import json
import sqlite3
from pathlib import Path

DB = Path('data/lottery_ai.db')
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

DATES = ('2026-05-02', '2026-05-03')

print('=== Final bundles (official) ===')
for date in DATES:
    for r in cur.execute(
        "SELECT date, region, bach_thu, bach_thu_status, lo2, lo2_status FROM final_bundles WHERE date=?",
        (date,),
    ):
        print(' ', dict(r))

print()
print('=== experimental_preview_shadow (V52.5.2 multi-region) ===')
for date in DATES:
    for r in cur.execute(
        """
        SELECT date, region, experiment_name, candidate_bt, baseline_bt,
               candidate_bt_hit, would_flip_baseline_to_win,
               would_flip_baseline_to_lose, false_promotion, selection_basis
        FROM experimental_preview_shadow WHERE date=?
        ORDER BY region, experiment_name
        """,
        (date,),
    ):
        d = dict(r)
        d['selection_basis'] = (d['selection_basis'] or '')[:80]
        print(' ', d)

print()
print('=== mb_experimental_preview_shadow (legacy MB-only) ===')
for date in DATES:
    for r in cur.execute(
        """
        SELECT date, region, experiment_name, candidate_bt, baseline_bt,
               candidate_bt_hit, would_flip_baseline_to_win,
               would_flip_baseline_to_lose, false_promotion
        FROM mb_experimental_preview_shadow WHERE date=?
        ORDER BY experiment_name
        """,
        (date,),
    ):
        print(' ', dict(r))

print()
print('=== du_doan_test_bundles latest ===')
for r in cur.execute(
    """
    SELECT run_date, region, experiment_name, mode,
           test_bt, official_bt
    FROM du_doan_test_bundles
    WHERE run_date IN ('2026-05-02','2026-05-03')
    ORDER BY run_date, region, experiment_name
    """,
):
    print(' ', dict(r))

print()
print('=== du_doan_test_results latest ===')
for r in cur.execute(
    """
    SELECT run_date, region, official_bt, official_bt_status, test_bt, test_bt_status,
           would_save, would_break, false_promotion
    FROM du_doan_test_results
    WHERE run_date='2026-05-03'
    ORDER BY region
    LIMIT 30
    """,
):
    print(' ', dict(r))

print()
print('=== Test runs by date and region (V52.5.x) ===')
for r in cur.execute(
    """
    SELECT run_date, region, mode, COUNT(*) AS n, MAX(run_label) AS sample_label,
           MIN(started_at) AS earliest, MAX(finished_at) AS latest
    FROM du_doan_test_runs
    GROUP BY run_date, region, mode
    ORDER BY run_date DESC, region
    LIMIT 25
    """,
):
    print(' ', dict(r))

conn.close()
