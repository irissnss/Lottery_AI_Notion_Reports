"""V55 — verify scheduler now routes gemma-* to google lane (post-fix)."""
import sys
sys.path.insert(0, '/root/Lottery_AI_Test/web/backend')
from gpt_analyzer import GOOGLE_DIRECT_SHADOW_MODELS, GOOGLE_MODEL_KEYS
from scheduler import _get_api_key_for_model, _preflight_check_provider_runtime

print("=== preflight on the 3 Google direct shadow models ===")
result = _preflight_check_provider_runtime(list(GOOGLE_DIRECT_SHADOW_MODELS))
print(result)

print("\n=== _get_api_key_for_model resolution per model ===")
for m in sorted(GOOGLE_DIRECT_SHADOW_MODELS):
    k = _get_api_key_for_model(m) or ''
    print(f"  {m}: len={len(k)} prefix={k[:10] if k else 'EMPTY'}")

print("\n=== full SHADOW_AUTO_EVAL preflight (13 models) ===")
from model_registry import SHADOW_AUTO_EVAL_MODELS
result = _preflight_check_provider_runtime(SHADOW_AUTO_EVAL_MODELS)
print(f"  ok={result['ok']} checked={result['checked_models']}")
print(f"  failures={result['failures']}")
print(f"  warnings={result['warnings']}")
