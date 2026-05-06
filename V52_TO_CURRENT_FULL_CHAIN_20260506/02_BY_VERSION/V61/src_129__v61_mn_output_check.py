import sqlite3, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
con = sqlite3.connect("data/lottery_ai.db")
con.row_factory = sqlite3.Row
cur = con.cursor()
date = "2026-05-06"
region = "MN"
print("=== MN 2026-05-06 /du-doan-test bundles ===")
rows = cur.execute("""
SELECT b.experiment_name, b.test_bt, b.official_bt, b.test_lo2_json, b.official_lo2_json,
       r.test_bt_status, r.test_lo2_status, r.would_save, r.would_break
FROM du_doan_test_bundles b
LEFT JOIN du_doan_test_results r ON r.run_id=b.run_id
WHERE b.run_date=? AND b.region=?
ORDER BY
  CASE WHEN b.experiment_name LIKE '%ADAPTIVE_BUDGET%' THEN 0
       WHEN b.experiment_name LIKE '%OFFICIAL_BASELINE%' THEN 1
       ELSE 2 END,
  b.experiment_name
""", (date, region)).fetchall()
for r in rows:
    print(dict(r))
print("\n=== C16 budget ===")
rows = cur.execute("""
SELECT total_pool_count, measured_pool_count, selected_count, watch_count, skipped_count, station_set_json
FROM du_doan_test_model_budget_daily
WHERE run_date=? AND region=? ORDER BY id DESC LIMIT 1
""", (date, region)).fetchall()
for r in rows:
    d = dict(r)
    try: d["station_set"] = json.loads(d.pop("station_set_json"))
    except Exception: pass
    print(d)
con.close()
