"""V52.5.7 final hash diff: pre-V52.5.1 vs post-V52.5.7."""
from pathlib import Path

def parse(path: str) -> dict:
    d = {}
    for line in Path(path).read_text().splitlines():
        if not line or line.startswith('#') or '\t' not in line:
            continue
        parts = line.split('\t')
        vals = {}
        for piece in parts[1:]:
            if '=' in piece:
                k, v = piece.split('=', 1)
                vals[k] = v
        d[parts[0]] = vals
    return d


pre = parse('artifacts/_v52_5_1_pre_hash_20260503.txt')
post = parse('artifacts/_v52_5_7_post_hash_20260503.txt')

official = ['predictions', 'final_bundles', 'lottery_results', 'model_daily_eval', 'scheduler_logs']
v52_measurement = ['mt_model_hit_output_drop_shadow', 'loz_selector_shadow', 'model_latency_cost_audit_daily']
v52_5_test = ['model_strength_by_region_weekday_station_daily', 'experimental_preview_shadow',
              'mb_experimental_preview_shadow', 'du_doan_test_runs', 'du_doan_test_bundles',
              'du_doan_test_results', 'du_doan_test_candidates',
              'du_doan_test_model_contribution', 'du_doan_test_experiments',
              'du_doan_test_audit_log']

print('=== Official source tables (must be unchanged) ===')
for t in official:
    a = pre.get(t, {})
    b = post.get(t, {})
    same = a.get('sha256') == b.get('sha256')
    diff = '' if same else ' MISMATCH'
    print(f"  {t:30}  {a.get('count','-'):>8} -> {b.get('count','-'):>8}  same={same}{diff}")

print()
print('=== V52 measurement tables (must be unchanged after V52.2) ===')
for t in v52_measurement:
    a = pre.get(t, {})
    b = post.get(t, {})
    same = a.get('sha256') == b.get('sha256')
    print(f"  {t:30}  {a.get('count','-'):>8} -> {b.get('count','-'):>8}  same={same}")

print()
print('=== V52.5.x test-lane tables (created/grown this session) ===')
for t in v52_5_test:
    a = pre.get(t, {})
    b = post.get(t, {})
    pre_c = a.get('count', '-')
    post_c = b.get('count', '-')
    print(f"  {t:50}  {pre_c:>8} -> {post_c:>8}")
