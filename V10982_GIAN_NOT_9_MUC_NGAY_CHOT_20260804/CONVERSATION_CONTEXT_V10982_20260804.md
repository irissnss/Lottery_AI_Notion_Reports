# Bối cảnh hội thoại — V10982 · 2026-08-04

Ghi lại **nguyên văn** lời owner trong phiên, agent làm gì, và vấp ở đâu. Theo §57.2 (A55.2).

---

## 1. Nguyên văn lời owner

### 1.1 Quyết định gốc — 10:29 ngày 04/08/2026 (đã ký ở `QD-021`, phiên V10981)

> *"Giãn ra cuốn chiếu tới hết ngày 10/08 phải hoàn thành, làm lần lượt những vấn đề nào xác
> thực rõ ràng , đơn giản làm trước tới cuối cùng 10/08 phải xong"*

### 1.2 Quyết định của phiên này — ~11:0x ngày 04/08/2026

Sau khi V10981 giao trang lịch, trang đó tự nêu ra chỗ chưa xong:

> ⚠ **Ngày 10/08 đang gánh 11 mục** — nhóm 14 chỉ chiếm 2, còn 9 mục là hạn có sẵn từ các
> phiên trước (V10974–V10980). Nhóm 14 đã cố ý tránh dồn vào đây. Nếu owner muốn ngày chót nhẹ
> hơn thì phải giãn tiếp nhóm mục cũ đó — nằm ngoài phạm vi phiên này, cần owner cho phép.

Owner đọc và trả lời:

> *"Giãn luôn 9 mục cũ đó ra 05-09/08 cho ngày chốt nhẹ nhé"*

### 1.3 Owner duyệt đề nghị mục 6 — ~12:4x ngày 04/08/2026 (V10982b)

Báo cáo `V10982` mục 6 nêu một đề nghị và nói rõ *"nằm ngoài phạm vi V10982 nên không tự làm"*:

> **Đề nghị owner cân nhắc:** chuyển `FU-224` *Dọn trang frontend trùng/chết* từ 09/08 xuống
> 06/08 — mục đó chỉ đụng file HTML/JS, không chạm runtime dự đoán, kéo 09/08 từ 9 xuống 8.

Owner chọn phương án, nguyên văn:

> *"Chuyển xuống 06/08 - 09/08 còn 8 mục"*

