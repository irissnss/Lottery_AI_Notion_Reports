"""Null Test 3: Retroactive Bonferroni + BH q-value correction on V106.05/V106.06 rules.

For every rule in V106.06 candidates + rejected (= 153,228):
  raw_p = exact binomial P(X>=hits | n=days, p=baseline)
  family_n = count of rules in the same transform-family
  bonferroni_p = min(1, raw_p * family_n)
  bh_q = BH adjusted q within family

Output: machine_readable/V107_NULL3_CORRECTION.json + V107_NULL3_RULES.csv
"""
from __future__ import annotations

import csv
import json
import math
from collections import defaultdict, Counter
from pathlib import Path

import _v107_lib as lib

ROOT = lib.ROOT
SRC_ACC = ROOT / 'artifacts' / 'v106_06_deep_source_rule_discovery' / 'deep_source_rule_candidates.csv'
SRC_REJ = ROOT / 'artifacts' / 'v106_06_deep_source_rule_discovery' / 'rejected_rules.csv'
OUT_JSON = lib.MR_DIR / 'V107_NULL3_CORRECTION.json'
OUT_CSV = lib.MR_DIR / 'V107_NULL3_RULES.csv'


def fast_binom_p(k, n, p):
    if n <= 0 or k <= 0:
        return 1.0
    if p <= 0:
        return 0.0 if k > 0 else 1.0
    if p >= 1:
        return 1.0 if k <= n else 0.0
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    if n * p > 10 and n * (1 - p) > 10:
        z = (k - 0.5 - mu) / sigma
        # P(X >= k) = 1 - Phi(z)
        return 0.5 * math.erfc(z / math.sqrt(2))
    return lib.binomial_pvalue_one_sided(k, n, p)


def load_rules(path, has_reject=False):
    rows = []
    with path.open(encoding='utf-8') as f:
        rd = csv.DictReader(f)
        for r in rd:
            try:
                hits = int(r['hits'])
                days = int(r['days'])
                baseline = float(r['hit_baseline'])
            except Exception:
                continue
            r['hits'] = hits
            r['days'] = days
            r['hit_baseline'] = baseline
            r['hit_lift_pp'] = float(r['hit_lift_pp'])
            r['db_day_lift_pp'] = float(r['db_day_lift_pp'])
            r['raw_p'] = fast_binom_p(hits, days, baseline)
            r['_status'] = 'accepted'
            if has_reject:
                r['_status'] = 'rejected'
                r['reject_reason'] = r.get('reject_reason', '')
            rows.append(r)
    return rows


