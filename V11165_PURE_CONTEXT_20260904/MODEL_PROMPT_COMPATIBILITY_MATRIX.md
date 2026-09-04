# MODEL_PROMPT_COMPATIBILITY_MATRIX — V11165 · GATE 8

**Do ngay:** 2026-09-04 · **Pham vi:** toan bo LLM `active` + `shadow` (19 model, class=TOKEN role=GENERATOR).
**Nguon ma:** `web/backend` tren VPS production (hash khoa o Gate 0). **Nguon so:** `prediction_trace.jsonl` (van tay do CHINH ham dang serve ghi ra) + clone bat bien `artifacts/v11165_immutable.db` (`mode=ro`).
**Cua so do:** 2026-08-06 → 2026-09-04 (30 ngay, 1.777 luot) va rieng ngay 2026-09-04 (60 luot).

> **RM-14:** moi con so ve prompt lay tu `runtime_prompt_chars` (`gpt_analyzer.py:6723`) va `prompt_total_chars` (`:6868`) — hai truong do chinh ham dang phuc vu tu bam/tu dem, KHONG doc tai lieu.
> **RM-10:** moi ten ham / ten bang / ten tham so duoi day deu quet ra bang `grep`/`AST`/`PRAGMA`, khong doan theo ten.
> **RM-21:** ban dau ma tran nay muon hang so **160 token/s** (do cho `deepseek-reasoner` o V11158) ap cho moi model. Da **bo**, do lai toc do cho **chinh tung model**.

**Tep goc may doc:** `artifacts/v11165_h8_model_matrix.json` · sha256 `85f009622bb4d7fe0976e7b0499c1cb37ce56485fc2ceece04104ac87d55d688`

---

## 1. Ket luan ngan

| # | Ket luan | Phan loai |
|---|---|---|
| 1 | `gpt-oss-120b` — model **OFFICIAL, `output_eligible=True`** — nhan **goi ngu canh SHADOW** o **88/88** luot official trong 30 ngay (`+2.535` ky tu trung binh, toi da `+3.269`). Goi shadow them **2 khoi** ma 7 model official khac KHONG co: `MINED RULES — PHASE-STATE CLASSIFICATION` (`:5059`) va `PHASE-FIRST REASONING GATE — 8 buoc BAT BUOC` (`:5849`). | `PROVEN_DEFECT` |
| 2 | Hai payload khac han nhau dang mang **cung mot nhan** `prompt_version=PB-20.1` va **cung** `prompt_layers={SP-4.4, RR-16.5, CTX-18.6, PB-20.1}`. Ngay 04/09: 60 luot → **60 van tay sha256 khac nhau**, hai regime (`LEGACY_PROMPT` 27 luot, `CONTEXT_ONLY_V2` 33 luot), hai bien goi ngu canh. | `PROVEN_DEFECT` |
| 3 | **KHONG co bat ky co che cat dau vao nao**: khong uu tien section, khong phien ban hoa thu tu cat, khong ghi section bi bo, khong bam payload sau cat. `grep` `user_prompt[:` / `system_prompt[:` / `_ctx_pack[:` / `MAX_INPUT` = **0 dong**. | `PROVEN_DEFECT` |
| 4 | **Khong model nao co context window khai trong ma.** `grep 'context_window\|ctx_window\|CONTEXT_WINDOW'` = 0 dong. He **khong the** biet prompt co vua khong, nen cung khong the co bien an toan dau vao. | `PROVEN_DEFECT` |
| 5 | **Tool calling KHONG BAT o bat ky model nao.** `grep` `"tools":` / `tool_choice` / `function_call` / `tools=` / `parallel_tool_calls` tren toan `web/backend` = **0 dong**. Prompt **khong duoc** bao model "tu truy van". | `EXPECTED_BEHAVIOR` (nhung rang buoc thiet ke) |
| 6 | Van tay `runtime_prompt_sha256` bam **TRUOC** khi noi `ctx_pack` + `REASONING_RULEBOOK` (`:6723` vs `:6755-6762`) → chi phu **44,1%** chuoi that (n=60, p5 40,1% · p95 48,3%). | `PROVEN_DEFECT` |
| 7 | Prompt **OFFICIAL** con day du **4/5 dau o nhiem** owner cam: ten model + `win_rate` + `weight` + menh lenh *"AI nen uu tien patterns tu models co win_rate cao hon"* (`:3040-3043`), `Win Rate` (`:2991`), `SO DA TRUNG GAN DAY` (`:3006`), `THAM KHAO hieu suat gan day` (`:3185`). Do duoc: `contam_hits=4` o **ca 27** luot `LEGACY_PROMPT` ngay 04/09, `=0` o ca 33 luot `CONTEXT_ONLY_V2`. | `PROVEN_DEFECT` |
| 8 | `PHASE_FIRST_CONTRACT_MODELS = set()` (rong) — khoi `PHASE_FIRST_JSON_CONTRACT` (1.343 ky tu) **khong bao gio** duoc noi vao prompt. Nhung goi ngu canh shadow van bom cau *"OUTPUT KHONG HOP LE neu thieu bat ky field nao"* (`:5861`) trong khi **khong co** buoc kiem nao chay. | `PROVEN_DEFECT` (`PRJ_PROMPT_CONTRADICTS`) |
| 9 | `SHADOW_GATE_MODELS` co 8 thanh vien: **6 RETIRED**, 1 `SHADOW_AUTO`, 1 **`ACTIVE`+`output_eligible`**. Danh sach 75% chet nay la thu duy nhat dieu khien `_shadow_mode` o `:6738`. | `PROVEN_DEFECT` |
| 10 | `deepseek-v4-pro-real`: `max_tokens = 393.216` nhung `hard_timeout = 300s`. Toc do gop do RIENG model p95 = 330,8 tok/s → can tren ~**99.240** token trong 300s. Tran dat cao gap ~4 lan muc voi toi duoc. Do duoc **12/89 luot vuot 300s**. | `PROVEN_DEFECT` |
| 11 | Goi ngu canh **bi bo ca goi** khi `len <= CTX_PACK_SAN=500`: 3 cap (ngay,mien) × 12 model shadow = **36 luot** chay **khong co ngu canh nao** (06/08 MB · 07/08 MB · 08/08 MN, `cpc=64`). Trace **khong co co** danh dau viec nay. | `PROVEN_DEFECT` |
| 12 | `gemini-2.5-flash` (official) va `gemini-3.5-flash`: co luot **reasoning tokens an 96,0% tran dau ra** (62.912/65.536 va 62.911/65.536), chi con ~2.600 token cho JSON. Moi model **1 luot** trong 30 ngay ⇒ theo `RM-04` **chua duoc phep ket luan** ve ty le, nhung **co che da tai lap duoc**. | `SUSPICIOUS_NEEDS_MORE_EVIDENCE` |
| 13 | Pool `combo_super.AI_MODELS` co **9** model, trong do **2 model `shadow_only=True`** (`gemini-3.5-flash`, `gemini-3.6-flash`) — tuc model shadow **co the bo phieu vao output official** qua duong combo-super. Ghi chu registry "4ML + 7AI" da **cu**. | `SUSPICIOUS_NEEDS_MORE_EVIDENCE` |

