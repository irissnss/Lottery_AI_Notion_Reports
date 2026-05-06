import json
import sqlite3
from pathlib import Path

DB = Path("data/lottery_ai.db")
ANCHOR = "2026-05-04"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def q(sql, params=()):
    return [dict(r) for r in cur.execute(sql, params).fetchall()]

out = {
    "date": ANCHOR,
    "official": {},
    "test_methods": {},
    "rolling": {},
    "measurement_counts": {},
    "loz_trace": {},
    "blackspots": [],
    "latency": {},
}

for region in ("MN", "MT", "MB"):
    fb = cur.execute(
        "SELECT date,region,bach_thu,bach_thu_status,lo2,lo2_status,created_at,updated_at,verified_at,notes FROM final_bundles WHERE date=? AND region=? ORDER BY id DESC LIMIT 1",
        (ANCHOR, region),
    ).fetchone()
    out["official"][region] = dict(fb) if fb else None
    out["test_methods"][region] = q(
        """
        SELECT b.experiment_name, b.test_bt, b.official_bt,
               r.test_bt_status, r.official_bt_status, r.would_save,
               r.would_break, r.false_promotion, b.mode
        FROM du_doan_test_bundles b
        LEFT JOIN du_doan_test_results r ON r.run_id=b.run_id
        WHERE b.run_date=? AND b.region=?
        ORDER BY b.experiment_name, b.id DESC
        """,
        (ANCHOR, region),
    )
    out["rolling"][region] = {}
    for days in (7, 14, 30, 60):
        rows = q(
            """
            SELECT bach_thu_status, lo2_status, COUNT(*) n
            FROM final_bundles
            WHERE region=? AND date >= date(?, ?) AND date <= ?
              AND bach_thu_status IN ('WIN','LOSE','PARTIAL')
            GROUP BY bach_thu_status, lo2_status
            """,
            (region, ANCHOR, f"-{days-1} days", ANCHOR),
        )
        bt_total = sum(r["n"] for r in rows)
        bt_win = sum(r["n"] for r in rows if r["bach_thu_status"] == "WIN")
        lo2_total = sum(r["n"] for r in rows if r["lo2_status"] in ("WIN", "PARTIAL", "LOSE"))
        lo2_full = sum(r["n"] for r in rows if r["lo2_status"] == "WIN")
        lo2_any = sum(r["n"] for r in rows if r["lo2_status"] in ("WIN", "PARTIAL"))
        out["rolling"][region][str(days)] = {
            "bt": [bt_win, bt_total],
            "bt_rate": round(bt_win / bt_total, 4) if bt_total else None,
            "lo2_full": [lo2_full, lo2_total],
            "lo2_full_rate": round(lo2_full / lo2_total, 4) if lo2_total else None,
            "lo2_any": [lo2_any, lo2_total],
            "lo2_any_rate": round(lo2_any / lo2_total, 4) if lo2_total else None,
        }

for table in [
    "mt_model_hit_output_drop_shadow",
    "loz_selector_shadow",
    "model_latency_cost_audit_daily",
    "model_strength_by_region_weekday_station_daily",
    "experimental_preview_shadow",
    "du_doan_test_runs",
    "du_doan_test_bundles",
    "du_doan_test_results",
    "loz_stage_trace_shadow",
    "weekday_blackspot_shadow",
]:
    exists = cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone()
    out["measurement_counts"][table] = cur.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0] if exists else 0

out["loz_trace"]["by_region_stage"] = q(
    "SELECT region, drop_stage, COUNT(*) n FROM loz_stage_trace_shadow GROUP BY region, drop_stage ORDER BY region, n DESC"
)
out["blackspots"] = q(
    """
    SELECT region, weekday_name, total_days, bt_wins, bt_rate,
           lo2_full_wins, lo2_full_rate, blackspot_label
    FROM weekday_blackspot_shadow
    WHERE anchor_date='2026-05-03' AND window_days=30
      AND blackspot_label IN ('WEEKDAY_BLACK_SPOT_CONFIRMED','WEEKDAY_STRUCTURAL_RISK')
    ORDER BY region, weekday
    """
)
out["latency"]["rollup"] = q(
    """
    SELECT missing_reason, COUNT(*) rows_count,
           SUM(latency_available) latency_available_rows,
           SUM(CASE WHEN cost_estimate IS NOT NULL THEN 1 ELSE 0 END) cost_available_rows
    FROM model_latency_cost_audit_daily
    GROUP BY missing_reason
    ORDER BY rows_count DESC
    """
)

print(json.dumps(out, ensure_ascii=False, indent=2, default=str))
conn.close()
