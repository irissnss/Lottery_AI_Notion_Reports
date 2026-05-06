import json
import sqlite3

conn = sqlite3.connect("data/lottery_ai.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

print("NOW DB AUDIT 2026-05-04")
for region in ("MN", "MT", "MB"):
    print("REGION", region)
    fb = cur.execute(
        """
        SELECT id,date,region,bach_thu,lo2,bach_thu_status,lo2_status,
               created_at,updated_at,verified_at,notes
        FROM final_bundles
        WHERE date=? AND region=?
        ORDER BY id DESC LIMIT 1
        """,
        ("2026-05-04", region),
    ).fetchone()
    print(" final_bundle", json.dumps(dict(fb), ensure_ascii=False, default=str) if fb else None)
    preds = cur.execute(
        "SELECT run_source, COUNT(*) n FROM predictions WHERE date=? AND target_region=? GROUP BY run_source",
        ("2026-05-04", region),
    ).fetchall()
    print(" predictions", [dict(x) for x in preds])
    res = cur.execute(
        "SELECT COUNT(*) n FROM lottery_results WHERE date=? AND region=?",
        ("2026-05-04", region),
    ).fetchone()["n"]
    print(" result_rows", res)
    mde = cur.execute(
        "SELECT COUNT(*) n FROM model_daily_eval WHERE date=? AND region=?",
        ("2026-05-04", region),
    ).fetchone()["n"]
    print(" mde_rows", mde)

print("recent scheduler markers")
for row in cur.execute(
    """
    SELECT timestamp, job_name, status, message
    FROM scheduler_logs
    WHERE timestamp >= '2026-05-04 16:00:00'
    ORDER BY id DESC LIMIT 30
    """
):
    print(json.dumps(dict(row), ensure_ascii=False, default=str))

conn.close()
