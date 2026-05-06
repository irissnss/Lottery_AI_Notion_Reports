import sqlite3, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DB = "data/lottery_ai.db"
DATE = "2026-05-06"
REGIONS = ["MN", "MT", "MB"]

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
cur = con.cursor()

print("=== 2026-05-06 official/test current state ===")
for region in REGIONS:
    print(f"\n--- {region} ---")
    for sql_name, sql in [
        ("predictions", "SELECT run_source, COUNT(*) n, GROUP_CONCAT(DISTINCT ai_model) models FROM predictions WHERE date=? AND target_region=? GROUP BY run_source"),
        ("final_bundles", "SELECT COUNT(*) n, GROUP_CONCAT(bach_thu) bt, GROUP_CONCAT(created_at) created FROM final_bundles WHERE date=? AND region=?"),
        ("lottery_results", "SELECT COUNT(*) n, GROUP_CONCAT(station) stations FROM lottery_results WHERE date=? AND region=?"),
        ("budget_daily", "SELECT COUNT(*) n, GROUP_CONCAT(selected_count) selected FROM du_doan_test_model_budget_daily WHERE run_date=? AND region=?"),
        ("test_runs", "SELECT COUNT(*) n, GROUP_CONCAT(DISTINCT experiment_name) exps FROM du_doan_test_runs WHERE run_date=? AND region=?"),
        ("test_bundles", "SELECT COUNT(*) n, GROUP_CONCAT(experiment_name || ':' || COALESCE(test_bt,'--')) picks FROM du_doan_test_bundles WHERE run_date=? AND region=?"),
        ("experimental_preview", "SELECT COUNT(*) n, GROUP_CONCAT(experiment_name || ':' || COALESCE(candidate_bt,'--')) picks FROM experimental_preview_shadow WHERE date=? AND region=?"),
    ]:
        try:
            rows = cur.execute(sql, (DATE, region)).fetchall()
            print(sql_name, [dict(r) for r in rows])
        except Exception as e:
            print(sql_name, "ERR", e)

print("\n=== scheduler logs 2026-05-06 relevant ===")
rows = cur.execute("""
    SELECT log_time, log_level, region, job_name, date_str, message
    FROM scheduler_logs
    WHERE log_time >= '2026-05-06'
      AND (job_name LIKE '%du_doan%' OR job_name LIKE '%shadow%' OR job_name LIKE '%ai_predict%' OR message LIKE '%DU-DOAN-TEST%' OR message LIKE '%C16%' OR message LIKE '%SHADOW_ORDER%')
    ORDER BY log_time
    LIMIT 200
""").fetchall()
for r in rows:
    msg = (r["message"] or "").replace("\n", " ")[:240]
    print(f"{r['log_time']} {r['log_level']} {r['region']} {r['job_name']} {r['date_str']} | {msg}")

print("\n=== latest final bundles ===")
for region in REGIONS:
    row = cur.execute("SELECT date, region, bach_thu, lo2, created_at, verified_at FROM final_bundles WHERE region=? ORDER BY date DESC LIMIT 1", (region,)).fetchone()
    print(region, dict(row) if row else None)

con.close()