---

## 2. Ma tran chinh — dinh tuyen · ngan sach · kha nang

| Model | Status / out | Provider THAT | Route | max_output | Nguon tran | JSON co cau truc | system/user | reasoning | tool calling |
|---|---|---|---|---:|---|---|---|---|---|
| `claude-opus-4-6` | ACTIVE / ✅ | anthropic (SDK anthropic) | api.anthropic.com · model=claude-opus-4-6 | 16384 | HARD-CODE :3403 token_limit=16384 (KHONG doc _MODEL_MAX_TOKENS) | KHONG co che JSON co cau truc — chi noi them cau «tra ve DUNG JSON» vao system (:3443) | system= native + messages=[user] (:3479) | khong gui tham so reasoning (chi bat khi id ket thuc '-thinking' — khong id nao trong roster) | KHONG BAT |
| `claude-sonnet-4-6` | ACTIVE / ✅ | anthropic (SDK anthropic) | api.anthropic.com · model=claude-sonnet-4-6 | 16384 | HARD-CODE :3403 token_limit=16384 (KHONG doc _MODEL_MAX_TOKENS) | KHONG co che JSON co cau truc — chi noi them cau «tra ve DUNG JSON» vao system (:3443) | system= native + messages=[user] (:3479) | khong gui tham so reasoning (chi bat khi id ket thuc '-thinking' — khong id nao trong roster) | KHONG BAT |
| `deepseek-reasoner` | ACTIVE / ✅ | deepseek (SDK openai, base_url=api.deepseek.com) | api.deepseek.com · model=deepseek-v4-flash · thinking=True | 49152 | _DIRECT_DEEPSEEK_SHADOW_MAX_TOKENS[:173] -> 49152 (mac dinh 16384) | KHONG (thinking gop system+user, khong gui response_format :3664) | GOP system+user thanh 1 message user (:3660-3661) | extra_body={'thinking':{'type':'enabled'}} (:3668) | KHONG BAT |
| `gemini-2.5-flash` | ACTIVE / ✅ | google (SDK google.genai) | generativelanguage · model=gemini-2.5-flash | 65536 | HARD-CODE :3546 max_output_tokens=65536 — GOM CA thinking tokens | CO response_mime_type='application/json' (:3547) | system_instruction= + contents=user_prompt (:3541-3548) | thinking dong (khong dat thinking_budget) · doc thoughts_token_count (:3615) | KHONG BAT |
| `gemini-2.5-pro` | ACTIVE / ✅ | google (SDK google.genai) | generativelanguage · model=gemini-2.5-pro | 65536 | HARD-CODE :3546 max_output_tokens=65536 — GOM CA thinking tokens | CO response_mime_type='application/json' (:3547) | system_instruction= + contents=user_prompt (:3541-3548) | thinking dong (khong dat thinking_budget) · doc thoughts_token_count (:3615) | KHONG BAT |
| `glm-5.1` | ACTIVE / ✅ | openrouter (raw httpx, KHONG dung SDK) | openrouter.ai/api/v1/chat/completions · slug=z-ai/glm-5.1 | 24576 | _MODEL_MAX_TOKENS[:3885] -> 24576 | CO response_format=json_object (:4058), co chuoi lui 4 buoc neu provider tu choi | system + user, user duoc noi them cau «CHI tra ve JSON» (:4022-4025) | khong gui truong reasoning | KHONG BAT |
| `gpt-5.4` | ACTIVE / ✅ | openai (SDK openai) | api.openai.com · model=gpt-5.4 | 16384 | HARD-CODE :3347 max_completion_tokens=16384 (KHONG doc _MODEL_MAX_TOKENS) | CO response_format=json_object (:3335). Luoc do json_schema chi dung cho o-series (:3227) | system + user (:3323-3326) | khong gui tham so reasoning | KHONG BAT |
| `gpt-oss-120b` | ACTIVE / ✅ | openrouter (raw httpx, KHONG dung SDK) | openrouter.ai/api/v1/chat/completions · slug=openai/gpt-oss-120b | 24576 | _MODEL_MAX_TOKENS[:3885] -> 24576 | CO response_format=json_object (:4058), co chuoi lui 4 buoc neu provider tu choi | system + user, user duoc noi them cau «CHI tra ve JSON» (:4022-4025) | khong gui truong reasoning | KHONG BAT |
| `claude-opus-5-fast` | SHADOW_AUTO / — | openrouter (raw httpx, KHONG dung SDK) | openrouter.ai/api/v1/chat/completions · slug=anthropic/claude-opus-5-fast | 32768 | _MODEL_MAX_TOKENS[:3885] -> 32768 | CO response_format=json_object (:4058), co chuoi lui 4 buoc neu provider tu choi | system + user, user duoc noi them cau «CHI tra ve JSON» (:4022-4025) | khong gui truong reasoning | KHONG BAT |
| `deepseek-v4-pro-real` | SHADOW_AUTO / — | deepseek (SDK openai, base_url=api.deepseek.com) | api.deepseek.com · model=deepseek-v4-pro · thinking=True | 393216 | _DIRECT_DEEPSEEK_SHADOW_MAX_TOKENS[:173] -> 393216 (mac dinh 16384) | KHONG (thinking gop system+user, khong gui response_format :3664) | GOP system+user thanh 1 message user (:3660-3661) | extra_body={'thinking':{'type':'enabled'}} (:3668) | KHONG BAT |
| `gemini-3.5-flash` | SHADOW_AUTO / — | google (SDK google.genai) | generativelanguage · model=gemini-3.5-flash · 503 -> OpenRouter google/gemini-3.5-flash (:3576) | 65536 | HARD-CODE :3546 max_output_tokens=65536 — GOM CA thinking tokens | CO response_mime_type='application/json' (:3547) | system_instruction= + contents=user_prompt (:3541-3548) | thinking dong (khong dat thinking_budget) · doc thoughts_token_count (:3615) | KHONG BAT |
| `gemini-3.6-flash` | SHADOW_AUTO / — | google (SDK google.genai) | generativelanguage · model=gemini-3.6-flash · 503 -> OpenRouter google/gemini-3.6-flash (:3576) | 65536 | HARD-CODE :3546 max_output_tokens=65536 — GOM CA thinking tokens | CO response_mime_type='application/json' (:3547) | system_instruction= + contents=user_prompt (:3541-3548) | thinking dong (khong dat thinking_budget) · doc thoughts_token_count (:3615) | KHONG BAT |
| `glm-5.2` | SHADOW_AUTO / — | openrouter (raw httpx, KHONG dung SDK) | openrouter.ai/api/v1/chat/completions · slug=z-ai/glm-5.2 | 49152 | _MODEL_MAX_TOKENS[:3885] -> 49152 | CO response_format=json_object (:4058), co chuoi lui 4 buoc neu provider tu choi | system + user, user duoc noi them cau «CHI tra ve JSON» (:4022-4025) | khong gui truong reasoning | KHONG BAT |
| `gpt-5-mini` | SHADOW_AUTO / — | openai (SDK openai) | api.openai.com · model=gpt-5-mini | 16384 | HARD-CODE :3347 max_completion_tokens=16384 (KHONG doc _MODEL_MAX_TOKENS) | CO response_format=json_object (:3335). Luoc do json_schema chi dung cho o-series (:3227) | system + user (:3323-3326) | khong gui tham so reasoning | KHONG BAT |
| `gpt-5.5` | SHADOW_AUTO / — | openrouter (raw httpx, KHONG dung SDK) | openrouter.ai/api/v1/chat/completions · slug=openai/gpt-5.5 | 24576 | _MODEL_MAX_TOKENS[:3885] -> 24576 | CO response_format=json_object (:4058), co chuoi lui 4 buoc neu provider tu choi | system + user, user duoc noi them cau «CHI tra ve JSON» (:4022-4025) | reasoning={'effort':'high'} (:4066) | KHONG BAT |
| `gpt-5.6-sol-pro` | SHADOW_AUTO / — | openrouter (raw httpx, KHONG dung SDK) | openrouter.ai/api/v1/chat/completions · slug=openai/gpt-5.6-sol-pro | 32768 | _MODEL_MAX_TOKENS[:3885] -> 32768 | CO response_format=json_object (:4058), co chuoi lui 4 buoc neu provider tu choi | system + user, user duoc noi them cau «CHI tra ve JSON» (:4022-4025) | khong gui truong reasoning | KHONG BAT |
| `grok-4.3` | SHADOW_AUTO / — | openrouter (raw httpx, KHONG dung SDK) | openrouter.ai/api/v1/chat/completions · slug=x-ai/grok-4.3 | 24576 | _MODEL_MAX_TOKENS[:3885] -> 24576 | CO response_format=json_object (:4058), co chuoi lui 4 buoc neu provider tu choi | system + user, user duoc noi them cau «CHI tra ve JSON» (:4022-4025) | reasoning={'effort':'high'} (:4066) | KHONG BAT |
| `qwen3-max-thinking` | SHADOW_AUTO / — | openrouter (raw httpx, KHONG dung SDK) | openrouter.ai/api/v1/chat/completions · slug=qwen/qwen3-max-thinking | 24576 | _MODEL_MAX_TOKENS[:3885] -> 24576 | CO response_format=json_object (:4058), co chuoi lui 4 buoc neu provider tu choi | system + user, user duoc noi them cau «CHI tra ve JSON» (:4022-4025) | reasoning={'exclude':True} (:4068) | KHONG BAT |
| `qwen3.7-max` | SHADOW_AUTO / — | openrouter (raw httpx, KHONG dung SDK) | openrouter.ai/api/v1/chat/completions · slug=qwen/qwen3.7-max | 32768 | _MODEL_MAX_TOKENS[:3885] -> 32768 | CO response_format=json_object (:4058), co chuoi lui 4 buoc neu provider tu choi | system + user, user duoc noi them cau «CHI tra ve JSON» (:4022-4025) | reasoning={'effort':'high'} (:4066) | KHONG BAT |

