# V10793 — K14 sandbox retrain MB (train/serve mismatch): MEASURED_NO_EDGE (12/07 21:4x, SANDBOX-ONLY)

**Owner 21:35:** "Các vấn đề nào rõ ràng, xác định, an toàn có tính chất cải thiện thì tiến hành dùm anh." → Thực thi K14 (việc duy nhất chờ ký thoả zero-risk, khuyến nghị LÀM từ V10788-B) + housekeeping CP-R4/CP-R5.

**Kết quả chính:**
- Mismatch **có thật về dữ liệu**: 2 bộ training MB 260 ngày cùng seed chỉ khác `cross_region_momentum` (73% hàng, mean Δ 0.079).
- Nhưng khép mismatch **KHÔNG cho cải thiện đo được** — walk-forward 12 tuần refit (84 ngày, 72 lần train, đúng class production): meta AUC 0.5032→0.5047 · xgb 0.5003→0.5005 · rf 0.4910→0.4904 (±0.002 = nhiễu); top1/top5 đổi dấu tuỳ thước.
- Gốc: AUC MB ~0.49–0.53 = model gần như không có sức phân biệt (khớp V10788). Cải thiện MB thật sự nằm ở tầng CHỌN (K11a đang đo live), không phải tầng feature ML.
- **Khuyến nghị: KHÔNG đổi retrain production; K14 đóng MEASURED_NO_EDGE.** Mismatch = hygiene defect, xét khép sau checkpoint K11a/K15 nếu owner muốn sạch kiến trúc.
- Housekeeping: CP-R5 → SUPERSEDED (K10/K13 phủ mục tiêu) · CP-R4 → AWAITING_OWNER_OK hạn 19/07 (wire chạm runtime, chờ ký).

**An toàn:** sandbox-only — model production MB mtime nguyên 05/07 02:02; hash 4 bảng IDENTICAL; 0 restart; journal 0 warning.

**Nhắc owner:** CP-L6 hạn 14/07 cần OK · 13/07 verify weekly lock · 16/07 K11a · 17/07 K15 · 23/07 selector.

**Báo cáo đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10793_K14_SANDBOX_RETRAIN_MB_20260712_PUBLIC_SAFE/BAO_CAO_V10793.md`
