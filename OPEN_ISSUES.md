# Open Issues — as of V105.30 (2026-05-12 VN)

## V105.30 / V105.28 follow-up

- `FU-V105-28-CLOSED-FILE-NO-TOKEN`: **CLOSED (V105.30)** — `_safe_stdio_ctx` bọc toàn bộ path no-token trên VPS; theo audit finalization + journal post-deploy.
- `FU-V105-28-AI-PRIORITY-ORDER`: **OPEN P1** — scheduler vẫn static `AUTO_AI_MODELS`; reorder strongest-first + tensor daily refresh chờ owner OK.
- `FU-V105-28-SSH-DEPLOY-KEY`: **CLOSED (account SSH)** — GitHub: `Hi irissnss! You've successfully authenticated`; mirror public push SSH.
- `FU-V105-28-TENSOR-REFRESH-CRON`: **OPEN P1** — materialize `model_strength_by_region_weekday_station_daily` định kỳ (đề xuất 19:30 VN).
- `FU-V105-30-NOTION-PAGE`: **DEFERRED** — owner ưu tiên GitHub raw thay vì Notion (page ID có thể bổ sung sau).

## V105.27 carry-over

- `FU-V105-27-MN-D2-RANKED-PROMPT-WIRE`: PARTIAL/CLOSED-FOR-SHADOW. 137/137 injected; official prompt untouched.
- `FU-V105-27-TOP2-BUNDLER-AB`: OPEN. Shadow only; promotion math not met.
- `FU-V105-27-MB-D-V2-SHADOW`: OPEN/HOLD. `auto_disable=true`. Do not promote.
- `FU-V105-27-SECURITY-PAT-SSH`: CLOSED PAT side; SSH account live.

## Earlier carry-over

- `FU-V105-25-STATION-ALIAS-FIXUP`: CLOSED under canonical target `Thừa Thiên Huế`.
- `FU-V105-24-SOURCE-POOL-FORMULA`: OPEN (miss matrix evolves; xem SSOT mới nhất).
- `FU-V105-24-RELAXED-PROMOTION-RULE`: OPEN. Promotion gate >= 14d, save_ratio >= 0.30, break_ratio <= 0.10, net_save > 0, owner OK.

## Measurement risk

Không promote official từ các lane thí nghiệm; MT source formula và 4 bảng chính chỉ đọc/hash trong audit.