### 2b. Ngan sach thoi gian · retry · circuit breaker · parser

| Model | hard_timeout | soft_continue | HTTP timeout | Retry | Circuit breaker | temperature |
|---|---:|---:|---|---|---|---|
| `claude-opus-4-6` | 300s | 90s | KHONG DAT timeout -> mac dinh SDK anthropic (600s) | 1 lan lui khi loi chua chu 'temperature'; opus dung stream (:3449) tranh loi 'Streaming is required' | KHONG | temperature=0; neu bi tu choi -> retry temperature=1 (:3484) |
| `claude-sonnet-4-6` | 300s | 90s | KHONG DAT timeout -> mac dinh SDK anthropic (600s) | 1 lan lui khi loi chua chu 'temperature'; opus dung stream (:3449) tranh loi 'Streaming is required' | KHONG | temperature=0; neu bi tu choi -> retry temperature=1 (:3484) |
| `deepseek-reasoner` | 480s | 90s | KHONG DAT timeout -> mac dinh SDK openai (600s) | KHONG retry — loi la tra {'error': ...} ngay (:3670) | KHONG | khong gui temperature khi thinking |
| `gemini-2.5-flash` | 300s | 90s | KHONG DAT timeout -> mac dinh SDK google.genai | retry 429/503 [5,15,30]s (:3533,:3587) + 503 nhay thang OpenRouter neu co slug | KHONG (tru khi roi qua nhanh OpenRouter) | temperature=0, top_p=0.95, top_k=40 (:3543-3545) |
| `gemini-2.5-pro` | 300s | 90s | KHONG DAT timeout -> mac dinh SDK google.genai | retry 429/503 [5,15,30]s (:3533,:3587) + 503 nhay thang OpenRouter neu co slug | KHONG (tru khi roi qua nhanh OpenRouter) | temperature=0, top_p=0.95, top_k=40 (:3543-3545) |
| `glm-5.1` | 840s | 90s | httpx timeout=300.0 (:4089) | 4 buoc lui (json+temp / json / temp / tran) x retry HTTP 429,502,503,520,524 voi [5,15,30]s (:4080-4108) | CO — 600s (credit/incompatible/empty/cost) · 90s (429) (:3790-3792) | temperature=0; lui bo temperature neu bi tu choi (:4055) |
| `gpt-5.4` | 300s | 90s | KHONG DAT timeout -> mac dinh SDK openai (600s) | lui max_completion_tokens->max_tokens hoac bo temperature (:3349-3365) | KHONG | KHONG dat temperature (gpt-5* khong ho tro temperature=0, :3339) |
| `gpt-oss-120b` | 900s | 90s | httpx timeout=300.0 (:4089) | 4 buoc lui (json+temp / json / temp / tran) x retry HTTP 429,502,503,520,524 voi [5,15,30]s (:4080-4108) | CO — 600s (credit/incompatible/empty/cost) · 90s (429) (:3790-3792) | temperature=0; lui bo temperature neu bi tu choi (:4055) |
| `claude-opus-5-fast` | 300s | 90s | httpx timeout=300.0 (:4089) | 4 buoc lui (json+temp / json / temp / tran) x retry HTTP 429,502,503,520,524 voi [5,15,30]s (:4080-4108) | CO — 600s (credit/incompatible/empty/cost) · 90s (429) (:3790-3792) | temperature=0; lui bo temperature neu bi tu choi (:4055) |
| `deepseek-v4-pro-real` | 300s | 90s | KHONG DAT timeout -> mac dinh SDK openai (600s) | KHONG retry — loi la tra {'error': ...} ngay (:3670) | KHONG | khong gui temperature khi thinking |
| `gemini-3.5-flash` | 300s | 90s | KHONG DAT timeout -> mac dinh SDK google.genai | retry 429/503 [5,15,30]s (:3533,:3587) + 503 nhay thang OpenRouter neu co slug | KHONG (tru khi roi qua nhanh OpenRouter) | temperature=0, top_p=0.95, top_k=40 (:3543-3545) |
| `gemini-3.6-flash` | 300s | 90s | KHONG DAT timeout -> mac dinh SDK google.genai | retry 429/503 [5,15,30]s (:3533,:3587) + 503 nhay thang OpenRouter neu co slug | KHONG (tru khi roi qua nhanh OpenRouter) | temperature=0, top_p=0.95, top_k=40 (:3543-3545) |
| `glm-5.2` | 720s | 90s | httpx timeout=300.0 (:4089) | 4 buoc lui (json+temp / json / temp / tran) x retry HTTP 429,502,503,520,524 voi [5,15,30]s (:4080-4108) | CO — 600s (credit/incompatible/empty/cost) · 90s (429) (:3790-3792) | temperature=0; lui bo temperature neu bi tu choi (:4055) |
| `gpt-5-mini` | 300s | 90s | KHONG DAT timeout -> mac dinh SDK openai (600s) | lui max_completion_tokens->max_tokens hoac bo temperature (:3349-3365) | KHONG | KHONG dat temperature (gpt-5* khong ho tro temperature=0, :3339) |
| `gpt-5.5` | 300s | 90s | httpx timeout=300.0 (:4089) | 4 buoc lui (json+temp / json / temp / tran) x retry HTTP 429,502,503,520,524 voi [5,15,30]s (:4080-4108) | CO — 600s (credit/incompatible/empty/cost) · 90s (429) (:3790-3792) | temperature=0; lui bo temperature neu bi tu choi (:4055) |
| `gpt-5.6-sol-pro` | 300s | 90s | httpx timeout=300.0 (:4089) | 4 buoc lui (json+temp / json / temp / tran) x retry HTTP 429,502,503,520,524 voi [5,15,30]s (:4080-4108) | CO — 600s (credit/incompatible/empty/cost) · 90s (429) (:3790-3792) | temperature=0; lui bo temperature neu bi tu choi (:4055) |
| `grok-4.3` | 300s | 90s | httpx timeout=300.0 (:4089) | 4 buoc lui (json+temp / json / temp / tran) x retry HTTP 429,502,503,520,524 voi [5,15,30]s (:4080-4108) | CO — 600s (credit/incompatible/empty/cost) · 90s (429) (:3790-3792) | temperature=0; lui bo temperature neu bi tu choi (:4055) |
| `qwen3-max-thinking` | 300s | 90s | httpx timeout=300.0 (:4089) | 4 buoc lui (json+temp / json / temp / tran) x retry HTTP 429,502,503,520,524 voi [5,15,30]s (:4080-4108) | CO — 600s (credit/incompatible/empty/cost) · 90s (429) (:3790-3792) | temperature=0; lui bo temperature neu bi tu choi (:4055) |
| `qwen3.7-max` | 480s | 90s | httpx timeout=300.0 (:4089) | 4 buoc lui (json+temp / json / temp / tran) x retry HTTP 429,502,503,520,524 voi [5,15,30]s (:4080-4108) | CO — 600s (credit/incompatible/empty/cost) · 90s (429) (:3790-3792) | temperature=0; lui bo temperature neu bi tu choi (:4055) |

