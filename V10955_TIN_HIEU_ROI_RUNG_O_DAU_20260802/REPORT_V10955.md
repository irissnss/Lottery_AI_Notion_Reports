# V10955 — Tin hiệu MT rơi rụng ở đâu?

**Ngày:** 02/08/2026 · **Commit riêng:** `0bea9b9` · **Commit công khai:** `07147b4` · **Trạng thái:** ĐẠT (chỉ đọc)

> Khung A55.3. Phiên **chỉ đo** — không sửa code, không deploy, không huấn luyện lại. Owner đã đóng băng đường ra số tới 08/08.

---

## 1. Tóm tắt

Đo năm giả thuyết trên VPS để trả lời: model MT vẫn xếp hạng hơn ngẫu nhiên (AUC ~0,53–0,55) nhưng số công bố không hơn đánh bừa — tín hiệu rơi ở đâu?

**Kết luận một câu:** tín hiệu rơi chủ yếu khi **gộp phiếu** (pha loãng model ML tốt) rồi bị **ghi đè** làm tệ thêm; cây RF/XGB còn bị bó trong top-30 thống kê (chỉ phủ ~41% số trúng); LSTM trên tập kiểm có tín hiệu ở đỉnh bảng nhưng bản live lệch/kẹt số.

Số chính (MT, nửa sau từ 06/05, đếm theo đài): RF **19,91%** (+3,42pp vs đánh bừa, z 1,34) → số thắng phiếu **15,17%** (−1,32pp) → số công bố **12,32%** (−4,16pp). Chênh RF → công bố = **7,59pp**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> Nhiệm vụ điều tra quan trọng nhất… **CHỈ ĐỌC VÀ ĐO — TUYỆT ĐỐI KHÔNG SỬA CODE, KHÔNG DEPLOY.** Chủ dự án (owner) vừa ký lệnh **đóng băng đường ra số tới 08/08** để đo cho sạch.
>
> …Vậy tín hiệu rơi rớt ở đâu giữa "model xếp hạng được" và "số công bố trúng"?
>
> …Nếu kết luận là "không cứu được", **hãy nói thẳng**. Owner đã mất lòng tin vì báo cáo tô hồng.

Kèm năm giả thuyết bắt buộc kiểm: GT-1 (đỉnh vs giữa bảng) · GT-2 (bt có đúng argmax) · GT-3 (gộp phiếu loãng) · GT-4 (ghi đè) · GT-5 (AUC 0,55 có đủ thành tiền).

---

## 3. Đào bới / phát hiện

### Cách đo

- Chạy trên VPS qua paramiko (`_v10955_do_tin_hieu.py`, `_v10955_bo_sung.py`).
- Thước đếm theo **đài** (giống V10942/V10946): thử cả 100 số trên đúng kết quả ngày đó để ra mặt bằng đánh bừa.
- AUC: nạp đúng model + scaler đã lưu, phần 20% cuối theo thời gian của CSV/NPZ; đối chiếu `*_metrics.json` — khớp từng số (không lặp lỗi đưa đặc trưng thô vào meta-learning).
- Cửa sổ chính cho tiền thật: **nửa sau từ 06/05** (khi lợi thế tắt). Có thêm 180 ngày và cửa sổ holdout để đối chiếu.
- **Thử nhiều lát cắt:** 3 cửa sổ × 4 model × 5 giả thuyết. Kết luận chính bám cửa sổ nửa sau + giả thuyết GT-3 đã ghi sẵn trong FU-212 — không săn p-value trên lát cắt đẹp nhất.

### AUC đối chiếu (file metrics sau huấn luyện 02/08 02:00)

| Model | AUC đo lại | AUC trong file | Khớp? |
|---|---:|---:|---|
| random-forest | 0,5299 | 0,5299 | có |
| xgboost | 0,5236 | 0,5236 | có |
| meta-learning | 0,5394 | 0,5394 | có |
| lstm | 0,5554 | (tự tính) | — |

