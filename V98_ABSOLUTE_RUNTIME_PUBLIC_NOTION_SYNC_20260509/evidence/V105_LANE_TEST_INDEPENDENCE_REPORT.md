# V105 — True Lane Test Independence (2026-05-10 01:30 VN)

V105 delivered real, independent shadow measurement for lane test without touching production.

## Runtime Proof

- VPS real provider pass: `2026-05-10T01:23+07:00`, target_date `2026-05-09`.
- GPT routing fixed: `gpt-5.5` now uses OpenRouter; GPT 5 mini / GPT 5.4 remain OpenAI platform-key slots.
- AI independent rows: `93`.
- No-token independent rows: `7422`.
- Context completeness rows: `7515`.
- `/api/admin/v105-lane-test-control`: admin-locked (`401` unauth).
- `/monitoring`: admin-locked (`401` unauth) and has V105 panel registered in load-all + 60s refresh.

## Official Guard

| Table | Rows | SHA256 |
|---|---:|---|
| predictions | 4625 | `28f20753facd5ddb5b315a8cbe9d95b8999f4812b5081c38da1fffc965db4933` |
| final_bundles | 213 | `e3da0e0709df93e01d1466ab64aae9b3424df2eebfbd4ae26f97632708910005` |
| lottery_results | 14642 | `6972fddfeb574e4b436993a7f73989162d7e95ef3986f283b3151d193380fb32` |
| model_daily_eval | 4493 | `a865b9e3ea3523b85412be455469ef37417fb84ad27305b437408ddc7f1e46cc` |

`OFFICIAL_TOUCHED=false`.

## Remaining

Gemini 2.5 Pro still returns empty/parse-fail responses in some regions; V105 now records this explicitly as provider health instead of hiding it.