**Parser — dung chung 100%, khong nhanh rieng theo model:**

> `_parse_ai_json_payload` (`:1294`) → go rao ```` ```json ```` → `json.loads` chat → `_tim_json_lech_dau` (`:1270`) → nhanh `Extra data` quet ngoac → `raw_decode` → va cat V5.9.5 (`:7117`) → `_repair_json_lenient` (`:4619`). `grep selected_model` trong vung parse (`:7090-7183`) chi ra **4 dong**, deu la ghi nhan, khong phai re nhanh.

**Locale / Unicode — dung chung, khong xu ly rieng theo model:**

> Prompt tieng Viet co dau + emoji (🏆 ✅ 🔒) + ky tu ve khung `U+2550..U+255D` (khoi `PHASE-FIRST GATE`). Bam van tay `.encode('utf-8','replace')` (`:6724`). stdout boc `_safe_stdio_ctx` (`:44`) chong loi ma hoa console. **Khong co** buoc chuan hoa/kiem tra Unicode rieng cho provider nao.

---

## 3. So DO DUOC — 30 ngay (2026-08-06 → 2026-09-04)

| Model | n | prompt_total ky tu p50 / max | ctx_pack p50 | token p50 / max | reasoning max | latency p50 / p95 / max | finish_reason |
|---|---:|---|---:|---|---:|---|---|
| `claude-opus-4-6` | 114 | 50666.0 / 57644.0 | 10581.0 | 31116.0 / 35276.0 | None | 52.6 / 61.6 / 71.4 | end_turn=114 |
| `claude-sonnet-4-6` | 95 | 50792.0 / 57651.0 | 10599.0 | 31863.0 / 36427.0 | None | 52.7 / 70.6 / 85.0 | end_turn=95 |
| `deepseek-reasoner` | 108 | 50654.0 / 57772.0 | 10571.0 | 47557.0 / 68692.0 | 43323.0 | 188.8 / 275.9 / 367.3 | stop=108 |
| `gemini-2.5-flash` | 112 | 50787.0 / 57648.0 | 10676.0 | 30837.0 / 86468.0 | 62912.0 | 37.4 / 47.7 / 223.2 | FinishReason.STOP=112 |
| `gemini-2.5-pro` | 115 | 50738.0 / 57646.0 | 10668.0 | 26918.0 / 30896.0 | 4933.0 | 36.7 / 45.7 / 51.5 | FinishReason.STOP=115 |
| `glm-5.1` | 88 | 50854.0 / 57716.0 | 10672.0 | 29788.0 / 47726.0 | 22683.0 | 139.2 / 561.9 / 1429.5 | length=1, stop=87 |
| `gpt-5.4` | 89 | 50867.0 / 57659.0 | 10668.0 | 22459.0 / 25655.0 | None | 15.5 / 20.3 / 25.4 | stop=89 |
| `gpt-oss-120b` | 88 | 53865.0 / 60754.0 | 13692.0 | 27731.0 / 46813.0 | 6876.0 | 91.8 / 203.6 / 324.1 | length=1, stop=87 |
| `claude-opus-5-fast` | 89 | 55342.0 / 62267.0 | 13651.0 | 43361.0 / 49676.0 | 8720.0 | 33.0 / 43.8 / 61.8 | error=1, stop=88 |
| `deepseek-v4-pro-real` | 89 | 55300.0 / 62249.0 | 13651.0 | 42312.0 / 53761.0 | 22818.0 | 223.9 / 329.8 / 371.1 | stop=89 |
| `gemini-3.5-flash` | 94 | 55319.0 / 62399.0 | 13645.0 | 30946.0 / 88332.0 | 62911.0 | 32.6 / 68.3 / 198.5 | FinishReason.STOP=93, stop=1 |
| `gemini-3.6-flash` | 90 | 55369.0 / 62419.0 | 13651.0 | 28850.0 / 33600.0 | 5174.0 | 25.1 / 63.6 / 111.2 | FinishReason.STOP=86, stop=4 |
| `glm-5.2` | 72 | 55249.0 / 61720.0 | 13563.0 | 31905.0 / 47369.0 | 23113.0 | 87.6 / 216.3 / 957.1 | stop=72 |
| `gpt-5-mini` | 89 | 55321.0 / 62181.0 | 13651.0 | 29032.0 / 35636.0 | None | 65.5 / 101.0 / 120.6 | stop=89 |
| `gpt-5.5` | 89 | 55284.0 / 62236.0 | 13651.0 | 34664.0 / 40693.0 | 14123.0 | 144.7 / 257.7 / 1159.7 | stop=89 |
| `gpt-5.6-sol-pro` | 89 | 55289.0 / 62232.0 | 13651.0 | 121729.0 / 135745.0 | 9410.0 | 100.7 / 155.8 / 377.7 | stop=89 |
| `grok-4.3` | 89 | 55308.0 / 62260.0 | 13650.0 | 26746.0 / 30208.0 | 6131.0 | 33.2 / 57.6 / 90.0 | stop=89 |
| `qwen3-max-thinking` | 89 | 55420.0 / 62221.0 | 13651.0 | 25330.0 / 28887.0 | 0.0 | 25.6 / 41.4 / 52.6 | stop=89 |
| `qwen3.7-max` | 89 | 55420.0 / 62280.0 | 13651.0 | 34596.0 / 49433.0 | 23083.0 | 165.2 / 342.0 / 430.1 | stop=89 |

### 3b. Bien an toan do RIENG cho tung model (RM-21)

| Model | tok/s gop p50 / p95 | Can tren token sinh trong hard_timeout | max_output | Tran co voi toi duoc? | Vuot hard_timeout 30 ngay |
|---|---|---:|---:|---|---|
| `claude-opus-4-6` | 586.3 / 719.0 | 215700 | 16384 | CO | 0/114 |
| `claude-sonnet-4-6` | 611.6 / 712.6 | 213780 | 16384 | CO | 0/95 |
| `deepseek-reasoner` | 255.2 / 347.4 | 166752 | 49152 | CO | 0/108 |
| `gemini-2.5-flash` | 824.4 / 1005.6 | 301680 | 65536 | CO | 0/112 |
| `gemini-2.5-pro` | 752.3 / 868.0 | 260400 | 65536 | CO | 0/115 |
| `glm-5.1` | 223.6 / 635.6 | 533904 | 24576 | CO | 2/88 |
| `gpt-5.4` | 1454.7 / 1866.6 | 559980 | 16384 | CO | 0/89 |
| `gpt-oss-120b` | 308.5 / 1274.9 | 1147410 | 24576 | CO | 0/88 |
| `claude-opus-5-fast` | 1320.0 / 1620.9 | 486270 | 32768 | CO | 0/89 |
| `deepseek-v4-pro-real` | 189.3 / 330.8 | 99240 | 393216 | KHONG — tran 393216 > can tren 99240 | 12/89 |
| `gemini-3.5-flash` | 955.7 / 1318.5 | 395550 | 65536 | CO | 0/94 |
| `gemini-3.6-flash` | 1177.1 / 1615.3 | 484590 | 65536 | CO | 0/90 |
| `glm-5.2` | 376.6 / 1109.6 | 798911 | 49152 | CO | 1/72 |
| `gpt-5-mini` | 451.9 / 646.4 | 193920 | 16384 | CO | 0/89 |
| `gpt-5.5` | 239.0 / 354.2 | 106260 | 24576 | CO | 1/89 |
| `gpt-5.6-sol-pro` | 1206.1 / 1654.1 | 496230 | 32768 | CO | 2/89 |
| `grok-4.3` | 802.1 / 1149.5 | 344850 | 24576 | CO | 0/89 |
| `qwen3-max-thinking` | 1035.6 / 1381.8 | 414540 | 24576 | CO | 0/89 |
| `qwen3.7-max` | 206.7 / 312.6 | 150048 | 32768 | CO | 0/89 |

> `tok/s gop` = `token_count / latency_seconds`, **gom ca token dau vao** ⇒ day la **CAN TREN** cua toc do sinh, khong phai toc do sinh that. Dung no lam nguong «tran co voi toi duoc khong» la **bao thu dung chieu**: neu ngay ca can tren cung khong voi toi tran thi tran chac chan khong voi toi duoc.

---

## 4. Kiem BAT BUOC — thong tin ngu nghia co TUONG DUONG giua cac model khong?

### 4.1 Thuoc do

`context_pack_chars` — do dai khoi ngu canh **thuc su bom vao prompt**, do chinh ham dang serve ghi ra (`:6773 _ctx_len = len(_ctx_pack)` → `:6853`). So sanh **trong cung** `(ngay, mien, nhom vai tro)`.

### 4.2 Ket qua — nhom OFFICIAL (8 model `output_eligible`)

| Model | So luot LECH khoi chuan cua chinh nhom | Tong luot | delta trung binh | delta min | delta max |
|---|---:|---:|---:|---:|---:|
| **`gpt-oss-120b`** | **88** | **88** | **+2.534,9** | −14.526 | +3.269 |
| `gpt-5.4` | 0 | 89 | — | — | — |
| `gemini-2.5-flash` | 0 | 112 | — | — | — |
| `gemini-2.5-pro` | 0 | 115 | — | — | — |
| `claude-sonnet-4-6` | 0 | 95 | — | — | — |
| `claude-opus-4-6` | 0 | 114 | — | — | — |
| `deepseek-reasoner` | 0 | 108 | — | — | — |
| `glm-5.1` | 0 | 88 | — | — | — |

**⇒ 88/88 = 100%.** `gpt-oss-120b` **chua bao gio** nhan cung goi ngu canh voi 7 model official con lai trong ca cua so 30 ngay. Do rieng ngay 04/09 (ca 3 mien deu `run_source` official — `auto_daily` MN, `ai_chain` MT/MB, tra tu clone bat bien):

| Mien | `gpt-oss-120b` cpc | 7 model official khac | Nhom shadow cung ngay/mien | Ket |
|---|---:|---:|---:|---|
| MN | **14.142** | 10.977 | 14.142 | **trung KHIT nhom shadow** |
| MT | **14.536** | 11.557 | 14.536 | **trung KHIT nhom shadow** |
| MB | **18.427** | 15.448 | 18.427 | **trung KHIT nhom shadow** |

### 4.3 Vi sao — nguyen nhan goc, doc thang tu ma dang serve

```python
# gpt_analyzer.py:6680-6682  — V11160 DA SUA cho regime prompt
_la_shadow        = bool(lane_test_shadow_pack) or (selected_model in SHADOW_GATE_MODELS)
_la_shadow_prompt = bool(lane_test_shadow_pack)   # ← tin hieu THEO LUOT, dung

