"""V55 forensic query — covers 2026-05-04 and 2026-05-05 across all regions.

Output:
  - artifacts/_v55_official_closeout_20260504_20260505.json
  - artifacts/_v55_du_doan_test_closeout_20260504_20260505.json
  - artifacts/_v55_pre_hash_20260505.txt
  - artifacts/_v55_rolling_metrics_after_20260505.json
"""
import sqlite3, json, hashlib, os, datetime
from collections import defaultdict, Counter

DB = 'data/lottery_ai.db'
OUT_DIR = 'artifacts'
DATES = ['2026-05-04', '2026-05-05']
REGIONS = ['MN', 'MT', 'MB']

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
cur = con.cursor()


def tail_of(num):
    s = ''.join(c for c in str(num) if c.isdigit())
    return s[-2:].zfill(2) if s else ''


def to_tail_set(values):
    out = set()
    if not values:
        return out
    if isinstance(values, str):
        try:
            values = json.loads(values)
        except Exception:
            values = [values]
    if isinstance(values, dict):
        values = list(values.values())
    if not isinstance(values, list):
        values = [values]
    for v in values:
        if isinstance(v, list):
            out.update(to_tail_set(v))
        elif v is not None:
            t = tail_of(v)
            if t:
                out.add(t)
    return out


# ---------- 1. PRE-HASH ----------
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

hash_lines = ["table | rows | sha256(rowids+date+region) (best-effort)"]
for t in TABLES_FOR_HASH:
    try:
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        n = cur.fetchone()[0]
        # cheap content fingerprint
        try:
            cur.execute(f"SELECT * FROM {t} LIMIT 5000")
            rows = cur.fetchall()
            blob = '|'.join(','.join(str(c) for c in r) for r in rows)
            sig = hashlib.sha256(blob.encode('utf-8','replace')).hexdigest()[:16]
        except Exception:
            sig = 'NA'
        hash_lines.append(f"{t} | {n} | {sig}")
    except sqlite3.OperationalError as e:
        hash_lines.append(f"{t} | MISSING | {e}")

