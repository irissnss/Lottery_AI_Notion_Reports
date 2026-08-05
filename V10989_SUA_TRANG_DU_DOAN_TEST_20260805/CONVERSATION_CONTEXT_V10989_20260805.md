# NGỮ CẢNH PHIÊN V10989 — 05/08/2026

Ghi **nguyên văn** lời owner, agent làm gì, và **vấp ở đâu**. Không diễn giải lại lời owner.

---

## 1. Owner nói gì — nguyên văn

**~10:07 ngày 05/08/2026 (giờ VN)** — owner gửi một ảnh chụp toàn màn hình trang
`/du-doan-test` tab MN, kèm đúng bốn chữ:

> **"em tự nhìn đi"**

Ảnh lưu tại `evidence/anh_chup_owner_du_doan_test_MN_1007.png`.

**Bối cảnh (nguyên văn từ đề bài phiên):**

> *"Owner đang rất bực vì hôm qua agent báo mục `FU-225` (xác minh UI) 'phần thuộc hệ đã đạt,
> chỉ chờ owner nhìn tận mắt' — owner nhìn, và **nó không đạt**."*

**Owner ra đề sáu câu, bắt trả lời bằng số, không đoán:**

1. Vì sao lane test MN không có số hôm nay 05/08 trong khi official đã chốt 05:19:51 và bây giờ
   đã 10:07? Job nào chạy lane test MN, lúc mấy giờ, có chạy không, log nói gì? Có phải cùng họ
   "cổng chỉ mở khi official chốt" như sự cố MB `/nghiem-thu` ngày 03/08 không?
2. Vì sao lùi về 01/08 mà không phải 04/08? Logic chọn ngày dự phòng ở đâu trong code? Đo xem
   `du_doan_test_bundles` có dòng nào cho MN ngày 02, 03, 04/08 không — nếu CÓ mà trang vẫn lùi
   về 01/08 thì đây là **lỗi chọn ngày**, không phải thiếu dữ liệu.
3. Vì sao ghi "MN cập nhật lúc ~04:30" trong khi mốc thật là 05:19? Con số 04:30 nằm ở đâu trong
   code, còn đúng không?
4. Vì sao TỰ MÂU THUẪN trên cùng một màn hình: *"(đã có kết quả)"* và *"Chưa xổ — cập nhật sau
   19:00"*? Hai chuỗi này do hai nhánh nào sinh ra, nhánh nào đúng?
5. Con số `Official 38%` lấy từ đâu? Cửa sổ bao nhiêu ngày, trục gì? Đối chiếu với số đã đo:
   7 ngày official **9/21 = 42,86%**; theo trục tiến MN **22,73%** (z 0,83). **Nếu 38% không
   khớp trục nào thì đây là con số gây hiểu nhầm** — nói thẳng.
6. `ADAPTIVE EXPLOIT V1 62%` — có mẫu bao nhiêu? z bao nhiêu? Nhãn *"hứa hẹn"* có vi phạm bài học
   **"đừng bật lại bằng backtest, chỉ bằng đo tiến"** không (chuỗi
   V10655→V10672→V10677→V10753→V10789→V10790 đều rữa)? Trang đang **hứa hẹn một lane 62%** ngay
   cạnh khuyến cáo — đây chính là kiểu chủ đề owner mất tiền theo. Đánh giá thẳng.

**Câu hỏi phụ:** sức khoẻ theo đài **n=6** có quá nhỏ để dán nhãn "MẠNH/YẾU" không? (Sóc Trăng
**YẾU 0%** với n=6 — 0/6 là chuyện bình thường khi nền 16%). Đánh giá và đề xuất ngưỡng tối thiểu.

**Ràng buộc owner đặt cho phiên:**

- `FU-225` phải mở lại thành `CLOSED_FAIL` / `REOPENED` — hôm qua đóng sai. Ghi rõ **đây là lỗi
  của agent, không được đổ cho owner**.