# gpt_analyzer.py:6738  — VAN CON NGUYEN menh de THEO MODEL
_shadow_mode = lane_test_shadow_pack or (selected_model in SHADOW_GATE_MODELS)
_ctx_pack = build_context_pack(target_region, date_str, shadow_mode=_shadow_mode)   # :6740
```

V11160 sua **mot nua**: doi duoc **regime prompt** (`_ctx_only_lane`) sang tin hieu theo-luot, nhung **de nguyen** bien `_shadow_mode` cap cho `build_context_pack`. Ket qua do duoc ngay 04/09: `gpt-oss-120b` khai `context_only_regime=LEGACY_PROMPT`, `is_shadow_lane=False`, `contam_hits=4` (= dung prompt official) **nhung** `cpc` = dung so cua nhom shadow. Day la ho `A58_VIOLATION_HALF_DONE`.

### 4.4 Khac nhau O DAU — khong chi la "nhieu ky tu hon"

`shadow_mode=True` mo dung **hai** khoi trong `build_context_pack` (quet toan ham `:4831-5937`, `shadow_mode` xuat hien 9 lan, chi **2** lan la nhanh dieu kien sinh noi dung):

| Dong | Khoi | Noi dung |
|---|---|---|
| `:5059` | `if shadow_mode and _has_phase_funcs and rules:` | `### 🔒 MINED RULES — PHASE-STATE CLASSIFICATION (PB-18.0 shadow)` — phan loai tung luat thanh PRIMARY / SECONDARY / SHADOW / STALE / DROP |
| `:5849` | `if shadow_mode:` | `🔒 PHASE-FIRST REASONING GATE (PB-18.0 — BAT BUOC)` — *"Ban PHAI hoan tat 8 buoc nay TRUOC KHI chot so. OUTPUT KHONG HOP LE neu thieu bat ky field nao."* |

