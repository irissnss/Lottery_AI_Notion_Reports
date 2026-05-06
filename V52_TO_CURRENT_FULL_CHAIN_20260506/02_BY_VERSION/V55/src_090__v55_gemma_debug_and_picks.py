"""V55 — debug gemma-4-31b missing rows + show new shadow models picks 05/05."""
import sqlite3, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
c = sqlite3.connect('data/lottery_ai.db')
c.row_factory = sqlite3.Row
cu = c.cursor()

print("=== picks for new shadow models on 05/05 ===")
cu.execute("SELECT date, target_region, ai_model, run_source, main_numbers, hit_count, hit_numbers, status, hit_level FROM predictions WHERE ai_model IN ('gemini-3.1-pro','gemini-3-flash','gemma-4-31b') AND date='2026-05-05' ORDER BY ai_model, target_region")
for r in cu.fetchall():
    print(f"  {r['ai_model']:20s} {r['target_region']:3s} status={r['status']:8s} picks={r['main_numbers']} hits={r['hit_numbers']} ({r['hit_count']})")

print("\n=== scheduler log mentions of 'gemma-4-31b' on 05/05 ===")
cu.execute("SELECT log_time, log_level, region, job_name, message FROM scheduler_logs WHERE log_time >= '2026-05-05' AND message LIKE '%gemma%' ORDER BY log_time")
rows = cu.fetchall()
print(f"  total mentions: {len(rows)}")
for r in rows[:30]:
    msg = (r['message'] or '')[:200]
    print(f"  {r['log_time']} L{r['log_level']} {r['region']} {r['job_name']:30s} {msg}")

print("\n=== look in prediction_trace.jsonl for gemma calls ===")
import os
trace_path = 'web/backend/prediction_trace.jsonl'
if os.path.exists(trace_path):
    seen = 0
    with open(trace_path, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            if 'gemma-4-31b' in line:
                try:
                    j = json.loads(line)
                    if (j.get('date') or '').startswith('2026-05-05') or (j.get('timestamp') or '').startswith('2026-05-05'):
                        seen += 1
                        print(f"  ts={j.get('timestamp')} model={j.get('model')} region={j.get('target_region') or j.get('region')} pred={j.get('prediction')} finish={j.get('finish_reason')} ctx={j.get('context_pack_chars')} retry={j.get('phase_first_repair_retry_used')} contract_invalid={j.get('phase_first_contract_invalid_count')}")
                        if seen > 8:
                            break
                except Exception:
                    pass
    print(f"  trace lines for gemma 05/05: {seen}")
else:
    print("  trace file not found")