- Lỗi rõ ràng có bằng chứng thì **sửa ngay trong phiên**. NHƯNG `QD-014` còn hiệu lực đến hết
  08/08: **CẤM** đổi 15 model official, combo-super filter constants, override toggles,
  `/du-doan` writer, `final_bundles` writer, bộ chọn model production.
- Lỗi hiển thị / chọn ngày / nhãn chữ / con số thống kê trên trang → **không chạm vùng cấm** →
  sửa ngay. Lỗi nằm trong vùng đóng băng → **không tự sửa**, viết phương án + rủi ro + xin owner
  quyết.
- **Không được hứa hẹn** con số chưa đủ cỡ mẫu: phải ghi rõ cỡ mẫu + z, hoặc bỏ nhãn "hứa hẹn".
- Nguyên tắc §54: output thô phải luôn nhìn thấy được; cổng chỉ khoá tiền.
- **Tự kiểm lại bằng mắt máy:** sau khi sửa, **gọi thật API và đọc thật nội dung trả về** cho cả
  3 miền, dán số vào báo cáo. *"Đừng kết luận 'đã đạt' chỉ vì file giống nhau hay header đúng —
  đó là dùng cái sai hôm qua."*

---

## 2. Agent đã làm gì, theo thứ tự

| # | Việc | Kết quả |
|---|---|---|
| 1 | **Đọc ảnh chụp bằng công cụ đọc ảnh** (không tin mô tả) | Xác nhận đủ 4 nhãn sai + 2 con số + nhãn n=6 |
| 2 | Chạy `_v10920_session_start.py` | `FU-225` đúng là mục quá hạn duy nhất (hạn 03/08) |
| 3 | Đồng bộ dữ liệu sống từ VPS | `artifacts/live_sync/20260805_101006` |
| 4 | Dò `du_doan_test_bundles` (`PRAGMA table_info` trước — cột là `test_bt`, không phải `bach_thu`) | `MN_OUTPUT_V1` dòng cuối **01/08**; MT/MB dừng **31/07** |
| 5 | Dò VPS: crontab + syslog + log lane + `--dry-run` | **Cả 4 dòng cron bị chú thích** từ 01/08; lane **vẫn chạy tốt** khi gọi tay |
| 6 | Tra sổ quyết định | `OD-20260801-B` — owner **đã ký** cho lane nghỉ; `OD-20260801-G` đã tự nhận lỗ "chỉ soi import, không soi ai đọc BẢNG" |
| 7 | Tính kiểm định nhị thức 4 ô sức khoẻ | 3/4 nhãn **vô nghĩa** về thống kê |
| 8 | Sửa `main.py` + `du-doan-test.html` | 3 trạng thái lane · bỏ chuỗi ghi cứng · mọi tỉ lệ kèm `n=` · nhãn theo p-value |
| 9 | Soát cú pháp JS + đối chiếu bản Python | 0 lỗi · 4/4 ca khớp |
| 10 | Ghi sổ theo dõi + CHANGELOG + SSOT + bảng mốc tải | 3 cổng tự chặn đều qua |
| 11 | Deploy lượt 1 (10:30) | PID 834969→838717 · hash 4 bảng giữ nguyên |
| 12 | **Tự gọi API thật 3 miền** | Phát hiện `watch_n` của chính mình **đếm sai** |
| 13 | Sửa `watch_n` + dựng cổng đối chiếu + deploy lượt 2 (10:34) | PID 838717→839095 · 5/5 cặp khớp |
| 14 | Tự gọi API thật lại 3 miền | **ĐẠT 3/3** |
| 15 | Chạy 7 cổng kiểm tách riêng từng lệnh | Tất cả thoát 0 |

---

## 3. Vấp ở đâu — kể cả vấp do chính agent gây ra

### 3.1 Agent tự gây: `watch_n` đầu tiên đếm SAI, suýt viết một cáo buộc sai vào báo cáo

