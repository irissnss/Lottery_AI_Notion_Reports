# V106.38-R8 — TỔNG HỢP SỰ THẬT + CHUẨN HÓA + TÁCH LUỒNG (PUBLIC-SAFE)

> Public-safe mirror. Không chứa code riêng, dòng DB thô, API key, hay nội bộ VPS.
> Không claim ACCURACY_READY / OFFICIAL_IMPROVED / *_FIXED / LANE_TEST_PROMOTED.
> Read-only forensic + backtest. 0 thay đổi production. AI vẫn chạy bình thường.

- **Auditor**: Opus 4.7
- **Ngày**: 2026-05-29
- **Phạm vi live đo**: 91 ngày (2026-02-28 → 2026-05-29), 3 miền MN/MT/MB.

---

## 0. TÓM TẮT CHO CHỦ HỆ THỐNG

Sau khi soi toàn diện theo yêu cầu, có **6 nhóm phát hiện** lớn. Phần lớn là sự thật khó nghe nhưng cần thiết:

1. **Thước đo "win ~44%" gần như ngẫu nhiên** (định nghĩa hit = trúng bất kỳ giải nào toàn miền).
2. **Trần khả thi thấp** — xổ số gần ngẫu nhiên; edge thật tối đa nhỏ.
3. **Edge thật duy nhất có ý nghĩa thống kê: MB "số nóng" (frequency), miễn phí** — biên độ nhỏ, cần forward proof.
4. **Đơn model là "chuyên gia theo thứ/đài"** nhưng hệ thống chấm điểm gộp theo miền → loạn, không xếp hạng nổi.
5. **Tên đài + cột + bảng + file chưa chuẩn hóa** trên quy mô lớn (163 bảng, ~100 script).
6. **3 luồng (official / lane-test / shadow)** đã tách theo tên nhưng trục per-slice (miền×thứ×đài) còn thiếu.

---

## 1. SỰ THẬT ĐỘ CHÍNH XÁC (91 NGÀY)

| Miền | Win "lô toàn miền" | Ngẫu nhiên | Hơn ngẫu nhiên |
|---|---|---|---|
| MN | 43.96% | ~43% | ~0 (≈ ngẫu nhiên) |
| MT | 45.05% | ~35% | +~10pp (có chút skill) |
| MB | 24.18% | ~24% | ~0 (≈ ngẫu nhiên) |

- Bạch thủ "đề" (mục tiêu khó thật): ≈ bằng hoặc dưới ngẫu nhiên ở cả 3 miền.
- Xu hướng gần đây: MB tụt mạnh (đầu kỳ ~40% → cuối kỳ ~10%); MN giảm nhẹ; MT dao động, 14 ngày gần yếu.

---

## 2. NGHIÊN CỨU NGUỒN TÍN HIỆU (đã thử hết)

Đã backtest walk-forward + kiểm định thống kê (z, p) các hướng: đổi thuật toán gộp, chọn model giỏi, frequency (số nóng), gan (số lâu chưa về), lô rơi, chạm, đầu, đuôi, nháy, hybrid, per-slice, shrinkage.

| Hướng | Kết quả tốt nhất | Ý nghĩa thống kê |
|---|---|---|
| Model AI/ML curated | MT +~0.2 hít/ngày (p≈0.09) | chưa đạt |
| **MB frequency (số nóng)** | **+~0.4 hít/ngày (p≈0.004)** | **ĐẠT (borderline)** |
| gan / lô rơi / chạm / đầu / đuôi / nháy | ≈ ngẫu nhiên | không |

→ **Edge thật duy nhất: MB frequency — và miễn phí (không token AI).** Model AI tốn token nhưng không cho edge có ý nghĩa ở đâu cả.

---

## 3. ĐƠN MODEL LÀ CHUYÊN GIA THEO THỨ/ĐÀI

- Với mỗi miền, **model giỏi nhất KHÁC nhau gần như mỗi thứ** (MN: 7/7 thứ khác model; MT/MB: 6/7).
- "Model giỏi nhất toàn cục" KHÔNG phải số 1 ở phần lớn các thứ → xếp hạng gộp theo miền gây hiểu lầm.
- Hệ thống hiện chấm trọng số model **gộp theo miền** (trộn cả 7 thứ) → đây là lý do "ngày trúng ngày trật, không xếp hạng nổi".
- Hạn chế: 91 ngày = ~13 ngày/thứ → chưa đủ mẫu để chọn chuyên gia ổn định. Cần kỹ thuật co giãn (shrinkage) + tích lũy.

---

## 4. CHUẨN HÓA — TÊN ĐÀI / CỘT / BẢNG / FILE (quy mô lớn)

### 4.1. Tên đài trùng (cùng đài, khác cách viết)
- MN: HCM / TP. HCM (đài này chạy **T2 + T7**).
- MT (loạn nhất): Huế / Thừa Thiên Huế; Đắc Lắc / Đắk Lắk; Đắc Nông / Đắk Nông.
- MB: sạch (nhưng Hà Nội chạy T2 + T5).
- Đài chạy nhiều thứ phải tách thành ô `(đài × thứ)` riêng.

