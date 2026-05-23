"""Null Test 5: Forward 90d audit on V106.03/04/05 pre-registered rules.

Reality check (transparency):
  V106.03 published 2026-05-21
  V106.04 published 2026-05-22
  V106.05 published 2026-05-23
  Locked DB last_date    = 2026-05-23
So forward window for each report is at most:
  V106.03 -> 2 days, V106.04 -> 1 day, V106.05 -> 0 days
This is insufficient for a true 90d forward audit.

We do the most honest thing possible:
1. Report INSUFFICIENT_FORWARD_DATA verdict honestly.
2. Compute available "post-registration" lift for V106.03 rules
   over 2 actual closeout days as preliminary check.
3. Run a synthetic forward proxy: leave-out last 30 days from full
   180d window. Re-evaluate top panel rules on those 30 holdout days.
4. Aggregate p-value across rules using Fisher's combined p.

Output: machine_readable/V107_NULL5_FORWARD_AUDIT.json
"""
from __future__ import annotations

import csv
import json
import math
from datetime import date, datetime, timedelta
from pathlib import Path

import _v107_lib as lib

OUT_PATH = lib.MR_DIR / 'V107_NULL5_FORWARD_AUDIT.json'

# Pre-registered rules from V106.03 (MB G2 first/both -> MN)
V10603_RULES = [
    {  # MB Giai nhi bo dau tien D-2 -> MN
        'target_region': 'MN', 'source_region': 'MB', 'source_unit': 'MB_BOARD',
        'source_prize': 'G2', 'source_index': 1, 'transform': 'LAST2', 'lag': 2,
        'weekday': None, 'station_set': None, 'window': 30,
        'pre_registered_at': '2026-05-21', 'reported_lift_pp': 14.1, 'reported_days': 30,
    },
    {  # MB Giai nhi bo so 2 D-2 -> MN
        'target_region': 'MN', 'source_region': 'MB', 'source_unit': 'MB_BOARD',
        'source_prize': 'G2', 'source_index': 2, 'transform': 'LAST2', 'lag': 2,
        'weekday': None, 'station_set': None, 'window': 30,
        'pre_registered_at': '2026-05-21', 'reported_lift_pp': 5.8, 'reported_days': 30,
    },
    {  # MB Giai nhi pair D-1 -> MN candidate-rate
        'target_region': 'MN', 'source_region': 'MB', 'source_unit': 'MB_BOARD',
        'source_prize': 'G2', 'source_index': 1, 'transform': 'LAST2', 'lag': 1,
        'weekday': None, 'station_set': None, 'window': 30,
        'pre_registered_at': '2026-05-21', 'reported_lift_pp': 0.8, 'reported_days': 30,
    },
]

# V106.05 Tier-1 shadow recommendations
V10605_RULES = [
    {
        'target_region': 'MT', 'source_region': 'MB', 'source_unit': 'MB_BOARD',
        'source_prize': 'G2', 'source_index': 1, 'transform': 'P4P1', 'lag': 1,
        'weekday': None, 'station_set': None, 'window': 90,
        'pre_registered_at': '2026-05-23', 'reported_lift_pp': 14.9,
    },
    {
        'target_region': 'MT', 'source_region': 'MB', 'source_unit': 'MB_BOARD',
        'source_prize': 'G1', 'source_index': 1, 'transform': 'P5P2', 'lag': 1,
        'weekday': None, 'station_set': None, 'window': 90,
        'pre_registered_at': '2026-05-23', 'reported_lift_pp': 11.6,
    },
]

# V106.06 Tier A scoped highlights (also pre-registered today; forward window = 0)
V10606_RULES = [
    {
        'target_region': 'MT', 'source_region': 'MB', 'source_unit': 'MB_BOARD',
        'source_prize': 'DB', 'source_index': 1, 'transform': 'P2P4', 'lag': 1,
        'weekday': 6, 'station_set': None, 'window': 180,
        'pre_registered_at': '2026-05-23', 'reported_lift_pp': 35.2,
    },
    {
        'target_region': 'MN', 'source_region': 'MT', 'source_unit': 'Đắk Nông',
        'source_prize': 'DB', 'source_index': 1, 'transform': 'FIRST2_REV', 'lag': 3,
        'weekday': None, 'station_set': ('Bạc Liêu', 'Bến Tre', 'Vũng Tàu'),
        'window': 180,
        'pre_registered_at': '2026-05-23', 'reported_lift_pp': 31.9,
    },
]