Lượt đầu agent đếm `watch_n` bằng `JOIN du_doan_test_results`. Chạy ra
`MT_SCREEN_BLEND_V1 50% n=0` và **đã soạn sẵn câu** "MT đang quảng cáo một lane với 0 mẫu — còn
tệ hơn 62%". Trước khi viết vào báo cáo, agent đọc lại `_v10725_champion_selector.trailing_pct`
và phát hiện nó **không chấm qua bảng đó** — nó so `test_bt` thẳng với tập đuôi trong
`lottery_results`. Vì bộ chấm lane test đã chết từ 28/07, đếm kiểu cũ ra `n=0` cho một lane
**vẫn đang được chấm bình thường**. Số thật là **n=14**.

**Đây là vấp nghiêm trọng nhất của phiên:** phiên đi sửa "con số gây hiểu nhầm" thì **suýt tự
đặt lên trang một con số gây hiểu nhầm khác**, và báo cáo gửi owner suýt chứa một cáo buộc sai.

Cách chặn: dựng `_v10989_check_n.py` **bắt `watch_n` khớp đúng `trailing_pct` 5/5 cặp mới cho
deploy**, rồi deploy lại lượt 2.

### 3.2 `FU-267` đã có chủ — suýt tái dùng số FU

Đề bài ghi *"số FU đang tới FU-267"*. Tra sổ thì `FU-267` **đã thuộc V10986**. Đã bắt đầu từ
`FU-268` và dựng cổng tự chặn tái dùng số ngay trong script ghi sổ.

### 3.3 Nhãn `REOPENED` owner nhắc tới không hợp lệ — phải chọn khác và nói rõ vì sao

Owner yêu cầu `FU-225` mở lại thành `CLOSED_FAIL` / `REOPENED`. Tra `_v10958_fu_reader`:
`REOPENED` **không có** trong `TREO_STATUSES` (9 nhãn) lẫn `DONG_STATUSES` (7 nhãn). Dùng nó là
đẩy mục thành **mồ côi** — đúng cái bẫy V10981b từng làm mất 11/14 mục. Đã dùng **`CLOSED_FAIL`**
(nhãn đóng hợp lệ, đúng nghĩa "đã kiểm và TRƯỢT") và chuyển việc sang `FU-268`.

### 3.4 Phải cập nhật bảng mốc tải cùng phiên, không thì cổng J5 trượt

Thêm 4 mục mới có hạn thì **bắt buộc** cập nhật `TAI_PHIEN_KHAC_DO_DUOC` trong
`_v10982_lich9.py` ngay trong phiên. Đã làm; `J5` báo *"mốc tải phiên khác khớp sổ thật 7/7 ngày"*.

### 3.5 Lỗi gốc của các phiên trước — nghiệm thu bằng dấu hiệu hình thức

`FU-225` được coi là "phần thuộc hệ đã đạt" dựa trên: file trên VPS giống file local · header
đúng · PID đã đổi. **Không phiên nào gọi API rồi đọc chữ trả về.** Trang chỉ cần một chuỗi ghi
cứng như `(đã có kết quả)` là mọi phép so file đều xanh trong khi người đọc bị nói dối.

### 3.6 Bài học đã ghi vào sổ mà không ai biến thành phép kiểm

`OD-20260801-G` đã ghi *"lượt đầu chỉ soi ai import MODULE, không soi ai đọc BẢNG mà module đó
ghi"*. Ghi rồi **nhưng không thành cổng**, nên `{MIỀN}_OUTPUT_V1` lọt lưới 4 ngày. Còn 5 lane
khác trong cùng đợt nghỉ chưa được soát lại — đưa vào `FU-269`.

---

## 4. Việc agent CỐ Ý KHÔNG làm, và vì sao

- **KHÔNG bật lại 4 dòng cron lane V10692.** Đó là **lật một quyết định owner đã ký**
  (`OD-20260801-B`, còn `ACTIVE`, hạn rà soát 08/08). §56 cấm agent tự đảo quyết định đã ký.
  Chuyển `FU-269` cho owner quyết, kèm hai đường và hậu quả bằng số. Bộ deploy có **phép tự
  chứng minh** không lén bật: đếm cron v10692 đang bật trước/sau = **0/0**.