Kèm chỉ đạo thực thi: đổi hạn trong sổ theo dõi, cập nhật mã đọc §58 cho khớp hạn mới, **giữ
nhãn trạng thái hợp lệ** (*"tuyệt đối không tạo nhãn lạ - nhớ lại lỗi V10981b làm 11 mục mồ
côi"*), cập nhật trang lịch, ghi nhận vào `QD-022`, prepend `CHANGELOG` + `SSOT`, cập nhật báo
cáo công khai mà **không xoá tiêu đề 9 phần**.

Đó là toàn bộ chỉ đạo trong phiên. Không có câu nào khác.

---

## 2. Agent làm gì

### 2.1 Trình tự

1. Đọc `docs/LICH_CUON_CHIEU_DEN_10082026.md` và `web/backend/_v10981_kiem_lich.py` để hiểu
   phiên trước đã dựng gì và cổng nào đang canh.
2. Đọc `_v10958_fu_reader.py` (bộ đọc sổ theo dõi), `_v10981_lich.py` (bảng 14 mục),
   `_v10981_trang_lich.py` (bộ sinh trang).
3. Chạy baseline: `_v10981_kiem_lich.py` → **8/8 ĐẠT**; `_v10920_decision_ledger.py` → **0
   TRÔI**, 23 quyết định.
4. Viết `_v10982_probe.py` (chỉ đọc) để đếm chính xác mục theo ngày và tách nhóm 9 khỏi nhóm
   14 → xác định đúng **9 mã**: `FU-185` `FU-188` `FU-223` `FU-244` `FU-252` `FU-253` `FU-254`
   `FU-255` `FU-257`. Cũng đếm được **19 mục mồ côi** làm mốc trước phiên.
5. Viết `_v10982_probe2.py` để in nguyên thân khối mới nhất của từng mục trong 9 mục — biết
   mỗi mục là gì, ai mở, ngưỡng ra sao.
6. Đọc `QD-013` `QD-014` `QD-021` nguyên văn trong `docs/OWNER_DECISION_LEDGER.json` để biết
   phạm vi đóng băng chính xác đến đâu.
7. Đọc `docs/ACTIVE_ROADMAP_LEAN_HARVEST_20260619.md` — phát hiện 3 trong 9 mục thuộc thẳng
   CP-L2 và CP-L3.
8. Viết `_v10982_probe3.py` soát va chạm mã đọc §58 cho 9 mã ứng viên.
9. **Phiên bị gián đoạn tại đây.**
10. Nối lại: tự kiểm `git status` + `git log` cả hai repo, xác nhận chưa ghi gì ngoài 3 script
    dò.
11. Backup 7 file vào `backups/v10982_pre/` **trước khi** sửa bất cứ thứ gì.
12. Dựng `_v10982_lich9.py` (nguồn sự thật), `_v10982_kiem_lich9.py` (cổng J1–J8),
    `_v10982_ghi_so.py` (ghi sổ qua `prepend()`), `_v10982_ghi_quyet_dinh.py` (`QD-022`),
    `_v10982_gov.py` (CHANGELOG + SSOT).
13. Mở rộng `_v10981_trang_lich.py` thêm cột nhóm 9 và mục §8.
14. Chạy lại toàn bộ cổng kiểm, viết báo cáo, push.

### 2.2 Kết quả

Ngày chốt **10/08: 11 → 3 mục**. Mồ côi **19 → 18**. Cả hai cổng lịch **8/8**. Sổ quyết định
**0 TRÔI**, `QD-022` khớp **7/7**.

---

## 3. Vấp ở đâu

### 3.1 Trần ≤5 mục/ngày không đạt được — phải báo lại thay vì ép số

Yêu cầu ban đầu là tổng tải mỗi ngày ≤5. Khi đếm tải sẵn có mới thấy **09/08 đã là 7 mục trước
khi phiên bắt đầu**, và chỗ trống thật ở mức trần 5 chỉ còn 6 khe trong khi phải xếp 8 mục.

Cách xử: nhận trần **thực tế = 6** cho những ngày phiên này động vào, để nguyên 09/08 ở mức 9,
ghi rõ 7/9 mục ở đó là có sẵn từ trước, và kèm một đề nghị cụ thể cho owner (chuyển `FU-224`
xuống 06/08). Không giấu, không làm tròn cho đẹp.

### 3.2 Suýt lặp lại đúng lỗi mà V10981b vừa vấp 2 giờ trước

`V10981b` (cùng ngày) đã gán nhãn tự chế `SCHEDULED` cho 14 mục; nhãn đó không nằm trong
`_v10958_fu_reader.TREO_STATUSES` nên **11/14 mục rơi khỏi mọi bộ đếm** — ngay trong phiên đi
vá chuyện mồ côi. Họ đã sửa và thêm phép `K8` để chặn.

Phiên này chủ động phòng bằng máy chứ không bằng trí nhớ: tra danh sách nhãn hợp lệ **trước
khi** viết bảng, và `_v10982_ghi_so.py` có đoạn chặn `sys.exit(1)` nếu gặp nhãn ngoài danh
sách. Phép `J8` canh cả nhóm 9 lẫn tổng mồ côi toàn sổ. Kết quả 9/9 nhãn hợp lệ ngay lần ghi
đầu tiên, không phải sửa lại.

### 3.3 Lý do hoãn cũ rộng hơn chữ ký của owner — nhưng không lật hết

`FU-185` `FU-188` `FU-244` đều bị các phiên V10975/V10978 hoãn với lý do *"đụng production
trong cửa sổ đóng băng QD-014"*. Đọc nguyên văn `QD-014.ghi_chu` thì phạm vi đóng băng là
**đường TẠO SỐ CÔNG BỐ**, và ghi rõ *"Được phép: sửa lỗi kỹ thuật rõ ràng, điều tra chỉ-đọc,
viết tài liệu"*. Không mục nào trong 9 mục chạm 5 thứ bị cấm đích danh.

Nhưng khi đào tiếp thì tìm ra một ràng buộc THẬT mà các phiên trước chưa nêu: `FU-185` và
`FU-253` sửa cron trong khung **17:38–17:43**, trong khi tiêu chí thứ 3 của `FU-186`
(*"6 lane đã nghỉ vẫn lệch 0 ở bộ tự kiểm 18:05"*) đang được đo ở đúng khung đó, cửa sổ 7 ngày
kết thúc 08/08. Sửa giữa cửa sổ là lật tiêu chí đang đo từ TRƯỢT sang ĐẠT giữa chừng.

Nên kết cục là: `FU-244` và `FU-188` **kéo lên được**, `FU-185` và `FU-253` **vẫn nằm 09/08** —
nhưng lý do ghi trong sổ nay là lý do thật, không phải lý do mượn.

### 3.4 `FU-185` đổi mẫu số của `FU-253` — phát hiện muộn, suýt bỏ sót

Xếp xong lần đầu mới nhận ra `FU-185` gỡ **2 trong 5 cron** đang đè nhau ở khung 17:40–17:43,
tức là nó thay đổi chính điều kiện mà `FU-253` đang đếm. Nếu để `FU-185` chạy trước rồi mới
đếm cho `FU-253`, con số đếm được sẽ vô nghĩa.

Đã xử: chốt cửa sổ đếm của `FU-253` là **04→08/08** (nền sạch, trước khi dọn), hai mục đứng
cùng ngày 09/08 theo thứ tự `FU-185` trước, và ghi quan hệ này vào ô `phu_thuoc` của cả hai.

### 3.5 `FU-244` hoá ra đang là mồ côi

Khi in thân khối mới nhất mới thấy `FU-244` có ô `status` **rỗng** — nó là 1 trong 19 mục mồ
côi mà kiểm toán V10980 sáng nay vừa bêu. Đã trả về nhãn thật `MEASURED_ROOT_CAUSE`, cùng nhãn
với ba mục anh em cùng phiên V10978. Mồ côi toàn sổ **19 → 18**.

### 3.6 Mã đọc `KS1008` viết sai quy ước

`FU-252` mang mã đọc `KS1008` (DDMM) trong khi cả kho dùng **MMDD** — đọc theo quy ước kho thì
`1008` là tháng 10. Đã đổi thành `KS0810-5` cho khớp hạn 10/08 thật, dù hạn của mục này không
thay đổi. Không tái dùng mã `KS0810` mà `FU-244` vừa nhả ra, để lịch sử tra ngược không lẫn.

### 3.7 V10982b — bảng mốc tải ghi cứng, cổng không bắt được nếu quên cập nhật

Khi chuyển `FU-224` mới thấy: bảng `TAI_PHIEN_KHAC_DO_DUOC` trong `_v10982_lich9.py` được **ghi
cứng** làm mốc, và mọi con số tải trong `CHANGELOG`, trang lịch, báo cáo đều đọc từ đó. Nếu chỉ
đổi hạn trong sổ theo dõi mà quên bảng này thì tất cả số in ra sẽ sai **mà cả 8 phép J1–J8 vẫn
báo ĐẠT** — đúng loại xanh giả owner sợ nhất.

Cách xử: siết phép `J5` cho đối chiếu bảng mốc với **sổ theo dõi THẬT**, trượt nếu lệch. Rồi
**thử ngược để chứng minh cổng thật sự có tác dụng**: chạy cổng ở trạng thái mốc đã đổi nhưng
sổ chưa đổi → `J5` TRƯỢT, in đúng tên `FU-224` ở cả hai ngày lệch (06/08 và 09/08), exit 1. Sau
khi ghi sổ thì ĐẠT. Vẫn giữ 8 phép, không thêm phép thứ 9 để khỏi phá lời hứa "8/8".

**Hậu quả nếu bỏ qua:** owner xếp việc theo một bảng số cũ mà tưởng là mới.

### 3.8 V10982b — nhãn `OWNER_LOCK` phải giữ, không được nâng

Có thoáng nghĩ đổi nhãn `FU-224` vì "owner đã duyệt rồi". **Sai.** Owner duyệt việc **đổi
ngày**, chưa duyệt việc xử từng trang — `next_action` vẫn là *"Owner chọn: giữ / gộp / bỏ. Agent
KHÔNG tự xoá trang."* Đổi nhãn sẽ biến một mục còn chờ owner thành mục đã thông, và ngày 06/08
agent có thể tự cho phép mình xoá trang. Giữ nguyên `OWNER_LOCK`, ghi rõ ranh giới này vào cả
sổ theo dõi, trang lịch và `QD-022`.

### 3.9 PowerShell không nhận `&&`

Lệnh đầu tiên dùng `cd ... && python ...` bị PowerShell từ chối (*"The token '&&' is not a
valid statement separator"*). Chuyển sang `;`. Ghi lại vì đây là lỗi lặp trên máy Windows này.

---

## 4. Việc phiên này CỐ Ý không làm

| Việc | Vì sao không làm |
|---|---|
| Deploy | Phiên là lập kế hoạch + tài liệu. `QD-014` còn hiệu lực hết 08/08 |
| Sửa đường ra số | Không đụng 15 model official, bộ lọc combo-super, lớp ghi đè, `/du-doan`, writer `final_bundles` |
| Đổi crontab | Không dòng cron nào bị thêm/xoá trong phiên này — các mục chỉ được **xếp ngày**, chưa thi hành |
| Đụng lịch nhóm 14 | Ngoài phạm vi. `_v10981_kiem_lich.py` chạy lại vẫn 8/8 để chứng minh |
| Chuyển `FU-224` khỏi 09/08 | Ban đầu chỉ **đề nghị** vì ngoài 9 mục được giao. **Owner duyệt ~12:4x cùng ngày → đã làm ở V10982b** (§1.3) |
| Xoá/gộp trang frontend của `FU-224` | Owner duyệt đổi ngày, **chưa** duyệt xử trang. Nhãn `OWNER_LOCK` giữ nguyên, agent không tự xoá |
| Ghi vào Notion | §57.1 cấm mọi thao tác ghi Notion |

---

## 5. Tệp bằng chứng

| Tệp | Nội dung |
|---|---|
| `evidence/v10982_gian_9_muc.json` | Bảng lịch mới dạng JSON — 9 mục, tải mỗi ngày, mục không kết luận nổi trong hạn |
| `evidence/cong_kiem_J1_J8.txt` | Kết xuất `_v10982_kiem_lich9.py` — 8/8 ĐẠT |
| `evidence/cong_kiem_nhom14_K1_K8.txt` | Kết xuất `_v10981_kiem_lich.py` — nhóm 14 vẫn 8/8, không bị phá |
| `evidence/so_quyet_dinh_0_troi.txt` | Kết xuất `_v10920_decision_ledger.py` — 0 TRÔI, `QD-022` khớp 7/7 |
| `evidence/briefing_dau_phien_sau.txt` | Briefing sau phiên — hạn mới hiện đúng, mồ côi 18 |

Không có API key, secret hay thông tin đăng nhập trong bất kỳ tệp nào ở trên.
