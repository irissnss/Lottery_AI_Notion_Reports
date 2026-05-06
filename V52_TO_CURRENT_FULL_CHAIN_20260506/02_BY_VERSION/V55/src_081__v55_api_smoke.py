"""V20.3.37.55 — minimal API smoke test for new Google direct shadow models.

Calls each new model with a tiny prompt to verify:
  1. The Google AI Studio key (project sxkt) accepts the model name
  2. The Google GenAI SDK can route correctly
  3. The actual API model id resolves (e.g. gemma-4-31b → gemma-4-31b-it)

Failure on any model means that model is NOT ready for tomorrow's shadow run.
"""
import sys, os, time, json, traceback
sys.path.insert(0, '/root/Lottery_AI_Test/web/backend')

from env_loader import load_project_env
load_project_env()

from google import genai as google_genai
from google.genai import types as google_genai_types

KEY_SHADOW = os.getenv('GEMINI_KEY_SHADOW_NEW', '')
KEY_LEGACY = os.getenv('GEMINI_API_KEY', '')

assert KEY_SHADOW, "GEMINI_KEY_SHADOW_NEW must be present"
assert KEY_LEGACY, "GEMINI_API_KEY must be present"
assert KEY_SHADOW != KEY_LEGACY, "Two keys must be distinct"

import importlib
import gpt_analyzer as g
importlib.reload(g)
REGISTRY_TO_API = {
    mid: g.GOOGLE_MODEL_API_MAP.get(mid, mid)
    for mid in ['gemini-3.1-pro', 'gemini-3-flash', 'gemma-4-31b']
}
print("REGISTRY_TO_API resolved from gpt_analyzer:", REGISTRY_TO_API)

# Tiny prompt to keep cost minimal
PROMPT = "Reply with exactly one word: PONG"

results = []
client = google_genai.Client(api_key=KEY_SHADOW)

for reg_id, api_id in REGISTRY_TO_API.items():
    row = {'registry_id': reg_id, 'api_id': api_id, 'ok': False, 'err': '', 'latency_s': None, 'reply_len': 0, 'finish_reason': None}
    t0 = time.time()
    try:
        resp = client.models.generate_content(
            model=api_id,
            contents=PROMPT,
            config=google_genai_types.GenerateContentConfig(
                temperature=0,
                max_output_tokens=4096,
            )
        )
        row['latency_s'] = round(time.time() - t0, 2)
        text = ''
        try:
            text = resp.text or ''
        except Exception:
            text = '<no_text_attr>'
        row['reply_len'] = len(text)
        row['reply_preview'] = text[:120]
        if resp.candidates:
            row['finish_reason'] = str(resp.candidates[0].finish_reason)
        if hasattr(resp, 'usage_metadata') and resp.usage_metadata:
            um = resp.usage_metadata
            row['tokens_total'] = getattr(um, 'total_token_count', None)
            row['tokens_input'] = getattr(um, 'prompt_token_count', None)
            row['tokens_output'] = getattr(um, 'candidates_token_count', None)
        row['ok'] = bool(text)
    except Exception as e:
        row['latency_s'] = round(time.time() - t0, 2)
        row['err'] = f"{type(e).__name__}: {e}"
    results.append(row)

print(json.dumps(results, indent=2, ensure_ascii=False))

ok_count = sum(1 for r in results if r['ok'])
print(f"\nSMOKE_SUMMARY: {ok_count}/{len(results)} models passed")
if ok_count == len(results):
    print("ALL_API_SMOKE_OK")
else:
    print("SOME_MODELS_FAILED — see errors above")
    sys.exit(2)
