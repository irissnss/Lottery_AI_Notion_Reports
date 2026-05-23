"""V107 shared library: locked-manifest loaders + transforms + baseline.

Hard rules (governance):
- Live snapshot manifest LOCKED to one path.
- No DB / jsonl / log committed to public.
- No official mutation. No provider call.
- No broad selectors as boost rules.
"""
from __future__ import annotations

import json
import math
import re
import sqlite3
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DB_PATH = ROOT / 'data' / 'lottery_ai.db'
LOCKED_MANIFEST = 'artifacts/live_sync/20260523_233622/manifest.json'
ART_DIR = ROOT / 'artifacts' / 'v107_null_and_signal_test'
MR_DIR = ART_DIR / 'machine_readable'

VN_WEEKDAY = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']

LAGS_DAY = [1, 2, 3, 4, 5, 6, 7]
LAGS_WEEK = [7, 14, 21, 28]

# Source restriction (low-cardinality)
ALLOWED_SOURCE_PRIZES = ('DB#1', 'G1#1', 'G2#1', 'G2#2')


def dparse(s):
    return datetime.strptime(s, '%Y-%m-%d').date()


def digits(x):
    return ''.join(re.findall(r'\d', str(x)))


def tail2(x):
    ds = digits(x)
    return ds[-2:] if len(ds) >= 2 else None


def flatten(x):
    if isinstance(x, dict):
        for v in x.values():
            yield from flatten(v)
    elif isinstance(x, list):
        for v in x:
            yield from flatten(v)
    else:
        yield str(x)


def low_positions_for_region(prizes_json, region):
    obj = json.loads(prizes_json)
    vals = list(obj.values())
    if region == 'MB':
        specs = [('DB', 0, 1), ('G1', 1, 1), ('G2', 2, 1), ('G2', 2, 2)]
    else:
        specs = [('G2', 6, 1), ('G2', 6, 2), ('G1', 7, 1), ('DB', 8, 1)]
    out = []
    for code, idx, sub in specs:
        if idx >= len(vals):
            continue
        arr = vals[idx] if isinstance(vals[idx], list) else [vals[idx]]
        if len(arr) < sub:
            continue
        v = arr[sub - 1]
        ds = digits(v)
        if len(ds) >= 2:
            out.append((f'{code}#{sub}', str(v), ds))
    return out


def transforms_for(ds):
    out = {}
    n = len(ds)

    def add(k, v):
        if v and len(v) == 2:
            out[k] = v

    add('LAST2', ds[-2:])
    if n >= 2:
        add('LAST2_REV', ds[-1] + ds[-2])
        add('FIRST2', ds[:2])
        add('FIRST2_REV', ds[1] + ds[0])
        add('HEAD_TAIL', ds[0] + ds[-1])
        add('TAIL_HEAD', ds[-1] + ds[0])
        if n >= 3:
            add('HEAD_SECOND_LAST', ds[0] + ds[-2])
            add('SECOND_HEAD_TAIL', ds[1] + ds[-1])
    s = sum(int(c) for c in ds)
    unit = s % 10
    add('SUM_LAST2', str(s % 100).zfill(2))
    add('SUM_UNIT_TAIL', f"{unit}{ds[-1]}")
    add('TAIL_SUM_UNIT', f"{ds[-1]}{unit}")
    add('SUM_UNIT_HEAD', f"{unit}{ds[0]}")
    add('HEAD_SUM_UNIT', f"{ds[0]}{unit}")
    for i in range(n):
        for j in range(n):
            if i != j:
                add(f'P{i + 1}P{j + 1}', ds[i] + ds[j])
    return out


def load_rows():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT date, region, station, prizes_json, tail_db FROM lottery_results "
        "WHERE region IN ('MN','MT','MB') ORDER BY date, region, station"
    ).fetchall()
    conn.close()
    return rows


def build_indices(rows):
    """Return source_index, target_index, sorted_dates."""
    source_index = {}
    target_index = defaultdict(lambda: {'all_set': set(), 'dbs': [], 'db_unique': set(), 'stations': []})
    all_dates = set()
    for r in rows:
        dt = dparse(r['date'])
        region = r['region']
        unit = 'MB_BOARD' if region == 'MB' else r['station']
        all_dates.add(dt)
        for prize_idx_str, num, ds in low_positions_for_region(r['prizes_json'], region):
            prize, idx_str = prize_idx_str.split('#')
            idx = int(idx_str)
            for tr_name, val in transforms_for(ds).items():
                source_index[(dt, region, unit, prize, idx, tr_name)] = {'tail': val, 'num': num}
        obj = json.loads(r['prizes_json'])
        for v in flatten(obj):
            t = tail2(v)
            if t:
                target_index[(dt, region)]['all_set'].add(t)
        db = tail2(r['tail_db']) if r['tail_db'] else None
        if db:
            target_index[(dt, region)]['dbs'].append((r['station'], db))
            target_index[(dt, region)]['db_unique'].add(db)
        target_index[(dt, region)]['stations'].append(r['station'])
        target_index[(dt, region)]['weekday'] = dt.weekday()
    for k, v in target_index.items():
        v['stations'] = tuple(sorted(v['stations']))
    return source_index, target_index, sorted(all_dates)


