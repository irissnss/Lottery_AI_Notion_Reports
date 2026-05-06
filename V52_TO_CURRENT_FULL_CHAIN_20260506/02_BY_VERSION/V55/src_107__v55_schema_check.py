import sqlite3
c = sqlite3.connect('data/lottery_ai.db')
cu = c.cursor()
target = ['predictions', 'lottery_results', 'final_bundles',
          'du_doan_test_runs', 'du_doan_test_bundles', 'du_doan_test_results',
          'du_doan_test_candidates', 'du_doan_test_model_contribution',
          'du_doan_test_audit_log',
          'experimental_preview_shadow', 'mb_experimental_preview_shadow',
          'loz_stage_trace_shadow', 'weekday_blackspot_shadow',
          'mt_model_hit_output_drop_shadow',
          'model_strength_by_region_weekday_station_daily',
          'model_latency_cost_audit_daily',
          'scheduler_logs']
for t in target:
    try:
        cols = [r[1] for r in cu.execute(f"PRAGMA table_info({t})").fetchall()]
        print(f"{t}: {cols}")
    except Exception as e:
        print(f"{t}: ERR {e}")
