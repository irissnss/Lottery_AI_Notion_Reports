"""Reconcile bundle status with extracted actual tails."""
import sqlite3, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
c = sqlite3.connect('data/lottery_ai.db')
c.row_factory = sqlite3.Row
cu = c.cursor()


def tail2(x):
    s = ''.join(ch for ch in str(x) if ch.isdigit())
    return s[-2:].zfill(2) if s else ''


def all_tails(date, region):
    cu.execute("SELECT tail_db, tail_g8, prizes_json FROM lottery_results WHERE date=? AND region=?", (date, region))
    rows = cu.fetchall()
    by_prize = {}
    s = set()
    for r in rows:
        if r['tail_db']:
            t = tail2(r['tail_db']);
            s.add(t)
            by_prize.setdefault('DB', set()).add(t)
        if r['tail_g8']:
            t = tail2(r['tail_g8']);
            s.add(t)
            by_prize.setdefault('G8', set()).add(t)
        if r['prizes_json']:
            try:
                pj = json.loads(r['prizes_json'])
            except Exception:
                pj = {}
            for prize_name, vals in (pj or {}).items():
                if not isinstance(vals, list):
                    vals = [vals]
                key = prize_name
                for v in vals:
                    t = tail2(v)
                    if t:
                        s.add(t)
                        by_prize.setdefault(key, set()).add(t)
    return s, by_prize


for date in ['2026-05-04', '2026-05-05']:
    print(f"\n=================== {date} ===================")
    for region in ['MN', 'MT', 'MB']:
        cu.execute("SELECT bach_thu, lo2, bach_thu_status, lo2_status FROM final_bundles WHERE date=? AND region=?", (date, region))
        b = cu.fetchone()
        if not b:
            print(f"  {region}: NO BUNDLE")
            continue
        bt = tail2(b['bach_thu'])
        try:
            lo2 = [tail2(x) for x in (json.loads(b['lo2']) if b['lo2'] else [])]
        except Exception:
            lo2 = []
        all_t, by_prize = all_tails(date, region)
        print(f"  {region}: BT={bt} status={b['bach_thu_status']} | lo2={lo2} status={b['lo2_status']}")
        print(f"     all_actual_tails (n={len(all_t)}) = {sorted(all_t)}")
        print(f"     BT_in_actual = {bt in all_t}, lo2[0]_in = {lo2[0] in all_t if lo2 else None}, lo2[1]_in = {lo2[1] in all_t if len(lo2)>1 else None}")
        # check by prize
        per_prize_match = {k: bt in v for k, v in by_prize.items() if bt in v}
        print(f"     BT match by prize: {per_prize_match}")
