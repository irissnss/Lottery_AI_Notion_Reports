# MASTER_RECONCILE_MATRIX

| Item | Notion doctrine | Code/runtime | Public report | Status | Gap | Action |
| --- | --- | --- | --- | --- | --- | --- |
| measurement grain model×region×weekday×station×output | Yes | model_strength tensor + C16 budget | V74/V76 | SYNCED | needs Notion V79/V80 new surface refs | DOC_UPDATE |
| V66.1 lag1/cross-region | partial/roadmap | deployed shadow | V66/V67 | CODE_AHEAD | Notion older | DOC_UPDATE |
| V67 exploit eager | not fully current | deployed | V67/V72/V73 | CODE_AHEAD | Notion needs current eager state | DOC_UPDATE |
| V70 consensus | planned shadow | deployed + V77 timing fix | V70/V77 | CODE_AHEAD | Notion lacks 19:00 rerun | DOC_UPDATE |
| V73 hybrid region-adaptive | planned multi-lane | deployed | V73/V77 | CODE_AHEAD | Notion stale | DOC_UPDATE |
| V76 drift/latency/cost | measurement doctrine | deployed | V76 | CODE_AHEAD | Notion needs V76 specifics | DOC_UPDATE |
| V77 19:00/19:05 | not present | deployed + timezone fixed | V77/V78 | CODE_AHEAD | Notion missing | DOC_UPDATE |
| V78 prompt shadow audit | prompt shadow planned | deployed | V78 | CODE_AHEAD | Notion missing | DOC_UPDATE |
| V79 AI/no-token cross verify | owner doctrine yes | deployed shadow | V79 | CODE_AHEAD | Notion missing | DOC_UPDATE |
| cluster consensus | implied | deployed shadow | V79 | CODE_AHEAD | Notion missing | DOC_UPDATE |
| rule-phase synthesis pack | ahead | V80 shadow implemented | V80 | SYNCED_AFTER_V80 | natural proof pending | WAIT_NATURAL_CRON_PROOF |
| no-token rule-aware pack | ahead | V80 shadow implemented | V80 | SYNCED_AFTER_V80 | not production features | SHADOW_ACTIVE |
| MB regime-shift | partial | V80 shadow implemented | V80 | SYNCED_AFTER_V80 | needs 7d live watch | WAIT_LIVE |
| MN V67 save monitor | partial | V80 shadow implemented | V80 | SYNCED_AFTER_V80 | needs live continuation | WAIT_LIVE |
| timezone HCM | canonical | selector chain fixed; legacy watch | V78/V79/V80 | PARTIAL_SYNC | legacy naive datetime remains outside touched path | P1_AUDIT |
| official promotion gate | yes | docs gate locked | V74+ | SYNCED | none | DO_NOT_TOUCH_OFFICIAL |
