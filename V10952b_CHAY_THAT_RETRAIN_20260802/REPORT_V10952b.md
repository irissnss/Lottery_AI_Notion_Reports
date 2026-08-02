# REPORT V10952b — Chạy thật một lượt huấn luyện lại (02/08/2026)

**Ngày:** 02/08/2026 · **Trạng thái:** bù báo cáo công khai A55 (V10962)

---

## 1. Tóm tắt

00:02 ngày 02/08 chạy thật `_v10646_retrain_guard.py --force` trên VPS. Bảng `training_history` ghi được **12/12 dòng có AUC** (trước đó rỗng). 8/9 model so được thì AUC giảm; MT random-forest 0,5517→0,5248 vượt ngưỡng cảnh báo. Hash 4 bảng quản trị y nguyên. Không bật lại cổng tự gỡ model (FU-213).

## 2. Owner yêu cầu gì (nguyên văn)

Phiên kỹ thuật sau V10952: xác nhận bảng journal đã ghi được số thật sau khi sửa, không để trống. Không có nguyên văn riêng ngoài chuỗi sửa lỗi huấn luyện — nội dung lấy từ CHANGELOG V10952b.

## 3. Đào bới / phát hiện

- 12/12 dòng ngày 2026-08-02 có AUC; cột `nguon` phân biệt guard vs `_retrain_all`.
- Hai dòng vượt ngưỡng −0,02: **MT random-forest** và **MB meta-learning**.
- So `old_auc` vs `auc` chưa công bằng (cửa sổ kiểm trượt ~1 tuần) → chưa kết luận model hỏng.
- MT cả bốn model vẫn >0,5; MB hầu hết ≤0,5.

## 4. Hướng xử lý và vì sao chọn

Chỉ ghi hồ sơ + đẩy repo. **Không** bật lại cổng tự gỡ model về bản cũ (logic cửa sổ lệch). Ghi FU-213. Không deploy thêm.

## 5. Đã làm gì

| File / việc | Thay đổi |
|---|---|
| VPS chạy `_v10646_retrain_guard.py --force` | 12/12 dòng AUC |
| Sao lưu 30 file model | `backups/v10952_models_pre/` trên VPS |
| CHANGELOG / SSOT / FU | Ghi V10952b (phiên gốc) |
| Báo cáo công khai | Bù thư mục này tại V10962 |

## 6. Cổng kiểm

- 12/12 dòng có AUC · 0 dòng rỗng · mã thoát 0
- Hash 4 bảng khoá: y nguyên trước/sau (phiên gốc)
- Không sửa `/du-doan` / final_bundles writer

## 7. Vướng vấp

So AUC cũ/mới trên hai cửa sổ khác nhau — nếu bỏ qua sẽ tưởng huấn luyện lại đang phá MT RF và bật cổng gỡ sai. Hậu quả: gỡ model tốt vì tuần mới khó hơn.

## 8. Gỡ về

```
cp -a /root/Lottery_AI_Test/backups/v10952_models_pre/. /root/Lottery_AI_Test/data/models/
```

Không gỡ trong phiên gốc: job CN 02:00 sẽ đè lại; QD-013 đã dừng tiền thật.

## 9. Theo dõi tiếp

- **FU-213** — cổng so AUC cùng cửa sổ (chưa bật lại cổng cũ)
- Job CN 02:00 → xác minh V10953