### 4.2. Cột: cùng chức năng, khác tên
- Model: 4 tên · Ngày: 3 · Miền: 3 · Thứ: 3 · Đài: 3 · Bạch thủ: 3 · Hit: 6 · Strength: 5 · Status: 4.
- Cùng tên khác kiểu (clash ngầm): có cột vừa dạng số vừa dạng chữ ('ALL'), dễ gây lỗi truy vấn.

### 4.3. Bảng + file
- **163 bảng** tổng cộng; **6 cặp bảng trùng chức năng** (3 cặp giống ~100%); **9 bảng chết** (0 dòng).
- **~100 script** backend nhiều cái trùng mục đích + bản sao trong thư mục backup.

---

## 5. TÁCH 3 LUỒNG (OFFICIAL / LANE-TEST / SHADOW)

| Luồng | Số bảng | Có đủ trục (miền×thứ×đài) |
|---|---|---|
| OFFICIAL | 10 | 2/10 |
| LANE-TEST | 24 | 2/24 |
| SHADOW | 62 | 13/62 |
| MEASUREMENT/DAILY | 38 | 3/38 |
| KHÁC/MƠ HỒ | 29 | 4/29 |

- 3 luồng ĐÃ tách vật lý theo tên (official = tên trần; lane = tiền tố `du_doan_test_`; shadow = hậu tố `_shadow`). Tốt.
- NHƯNG: phần lớn bảng **thiếu trục per-slice** (chỉ có miền, thiếu thứ/đài) → không phân tích độc lập theo miền×thứ×đài được.
- 29 bảng "mơ hồ" chưa rõ thuộc luồng nào.

---

## 6. ĐỀ XUẤT XỬ LÝ BÀI BẢN

### 6.1. Một chuẩn duy nhất (Data Dictionary)
- 1 tên/khái niệm: `date`, `region`, `ai_model`, `weekday`(0-6), `station`(canonical), `bach_thu`, `lo2`, `status`, `bt_hit`+`hit_count`, `strength`, `run_source`.
- Khóa per-slice = `(region, station_canonical, weekday)` + nhãn luồng `flow ∈ {official, lane, shadow}`.

### 6.2. Migration an toàn (từng bước, chờ duyệt)
1. **Phase 0 (rủi ro 0)**: viết Data Dictionary + bảng alias đài + map 163 bảng theo nhóm/luồng + lint cảnh báo tên không chuẩn.
2. **Phase 1 (rủi ro ~0)**: VIEW chuẩn hóa tên cột trên bảng gốc (không đổi bảng gốc).
3. **Phase 2 (duyệt)**: chuẩn hóa tên đài tại điểm nhập + giữ cột cũ làm alias.
4. **Phase 3 (duyệt + backup)**: backfill tên đài (chỉ đổi TÊN, không đổi SỐ) + gộp 6 cặp bảng trùng + bỏ 9 bảng chết.
5. **Phase 4 (duyệt)**: dọn file sprawl + bản sao backup.
6. **Phase 5**: governance chống tái loạn (Data Dictionary bắt buộc + hook lint).

### 6.3. Tách luồng rõ ràng
- Mỗi bảng/file gắn nhãn luồng minh bạch; bổ sung trục `(thứ, đài)` cho bảng còn thiếu.
- official / lane / shadow độc lập hoàn toàn theo miền×thứ×đài, kể cả prompt thử nghiệm shadow.

### 6.4. Tín hiệu
- Triển khai MB frequency (forward-validate, miễn phí).
- Chọn/đánh trọng số model theo `(miền × thứ × đài)` + shrinkage.
- Cắt token AI nơi không có edge.
- KPI thật: hít/ngày vs ngẫu nhiên + p-value, theo từng ô.

---

## 7. KẾ HOẠCH KIỂM CHỨNG 7 NGÀY
- Giữ AI chạy bình thường (không tắt) tới 2026-06-03.
- Sau khi chuẩn hóa tên (chỉ đổi tên, không đổi số) → đo mỗi ngày hít/ngày vs ngẫu nhiên per slice; so baseline.
- 2026-06-03: báo cáo "chuẩn hóa có tăng tín hiệu tốt không" bằng số thật.

---

## 8. NGUYÊN TẮC AN TOÀN (đã giữ trong toàn bộ R8)
- 0 thay đổi production · 0 deploy · 0 token chi thêm · 0 promote lane→official.
- Mọi thay đổi production chờ chủ hệ thống duyệt.
- Chuẩn hóa chỉ đổi TÊN, không đổi SỐ/giá trị.
- Không claim "đã fix" khi chưa đủ forward proof.

---

**Bottom line**: Hệ thống cần một đợt **chuẩn hóa nhất quán bài bản** (tên đài/cột/bảng/file + tách 3 luồng + trục miền×thứ×đài) làm NỀN, rồi mới khai thác edge thật (MB frequency) và chọn model theo slice. Trần xổ số thấp là thật, nhưng nền sạch + edge thật + đo đúng = hướng đi bền vững thay cho "đo nhiều chỉnh nhiều mà loạn".
