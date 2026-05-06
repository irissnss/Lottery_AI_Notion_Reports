"""V20.3.37.55 — VPS verification of new Google direct shadow cohort.

Runs on VPS via venv python; verifies imports + new wiring + key resolution
without making any external API calls.
"""
import sys
sys.path.insert(0, '/root/Lottery_AI_Test/web/backend')

import os

print("=== Python version ===")
print(sys.version)

print("\n=== model_registry imports ===")
from model_registry import (
    SHADOW_AUTO_EVAL_MODELS,
    OUTPUT_ELIGIBLE_MODELS,
    ALL_RUNTIME_MODELS,
    MODEL_REGISTRY,
)
print("SHADOW_AUTO=", len(SHADOW_AUTO_EVAL_MODELS), SHADOW_AUTO_EVAL_MODELS)
print("OUTPUT_ELIGIBLE=", len(OUTPUT_ELIGIBLE_MODELS))
print("ALL_RUNTIME=", len(ALL_RUNTIME_MODELS))

assert 'gemini-3.1-pro' in SHADOW_AUTO_EVAL_MODELS
assert 'gemini-3-flash' in SHADOW_AUTO_EVAL_MODELS
assert 'gemma-4-31b' in SHADOW_AUTO_EVAL_MODELS

new_entries = [m for m in MODEL_REGISTRY if m['id'] in {'gemini-3.1-pro','gemini-3-flash','gemma-4-31b'}]
print("\n=== new entries roster ===")
for m in new_entries:
    print(f"  id={m['id']} status={m['status']} provider={m['provider']} output_eligible={m['output_eligible']} slots={m['schedule_slots']}")

print("\n=== gpt_analyzer imports ===")
import gpt_analyzer as g
print("SHADOW_GATE_MODELS:", sorted(g.SHADOW_GATE_MODELS))
print("GOOGLE_DIRECT_SHADOW_MODELS:", sorted(g.GOOGLE_DIRECT_SHADOW_MODELS))
print("GOOGLE_MODEL_API_MAP:", g.GOOGLE_MODEL_API_MAP)
print("GOOGLE_MODEL_KEYS keys:", list(g.GOOGLE_MODEL_KEYS.keys()))
print("Latest cohort:", g.PHASE_FIRST_GATE_HISTORY[-1]['cohort_id'])
print("Latest cohort models n=", len(g.PHASE_FIRST_GATE_HISTORY[-1]['models']))
print("Latest cohort models:", g.PHASE_FIRST_GATE_HISTORY[-1]['models'])

assert 'gemini-3.1-pro' in g.SHADOW_GATE_MODELS
assert 'gemini-3-flash' in g.SHADOW_GATE_MODELS
assert 'gemma-4-31b' in g.SHADOW_GATE_MODELS
assert g.GOOGLE_MODEL_API_MAP.get('gemma-4-31b') == 'gemma-4-31b-it'
assert all(m in g.MODEL_DISTRIBUTION_POLICY for m in ['gemini-3.1-pro','gemini-3-flash','gemma-4-31b'])

print("\n=== key resolution dry (ENV) ===")
shadow_key_env = os.getenv('GEMINI_KEY_SHADOW_NEW', '')
gemini_legacy_env = os.getenv('GEMINI_API_KEY', '')
print(f"GEMINI_KEY_SHADOW_NEW set? {bool(shadow_key_env)} len={len(shadow_key_env)}")
print(f"GEMINI_API_KEY set? {bool(gemini_legacy_env)} len={len(gemini_legacy_env)}")
print("Distinct values?", shadow_key_env != gemini_legacy_env if (shadow_key_env and gemini_legacy_env) else 'one_or_both_empty')

print("\n=== Phase-first gate runtime state for new cohort ===")
for mid in ['gemini-3.1-pro','gemini-3-flash','gemma-4-31b']:
    state = g.get_phase_first_gate_runtime_state(mid)
    print(f"  {mid}: cohort_id={state.get('cohort_id')} gate_applied={state.get('gate_applied')} contract_required={state.get('contract_required')} status={state.get('cohort_status')}")

print("\n=== distribution policy lookup ===")
for mid in ['gemini-3.1-pro','gemini-3-flash','gemma-4-31b']:
    print(f"  {mid}: {g.MODEL_DISTRIBUTION_POLICY[mid]}")

print("\n=== get_models_for_slot('completion_triggered_shadow', region) ===")
from model_registry import get_models_for_slot
for region in ['MN','MT','MB']:
    models = get_models_for_slot('completion_triggered_shadow', region)
    print(f"  {region}: n={len(models)} {models}")

print("\nALL_VERIFY_OK")
