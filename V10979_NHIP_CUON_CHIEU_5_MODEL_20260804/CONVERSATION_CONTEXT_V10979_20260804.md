# NGỮ CẢNH PHIÊN V10979 — 04/08/2026

Ghi **nguyên văn** lời owner, agent làm gì, và vấp ở đâu. Không diễn giải lại lời owner.

---

## 1. Lời owner trong phiên này

**04/08/2026 09:47 (giờ VN):**

> Mốc thời gian không ổn ah em. Hay Sao đó mà trễ outout block luôn anh đã nói sau khi vào đủ dữ
> liệu và verify tiến hành dự đoán cho đơn model , lần lượt cuốn chiếu với 5 model AI 1 lượt mà
> em. mốc MB chốt 17h58 , mốc miền T 16h58 output cuối cùng xong sớm thì thông báo đã xong block
> thôi em. Kiểm tra toàn diện hệ thóng đầu ngày dùm anh luôn em

*(Vế "kiểm tra toàn diện hệ thống đầu ngày" do phiên V10980 chạy song song xử lý. Phiên này xử
vế nhịp chạy và thông báo xong.)*

---

## 2. Owner đã nói việc này từ trước — nguyên văn cả ba lần

### Lần 1 — trước 27/07 (không tìm được bản gốc)

Owner ngày 27/07 tự ghi *"**trước đó đã xác nhận**"*, nên còn ít nhất một lần sớm hơn nữa nằm
ngoài transcript phiên hiện tại.

### Lần 2 — 27/07/2026 00:48

> Anh thấy nghi nghi vấn rồi , hôm qua bảo /choi cho output đầy đủ các ngày không chặn chỉ kèm
> them cảnh báo , chơi hay không do người dung , output phải đúng với cơ chế của /choi để có thể
> đo lường và so sánh nha em. còn chơi hay không là do người dùng , thế làm làm sao hôm nay không
> hiển thị output MB luôn và còn làm lỗi luôn. Đòng thời xem thời gian output tối đa của mỗi miền
> như sau : MN 15h55 nhưng miền nam đầu ngày thời gian khá dài nên không đến nổi quan ngại, nhưng
> MT 16h55 và MB là 17h55 thời gian quá ngắn, **trước đó đã xác nhận cho các model AI chạy theo
> nhóm 5 model 1 lượt cuốn chiếu hết model này đến model kia và sao anh có cảm giác vẫn muôn ah
> em.** Xem kỹ dùm anh nha . Anh đang nghi hệ thống đang có vấn đề đang làm ảnh hưởng đến kết quả
> dự đoán đến total output ah em. Đơn model hôm qua em đánh giá khá hơn và ngày nào output cũng
> tệ là sao em? ah UI P&L trên model tràn lang không tương thích mobile em đã xem chưa ?

### Lần 3 — 31/07/2026 10:53

> Trong quá trình vừa qua có 1 số điều chỉnh nên mất kiểm soát hay sao đó . - Nếu có same day hay
> không có sameday gì vì trong thời gian qua có 1 số chốt sameday được cắt bỏ ở MT thì phải anh
> không nhớ rõ lắm. ==> thì các model dự đoán của MT được khởi động chạy dự đoán sau khi cào và
> verify kết quả MN , MB được khởi động chạy dự đoán sau khi cào và verify kết quả MN , MT nên em
> ghi là 17h anh thấy có gì đó không đúng rồi. **Và đối với các model đang chọn phương pháp chạy
> 5 model song song 1 lượt cuốn chiếu tuần từ hết model này đến model kia, ưu tiên model được
> đánh giá xếp hạng tốt nhất trước nên kết quả dự đoán total ở các luồng muộn nhất cũng chỉ là
> 17h55 cho MB và 16h55 cho miền T như thế mới kịp thời gian cho ngươi dùng**, còn MN quy trình
> dự đoán đầu ngày cũng tương tự như có khá nhiều thời gian hơn nên anh không đề cập em tự xem
> lại. **Tất cả show list ra để anh xem lại đi anh thấy không đúng , không ổn rồi đó nha.** - Câu
> 3 trùng là do số của đơn model + phương pháp toán học , tổng hợp bên trong nó, việc trùng có cơ
> sở có lý do không bàn nhưng nếu trùng mà do bốc qua gắn vô 1 cách vô thức thì chịu em luôn. -
> Còn khá nhiều thời gian em nên audit , show ra báo cáo lại hoặc phát hiện các vấn đề nào chưa tư
> duy logic hợp lý thì xử lý ngay luôn đi. Với cần xem thêm tài liệu notion lại thử xem có mâu
> thuẫn chỗ nào không?

