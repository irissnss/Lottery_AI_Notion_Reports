"""Check /du-doan-test test lane and experimental preview shadow rows for 04/05 and 05/05."""
import sqlite3, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
c = sqlite3.connect('data/lottery_ai.db')
c.row_factory = sqlite3.Row
cu = c.cursor()

print("=== du_doan_test_runs counts ===")
for date in ['2026-05-03', '2026-05-04', '2026-05-05']:
    cu.execute("SELECT COUNT(*), GROUP_CONCAT(DISTINCT region) FROM du_doan_test_runs WHERE run_date=?", (date,))
    n, regs = cu.fetchone()
    print(f"  {date}: runs={n} regions={regs}")

print("\n=== du_doan_test_bundles for 04/05 + 05/05 ===")
for date in ['2026-05-04', '2026-05-05']:
    cu.execute("SELECT region, experiment_name, mode, test_bt, official_bt, test_lo2_json, official_lo2_json FROM du_doan_test_bundles WHERE run_date=? ORDER BY region, experiment_name", (date,))
    rows = cu.fetchall()
    print(f"\n  --- {date} ({len(rows)} rows) ---")
    for r in rows:
        print(f"    {r['region']} {r['experiment_name']:35s} mode={r['mode']:30s} test_bt={r['test_bt']} off_bt={r['official_bt']} test_lo2={r['test_lo2_json']}")

print("\n=== du_doan_test_results for 04/05 + 05/05 ===")
for date in ['2026-05-04', '2026-05-05']:
    cu.execute("SELECT region, COUNT(*) FROM du_doan_test_results WHERE run_date=? GROUP BY region", (date,))
    print(f"  {date}: {[(r[0],r[1]) for r in cu.fetchall()]}")

print("\n=== experimental_preview_shadow rows by date ===")
cu.execute("SELECT date, region, COUNT(*), SUM(CASE WHEN actual_known=1 THEN 1 ELSE 0 END) as resolved FROM experimental_preview_shadow WHERE date IN ('2026-05-03','2026-05-04','2026-05-05') GROUP BY date, region ORDER BY date, region")
for r in cu.fetchall():
    print(f"  {r[0]} {r[1]}: {r[2]} (actual_known={r[3]})")

print("\n=== experimental_preview_shadow BT comparison 04/05 + 05/05 ===")
for date in ['2026-05-04', '2026-05-05']:
    cu.execute("SELECT region, experiment_name, candidate_bt, baseline_bt, candidate_bt_hit, baseline_bt_status, would_flip_baseline_to_win, would_flip_baseline_to_lose, false_promotion FROM experimental_preview_shadow WHERE date=? ORDER BY region, experiment_name", (date,))
    rows = cu.fetchall()
    print(f"\n  --- {date} ({len(rows)} preview rows) ---")
    for r in rows:
        print(f"    {r['region']} {r['experiment_name']:35s} cand_bt={r['candidate_bt']} base_bt={r['baseline_bt']} hit={r['candidate_bt_hit']} flip_win={r['would_flip_baseline_to_win']} flip_lose={r['would_flip_baseline_to_lose']} fp={r['false_promotion']}")

print("\n=== mb_experimental_preview_shadow rows ===")
cu.execute("SELECT date, COUNT(*), SUM(actual_known), SUM(would_flip_baseline_to_win), SUM(would_flip_baseline_to_lose) FROM mb_experimental_preview_shadow WHERE date IN ('2026-05-03','2026-05-04','2026-05-05') GROUP BY date")
for r in cu.fetchall():
    print(f"  {r[0]}: total={r[1]} resolved={r[2]} flip_win={r[3]} flip_lose={r[4]}")

