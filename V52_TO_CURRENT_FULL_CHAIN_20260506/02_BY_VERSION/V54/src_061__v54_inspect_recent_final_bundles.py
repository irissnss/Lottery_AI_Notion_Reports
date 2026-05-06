import json
import sqlite3

conn = sqlite3.connect("data/lottery_ai.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()
for row in cur.execute(
    """
    SELECT id, date, region, bach_thu, lo2, bach_thu_status, lo2_status,
           created_at, updated_at, verified_at, status, notes
    FROM final_bundles
    WHERE date >= '2026-05-03'
    ORDER BY date, region
    """
):
    print(json.dumps(dict(row), ensure_ascii=False, default=str))
conn.close()