**Nguồn:** transcript phiên `eeb49d3c-16d5-440b-9e2e-df1485c7bdf9`, dòng 3514 · 5202 · 6603.

---

## 3. Vì sao việc này trôi bốn lần — nói thẳng

Lời owner ngày 31/07 **có được ghi lại**, nhưng ghi vào **docstring của một script đo**
(`web/backend/_v10889_timing_list.py`):

```
Owner 31/07 10:53 nêu đúng thiết kế của hệ:
  · MT chỉ khởi động dự đoán SAU khi cào và verify xong kết quả MN
  · MB chỉ khởi động SAU khi cào và verify xong MN và MT
  · Model chạy 5 con song song, cuốn chiếu, ưu tiên model xếp hạng tốt trước
  · Nên total muộn nhất phải là 16:55 cho MT và 17:55 cho MB
```

Docstring **không phải cổng kiểm**. Nó không nằm trong `docs/OWNER_DECISION_LEDGER.json`, không
có mệnh đề nào máy chạy được, không có mục theo dõi nào trỏ tới. Nên không có gì canh, và owner
phải nhắc lại lần thứ tư.

Đây đúng thứ owner đã ký thành quy tắc §56 ngày 01/08: *"Anh không muốn nhắc tới nhắc lui hoài
những vấn đề mà em có thể tra ra, có thể kiểm soát được đâu?"*

Nay đã vào sổ thành **QD-020** với **8 mệnh đề máy kiểm được**, chạy mỗi lần
`_v10920_decision_ledger.py` chạy.

---

## 4. Agent làm gì trong phiên

| thứ tự | việc |
|---|---|
| 1 | Chạy `_v10920_session_start.py` — 0 mục quá hạn |
| 2 | Tra 6 nguồn theo §56 (sổ quyết định · roadmap · FU tracker · transcript · playbook · 2 tài liệu cơ chế) → tìm ra 3 lần owner đã nói |
| 3 | Đo VPS 30 ngày: bể cuốn chiếu, biên trước hạn, đường găng từng model, thời gian verify → gọi model |
| 4 | Phát hiện `/monitoring` bị cắt cụt 53,5% từ 03/08 → vá bằng nối mỏ neo |
| 5 | Dựng `_v10979_early_block.py` + 3 phép tự kiểm + API + panel |
| 6 | Ghi QD-020 vào sổ · ghép 3 tài liệu quản trị · cập nhật playbook §1/§5 |
| 7 | Deploy 2 lần (lần 2 vì phát hiện 2 lỗ hổng khi kiểm sau deploy) · kiểm hash · kiểm live |
| 8 | Viết báo cáo công khai |

---

## 5. Vấp ở đâu — ghi đủ, kể cả vấp do chính agent gây ra

**5.1 Bẫy múi giờ, suýt báo cáo sai toàn bộ.** Lần đo đầu dùng `time(p.created_at)` của SQLite,
ra kết quả vô lý (MB "chạy 10:30, chốt 18:31", cả ba miền "trễ hạn 30–50 phút"). Nguyên nhân:
`predictions.created_at` lưu ISO **có đuôi `+07:00`**, `time()` gặp đuôi đó thì tự quy về UTC,
lệch 7 tiếng. Phải dùng `substr(created_at, 12, 8)`.
Đây đúng cái bẫy quy tắc §55 đã cảnh báo — vẫn sập.
**Phát hiện kèm:** script cũ `_v10935_slack.py` dùng đúng công thức sai đó, nên mọi kết luận
"dư bao nhiêu phút" từ script ấy đều lệch 7 tiếng.