print("\n=== loz_stage_trace_shadow 04/05 + 05/05 ===")
for date in ['2026-05-04', '2026-05-05']:
    cu.execute("SELECT region, COUNT(*), SUM(in_top1) as t1, SUM(in_top2) as t2, SUM(in_top10) as t10, SUM(CASE WHEN drop_stage='LOZ_LINE_SELECTION_MISS' THEN 1 ELSE 0 END) as ls, SUM(CASE WHEN drop_stage='AI_SIGNAL_DROPPED' THEN 1 ELSE 0 END) as ad, SUM(CASE WHEN drop_stage='CANDIDATE_POOL_MISS' THEN 1 ELSE 0 END) as cm FROM loz_stage_trace_shadow WHERE date=? GROUP BY region", (date,))
    rows = cu.fetchall()
    print(f"  --- {date} ({sum(r[1] for r in rows)} actual tails traced) ---")
    for r in rows:
        print(f"    {r[0]}: n={r[1]} top1={r[2]} top2={r[3]} top10={r[4]} loz_select_miss={r[5]} ai_dropped={r[6]} cand_miss={r[7]}")

print("\n=== mt_model_hit_output_drop_shadow 04/05 + 05/05 ===")
for date in ['2026-05-04', '2026-05-05']:
    cu.execute("SELECT region, COUNT(*), SUM(ai_signal_dropped), SUM(no_token_signal_dropped), SUM(in_official_bt), SUM(in_official_loz1), SUM(in_official_loz2) FROM mt_model_hit_output_drop_shadow WHERE date=? GROUP BY region", (date,))
    rows = cu.fetchall()
    print(f"  --- {date} ({sum(r[1] for r in rows)} actual tails) ---")
    for r in rows:
        print(f"    {r[0]}: n={r[1]} ai_drop={r[2]} notoken_drop={r[3]} in_off_bt={r[4]} in_off_loz1={r[5]} in_off_loz2={r[6]}")

print("\n=== model_strength_by_region_weekday_station_daily latest anchor ===")
cu.execute("SELECT MAX(anchor_date) FROM model_strength_by_region_weekday_station_daily")
latest_anchor = cu.fetchone()[0]
print(f"  Latest anchor: {latest_anchor}")
cu.execute("SELECT region, model_family, run_source, COUNT(DISTINCT model_name) FROM model_strength_by_region_weekday_station_daily WHERE anchor_date=? AND grain='REGION' AND window_days=30 GROUP BY region, model_family, run_source ORDER BY region, model_family", (latest_anchor,))
for r in cu.fetchall():
    print(f"  {r[0]:3s} {r[1]:12s} {r[2]:30s} models={r[3]}")

print("\n=== model_latency_cost_audit_daily 04/05 + 05/05 ===")
cu.execute("SELECT date, region, COUNT(*), SUM(latency_available), SUM(CASE WHEN missing_reason='NO_PER_MODEL_DURATION' THEN 1 ELSE 0 END) FROM model_latency_cost_audit_daily WHERE date IN ('2026-05-04','2026-05-05') GROUP BY date, region")
for r in cu.fetchall():
    print(f"  {r[0]} {r[1]}: n={r[2]} latency_avail={r[3]} no_dur={r[4]}")

print("\n=== weekday_blackspot_shadow latest ===")
cu.execute("SELECT MAX(anchor_date) FROM weekday_blackspot_shadow")
ba = cu.fetchone()[0]
cu.execute("SELECT region, weekday_name, blackspot_label, total_days, bt_wins, bt_rate, lo2_full_rate, lo2_any_rate FROM weekday_blackspot_shadow WHERE anchor_date=? ORDER BY region, weekday", (ba,))
for r in cu.fetchall():
    print(f"  anchor={ba} {r[0]} {r[1]:10s} {r[2]:35s} n={r[3]} bt_win={r[4]} bt%={r[5]} lo2full%={r[6]} lo2any%={r[7]}")

print("\n=== scheduler_logs 04/05 + 05/05 markers ===")
cu.execute("SELECT date_str, region, job_name, COUNT(*) FROM scheduler_logs WHERE log_time >= '2026-05-04' GROUP BY date_str, region, job_name ORDER BY 1 DESC, 2, 3")
for r in cu.fetchall():
    print(f"  {r[0]} {r[1]} {r[2]:50s} {r[3]}")
