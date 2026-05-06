#!/bin/bash
# V20.3.37.55 — apply Google direct shadow cohort key + verify imports
set -e

ENVF=/root/Lottery_AI_Test/web/backend/.env

# 1. Append key only if not present (idempotent)
if grep -q '^GEMINI_KEY_SHADOW_NEW=' "$ENVF"; then
    echo "GEMINI_KEY_SHADOW_NEW already set — skipping append"
else
    echo "GEMINI_KEY_SHADOW_NEW=<REDACTED_GOOGLE_API_KEY>" >> "$ENVF"
    echo "GEMINI_KEY_SHADOW_NEW appended"
fi

echo "=== ENV KEY LIST (names only, redacted values) ==="
grep -E '^[A-Z_]+=' "$ENVF" | sed 's/=.*/=<set>/'

echo "=== POST-EDIT HASHES ==="
sha256sum /root/Lottery_AI_Test/web/backend/model_registry.py /root/Lottery_AI_Test/web/backend/gpt_analyzer.py /root/Lottery_AI_Test/web/backend/.env

echo "=== PYTHON SYNTAX CHECK ==="
cd /root/Lottery_AI_Test/web/backend
python3 -c "import ast, sys; ast.parse(open('model_registry.py').read()); ast.parse(open('gpt_analyzer.py').read()); print('AST_OK')"

echo "=== REGISTRY SELF-TEST (counts) ==="
python3 -c "import sys; sys.path.insert(0, '/root/Lottery_AI_Test/web/backend'); from model_registry import SHADOW_AUTO_EVAL_MODELS, OUTPUT_ELIGIBLE_MODELS, ALL_RUNTIME_MODELS; print('SHADOW_AUTO=', len(SHADOW_AUTO_EVAL_MODELS), SHADOW_AUTO_EVAL_MODELS); print('OUTPUT_ELIGIBLE=', len(OUTPUT_ELIGIBLE_MODELS)); print('ALL_RUNTIME=', len(ALL_RUNTIME_MODELS))"

echo "=== SHADOW_GATE + GOOGLE DIRECT CHECK ==="
python3 -c "import sys; sys.path.insert(0, '/root/Lottery_AI_Test/web/backend'); import gpt_analyzer as g; print('SHADOW_GATE_MODELS=', sorted(g.SHADOW_GATE_MODELS)); print('GOOGLE_DIRECT_SHADOW_MODELS=', sorted(g.GOOGLE_DIRECT_SHADOW_MODELS)); print('Latest cohort=', g.PHASE_FIRST_GATE_HISTORY[-1]['cohort_id'], '| n=', len(g.PHASE_FIRST_GATE_HISTORY[-1]['models']))"

echo "=== KEY RESOLUTION DRY ==="
python3 -c "import os; os.environ.setdefault('GEMINI_KEY_SHADOW_NEW','x'); import sys; sys.path.insert(0,'/root/Lottery_AI_Test/web/backend'); from dotenv import load_dotenv; load_dotenv('/root/Lottery_AI_Test/web/backend/.env'); k=os.environ.get('GEMINI_KEY_SHADOW_NEW',''); print('GEMINI_KEY_SHADOW_NEW length=', len(k))"
