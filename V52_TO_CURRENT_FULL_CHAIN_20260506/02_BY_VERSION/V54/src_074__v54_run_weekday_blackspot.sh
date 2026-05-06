#!/bin/bash
set -e
cd /root/Lottery_AI_Test
/root/Lottery_AI_Test/venv/bin/python3 -m py_compile web/backend/_materialize_weekday_blackspot_shadow.py
/root/Lottery_AI_Test/venv/bin/python3 web/backend/_materialize_weekday_blackspot_shadow.py \
  --anchor-date 2026-05-03 --window-days 30 --json \
  > artifacts/_v54_weekday_blackspot_20260504.json
/root/Lottery_AI_Test/venv/bin/python3 - <<'PY'
import sqlite3

conn = sqlite3.connect('data/lottery_ai.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
for row in cur.execute(
    "SELECT region, weekday_name, total_days, bt_wins, bt_rate, "
    "lo2_full_wins, lo2_full_rate, blackspot_label "
    "FROM weekday_blackspot_shadow "
    "WHERE anchor_date='2026-05-03' AND window_days=30 "
    "ORDER BY region, weekday"
):
    print(dict(row))
conn.close()
PY
