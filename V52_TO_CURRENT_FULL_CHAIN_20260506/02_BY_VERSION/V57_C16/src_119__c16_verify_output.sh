#!/bin/bash
set -e
echo "=== adaptive bundles ==="
sqlite3 /root/Lottery_AI_Test/data/lottery_ai.db "
SELECT b.region, b.experiment_name, b.test_bt, b.official_bt,
       r.test_bt_status, r.would_save, r.would_break
FROM du_doan_test_bundles b
LEFT JOIN du_doan_test_results r ON r.run_id=b.run_id
WHERE b.run_date='2026-05-05'
  AND b.experiment_name LIKE '%ADAPTIVE_BUDGET_SELECTOR%'
ORDER BY b.region;"
echo "=== smoke ==="
systemctl is-active lottery
curl -s -o /dev/null -w 'health=%{http_code}\n' http://127.0.0.1:8000/api/health
curl -s -o /dev/null -w 'du_doan_test=%{http_code}\n' http://127.0.0.1:8000/du-doan-test
curl -s -o /dev/null -w 'final_mb=%{http_code}\n' 'http://127.0.0.1:8000/api/final-bundle?region=MB'
