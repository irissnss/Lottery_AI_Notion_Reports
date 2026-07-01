# V10766 — MT: bỏ re-predict MN→MT (giữ DD Trước 04:00) — OFFICIAL CHANGE

**Ngày:** 2026-07-01 (UTC+7) · **Loại:** OFFICIAL (chỉ ảnh hưởng cascade tương lai) · **Rollback:** dễ

## Bối cảnh (owner)
Owner: "có hướng nào tận dụng tối đa tín hiệu anh đều đồng ý, quá nhiều ngày rồi" + hỏi kỹ nghi ngờ prompt AI và cơ chế ML "dự đoán trước/sau" (re-predict sau khi cào verify).

## Điều tra forensic (live sync 20260701_212137)
**1) Prompt ngữ cảnh AI — KHÔNG rò kết quả cùng ngày.** Context = WR 14d (loại PENDING), BT ranking 30d, top model theo thứ, mined_rules, KQ D-1, cross-ref chu kỳ lùi 1–8 tuần (không bao giờ hôm nay), query có guard `date < ?`. Nếu rò thì AI phải trúng ~100%; thực tế AI trượt nhiều → không leakage.

**2) ML "dự đoán trước/sau" — CÓ cơ chế nhưng KHÔNG phải leakage.**
- Timing: ML ghi `main_numbers` trước giờ xổ vùng đích (MN@4h, MT@16h, MB@17h) → **0/180 ghi sau xổ**.
- Hit DD Trước vs DD Sau (nếu leakage phải ~100%): MN Δ0, MT **Δ−8 (tệ hơn)**, MB Δ+13. lstm MT Δ−13.
- AI token models: 100% single-save (không re-predict).

## Phát hiện actionable — MT bị hại bởi re-predict MN→MT
| MT | ml_sau→ml_truoc | Δ | all_sau→all_truoc_ml | Δ |
|---|---|---|---|---|
| Nửa cũ (31d) | +13.8M→+28.5M | +14.7M | −15.6M→−10.7M | +4.9M |
| Nửa mới (14d) | +2.5M→+17.2M | +14.7M | +17.2M→+27.0M | +9.8M |

MN→MT same-day cross là **nhiễu** với MT → giữ bản 04:00 (DD Trước) tốt hơn hẳn, bền cả 2 nửa.

## Cascade đã làm rõ cho owner
- **MN**: ML 04:00 (D-1) dự đoán MN + pre-dự đoán MT/MB. MN không re-predict tự động (chỉ thủ công) → bản 04:00 là bản chơi thật. MN **vướng ở mốc ML 04:00** (ML MN −43.1M/45d rất yếu, kéo tụt aggregate; AI MN +10.8M/45d) → lối ra là AI-plurality (V10765 shadow).
- **MB**: 2 lần re-predict — sau cào MN (nạp MN same-day) → sau cào MT (nạp MN+MT same-day = **bản CUỐI, chơi**). Lưu `pre`=04:00, `main`=bản cuối; bản giữa bị ghi đè. Bản cuối ra số mới thật (khác 53–100%) và hit ≥ 04:00 → giữ MB.

## Thay đổi (V10766)
`scheduler.py::_rerun_free_models_after_scrape_inner`: khi `trigger_region=="MN"`, `repredict_regions` từ `['MT','MB']` → `['MB']` (guard `_V10766_SKIP_MT_REPREDICT=True`). MT giữ free-models 04:00. **AI chain MT KHÔNG đổi. MB re-predict KHÔNG đổi.**

## An toàn / verify VPS
- compile OK; change confirmed trong file remote; health=200; `/du-doan`=200.
- **hash-guard 4 official IDENTICAL** (predictions/final_bundles/lottery_results/model_daily_eval) → không sửa dữ liệu cũ; thay đổi chỉ áp dụng cascade từ 02/07.
- Rollback: restore `backups/v10766_remote_pre/scheduler.py` hoặc set guard `False`.

## Next action
Theo dõi MT official forward từ 02/07 (FU-V10766): BT hit + P&L so baseline. Tụt bất thường → rollback. Chéo với bảng nghiệm thu tự động V10760.
