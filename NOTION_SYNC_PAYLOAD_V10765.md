# V10765 — Aggregation Signal Shadow: official vs plurality/strength/AI-plurality (forward proof, INFO-only)

**Ngày:** 2026-07-01 (UTC+7) · **Loại:** SHADOW / INFO-only · **Official impact:** ZERO (hash-guard 4 bảng IDENTICAL)

## Bối cảnh (owner)
Owner: "quá nhiều ngày miss dù model có tín hiệu; giờ có hướng nào cải tiến, tận dụng tối đa tín hiệu anh đều đồng ý hết". Thay vì đoán, chạy đo dứt điểm.

## Việc đã làm
Chạy **walk-forward search causal** nhiều cách ghép số song-thủ từ vote của model, so với official, trên **clean-era 45 ngày + 14 ngày gần nhất**, cho cả 3 miền. Các cách ghép:
- `official` — lo2 chính thức (chuẩn so sánh)
- `plurality2` — top-2 số được nhiều model vote nhất
- `strength2` — top-2 theo tổng strength
- `ai_plurality2` — top-2 số được nhiều model **AI** (loại ML/no-token/combo) vote nhất

Tất cả đều causal (chỉ dùng prediction pre-draw của ngày D + bundle official pre-draw).

## Phát hiện quyết định (đã đo)
| Miền | official (45d / 14d) | AI-plurality (45d / 14d) | Kết luận |
|---|---|---|---|
| **MN** | **−48.0M / −0.8M** | **+10.8M / +33.5M** | AI-plurality VƯỢT official rõ |
| MT | **+21.2M / +27.0M** | +16.3M / +17.2M | official tốt nhất — giữ |
| MB | **+5.9M / +1.4M** | +15.7M / −3.5M | official ổn định recent hơn — giữ |

Đúng case 01/07: MN số **65** là AI-vote cao nhất và VỀ, official chọn 12 (miss). AI-plurality bắt được, official bỏ lỡ.

## Vì sao CHƯA flip official ngay
MN AI-plurality biến động cao (nửa đầu tháng 6 âm, nửa sau dương mạnh) → cần **bằng chứng forward** để chắc chắn không phải hot-streak. Dựng shadow tracker forward trước; nếu MN AI-plurality giữ edge ~1-2 tuần forward và không dồn vào vài ngày → mới đề xuất owner cho dùng chính thức cho MN.

## Thành phần kỹ thuật
- `_v10765_aggregation_signal_shadow.py` — snapshot/score/backfill/compute_view; bảng `v10765_aggregation_signal_shadow` (diagnostic_only=1, shadow_only=1, output_eligible=0, owner_approved=0).
- API `/api/admin/aggregation-signal` (require_admin, Cache-Control: no-store).
- Panel `/monitoring` "TÍN HIỆU TỔNG HỢP" (data-cat=shadow, auto-refresh 60s, đăng ký loadAllSections + setInterval).
- Scheduler closeout hook: snapshot + score mỗi ngày.

## An toàn / verify VPS
- compile OK; backfill 45d trên VPS **khớp** local.
- health=200; endpoint noauth=401; `/monitoring`=401.
- **hash-guard 4 official IDENTICAL:** predictions / final_bundles / lottery_results / model_daily_eval.
- KHÔNG đổi official `/du-doan`, KHÔNG đổi `/choi`, KHÔNG staking, KHÔNG đụng prompt/ví.

## Next action
Forward-watch MN AI-plurality vs official ~14 ngày (FU-V10765-AGG-SIGNAL). Giữ edge → đề xuất route MN sang AI-plurality; mất edge → giữ official.
