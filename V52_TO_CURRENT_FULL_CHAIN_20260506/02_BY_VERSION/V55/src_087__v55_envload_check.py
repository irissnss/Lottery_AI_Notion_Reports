"""V20.3.37.55 — verify env_loader.load_project_env() picks up GEMINI_KEY_SHADOW_NEW."""
import sys, os
sys.path.insert(0, '/root/Lottery_AI_Test/web/backend')
from env_loader import load_project_env
load_project_env()

shadow_key = os.getenv('GEMINI_KEY_SHADOW_NEW', '')
legacy_key = os.getenv('GEMINI_API_KEY', '')

print(f"GEMINI_KEY_SHADOW_NEW len={len(shadow_key)} prefix={shadow_key[:10] if shadow_key else 'EMPTY'}")
print(f"GEMINI_API_KEY      len={len(legacy_key)} prefix={legacy_key[:10] if legacy_key else 'EMPTY'}")

distinct = bool(shadow_key) and bool(legacy_key) and shadow_key != legacy_key
print(f"DISTINCT_KEYS={distinct}")

# Now reimport gpt_analyzer with env loaded and check key resolution path
import importlib
import gpt_analyzer as g
importlib.reload(g)
print(f"GOOGLE_MODEL_KEYS values prefix:")
for mid, k in g.GOOGLE_MODEL_KEYS.items():
    print(f"  {mid}: len={len(k)} prefix={k[:10] if k else 'EMPTY'}")

assert shadow_key, "GEMINI_KEY_SHADOW_NEW must be present after env load"
assert legacy_key, "GEMINI_API_KEY must remain present after env load"
assert distinct, "Two keys must be distinct"
assert all(g.GOOGLE_MODEL_KEYS[mid] == shadow_key for mid in ['gemini-3.1-pro','gemini-3-flash','gemma-4-31b']), "GOOGLE_MODEL_KEYS must resolve to shadow key for new cohort"
print("ENV_LOAD_OK")
