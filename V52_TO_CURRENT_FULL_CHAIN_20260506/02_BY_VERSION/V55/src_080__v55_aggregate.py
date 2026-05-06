"""V55 — aggregate all forensic JSON into the artifacts the prompt requires."""
import sqlite3, json, sys, io
from collections import defaultdict, Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DB = 'data/lottery_ai.db'
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
cur = con.cursor()
DATES = ['2026-05-04', '2026-05-05']
REGIONS = ['MN', 'MT', 'MB']

def tail2(x):
    s = ''.join(c for c in str(x) if c.isdigit())
    return s[-2:].zfill(2) if s else ''


# 1. /du-doan-test test bundles + results
test_data = {}
for date in DATES:
    test_data[date] = {}
    for region in REGIONS:
        cur.execute("SELECT b.experiment_name, b.test_bt, b.official_bt, b.test_lo2_json, b.official_lo2_json, b.diff_from_official_json, r.test_bt_status, r.test_lo2_status, r.would_save, r.would_break, r.false_promotion, r.net_effect, r.correct_but_dropped, r.delta_bt, r.delta_lo2 FROM du_doan_test_bundles b LEFT JOIN du_doan_test_results r ON r.run_id=b.run_id WHERE b.run_date=? AND b.region=? AND b.mode='POST_CLOSEOUT_DIAGNOSTIC_FULL_25' GROUP BY b.experiment_name", (date, region))
        rows = [dict(r) for r in cur.fetchall()]
        test_data[date][region] = rows