- **KHÔNG đổi `RECENT`/`MIN_N`** trong `_v10642_slice_health.py` — bảng `slice_health` còn nơi
  khác đọc; owner mới yêu cầu *"đánh giá và đề xuất ngưỡng"*. Đã vá ở tầng hiển thị, đề xuất ghi
  `FU-271`.
- **KHÔNG sửa `recommend_play`** dù phát hiện MB đang khuyên chơi LANE trên n=8 — đụng bộ chọn
  khuyến cáo. Ghi `FU-269` để owner đọc sớm.
- **KHÔNG ghi gì vào Notion** — §57 cấm mọi thao tác ghi.

---

## 5. Điều agent muốn nói thẳng với owner

Owner không sai khi bực. Mục `FU-225` do **chính agent** tự viết `next_action = "Owner
hard-refresh /du-doan-test MN/MT/MB"` rồi **tự coi phần mình là xong** — tức là đẩy việc kiểm
thử sang owner trong khi phần thuộc về máy chưa hề được kiểm bằng máy. Bốn chữ *"em tự nhìn đi"*
là đúng chỗ.

Và có một chi tiết đáng nói hơn con số: lỗ hổng gây ra chuyện này **đã được ghi vào sổ quyết
định từ 01/08**, bằng chính lời owner chất vấn hôm đó. Ghi vào sổ nhưng không biến thành phép
kiểm thì nó chỉ là chữ. Vì vậy `FU-268` lần này định nghĩa "xong" bằng **nội dung API thật đọc
được**, không bằng "file giống nhau".


---

## Vòng hai cùng ngày (V10989b) — agent tự bắt thêm, owner chưa phải nhắc

**Owner không nói thêm câu nào ở vòng này.** Đây là hệ quả của đúng một câu owner đã ra lệnh ở
vòng đầu:

> *"Tự gọi API đọc nội dung THẬT cho cả 3 miền sau khi sửa, dán số vào báo cáo. Đừng kết luận
> 'đã đạt' chỉ vì file giống nhau hay header đúng — đó đúng là cái sai hôm qua."*

Làm đúng lệnh đó thì lòi ra dòng MB: `khuyến cáo = LANE · nền 11% n=8`. Soi tiếp thì thấy trang
đang bảo người đọc **chơi theo lane trên đúng 2 lượt trúng** (p=0,217), kèm chuỗi ghi cứng
*"vượt rõ + bền"* in ra bất kể cỡ mẫu, và chân khối mô tả cổng `n≥40` trong khi cổng thật của
đường đang đi là `n≥8`.

**Agent vấp ở đâu trong vòng này:**

1. **Vòng đầu chữa chưa hết.** Tôi chỉ soi nhánh *"đang THEO DÕI"* vì đó là chỗ owner chỉ mặt
   (`62% hứa hẹn`), mà **không soi nhánh khuyến cáo chính** — dù nó cùng một khối, cùng một hàm,
   cùng một bệnh. Nếu owner không ra lệnh "tự gọi API đọc chữ thật", lỗi này đã trôi qua và
   owner lại là người phát hiện lần thứ hai.
2. **Bộ hậu kiểm tôi tự viết báo TRƯỢT vì chính nó gõ nhầm đường dẫn** (`/api/admin/v10642/
   slice-health` → 404). Mất một lượt chạy để nhận ra lỗi nằm ở bộ đo chứ không ở hệ.
3. **Bộ deploy đếm chữ `"hứa hẹn"` ra 2 và gắn cờ**, hoá ra là 2 dòng **chú thích JS** tôi vừa
   viết. Phép đếm chuỗi thô không phân biệt mã với chú thích — thêm một bằng chứng nữa rằng
   nghiệm thu bằng đếm chuỗi là **không đủ**, phải dựng chữ thật rồi đọc.

**Cái được:** từ vòng này trở đi việc nghiệm thu trang không còn dựa vào "API trả đúng trường"
nữa. `_v10989b_render_check.js` **bốc đúng hàm dựng khối ra khỏi tệp đang phục vụ**, đổ dữ liệu
thật vào, rồi đọc chữ sau khi bỏ thẻ HTML — đúng thứ người đọc nhìn thấy.
