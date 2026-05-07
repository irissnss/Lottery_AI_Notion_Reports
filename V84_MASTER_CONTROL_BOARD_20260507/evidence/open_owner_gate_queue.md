# Open owner-gate queue

| Item | Trigger date | Blocker | Owner action | Official impact |
| --- | --- | --- | --- | --- |
| MN_TEST_LANE_VOTER_PROPOSAL dossier | 2026-05-21 | Need 14d fresh-live sustained lift | Read dossier + OK or REJECT for test-lane voter (NOT official) | NO (test-lane only) |
| Provider invoice update _provider_pricing_table.py | Anytime owner sees real bill | Owner provides real $ per 1k tokens | Edit table or instruct agent to update | NO (cost tracking only) |
| MB regime forensic deep dive | 2026-05-14 if MB OFFICIAL 0/7 | MB cold-streak escalation auto-trigger | OK to proceed with deep dive (read-only forensic) | NO (forensic only) |
| GPT-5-mini API key validation | Whenever owner has time | VPS OPENAI key returned 401 on gpt-5-mini endpoint during V81 smoke | Check OPENAI_API_KEY in OpenAI org for gpt-5-mini access | NO (V81 swap to deepseek-chat works) |
| V82 monitor UI feedback / layout adjustment | Whenever owner reviews /v82-monitor | Owner UX preference | Comment on layout/data; agent will tweak read-only HTML/CSS | NO (UI only) |
| Selector promotion (V67/V70/V73/V79/V81 → official) | Earliest 60d (2026-07-06) + dossier | 60d Wilson CI > baseline + zero MT break | Owner explicit OK + dossier review | YES (DO NOT EXECUTE without owner OK) |
| Official prompt change | Owner-locked indefinitely | Owner explicit decision | Owner directive | YES (LOCKED) |
| Production model swap | Owner-locked indefinitely | Owner explicit decision | Owner directive | YES (LOCKED) |
| Global NO_TOKEN floor change | Owner-locked indefinitely | Region delta differ (MN +3.4pp / MT +8.3pp / MB -3.3pp) | Owner directive | YES (LOCKED) |