⇒ Mot model **official dang bo phieu vao bundle cong bo** dang chay duoi **mot hop dong suy luan khac** voi 7 model official con lai. Day khong phai khac dinh dang theo provider — day la khac **thong tin ngu nghia** va khac **rang buoc lap luan**.

⚠️ Va cau *"OUTPUT KHONG HOP LE neu thieu bat ky field nao"* la **loi de doa suong**: `PHASE_FIRST_CONTRACT_MODELS = set()` (`:1050`) nen `gate_contract_mode` luon `False`, khoi kiem `_phase_first_contract_missing_fields` (`:1190`) **khong bao gio** chay. → `PRJ_PROMPT_CONTRADICTS`.

### 4.5 Nhom SHADOW — 15 luot lech, da truy het nguyen nhan

| Nguyen nhan | So luot | Phan loai |
|---|---:|---|
| **Luot combo-super**: `gemini-3.5-flash` / `gemini-3.6-flash` nam trong `combo_super.AI_MODELS`; luot do goi qua `analyze_and_predict` **khong** co `lane_test_shadow_pack`, va hai model nay **khong** thuoc `SHADOW_GATE_MODELS` ⇒ nhan goi **official**. `cpc` trung **khit** gia tri official. | 8 | `EXPECTED_BEHAVIOR` |
| **Troi theo thoi diem goi**: `qwen3.7-max` (×4), `gpt-5-mini`, `glm-5.2`, `grok-4.3` chay cham hon cohort 5–10 phut; `cpc` **khong trung** ca gia tri shadow lan official ⇒ goi duoc dung lai o thoi diem khac, du lieu DB da khac. | 7 | `SUSPICIOUS_NEEDS_MORE_EVIDENCE` — chua dung lai duoc goi de chung minh (dung lai = goi `build_context_pack`, ngoai pham vi lan song 1) |

---

## 5. Kiem BAT BUOC — prompt vuot ngan sach thi he CAT THE NAO?

| Cau hoi cua de bai | Tra loi do duoc | Bang chung |
|---|---|---|
| Hien tai he cat the nao? | **KHONG CAT GI CA.** Chuoi duoc gui nguyen ven. | `grep -rE 'user_prompt\s*\[\s*:' web/backend --include=*.py` → **0 dong**; `system_prompt[:` → **0**; `_ctx_pack[:` → **0**. Lat cat duy nhat lien quan prompt la `raw_prompt[:CUSTOM_PROMPT_RUNTIME_MAX_CHARS]` (`:973`) — do la **custom prompt cua owner**, dang `ARCHIVE_ONLY`, `MAX_CHARS=500`, khong phai prompt lap rap. |
| Co section priority da phien ban hoa chua? | **CHUA CO.** Khong co bang uu tien, khong co thu tu bo. | AST `gpt_analyzer.py`: khong co hang so nao ten `*PRIORITY*` / `*SECTION_ORDER*`; `grep MAX_PROMPT\|PROMPT_MAX\|MAX_INPUT\|max_input` chi trung `knowledge_weights.py` (trong so hoc, khong lien quan). |
| Co ghi section nao bi bo khong? | **KHONG.** Chi mot truong hop bo — bo **ca goi ngu canh** khi `len <= 500` — va no chi in ra `print('[CONTEXT_PACK] No context data')` (`:6769`). Trace **khong co truong** nao khai "da bo goi". | Do duoc: 3 cap (ngay,mien) × 12 model = **36 luot** co `cpc=64` (06/08 MB · 07/08 MB · 08/08 MN). |
| Co bam payload SAU khi cat khong? | **KHONG** — va te hon: van tay bam **TRUOC** khi noi them. | `:6723` bam `system_prompt + '\n<<<USER>>>\n' + prompt`; `ctx_pack` + `REASONING_RULEBOOK` moi duoc noi vao o `:6755-6762`. Do phu do duoc: **44,1%** (n=60, p5 40,1% · p95 48,3%). |
| ⇒ Hai payload khac nhau co bi goi la cung mot prompt version khong? | **CO — `PROVEN_DEFECT`.** | Ngay 04/09: **60/60** luot deu `prompt_version=PB-20.1` va `prompt_layers={SP-4.4, RR-16.5, CTX-18.6, PB-20.1}`, `declared_but_inactive_layers=[]`; nhung sinh ra **60 van tay sha256 khac nhau**, **2 regime** (`LEGACY_PROMPT` 27 · `CONTEXT_ONLY_V2` 33), **2 bien goi ngu canh**, va `contam_hits` chia doi **4 vs 0**. |

**Hau qua truc tiep:** vi khong co context window trong ma (muc 1 · ket luan 4) nen he **khong the** biet prompt sap vuot; vi khong co co che cat nen neu co vuot thi provider tra 400 → roi vao chuoi lui 4 buoc → ca 4 buoc hong → `MODEL_INCOMPATIBLE` + circuit breaker 600s (`:4222-4230`). Tuc **loi ngan sach dau vao se hien ra duoi lop nguy trang "model khong tuong thich"**.

