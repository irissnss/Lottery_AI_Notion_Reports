# V20.3.37.55 — Shadow lane add: Gemini 3.1 Pro, Gemini 3 Flash, Gemma 4 31B

**Owner:** anh
**Date:** 2026-05-05 (Asia/Saigon)
**Trigger:** Owner-supplied Google AI Studio key (project sxkt, Tier 2) and explicit instruction to add 3 new shadow models, "đầy đủ thông thiếu sót luồng nào mà showdow đang hoạt động".
**Risk class:** ADDITIVE / MEASUREMENT-ONLY (no `/du-doan` impact)
**Live timing:** Deployed 07:55 VN; live windows are 16:30/16:42/17:42; ~9h buffer.

---

## 1. Scope

Add three new generative models into the `SHADOW_AUTO` lane only:

| registry_id | display | provider | output_eligible | API model name (2026-05-05) |
|---|---|---|---|---|
| `gemini-3.1-pro` | Gemini 3.1 Pro | google | False | `gemini-3.1-pro-preview` |
| `gemini-3-flash` | Gemini 3 Flash | google | False | `gemini-3-flash-preview` |
| `gemma-4-31b` | Gemma 4 31B | google | False | `gemma-4-31b-it` |

Same plumbing pattern as the V20.3.32 owner-added cohort (gpt-5.5 / deepseek-v4-pro / deepseek-v4-flash / qwen3.6-plus + V17.19.4 gpt-oss-120b), so the shadow batch already in production knows how to consume them via registry-derived sets.

---

## 2. Files changed (local + VPS)

### `web/backend/model_registry.py`
- Three new `MODEL_REGISTRY` entries with `status='SHADOW_AUTO'`, `provider='google'`, `output_eligible=False`, `allowed_regions=['MN','MT','MB']`, `schedule_slots=['completion_triggered_shadow','shadow_eval_post_verify']`.
- Self-test counters bumped: SHADOW_AUTO 10 → 13, ALL_RUNTIME 28 → 31. OUTPUT_ELIGIBLE stays 15.

### `web/backend/gpt_analyzer.py`
- New module-level constants:
  - `GOOGLE_MODEL_KEYS` (per-model key lookup; reads `GEMINI_KEY_SHADOW_NEW`).
  - `GOOGLE_MODEL_API_MAP` (registry id → current Google API name).
  - `GOOGLE_DIRECT_SHADOW_MODELS = set(GOOGLE_MODEL_KEYS.keys())`.
- `is_gemini` extended to also match `selected_model.startswith("gemma")` so Gemma 4 31B routes through `_call_gemini`.
- `MODEL_DISTRIBUTION_POLICY`: 3 new entries set to `FULL_CONTEXT` (system prompt + dynamic prompt + context pack + REASONING_RULEBOOK + PHASE-FIRST GATE).
- `SHADOW_GATE_MODELS`: union of prior 5 plus 3 new (8 total). `PHASE_FIRST_CONTRACT_MODELS = set(SHADOW_GATE_MODELS)` automatically follows.
- `PHASE_FIRST_GATE_HISTORY`: closed cohort `PFG-20260428-D` at `2026-05-05 07:44:59`, opened new cohort `PFG-20260505-E` at `2026-05-05 07:45:00` containing the 8 models.
- Gemini-lane key resolution updated: `api_key → GOOGLE_MODEL_KEYS.get(...) → DB ai_keys.gemini_key_shadow_new → GEMINI_API_KEY` (legacy fallback). Output models `gemini-2.5-flash`/`gemini-2.5-pro` keep using `GEMINI_API_KEY` because they are not in `GOOGLE_MODEL_KEYS`.
- Dispatch to `_call_gemini` now resolves API model id via `GOOGLE_MODEL_API_MAP.get(selected_model, selected_model)`.

### `/root/Lottery_AI_Test/.env` (project-root, the file `env_loader.PROJECT_ENV_PATH` actually reads)
- Appended `GEMINI_KEY_SHADOW_NEW=AIzaSy…` (Google AI Studio Tier-2 project `sxkt`).
- All 14 prior keys preserved verbatim. Legacy `GEMINI_API_KEY` UNCHANGED.

### Backups (VPS)
- `/root/Lottery_AI_Test/backups/v55_shadow_add_20260505_0750/`:
  - `model_registry.py.bak`
  - `gpt_analyzer.py.bak`
  - `env.bak` (backend/.env)
  - `project_root_env.bak` (project-root .env, the real one)

---

## 3. VPS verification chain (ALL PASSED)

### 3.1 Static / structural
```
=== model_registry counts ===
SHADOW_AUTO=13, OUTPUT_ELIGIBLE=15, ALL_RUNTIME=31

=== new entries ===
gemini-3.1-pro  status=SHADOW_AUTO provider=google output_eligible=False slots=[completion_triggered_shadow, shadow_eval_post_verify]
gemini-3-flash  status=SHADOW_AUTO provider=google output_eligible=False slots=[completion_triggered_shadow, shadow_eval_post_verify]
gemma-4-31b     status=SHADOW_AUTO provider=google output_eligible=False slots=[completion_triggered_shadow, shadow_eval_post_verify]

=== gpt_analyzer plumbing ===
SHADOW_GATE_MODELS = 8 [deepseek-v4-flash, deepseek-v4-pro, gemini-3-flash, gemini-3.1-pro, gemma-4-31b, gpt-5.5, gpt-oss-120b, qwen3.6-plus]
GOOGLE_DIRECT_SHADOW_MODELS = [gemini-3-flash, gemini-3.1-pro, gemma-4-31b]
GOOGLE_MODEL_API_MAP = {gemma-4-31b: gemma-4-31b-it, gemini-3.1-pro: gemini-3.1-pro-preview, gemini-3-flash: gemini-3-flash-preview}
Latest cohort = PFG-20260505-E (8 models, contract_required=True)
MODEL_DISTRIBUTION_POLICY[3 new] = FULL_CONTEXT
```

