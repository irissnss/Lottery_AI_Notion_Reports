# V10883 — Trang riêng `/nghiem-thu` + ổ cắm bộ chọn vào official

**Ngày:** 30/07/2026 · **Trạng thái:** đã deploy · **Ổ cắm: TẮT cả 3 miền**

---

## 1. Owner yêu cầu gì

> *"UI của nó cũng cần làm cho chuẩn chỉnh để anh theo dõi ah em 3 miền rõ ràng. kế hoạch gộp và officical nên là đấu nối tiện lợi đấu nối xong mình cắt bỏ hoặc khởi động qua luồng khác đo khác cho tiện nha em."*

Hai việc: giao diện theo dõi cho ra hồn, và chỗ ghép vào official phải là công tắc chứ không phải hàn cứng.

---

## 2. Trang riêng `/nghiem-thu`

Luồng thứ 5 giờ có trang riêng như bốn luồng kia, không còn nằm nhờ trong bảng dày đặc ở `/monitoring`.

Trang lấy **nguyên các khối dùng chung của `/choi`** — theme, khung sidebar, drawer mobile — qua `_v10883_build_page.py`. Owner từng khen `/choi` là trang chuẩn nhất nên dùng đúng nó làm khuôn. Sau này `/choi` đổi áo thì chạy lại script là trang này khớp lại, không phải sửa tay.

**Bố cục:**

1. Khối phán quyết — đang chạy được mấy ngày, sớm nhất chốt ngày nào
2. **Ba thẻ miền — số hôm nay**, mỗi miền đủ 5 lá
3. **Ba thẻ miền — kỳ gần nhất đã có kết quả**, bản mới và official hai cột cạnh nhau, mỗi lá có nhãn TRÚNG / trượt
4. Bảng thành tích: forward (chạy thật) và backfill (đối chứng), gộp 3 miền và từng miền riêng
5. Lịch sử từng ngày, hai bên hai dòng liền nhau

Thêm mục **"Nghiệm Thu"** vào sidebar dùng chung của **12 trang**. Danh sách điều hướng được nội tuyến trong từng file HTML nên phải vá đồng loạt — thiếu bước này thì không có đường vào trang mới từ nơi khác.

---

## 3. Bộ kiểm giao diện bắt được lỗi mobile thật

Chạy Playwright trên 5 khổ màn hình: 1440 · 1280 · 820 · 390 · 360, cả Chromium lẫn WebKit.

### Lỗi tìm được

Trang rộng **630px trên màn 390px**.

Nguyên nhân: `.v2-content` là flex theo cột, mà `min-width:0` **chỉ có tác dụng theo trục chính**. Theo trục ngang, phần tử con vẫn nở tới kích thước nội dung tối thiểu — mà bảng bên trong đặt `min-width:620px` cho dễ đọc.

**Cách sửa đúng:** `max-width: min(1240px, 100%)` trên `.nt-wrap`. Lúc đó khung co về đúng bề ngang màn hình, và bảng tự cuộn ngang bên trong vùng `.nt-scroll` của nó.

### Một bản vá sai đã bị loại

Em từng thử `overflow-x:hidden` ở `.v2-content`. Nó làm chỉ số tràn trang biến mất, nhưng nội dung vẫn rộng 622px và **bị cắt** — che lỗi chứ không sửa. Đo lại bằng script riêng mới lộ ra.

### Bộ kiểm cũng từng báo sai

Lần chạy đầu mở trang bằng `file://` nên lệnh gọi API hỏng, trang trắng trơn mà vẫn báo "sạch, không có lỗi tràn". Đã đổi sang phục vụ qua http, và thêm điều kiện: trang render rỗng thì **không được** tính là sạch.

**Kết quả cuối: 5/5 khổ màn hình sạch**, không tràn ngang, không cắt chữ.

---

## 4. Ổ cắm bộ chọn vào official

Thay vì mỗi lần đổi phương pháp lại sửa thẳng `generate_final_bundle` rồi deploy (và muốn gỡ ra thì sửa lại lần nữa), official giờ có sẵn **một ổ cắm**.

```
official chấm điểm 15 model  ─┐
                              ├─→ [Ổ CẮM] ─→ lắp 5 lá bài ─→ final_bundles
bộ chọn ứng viên đã cắm      ─┘
```