Muc prompt lon nhat quan sat duoc trong 30 ngay: **62.419 ky tu** (`gemini-3.6-flash`, MB). Chua co luot nao trung loi context-length, nen day la **rui ro chua kich hoat**, khong phai su co dang xay ra.

---

## 6. Prompt OFFICIAL van chua thu owner cam (doi chieu 9 muc tieu "thuan ngu canh")

`gpt_analyzer.py:6719-6726` tu dem 5 dau o nhiem tren chinh chuoi sap gui. Do duoc ngay 04/09:

| Regime | So luot | `contam_hits` |
|---|---:|---|
| `LEGACY_PROMPT` (8 model official) | 27 | **4** o ca 27 luot |
| `CONTEXT_ONLY_V2` (11 model shadow) | 33 | **0** o ca 33 luot |

Bon dau do nam o dau (phan loai theo `RM-09`, khong dem chuoi tho):

| Dong | Loai | Nguyen van | Vi pham muc tieu owner |
|---|---|---|---|
| `:3040` | `GHI_VAO_PROMPT` | `prompt += f"\n🏆 HIEU SUAT THEO MODEL ({target_region}, 30 ngay):\n"` | #5 — cam dung **ten model** |
| `:3042` | `GHI_VAO_PROMPT` | `prompt += f"  {model}: {stats['win_rate']:.0f}% ({wins}/{verified}) — weight={weight:.2f}\n"` | #5 — **ten model + win rate + trong so**, ca ba |
| `:3043` | `GHI_VAO_PROMPT` | `prompt += "  → AI nen uu tien patterns tu models co win_rate cao hon.\n"` | #5 va #8 — day LLM **bat chuoc nhau**, va la **KHUYEN NGHI** chu khong phai `CONDITION` |
| `:2991` | `GHI_VAO_PROMPT` | `prompt += f"  Win Rate: {perf['win_rate']:.1f}% ({wins}/{verified} verified)\n"` | #5 |
| `:3006` | `GHI_VAO_PROMPT` | `prompt += f"✅ SO DA TRUNG GAN DAY: {', '.join(hit_nums[:8])}\n"` | #3 — ro so da loc san |
| `:3185` | `TRONG_PROMPT` | `_yc.append("THAM KHAO hieu suat gan day va so da trung de dieu chinh confidence")` | #8 — dieu kien bi viet thanh **khuyen nghi** |

> `_deherd_strip_ranking` (`:4601`) **khong** cham duoc nhung dong nay: no chi loc **trong `_ctx_pack`** (`:6744`), con sau dong tren nam trong `create_analysis_prompt` — tuc trong phan **base prompt** da duoc dung **truoc** khi `_ctx_pack` duoc noi vao. Day dung la ho loi `A58_VIOLATION_HALF_DONE`.

**Ve muc tieu #6 ("khong bao model tu truy van neu khong co tool"):** ket luan **KHONG BAT tool calling** duoc chung minh bang `grep` toan `web/backend` cho 5 mau (`"tools":`, `tool_choice`, `function_call`, `tools=`, `parallel_tool_calls`) — **0 dong**. Nen moi cau trong prompt bao model "tu truy xuat" deu la menh lenh **khong the thi hanh**. (Viec quet tung cau trong prompt de tim menh lenh loai nay **chua lam** o gate nay — no thuoc gate prompt, va can dump prompt tu ham dang serve.)

---

## 7. Ket luan tuong thich tung model

| Model | Ket luan | Dieu kien kem theo |
|---|---|---|
| `claude-opus-4-6` | ✅ **TUONG THICH** | — |
| `claude-sonnet-4-6` | ✅ **TUONG THICH** | — |
| `deepseek-reasoner` | ⚠️ **TUONG THICH CO DIEU KIEN** | • reasoning_tokens_max 43323.0 an >=80% tran dau ra 49152 |
| `gemini-2.5-flash` | ⚠️ **TUONG THICH CO DIEU KIEN** | • reasoning_tokens_max 62912.0 an >=80% tran dau ra 65536 |
| `gemini-2.5-pro` | ✅ **TUONG THICH** | — |
| `glm-5.1` | ⚠️ **TUONG THICH CO DIEU KIEN** | • co 1 luot finish_reason=length trong 30 ngay<br>• reasoning_tokens_max 22683.0 an >=80% tran dau ra 24576<br>• 2/88 luot vuot hard_timeout 840s (scheduler NGUNG CHO; lane official mat phieu, lane shadow duoc late-fill) |
| `gpt-5.4` | ✅ **TUONG THICH** | — |
| `gpt-oss-120b` | ⚠️ **TUONG THICH CO DIEU KIEN** | • co 1 luot finish_reason=length trong 30 ngay<br>• nam trong SHADOW_GATE_MODELS NHUNG output_eligible=True -> nhan goi ngu canh shadow o luot OFFICIAL (:6738) |
| `claude-opus-5-fast` | ⚠️ **TUONG THICH CO DIEU KIEN** | • co 1 luot finish_reason=error |
| `deepseek-v4-pro-real` | ⚠️ **TUONG THICH CO DIEU KIEN** | • tran max_output 393216 KHONG voi toi duoc trong hard_timeout 300s (can tren do RIENG model: ~99240 token)<br>• 12/89 luot vuot hard_timeout 300s (scheduler NGUNG CHO; lane official mat phieu, lane shadow duoc late-fill) |
| `gemini-3.5-flash` | ⚠️ **TUONG THICH CO DIEU KIEN** | • reasoning_tokens_max 62911.0 an >=80% tran dau ra 65536 |
| `gemini-3.6-flash` | ✅ **TUONG THICH** | — |
| `glm-5.2` | ⚠️ **TUONG THICH CO DIEU KIEN** | • 1/72 luot vuot hard_timeout 720s (scheduler NGUNG CHO; lane official mat phieu, lane shadow duoc late-fill) |
| `gpt-5-mini` | ✅ **TUONG THICH** | — |
| `gpt-5.5` | ⚠️ **TUONG THICH CO DIEU KIEN** | • 1/89 luot vuot hard_timeout 300s (scheduler NGUNG CHO; lane official mat phieu, lane shadow duoc late-fill) |
| `gpt-5.6-sol-pro` | ⚠️ **TUONG THICH CO DIEU KIEN** | • 2/89 luot vuot hard_timeout 300s (scheduler NGUNG CHO; lane official mat phieu, lane shadow duoc late-fill) |
| `grok-4.3` | ✅ **TUONG THICH** | — |
| `qwen3-max-thinking` | ✅ **TUONG THICH** | — |
| `qwen3.7-max` | ✅ **TUONG THICH** | — |

> "Vuot `hard_timeout`" **khong** la bi giet: `scheduler.py:308-345` dung `future.result(timeout=...)` nen **chi ngung cho**, luong van chay tiep. Voi lane **shadow** thi `_v10785_late_fill` vot lai (`run_source='shadow_auto_eval'`, `late=1`). Voi lane **official** thi khong co duong vot — `persist_late_fill_row` ghi thang vao lane do. Nen **2 luot cua `glm-5.1`** (model official, 13/08 MT `1.429,5s` va 26/08 MN `1.084,3s`) la **2 lan bundle cong bo thieu mot la phieu**.

