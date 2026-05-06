#!/bin/bash
set -e
cd /root/Lottery_AI_Test
/root/Lottery_AI_Test/venv/bin/python3 web/backend/_materialize_experimental_preview_shadow.py \
  --region ALL --backfill-days 60 > artifacts/_v52_5_2_backfill_60d.json
/root/Lottery_AI_Test/venv/bin/python3 - <<'PY'
import json
with open('artifacts/_v52_5_2_backfill_60d.json') as f:
    data = json.load(f)
for region, payload in data.items():
    days = len(payload.get('results', []))
    rows = sum(int(r.get('rows_written') or 0) for r in payload.get('results', []))
    skipped = sum(1 for r in payload.get('results', []) if r.get('skipped'))
    errors = [r for r in payload.get('results', []) if r.get('error')]
    print(f'{region}\tdays_processed={days}\trows_written={rows}\tdays_skipped={skipped}\terrors={len(errors)}')
PY
