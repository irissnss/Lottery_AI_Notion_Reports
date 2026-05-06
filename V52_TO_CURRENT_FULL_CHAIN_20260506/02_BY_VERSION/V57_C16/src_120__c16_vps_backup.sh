#!/bin/bash
set -e
BK=/root/Lottery_AI_Test/backups/c16_model_budget_20260505_2248
mkdir -p "$BK"
cp /root/Lottery_AI_Test/web/backend/main.py "$BK/main.py.bak"
cp /root/Lottery_AI_Test/web/backend/_du_doan_test_schema.py "$BK/_du_doan_test_schema.py.bak"
cp /root/Lottery_AI_Test/web/frontend/du-doan-test.html "$BK/du-doan-test.html.bak"
if [ -f /root/Lottery_AI_Test/web/backend/_materialize_du_doan_test_model_budget.py ]; then
  cp /root/Lottery_AI_Test/web/backend/_materialize_du_doan_test_model_budget.py "$BK/_materialize_du_doan_test_model_budget.py.bak"
fi
echo "BACKUP_DIR=$BK"
ls -lh "$BK"
