# V10882 — Luồng thứ 5 "Nghiệm Thu 19/08" = OFFICIAL NEW

**Ngày:** 30/07/2026 · **Trạng thái:** đã dựng lại đúng hình dạng, đã deploy, đang chạy thật

---

## 1. Owner nói gì

> *"Anh chả hiểu gì cả em làm cái gì thế? Anh đang nói vấn đề là xây 1 luồng mới 'Nghiệm Thu 19/08' chạy song song với 4 luồng hiện tại, áp dụng các phương pháp cơ chế mà em đã đo lường chuẩn bị để áp dụng cho offical. Nghĩa là 'Nghiệm Thu 19/08' offical New đó em hiểu chứ... Còn các vấn đề cắt đài, đổi số gì đó anh không hiểu thực sự không hiểu?"* — 30/07 10:41

---

## 2. Em làm sai hình dạng

V10879 dựng một phương án **đặt tiền**: mỗi miền một số, chỉ đánh vài đài chọn theo phong độ, rồi chấm lãi lỗ. Đó là việc của **luồng 4 — `/choi`, khuyên chơi**.

Owner cần một **luồng dự đoán** thứ 5: cùng khuôn với official, đặt cạnh official mà so từng ngày, và nếu tốt thì thay thẳng official.

Chuyện "cắt đài, đổi số" là do em trộn hai việc khác nhau vào một chỗ. Đã tách ra: luồng này chỉ dự đoán, không nói gì tới tiền. Phần tiền vẫn nằm nguyên ở `/choi` và các báo cáo V10876, V10881.

---

## 3. Vai trò trong sơ đồ luồng

| Luồng | Vai trò |
|---|---|
| 1 · official `/du-doan` | ÁP DỤNG |
| 2 · K-lane `/du-doan-test` | ĐỔI/THỬ — nơi duy nhất tiêm biến số mới |
| 3 · Total V2/V3 | ĐO LƯỜNG |
| 4 · `/choi` | KHUYÊN CHƠI |
| **5 · Nghiệm Thu 19/08** | **OFFICIAL NEW — ứng viên thay official** |

---

## 4. Giống official mọi thứ, khác đúng một biến

**Giống hệt:**

- Cùng 15 model output-eligible, cùng các dòng dự đoán pre-draw
- Cùng 5 lá bài: `bach_thu` · `lo2` · `lo3` · `xien2` · `xien3`
- Cùng luật lắp ráp: bạch thủ = hạng 1, lô 2 = hạng 1 + 2, xiên 2 = top 2, xiên 3 = top 3 nếu tỷ số điểm ≥ 0,40
- Cùng công thức `lo3` tần suất kề 180 ngày
- Cùng thước chấm: xiên chỉ tính TRÚNG khi tất cả số về **cùng một đài**; lô 3 càng phải khớp đủ 3 chữ số

**Khác đúng một chỗ — cách đếm phiếu:**

| | Cách đếm |
|---|---|
| official | `weighted_voting_wr` — cộng trọng số theo phong độ từng model |
| luồng mới | **de-herd family-√** — cộng theo họ model rồi lấy căn bậc hai trọng số họ |

Một biến số mỗi lần. Có khác biệt thì biết chắc nó đến từ đâu.

**Vì sao chọn de-herd:** đây là phương pháp duy nhất đã đo xong và sẵn sàng — hơn official +7,9pp trên 267 ngày (McNemar p≈0,0035, V10872) và thắng cả 15 phương án khác ở bake-off V10874. Lý do nó ăn: khi mười model cùng một họ đồng loạt chọn một số, đó là **một tiếng nói bị nhân lên mười**, không phải mười tiếng nói độc lập. Căn bậc hai bóp phần nhân lên đó lại.

---

## 5. Đối chứng 15/06 – 29/07 · 135 miền-ngày

### Gộp cả 3 miền

