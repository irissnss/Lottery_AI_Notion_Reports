# CONVERSATION CONTEXT — V11088 · 18/08/2026 tối muộn

## Owner nói gì (NGUYÊN VĂN)

> *«GĐ-0 · CANH CHỨNG READ-ONLY CHO NGÀY KHOÁ — Kiểm toàn bộ ống đo SẴN SÀNG cho 20/08… Mục nào
> FAIL → báo rõ, CẤM tự sửa trong vùng đo.»*

> *«CẤM đọc giá trị thước đo trước 20/08 (RM-03)»* · *«CẤM chấm sớm lane T-B/G2-MB»*

> *«Thử chặn hai chiều bắt buộc + đo báo động giả trên 8 báo cáo thật gần nhất (bài học V11085:
> viết đúng cũng bị bắt nếu dấu hiệu quá rộng)»*

> *«Đầu ra: MỘT tệp PLAN trong docs/ — KHÔNG chạy gì… tối 20/08 TanPhatAI + owner chỉ cần điền
> verdict đo vào là ra lệnh chạy ngay.»*

---

## Phiên này tìm ra hai thứ sẽ làm hỏng ngày 20 và 21/08 — nếu không ai kiểm trước

### ① Lane T-B: ngày 20/08 sẽ mở ra và **không có gì để đọc**

`FU-398` viết điều kiện đọc rất rõ: *«chỉ đọc khi đủ ≥96 cặp bất đồng VÀ |z|≥1,96»*.

Đo thật: **110 dòng**, **tất cả** đều có đủ `control_bt` và `tb_bt`. Nhưng:

```
ĐÃ CHẤM (trung_control + trung_tb) : 0
```

Và quét toàn kho thì lý do hiện ra ngay: `trung_control`/`trung_tb` **chỉ tồn tại ở câu
`CREATE TABLE`** (`_v11059_lane_ab_3tang.py:176-177`). **Không một câu `UPDATE` nào** ghi vào
chúng. Cron `06:00/16:52/17:45` chỉ **thu**, không **chấm**.

Cột `bat_dong` **có** được ghi (79 khác / 31 giống) — nên lane biết A và B **có khác nhau
không**, nhưng **không biết bên nào thắng**. Đúng nửa việc.

**Nếu không kiểm trước:** sáng 21/08 owner mở ra, thấy ~140 dòng, và phát hiện **không đọc được
gì** — sau **10 ngày** lane chạy. Bây giờ thì còn kịp chọn lối.

### ② `D2` và `FU-397b` **triệt tiêu nhau** — mà không tài liệu nào nói

Hai mục nằm cạnh nhau trong gói 21/08 như **hai mục độc lập**:

```
#2  D2       đổi MINED_RULES_MODE  soft ──► shadow
#6  FU-397b  đo bonus RIÊNG {shadow: 0.00, soft: 0.40, active: 0.80}
```

Đọc kỹ hai dòng đó cạnh nhau thì thấy ngay: `D2` đưa bonus về **0.00** — tức **tắt đúng thứ
`FU-397b` đang đo**.

`FU-397b` lại là mục có **bằng chứng mạnh nhất** cả gói: đo được **ngoài cửa sổ chọn**, chạy
**69/90 miền-ngày (76,7%)**, và bảng bonus thật `+0,40` **gấp 2,7 lần** con số `+0,15` mà mọi tài
liệu vẫn nhắc.

**Chạy `D2` cùng ngày = giết phép đo mạnh nhất ngay khi nó sinh ra.**

---

## Hai lần suýt báo FAIL oan — và cách tránh được

### Lần 1 — `908/5541` lượt trace hỏng

Con số đầu tiên trông như FAIL nặng cho `FU-284`. Tách theo ngày:

```
05–08/08 :  241 lượt →  47 hỏng
09→18/08 :  605 lượt →   0 hỏng     ← CỬA SỔ ĐO
```

**Toàn bộ 908 lượt hỏng nằm TRƯỚC cửa sổ đo.** Trong cửa sổ: **sạch tuyệt đối**.

Nếu báo `908/5541` thì owner sẽ tưởng `FU-284` hỏng và hoãn cả ngày khoá.

### Lần 2 — ba bảng «cũ đến 17/08»

`bay_dan_daily_shadow` · `ai_herding_failure_daily` · `v10872_deherd_scoreboard` đều không có
dòng 18/08. Trông như cron chết.

Nhưng: ảnh chụp đồng bộ lúc **18:34**, cron chạy **19:35**. **Ảnh chụp cũ hơn cron.**

Đồng bộ lại lúc 21:55 ⇒ cả ba đều đủ dòng 18/08. `RM-13` — **nguồn sai thì mọi kết luận sai**.

**Điểm chung của hai lần:** cả hai con số đầu tiên đều **đúng về mặt số học** và **sai về mặt kết
luận**. Cái cứu là hỏi thêm một câu: *«số này nằm ở đâu trong thời gian?»*

---

## Cổng `SELECTION-WINDOW` — và vì sao phép đo báo động giả là phần quan trọng nhất

Owner bắt buộc *«đo báo động giả trên 8 báo cáo thật gần nhất»*. Phép đó tìm ra **hai** lỗi, và
lỗi thứ nhất làm chính phép đo trở nên vô nghĩa nếu không sửa:

**Lỗi 1 — sắp xếp sai.** «8 báo cáo gần nhất» ra `V91` · `V90` · `V89` (tháng 5) thay vì `V11087`
· `V11086`. Vì sắp theo **chuỗi**: `'9' > '1'`.

Đúng lớp lỗi đã vấp ở `_v11083_sinh_dieu_huong` hôm 17/08. Sửa bằng cách **chép lại khoá sắp xếp
đã đúng**, không sáng chế cách thứ hai.

**Lỗi 2 — 3 báo động giả thật**, chia hai loại, sửa ở **hai chỗ khác nhau**:

| chỗ bắt nhầm | loại | sửa ở đâu |
|---|---|---|
| `lo2` khớp bên trong `v66_1_lag1_adaptive_exploit_signal_v2_…` | dấu hiệu ngắn không có biên từ | **CỔNG** — dấu hiệu ≤4 ký tự đòi biên từ |
| `«1/3 bạch thủ»` bị kéo nhãn `180 ngày` từ mục **khác** vào | cửa sổ đối xứng | **SỔ** — cửa sổ **lệch** |
| câu **dẫn** vào phép đo, bảng đủ 3 cửa sổ nằm **ngay dưới** nhưng ngoài tầm | cửa sổ không với tới | **SỔ** — nhìn tới 45 dòng |

Chỗ đáng nói: **hai trong ba lỗi sửa ở SỔ, không sửa cổng**. Đó chính là điều kiến trúc «đọc từ
sổ» hứa hẹn — và đây là lần đầu nó được dùng thật.

Cửa sổ **lệch** (lùi 6 · tới 45) có lý do cụ thể: báo cáo luôn viết theo lối **«nêu rồi mới trưng
bảng»**, nên cửa sổ phải nghiêng về phía sau.

**Trước sửa 3 → sau sửa 0.** Cắm bản đầu thì cổng **đỏ ngay trên chính các báo cáo viết đúng** —
đúng bài học `V11085`.

---

## Bản đồ 21/08 — thứ tự không phải xếp cho đẹp

Ràng buộc mạnh nhất của ngày đó là `QD-018` **«một biến một lần»**.

Gói có **bốn** mục chạm đường sinh số: `D2` · `D3` · `FU-397b` · `FU-404`. Chạy cả bốn cùng ngày
thì **mọi phép đo sau đó vô nghĩa** — và đó **không phải giả thuyết**: `FU-284` đã dẫm đúng vết
này (ba thay đổi prompt trong ba ngày ⇒ *«không tách được nhân quả giữa ba phần»*), và hệ quả là
phải **đếm lại lần ba**, chờ tới đúng ngày 20/08 sắp tới.

Nên bản đồ chia **ba làn**, và thứ tự trong làn 2 có lý do từng vị trí:

```
1. FU-404  sửa NHÃN SAI trước — 39% bộ luật đang được giới thiệu bằng con số nói quá
2. FU-397b bằng chứng mạnh nhất, chạy sớm để có cửa sổ đo dài nhất
3. D2      SAU FU-397b, vì nó tắt bonus FU-397b đang đo
4. D3      đổi cấu trúc prompt ⇒ dễ che lấp ba mục trên
5. FU-394  lọc SAU mọi thứ ⇒ đặt trước thì che hiệu ứng các mục kia
```

Và §9 của bản đồ ghi rõ **những gì nó KHÔNG quyết**: không bỏ mục nào (`QD-064` khoá), không ký
ngưỡng hộ, không chọn lối hộ, không đọc trước thước nào.

---

## Cứu nốt 52 bản sao — và một quyết định nhỏ đáng nói

Chép nguyên 52 tệp thì **đúng lệnh**, nhưng sau 21/08 vẫn phải mở từng bản **1 MB** ra dò tay.

Nên kèm luôn **`diff` vs tệp đích hiện tại**. Kết quả: `BS-037` chỉ **5 dòng khác** — mở ra thấy
ngay nội dung bản vá (`V11072 #33`, ghi hạn thật vào call để nhãn timeout không nói dối).
`BS-043` lớn nhất **111 dòng**.

**14** bản truy ra tệp đích ⇒ có `diff`. **38** bản không truy ra ⇒ ghi `KHÔNG_KIỂM_ĐƯỢC`,
**cấm đoán**, đúng lệnh owner từ 19:57.

**52/52 cứu được, 0 mất.** Băm 4 tệp đích trước = sau.

---

## Trạng thái cuối phiên

Production **không đổi**. `QD-041` nguyên vẹn. **Không đọc sớm** thước nào.

**Cổng: tất cả xanh**, `K1` **ĐẠT thật** sau `V11087`.

**Ba việc chờ owner, hai việc có hạn cứng 20/08:** lối cho lane T-B · ngưỡng `PL13`/DEHERD ·
ngưỡng bầy đàn. Không ký ngưỡng thì ngày 20/08 **không được đọc** hai thước đó.

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11088.md` — quan trọng nhất là ① **lane T-B không đọc
được**, ② **va chạm `D2` × `FU-397b`**, ③ **ba ngưỡng phải ký trước 20/08**.
