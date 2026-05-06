"""V52.5.8/V53 official quality rolling stats."""
import sqlite3
from pathlib import Path
import datetime as dt

conn = sqlite3.connect(Path('data/lottery_ai.db'))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

ANCHOR = '2026-05-03'

print('=== Rolling 7/14/30/60-day BT-only WR per region (final_bundles vs lottery_results) ===')
for region in ('MN', 'MT', 'MB'):
    print(f'\nRegion {region}')
    for days in (3, 7, 14, 30, 60):
        rows = cur.execute(
            """
            SELECT bach_thu_status, lo2_status, COUNT(*) AS n
            FROM final_bundles
            WHERE region=? AND date >= date(?, ?) AND date <= ?
              AND bach_thu_status IN ('WIN','LOSE','PARTIAL')
            GROUP BY bach_thu_status, lo2_status
            """,
            (region, ANCHOR, f'-{days-1} days', ANCHOR),
        ).fetchall()
        bt_w = 0
        bt_total = 0
        lo2_full_w = 0
        lo2_partial_w = 0
        lo2_total = 0
        for r in rows:
            bt_status = r['bach_thu_status'] or 'PENDING'
            lo2_status = r['lo2_status'] or 'PENDING'
            n = int(r['n'] or 0)
            if bt_status in ('WIN', 'LOSE', 'PARTIAL'):
                bt_total += n
                if bt_status == 'WIN':
                    bt_w += n
            if lo2_status in ('WIN', 'PARTIAL', 'LOSE'):
                lo2_total += n
                if lo2_status == 'WIN':
                    lo2_full_w += n
                elif lo2_status == 'PARTIAL':
                    lo2_partial_w += n
        bt_rate = round(bt_w / bt_total, 4) if bt_total else None
        lo2_full_rate = round(lo2_full_w / lo2_total, 4) if lo2_total else None
        lo2_any_rate = round((lo2_full_w + lo2_partial_w) / lo2_total, 4) if lo2_total else None
        print(f'  {days:>2}d  BT={bt_w}/{bt_total} ({bt_rate})  LO2_FULL={lo2_full_w}/{lo2_total} ({lo2_full_rate})  LO2_ANY(W+P)={lo2_full_w + lo2_partial_w}/{lo2_total} ({lo2_any_rate})')

print()
print('=== Per-weekday WR (window 30d) ===')
for region in ('MN', 'MT', 'MB'):
    print(f'\nRegion {region}')
    rows = cur.execute(
        """
        SELECT date, bach_thu_status, lo2_status FROM final_bundles
        WHERE region=? AND date >= date(?, '-29 days') AND date <= ?
          AND bach_thu_status IN ('WIN','LOSE','PARTIAL')
        """,
        (region, ANCHOR, ANCHOR),
    ).fetchall()
    weekday_buckets = {i: {'bt_w': 0, 'bt_total': 0, 'lo2_w': 0, 'lo2_p': 0, 'lo2_total': 0} for i in range(7)}
    for r in rows:
        wd = dt.date.fromisoformat(r['date']).weekday()
        b = weekday_buckets[wd]
        b['bt_total'] += 1
        if r['bach_thu_status'] == 'WIN':
            b['bt_w'] += 1
        b['lo2_total'] += 1
        if r['lo2_status'] == 'WIN':
            b['lo2_w'] += 1
        elif r['lo2_status'] == 'PARTIAL':
            b['lo2_p'] += 1
    days_name = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for wd, b in weekday_buckets.items():
        if b['bt_total']:
            print(f'  {days_name[wd]}: BT {b["bt_w"]}/{b["bt_total"]}, LO2_full {b["lo2_w"]}/{b["lo2_total"]}, LO2_any {b["lo2_w"]+b["lo2_p"]}/{b["lo2_total"]}')

print()
print('=== Last 5 closeouts each region ===')
for region in ('MN', 'MT', 'MB'):
    print(f'\nRegion {region}')
    rows = cur.execute(
        """
        SELECT date, bach_thu, bach_thu_status, lo2, lo2_status
        FROM final_bundles WHERE region=? ORDER BY date DESC LIMIT 5
        """,
        (region,),
    ).fetchall()
    for r in rows:
        print(' ', dict(r))

conn.close()