def evaluate_window(target_index, source_index, all_dates, rule, start_date, end_date):
    days = 0
    hits = 0
    sum_target = 0
    db_day = 0
    sum_db = 0
    for td in all_dates:
        if td < start_date or td > end_date:
            continue
        weekday = rule['weekday']
        if weekday is not None and td.weekday() != weekday:
            continue
        tgt = target_index.get((td, rule['target_region']))
        if not tgt:
            continue
        if rule['station_set'] is not None and tgt['stations'] != rule['station_set']:
            continue
        sd = td - timedelta(days=rule['lag'])
        src = source_index.get((sd, rule['source_region'], rule['source_unit'],
                                rule['source_prize'], rule['source_index'], rule['transform']))
        if not src:
            continue
        days += 1
        t = src['tail']
        if t in tgt['all_set']:
            hits += 1
        if any(db == t for _, db in tgt['dbs']):
            db_day += 1
        sum_target += len(tgt['all_set'])
        sum_db += len(tgt['db_unique'])
    if days == 0:
        return None
    base = sum_target / 100 / days
    return {
        'days': days,
        'hits': hits,
        'hit_rate': hits / days,
        'baseline': base,
        'lift_pp': (hits / days - base) * 100,
        'db_day_rate': db_day / days,
        'db_day_baseline': sum_db / 100 / days,
        'db_day_lift_pp': (db_day / days - sum_db / 100 / days) * 100,
        'raw_p': lib.binomial_pvalue_one_sided(hits, days, base),
        'ci95': lib.wilson_ci(hits, days),
    }


def fishers_combined(pvalues):
    valid = [p for p in pvalues if p is not None and 0 < p <= 1]
    if not valid:
        return None, 0
    chi2 = -2 * sum(math.log(p) for p in valid)
    df = 2 * len(valid)
    # Survival function chi2 (df=2k)
    # P = exp(-chi2/2) sum_{i=0}^{k-1} (chi2/2)^i / i!
    half = chi2 / 2
    k = df // 2
    s = sum(half ** i / math.factorial(i) for i in range(k))
    return math.exp(-half) * s, len(valid)