Ghi chú: trước huấn luyện lại, RF từng ~0,5517 (cửa sổ cũ). Sau 02:00 vẫn **cả bốn trên 0,5** ở MT — hướng không đổi.

### GT-1 — Tín hiệu ở giữa bảng, không ở đỉnh?

**Bộ ứng viên:** CSV/live RF·XGB·meta chỉ có **40 số/ngày** (top-30 thống kê + ~10 âm). Chỉ **40,9%** số trúng thật nằm trong bộ này → hơn nửa số trúng model **không bao giờ chọn được**, trước cả bước xếp hạng.

| Model | Top-1 % | vs đánh bừa | z | Trung vị hạng số trúng |
|---|---:|---:|---:|---:|
| random-forest | 14,38 | −2,08 | −0,68 | 21 / 40 |
| xgboost | 13,01 | −3,45 | −1,12 | 21 / 40 |
| meta-learning | 17,12 | +0,66 | 0,21 | 21 / 40 |
| **lstm (đủ 100)** | **21,40** | **+4,94** | **2,08** | 49 / 100 |

Top-3/5/10/20 của RF/XGB cũng không vượt đánh bừa có ý nghĩa. LSTM: lợi thế **lớn nhất ở top-1**, giảm dần khi mở rộng K — ngược giả thuyết "tin ở giữa bảng".

**Kết GT-1:** đúng một phần với RF/XGB (đỉnh vô dụng); **bác** với LSTM holdout (tin ở đỉnh). Lỗ lớn hơn giả thuyết gốc: **bộ ứng viên chỉ phủ 41% số trúng**.

### GT-2 — bt_number có đúng argmax không?

368/368 dòng MDE MT (từ 01/05): `bt_number == main_numbers[0]`. Khớp luôn với `predictions.main_numbers[0]`. Code `ml_predict` sắp theo `ml_prob` rồi lấy `[0]` — không có lớp lọc/phạt đổi lựa chọn **sau** argmax trong bộ ứng viên.

**Kết GT-2: bác bỏ** (không phải chỗ rơi). Lưu ý: argmax chỉ trong top-30 thống kê, không phải trên cả 100 số.

### GT-3 — Gộp phiếu làm loãng?

MT nửa sau từ 06/05 (87 ngày, 211 đài):

| Nguồn | Hit % | vs đánh bừa | z |
|---|---:|---:|---:|
| RF (tốt nhất cố định) | 19,91 | +3,42 | 1,34 |
| XGB | 19,43 | +2,95 | 1,15 |
| meta-learning | 12,80 | −3,69 | −1,44 |
| lstm (live MDE) | 10,90 | −5,58 | −2,19 |
| Số thắng phiếu | 15,17 | −1,32 | −0,52 |
| **Số công bố** | **12,32** | **−4,16** | **−1,63** |

Chênh ML tốt nhất → công bố: **+7,59pp**. Bundle trung bình **14 model**. Số thắng phiếu trùng ít nhất một ML 72,7% ngày — nhưng **không** phải luôn trùng RF/XGB tốt nhất. LSTM **0/88** ngày trùng phiếu thắng.

**Kết GT-3: xác nhận** — đây là chỗ rơi chính.

### GT-4 — Ghi đè sau bầu?

Cờ hiện tại: V10640 MT tắt · V10790 MT tắt · các lớp MB tắt; chỉ còn V10640 MN.

| Cửa sổ | % ngày ghi đè | Hit phiếu | Hit công bố | Chênh |
|---|---:|---:|---:|---:|
| Nửa sau từ 06/05 | 25,0% | 15,42% | 12,62% | **−2,80pp** |
| 180 ngày | 14,2% | 18,30% | 16,71% | −1,59pp |

Trong nửa sau: 3 lần ghi đè cứu / 6 lần phá / 13 hòa.

**Kết GT-4: xác nhận phụ** — ghi đè làm mất thêm ~2–3pp, không lớn bằng gộp phiếu.