Ổ cắm đặt **sau** khi official chấm xong và **trước** khi lắp 5 lá. Nên bộ chọn được cắm chỉ thay đúng một việc: thứ tự xếp hạng các số. Mọi thứ phía sau giữ nguyên — bạch thủ lấy hạng 1, lô 2 lấy hạng 1+2, cổng 0,40 cho xiên 3, công thức lô 3 càng, cách chấm điểm.

| Tính chất | Cách bảo đảm |
|---|---|
| **Mặc định TẮT** | Không có thiết lập nào thì official chạy y như cũ. Riêng việc deploy file này không làm đổi một con số. |
| **Theo từng miền** | Bằng chứng chắc khi gộp 3 miền nhưng mỏng ở từng miền (MN p=0,0625 · MT và MB p=0,1797), nên phải cắm riêng được cho từng miền. |
| **Hỏng thì tự rút** | Thiếu module, bộ chọn trả rỗng, ra dưới 2 số — đều rơi về xếp hạng official và ghi lại lý do. Ổ cắm không bao giờ được làm official mất số. |
| **Không cần deploy** | Cắm/rút bằng nút ở `/monitoring` hoặc dòng lệnh, hiệu lực từ lần chốt bundle kế tiếp. |
| **Bắt buộc ghi lý do** | API từ chối nếu không có lý do — đây là thay đổi chạm vào official. |
| **Truy vết được** | `generation_method` đổi thành `weighted_voting_wr+connector_<tên>` những ngày có cắm. |

**Nhật ký:** `v10883_connector_switch_log` ghi mỗi lần cắm/rút (ai, khi nào, lý do). `v10883_connector_apply_log` ghi mỗi ngày ổ cắm có tác dụng thật, kèm top 3 trước và sau, có đổi bạch thủ hay không.

**Bộ chọn hiện có:** `deherd_family_sqrt` — bằng chứng backfill 135 miền-ngày, bạch thủ 49 so với 34, +11,1pp, p=0,0026.

**Trạng thái sau deploy: TẮT cả MN, MT, MB.**

---

## 5. Một lỗi quy trình của em

Bài kiểm "chốt lại bundle của một ngày rồi so xem có giống không" trong lần deploy đầu đã gọi `generate_final_bundle`. **Hàm đó ghi vào `final_bundles`**, không phải chỉ đọc. Hậu quả: bundle MN 30/07 nhảy `bundle_version` từ 1 lên 2.

**Nội dung không đổi một chữ:** `BT=86`, `lo2=["86","31"]`, `lo3=086`, `xien2=["86","31"]`, `xien3=["86","31","36"]`, `method=weighted_voting_wr` — giống hệt bản chốt lúc 04:17. Chưa xổ nên không mất kết quả chấm nào. Và v2 vốn là trạng thái bình thường: mọi bundle của 29/07, 28/07, 27/07 đều là v2.

Đã thay bằng cách chứng minh **chỉ đọc code**: kiểm ổ cắm nằm trong `try/except`, lỗi thì giữ nguyên xếp hạng official, chỉ thay khi hàm trả về giá trị, nhãn method rơi về mặc định khi không cắm, và ổ cắm đặt trước khi lắp lá bài.

Bài học ghi vào tracker: bài kiểm "không tác động" tuyệt đối không được gọi hàm có ghi.

---

## 6. An toàn

Hash 4 bảng official trước/sau **giống hệt**. `V10841_CONTRACT_PASS`. Công tắc TẮT cả 3 miền.

Smoke: `/api/health=200` · `/du-doan=200` · `/nghiem-thu`, `/api/nghiem-thu`, `/api/admin/official-connector`, `/choi`, `/monitoring` đều `=401` khi chưa đăng nhập — đúng, tất cả đều là trang quản trị.

---

## 7. Bước tiếp

| Việc | Khi nào |
|---|---|
| Đọc phán quyết luồng Nghiệm Thu | 05/08 |
| Nếu ĐẠT, owner quyết cắm miền nào | sau 05/08 |
| Hạn chót | 19/08 |

**Ổ cắm sẽ không tự bật.** Mọi lần cắm đều cần quyết định của owner và lý do được ghi lại.