# ----- Statistics helpers ---------------------------------------------------

def binomial_pvalue_one_sided(k, n, p):
    """One-sided binomial p-value: P(X >= k) when X ~ Binom(n, p)."""
    if n <= 0:
        return 1.0
    if k <= 0:
        return 1.0
    if p <= 0:
        return 0.0 if k > 0 else 1.0
    if p >= 1:
        return 1.0 if k <= n else 0.0
    # Use survival function via log-binomial
    # P(X >= k) = sum_{i=k..n} C(n,i) p^i (1-p)^(n-i)
    # For large n, compute incrementally to avoid overflow
    log_p = math.log(p)
    log_q = math.log(1 - p)
    log_factorials = [0.0] * (n + 1)
    for i in range(1, n + 1):
        log_factorials[i] = log_factorials[i - 1] + math.log(i)

    def log_binom(i):
        return log_factorials[n] - log_factorials[i] - log_factorials[n - i] + i * log_p + (n - i) * log_q

    # logsumexp
    log_terms = [log_binom(i) for i in range(k, n + 1)]
    if not log_terms:
        return 0.0
    m = max(log_terms)
    return math.exp(m + math.log(sum(math.exp(t - m) for t in log_terms)))


def wilson_ci(k, n, alpha=0.05):
    if n == 0:
        return (0.0, 0.0)
    z = 1.959963984540054  # 95% normal
    phat = k / n
    denom = 1 + z * z / n
    centre = phat + z * z / (2 * n)
    half = z * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n))
    lo = (centre - half) / denom
    hi = (centre + half) / denom
    return (max(0.0, lo), min(1.0, hi))


def benjamini_hochberg(pvalues):
    """Return list of BH-adjusted q-values, same length as pvalues."""
    n = len(pvalues)
    if n == 0:
        return []
    indexed = sorted(enumerate(pvalues), key=lambda x: x[1])
    q = [0.0] * n
    cumulative_min = 1.0
    # Walk from largest p to smallest
    for rank in range(n - 1, -1, -1):
        idx, p = indexed[rank]
        adj = p * n / (rank + 1)
        if adj < cumulative_min:
            cumulative_min = adj
        q[idx] = min(1.0, cumulative_min)
    return q


def bonferroni(pvalues, family_n=None):
    n = family_n if family_n is not None else len(pvalues)
    return [min(1.0, p * n) for p in pvalues]


def family_of(tr):
    if tr in ('LAST2', 'LAST2_REV'):
        return 'tail'
    if tr in ('FIRST2', 'FIRST2_REV'):
        return 'head'
    if tr in ('HEAD_TAIL', 'TAIL_HEAD'):
        return 'head_tail_cross'
    if tr in ('HEAD_SECOND_LAST', 'SECOND_HEAD_TAIL'):
        return 'head_secondlast_cross'
    if tr.startswith('SUM') or 'SUM' in tr:
        return 'digit_sum'
    if re.match(r'^P\d+P\d+$', tr):
        a, b = map(int, re.findall(r'\d+', tr))
        return 'adjacent_pair' if abs(a - b) == 1 else 'position_pair'
    return 'other'


def evaluate_rule(target_index, source_index, all_dates, last_date,
                  target_region, source_region, source_unit, source_prize, source_idx,
                  transform, lag, window=180, weekday=None, station_set=None):
    """Compute hits / days / hit_rate / baseline / lift_pp / db_day stats. No tier."""
    start = last_date - timedelta(days=window - 1)
    days = 0
    hits = 0
    db_day = 0
    sum_mt_unique = 0
    sum_db_unique = 0
    for td in all_dates:
        if td < start or td > last_date:
            continue
        if weekday is not None and td.weekday() != weekday:
            continue
        tgt = target_index.get((td, target_region))
        if not tgt or not tgt['all_set']:
            continue
        if station_set is not None and tgt['stations'] != station_set:
            continue
        sd = td - timedelta(days=lag)
        src = source_index.get((sd, source_region, source_unit, source_prize, source_idx, transform))
        if not src:
            continue
        days += 1
        t = src['tail']
        if t in tgt['all_set']:
            hits += 1
        if any(db == t for _, db in tgt['dbs']):
            db_day += 1
        sum_mt_unique += len(tgt['all_set'])
        sum_db_unique += len(tgt['db_unique'])
    if days == 0:
        return None
    baseline = sum_mt_unique / 100 / days
    db_baseline = sum_db_unique / 100 / days
    hit_rate = hits / days
    db_day_rate = db_day / days
    lo, hi = wilson_ci(hits, days)
    p = binomial_pvalue_one_sided(hits, days, baseline)
    return {
        'days': days,
        'hits': hits,
        'hit_rate': hit_rate,
        'baseline': baseline,
        'lift_pp': (hit_rate - baseline) * 100,
        'db_day_hits': db_day,
        'db_day_rate': db_day_rate,
        'db_day_baseline': db_baseline,
        'db_day_lift_pp': (db_day_rate - db_baseline) * 100,
        'ci95_lo': lo,
        'ci95_hi': hi,
        'raw_p': p,
    }
