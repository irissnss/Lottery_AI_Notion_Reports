# V10955b — Làm rõ mâu thuẫn hai con số RF (bổ sung vào báo cáo V10955)

**Ngày:** 02/08/2026 · **Phiên bản:** V10955b · **Trạng thái:** ĐẠT (chỉ đọc) · **Commit riêng / công khai:** *(điền sau push)*

Owner bắt đúng chỗ: bảng chuỗi rơi nói RF +3,42pp trong khi GT-1 nói RF kém đánh bừa 2–3pp. Đo lại. Không sửa code, không deploy.

---

## 1. Hai con số đó khác nhau ở chỗ nào?

| | Con số A (+3,42pp) | Con số B (−2,09pp) |
|---|---|---|
| **Là gì** | `bt_number` RF đã ghi thật vào `model_daily_eval` lúc chạy hàng ngày | Argmax xác suất khi **tự chấm lại** trên các dòng CSV holdout (20% cuối), **không** gọi `predict_with_random_forest` |
| **Cửa sổ** | 06/05 → 01/08 · **87 ngày** · 211 đài | 03/06 → 01/08 · **60 ngày** · 146 đài |
| **Hit %** | 19,91% | 14,38% |
| **vs đánh bừa** | **+3,42pp** (z 1,34) | **−2,09pp** (z −0,68) |

Đoán của owner **đúng hướng**: A = số live, B = số tái suy luận kiểu khác (CSV đóng băng), không phải cùng một phép.

Cùng cửa sổ 60 ngày holdout: live RF vẫn **+1,34pp** còn CSV top-1 **−2,09pp** — lệch không chỉ vì khác ngày. CSV holdout dùng đặc trưng đã đóng trong file huấn luyện; live dùng `run_full_analysis` + `extract_prediction_features` ngày đó.

---

## 2. Tỉ lệ khớp live ↔ tái suy luận (`predict_with_*`)

Cùng cách đo LSTM (13,3%). Gọi lại `predict_with_random_forest` / `predict_with_xgboost` trên đúng 87 ngày, so với `bt_number` đã ghi. File model hiện tại mtime **02/08 02:00** (huấn luyện lại sau khi hầu hết các ngày live đã chạy).

| Model | Khớp top-1 | Live nằm trong top-5 tái suy luận | Hit % live | Hit % tái suy luận |
|---|---:|---:|---:|---:|
| **random-forest** | **31,0%** (27/87) | 66,7% | 19,91% (+3,42pp) | 19,43% (**+2,95pp**) |
| **xgboost** | **20,7%** (18/87) | 52,9% | 19,43% (+2,95pp) | 16,59% (**+0,10pp**) |
| lstm (V10955) | 13,3% (15 ngày) | — | kém | — |

Đọc thẳng:

- RF **lệch nặng ở từng số** (31% khớp) — một phần vì đang phát lại lịch sử bằng file model mới (02/08). Không phải bằng chứng RF “giỏi ảo” theo nghĩa số cũ tái tạo 1:1.
- Nhưng **đường predict hiện tại của RF vẫn còn lợi thế +2,95pp** trên đúng những ngày đó — gần với live +3,42pp. Hai phía đổi số ngày-qua-ngày nhưng chất lượng gần nhau (live thắng / re thắng gần đối xứng: 13 vs 12 ngày).
- XGB tái suy luận **sụp về đánh bừa** (+0,10pp) dù live từng +2,95pp → **không** đặt XGB ngang RF.

---

## 3. Đề xuất số 1 còn đứng vững không?

**Đứng, nhưng phải sửa — không rút hết, không giữ nguyên.**

| Hạng mục | V10955 (cũ) | V10955b (sửa) |
|---|---|---|
| Model | RF hoặc XGB | **Chỉ RF** (rút XGB khỏi vị trí ngang hàng) |
| Ước lợi thế | 3–7pp | **~3pp** (neo vào live +3,42 và re-infer +2,95; **không** lấy từ CSV −2) |
| Nền | Live MDE | Live MDE **và** re-infer đường predict hiện tại; CSV holdout chỉ là phép phụ, không làm nền đề xuất |
| Điều kiện trước khi tin | (không có) | **7 ngày đầu sau 08/08:** cùng ngày, live bt phải khớp re-infer ≥ **95%**. Dưới ngưỡng → dừng shadow, mở điều tra train/serve trước |
| QD-013 | Đóng | Vẫn đóng (z 1,34 chưa đủ đặt tiền) |

Nói thẳng: đề xuất **không** đứng trên nền “RF sống khác model file mà ta vẫn tin số đẹp”. Nó đứng trên việc **hai phép đo độc lập trên đường predict thật** (lịch sử live + file hiện tại) cùng ra ~+3pp. Phần yếu là chưa chứng minh live tương lai sẽ khớp file đang chạy — nên có cổng 7 ngày.

Thứ tự ưu tiên sửa lại:

1. **Ưu tiên A:** Sau 08/08 — 7 ngày chỉ đo khớp live↔re RF (không đặt tiền). Đạt ≥95% rồi mới bật shadow BT=RF đơn.
2. **Ưu tiên B:** Shadow RF đơn ~60–90 ngày, ngưỡng pass hit≥18,37% và z≥2.
3. **Xuống hạng:** XGB đơn (re-infer ≈0).
4. **Giữ:** điều tra LSTM live (kẹt 96 / khớp 13%).

---

## Bằng chứng

- `evidence/v10955b_live_vs_re.json`
- `evidence/v10955b_top5.json`
- Script: `_v10955b_live_vs_re.py`, `_v10955b_top5.py` (repo riêng)
