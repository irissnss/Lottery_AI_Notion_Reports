#!/bin/bash
set -e
cd /root/Lottery_AI_Test
/root/Lottery_AI_Test/venv/bin/python3 -m py_compile web/backend/_du_doan_test_schema.py web/backend/_du_doan_test_engine.py
cd web/backend
/root/Lottery_AI_Test/venv/bin/python3 _du_doan_test_engine.py --region ALL --backfill-days 30 --json > /root/Lottery_AI_Test/artifacts/_v52_5_3_engine_backfill_30d.json
cd /root/Lottery_AI_Test
/root/Lottery_AI_Test/venv/bin/python3 - <<'PY'
import json
with open('artifacts/_v52_5_3_engine_backfill_30d.json') as f:
    data = json.load(f)
for region, payload in data.items():
    days = len(payload.get('results', []))
    runs = sum(int(r.get('runs_written') or 0) for r in payload.get('results', []))
    cands = sum(int(r.get('candidates_written') or 0) for r in payload.get('results', []))
    contribs = sum(int(r.get('model_contrib_written') or 0) for r in payload.get('results', []))
    errs = [r for r in payload.get('results', []) if r.get('error')]
    print(f'{region}\tdays={days}\truns={runs}\tcands={cands}\tcontribs={contribs}\terrors={len(errs)}')
PY