| Lá bài | OFFICIAL NEW | official | Chênh | Chỉ NEW trúng | Chỉ official trúng | p |
|---|---|---|---|---|---|---|
| **Bạch thủ** | **49/135** | 34/135 | **+11,1pp** | **19** | 4 | **0,0026** |
| **Lô 2 số** | **20/135** | 11/135 | **+6,7pp** | 12 | 3 | **0,0352** |
| Lô 3 càng | 6/135 | 6/135 | +0,0pp | 3 | 3 | 1,0 |
| Xiên 2 | 9/135 | 8/135 | +0,7pp | 3 | 2 | 1,0 |
| Xiên 3 | 2/111 | 2/111 | +0,0pp | 0 | 0 | — |

Hai lá chính hơn rõ rệt. Ba lá phụ gần như ngang — hợp lý, vì `lo3` dùng chung công thức tần suất, còn xiên phụ thuộc top-2 và top-3 vốn trùng nhau nhiều.

Cột `p` là xác suất chênh lệch này xảy ra do may rủi thuần tuý. Chỉ những ngày hai bên ra kết quả **khác nhau** mới mang thông tin; ngày cả hai cùng trúng hoặc cùng trượt không nói được gì.

### Bạch thủ theo từng miền

| Miền | NEW | official | Chênh | Lệch | p |
|---|---|---|---|---|---|
| MN | 22/45 | 17/45 | +11,1pp | 5 – 0 | 0,0625 |
| MT | 16/45 | 11/45 | +11,1pp | 7 – 2 | 0,1797 |
| MB | 11/45 | 6/45 | +11,1pp | 7 – 2 | 0,1797 |

Cả ba miền đều dương và đều đúng +11,1pp. Nhưng khi tách nhỏ, mỗi miền chỉ còn 45 ngày nên `p` chưa đủ mạnh.

**Nói thẳng: bằng chứng chắc ở mức gộp 3 miền, chưa chắc ở mức từng miền.** Đây là điều cần cân nhắc ở mốc chốt — có thể chỉ áp cho miền nào đủ bằng chứng thay vì áp cả ba.

Hai bên cùng ra một bạch thủ ở 48,9% số ngày — đồng ý khoảng một nửa.

---

## 6. Ngày đầu chạy thật — 30/07

| Miền | Bạch thủ | Lô 2 | Lô 3 càng | Xiên 2 | Xiên 3 |
|---|---|---|---|---|---|
| MN | `86` | 86 - 84 | `086` | 86 - 84 | — (không qua cổng 0,40) |
| MT | `20` | 20 - 54 | `120` | 20 - 54 | 20 - 54 - 76 |
| MB | `43` | 43 - 61 | `243` | 43 - 61 | 43 - 61 - 78 |

---

## 7. Luật chốt — giữ mốc, đổi thước

Vẫn tối thiểu **7 ngày** chạy thật, sớm nhất **05/08**, chặn cuối **19/08**.

Thước giờ là **bạch thủ** — lá bài chính của official — thay vì tiền. Cách đếm: chỉ tính những ngày hai bên ra kết quả khác nhau, bên nào thắng nhiều hơn thì bên đó hơn.

---

## 8. An toàn

Ghi `du_doan_test_bundles` tên `{REGION}_NGHIEMTHU_1908_V1`, `mode=OFFICIAL_NEW_CANDIDATE`, `test_only=1`, `output_eligible=0`. Ba dòng 30/07 tạo từ bản cũ đã ghi đè sang nhãn mới.

Hash 4 bảng official trước/sau **giống hệt**. `V10841_CONTRACT_PASS`. `/api/health=200` · `/du-doan=200` · endpoint admin `=401`.

`/du-doan-test` trả 401 là **bình thường** — trang cần đăng nhập, `/monitoring` và `/choi` cũng trả 401 khi chưa đăng nhập.

Không ghi `final_bundles`, không đụng `/choi`, không sửa official. Muốn lên official phải có chữ ký owner, và nếu lên thì đi qua cơ chế cờ có thể tắt (mẫu V10789 / V10790), không sửa thẳng.
