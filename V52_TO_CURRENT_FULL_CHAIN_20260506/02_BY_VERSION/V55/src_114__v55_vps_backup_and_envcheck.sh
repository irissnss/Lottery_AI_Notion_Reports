#!/bin/bash
# V20.3.37.55 — VPS backup before shadow model add (Gemini 3.1 Pro / Gemini 3 Flash / Gemma 4 31B)
set -e
BK=/root/Lottery_AI_Test/backups/v55_shadow_add_20260505_0750
mkdir -p "$BK"
cp /root/Lottery_AI_Test/web/backend/model_registry.py "$BK/model_registry.py.bak"
cp /root/Lottery_AI_Test/web/backend/gpt_analyzer.py "$BK/gpt_analyzer.py.bak"
cp /root/Lottery_AI_Test/web/backend/.env "$BK/env.bak"

echo "=== BACKUP_DIR ==="
echo "$BK"
ls -lh "$BK"

echo "=== ENV KEY CHECK ==="
if grep -q '^GEMINI_KEY_SHADOW_NEW=' /root/Lottery_AI_Test/web/backend/.env; then
    echo "GEMINI_KEY_SHADOW_NEW=PRESENT"
else
    echo "GEMINI_KEY_SHADOW_NEW=NOT_PRESENT"
fi

echo "=== SERVICE STATUS ==="
systemctl is-active lottery
systemctl show lottery --property=MainPID,ActiveEnterTimestamp --no-page

echo "=== CURRENT REGISTRY HASH ==="
sha256sum /root/Lottery_AI_Test/web/backend/model_registry.py /root/Lottery_AI_Test/web/backend/gpt_analyzer.py /root/Lottery_AI_Test/web/backend/.env
