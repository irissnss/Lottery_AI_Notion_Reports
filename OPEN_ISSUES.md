# Open issues — as of V105.27 (2026-05-11 21:30 VN)

## P0 — stability (blocks any official semantic change)

- `FU-V105-25B-CLOSED-FILE-VPS-DEPLOY` — scheduler.py `_safe_stdio_ctx` patch deployed locally, NOT yet on VPS. Live 2026-05-11 cascade shows recurrence: 0/14 MT no-token success in rerun_post_mn batch (all errors are `I/O operation on closed file`). Owner Decision #10 required.
- `FU-V105-27-SECRET-HYGIENE` — owner must confirm old PAT revoked + SSH deploy key migration approved. Owner Decision #9.

## P1 — prediction quality (post-stability)

- `FU-V105-27-PUBLIC-MIRROR-SYNC` — V105.24/25/25b/26 backfill + V105.27 publish; this push window covers V105.24/25/27 (V105.25b/V105.26 backfill scheduled next round). Owner Decision #1.
- `FU-V105-27-STATION-CANONICAL-DECISION` — `Huế` vs `Thừa Thiên Huế` canonical conflict. Owner Decision #2.
- `FU-V105-27-MN-D2-PROMPT-WIRE` — MN D-2 implicit at no-token statistical level but not in AI prompt priority_meta; `mn_d2_shadow_v1` profile shadow-only. Owner Decision #3.
- `FU-V105-27-TOP2-AB-SHADOW` — 14d MN+MB shadow, MT measurement-only. Owner Decision #4.
- `FU-V105-27-MB-D2-V2-OPTIONS` — 4-way scope decision for MB_D_v2 shadow. Owner Decision #5.
- `FU-V105-27-V102-RELAXED-HOLD` — keep HOLD until V103 supply class backfill 14d clean. Owner Decision #6.
- `FU-V105-27-MANUAL-CUONCHIEU-LOCK` — keep manual AI/provider "cuốn chiếu" blocked. Owner Decision #7.
- `FU-V105-27-MB-INTERMEDIATE-DISPLAY` — MB `rerun_post_mn` intermediate label decision. Owner Decision #8.

## Watch

- `FU-V105-27-NATURAL-LIVE-VERIFY` — after VPS deploy of #10, expect 7/7 MT rerun_post_mn + 7/7 MB rerun_post_mn/mt with 0 closed-file errors.
