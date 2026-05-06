#!/bin/bash
# V55 — materialize measurement-only surfaces for 04/05 and 05/05
# (no official mutation, all writes are diagnostic/test-only tables)
set -e
cd /root/Lottery_AI_Test/web/backend
PY=/root/Lottery_AI_Test/venv/bin/python3

echo "=== loz_stage_trace_shadow 04/05 + 05/05 ==="
$PY _materialize_loz_stage_trace_shadow.py --start 2026-05-04 --end 2026-05-05 2>&1 | tail -8 || true

echo "=== v52 measurement surfaces 04/05 + 05/05 ==="
$PY _materialize_v52_measurement_surfaces.py --start 2026-05-04 --end 2026-05-05 2>&1 | tail -8 || true

echo "=== weekday_blackspot anchor 2026-05-05 ==="
$PY _materialize_weekday_blackspot_shadow.py --anchor 2026-05-05 2>&1 | tail -8 || true

echo "=== model strength tensor anchor 2026-05-05 ==="
$PY _compute_model_strength_tensor.py --anchor 2026-05-05 2>&1 | tail -8 || true

echo "=== experimental_preview_shadow 04/05 + 05/05 (MN+MT+MB) ==="
$PY _materialize_experimental_preview_shadow.py --start 2026-05-04 --end 2026-05-05 --regions MN,MT,MB 2>&1 | tail -8 || true

echo "=== du_doan_test_daily_runner ALL 2026-05-04 ==="
$PY _du_doan_test_daily_runner.py --date 2026-05-04 --region ALL --mode POST_CLOSEOUT_DIAGNOSTIC_FULL_25 2>&1 | tail -10 || true

echo "=== du_doan_test_daily_runner ALL 2026-05-05 ==="
$PY _du_doan_test_daily_runner.py --date 2026-05-05 --region ALL --mode POST_CLOSEOUT_DIAGNOSTIC_FULL_25 2>&1 | tail -10 || true

echo "=== DONE ==="