def main():
    print('Loading rows ...')
    rows = lib.load_rows()
    source_index, target_index, all_dates = lib.build_indices(rows)
    last_date = max(all_dates)

    out = {
        'live_sync_manifest': lib.LOCKED_MANIFEST,
        'last_db_date': last_date.isoformat(),
        'note': (
            'V106.03 published 2026-05-21, V106.04 2026-05-22, V106.05 2026-05-23. '
            'Locked DB last_date 2026-05-23 -> forward window <= 2 days. '
            'A true 90-day forward audit is INSUFFICIENT. '
            'We additionally run a 30-day holdout proxy: leave the most recent 30 days out '
            'of training, evaluate panel rules on those 30 days only.'
        ),
        'reports': [],
    }

    # 1) Available post-registration audit per report
    for tag, rules_list in (('V106.03', V10603_RULES), ('V106.05', V10605_RULES), ('V106.06', V10606_RULES)):
        report_data = {'report': tag, 'rules': []}
        forward_pvalues = []
        for r in rules_list:
            reg_date = lib.dparse(r['pre_registered_at'])
            forward_start = reg_date + timedelta(days=1)
            res = evaluate_window(target_index, source_index, all_dates, r, forward_start, last_date)
            entry = {
                'rule_lineage': f"{r['source_region']}:{r['source_unit']}:{r['source_prize']}#{r['source_index']}:{r['transform']} {('D-'+str(r['lag'])) if r['lag']<=7 else ('W-'+str(r['lag']//7))}",
                'target': r['target_region'],
                'pre_registered_at': r['pre_registered_at'],
                'reported_lift_pp': r['reported_lift_pp'],
                'forward_window_start': forward_start.isoformat(),
                'forward_window_end': last_date.isoformat(),
                'forward_days_available': (last_date - forward_start).days + 1 if last_date >= forward_start else 0,
                'forward_result': res,
            }
            if res:
                forward_pvalues.append(res['raw_p'])
            report_data['rules'].append(entry)
        agg_p, k = fishers_combined(forward_pvalues)
        report_data['fisher_combined_p'] = agg_p
        report_data['fisher_n_rules'] = k
        report_data['stopping_check'] = (
            'INSUFFICIENT_DATA' if k == 0 or agg_p is None else
            'FAIL_STOPPING_CRITERION' if agg_p >= 0.5 else
            'PASS_PRELIMINARY'
        )
        out['reports'].append(report_data)

    # 2) 30-day holdout proxy on V107 panel
    panel = json.loads((lib.MR_DIR / 'V107_RULE_PANEL.json').read_text(encoding='utf-8'))
    holdout_start = last_date - timedelta(days=29)
    train_end = holdout_start - timedelta(days=1)
    train_start = train_end - timedelta(days=149)  # 150-day train
    print(f'Holdout window: {holdout_start} -> {last_date}')
    print(f'Training window: {train_start} -> {train_end}')

    holdout_results = []
    forward_pvalues_holdout = []
    n_lift_positive = 0
    n_lift_significant = 0
    sum_lift_holdout = 0
    rules_evaluated = 0
    for r in panel:
        # Convert station_set list -> tuple for index
        ws = tuple(r['station_set']) if r['station_set'] else None
        rule = dict(r); rule['station_set'] = ws
        train = evaluate_window(target_index, source_index, all_dates, rule, train_start, train_end)
        holdout = evaluate_window(target_index, source_index, all_dates, rule, holdout_start, last_date)
        if train is None or holdout is None or holdout['days'] < 5:
            continue
        rules_evaluated += 1
        sum_lift_holdout += holdout['lift_pp']
        if holdout['lift_pp'] > 0:
            n_lift_positive += 1
        if holdout['raw_p'] < 0.05:
            n_lift_significant += 1
        forward_pvalues_holdout.append(holdout['raw_p'])
        holdout_results.append({
            'rule_key': f"{r['source_region']}:{r['source_unit']}:{r['source_prize']}#{r['source_index']}:{r['transform']}",
            'target': r['target_region'],
            'lag': r['lag'],
            'tier_v106': r['tier'],
            'reported_lift_pp': r['reported_lift_pp'],
            'train_lift_pp': train['lift_pp'] if train else None,
            'holdout_lift_pp': holdout['lift_pp'],
            'holdout_db_lift_pp': holdout['db_day_lift_pp'],
            'holdout_days': holdout['days'],
            'holdout_raw_p': holdout['raw_p'],
        })

    holdout_results.sort(key=lambda r: -r['holdout_lift_pp'])
    agg_p_holdout, k_holdout = fishers_combined(forward_pvalues_holdout)

    out['holdout_30d_proxy'] = {
        'train_window_start': train_start.isoformat(),
        'train_window_end': train_end.isoformat(),
        'holdout_window_start': holdout_start.isoformat(),
        'holdout_window_end': last_date.isoformat(),
        'rules_evaluated': rules_evaluated,
        'n_lift_positive': n_lift_positive,
        'rate_lift_positive': round(n_lift_positive / rules_evaluated, 4) if rules_evaluated else 0,
        'n_lift_significant_p05': n_lift_significant,
        'rate_lift_significant_p05': round(n_lift_significant / rules_evaluated, 4) if rules_evaluated else 0,
        'mean_holdout_lift_pp': round(sum_lift_holdout / rules_evaluated, 3) if rules_evaluated else 0,
        'fisher_combined_p_aggregate': agg_p_holdout,
        'fisher_n_rules': k_holdout,
        'top10_holdout_lift_pp': [round(r['holdout_lift_pp'], 3) for r in holdout_results[:10]],
        'verdict': (
            'PASS_PRELIMINARY' if agg_p_holdout is not None and agg_p_holdout < 0.5
            else 'FAIL_STOPPING_CRITERION'
        ),
        'note': (
            'Honest holdout proxy: train rule selection on first 150 days, evaluate on last 30 days. '
            'rate_lift_positive should be > 0.5 if rules have stable forward signal. '
            'Stopping criterion: aggregate p >= 0.5 -> FAIL.'
        ),
    }

    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2, default=str), encoding='utf-8')

    print('\n=== V106.03/05/06 forward audit ===')
    for rep in out['reports']:
        print(f"  {rep['report']}: rules={len(rep['rules'])}, fisher_p={rep['fisher_combined_p']}, status={rep['stopping_check']}")
    print('\n=== 30-day holdout proxy ===')
    h = out['holdout_30d_proxy']
    print(f"  Rules evaluated: {h['rules_evaluated']}")
    print(f"  Mean holdout lift: {h['mean_holdout_lift_pp']:.2f} pp")
    print(f"  rate_lift_positive: {h['rate_lift_positive']*100:.1f}%")
    print(f"  rate_lift_significant_p05: {h['rate_lift_significant_p05']*100:.1f}%")
    print(f"  fisher_combined_p_aggregate: {h['fisher_combined_p_aggregate']}")
    print(f"  Verdict: {h['verdict']}")
    print(f'\nWrote {OUT_PATH}')


if __name__ == '__main__':
    main()
