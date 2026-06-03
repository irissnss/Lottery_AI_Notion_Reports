# V10693 — KẾT QUẢ FIX (MB per-position rule-driven, lane test)

> **Owner duyệt:** "đưa giải pháp tốt nhất hiện tại cho MB lane test cho BT, số phụ 1, số phụ 2 … so sánh sau 2 tuần live … lấy top Rules của thứ hiện tại của MB."
> **Pha:** FIX (lane `/du-doan-test` only). **Official 4-table ZERO-DRIFT: PASS** (IDENTICAL trước & sau toàn bộ fix). **MN/MT bất biến.** Data as-of 2026-06-03.

---

## 1. ĐÃ LÀM GÌ

Xây **per-position predictor cho MB** (`_v10693_mb_perpos_predictor.py`) — KHÔNG dùng đồng thuận AI/model (đã chứng minh phản tác dụng cho MB), thay bằng **rule soi-cầu MANUAL xếp hạng hàng ngày**:

- **Cơ chế học tập tích luỹ xếp hạng (đúng yêu cầu owner):**
  - `mb_rule_ranker.py` re-rank **mỗi ngày**: PRODUCTION 35 + MANUAL 77, **gắn theo từng THỨ** (target_weekday), composite nhấn 8 tuần + lifecycle (MẠNH/TĂNG_TRƯỞNG/XUỐNG_CẤP/YẾU/ỔN_ĐỊNH).
  - `_v10689` rolling re-measure 90 ngày → `drive_weight` (loại mining gap W20/W21).
  - **Ngày dự đoán** → lấy **top rules của THỨ hiện tại** (drive_weight>0, bỏ confirm-only forward-audit).
- **Phương pháp từng vị trí:**
  - `score(đuôi) = Σ rules  drive_weight / sqrt(|tập đuôi rule bắn|)` (trọng số theo độ đặc hiệu) `+ bonus` đuôi ĐB same-day MN(D)/MT(D) (MB xổ cuối → hợp nhân quả).
  - **top1 (BT)** = điểm cao nhất; **top2 (số phụ 1)** = kế tiếp khác; **top3 (số phụ 2)** = kế tiếp khác. Mỗi vị trí độc lập, anti-herd theo cấu trúc (không dùng phiếu model).

---

## 2. KẾT QUẢ WALK-FORWARD TRUNG THỰC (60 ngày, KHÔNG look-ahead)

> Tính lại `drive_weight` bằng **chỉ dữ liệu TRƯỚC mỗi ngày** (no look-ahead) → con số thật, không tô hồng.

| Cửa sổ | top1 (BT) mới | top2 | top3 | xiên2 | **official top1** | random |
|---|---|---|---|---|---|---|
| **60 ngày** | **25.0%** | 26.7% | 15.0% | **11.7%** | 13.3% | 23.7% |
| **90 ngày** | **22.2%** | 25.6% | 18.9% | 8.9% | **21.1%** | 23.7% |

**Diễn giải TRUNG THỰC (không tô hồng):**
- 60d: BT gấp ~1.9 lần official (13.3%→25%); xiên2 gấp ~2.3 lần (5%→11.7%).
- **90d: top1 method 22.2% ≈ official 21.1% (chỉ +1.1pp — gần như HÒA).** Cửa sổ 60d official rơi giai đoạn đặc biệt tệ; mở 90d thì official hồi phục → **method KHÔNG thắng áp đảo**, chỉ ngang/nhỉnh.
- Giá trị thật: tín hiệu **độc lập, rule-based, anti-herd** + **top2 ổn định 25.6%** cho xiên. top3 còn yếu (15-19%).
- `control_top1` (13.3%/60d, 21.1%/90d) khớp official đo độc lập → cross-validate đúng.
- ⚠️ Số as-of (weight hôm nay) = top1 40% là **overfit/look-ahead**; số CHUẨN là walk-forward (22-25%).
- 👉 Chi tiết phân tích + per-weekday + câu hỏi mở: **`ANALYSIS_FOR_AI_REVIEW.md`**.

---

## 3. CÔ LẬP & AN TOÀN (bằng chứng)

| Kiểm tra | Kết quả |
|---|---|
| Official 4 bảng (predictions/final_bundles/lottery_results/model_daily_eval) | **IDENTICAL** trước & sau (ZERO-DRIFT PASS) |
| `mined_rules` MN / MT / MB base | bất biến (ranker chỉ ghi bảng riêng `mined_rules_mb_daily`) |
| predictions MN / MT | bất biến |
| File runtime chung (gpt_analyzer/rule_engine/prompt_registry) | **KHÔNG sửa trong pha này**; predictor không import chúng |
| Ghi vào | chỉ `mb_experimental_preview_shadow` (branch `MB_PERPOS_RULEDRIVEN_V1`, 60 rows) + `du_doan_test_experiments` (register) + bảng MB-only ranker |
| `generate_final_bundle()` / final_bundles / predictions production | KHÔNG gọi/ghi |

---

## 4. TRẠNG THÁI & BƯỚC TIẾP

- **Local:** hoàn tất — method + 60 ngày backfill + walk-forward + zero-drift.
- **VPS lane (`/du-doan-test`):** CHƯA deploy. Deploy lane-only an toàn (`_v10690_deploy_lane_only.py`, thêm `_v10693_*` vào SAFE_FILES) — hash official before/after + auto-rollback. **Chờ owner xác nhận "deploy"** (VPS là hệ thống tiền thật → giữ ranh giới production).
- Sau deploy: lane tích luỹ **2 tuần live** → so sánh trực tiếp per-position + xiên2/3 vs OFFICIAL.

---

## 5. FILE

- Code (private, KHÔNG public): `web/backend/_v10693_mb_perpos_predictor.py`.
- Evidence: `evidence/V10693_WALKFORWARD_PERPOS.json`.
