# V98 Conflict Matrix (Doc ↔ Code ↔ Runtime ↔ Public ↔ Notion)

| Conflict ID | Doc says | Code says | Runtime | Public | Notion | Resolution |
|---|---|---|---|---|---|---|
| **PROMPT-3-vs-2** | "TỐI ĐA 2 số" (V96 audit) | L159+L161 said "3 số" → **fixed V97 SP-4.1** | DEPLOYED | RESOLVED V98 | UNVERIFIED | ✅ DEC-019-PROMPT-2NUM (FINAL) V97 |
| **COMBO-WR-vs-BT** | BT_NORTH_STAR (Antigravity §BT) | combo_super L197+ uses WR | RUNNING | DOCS_DEPLOYED | UNVERIFIED | OWNER_LOCK FU-174 14d gate |
| **REGISTRY-SSOT** | model_registry.py is SSOT | combo_super L69-74 hardcode 6 AI | RUNNING | DOCS_DEPLOYED | UNVERIFIED | OWNER_LOCK FU-174 14d gate |
| **AI-CONTEXT** | 21 fields ideal | prod 10/21 (47-52%); 11 shadow-only | RUNNING | DOCS_DEPLOYED | UNVERIFIED | OWNER_LOCK FU-175 14d gate |
| **D-2-REGION** | RR-16.4 §9 region-gated | code applies uniform | RUNNING | DOCS_DEPLOYED | UNVERIFIED | OWNER_LOCK FU-165 14d gate |
| **3-CANG-DISPLAY** | predictions = 2-digit only | predictions main_numbers 100% 2-digit; lo3 = post-AI mechanical frequency | RUNNING | DOCS_DEPLOYED | UNVERIFIED | DOCS_DEPLOYED FU-161 |
| **CRON-23:45+** | All cron should fire daily | V70/V73/V76/C16 misfire post-restart | PARTIAL | DOCS_DEPLOYED | UNVERIFIED | OWNER_LOCK FU-172 |
| **PUBLIC-V92** | Latest is V92 | Private V97 | V97 | RESOLVED V98 | UNVERIFIED | ✅ V98 wrapper |
| **README-V74** | README says V74 latest | V74 was 5 versions ago | V97 | RESOLVED V98 | UNVERIFIED | ✅ V98 README updated |
| **MD5-DRIFT** | Local = VPS truth | 4 files differ | VPS truth | DOCS_DEPLOYED | UNVERIFIED | OWNER_LOCK FU-171 |

## Hard prohibitions honored

- ✅ NO `/du-doan` change
- ✅ NO `/api/final-bundle` change
- ✅ NO `final_bundles` table mutation
- ✅ NO production `predictions` mutation
- ✅ NO scoring/selector/voting change
- ✅ NO promote/rollback/auto-trigger button
- ✅ V97 prompt text-only fix (L159+L161 surgical, JSON schema unchanged, parser unchanged)
- ✅ All V93-V98 surfaces shadow_only=1 / output_eligible=0 / output_impact='false'
