# Open Issues — V105.33 natural verify snapshot (2026-05-12 16:08 VN)

Latest public truth: V105.33 is a read-only natural-verify snapshot on top of V105.32. It does not change official prediction policy. At the 16:00 VN live sync, MN remains clean (`official=15/15`, final bundle `model_count=15`, `shadow=13/13`, `missing_shadow=[]`, `glm-5.1` diagnostic empty due `finish_reason=length`), while MT/MB are still `NATURAL_VERIFY_PENDING` (`official=7/15` each, no 2026-05-12 final bundle, no natural shadow run).

## V105.33 / V105.32 / V105.31 active issues

- `FU-V105-28-CLOSED-FILE-NO-TOKEN`: **CLOSED (V105.30)** — `_safe_stdio_ctx` bọc toàn bộ path no-token trên VPS; theo audit finalization + journal post-deploy.
- `FU-V105-28-AI-PRIORITY-ORDER`: **OPEN P1** — scheduler vẫn static `AUTO_AI_MODELS`; reorder strongest-first + tensor daily refresh chờ owner OK.
- `FU-V105-28-SSH-DEPLOY-KEY`: **CLOSED (account SSH)** — GitHub: `Hi irissnss! You've successfully authenticated`; mirror public push SSH.
- `FU-V105-28-TENSOR-REFRESH-CRON`: **OPEN P1** — materialize `model_strength_by_region_weekday_station_daily` định kỳ (đề xuất 19:30 VN).
- `FU-V105-30-NOTION-PAGE`: **DEFERRED** — owner ưu tiên GitHub raw thay vì Notion (page ID có thể bổ sung sau).
- `FU-V105-30B-RULE105-PRIZE-SOURCE`: **CLOSED / CORRECTED** — source lock theo `source_region`; 0 true violation; 30 prior flags are false positives.
- `FU-V105-30D-SHADOW-NO-MISSING-CONTRACT`: **DEPLOYED_PENDING_FULL_NATURAL_VERIFY** — V105.30d scheduler/database hardening deployed. MN 2026-05-12 proves shadow `13/13`, `missing_shadow=[]`; `glm-5.1` diagnostic empty row is valid non-timeout diagnostic, not missing. MT/MB natural-cycle verification remains pending at the 16:00 VN snapshot.
- `FU-V105-33-NATURAL-VERIFY-FULL-CYCLE`: **OPEN P1 / NATURAL_VERIFY_PENDING** — V105.33 sync `artifacts/live_sync/20260512_160034/manifest.json` shows no P0 regression, but MT/MB are not complete: both only `official=7/15`, no same-day final bundle, no natural shadow run. Do not call `V105_33_NATURAL_VERIFY_PASS` until MT/MB complete naturally and cleanly.
- `FU-V105-31-GLM51-COMPACT-PROFILE`: **OPEN P1 / OWNER_GATE** — `glm-5.1` full-context shadow run returned empty content with `finish_reason=length`; proposal file created in V105.32 as `glm-5.1_compact_json_profile`. No provider/manual re-call without owner OK.
- `FU-V105-32-SOURCE-POOL-ROOT-CAUSE`: **OPEN P1 / ACCURACY_LANE** — after runtime stability is clean, drill down where actual tails drop across `source_pool -> prompt -> rank -> top5 -> top2 -> bundle -> UI`, using `region + weekday + station_set` and Rule105 `source_region` wording. Plan created in V105.32; no official change.

## V105.27 carry-over

- `FU-V105-27-MN-D2-RANKED-PROMPT-WIRE`: PARTIAL/CLOSED-FOR-SHADOW. 137/137 injected; official prompt untouched.
- `FU-V105-27-TOP2-BUNDLER-AB`: OPEN. Shadow only; promotion math not met.
- `FU-V105-27-MB-D-V2-SHADOW`: OPEN/HOLD. `auto_disable=true`. Do not promote.
- `FU-V105-27-SECURITY-PAT-SSH`: CLOSED PAT side; SSH account live.

## Earlier carry-over

- `FU-V105-25-STATION-ALIAS-FIXUP`: CLOSED under canonical target `Thừa Thiên Huế`.
- `FU-V105-24-SOURCE-POOL-FORMULA`: OPEN / SUPERSEDED-BY-V105.32-PLAN for next execution wording. Miss matrix evolves; use V105.32 source-pool root-cause plan as current readout.
- `FU-V105-24-RELAXED-PROMOTION-RULE`: OPEN. Promotion gate >= 14d, save_ratio >= 0.30, break_ratio <= 0.10, net_save > 0, owner OK.

## Measurement risk

Không promote official từ các lane thí nghiệm; MT source formula và 4 bảng chính chỉ đọc/hash trong audit.