def main():
    print('Loading V106.06 rules ...')
    accepted = load_rules(SRC_ACC, has_reject=False)
    rejected = load_rules(SRC_REJ, has_reject=True)
    all_rules = accepted + rejected
    print(f'  accepted={len(accepted)}, rejected={len(rejected)}, total={len(all_rules)}')

    # family_n per transform family
    family_counts = Counter(r['family'] for r in all_rules)
    print('Family counts:', dict(family_counts))

    # BH within family
    by_family = defaultdict(list)
    for r in all_rules:
        by_family[r['family']].append(r)
    for fam, lst in by_family.items():
        ps = [r['raw_p'] for r in lst]
        qs = lib.benjamini_hochberg(ps)
        for r, q in zip(lst, qs):
            r['bh_q'] = q
            r['family_n'] = len(lst)
            r['bonferroni_p'] = min(1.0, r['raw_p'] * len(lst))
            r['bonferroni_p_full'] = min(1.0, r['raw_p'] * len(all_rules))

    # Survivors at q<0.05 within family
    survivors_q05 = [r for r in all_rules if r['bh_q'] < 0.05]
    survivors_q01 = [r for r in all_rules if r['bh_q'] < 0.01]
    survivors_bonferroni = [r for r in all_rules if r['bonferroni_p'] < 0.05]
    survivors_bonferroni_full = [r for r in all_rules if r['bonferroni_p_full'] < 0.05]

    # Top 50 panel V107 rule mapping with BH/Bonferroni
    panel = json.loads((lib.MR_DIR / 'V107_RULE_PANEL.json').read_text(encoding='utf-8'))
    panel_keys = set()
    for r in panel:
        panel_keys.add((
            r['target_region'], r['source_region'], r['source_unit'], r['source_prize'],
            int(r['source_index']), r['transform'], int(r['lag']), int(r['window']),
            '' if r['weekday'] is None else str(r['weekday']),
            'ALL' if r['station_set'] is None else '|'.join(r['station_set'])
        ))
    panel_results = []
    for r in all_rules:
        key = (
            r['target_region'], r['source_region'], r['source_unit'], r['source_prize'],
            int(r['source_index']), r['transform'], int(r['lag']), int(r['window']),
            r['weekday'], r['station_set']
        )
        if key in panel_keys:
            panel_results.append({
                'rule_key': r['rule_key'],
                'target': r['target_region'],
                'axis': r['axis'],
                'window': r['window'],
                'weekday': r['weekday'],
                'station_set': r['station_set'],
                'tier_v106': r['tier'] if 'tier' in r else '',
                'days': r['days'],
                'hits': r['hits'],
                'hit_lift_pp': r['hit_lift_pp'],
                'baseline': r['hit_baseline'],
                'raw_p': r['raw_p'],
                'family': r['family'],
                'family_n': r['family_n'],
                'bonferroni_p': r['bonferroni_p'],
                'bonferroni_p_full': r['bonferroni_p_full'],
                'bh_q': r['bh_q'],
                'survives_q05': r['bh_q'] < 0.05,
                'survives_q01': r['bh_q'] < 0.01,
                'survives_bonferroni': r['bonferroni_p'] < 0.05,
                'survives_bonferroni_full': r['bonferroni_p_full'] < 0.05,
                'status': r['_status'],
            })

    # Family-level survivor breakdown
    fam_survivors = defaultdict(lambda: {'n_total': 0, 'n_q05': 0, 'n_q01': 0, 'n_bonferroni': 0})
    for r in all_rules:
        fs = fam_survivors[r['family']]
        fs['n_total'] += 1
        if r['bh_q'] < 0.05:
            fs['n_q05'] += 1
        if r['bh_q'] < 0.01:
            fs['n_q01'] += 1
        if r['bonferroni_p'] < 0.05:
            fs['n_bonferroni'] += 1

    summary = {
        'live_sync_manifest': lib.LOCKED_MANIFEST,
        'total_rules': len(all_rules),
        'accepted_rules': len(accepted),
        'rejected_rules': len(rejected),
        'family_counts': dict(family_counts),
        'family_survivor_breakdown': {k: v for k, v in fam_survivors.items()},
        'survivors': {
            'bh_q05': len(survivors_q05),
            'bh_q01': len(survivors_q01),
            'bonferroni_within_family_p05': len(survivors_bonferroni),
            'bonferroni_full_p05': len(survivors_bonferroni_full),
        },
        'panel_results_size': len(panel_results),
        'panel_results_top30_by_bh_q': sorted(panel_results, key=lambda r: r['bh_q'])[:30],
        'verdict': (
            'PASS_HAS_SURVIVORS' if len(survivors_q05) > 0 else 'FAIL_NO_SURVIVORS'
        ),
        'note': (
            'BH and Bonferroni adjusted for multiple testing within family. '
            'Family-level survivor count = rules whose adjusted q < 0.05. '
            'Bonferroni full = adjusted across all 153228 hypotheses (most conservative).'
        ),
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2, default=str), encoding='utf-8')

    # Write per-rule CSV (panel only for size control)
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        keys = ['rule_key', 'target', 'axis', 'window', 'weekday', 'station_set', 'tier_v106',
                'days', 'hits', 'hit_lift_pp', 'baseline', 'raw_p', 'family', 'family_n',
                'bonferroni_p', 'bonferroni_p_full', 'bh_q',
                'survives_q05', 'survives_q01', 'survives_bonferroni', 'survives_bonferroni_full',
                'status']
        wr = csv.DictWriter(f, fieldnames=keys)
        wr.writeheader()
        for r in sorted(panel_results, key=lambda r: r['bh_q']):
            wr.writerow({k: r.get(k, '') for k in keys})

    print(f'\nTotal hypotheses: {len(all_rules)}')
    print(f'Survivors at BH q<0.05: {len(survivors_q05)}')
    print(f'Survivors at BH q<0.01: {len(survivors_q01)}')
    print(f'Survivors Bonferroni within family p<0.05: {len(survivors_bonferroni)}')
    print(f'Survivors Bonferroni full (all 153k) p<0.05: {len(survivors_bonferroni_full)}')
    print(f'Panel survivors q<0.05: {sum(1 for r in panel_results if r["survives_q05"])}/{len(panel_results)}')
    print(f'Verdict = {summary["verdict"]}')
    print(f'Wrote {OUT_JSON} and {OUT_CSV}')


if __name__ == '__main__':
    main()