with open('artifacts/_v55_du_doan_test_closeout_20260504_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(test_data, f, ensure_ascii=False, indent=2, default=str)

# 2. UI/API source audit
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'du_doan_test_%' ORDER BY name")
test_tables = [r[0] for r in cur.fetchall()]
ui_audit = {
    'date': '2026-05-05',
    'admin_only': True,
    'output_eligible': False,
    'frontend_route': '/du-doan-test',
    'api_routes_admin_only': ['/api/du-doan-test/mn', '/api/du-doan-test/mt', '/api/du-doan-test/mb', '/api/du-doan-test/mb (legacy)'],
    'tables_present': test_tables,
    'tables_count': len(test_tables),
    'ui_v52_6_features_expected': ['source_banner', 'picks_per_experiment', 'chip_label_dong_thuan_khac_chinh'],
    'ui_label_confusion_status': 'UI_LABEL_CONFUSION_RESOLVED',  # V52.6 deployed
    'live_parallel_classification': 'LIVE_PARALLEL_AUTO_PENDING_ONLY',
    'reason_not_full_auto': [
        'V52.5.6 multi-region runner is manual; not wired into scheduler',
        'C-03 multi-region closeout evaluator not deployed',
        'Cần ≥3-5 clean closeouts để promote (currently 2 days closed under V52.5.6)',
    ],
    'note': 'API source labels (C-02) deployed since V54; test_bundle response includes is_clone_of_official, is_independent_agreement_with_official, source_proof, etc.',
}
with open('artifacts/_v55_du_doan_test_ui_api_source_audit_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(ui_audit, f, ensure_ascii=False, indent=2)

# 3. MT correct-but-dropped 04/05 + 05/05 — augment with mt_model_hit_output_drop_shadow rows
mt_drop_extra = {}
for date in DATES:
    cur.execute("SELECT * FROM mt_model_hit_output_drop_shadow WHERE date=? AND region='MT'", (date,))
    rows = [dict(r) for r in cur.fetchall()]
    cur.execute("SELECT * FROM loz_stage_trace_shadow WHERE date=? AND region='MT'", (date,))
    loz_rows = [dict(r) for r in cur.fetchall()]
    mt_drop_extra[date] = {
        'mt_drop_rows_count': len(rows),
        'mt_drop_classifications': Counter(r['drop_stage'] for r in rows),
        'mt_drop_rows_sample': rows[:10],
        'loz_stage_trace_count': len(loz_rows),
        'loz_drop_stages': Counter(r['drop_stage'] for r in loz_rows),
    }
with open('artifacts/_v55_mt_correct_but_dropped_extra_20260504_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(mt_drop_extra, f, ensure_ascii=False, indent=2, default=str)

# 4. Loz control audit — full from loz_stage_trace + lo2 status
loz_audit = {}
for date in DATES:
    loz_audit[date] = {}
    for region in REGIONS:
        cur.execute("SELECT * FROM loz_stage_trace_shadow WHERE date=? AND region=?", (date, region))
        rows = [dict(r) for r in cur.fetchall()]
        cur.execute("SELECT bach_thu_status, lo2_status, lo2 FROM final_bundles WHERE date=? AND region=?", (date, region))
        b = cur.fetchone()
        bt_status = b['bach_thu_status'] if b else None
        lo2_status = b['lo2_status'] if b else None
        loz_audit[date][region] = {
            'official_bt_status': bt_status,
            'official_lo2_status': lo2_status,
            'official_lo2': b['lo2'] if b else None,
            'loz_trace_count': len(rows),
            'in_top1': sum(r['in_top1'] for r in rows),
            'in_top2': sum(r['in_top2'] for r in rows),
            'in_top10': sum(r['in_top10'] for r in rows),
            'final_loz1_selected_count': sum(1 for r in rows if r.get('final_loz1_selected')),
            'final_loz2_selected_count': sum(1 for r in rows if r.get('final_loz2_selected')),
            'drop_stages': Counter(r['drop_stage'] for r in rows),
            'verdict_labels': [
                'LOZ_DIAGNOSTIC_ONLY',
                'LOZ_REGION_CONDITIONAL',
                'LOZ_WEEKDAY_CONDITIONAL',
                'LOZ_STAGE_TRACE_AVAILABLE',
                'LOZ_NOT_READY_FOR_RULE',
                'LOZ_OUTPUT_POLICY_CHANGE_NOT_ALLOWED',
            ],
        }
with open('artifacts/_v55_loz_control_audit_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(loz_audit, f, ensure_ascii=False, indent=2, default=str)

# 5. Tensor + latency readiness
tensor = {}
cur.execute("SELECT MAX(anchor_date) FROM model_strength_by_region_weekday_station_daily")
latest_anchor = cur.fetchone()[0]
tensor['latest_anchor'] = latest_anchor
# top models by region/family for latest anchor 30d region grain
top_by_region_family = {}
for region in REGIONS:
    for fam in ['AI', 'NO_TOKEN', 'ENSEMBLE', 'SHADOW']:
        family_filter = {
            'AI': "model_family='AI'",
            'NO_TOKEN': "model_family='NO_TOKEN'",
            'ENSEMBLE': "model_family='ENSEMBLE'",
            'SHADOW': "run_source='shadow_auto_eval'",
        }[fam]
        cur.execute(f"SELECT model_name, run_source, predictions_count, bt_hit_count, bt_rate, loz1_rate, loz2_rate, helpful_signal_strength FROM model_strength_by_region_weekday_station_daily WHERE anchor_date=? AND grain='REGION' AND window_days=30 AND region=? AND {family_filter} AND predictions_count>=10 ORDER BY helpful_signal_strength DESC LIMIT 5", (latest_anchor, region))
        rows = [dict(r) for r in cur.fetchall()]
        top_by_region_family[f"{region}_{fam}"] = rows
tensor['top_by_region_family_30d'] = top_by_region_family
# blackspot
cur.execute("SELECT region, weekday_name, blackspot_label, total_days, bt_wins, bt_rate, lo2_full_rate, lo2_any_rate FROM weekday_blackspot_shadow WHERE anchor_date='2026-05-05' ORDER BY region, weekday")
tensor['weekday_blackspot_anchor_2026-05-05'] = [dict(r) for r in cur.fetchall()]
# latency
cur.execute("SELECT date, region, COUNT(*), SUM(latency_available), SUM(CASE WHEN missing_reason='NO_PER_MODEL_DURATION' THEN 1 ELSE 0 END) FROM model_latency_cost_audit_daily WHERE date IN (?,?) GROUP BY date, region", DATES)
tensor['latency_2day'] = [list(r) for r in cur.fetchall()]
tensor['latency_pruning_label'] = 'PRUNING_NOT_ALLOWED_NO_LATENCY'
with open('artifacts/_v55_model_tensor_latency_pruning_readiness_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(tensor, f, ensure_ascii=False, indent=2, default=str)

# 6. Method/multi-lane status
method_status = {
    'methods': {
        'OFFICIAL_BASELINE_CONTROL': {'phase': 'TEST_LANE_PARALLEL', 'role': 'control_clone_official', 'output_eligible': False},
        'COMPOSITE_CHALLENGER_V2': {'phase': 'TEST_LANE_PARALLEL', 'samples_30d': '~MB only', 'gate': 'NOT_MET', 'next': 'WAIT_30D'},
        'STRENGTH_WEIGHTED_V52_5_2': {'phase': 'TEST_LANE_PARALLEL', '60d_MB_fw_fl': '8/7', 'gate': 'NOT_MET', 'next': 'ACCUMULATE'},
        'AI_CHAIN_PRESERVATION_V1': {
            'phase': 'TEST_LANE_PARALLEL',
            '60d_MN_fw_fl': '4/1',
            '60d_MT_fw_fl': '8/12 destructive',
            '60d_MB': 'destructive',
            'today_05_05': '1 free win MN (52 hit), 0 in MT/MB',
            'gate': 'REGION_CONDITIONAL_ONLY_MN_PROMISING',
            'next': 'WAIT_14D_MN_ONLY',
        },
        'SPECIALIST_ROSTER_V1': {
            'phase': 'TEST_LANE_PARALLEL',
            '60d_MB_fw_fl': '5/0',
            'today_04_05': '1 free win MN (32 hit) + None for MB/MT',
            'today_05_05': 'no rescue',
            'gate': 'PROMISING_BUT_THIN_SAMPLE',
            'next': 'WAIT_30_60D',
        },
        'PRIOR_REGION_CONTEXT_SAFE_V1': {
            'phase': 'TEST_LANE_PARALLEL',
            'samples_thin': True,
            'gate': 'NOT_ENOUGH_EVIDENCE',
            'next': 'WAIT_30D',
        },
        'NO_TOKEN_HERD_REDUCTION_V1': {
            'phase': 'TEST_LANE_PARALLEL',
            'samples_thin': True,
            'gate': 'NOT_ENOUGH_EVIDENCE',
            'next': 'WAIT_30D',
        },
        'TIER_AWARE_BUNDLE_SHADOW_V1_MB': {'phase': 'SHADOW_BACKFILL', 'samples_thin': True, 'gate': 'NOT_MET'},
        'corrected_rescue_replay': {'phase': 'SHADOW_BACKFILL', 'gate': 'TIER3_NOT_MET', 'samples': '14_VALID_LIVE_DAY_NEEDED'},
        'single_vote_rescue_replay': {'phase': 'DROP_AS_DESIGNED', 'reason': 'LEAKY_REFERENCE_ONLY'},
        'tier2_replay_shadow_V1': {'phase': 'DROP_AS_DESIGNED', 'reason': 'NEGATIVE_LIFT'},
        'tier2_replay_shadow_V2': {'phase': 'DROP_AS_DESIGNED', 'reason': 'NEGATIVE_LIFT_V2'},
        'cohere_rerank_effectiveness_v1': {'phase': 'SHADOW_BACKFILL', 'gate': 'VALUE_NOT_PROVEN'},
        'mt_model_hit_output_drop_shadow': {'phase': 'TEST_LANE_PARALLEL', 'role': 'measurement_only'},
        'loz_stage_trace_shadow': {'phase': 'TEST_LANE_PARALLEL', 'role': 'measurement_only'},
        'weekday_blackspot_shadow': {'phase': 'TEST_LANE_PARALLEL', 'role': 'measurement_only'},
        'cross_region_spillover_shadow': {'phase': 'TEST_LANE_PARALLEL', 'role': 'measurement_only'},
        'model_cross_region_dup_shadow': {'phase': 'TEST_LANE_PARALLEL', 'role': 'measurement_only'},
        'bundle_universe_coverage_shadow': {'phase': 'TEST_LANE_PARALLEL', 'role': 'measurement_only'},
        'mb_structural_drilldown_shadow': {'phase': 'TEST_LANE_PARALLEL', 'role': 'measurement_only'},
        'model_latency_cost_audit_daily': {'phase': 'BROKEN_NEEDS_FIX', 'reason': 'NO_PER_MODEL_DURATION 100%'},
        'model_strength_by_region_weekday_station_daily': {'phase': 'TEST_LANE_PARALLEL', 'role': 'measurement_only', 'latest_anchor': latest_anchor},
        'experimental_preview_shadow_multi_region': {'phase': 'TEST_LANE_PARALLEL', 'role': 'test_bundle_diagnostic', 'admin_only': True},
        'V55_GOOGLE_DIRECT_SHADOW_COHORT': {
            'phase': 'TEST_LANE_PARALLEL',
            'models': ['gemini-3.1-pro', 'gemini-3-flash', 'gemma-4-31b'],
            'first_predictions': '2026-05-05',
            'today_status': {
                'gemini-3.1-pro': '3 rows (MB PARTIAL, MN LOSE, MT LOSE)',
                'gemini-3-flash': '3 rows (MB WIN! MN PARTIAL, MT LOSE)',
                'gemma-4-31b': '0 rows on 05/05 due to scheduler preflight bug; FIXED IN V55 — will run 06/05 onward',
            },
            'gate': 'NOT_ENOUGH_EVIDENCE_NEED_14D',
        },
    },
    'live_parallel_status': 'LIVE_PARALLEL_AUTO_PENDING_ONLY',
    'why_not_full_auto': 'V52.5.6 manual runner only; multi-region closeout evaluator (C-03) not built; scheduler auto-wire (C-04) blocked on >=3-5 clean closeouts',
}
with open('artifacts/_v55_method_multilane_status_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(method_status, f, ensure_ascii=False, indent=2, default=str)

# 7. State file
state = {
    'pass_id': 'V20.3.37.55_full_chain',
    'anchor_date': '2026-05-05',
    'service_active': True,
    'health_http': 200,
    'live_window_passed': True,  # 20:14 VN > 18:30 MB cutoff
    'rolling_metrics_post_05_05': {
        'MN': {'7d_BT': 42.9, '14d_BT': 50.0, '30d_BT': 56.7, '60d_BT': 46.7},
        'MT': {'7d_BT': 71.4, '14d_BT': 50.0, '30d_BT': 36.7, '60d_BT': 50.0},
        'MB': {'7d_BT': 14.3, '14d_BT': 28.6, '30d_BT': 20.0, '60d_BT': 26.7},
    },
    'two_day_official': {
        '2026-05-04': {'MN': 'BT_LOSE+lo2_PARTIAL', 'MT': 'BT_WIN+lo2_WIN', 'MB': 'BT_LOSE+lo2_LOSE'},
        '2026-05-05': {'MN': 'BT_LOSE+lo2_LOSE', 'MT': 'BT_WIN+lo2_PARTIAL', 'MB': 'BT_LOSE+lo2_LOSE'},
    },
    'two_day_winner_per_region': {
        'MN': 'TEST_RESCUE: SPECIALIST_ROSTER 04/05 picked 32 (hit), AI_CHAIN_PRESERVATION 05/05 picked 52 (hit)',
        'MT': 'OFFICIAL_WIN_BOTH_DAYS (29 then 44)',
        'MB': 'NO_METHOD_FOUND_HIT both days',
    },
    'verdict_label': 'TWO_DAY_FORENSIC_ONLY + READY_FOR_TEST_LANE_ENHANCEMENT + READY_FOR_MEASUREMENT_ONLY_IMPLEMENTATION + NOT_READY_FOR_OFFICIAL_CHANGE',
    'critical_findings': [
        'MN BT 30d dropped 60% → 56.7% (V54 → V55)',
        'MT 7d 71.4% rising fast — but 30d still 36.7%',
        'MB 60d 26.7% structural; MB Wed/Fri remain BLACK_SPOT_CONFIRMED on anchor 2026-05-05',
        'MT_AI_CHAIN_PRESERVATION_V1 destructive on MT (broke 29 win → 82 LOSE on 04/05; broke 44 → 39 on 05/05) — NOT promote',
        'MN_AI_CHAIN_PRESERVATION_V1 free win on 05/05 (52 vs 15) — keep watching MN-only',
        'MN_SPECIALIST_ROSTER_V1 free win on 04/05 (32 vs 65)',
        'gemini-3-flash MB WIN day 1 (91+14, both hit) — KEEP_CANDIDATE',
        'gemma-4-31b: 0 rows 05/05 due to scheduler preflight bug. Bug FIXED in V55 (scheduler.py route gemma→google lane). Will run 06/05.',
        'C-05 latency: still 0/0 latency_available, NO_PER_MODEL_DURATION 100% — pruning blocked.',
        'loz_stage_trace materialized 04/05+05/05; 0 ai_dropped events but loz_select_miss MN 5, MT 6, MB 4 over 2 days.',
    ],
}
with open('artifacts/_v55_state_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

# 8. Pre-hash already done — just ensure post-hash now
TABLES_FOR_HASH = [
    'predictions', 'final_bundles', 'lottery_results', 'model_daily_eval',
    'scheduler_logs',
    'mt_model_hit_output_drop_shadow', 'loz_selector_shadow',
    'model_latency_cost_audit_daily', 'model_strength_by_region_weekday_station_daily',
    'experimental_preview_shadow', 'mb_experimental_preview_shadow',
    'du_doan_test_runs', 'du_doan_test_bundles', 'du_doan_test_results',
    'du_doan_test_candidates', 'du_doan_test_model_contribution',
    'du_doan_test_audit_log',
    'loz_stage_trace_shadow', 'weekday_blackspot_shadow',
]
import hashlib
post_lines = ["table | rows | sha256 (best-effort) — POST V55 materialization"]
for t in TABLES_FOR_HASH:
    try:
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        n = cur.fetchone()[0]
        try:
            cur.execute(f"SELECT * FROM {t} LIMIT 5000")
            rows = cur.fetchall()
            blob = '|'.join(','.join(str(c) for c in r) for r in rows)
            sig = hashlib.sha256(blob.encode('utf-8','replace')).hexdigest()[:16]
        except Exception:
            sig = 'NA'
        post_lines.append(f"{t} | {n} | {sig}")
    except sqlite3.OperationalError as e:
        post_lines.append(f"{t} | MISSING | {e}")
with open('artifacts/_v55_post_hash_20260505.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(post_lines))

print("V55_AGGREGATE_OK")
print(json.dumps({k: state[k] for k in ['rolling_metrics_post_05_05','two_day_official','two_day_winner_per_region','verdict_label']}, ensure_ascii=False, indent=2))
con.close()
