"""V107 Family A (within-region positional autocorrelation) + Family D (reverse causality).

Family A: For each (region, source_unit, prize, index), test self-lag autocorrelation
  on LAST2 transform: tail at d vs tail at d-k for k in {1,7,14,30,7,14,28}.
  If RNG is clean, lift ≈ 0.

Family D: For top 20 V107 panel rules of form "X D-k -> Y D", reverse to
  "Y D -> X D+k". If reverse_lift ≈ forward_lift, the rule is contemporaneous
  artifact, not predictive.

Output: machine_readable/V107_FAMILY_A.json + V107_FAMILY_D.json
"""
from __future__ import annotations

import csv
import json
from datetime import timedelta
from pathlib import Path

import _v107_lib as lib

OUT_A = lib.MR_DIR / 'V107_FAMILY_A_AUTOCORR.json'
OUT_D = lib.MR_DIR / 'V107_FAMILY_D_REVERSE_CAUSALITY.json'


def family_A():
    print('FAMILY A: within-region positional autocorrelation')
    rows = lib.load_rows()
    source_index, target_index, all_dates = lib.build_indices(rows)
    last_date = max(all_dates)
    self_lags = [1, 7, 14, 28, 30]
    window = 180
    results = []
    for tr in ['MN', 'MT', 'MB']:
        for prize in ['DB', 'G1', 'G2']:
            for idx in (1, 2):
                if prize != 'G2' and idx != 1:
                    continue
                # source_unit = MB_BOARD for MB, station for MN/MT — for autocorrelation we evaluate
                # against same region target's all_set on day d for source unit's tail at day d-k.
                # We test using LAST2 transform.
                # Sample multiple stations for MN/MT — pick top frequent units
                if tr == 'MB':
                    units = ['MB_BOARD']
                else:
                    # take top 6 stations by appearance in source_index
                    counter = {}
                    for (dt, region, unit, p_, idx_, tr_) in source_index.keys():
                        if region == tr and p_ == prize and idx_ == idx and tr_ == 'LAST2':
                            counter[unit] = counter.get(unit, 0) + 1
                    units = [u for u, _ in sorted(counter.items(), key=lambda x: -x[1])[:6]]
                for unit in units:
                    for lag in self_lags:
                        res = lib.evaluate_rule(
                            target_index, source_index, all_dates, last_date,
                            target_region=tr, source_region=tr, source_unit=unit,
                            source_prize=prize, source_idx=idx, transform='LAST2',
                            lag=lag, window=window
                        )
                        if not res:
                            continue
                        results.append({
                            'target': tr, 'source_region': tr, 'source_unit': unit,
                            'source_prize': prize, 'source_index': idx,
                            'transform': 'LAST2', 'lag': lag, 'window': window,
                            'days': res['days'],
                            'hit_rate': round(res['hit_rate'], 4),
                            'baseline': round(res['baseline'], 4),
                            'lift_pp': round(res['lift_pp'], 3),
                            'db_day_lift_pp': round(res['db_day_lift_pp'], 3),
                            'raw_p': res['raw_p'],
                        })
    # Aggregate stats
    lifts = [r['lift_pp'] for r in results]
    summary = {
        'live_sync_manifest': lib.LOCKED_MANIFEST,
        'description': (
            'Family A: within-region positional autocorrelation. '
            'For each (region, station/MB_BOARD, prize, index, LAST2), test self-lag '
            'in {1,7,14,28,30} day. If lottery RNG is clean, mean lift_pp should ≈ 0.'
        ),
        'n_tests': len(results),
        'mean_lift_pp': round(sum(lifts) / len(lifts), 3) if lifts else 0,
        'median_lift_pp': round(sorted(lifts)[len(lifts) // 2], 3) if lifts else 0,
        'max_lift_pp': round(max(lifts), 3) if lifts else 0,
        'min_lift_pp': round(min(lifts), 3) if lifts else 0,
        'pct_lift_positive': round(sum(1 for x in lifts if x > 0) / len(lifts), 4) if lifts else 0,
        'pct_lift_above_5pp': round(sum(1 for x in lifts if x > 5) / len(lifts), 4) if lifts else 0,
        'verdict': 'NORMAL_RNG' if abs(sum(lifts) / len(lifts)) < 1.5 else 'POTENTIAL_BIAS',
        'top_10_by_lift': sorted(results, key=lambda r: -r['lift_pp'])[:10],
        'bottom_10_by_lift': sorted(results, key=lambda r: r['lift_pp'])[:10],
    }
    OUT_A.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'  n_tests={len(results)}')
    print(f'  mean_lift_pp = {summary["mean_lift_pp"]}')
    print(f'  median_lift_pp = {summary["median_lift_pp"]}')
    print(f'  max_lift_pp = {summary["max_lift_pp"]}')
    print(f'  min_lift_pp = {summary["min_lift_pp"]}')
    print(f'  verdict = {summary["verdict"]}')


def family_D():
    print('FAMILY D: reverse causality on top V107 panel rules')
    rows = lib.load_rows()
    source_index, target_index, all_dates = lib.build_indices(rows)
    last_date = max(all_dates)
    panel = json.loads((lib.MR_DIR / 'V107_RULE_PANEL.json').read_text(encoding='utf-8'))
    panel.sort(key=lambda r: -r['reported_score'])
    top20 = panel[:20]

    out_rows = []
    for r in top20:
        ws = tuple(r['station_set']) if r['station_set'] else None
        # Forward: source@(td-lag) -> target@td
        forward = lib.evaluate_rule(
            target_index, source_index, all_dates, last_date,
            target_region=r['target_region'], source_region=r['source_region'],
            source_unit=r['source_unit'], source_prize=r['source_prize'],
            source_idx=r['source_index'], transform=r['transform'],
            lag=r['lag'], window=r['window'],
            weekday=r['weekday'], station_set=ws,
        )

        # Reverse: target@(sd-lag) -> source@sd  (i.e., target's tails at d vs source's tails at d+lag)
        # Implementation: swap target/source, swap target_region/source_region, swap units etc.
        # Use the source as target (look up its tail set) and use target's all_set as source.
        # But target side is "all tails of region", which doesn't have a single tail per source role.
        # Alternative reverse: compute lift where target is at td and source is shifted by +lag instead of -lag.
        # = swap: source_index[(td+lag, source_region, ...)] -> target_index[(td, target_region)]
        days = 0
        hits = 0
        sum_target = 0
        for td in all_dates:
            start = last_date - timedelta(days=r['window'] - 1)
            if td < start or td > last_date:
                continue
            if r['weekday'] is not None and td.weekday() != r['weekday']:
                continue
            tgt = target_index.get((td, r['target_region']))
            if not tgt or not tgt['all_set']:
                continue
            if ws is not None and tgt['stations'] != ws:
                continue
            # Reverse: source at td+lag (future)
            sd = td + timedelta(days=r['lag'])
            src = source_index.get((sd, r['source_region'], r['source_unit'],
                                    r['source_prize'], r['source_index'], r['transform']))
            if not src:
                continue
            days += 1
            t = src['tail']
            if t in tgt['all_set']:
                hits += 1
            sum_target += len(tgt['all_set'])
        reverse_lift = ((hits / days) - (sum_target / 100 / days)) * 100 if days else None
        reverse_days = days

        out_rows.append({
            'rule_lineage': f"{r['source_region']}:{r['source_unit']}:{r['source_prize']}#{r['source_index']}:{r['transform']}",
            'target': r['target_region'],
            'lag': r['lag'],
            'window': r['window'],
            'tier_v106': r['tier'],
            'forward_lift_pp': forward['lift_pp'] if forward else None,
            'forward_days': forward['days'] if forward else 0,
            'reverse_lift_pp': reverse_lift,
            'reverse_days': reverse_days,
            'reverse_minus_forward_pp': (reverse_lift - forward['lift_pp']) if (reverse_lift is not None and forward) else None,
        })

    diffs = [r['reverse_minus_forward_pp'] for r in out_rows if r['reverse_minus_forward_pp'] is not None]
    summary = {
        'live_sync_manifest': lib.LOCKED_MANIFEST,
        'description': (
            'Family D: reverse causality test. For each top V107 panel rule '
            '(source X at d-lag predicts target Y at d), test reverse: source X at d+lag '
            'against target Y at d (future-source). If reverse_lift is similar to '
            'forward_lift, the rule captures contemporaneous correlation and is NOT '
            'truly predictive.'
        ),
        'n_rules': len(out_rows),
        'mean_forward_lift_pp': round(sum(r['forward_lift_pp'] for r in out_rows) / len(out_rows), 3) if out_rows else 0,
        'mean_reverse_lift_pp': round(sum(r['reverse_lift_pp'] for r in out_rows if r['reverse_lift_pp'] is not None) / max(1, len([r for r in out_rows if r['reverse_lift_pp'] is not None])), 3),
        'mean_reverse_minus_forward_pp': round(sum(diffs) / len(diffs), 3) if diffs else 0,
        'pct_reverse_lift_positive': round(sum(1 for r in out_rows if r['reverse_lift_pp'] is not None and r['reverse_lift_pp'] > 0) / len(out_rows), 4),
        'rules': out_rows,
        'verdict': (
            'PREDICTIVE_LIKE' if (sum(diffs) / len(diffs) if diffs else 0) < -3 else
            'CONTEMPORANEOUS_LIKE' if abs(sum(diffs) / len(diffs) if diffs else 0) < 3 else
            'INVERSE_PATTERN'
        ),
    }
    OUT_D.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'  n_rules = {len(out_rows)}')
    print(f'  mean forward_lift = {summary["mean_forward_lift_pp"]}')
    print(f'  mean reverse_lift = {summary["mean_reverse_lift_pp"]}')
    print(f'  mean (reverse - forward) = {summary["mean_reverse_minus_forward_pp"]} pp')
    print(f'  verdict = {summary["verdict"]}')


def main():
    family_A()
    print()
    family_D()


if __name__ == '__main__':
    main()