### 3.2 Env loader integrity
```
GEMINI_KEY_SHADOW_NEW len=39 prefix=<REDACTED_GOOGLE_API_KEY>
GEMINI_API_KEY        len=39 prefix=<REDACTED_GOOGLE_API_KEY>
DISTINCT_KEYS=True
GOOGLE_MODEL_KEYS resolves all 3 to the new shadow key
```

### 3.3 Phase-first runtime gate
For each new model `get_phase_first_gate_runtime_state(...)` returns `cohort=PFG-20260505-E gate_applied=True contract_required=True status=CURRENT`.

### 3.4 Shadow batch composition (`get_models_for_slot('completion_triggered_shadow', region)`)
- MN: n=13, all 3 new present.
- MT: n=13, all 3 new present.
- MB: n=13, all 3 new present.

### 3.5 Service health (post `systemctl restart lottery` at 07:55:55)
```
systemctl is-active lottery → active
MainPID=712542
/api/health → HTTP 200
version=V20.3.36, runtime_model_count=28, registry_visible_model_count=31, active_rerank_measurement_model_count=1
```
(Note: `version` field in /api/health remains `V20.3.36`; this is the pattern used by all V20.3.37.x entries — changelog version differs from health endpoint version.)

### 3.6 Real Google API smoke (3/3 PASSED)
| registry_id | api_id | latency | tokens | reply | finish_reason |
|---|---|---|---|---|---|
| `gemini-3.1-pro` | `gemini-3.1-pro-preview` | 2.54s | total 151 (in 9, out 2, ~140 thinking) | `PONG` | STOP |
| `gemini-3-flash` | `gemini-3-flash-preview` | 1.40s | total 57 (in 9, out 2) | `PONG` | STOP |
| `gemma-4-31b` | `gemma-4-31b-it` | 2.56s | total 65 (in 9, out 2) | `PONG` | STOP |

Verdict: `ALL_API_SMOKE_OK`.

---

## 4. Hash guard

| Table | Pre-V55 hash | Post-V55 expected | Note |
|---|---|---|---|
| `predictions` | unchanged | unchanged | no scoring/voting code path touched |
| `final_bundles` | unchanged | may shift only via natural startup catch-up `updated_at/verified_at`; BT/lo2/status content unchanged |
| `lottery_results` | unchanged | unchanged |
| `model_daily_eval` | unchanged | unchanged |
| `scheduler_logs` | grew by ~30-50 rows | natural restart logging |

(Code-file hashes BEFORE → AFTER on VPS:
- `model_registry.py`: `f062…363c` → `0dec…627d8`
- `gpt_analyzer.py`: `8a09…b813` → `16cf…2ec8` then re-deployed once after `GOOGLE_MODEL_API_MAP` correction
- `.env` (project-root): `c799…400d` (backend stays) + new `f1824…32df` for project-root after key append)

---

## 5. Risk and rollback

### Risk
- Gemini 3.1 Pro is a thinking model. Production `_call_gemini` already uses `max_output_tokens=65536`, well above thinking budget needed (~140-200 tokens), so it will not hit `MAX_TOKENS` like the 64-token smoke probe initially did.
- New shadow batch increases per-cycle Google API calls by 3 per region (≤9 calls/day extra). Shadow lane has its own retry/circuit logic.
- `*-preview` API names are current as of 2026-05-05 ListModels. If Google graduates them, only `GOOGLE_MODEL_API_MAP` needs updating.
- Output roster is unchanged; `/du-doan` cannot be affected.

### Rollback (if needed)
1. SSH VPS, restore from backup:
   ```bash
   BK=/root/Lottery_AI_Test/backups/v55_shadow_add_20260505_0750
   cp $BK/model_registry.py.bak  /root/Lottery_AI_Test/web/backend/model_registry.py
   cp $BK/gpt_analyzer.py.bak    /root/Lottery_AI_Test/web/backend/gpt_analyzer.py
   cp $BK/project_root_env.bak   /root/Lottery_AI_Test/.env
   systemctl restart lottery
   ```
2. Confirm `/api/health` HTTP 200 and `registry_visible_model_count=28`.

---

## 6. Next steps (not in this pass)

- Watch first natural shadow cascade for the 3 new IDs (today's `ai_chain_post_verify` + `shadow_eval_post_verify` after MN/MT/MB results).
- After 3-5 clean closeouts, evaluate WR/BT and PHASE-FIRST contract field population vs. cohort `PFG-20260505-E`.
- After 14+ valid days, owner-decide whether any of the three should graduate (would require explicit `output_eligible=True` change — not part of V55).

---

## 7. Cross-references

- Workspace rules followed: `live-data-integrity.mdc`, `governance-traceability-automation.mdc`, `active-roadmap-precedence.mdc`.
- CHANGELOG: `V20.3.37.55`.
- SSOT row: `V55 add 3 Google direct shadow models`.
- Tracker item: `FU-125`.
- Active roadmap history row: `2026-05-05`.
- Verification scripts: `artifacts/_v55_vps_backup_and_envcheck.sh`, `_v55_vps_apply.sh`, `_v55_fix_envpath.sh`, `_v55_vps_verify.py`, `_v55_envload_check.py`, `_v55_post_restart_check.py`, `_v55_api_smoke.py`, `_v55_list_models.py`.
