import sqlite3, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
c = sqlite3.connect('data/lottery_ai.db')
c.row_factory = sqlite3.Row
cu = c.cursor()
for date in ['2026-05-04', '2026-05-05']:
    print(f"\n=== {date} ===")
    cu.execute("SELECT date, region, station, tail_db, tail_g8, prizes_json FROM lottery_results WHERE date=? ORDER BY region, station", (date,))
    rows = cu.fetchall()
    for r in rows:
        try:
            pj = json.loads(r['prizes_json']) if r['prizes_json'] else None
        except Exception:
            pj = None
        keys = sorted((pj or {}).keys()) if isinstance(pj, dict) else []
        sample_vals = []
        if isinstance(pj, dict):
            for k in keys[:6]:
                v = pj[k]
                if isinstance(v, list):
                    v = v[:3]
                sample_vals.append(f"{k}={v}")
        print(f"  {r['region']:3s} {r['station']:20s} tail_db={r['tail_db']} tail_g8={r['tail_g8']} prize_keys={keys[:6]} sample={sample_vals[:3]}")
