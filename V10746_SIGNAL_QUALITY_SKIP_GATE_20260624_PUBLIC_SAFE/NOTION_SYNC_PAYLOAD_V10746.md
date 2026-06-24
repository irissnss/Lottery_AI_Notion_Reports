# V10746 — Signal Quality & Skip Gate (shadow, học từ cowork DDXS)

**Thời gian:** 2026-06-24T22:05:00+07:00
**Yêu cầu owner:** sau khi đối chiếu project cowork (DDXS_Full), owner chọn tiếp thu gói "Signal Quality & Skip Gate" — xây SHADOW đo trước, không đụng prompt/official.

## Nguồn học (cowork → adapt)
- Cowork DI-29 ScoreBandGuard: score 8–9 = bẫy (7%), 9+ = tốt (47%).
- Cowork decision_band SKIP: score/conf thấp → không chốt.
- Adapt sang hệ LLM+ML của mình bằng DỮ LIỆU THẬT: `model_daily_eval.strength`/`bt_hit` (vùng bẫy) + `final_bundles.top_score`/`bach_thu_status` (skip gate).

## Đã triển khai (READ-ONLY, admin)
- `_build_signal_quality_skip()` trong main.py — live-compute, KHÔNG bảng/cron mới.
- API `GET /api/admin/signal-quality-skip` (require_admin, no-store).
- Panel `/monitoring` "SIGNAL QUALITY & SKIP GATE": HÔM NAY advisory + A. Vùng bẫy strength + B. Skip gate top_score. Auto-refresh 60s.

## Phát hiện thật (đo live)
- MT vùng bẫy quá-tự-tin RÕ NHẤT: strength 8–9 = 35.9%, 9–10 = 29.3% BT-rate — TỆ hơn đỉnh 6–7 (44.5%). → MT khi model rất tự tin lại hay trật.
- MB skip-gate non-monotonic: ngày top_score 0.16–0.19 → BT thắng 0/13 (0%); hôm nay MB = 0.1899 đúng band đó → LOSE (khớp cảnh báo). Band tốt nhất MB là 0.13–0.16 (43.5%).
- MN lành mạnh: strength 9–10 tốt nhất 47.8%; top_score ≥0.19 → BT win 51.2% (WR chung 45.3%). MT band yếu: top_score 0.10–0.13 → 12.5%.

## An toàn / Verify
- Service lottery, port 8000. health=200; signal-quality endpoint=401.
- 4 bảng official hash IDENTICAL pre/post: predictions b6cd981a392bc987, final_bundles e069c59d12108179, lottery_results 6f595e2306153ddb, model_daily_eval fb495368581bd7fb.
- 0 official mutation, KHÔNG cron/bảng mới.

## Bước sau (chờ owner)
- Forward 2–4 tuần. Nếu vùng bẫy MT (strength ≥8) + band chết MB (0.16–0.19) ổn định → đề xuất owner-gated down-weight/skip trong lane shadow TRƯỚC khi đụng official. Không tự promote.

## Rollback
Khôi phục `backups/v10746_remote_pre/`, restart lottery. Official không liên quan.
