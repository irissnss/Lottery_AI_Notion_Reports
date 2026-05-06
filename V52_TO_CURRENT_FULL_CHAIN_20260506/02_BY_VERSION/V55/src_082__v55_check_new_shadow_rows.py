"""V55 — verify the 3 new Google-direct shadow models actually wrote rows today."""
import sqlite3, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
c = sqlite3.connect('data/lottery_ai.db')
c.row_factory = sqlite3.Row
cu = c.cursor()
new_models = ['gemini-3.1-pro', 'gemini-3-flash', 'gemma-4-31b']
print("=== predictions rows for 3 new models on 04/05 + 05/05 ===")
for m in new_models:
    cu.execute("SELECT date, target_region, run_source, status, hit_count, pick_count, created_at FROM predictions WHERE ai_model=? AND date IN ('2026-05-04','2026-05-05') ORDER BY date, target_region, created_at", (m,))
    rows = cu.fetchall()
    print(f"\n  --- {m}: {len(rows)} rows ---")
    for r in rows:
        print(f"    {r['date']} {r['target_region']} {r['run_source']:35s} status={r['status']} hits={r['hit_count']} picks={r['pick_count']} at={r['created_at']}")

print("\n=== predictions counts by ai_model on 2026-05-05 (top 30) ===")
cu.execute("SELECT ai_model, COUNT(*) FROM predictions WHERE date='2026-05-05' GROUP BY ai_model ORDER BY ai_model")
for r in cu.fetchall():
    print(f"  {r[0]:30s} {r[1]}")

print("\n=== predictions counts by ai_model on 2026-05-04 (top 30) ===")
cu.execute("SELECT ai_model, COUNT(*) FROM predictions WHERE date='2026-05-04' GROUP BY ai_model ORDER BY ai_model")
for r in cu.fetchall():
    print(f"  {r[0]:30s} {r[1]}")
