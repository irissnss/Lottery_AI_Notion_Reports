"""Null Test 2: Negative control synthetic features.

6 synthetic "source" features (deterministic, non-related to lottery):
  1. random_00_99_seed42      : seeded PRNG hash(date)
  2. moon_phase_28day         : tail = (day_of_year % 28) repeated to 2 digits
  3. lunar_day_30             : tail = (day_of_year % 30) repeated
  4. day_of_year_tail         : last 2 digits of day_of_year
  5. weekday_month_composite  : (weekday * 13 + month) % 100
  6. sine_period_27           : tail = int(50 + 49*sin(2*pi*doy/27)) % 100

Note: gold/USD/BTC tail features cannot be fetched without external API
(per governance: no provider call). The 6 features above are stable
proxies that are deterministic and uncorrelated with VN lottery RNG.

Pipeline parity with V106.05 mining:
- For each synthetic feature: run a full single-source matrix
  (lags D-1..D-7, W-1..W-4, windows 30/60/90/180, scopes global +
  weekday) against MN/MT/MB.
- Take best lift per (target, scope) and best lift overall.
- Compare to top lifts achieved by REAL MB_BOARD low-prize sources
  in V106.06 with same scope.

Output: machine_readable/V107_NULL2_NEGATIVE_CONTROL.json
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import random
from datetime import timedelta
from pathlib import Path

import _v107_lib as lib

OUT_PATH = lib.MR_DIR / 'V107_NULL2_NEGATIVE_CONTROL.json'
LAGS = [1, 2, 3, 4, 5, 6, 7, 14, 21, 28]
WINDOWS = [30, 60, 90, 180]


def random_tail_seed42(dt):
    rng = random.Random(int(hashlib.md5(f'42_{dt.isoformat()}'.encode()).hexdigest(), 16) % (2 ** 32))
    return f'{rng.randint(0, 99):02d}'


def moon_phase_tail(dt):
    doy = dt.timetuple().tm_yday
    v = doy % 28
    return f'{v:02d}'


def lunar_day_tail(dt):
    doy = dt.timetuple().tm_yday
    v = doy % 30
    return f'{v:02d}'


def day_of_year_tail(dt):
    doy = dt.timetuple().tm_yday
    return f'{doy % 100:02d}'


def weekday_month_composite(dt):
    v = (dt.weekday() * 13 + dt.month) % 100
    return f'{v:02d}'


def sine_period_27(dt):
    doy = dt.timetuple().tm_yday
    v = int(round(50 + 49 * math.sin(2 * math.pi * doy / 27))) % 100
    return f'{v:02d}'


SYNTHETIC_FEATURES = {
    'random_00_99_seed42': random_tail_seed42,
    'moon_phase_28day': moon_phase_tail,
    'lunar_day_30': lunar_day_tail,
    'day_of_year_tail': day_of_year_tail,
    'weekday_month_composite': weekday_month_composite,
    'sine_period_27': sine_period_27,
}


def build_synthetic_source(name, fn, all_dates):
    return {dt: fn(dt) for dt in all_dates}


def evaluate_negative(target_index, all_dates, last_date, target_region, source_map,
                     lag, window, weekday=None):
    start = last_date - timedelta(days=window - 1)
    days = 0
    hits = 0
    db_day = 0
    sum_target = 0
    sum_db = 0
    for td in all_dates:
        if td < start or td > last_date:
            continue
        if weekday is not None and td.weekday() != weekday:
            continue
        tgt = target_index.get((td, target_region))
        if not tgt or not tgt['all_set']:
            continue
        sd = td - timedelta(days=lag)
        if sd not in source_map:
            continue
        days += 1
        t = source_map[sd]
        if t in tgt['all_set']:
            hits += 1
        if any(db == t for _, db in tgt['dbs']):
            db_day += 1
        sum_target += len(tgt['all_set'])
        sum_db += len(tgt['db_unique'])
    if days < 20:
        return None
    base = sum_target / 100 / days
    db_base = sum_db / 100 / days
    hit_rate = hits / days
    db_rate = db_day / days
    return {
        'days': days,
        'hits': hits,
        'hit_rate': hit_rate,
        'baseline': base,
        'lift_pp': (hit_rate - base) * 100,
        'db_day_rate': db_rate,
        'db_day_baseline': db_base,
        'db_day_lift_pp': (db_rate - db_base) * 100,
        'raw_p': lib.binomial_pvalue_one_sided(hits, days, base),
    }


def main():
    print('Loading rows ...')
    rows = lib.load_rows()
    _, target_index, all_dates = lib.build_indices(rows)
    last_date = max(all_dates)
    targets = ['MN', 'MT', 'MB']

    # Build synthetic source maps
    print('Building synthetic features ...')
    syn_maps = {name: build_synthetic_source(name, fn, all_dates) for name, fn in SYNTHETIC_FEATURES.items()}

    print('Evaluating negative controls ...')
    results = []
    for name, smap in syn_maps.items():
        feature_results = {'feature': name, 'best_per_target': {}, 'best_overall': None,
                           'all_combos': [], 'top10_combos': []}
        all_lifts = []
        for tr in targets:
            best = None
            for window in WINDOWS:
                for lag in LAGS:
                    for wd in [None] + list(range(7)):
                        if wd is not None and window != 180:
                            continue  # weekday only for 180d
                        res = evaluate_negative(target_index, all_dates, last_date, tr, smap, lag, window, weekday=wd)
                        if res is None:
                            continue
                        item = {
                            'target': tr, 'lag': lag, 'window': window, 'weekday': wd,
                            **res,
                        }
                        all_lifts.append(item['lift_pp'])
                        if best is None or item['lift_pp'] > best['lift_pp']:
                            best = item
            feature_results['best_per_target'][tr] = best
        sorted_combos = sorted(all_lifts, reverse=True)
        feature_results['top10_lifts'] = [round(x, 4) for x in sorted_combos[:10]]
        feature_results['median_lift_pp'] = round(sorted(all_lifts)[len(all_lifts) // 2], 4) if all_lifts else 0
        feature_results['mean_lift_pp'] = round(sum(all_lifts) / len(all_lifts), 4) if all_lifts else 0
        feature_results['best_overall_lift_pp'] = round(max(all_lifts), 4) if all_lifts else 0
        results.append(feature_results)
        print(f'  {name}: best_overall_lift = {feature_results["best_overall_lift_pp"]:.2f} pp '
              f'| top10 mean = {sum(sorted_combos[:10])/10:.2f} pp')

    # Real source comparison: read panel data for similar scopes
    panel = json.loads((lib.MR_DIR / 'V107_RULE_PANEL.json').read_text(encoding='utf-8'))
    real_lifts = [r['reported_lift_pp'] for r in panel]
    real_best = max(real_lifts)
    real_top10_mean = sum(sorted(real_lifts, reverse=True)[:10]) / 10

    # Compare median
    syn_best_lifts = [r['best_overall_lift_pp'] for r in results]
    syn_top10_means = [sum(sorted(json.loads(json.dumps(r['top10_lifts'])), reverse=True)[:10]) / 10 for r in results]

    summary = {
        'live_sync_manifest': lib.LOCKED_MANIFEST,
        'real_panel_best_lift_pp': round(real_best, 4),
        'real_panel_top10_mean_lift_pp': round(real_top10_mean, 4),
        'synthetic_features': results,
        'syn_best_lift_max': round(max(syn_best_lifts), 4),
        'syn_best_lift_mean_across_features': round(sum(syn_best_lifts) / len(syn_best_lifts), 4),
        'verdict': 'FAIL_STOPPING_CRITERION' if max(syn_best_lifts) >= real_best else 'PASS',
        'note': (
            'Negative control compares synthetic deterministic features (no real lottery '
            'connection) against the real-source V106.06 panel. If a synthetic feature '
            'achieves lift >= real best, framework is rewarding noise. '
            'Stopping criterion: max(syn_best_lift) >= real_best -> FAIL.'
        ),
    }
    OUT_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2, default=str), encoding='utf-8')
    print(f'\nReal panel best lift = {real_best:.2f} pp')
    print(f'Synthetic max best lift = {max(syn_best_lifts):.2f} pp')
    print(f'Verdict = {summary["verdict"]}')


if __name__ == '__main__':
    main()
