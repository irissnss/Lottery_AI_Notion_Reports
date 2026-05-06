#!/bin/bash
set -e
cd /root/Lottery_AI_Test
/root/Lottery_AI_Test/venv/bin/python3 -m py_compile web/backend/_materialize_loz_stage_trace_shadow.py
/root/Lottery_AI_Test/venv/bin/python3 web/backend/_materialize_loz_stage_trace_shadow.py \
  --backfill-days 60 --anchor-date 2026-05-03 --json \
  > artifacts/_v54_loz_stage_trace_backfill_20260504.json
/root/Lottery_AI_Test/venv/bin/python3 - <<'PY'
import json
import sqlite3

with open('artifacts/_v54_loz_stage_trace_backfill_20260504.json', encoding='utf-8') as f:
    data = json.load(f)
print('processed', len(data.get('results', [])), 'date-region jobs')

conn = sqlite3.connect('data/lottery_ai.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
for row in cur.execute(
    "SELECT region, drop_stage, COUNT(*) AS n "
    "FROM loz_stage_trace_shadow "
    "GROUP BY region, drop_stage ORDER BY region, n DESC"
):
    print(dict(row))
conn.close()
PY
