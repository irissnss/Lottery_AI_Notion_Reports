"""V20.3.37.55 — post-restart health and roster verification."""
import sys, json, urllib.request

# 1) Health check
url = 'http://127.0.0.1:8000/api/health'
try:
    with urllib.request.urlopen(url, timeout=10) as r:
        data = json.load(r)
    print("=== /api/health ===")
    for k in [
        'version','runtime_model_count','output_model_count',
        'output_eligible_model_count','shadow_auto_eval_model_count',
        'registry_visible_model_count','active_rerank_measurement_model_count',
        'active_measured_component_count'
    ]:
        if k in data:
            print(f"  {k}={data[k]}")
except Exception as e:
    print(f"HEALTH_ERR={e}")

# 2) Roster confirm via direct registry import
sys.path.insert(0, '/root/Lottery_AI_Test/web/backend')
from model_registry import (
    SHADOW_AUTO_EVAL_MODELS, OUTPUT_ELIGIBLE_MODELS, ALL_RUNTIME_MODELS,
    get_models_for_slot
)
print("\n=== registry counts ===")
print(f"  SHADOW_AUTO={len(SHADOW_AUTO_EVAL_MODELS)}")
print(f"  OUTPUT_ELIGIBLE={len(OUTPUT_ELIGIBLE_MODELS)}")
print(f"  ALL_RUNTIME={len(ALL_RUNTIME_MODELS)}")

new_models = ['gemini-3.1-pro','gemini-3-flash','gemma-4-31b']
print("\n=== new model presence in shadow_auto ===")
for m in new_models:
    print(f"  {m}: in_SHADOW_AUTO={m in SHADOW_AUTO_EVAL_MODELS}, in_OUTPUT_ELIGIBLE={m in OUTPUT_ELIGIBLE_MODELS} (must be False)")

print("\n=== shadow batch composition (completion_triggered_shadow) ===")
for region in ['MN','MT','MB']:
    models = get_models_for_slot('completion_triggered_shadow', region)
    has_all_new = all(m in models for m in new_models)
    print(f"  {region}: n={len(models)} new_models_present={has_all_new}")

# 3) Phase-first runtime gate
import gpt_analyzer as g
print("\n=== phase-first gate runtime state ===")
for m in new_models:
    s = g.get_phase_first_gate_runtime_state(m)
    print(f"  {m}: cohort={s.get('cohort_id')} gate_applied={s.get('gate_applied')} contract_required={s.get('contract_required')}")

# 4) Key resolution at runtime (now env loaded by service)
import os
shadow_key = os.getenv('GEMINI_KEY_SHADOW_NEW', '')
legacy_key = os.getenv('GEMINI_API_KEY', '')
# env_loader was loaded by gpt_analyzer imports
print("\n=== env state at this verify run ===")
print(f"  GEMINI_KEY_SHADOW_NEW present? {bool(shadow_key)} len={len(shadow_key)}")
print(f"  GEMINI_API_KEY present? {bool(legacy_key)} len={len(legacy_key)}")
print(f"  distinct? {bool(shadow_key) and bool(legacy_key) and shadow_key != legacy_key}")

print("\nPOST_RESTART_OK")
