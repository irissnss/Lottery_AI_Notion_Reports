"""Null Test 4: Sub-sample replication (odd-DOY vs even-DOY).

For each rule in V107 panel, compute lift on:
  - odd_doy days only (within last 180d)
  - even_doy days only (within last 180d)
Intersect: rules with lift >= +15 pp in BOTH halves.
Random expectation under no-signal: ~ 1/(2*2) = 25% (depends on selection).

Output: machine_readable/V107_NULL4_SUBSAMPLE.json + V107_NULL4_RULES.csv
"""
from __future__ import annotations

import csv
import json
from datetime import timedelta
from pathlib import Path

import _v107_lib as lib

OUT_JSON = lib.MR_DIR / 'V107_NULL4_SUBSAMPLE.json'
OUT_CSV = lib.MR_DIR / 'V107_NULL4_RULES.csv'
LIFT_THRESHOLD = 15.0
WINDOW_DAYS = 180


def evaluate_with_doy_filter(target_index, source_index, all_dates, last_date,
                             rule, doy_parity):
    start = last_date - timedelta(days=WINDOW_DAYS - 1)
    days = 0
    hits = 0
    sum_target = 0
    sum_db = 0
    db_day = 0
    for td in all_dates:
        if td < start or td > last_date:
            continue
        if td.timetuple().tm_yday % 2 != doy_parity:
            continue
        weekday = rule['weekday']
        station_set = rule['station_set']
        if station_set is not None:
            station_set = tuple(station_set)
        if weekday is not None and td.weekday() != weekday:
            continue
        tgt = target_index.get((td, rule['target_region']))
        if not tgt:
            continue
        if station_set is not None and tgt['stations'] != station_set:
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
    }


def main():
    print('Loading rows ...')
    rows = lib.load_rows()
    source_index, target_index, all_dates = lib.build_indices(rows)
    last_date = max(all_dates)
    panel = json.loads((lib.MR_DIR / 'V107_RULE_PANEL.json').read_text(encoding='utf-8'))
    print(f'  panel size = {len(panel)}')

    out_rows = []
    n_pass_threshold_odd = 0
    n_pass_threshold_even = 0
    n_pass_both = 0
    for r in panel:
        odd = evaluate_with_doy_filter(target_index, source_index, all_dates, last_date, r, doy_parity=1)
        even = evaluate_with_doy_filter(target_index, source_index, all_dates, last_date, r, doy_parity=0)
        if odd is None or even is None:
            continue
        if odd['days'] < 8 or even['days'] < 8:
            continue
        odd_pass = odd['lift_pp'] >= LIFT_THRESHOLD
        even_pass = even['lift_pp'] >= LIFT_THRESHOLD
        n_pass_threshold_odd += int(odd_pass)
        n_pass_threshold_even += int(even_pass)
        if odd_pass and even_pass:
            n_pass_both += 1
        out_rows.append({
            'target': r['target_region'],
            'source_region': r['source_region'],
            'source_unit': r['source_unit'],
            'source_prize': r['source_prize'],
            'source_index': r['source_index'],
            'transform': r['transform'],
            'lag': r['lag'],
            'window': r['window'],
            'weekday': r['weekday'] if r['weekday'] is not None else '',
            'station_set': '|'.join(r['station_set']) if r['station_set'] else 'ALL',
            'tier_v106': r['tier'],
            'reported_lift_pp': r['reported_lift_pp'],
            'odd_days': odd['days'],
            'odd_lift_pp': odd['lift_pp'],
            'odd_db_lift_pp': odd['db_day_lift_pp'],
            'odd_pass15': odd_pass,
            'even_days': even['days'],
            'even_lift_pp': even['lift_pp'],
            'even_db_lift_pp': even['db_day_lift_pp'],
            'even_pass15': even_pass,
            'replicated': odd_pass and even_pass,
        })

    n_total = len(out_rows)
    rate_odd = n_pass_threshold_odd / n_total if n_total else 0
    rate_even = n_pass_threshold_even / n_total if n_total else 0
    rate_both = n_pass_both / n_total if n_total else 0
    expected_independent = rate_odd * rate_even

    summary = {
        'live_sync_manifest': lib.LOCKED_MANIFEST,
        'lift_threshold_pp': LIFT_THRESHOLD,
        'window_days': WINDOW_DAYS,
        'n_panel_evaluated': n_total,
        'n_pass_odd_only': n_pass_threshold_odd,
        'n_pass_even_only': n_pass_threshold_even,
        'n_pass_both_halves': n_pass_both,
        'rate_odd_pass15': round(rate_odd, 4),
        'rate_even_pass15': round(rate_even, 4),
        'rate_both_observed': round(rate_both, 4),
        'rate_both_expected_under_independence': round(expected_independent, 4),
        'replication_excess': round(rate_both - expected_independent, 4),
        'verdict': (
            'PASS_REPLICATES_ABOVE_INDEPENDENCE' if rate_both > 1.5 * expected_independent
            else 'INCONCLUSIVE' if rate_both >= expected_independent
            else 'FAIL_REPLICATION_BELOW_INDEPENDENCE'
        ),
        'note': (
            'Rule replicates if lift_pp >= +15 in BOTH odd-DOY and even-DOY halves of last 180d. '
            'Under no signal, replication rate ≈ rate_odd × rate_even (independence). '
            'PASS if observed > 1.5× expected.'
        ),
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2, default=str), encoding='utf-8')

    keys = list(out_rows[0].keys()) if out_rows else []
    if out_rows:
        with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
            wr = csv.DictWriter(f, fieldnames=keys)
            wr.writeheader()
            for r in sorted(out_rows, key=lambda r: -((r['odd_lift_pp'] + r['even_lift_pp']) / 2)):
                wr.writerow(r)

    print(f'\nPanel evaluated: {n_total}')
    print(f'Pass odd >=+15: {n_pass_threshold_odd} ({rate_odd*100:.1f}%)')
    print(f'Pass even >=+15: {n_pass_threshold_even} ({rate_even*100:.1f}%)')
    print(f'Pass BOTH: {n_pass_both} ({rate_both*100:.1f}%)')
    print(f'Expected under independence: {expected_independent*100:.2f}%')
    print(f'Replication excess: {(rate_both - expected_independent)*100:.2f} pp')
    print(f'Verdict: {summary["verdict"]}')


if __name__ == '__main__':
    main()