### GT-5 — AUC 0,55 có đủ thành tiền?

Mô phỏng Gaussian khớp AUC (điểm trúng ~ N(μ,1), trượt ~ N(0,1), μ=√2·Φ⁻¹(AUC); phân phối số đài/số trúng lấy từ MT thật):

| AUC | Hit top-1 ước lượng | vs hòa vốn 18,37% | Đủ hòa vốn? |
|---|---:|---:|---|
| 0,50 | 16,04% | −2,33 | không |
| 0,52 | 18,23% | −0,14 | không |
| **0,55** | **21,68%** | **+3,31** | **có** |
| 0,5517 | 21,84% | +3,47 | có |

AUC tối thiểu để hòa vốn (mô phỏng): **~0,5135**.

Đối chiếu thực tế: LSTM holdout top-1 **21,4%** ≈ lý thuyết. RF/XGB holdout top-1 **13–14%** — **không chuyển được** AUC thành tiền vì bộ ứng viên + xếp hạng trong bộ.

**Kết GT-5:** về toán, AUC 0,55 **không phải quá nhỏ**. Chỗ hỏng là khâu chuyển, không phải bản thân AUC. Nói thẳng: **RF/XGB hiện không cứu được ở top-1 holdout**; LSTM holdout có cửa nhưng live đang hỏng.

### Phát hiện thêm — LSTM live lệch

15 ngày gần: tái suy luận `predict_with_lstm` chỉ khớp `bt_number` đã ghi **13,3%**. Nhiều ngày 19–25/07 MDE kẹt số **96**. Holdout LSTM tốt (+4,94pp) nhưng live MDE nửa sau **10,9%** (−5,58pp) — hai thế giới khác nhau.

---

## 4. Hướng xử lý và vì sao chọn

| Phương án | Ước lợi thế thu lại | Ngày cần để chứng minh | Chọn? |
|---|---|---|---|
| A. Shadow BT MT = RF hoặc XGB đơn (không gộp) | ~3–7pp vs công bố hiện tại; hướng về ~19–20% | 60–90 ngày (z≥2 vs đánh bừa) | **Đề xuất #1 sau 08/08** |
| B. Sửa LSTM live (kẹt/lệch) rồi đo lại | Holdout gợi ý +5pp nếu live khớp | 30 ngày sau khi sửa | Đề xuất #2 — điều tra kỹ trước |
| C. Mở rộng bộ ứng viên >30 cho RF/XGB | Không rõ; có thể +vài pp nếu phủ thêm số trúng | 60 ngày | Phụ, sau A/B |
| D. Đánh top-10 thay vì 1 số | GT-1 RF/XGB **không** ủng hộ | — | **Loại** |
| E. Tăng trọng số ML vào total ngay | QD-013 đóng; z RF chỉ 1,34 | — | **Loại** — tô hồng |
| F. Kết luận "không cứu được", bỏ ML | LSTM holdout + RF live còn cửa đo được | — | **Loại** — quá sớm, nhưng cũng không được tô hồng |

**Chọn A làm đề xuất chính** vì bằng chứng GT-3 trực tiếp: bỏ gộp phiếu là lấy lại khâu mất nhiều nhất, không đụng official trong cửa sổ đóng băng (chỉ shadow sau 08/08).

Nói thẳng ngưỡng tiền: RF 19,91% chỉ **+1,54pp** trên hòa vốn 18,37%, z 1,34 — **chưa đủ chắc để đặt tiền** (QD-013 giữ đóng). Shadow là để chứng minh hoặc bác bỏ, không phải để chơi ngay.

