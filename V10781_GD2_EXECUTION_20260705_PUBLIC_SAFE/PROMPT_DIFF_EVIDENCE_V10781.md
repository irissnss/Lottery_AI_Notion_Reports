# V10781 — DIFF PROMPT TRƯỚC/SAU (E6a + E6b) — bằng chứng trích nguyên văn

Nguồn: `artifacts/v10780_prompt_audit/vps/prompt_*_2026-07-05.txt` (TRƯỚC — dựng trên VPS production GĐ1)
vs `artifacts/v10781_prompt_audit/prompt_*_2026-07-05.txt` (SAU — dựng lại sau deploy FIX-1/2/3).

## 1. E6b FIX-2 — Header đài MN Chủ Nhật (lỗi factual → đúng)

**TRƯỚC (dòng 187 + 557):**
```
## ĐÀI XỔ HÔM NAY (MN): Khánh Hòa, Kiên Giang, Kon Tum, Tiền Giang, Đà Lạt
Phân tích dữ liệu trên và DỰ ĐOÁN cho **MIỀN NAM** (Chủ Nhật, đài: Khánh Hòa, Kiên Giang, Kon Tum, Tiền Giang, Đà Lạt) xổ cùng ngày.
```
→ 5 đài, trong đó **Khánh Hòa + Kon Tum là đài MIỀN TRUNG** (nhiễm từ 229 rows 2020–21 gán region='MN' sai + query DISTINCT toàn lịch sử).

**SAU (dòng 187 + 505 + 512):**
```
## ĐÀI XỔ HÔM NAY (MN): Kiên Giang, Tiền Giang, Đà Lạt
Phân tích dữ liệu trên và DỰ ĐOÁN cho **MIỀN NAM** (Chủ Nhật, đài: Kiên Giang, Tiền Giang, Đà Lạt) xổ cùng ngày.
4. **FOCUS SÂU VÀO ĐÀI**: Phân tích pattern riêng của từng đài xổ hôm nay (Kiên Giang, Tiền Giang, Đà Lạt)
```
→ đúng **3 đài Chủ Nhật MN** theo lịch thực tế sau sáp nhập tỉnh (cửa sổ 84 ngày).

## 2. E6a FIX-1 — Nhãn nguồn MN (D-1 tường minh)

**SAU (dòng 191/201/230, prompt MN):**
```
### MIỀN BẮC (HÔM QUA) — ƯU TIÊN 1 (MB(D-1) 2026-07-04, 1 đài):
### MIỀN TRUNG (HÔM QUA) — ƯU TIÊN 2 (MT(D-1) 2026-07-04, 3 đài):
### MIỀN NAM (HÔM QUA) — ƯU TIÊN 3 (MN(D-1) 2026-07-04, 4 đài):
```
→ trước đây nhãn ưu tiên dạng "ƯU TIÊN ?" không rõ nguồn-ngày; nay mỗi khối nguồn khai (HÔM QUA) + mã nguồn `XX(D-1) <ngày>` — model không thể hiểu nhầm data D-1 là data cùng ngày.

## 3. E6a FIX-3 — Câu ràng buộc miền (dòng 506, ngay sau `## YÊU CẦU:`)

```
⚠️ RÀNG BUỘC MIỀN: Kết quả dự đoán CHỈ dành cho MIỀN NAM (MN) ngày 2026-07-05. Dữ liệu các miền
khác trong context chỉ là NGUỒN THAM KHẢO soi chéo — TUYỆT ĐỐI không dự đoán cho miền nguồn.
```
(tương tự cho MT và MB trong prompt tương ứng)

## 4. Ghi chú

- Snapshot POST cho target 2026-07-06 (`prompt_*_2026-07-06.txt`) dựng khi kết quả 05/07 chưa xổ nên khối nguồn D-1 trống — dùng cặp 2026-07-05 làm diff chính; snapshot 06/07 xác nhận header đài thứ Hai (TP.HCM, Đồng Tháp, Cà Mau) sẽ được verify lại trong báo cáo bổ sung sáng 06/07.
- Toàn văn 6 file snapshot nằm trong repo private `Lottery_AI_Test` tại `artifacts/v10781_prompt_audit/` (không đưa toàn văn lên public repo vì chứa chuỗi số liệu dài; trích dẫn trên là nguyên văn dòng liên quan).
