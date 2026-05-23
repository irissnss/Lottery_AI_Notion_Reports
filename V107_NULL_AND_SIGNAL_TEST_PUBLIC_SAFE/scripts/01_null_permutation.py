"""Null Test 1: Permutation test on V107 rule panel.

Approach:
- Shuffle target_date <-> (all_set, db_unique) mapping within last 365 days,
  keeping source-side fixed.
- Re-evaluate all panel rules under the shuffle.
- Record best_lift across panel per permutation.
- Compare to real best_lift -> empirical p-value.

Output: machine_readable/V107_NULL1_PERMUTATION.json
"""
from __future__ import annotations

import json
import random
import time
from datetime import timedelta
from pathlib import Path

import _v107_lib as lib

PANEL_PATH = lib.MR_DIR / 'V107_RULE_PANEL.json'
OUT_PATH = lib.MR_DIR / 'V107_NULL1_PERMUTATION.json'
N_PERMUTATIONS = 500
PERM_WINDOW_DAYS = 365  # Restrict to last year for realistic distribution
SEED = 20260524

random.seed(SEED)


def main():
    print('Loading rows ...')
    rows = lib.load_rows()
    print(f'  rows = {len(rows)}')
    print('Building indices ...')
    source_index, target_index, all_dates = lib.build_indices(rows)
    last_date = max(all_dates)
    print(f'  last_date = {last_date}')
    panel = json.loads(PANEL_PATH.read_text(encoding='utf-8'))
    print(f'  panel size = {len(panel)}')

    # Group target dates by region within last 365 days
    region_dates_in_window = {tr: [] for tr in ('MN', 'MT', 'MB')}
    perm_start = last_date - timedelta(days=PERM_WINDOW_DAYS - 1)
    for (dt, tr), v in target_index.items():
        if perm_start <= dt <= last_date and v['all_set']:
            region_dates_in_window[tr].append(dt)
    for tr in region_dates_in_window:
        region_dates_in_window[tr].sort()
    region_dates_count = {tr: len(v) for tr, v in region_dates_in_window.items()}
    print(f'  region target dates in {PERM_WINDOW_DAYS}d: {region_dates_count}')

    # Pre-compute per rule: (target_dates_used, source_tail_each, all_set_baseline)
    # within rule's window and scope.
    print('Pre-computing rule trajectories ...')
    rule_trajectories = []
    real_lifts = []
    for r in panel:
        target_region = r['target_region']
        window = r['window']
        weekday = r['weekday']
        station_set = r['station_set']
        if station_set is not None:
            station_set = tuple(station_set)
        start = last_date - timedelta(days=window - 1)
        traj = []
        for td in region_dates_in_window[target_region]:
            if td < start or td > last_date:
                continue
            if weekday is not None and td.weekday() != weekday:
                continue
            tgt = target_index.get((td, target_region))
            if not tgt:
                continue
            if station_set is not None and tgt['stations'] != station_set:
                continue
            sd = td - timedelta(days=r['lag'])
            src = source_index.get((sd, r['source_region'], r['source_unit'],
                                    r['source_prize'], r['source_index'], r['transform']))
            if not src:
                continue
            traj.append((td, src['tail']))
        rule_trajectories.append(traj)
        # Real lift
        if traj:
            hits = sum(1 for td, t in traj if t in target_index[(td, target_region)]['all_set'])
            base = sum(len(target_index[(td, target_region)]['all_set']) / 100 for td, _ in traj) / len(traj)
            real_lifts.append((hits / len(traj) - base) * 100)
        else:
            real_lifts.append(0.0)

    real_best_lift = max(real_lifts)
    real_top10_lift = sorted(real_lifts, reverse=True)[:10]
    print(f'  real best_lift = {real_best_lift:.2f} pp; top-10 mean = {sum(real_top10_lift)/10:.2f} pp')

    # Build permuted target lookup: per region, a list of (idx -> all_set)
    region_target_pool = {}
    for tr in ('MN', 'MT', 'MB'):
        region_target_pool[tr] = [target_index[(td, tr)]['all_set'] for td in region_dates_in_window[tr]]

    # Pre-compute, for each rule, the date_index_in_region of each traj target_date
    region_date_to_idx = {tr: {td: i for i, td in enumerate(region_dates_in_window[tr])}
                         for tr in region_dates_in_window}
    rule_date_indices = []
    for r, traj in zip(panel, rule_trajectories):
        tr = r['target_region']
        idx_list = []
        for td, t in traj:
            if td in region_date_to_idx[tr]:
                idx_list.append((region_date_to_idx[tr][td], t))
        rule_date_indices.append((tr, idx_list))

    print(f'Running {N_PERMUTATIONS} permutations ...')
    start_t = time.time()
    perm_best_lifts = []
    perm_topmean_lifts = []
    ge_real_best = 0
    ge_real_topmean = 0
    for perm in range(N_PERMUTATIONS):
        # Build shuffled mapping per region
        shuffled = {}
        for tr in ('MN', 'MT', 'MB'):
            n = len(region_target_pool[tr])
            perm_idx = list(range(n))
            random.shuffle(perm_idx)
            # shuffled[tr][i] = all_set originally at index perm_idx[i]
            shuffled[tr] = perm_idx
        # Compute lift per rule under shuffle
        lifts = []
        for (tr, idx_list), real_l in zip(rule_date_indices, real_lifts):
            if not idx_list:
                lifts.append(0.0)
                continue
            sh = shuffled[tr]
            pool = region_target_pool[tr]
            hits = 0
            base_sum = 0.0
            for date_idx, tail in idx_list:
                # Substitute target tails at date_idx with the all_set originally located at sh[date_idx]
                target_set = pool[sh[date_idx]]
                if tail in target_set:
                    hits += 1
                base_sum += len(target_set) / 100
            n = len(idx_list)
            lift = (hits / n - base_sum / n) * 100
            lifts.append(lift)
        best = max(lifts)
        topmean = sum(sorted(lifts, reverse=True)[:10]) / 10
        perm_best_lifts.append(best)
        perm_topmean_lifts.append(topmean)
        if best >= real_best_lift:
            ge_real_best += 1
        if topmean >= sum(real_top10_lift) / 10:
            ge_real_topmean += 1
        if (perm + 1) % 50 == 0:
            elapsed = time.time() - start_t
            print(f'  perm {perm+1}/{N_PERMUTATIONS} elapsed={elapsed:.1f}s')

    p_best = ge_real_best / N_PERMUTATIONS
    p_topmean = ge_real_topmean / N_PERMUTATIONS
    perm_best_lifts.sort()
    summary = {
        'live_sync_manifest': lib.LOCKED_MANIFEST,
        'panel_size': len(panel),
        'n_permutations': N_PERMUTATIONS,
        'permutation_window_days': PERM_WINDOW_DAYS,
        'seed': SEED,
        'real_best_lift_pp': round(real_best_lift, 4),
        'real_top10_mean_lift_pp': round(sum(real_top10_lift) / 10, 4),
        'permuted_best_lift_distribution': {
            'min': round(min(perm_best_lifts), 4),
            'p05': round(perm_best_lifts[int(0.05 * len(perm_best_lifts))], 4),
            'p25': round(perm_best_lifts[int(0.25 * len(perm_best_lifts))], 4),
            'median': round(perm_best_lifts[len(perm_best_lifts) // 2], 4),
            'mean': round(sum(perm_best_lifts) / len(perm_best_lifts), 4),
            'p75': round(perm_best_lifts[int(0.75 * len(perm_best_lifts))], 4),
            'p95': round(perm_best_lifts[int(0.95 * len(perm_best_lifts))], 4),
            'max': round(max(perm_best_lifts), 4),
        },
        'p_empirical_best_lift': p_best,
        'p_empirical_top10_mean': p_topmean,
        'verdict': 'PASS' if p_best <= 0.20 else 'FAIL_STOPPING_CRITERION',
        'note': (
            'Permutation shuffles target-date <-> target-tail mapping within last 365 days, '
            'keeping source side fixed. Tracks best_lift across the V107 panel. '
            'Stopping criterion: p_empirical > 0.20 -> FAIL.'
        ),
    }
    OUT_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'\nWrote {OUT_PATH}')
    print(f'real_best_lift = {real_best_lift:.2f} pp')
    print(f'permuted best_lift mean = {summary["permuted_best_lift_distribution"]["mean"]:.2f} pp')
    print(f'permuted best_lift p95 = {summary["permuted_best_lift_distribution"]["p95"]:.2f} pp')
    print(f'p_empirical_best_lift = {p_best:.4f}')
    print(f'p_empirical_top10_mean = {p_topmean:.4f}')
    print(f'verdict = {summary["verdict"]}')


if __name__ == '__main__':
    main()
