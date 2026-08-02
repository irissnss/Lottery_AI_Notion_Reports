# REPORT V10955b — Làm rõ hai con số RF: live +3,42pp ≠ CSV holdout −2pp (02/08/2026)

**Ngày:** 02/08/2026 · **Trạng thái:** bù báo cáo công khai A55 (V10962) · CHI ĐỌC

---

## 1. Tóm tắt

Owner bắt mâu thuẫn trong V10955. Đo lại: live RF **+3,42pp** (87 ngày) ≠ CSV holdout argmax **−2,09pp** (60 ngày). Re-infer cùng file model 02/08: RF còn **+2,95pp**, XGB chỉ **+0,10pp**. Đề xuất: giữ RF, rút XGB khỏi vị trí ngang hàng; shadow sau 08/08 kèm chốt tự cắt khớp live==re ≥95%/7 ngày. QD-013 vẫn đóng.

## 2. Owner yêu cầu gì (nguyên văn)

Owner bắt mâu thuẫn hai con số RF trong báo cáo V10955 (live dương vs holdout âm). Yêu cầu làm rõ — không sửa code.

## 3. Đào bới / phát hiện

| Con số | Nguồn | Cửa sổ | Hit % | vs bừa |
|---|---|---|---:|---:|
| **+3,42pp** | `bt_number` live MDE | 06/05→01/08 · 87 ngày | 19,91 | +3,42 |
| **−2,09pp** | Argmax CSV holdout | 03/06→01/08 · 60 ngày | 14,38 | −2,09 |

Re-infer: RF khớp top-1 live 31%; XGB 20,7%. Hit re-infer RF +2,95pp · XGB +0,10pp.

## 4. Hướng xử lý và vì sao chọn

Không rút RF; rút XGB khỏi ngang hàng. Ước lợi thế ~3pp (không 3–7, không lấy CSV −2). Chốt tự cắt 95% trước khi tin shadow. Không dựng code trong phiên (để QD-015 / 08/08).

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `_v10955b_live_vs_re.py` · `_v10955b_top5.py` | Đo chỉ-đọc |
| `artifacts/v10955b_*.json` | Bằng chứng |
| CHANGELOG V10955b | Ghi làm rõ |
| Báo cáo công khai | Bù thư mục riêng tại V10962 |

## 6. Cổng kiểm

- Chỉ đọc · không deploy · không đụng 4 bảng khoá
- Số liệu khớp artifacts V10955b

## 7. Vướng vấp

Hai thước đo khác nhau (live MDE vs CSV holdout) dễ bị trộn thành một kết luận. Hậu quả nếu bỏ qua: rút nhầm RF hoặc tin XGB ngang hàng khi re-infer ≈ đánh bừa.

## 8. Gỡ về

Không áp dụng (chỉ đo + tài liệu). Xoá artifacts/script đo nếu cần.

## 9. Theo dõi tiếp

- **QD-015 / FU-216** — shadow MT RF sau 08/08 + chốt tự cắt 95%
- QD-013 vẫn đóng tiền thật
