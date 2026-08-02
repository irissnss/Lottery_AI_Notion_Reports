# REPORT V10953 — Xác minh job huấn luyện tự động 02:00 (02/08/2026)

**Ngày:** 02/08/2026 · **Trạng thái:** bù báo cáo công khai A55 (V10962) · FU-211 CLOSED_PASS

---

## 1. Tóm tắt

Kiểm lúc 02:18 ngày 02/08: job chủ nhật 02:00 qua `scheduler.py` đã chạy thật. **12/12 dòng** `training_history` có AUC, 0 dòng rỗng, không lỗi `I/O operation on closed file`. Bằng chứng chạy nằm ở cột `old_auc` (ghi đè đúng khoá). Cả bốn model MT vẫn AUC >0,5.

## 2. Owner yêu cầu gì (nguyên văn)

Xác minh job huấn luyện tự động 02:00 đã chạy sau sửa V10952 — đóng FU-211. Nội dung từ CHANGELOG V10953.

## 3. Đào bới / phát hiện

- Số dòng vẫn 12, `created_at` vẫn 00:03–00:05 — ghi đè theo khoá `(date, region, model_type)`, không đẻ dòng mới.
- Chuỗi `old_auc`: MT RF 0,5517 → 0,5248 (00:02) → 0,5299 (02:00).
- AUC 02:00: MT cả bốn >0,5; MB ba/bốn <0,5.

## 4. Hướng xử lý và vì sao chọn

Chỉ ghi hồ sơ + đóng FU-211. Không sửa code, không deploy, không chạy phép đo thêm.

## 5. Đã làm gì

| File / việc | Thay đổi |
|---|---|
| `_v10953_canh_job_02h.py` | Script canh chỉ-đọc |
| FU-211 | → CLOSED_PASS |
| CHANGELOG V10953 | Ghi kết quả |
| Báo cáo công khai | Bù tại V10962 |

## 6. Cổng kiểm

- 12/12 AUC · 0 rỗng · journal sạch quanh 02:00
- Không deploy → không so hash 4 bảng (không áp dụng vì không chạm runtime)

## 7. Vướng vấp

Thoạt nhìn tưởng job 02:00 không chạy vì `created_at` không đổi. Hậu quả nếu bỏ qua: báo sai "job chết" và sửa nhầm. Phải đọc `old_auc`.

## 8. Gỡ về

Không áp dụng (chỉ đọc + ghi hồ sơ). Xoá dòng CHANGELOG V10953 nếu cần.

## 9. Theo dõi tiếp

- FU-211 đóng PASS
- Tiếp tục theo dõi tín hiệu MT vs mất ở khâu công bố (V10955+)
