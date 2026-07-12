# BÁO CÁO V10793 — K14 SANDBOX RETRAIN MB (KHÉP TRAIN/SERVE MISMATCH): MEASURED_NO_EDGE + HOUSEKEEPING CP-R4/CP-R5

- **Ngày:** 2026-07-12 21:4x
- **Tính chất:** SANDBOX-ONLY — zero production write, không restart, không đổi /du-doan //choi /lane
- **Lệnh owner (21:35):** "Các vấn đề nào rõ ràng, xác định, an toàn có tính chất cải thiện, cải tiến thì tiến hành dùm anh đi nha em."
- **Phạm vi em chọn (đúng 3 tiêu chí rõ ràng + an toàn + cải thiện):** (1) **K14** — sandbox retrain MB khép train/serve mismatch, việc duy nhất đang chờ ký được em khuyến nghị LÀM từ V10788-B vì zero risk; (2) **housekeeping 2 checkpoint quá hạn** CP-R4/CP-R5 (doc-only). KHÔNG làm: K9 (đã khuyến nghị chờ), wire CP-R4 (chạm runtime — cần chữ ký), drop 41 bảng chết (destructive — chờ ký).

---

## 1. K14 LÀ GÌ (nhắc lại)

Feature `cross_region_momentum` của ML MB:
- Khi **TRAIN** (retrain CN 02:00): luôn dùng `include_same_day=False` → chỉ thấy kết quả MT đến hết D-1.
- Khi **SERVE** (rerun 17:30 sau scrape MT, số này vào bundle official 17:34): dùng `include_same_day=True` → thấy cả kết quả MT CÙNG NGÀY.
→ Model đang chấm điểm trên phân phối feature nó **chưa từng học**. K14 = train lại biến thể `include_same_day=True` và so offline.

## 2. THIẾT KẾ SANDBOX (scripts `_v10793_k14_sandbox.py` + `_v10793_k14_walkforward.py`)

- Collect **2 bộ training data MB 260 ngày** (2025-10-22 → 2026-07-12) trên DB production (read-only), **cùng random seed**: bộ A (`False` — nguyên trạng) và bộ B (`True` — K14). Draw-order guard V10667 giữ causal (MB chỉ được thấy same-day của miền xổ TRƯỚC nó).
- **Sanity mismatch:** 10.400 hàng giống hệt nhau TRỪ cột `cross_region_momentum` — 73% hàng khác giá trị, mean |Δ| = 0.079 → mismatch **có thật về mặt dữ liệu**.
- Train bằng **đúng class production** (MetaLearner LightGBM · MLModel XGBoost · Random Forest), `model_path` override về `/root/sandbox_v10793/` — không đụng `data/models/`.
- Hai thước đo:
  1. **Single-split:** holdout 50 ngày cuối (24/05 → 12/07).
  2. **Walk-forward 12 tuần refit** (thước quyết — mô phỏng đúng nhịp retrain CN hằng tuần, train-window 200 ngày, tổng 72 lần train, đánh giá 84 ngày 20/04 → 12/07).
- Cả hai model A/B đều được chấm trên **cùng holdout với feature TRUE** = đúng điều kiện serve 17:34 của MB.

## 3. KẾT QUẢ — TRUNG THỰC: KHÔNG CÓ CẢI THIỆN ĐO ĐƯỢC

**Walk-forward 12 tuần (84 ngày, thước quyết):**

| Model | A (False — hiện tại) | B (True — K14) | Đọc |
|---|---|---|---|
| meta (LightGBM) | AUC 0.5032 · top1 20% · top5 74% | AUC 0.5047 · top1 17% · top5 76% | ±0.002 = nhiễu |
| xgboost | AUC 0.5003 · top1 21% · top5 75% | AUC 0.5005 · top1 19% · top5 76% | nhiễu |
| random-forest | AUC 0.4910 · top1 20% · top5 69% | AUC 0.4904 · top1 30% · top5 68% | AUC nhiễu; top1 +10pp KHÔNG tin được vì single-split cho NGƯỢC LẠI (10% vs 16%) |

**Kết luận:** gốc vấn đề là **AUC MB quanh 0.49–0.53** — model gần như không có sức phân biệt (khớp audit V10788: AUC MB 0.497 = tung xu). Feature momentum tươi hơn không cứu được model không có edge. Khép mismatch cho kết quả **trung tính**, không phải cải thiện.

## 4. KHUYẾN NGHỊ

1. **KHÔNG đổi retrain production** — không có bằng chứng cải thiện; đổi model MB giữa cửa sổ đo K11a (checkpoint 16/07) còn làm trộn biến.
2. Mismatch hạ cấp thành **hygiene defect**: nếu anh muốn sạch kiến trúc, khép SAU khi K11a/K15 chốt (kỳ vọng trung tính, cần chữ ký vì chạm model chấm phiếu official).
3. Hướng cải thiện MB thật sự nằm ở **tầng CHỌN số** (K11a MB_OUTPUT_V1 đang đo live) chứ không phải tầng feature ML — số liệu này củng cố thêm.
4. **K14 đóng: MEASURED_NO_EDGE.**

## 5. HOUSEKEEPING ROADMAP REDESIGN (doc-only, cùng phiên)

- **CP-R5** (selector per-slice, quá hạn từ 21/06) → **SUPERSEDED**: K10/K13 selector shadow (V10789) đã phủ đúng mục tiêu "selector validate ex-ante", forward đo đến 23/07.
- **CP-R4** (wire reduce-cadence, quá hạn từ 14/06) → **AWAITING_OWNER_OK, hạn mới 19/07**: wire chạm runtime gọi model nên em không tự làm — anh quyết wire hay huỷ.

## 6. AN TOÀN & TRUY VẾT

- Model production MB: mtime giữ nguyên **05/07 02:02** (verify `_v10793_k14_verify.py`).
- Hash 4 bảng official pre/post **IDENTICAL** (9888/405/15063/9752). Service active, journal 0 warning, 0 restart.
- Artifacts: VPS `/root/sandbox_v10793/` (4 CSV + 6 model + `k14_results.json` + `wf/k14_walkforward_results.json`).
- Docs cùng phiên: CHANGELOG V10793 · SSOT block V10793 · FU-V10793-K14-SANDBOX (CLOSED) · AUTOMATION_STATE seq 254 · roadmap REDESIGN cập nhật.
- Nhắc lịch: **CP-L6 hạn 14/07 cần anh OK** · 13/07 sáng verify weekly lock · 16/07 K11a · 17/07 K15 · 23/07 selector.