**5.2 Chọn nhầm cột mốc chốt.** Ban đầu lấy `final_bundles.updated_at`, nhưng cột này bị job
chấm điểm sau khi xổ ghi đè (MB `18:31:02` = đúng giây cào kết quả). Mốc chốt thật là `created_at`.

**5.3 Mệnh đề máy kiểm TRÔI hết vì dùng builtin.** Viết `__import__(...)`, `open(...)`, `any(...)`
trong khi bộ kiểm chạy `eval(..., {"__builtins__": {}}, vars(module))`. Bốn phép trôi.
**Vấp này V10977 đã ghi lại ngày 03/08 và vẫn lặp lại hôm nay.** Đã viết lại chỉ dùng tên có sẵn
trong module, và đổi sang chạy thật trên dữ liệu thật.

**5.4 Thiếu khoá `trang_thai` trong mục QD-020** → `sinh_md()` ném `KeyError`, không sinh được
bản đọc cho người. Nếu không để ý thì bản `.md` đứng im ở nội dung cũ mà vẫn trông như vừa cập nhật.

**5.5 Đâm số hiệu FU với phiên V10980 chạy song song.** V10980 chiếm FU-258/259 trước; đã dời
sang FU-260/261/262 và sửa lại các chỗ đã ghi nhầm. Phép kiểm "đã ghi chưa" cũng báo nhầm vì tìm
chuỗi `"V10979"` trơn, mà khối của V10980 có nhắc tên V10979 — đã đổi sang mốc nhận dạng riêng.

**5.6 Một lượt đo tay suýt bịt mất lượt thật.** Bản đầu chỉ cần thấy `DA_XONG_BLOCK` là bỏ qua,
nên một lượt `--no-lane` sẽ ghi trạng thái cuối và chặn luôn lượt cron thật sau đó. Bắt được khi
kiểm sau deploy, đã sửa và deploy lại.

**5.7 Suýt tự vi phạm quy tắc đóng băng.** Cron MB chạy cả giờ 17; nếu official chốt muộn thì
lượt sau 17:58 sẽ gọi lane và sinh số bù **sau mốc FINAL** — đúng thứ OD-20260803-B cấm. Đã thêm
rào chắn `_con_kip_goi_lane()`.

**5.8 (không do phiên này gây ra) `/monitoring` hỏng hai ngày.** Commit `9430141` của V10977
(03/08 19:21) ghi file xuống đúng 262.144 byte = 2^18, mất 53,5%. Mất luôn vòng `setInterval(60s)`.
18 phép tự kiểm vẫn xanh suốt hai ngày vì không phép nào kiểm tính toàn vẹn file giao diện.

---

## 6. Cái gì KHÔNG làm, và vì sao

Owner nói *"thông báo đã xong **block** thôi em"*. Phần **thông báo** đã làm. Phần **block** thì
chưa, và phải nói rõ vì sao:

Đo được mọi ngày đã hoàn tất đều kết thúc ở `bundle_version >= 2`, tức bundle **có bị dựng lại**
sau lần tạo đầu — job T-chốt (MT 16:55 · MB 17:55) gọi `generate_final_bundle()`, tức **có quyền
đổi số**. FU-207 ghi nhận một lần dựng lại đã kéo `model_count` từ 15 xuống 14.

Muốn "xong = khoá" thì phải cho T-chốt bỏ lượt và cho `is_frozen()` nghe theo sự kiện. **Cả hai
chạm writer `final_bundles`** — nằm trong vùng **QD-014 đóng băng tới hết 08/08**.

Rủi ro nếu làm ẩu: dò "đủ" sai một nhịp là khoá sớm và **mất model thật khỏi bundle** — đúng loại
lỗi đổi số công bố mà đóng băng sinh ra để chặn.

Nên **không tự làm**. Đã ghi thành **FU-261**, trình owner ngay sau 08/08.