---

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `web/backend/_v10955_do_tin_hieu.py` | Script đo GT-1..GT-5 trên VPS |
| `web/backend/_v10955_bo_sung.py` | LSTM live vs tái suy luận + voters |
| `web/backend/_v10955_governance.py` | Ghi CHANGELOG/SSOT/FU/AUTOMATION bằng `prepend()` |
| `artifacts/v10955_*.json` | Bằng chứng thô |
| `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` · `docs/FOLLOW_UP_TRACKER.md` | Cập nhật V10955 |
| `docs/AUTOMATION_STATE.json` | `governance_seq` +1 |

- **Backup / deploy:** không áp dụng — không sửa runtime.
- **Hash 4 bảng khoá:** không đụng DB ghi — không đổi.
- **Notion:** không ghi (A55).

---

## 6. Cổng kiểm

| Mục | Kết quả |
|---|---|
| Không sửa code runtime / không deploy | ĐẠT |
| AUC đo lại khớp file metrics (RF/XGB/meta) | ĐẠT — sai số 0 |
| Đủ 5 giả thuyết có số | ĐẠT |
| Tài liệu qua `prepend()` (không `open w` nuốt file) | ĐẠT |
| Báo cáo đủ 9 phần | ĐẠT (file này) |
| Đóng băng tới 08/08 được tôn trọng | ĐẠT |

---

## 7. Vướng vấp

1. **AUC sau huấn luyện 02:00 thấp hơn số 0,5517 cũ** (RF 0,5299) vì cửa sổ 20% cuối trượt theo ngày huấn luyện (FU-213). Hậu quả nếu bỏ qua: tưởng tín hiệu chết; thực tế hướng MT>0,5 vẫn còn.
2. **Holdout top-1 RF (14%) ≠ live MDE RF (20%)** trên cửa sổ khác nhau / đặc trưng CSV đóng băng vs live. Hậu quả nếu chỉ nhìn holdout: bỏ RF oan; nếu chỉ nhìn live: tô hồng. Báo cáo đưa cả hai.
3. **LSTM live ≠ tái suy luận (khớp 13%)** — phát hiện giữa phiên. Hậu quả nếu bỏ qua: đề xuất tin LSTM live dựa trên holdout sẽ sai.
4. **Thử nhiều lát cắt** — đã nêu rõ 3 cửa sổ; kết luận chính neo vào nửa sau + GT-3 đã khai trước trong FU-212.

---

## 8. Gỡ về

Không áp dụng vì không sửa code / không deploy. Xóa báo cáo công khai và hoàn nguyên mục tài liệu V10955 từ git nếu cần:

```
git checkout HEAD -- CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md docs/FOLLOW_UP_TRACKER.md docs/AUTOMATION_STATE.json
```

Thời gian: < 1 phút. Không có backup runtime vì không đụng VPS code.

---

## 9. Theo dõi tiếp

| Mã | Ngưỡng hành động bằng số | Hạn |
|---|---|---|
| **FU-212** | Sau 08/08: nếu owner ký shadow BT=RF/XGB — chạy 60 ngày; **pass nếu hit ≥18,37% và z≥2 vs đánh bừa** trên ≥150 đài | Rà 08/08; chốt shadow ~10/10 |
| **FU-210** | Vẫn mở: nguyên nhân tháng 6 mất lợi thế — V10955 chỉ khoanh chỗ rơi hiện tại, chưa giải thích vì sao nửa đầu từng +9,57pp | 08/08 |
| **FU-213** | Phép so AUC cũ↔mới lệch cửa sổ — không kết luận "tụt AUC" cho tới khi so cùng cửa sổ | Khi sửa guard |
| **QD-013** | Giữ đóng tới khi shadow (nếu có) đạt ngưỡng FU-212 | Đứng |

---

## Phụ lục — chuỗi rơi (nua sau MT)

```
Model RF đơn     19,91%  (+3,4pp, z 1,34)   ← còn tín hiệu yếu
      ↓ gộp phiếu (~14 model)
Số thắng phiếu   15,17%  (−1,3pp)           ← loãng
      ↓ ghi đè (25% ngày)
Số công bố       12,32%  (−4,2pp)           ← tệ hơn đánh bừa
```