with open(f'{OUT_DIR}/_v55_pre_hash_20260505.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(hash_lines))


# ---------- 2. OFFICIAL CLOSEOUT 04/05 + 05/05 ----------
official = {}
for date in DATES:
    official[date] = {}
    for region in REGIONS:
        # final_bundle
        cur.execute(
            "SELECT * FROM final_bundles WHERE date=? AND region=? ORDER BY id DESC LIMIT 1",
            (date, region))
        bundle_row = cur.fetchone()
        # actual lottery_results
        cur.execute(
            "SELECT * FROM lottery_results WHERE date=? AND region=?",
            (date, region))
        result_rows = cur.fetchall()
        actual_tails = set()
        actual_db = []
        actual_g7 = []
        actual_g8 = []
        actual_g6 = []
        for r in result_rows:
            keys = r.keys()
            if 'tail_db' in keys:
                td = tail_of(r['tail_db'])
                if td:
                    actual_db.append(td)
                    actual_tails.add(td)
            if 'tail_g8' in keys:
                tg = tail_of(r['tail_g8'])
                if tg:
                    actual_g8.append(tg)
                    actual_tails.add(tg)
            if 'prizes' in keys and r['prizes']:
                try:
                    pj = json.loads(r['prizes'])
                except Exception:
                    pj = {}
                for prize_key, vals in (pj or {}).items():
                    if not isinstance(vals, list):
                        vals = [vals]
                    for v in vals:
                        t = tail_of(v)
                        if t:
                            actual_tails.add(t)
                            if 'bảy' in prize_key.lower() or prize_key.upper().startswith('G7'):
                                actual_g7.append(t)
                            if 'sáu' in prize_key.lower() or prize_key.upper().startswith('G6'):
                                actual_g6.append(t)
        # predictions (schema uses `main_numbers`)
        cur.execute(
            "SELECT ai_model, run_source, main_numbers, status, pick_count, created_at, hit_count, hit_numbers, hit_level "
            "FROM predictions WHERE date=? AND target_region=? "
            "ORDER BY created_at",
            (date, region))
        preds = [dict(r) for r in cur.fetchall()]
        for p in preds:
            try:
                lst = json.loads(p['main_numbers']) if p.get('main_numbers') else []
            except Exception:
                lst = []
            if isinstance(lst, dict):
                lst = list(lst.values())
            p['numbers_list'] = [tail_of(n) for n in (lst or []) if tail_of(n)]
        # decode bundle
        bundle = dict(bundle_row) if bundle_row else None
        bt = None
        lo2 = []
        lo3 = None
        bundle_voters_top = {}
        if bundle:
            bt = tail_of(bundle.get('bach_thu') or '')
            try:
                lo2 = [tail_of(x) for x in (json.loads(bundle.get('lo2')) if bundle.get('lo2') else [])]
            except Exception:
                lo2 = []
            lo3 = bundle.get('lo3')
            # parse source_predictions_json for voter map
            try:
                spj = json.loads(bundle.get('source_predictions_json') or '{}')
                rn = spj.get('ranked_numbers') or []
                for entry in rn:
                    bundle_voters_top[tail_of(entry.get('number'))] = entry.get('voters') or []
            except Exception:
                pass
        # determine BT win/lose
        bt_status = bundle.get('bach_thu_status') if bundle else None
        # MN/MT BT hits if bt in any G7/G8/DB tail; MB if bt in any of all tails
        actual_top_set = set(actual_g7) | set(actual_g8) | set(actual_db)
        bt_hit_any = (bt in actual_tails) if bt else False
        # lo2 status
        lo2_full = bool(lo2) and all(t in actual_tails for t in lo2)
        lo2_any = bool(lo2) and any(t in actual_tails for t in lo2)
        # model-level correctness (top1 hit BT?, top1 hit any actual? )
        model_correct = []
        for p in preds:
            top1 = p['numbers_list'][0] if p['numbers_list'] else None
            top2 = p['numbers_list'][1] if len(p['numbers_list']) > 1 else None
            if top1 is None and top2 is None:
                continue
            row = {
                'model': p.get('ai_model'),
                'run_source': p.get('run_source'),
                'top1': top1, 'top2': top2,
                'top1_hit_actual': top1 in actual_tails if top1 else False,
                'top2_hit_actual': top2 in actual_tails if top2 else False,
                'top1_eq_official_bt': bt is not None and top1 == bt,
                'in_official_voter_set_top1': bt is not None and (p.get('ai_model') in bundle_voters_top.get(bt, [])),
            }
            model_correct.append(row)
        # candidate-universe miss: any actual tail in any prediction.numbers?
        candidate_universe = set()
        for p in preds:
            candidate_universe.update(p['numbers_list'])
        actual_in_candidates = sorted(t for t in actual_tails if t in candidate_universe)
        actual_missing = sorted(t for t in actual_tails if t not in candidate_universe)
        # bundle conversion
        bundle_top10 = list(bundle_voters_top.keys())
        actual_in_bundle_top10 = sorted(t for t in actual_tails if t in bundle_top10)
        actual_missed_by_bundle_but_in_candidates = sorted(
            t for t in actual_tails if t in candidate_universe and t not in bundle_top10
        )

        official[date][region] = {
            'final_bundle_exists': bundle is not None,
            'bt': bt,
            'lo2': lo2,
            'lo3': lo3,
            'bt_status_recorded': bt_status,
            'lo2_status_recorded': bundle.get('lo2_status') if bundle else None,
            'bt_hit_any_actual_tail': bt_hit_any,
            'lo2_full': lo2_full,
            'lo2_any': lo2_any,
            'created_at': bundle.get('created_at') if bundle else None,
            'updated_at': bundle.get('updated_at') if bundle else None,
            'verified_at': bundle.get('verified_at') if bundle else None,
            'actual_tails_count': len(actual_tails),
            'actual_db_tails': sorted(set(actual_db)),
            'actual_g7_tails': sorted(set(actual_g7)),
            'actual_g8_tails': sorted(set(actual_g8)),
            'actual_g6_tails': sorted(set(actual_g6)),
            'actual_tails_sample': sorted(actual_tails)[:30],
            'predictions_count': len(preds),
            'predictions_by_run_source': dict(Counter(p.get('run_source') for p in preds)),
            'candidate_universe_size': len(candidate_universe),
            'actual_in_candidates_count': len(actual_in_candidates),
            'actual_missing_from_candidates_count': len(actual_missing),
            'actual_missing_from_candidates_sample': actual_missing[:20],
            'actual_in_bundle_top10_count': len(actual_in_bundle_top10),
            'actual_in_bundle_top10': actual_in_bundle_top10,
            'actual_missed_by_bundle_but_in_candidates_count': len(actual_missed_by_bundle_but_in_candidates),
            'actual_missed_by_bundle_but_in_candidates_sample': actual_missed_by_bundle_but_in_candidates[:20],
            'model_correctness_summary': {
                'n_models': len(model_correct),
                'top1_hit_actual': sum(1 for x in model_correct if x['top1_hit_actual']),
                'top2_hit_actual': sum(1 for x in model_correct if x['top2_hit_actual']),
                'top1_or_top2_hit_actual': sum(1 for x in model_correct if x['top1_hit_actual'] or x['top2_hit_actual']),
                'top1_eq_official_bt': sum(1 for x in model_correct if x['top1_eq_official_bt']),
            },
            'model_correct_detail': model_correct,
            'bundle_top10_voters': bundle_voters_top,
        }

with open(f'{OUT_DIR}/_v55_official_closeout_20260504_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(official, f, ensure_ascii=False, indent=2)


# ---------- 3. /du-doan-test ROWS for 04/05 + 05/05 ----------
test = {}
for date in DATES:
    test[date] = {}
    for region in REGIONS:
        try:
            cur.execute(
                "SELECT * FROM du_doan_test_runs WHERE run_date=? AND region=?",
                (date, region))
            runs = [dict(r) for r in cur.fetchall()]
        except Exception:
            runs = []
        try:
            cur.execute(
                "SELECT * FROM du_doan_test_bundles WHERE run_date=? AND region=?",
                (date, region))
            bundles = [dict(r) for r in cur.fetchall()]
        except Exception:
            bundles = []
        try:
            cur.execute(
                "SELECT * FROM du_doan_test_results WHERE run_date=? AND region=?",
                (date, region))
            tres = [dict(r) for r in cur.fetchall()]
        except Exception:
            tres = []
        try:
            cur.execute(
                "SELECT * FROM du_doan_test_candidates WHERE run_date=? AND region=? LIMIT 200",
                (date, region))
            cands = [dict(r) for r in cur.fetchall()]
        except Exception:
            cands = []
        try:
            cur.execute(
                "SELECT * FROM experimental_preview_shadow WHERE date=? AND region=?",
                (date, region))
            preview = [dict(r) for r in cur.fetchall()]
        except Exception:
            preview = []
        try:
            cur.execute(
                "SELECT * FROM mb_experimental_preview_shadow WHERE date=?",
                (date,))
            mb_preview = [dict(r) for r in cur.fetchall()] if region == 'MB' else []
        except Exception:
            mb_preview = []

        test[date][region] = {
            'runs_count': len(runs),
            'runs_sample': runs[:5],
            'bundles_count': len(bundles),
            'bundles': bundles,
            'results_count': len(tres),
            'results': tres,
            'candidates_count': len(cands),
            'experimental_preview_count': len(preview),
            'experimental_preview_sample': preview[:5],
            'mb_experimental_preview_count': len(mb_preview),
            'mb_experimental_preview_sample': mb_preview[:5],
        }

with open(f'{OUT_DIR}/_v55_du_doan_test_closeout_20260504_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(test, f, ensure_ascii=False, indent=2, default=str)


# ---------- 4. ROLLING METRICS BT/LO2 PER REGION 7/14/30/60d ANCHOR 2026-05-05 ----------
def rolling(region, days):
    cur.execute(
        "SELECT date, bach_thu, bach_thu_status, lo2, lo2_status FROM final_bundles "
        "WHERE region=? AND date >= date('2026-05-05', ?) AND date <= '2026-05-05' "
        "ORDER BY date",
        (region, f'-{days-1} days'))
    rows = cur.fetchall()
    n = len(rows)
    bt_win = sum(1 for r in rows if (r['bach_thu_status'] or '').upper() == 'WIN')
    bt_lose = sum(1 for r in rows if (r['bach_thu_status'] or '').upper() == 'LOSE')
    lo2_win = sum(1 for r in rows if (r['lo2_status'] or '').upper() == 'WIN')
    lo2_partial = sum(1 for r in rows if (r['lo2_status'] or '').upper() == 'PARTIAL')
    lo2_lose = sum(1 for r in rows if (r['lo2_status'] or '').upper() == 'LOSE')
    return {
        'n': n,
        'bt_win': bt_win, 'bt_lose': bt_lose,
        'bt_win_pct': round(bt_win / n * 100, 1) if n else None,
        'lo2_win': lo2_win, 'lo2_partial': lo2_partial, 'lo2_lose': lo2_lose,
        'lo2_full_pct': round(lo2_win / n * 100, 1) if n else None,
        'lo2_any_pct': round((lo2_win + lo2_partial) / n * 100, 1) if n else None,
    }

rolling_metrics = {}
for region in REGIONS:
    rolling_metrics[region] = {}
    for d in [7, 14, 30, 60]:
        rolling_metrics[region][f'{d}d'] = rolling(region, d)

# Rolling per weekday for blackspot reconcile (last 60d)
weekday_metrics = {}
for region in REGIONS:
    cur.execute(
        "SELECT date, bach_thu_status, lo2_status FROM final_bundles "
        "WHERE region=? AND date >= date('2026-05-05','-59 days') AND date <= '2026-05-05'",
        (region,))
    rows = cur.fetchall()
    bydow = defaultdict(lambda: {'n': 0, 'bt_win': 0, 'lo2_win': 0, 'lo2_partial': 0})
    for r in rows:
        try:
            dt = datetime.datetime.strptime(r['date'], '%Y-%m-%d').date()
        except Exception:
            continue
        dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][dt.weekday()]
        bydow[dow]['n'] += 1
        if (r['bach_thu_status'] or '').upper() == 'WIN':
            bydow[dow]['bt_win'] += 1
        if (r['lo2_status'] or '').upper() == 'WIN':
            bydow[dow]['lo2_win'] += 1
        elif (r['lo2_status'] or '').upper() == 'PARTIAL':
            bydow[dow]['lo2_partial'] += 1
    for dow, d in bydow.items():
        d['bt_win_pct'] = round(d['bt_win']/d['n']*100, 1) if d['n'] else None
    weekday_metrics[region] = dict(bydow)

with open(f'{OUT_DIR}/_v55_rolling_metrics_after_20260505.json', 'w', encoding='utf-8') as f:
    json.dump({
        'anchor_date': '2026-05-05',
        'rolling': rolling_metrics,
        'weekday_60d': weekday_metrics,
    }, f, ensure_ascii=False, indent=2)


# ---------- 5. MT correct-but-dropped 04/05 + 05/05 ----------
mt_drop = {}
for date in DATES:
    region = 'MT'
    od = official[date][region]
    correct_models = [m for m in od['model_correct_detail']
                      if m['top1_hit_actual'] or m['top2_hit_actual']]
    dropped = [m for m in correct_models if not m['in_official_voter_set_top1']]
    bundle_top10 = list(od.get('bundle_top10_voters', {}).keys())
    correct_tails = sorted({m['top1'] for m in correct_models if m['top1_hit_actual']} |
                           {m['top2'] for m in correct_models if m['top2_hit_actual']})
    in_bundle_top10 = [t for t in correct_tails if t in bundle_top10]
    only_in_candidates = [t for t in correct_tails if t in od.get('actual_in_candidates_sample', []) or t in od.get('actual_missed_by_bundle_but_in_candidates_sample', [])]
    mt_drop[date] = {
        'n_correct_models': len(correct_models),
        'n_correct_models_with_top_outside_official_voters': len(dropped),
        'correct_models_dropped': dropped,
        'correct_tails': correct_tails,
        'correct_tails_in_bundle_top10': in_bundle_top10,
        'correct_tails_in_candidate_pool_only': only_in_candidates,
        'official_bt': od['bt'],
        'official_lo2': od['lo2'],
        'actual_tails_sample': od['actual_tails_sample'],
    }

with open(f'{OUT_DIR}/_v55_mt_correct_but_dropped_20260504_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(mt_drop, f, ensure_ascii=False, indent=2)


# ---------- 6. MB AI / no-token / specialist forensic 04/05 + 05/05 ----------
mb_forensic = {}
TOKEN_AI = {'gpt-5-mini','claude-sonnet-4-6','gemini-2.5-flash','claude-opus-4-20250514','deepseek-reasoner','gemini-2.5-pro','gpt-5.4'}
ML_MODELS = {'lstm','meta-learning','xgboost','random-forest'}
ENSEMBLE = {'smart-ensemble','smart-ml','combo-no-token','combo-super'}
SHADOW_AUTO = {'glm-5.1','grok-4.20-multi-agent','qwen3-coder','kimi-k2.5','qwen3-max-thinking',
               'gpt-oss-120b','gpt-5.5','deepseek-v4-pro','deepseek-v4-flash','qwen3.6-plus',
               'gemini-3.1-pro','gemini-3-flash','gemma-4-31b'}

for date in DATES:
    region = 'MB'
    od = official[date][region]
    by_family = defaultdict(list)
    for m in od['model_correct_detail']:
        mid = m['model']
        if mid in TOKEN_AI:
            fam = 'AI'
        elif mid in ML_MODELS:
            fam = 'ML'
        elif mid in ENSEMBLE:
            fam = 'ENSEMBLE'
        elif mid in SHADOW_AUTO:
            fam = 'SHADOW_AUTO'
        else:
            fam = 'OTHER'
        by_family[fam].append(m)
    fam_summary = {}
    for fam, lst in by_family.items():
        n = len(lst)
        h1 = sum(1 for x in lst if x['top1_hit_actual'])
        h2 = sum(1 for x in lst if x['top2_hit_actual'])
        h12 = sum(1 for x in lst if x['top1_hit_actual'] or x['top2_hit_actual'])
        fam_summary[fam] = {'n': n, 'top1_hit': h1, 'top2_hit': h2, 'top1or2_hit': h12,
                            'top1_hit_pct': round(h1/n*100,1) if n else None,
                            'top1or2_hit_pct': round(h12/n*100,1) if n else None}
    mb_forensic[date] = {
        'official_bt': od['bt'],
        'official_lo2': od['lo2'],
        'bt_hit_any_actual': od['bt_hit_any_actual_tail'],
        'lo2_full': od['lo2_full'],
        'lo2_any': od['lo2_any'],
        'family_summary': fam_summary,
        'family_detail': {fam: lst for fam, lst in by_family.items()},
    }

with open(f'{OUT_DIR}/_v55_mb_ai_notoken_specialist_forensic_20260504_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(mb_forensic, f, ensure_ascii=False, indent=2)


# ---------- 7. Loz control audit ----------
loz = {}
for date in DATES:
    loz[date] = {}
    for region in REGIONS:
        od = official[date][region]
        # model top2 union
        top1_or2 = []
        for m in od['model_correct_detail']:
            if m['top1']:
                top1_or2.append(m['top1'])
            if m['top2']:
                top1_or2.append(m['top2'])
        # how many of these hit
        hit_count = sum(1 for t in top1_or2 if t in od.get('actual_tails_sample', []))
        loz[date][region] = {
            'official_lo2': od['lo2'],
            'official_lo2_full': od['lo2_full'],
            'official_lo2_any': od['lo2_any'],
            'model_top1or2_count': len(top1_or2),
            'model_top1or2_unique_count': len(set(top1_or2)),
            'model_top1or2_hits_actual': hit_count,
        }
with open(f'{OUT_DIR}/_v55_loz_control_audit_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(loz, f, ensure_ascii=False, indent=2)


# ---------- 8. Tensor / latency snapshot ----------
tensor = {}
try:
    cur.execute(
        "SELECT COUNT(*) FROM model_strength_by_region_weekday_station_daily")
    tensor['model_strength_rows'] = cur.fetchone()[0]
    cur.execute(
        "SELECT MIN(anchor_date), MAX(anchor_date) FROM model_strength_by_region_weekday_station_daily")
    mn, mx = cur.fetchone()
    tensor['model_strength_date_range'] = [mn, mx]
except Exception as e:
    tensor['model_strength_error'] = str(e)
try:
    cur.execute(
        "SELECT COUNT(*) FROM model_latency_cost_audit_daily")
    tensor['latency_rows'] = cur.fetchone()[0]
    cur.execute(
        "SELECT COUNT(*) FROM model_latency_cost_audit_daily "
        "WHERE coverage_status='NO_PER_MODEL_DURATION'")
    tensor['no_per_model_duration_rows'] = cur.fetchone()[0]
except Exception as e:
    tensor['latency_error'] = str(e)
try:
    cur.execute(
        "SELECT date, region, drop_classification, COUNT(*) FROM mt_model_hit_output_drop_shadow "
        "WHERE date IN (?,?) GROUP BY date, region, drop_classification",
        DATES)
    tensor['mt_drop_2day'] = [list(r) for r in cur.fetchall()]
except Exception as e:
    tensor['mt_drop_error'] = str(e)
try:
    cur.execute(
        "SELECT region, drop_classification, COUNT(*) FROM mt_model_hit_output_drop_shadow "
        "WHERE date >= date('2026-05-05','-29 days') GROUP BY region, drop_classification")
    tensor['mt_drop_30d'] = [list(r) for r in cur.fetchall()]
except Exception as e:
    tensor['mt_drop_30d_error'] = str(e)
try:
    cur.execute(
        "SELECT region, weekday_name, blackspot_label, total_days, bt_wins, bt_rate, lo2_full_rate, lo2_any_rate "
        "FROM weekday_blackspot_shadow WHERE anchor_date=(SELECT MAX(anchor_date) FROM weekday_blackspot_shadow) "
        "ORDER BY region, weekday")
    tensor['weekday_blackspot'] = [dict(r) for r in cur.fetchall()]
except Exception as e:
    tensor['blackspot_error'] = str(e)
try:
    cur.execute(
        "SELECT date, region, COUNT(*) FROM loz_stage_trace_shadow "
        "WHERE date IN (?,?) GROUP BY date, region",
        DATES)
    tensor['loz_stage_trace_2day'] = [list(r) for r in cur.fetchall()]
except Exception as e:
    tensor['loz_stage_trace_error'] = str(e)

with open(f'{OUT_DIR}/_v55_model_tensor_latency_pruning_readiness_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(tensor, f, ensure_ascii=False, indent=2)


# ---------- 9. Service / source predictions check ----------
overview = {
    'anchor_date': '2026-05-05',
    'db_path': DB,
    'rows_today': {
        'predictions': cur.execute("SELECT COUNT(*) FROM predictions WHERE date='2026-05-05'").fetchone()[0],
        'final_bundles': cur.execute("SELECT COUNT(*) FROM final_bundles WHERE date='2026-05-05'").fetchone()[0],
        'lottery_results': cur.execute("SELECT COUNT(*) FROM lottery_results WHERE date='2026-05-05'").fetchone()[0],
        'predictions_yest': cur.execute("SELECT COUNT(*) FROM predictions WHERE date='2026-05-04'").fetchone()[0],
        'final_bundles_yest': cur.execute("SELECT COUNT(*) FROM final_bundles WHERE date='2026-05-04'").fetchone()[0],
        'lottery_results_yest': cur.execute("SELECT COUNT(*) FROM lottery_results WHERE date='2026-05-04'").fetchone()[0],
    },
}

# scheduler markers (extracted from message column)
try:
    cur.execute(
        "SELECT job_name, MAX(log_time), region, date_str FROM scheduler_logs "
        "WHERE log_time >= '2026-05-04' GROUP BY job_name, region, date_str ORDER BY 2 DESC LIMIT 50")
    overview['scheduler_jobs_recent'] = [list(r) for r in cur.fetchall()]
    cur.execute("SELECT COUNT(*) FROM scheduler_logs WHERE log_time >= '2026-05-04'")
    overview['scheduler_logs_recent_count'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM scheduler_logs WHERE log_time >= '2026-05-05'")
    overview['scheduler_logs_today_count'] = cur.fetchone()[0]
except Exception as e:
    overview['scheduler_markers_error'] = str(e)

with open(f'{OUT_DIR}/_v55_state_20260505.json', 'w', encoding='utf-8') as f:
    json.dump(overview, f, ensure_ascii=False, indent=2)


print("V55_FORENSIC_QUERY_OK")
print(json.dumps({
    'rolling_30d': {r: rolling_metrics[r]['30d'] for r in REGIONS},
    'rolling_60d': {r: rolling_metrics[r]['60d'] for r in REGIONS},
    'rolling_14d': {r: rolling_metrics[r]['14d'] for r in REGIONS},
    'rolling_7d': {r: rolling_metrics[r]['7d'] for r in REGIONS},
}, ensure_ascii=False, indent=2))
con.close()
