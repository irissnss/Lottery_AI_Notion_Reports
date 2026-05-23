"""Select a representative panel of V106.05 / V106.06 rules to use as fixed test set.

Output: machine_readable/V107_RULE_PANEL.json
Each entry: source_region, source_unit, source_prize, source_index, transform,
            lag, window, weekday, station_set (None|tuple), target_region.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
V10606_CSV = ROOT / 'artifacts' / 'v106_06_deep_source_rule_discovery' / 'deep_source_rule_candidates.csv'
OUT = ROOT / 'artifacts' / 'v107_null_and_signal_test' / 'machine_readable' / 'V107_RULE_PANEL.json'
OUT.parent.mkdir(parents=True, exist_ok=True)


def main():
    rows = list(csv.DictReader(V10606_CSV.open(encoding='utf-8')))
    panel = []
    seen = set()

    def push(r):
        key = (
            r['target_region'], r['source_region'], r['source_unit'], r['source_prize'],
            r['source_index'], r['transform'], r['lag'], r['window'],
            r['weekday'], r['station_set']
        )
        if key in seen:
            return
        seen.add(key)
        ws = None if r['station_set'] == 'ALL' else tuple(r['station_set'].split('|'))
        wd = None if r['weekday'] == '' else int(r['weekday'])
        panel.append({
            'target_region': r['target_region'],
            'source_region': r['source_region'],
            'source_unit': r['source_unit'],
            'source_prize': r['source_prize'],
            'source_index': int(r['source_index']),
            'transform': r['transform'],
            'lag': int(r['lag']),
            'window': int(r['window']),
            'weekday': wd,
            'station_set': ws,
            'tier': r['tier'],
            'family': r['family'],
            'reported_lift_pp': float(r['hit_lift_pp']),
            'reported_db_day_lift_pp': float(r['db_day_lift_pp']),
            'reported_days': int(r['days']),
            'reported_score': float(r['score']),
        })

    # Take per-target Tier A top 60 + Tier B top 80 + Tier C top 40 globally and scoped
    by_target_tier = {}
    for r in rows:
        by_target_tier.setdefault((r['target_region'], r['tier']), []).append(r)
    for (tr, tier), lst in by_target_tier.items():
        if tier not in ('A', 'B', 'C'):
            continue
        # Sort by score desc
        lst.sort(key=lambda r: -float(r['score']))
        cap = {'A': 60, 'B': 80, 'C': 40}[tier]
        for r in lst[:cap]:
            push(r)

    # Add the explicit V106.05 owner-mentioned rules to ensure traceability
    extra_keys = [
        ('MT', 'MB', 'MB_BOARD', 'G2', 1, 'P4P1', 1, 90, '', 'ALL'),
        ('MT', 'MB', 'MB_BOARD', 'G1', 1, 'P5P2', 1, 90, '', 'ALL'),
        ('MT', 'MB', 'MB_BOARD', 'G2', 1, 'LAST2', 2, 180, '6', 'Quảng Ngãi|Đà Nẵng|Đắk Nông'),
        ('MT', 'MB', 'MB_BOARD', 'G2', 1, 'P4P3', 1, 180, '3', 'Bình Định|Quảng Bình|Quảng Trị'),
        ('MT', 'MB', 'MB_BOARD', 'DB', 1, 'P2P4', 1, 180, '6', 'ALL'),
    ]
    by_full = {}
    for r in rows:
        by_full[(
            r['target_region'], r['source_region'], r['source_unit'], r['source_prize'],
            int(r['source_index']), r['transform'], int(r['lag']), int(r['window']),
            r['weekday'], r['station_set']
        )] = r
    for k in extra_keys:
        if k in by_full:
            push(by_full[k])

    OUT.write_text(json.dumps(panel, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Panel size = {len(panel)} -> {OUT}')


if __name__ == '__main__':
    main()
