# CONVERSATION CONTEXT — V11084 · 17/08/2026 tối

## Owner nói gì (NGUYÊN VĂN)

> *«Còn gì tồn đọng — luật · kiểm soát hệ thống, các vấn đề đã và đang xử lý, về kết quả dự đoán
> hôm nay.»*

> *«em đã push báo cáo hết chưa em?»*

---

## Câu hỏi thứ hai là lý do bản này tồn tại

Kiểm lại thì **mã đã push đủ** — cả hai kho, không commit nào treo. Nhưng **phân tích live hôm
nay chỉ nằm trong chat**.

Đó là đúng lỗ hổng `§57.2` sinh ra để bịt: *«sau MỌI việc code, fix, audit cần đẩy báo cáo report
lên github report public»*. Một phiên phân tích có số, có kết luận, có hai giả thuyết bị bác — mà
chỉ tồn tại trong khung chat thì **ngày mai không ai tìm lại được**, kể cả chính agent phiên sau.

Và nó thuộc loại **dễ mất nhất**: không có mã nào thay đổi nên không có commit, không có
diff, không có dấu vết nào trong `git log`.

---

## Hôm nay 3/3 — nhưng con số đáng nói không phải con số đó

Ba miền đều trúng bạch thủ. Kiểm từ `prizes_json`, **không** từ cột `bach_thu_status` — vì cột
đó là **kết quả chấm của chính hệ đang được đo** (`RM-13`).

| miền | bạch thủ | trúng ở | nền đúng ngày đó |
|---|---|---|---|
| MN | `89` | TP. HCM | **45%** |
| MT | `64` | Thừa Thiên Huế | **31%** |
| MB | `55` | Hà Nội | **25%** |

Xác suất 3/3 ngẫu nhiên: **3,5%**. Ngày đẹp thật.

**Nhưng:** dấu của lợi thế **đổi theo cửa sổ** — 30 ngày `+4,07pp`, **90 ngày `−3,18pp`**,
180 ngày `+0,91pp` với `CI95 [−3,2 · +5,0]`.

Nếu chỉ báo cửa sổ 30 ngày thì bản báo cáo này vi phạm **đúng luật vừa ban hành sáng nay**
(`PRJ-SELECTION-WINDOW-001` mục 3: *«tách và báo CẢ HAI»*). Luật ban hành buổi sáng, buổi tối đã
có ca thử — và ca thử đầu tiên là chính agent.

---

## Hai giả thuyết agent nêu, và tự bác bằng số

### ① «Ba miền tụ với nhau»

14 ngày gần nhất **không có ngày nào 2/3** — toàn `3/3`, `0/3`, `1/3`. Nếu độc lập với `p ≈ 0,34`
thì `2/3` phải xuất hiện **~3 lần**. Mẫu hình sạch sẽ, dễ tin.

Và nếu có tụ thật thì **hệ quả rất lớn**: mọi khoảng tin cậy đang tính đều **hẹp giả**, tức mọi
kết luận «chưa đủ bằng chứng» trước đó đều phải xem lại.

Đo phân bố thật so với kỳ vọng độc lập, dùng **nền riêng từng miền-ngày**:

```
30 ngày   χ² = 9,38   VIF = 1,416    ← trông có tụ (vượt ngưỡng 5%)
60 ngày   χ² = 7,02   VIF = 1,086    ← hết
90 ngày   χ² = 2,91   VIF = 1,002    ← độc lập gần như hoàn hảo
```

**BÁC.** Nhiễu của `n = 14`. Đúng `RM-04`: *n nhỏ không chỉ yếu mà KHÔNG ỔN ĐỊNH*.

Và `VIF = 1,002` cho thước bạch thủ **khớp** với `0,889` đo trước đó, **tiếp tục khác hẳn**
`2,92` của thước *16 model cùng đoán một ngày* — `RM-21` đứng vững thêm một lần.

### ② «MN chốt 05:20 nên lỡ bộ học»

Giờ chốt bundle rất ổn định qua 10 ngày: MN `05:19`–`05:31` · MT `16:42`–`16:57` ·
MB `17:34`–`17:42`. Hạn lần lượt `15:45` · `16:58` · `17:58`.

MN chốt sớm hơn hạn **hơn 10 tiếng**, trong khi hai miền kia chốt sát hạn. Nghe hiển nhiên là
bất lợi.

**Đo:** `model_daily_eval` ghi lúc **`20:20` tối hôm trước**, đều đặn 7/7 ngày. `20:20` hôm trước
**<** `05:20` hôm sau ⇒ MN **có** bản eval mới nhất. **BÁC.**

---

## Điểm chung của hai lần bác — và vì sao phải ghi lại

Cả hai giả thuyết **nghe rất thuyết phục TRƯỚC khi đo**. Nếu báo lên trước khi đo thì owner đã
mất công đi kiểm hộ **hai lần** — đúng chuyện owner đã than mệt.

Đây là **lần thứ hai trong tuần** cùng một cơ chế cứu: `FU-316` (neo pool D-1) cũng có cả agent
lẫn bản đào 49 tác nhân **cùng nghiêng về «có neo»**, đo ra `−0,79pp, z = −1,01` ⇒ **không neo**.

Và đây là lý do phải **ghi cả hai lần bác vào báo cáo**, không chỉ ghi kết luận: nếu chỉ ghi
*«180 ngày +0,91pp»* thì phiên sau nhìn bảng 14 ngày sẽ **thấy lại đúng mẫu hình «không có ngày
2/3»** và đi đo lại từ đầu. Ghi rõ *«đã đo, đã bác, đây là số»* là cách duy nhất để nó không quay
lại.

---

## Còn lại một quan sát — và cố ý KHÔNG gọi là phát hiện

MN chốt sớm hơn hạn **10h25m** trong khi MT/MB chốt sát hạn (13 và 22 phút). Giả thuyết «lỡ bộ
học» đã bị bác, nhưng **câu hỏi gốc chưa được trả lời**: chốt sớm 10 tiếng có mất gì không?

Mở `FU-405` để đo. **Không** viết nó thành phát hiện — chưa có số nào nói nó có hại.

---

## Trạng thái cuối

Production **không đổi** — bản này **read-only**, không sửa dòng mã nào, không ghi DB.

**Hai cổng đỏ, cả hai đỏ ĐÚNG, và cả hai chờ CHỮ KÝ OWNER chứ không chờ agent làm thêm việc:**
`_v11062` vì `V11080b` (không có bản ghi gốc, cấm tự bù) · `_v10981` K8 vì `QD-021` và `QD-066`
ngược nhau cùng `ACTIVE`.

**Gấp nhất:** `FU-348` hạn **HÔM NAY** — hạ `MO_COI_TRAN` 15 → 2, và hiện **đang rẻ** vì mồ côi
đúng bằng 2.

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11084.md` — quan trọng nhất là ② **dấu lợi thế đổi theo
cửa sổ** (cấm trích riêng 30 ngày) và ③ **hai giả thuyết đã bị bác, đừng đo lại**.