---

## 8. Gioi han cua gate nay — noi thang cho lan song 2

| Chua lam duoc | Vi sao | Can gi de lam |
|---|---|---|
| **Dem token dau vao that** cho tung model | Khong co tokenizer tren VPS (`import tiktoken` → `ModuleNotFoundError`), va tach `input` khoi `total_tokens` khong lam duoc voi du lieu trace hien co (chi co `token_count` tong). | Cai tokenizer **hoac** ghi them `prompt_tokens` vao trace tu `response.usage.prompt_tokens` (ca 5 wrapper deu co san truong nay). |
| **Context window** tung model | **Khong ton tai trong ma.** Con so trong chu thich la tai lieu, `RM-14` cam dung. | Dung mot bang `MODEL_CONTEXT_WINDOW` co nguon xac minh + smoke test, roi moi tinh duoc bien an toan. |
| **Noi dung** chinh xac cua hai goi ngu canh (official vs shadow) | Phai goi `build_context_pack` — de bai cam goi khi chua chung minh khong co duong ghi. Gate nay chi chung minh **cau truc** (2 nhanh `if shadow_mode`) va **kich thuoc** (do that). | Chung minh do lap phu tac dung + monkeypatch chan ghi + bay mutation, roi dung goi tren clone bat bien. |
| 7 luot lech trong nhom shadow | Chua dung lai duoc goi tai thoi diem do. | Nhu tren. |
| Ty le luot `reasoning` an het tran dau ra | n=1 cho moi model ⇒ `RM-04`: **chua duoc phep ket luan**. | Do tiep >= 30 luot, hoac dung `thinking_budget` tuong minh cho Gemini. |
| Co che that dang sau `latency > 300s` ma van thanh cong tren OpenRouter | `_call_openrouter` dat `httpx timeout=300.0` (`:4089`) nhung do duoc luot **thanh cong** dai 561,9s (p95 `glm-5.1`). Hai kha nang: (a) OpenRouter gui byte giu song lam `read timeout` reset; (b) `latency_seconds` gom ca cac lan retry. **Khong tach duoc** tu du lieu hien co. | Ghi them `so lan retry` + `thoi gian tung lan` vao trace. |

---

## 9. Cach tai lap (RM-11)

```bash
# tat ca chay tren VPS, cwd = /root/Lottery_AI_Test/web/backend, DB chi doc
python _h8_a_khaosat.py      # khao sat nguon + grep phan loai
python _h8_d_roster.py       # roster THAT tu model_registry (import that)
python _h8_m_do.py           # do tren prediction_trace.jsonl
python _h8_o_lech.py         # lech theo (ngay, mien, regime)
python _h8_p_lech2.py        # lech theo nhom vai tro + goi ngu canh bi bo
python _h8_q_ngan.py         # tran cau hinh vs so do duoc
python _h8_r_xacminh.py      # grep chung minh: tool calling · cat prompt · contract rong
python _h8_s_noidung.py      # khoi bi gac boi shadow_mode + 5 dau o nhiem
python _h8_u_env.py --env    # doc lai cau hinh DUOI env cua tien trinh service (RM-13)
python _h8_w_matrix.py --env # lap ma tran
python _h8_x_sua.py --env    # sua RM-21 + dem vuot timeout
python _h8_y_nhan.py         # nhan phien ban prompt vs van tay payload
```

**Artifact tren VPS** (`/root/Lottery_AI_Test/artifacts/`):

| Tep | Noi dung |
|---|---|
| `v11165_h8_model_matrix.json` | **ma tran chinh** (19 model × day du truong) |
| `v11165_h8_a_khaosat.json` | grep phan loai tren 8 tep nguon |
| `v11165_h8_d_roster.json` | roster + `output_eligible` theo mien |
| `v11165_h8_m_do.json` | do tong hop 30 ngay + 04/09 |
| `v11165_h8_n_0409.json` | **tung dong** 04/09 + doi chieu `run_source` tu clone |
| `v11165_h8_o_lech.json` · `v11165_h8_p_lech2.json` | phan tich lech |
| `v11165_h8_q_ngan.json` | tran cau hinh vs so do duoc |
| `v11165_h8_t_bosung.json` | pool combo-super + 15 luot lech shadow |
| `v11165_h8_u_env.json` | cau hinh doc duoi env service |

---

## 10. Ba lop nguon (§62 / A60)

| Lop | Noi dung |
|---|---|
| `OWNER_SAID` | 2026-09-04 23:14 — *"Ok dong y khuyen nghi de xuat, chu y ghi nhan day du thong tin keo quen."* (khoa `QD-073`). Muc tieu "thuan ngu canh" 9 diem do owner nêu, dung lam thuoc doi chieu o muc 6. |
| `CODE_DID` | `gpt_analyzer.py:6738` van dung menh de theo-model ⇒ `gpt-oss-120b` official nhan goi shadow **88/88** luot. `PHASE_FIRST_CONTRACT_MODELS = set()` nen cau "OUTPUT KHONG HOP LE" khong duoc thi hanh. `grep` tool calling = 0 dong. Toan bo so lieu tu `prediction_trace.jsonl` + clone `mode=ro`. |
| `DOC_SAID` | `model_registry.py` ghi `combo-super` = *"4ML + 7AI hybrid"* — **lech** voi ma: `combo_super.AI_MODELS` co **9** model. `CLAUDE.md §59` ghi *"4 ML + 9 AI = 13"* — **khop** ma. ⇒ ghi chu registry la ban **cu**, phai sua. |

**Lech giua ba lop — finding bat buoc bao:**

1. `OWNER_SAID` ≠ `CODE_DID`: owner khoa muc tieu "khong dung ten model / win rate / trong so de day LLM bat chuoc nhau"; ma **van** bom du ca ba vao prompt official (`:3042`) kem menh lenh `:3043`.
2. `DOC_SAID` ≠ `CODE_DID`: ghi chu `combo-super` trong registry noi 7 AI, ma co 9 AI (trong do 2 model `shadow_only`).
3. `DOC_SAID` ≠ `CODE_DID`: chu thich `:985-988` mo ta `SHADOW_GATE_MODELS` la *"measurement-only lanes... khong doi /du-doan output"*; do duoc thi 1/8 thanh vien (`gpt-oss-120b`) **la model official dang doi output that**.

---

**Tang verdict (RM-12):** `EVIDENCE_COMPLETE` cho phan **do luong va doi chieu ma**. **KHONG** nang len `RUNTIME_PROVEN` cho bat ky ban va nao — gate nay **khong viet va, khong deploy, khong restart, khong ghi DB**.

TanPhatAI can lam: cap nhat `docs/CURRENT_TRUTH_SSOT.md` muc prompt/model voi ba lech nguon o muc 10; theo doi `gpt_analyzer.py:6738` (con nguyen, chua va) va ghi chu pool `combo-super` trong `model_registry.py` (da cu).
