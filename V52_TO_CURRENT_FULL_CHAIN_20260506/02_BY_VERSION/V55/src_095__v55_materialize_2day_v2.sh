#!/bin/bash
set -e
cd /root/Lottery_AI_Test/web/backend
PY=/root/Lottery_AI_Test/venv/bin/python3

for date in 2026-05-04 2026-05-05; do
  echo "=== loz_stage_trace_shadow $date (all regions) ==="
  for region in MN MT MB; do
    $PY _materialize_loz_stage_trace_shadow.py --date $date --region $region --json 2>&1 | tail -3 || true
  done

  echo "=== v52 measurement surfaces $date ==="
  $PY _materialize_v52_measurement_surfaces.py --date $date --json 2>&1 | tail -3 || true

  echo "=== experimental_preview_shadow $date (all regions) ==="
  for region in MN MT MB; do
    $PY _materialize_experimental_preview_shadow.py --date $date --region $region --json 2>&1 | tail -3 || true
  done
done

echo "=== DONE ==="
