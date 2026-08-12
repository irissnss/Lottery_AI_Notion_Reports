# CONVERSATION CONTEXT — V11065 (FU-400) · 12/08/2026

## Owner nói gì (NGUYÊN VĂN)

Sáng:

> *«Đầu ngày em kiểm tra phân tích đánh giá trước live dùm anh nhé»*

Tối, sau khi hết chu kỳ:

> *«Đã hết chu kỳ live em tiến hành phân tích toàn lực, đánh giá nhận xét dự đoán hôm nay và các
> cơ chế, phương pháp đo lường, đề xuất xử lý tất cả thật tổng lực cực gắt nha em cấm rơi rụng,
> gián đoạn, ngắt quãng mọi thứ phải liền mạch, tương quan tương thích, tương ứng phù hợp tuyệt
> đối nha em»*

---

## Ngày hôm nay: 3/3 — và vì sao đó là lúc nguy hiểm nhất

MN `61` · MT `82` · MB `73`. **Cả ba trúng.** Vận hành sạch tuyệt đối.

Đây chính là lúc dễ viết một báo cáo sai nhất. Nên con số đầu tiên agent tính không phải *"3/3"*
mà là **nền**:

```
nền đúng hôm nay      0,42 + 0,30 + 0,22 = 0,94 lượt kỳ vọng
xác suất cả ba trúng  0,42 × 0,30 × 0,22 = 2,8%  =  1 ngày trong 36
trên 166 ngày         kỳ vọng ~4,6 ngày như vậy HOÀN TOÀN DO MAY
```

**n = 3 ⇒ `RM-04`: chưa được phép kết luận.** Một ngày đẹp không phải bằng chứng, y như một ngày
xấu không phải bằng chứng.

---

## Thứ hôm nay lộ ra, và nó lớn hơn kết quả ngày

Khâu chọn:

| miền | BT ở hạng | luật thô «nhiều phiếu nhất» |
|---|---|---|
| MN | **#1** | `61` — cùng số, cùng trúng |
| MT | **#1** | `82` — cùng số, cùng trúng |
| **MB** | **#4** (4 phiếu) | `91` (9 phiếu) — **sẽ trượt** ⇒ **trọng số CỨU** |

Và đặt cạnh hai ngày trước thì thành một bức tranh khó chịu:

| ngày | trọng số làm gì | kết quả |
|---|---|---|
| 10/08 MT | bỏ `19` (trúng) chọn `28` | **HẠI** |
| 11/08 MT | bỏ `82` (trúng) chọn `37` (cũng trúng) | **trung tính** |
| 12/08 MB | bỏ `91` (hạng #1) chọn `73` (hạng #4) | **CỨU** |

**Ba ngày, ba kết luận ngược nhau về cùng một cơ chế.** Mỗi lần agent đều bị cám dỗ kết luận từ
một ngày. Cả ba lần đều sai về mặt bằng chứng.

Nên câu hỏi thật không phải *"hôm nay trọng số làm gì"* mà **"trên toàn bộ lịch sử, trọng số có
hơn luật thô không?"** — và câu đó **chưa ai đo bao giờ**.

---

## `FU-400` — và con số làm agent phải đọc lại hai lần

Ghép cặp McNemar, 437 miền-ngày, cùng ngày cùng pool cùng tập phiếu:

```
A · trọng số (bạch thủ THẬT)   147/437 = 33,6%
B · luật thô «nhiều phiếu»     159/437 = 36,4%
nền ngẫu nhiên đúng                      34,4%

A − B = −2,75pp   CI95 [−6,28 … +0,79]   z = −1,456   p = 0,145
A cứu 25 lần · A hại 37 lần · hai luật trùng nhau 64,3%
```

**Toàn bộ máy chấm điểm — trọng số, boost, cổng lọc, cap phiếu — không hơn được phép đếm phiếu
thô.** Và điểm ước lượng **nghiêng về phía luật thô**.

Phải nói cho đúng mức: **CI vẫn trùm 0 ⇒ chưa kết luận được**. Nhưng CI cũng **loại trừ khả năng
trọng số đang giúp quá +0,79pp**. Nói cách khác: nếu trọng số có tác dụng, thì tác dụng đó **nhỏ
hơn 0,8 điểm phần trăm** — trong khi nó là toàn bộ phần phức tạp nhất của hệ.

4/5 cửa sổ đều âm (60d −4,44 · 90d −4,81 · 120d −3,61 · toàn bộ −2,75), chỉ 30 ngày cuối dương
+2,22. Không cửa sổ nào đạt |z|≥1,96 nên **cấm kết luận** — nhưng hình dạng nhất quán.

MB lệch nặng nhất: **A 18,2% vs B 24,1%**, z = −1,65.

---

## Agent tự bắt một lỗ trong CHÍNH phép đo của mình — lệch hơn 3 lần

Bản đầu cho **−0,80pp** trên 498 miền-ngày. Agent suýt viết vào báo cáo.

Rồi hỏi lại một câu: *B đang đếm phiếu của ai?*

`predictions` chứa cả `shadow_auto_eval`. MB ngày 12/08 có **27 model, 11 là shadow** — và chúng
chạy **SAU khi bundle đã chốt**. Chúng **chưa bao giờ có mặt lúc chọn số**.

Nên B không phải *"hệ bỏ trọng số"* mà là *"một pool khác, lớn hơn"*. **So sai đối tượng.**

Thêm hai lớp lọc — bỏ `shadow_auto_eval` **và** chỉ lấy dòng ghi trước giờ chốt:

```
498 miền-ngày  →  437
−0,80pp        →  −2,75pp      lệch hơn BA LẦN
```

Nếu không bắt được, báo cáo này đã công bố một con số sai gấp ba — và nó sẽ thành căn cứ cho
quyết định 21/08.

---

## Thứ agent CHỌN KHÔNG LÀM, dù số liệu nghiêng rõ

Không gỡ trọng số. Ba lý do, mỗi lý do đủ để dừng:

1. **`QD-041` khoá đường chọn số tới 21/08.**
2. **CI vẫn trùm 0.** Hành động trên một kết quả *"chưa được phép kết luận"* chính là cách sáu lần
   *«hứa rồi rữa»* (V10655→V10790) đã xảy ra.
3. **`QĐ-4` khoá phạm vi gói 21/08** — thêm mục là vi phạm chữ ký của owner.

`FU-400` là **bằng chứng cho `FU-290A` đã có sẵn trong gói**, **không phải mục mới**.

---

## Một cổng đang chặn mọi phiên — và nguyên tắc đã có sẵn trong chính tệp đó

Cổng lịch cuốn chiếu báo đỏ. Truy ra: **7 nhãn trạng thái đang dùng thật mà chưa bao giờ được
khai** trong `TREO_STATUSES`/`DONG_STATUSES` ⇒ **15 mục rơi khỏi mọi bộ đếm**.

Đúng gốc bệnh **V10980** từng làm 14 mục biến mất.

Agent định tự quyết cách xếp. Rồi đọc chính tệp đó, dòng 116–118:

> *«NGUYÊN TẮC PHÂN LOẠI: không chắc thì để TREO. Gán nhầm "đã đóng" làm mục BIẾN MẤT khỏi mọi bộ
> đếm — đúng thứ đã gây ra V10980. Gán nhầm "còn treo" chỉ hơi ồn.»*

Luật đã có. Agent chỉ áp nó:

```
mồ côi     15 → 2          (chỉ còn DEPLOYED_LIVE_VERIFIED, cố ý không tự xếp)
còn treo   140 → 153       (+13 mục HIỆN RA)
quá hạn    48 → 48         KHÔNG ĐỔI — không mục nào bị đóng lén
```

`DEPLOYED_LIVE_VERIFIED` để lại cho owner vì **đóng một mục là chiều rủi ro**.

---

## Hai lần suýt sai còn lại

**Sáng nay suýt báo danh sách đến hạn của HÔM QUA.** Tệp `_BRIEFING_DAU_PHIEN.txt` cũ **12,2 giờ**,
ghi ngày 11/08. Nguyên nhân: nó do **hook Cursor** ghi, **không kích hoạt trong Claude Code**. Tức
`CLAUDE.md` bảo Claude Code dựa vào một tệp mà **chỉ Cursor mới sinh lại**.

**Một lệnh treo 600 giây và chuyển nền.** Agent kiểm lại thì bản vá **chưa hề chạy** — `V11065`
xuất hiện **0 lần** trong tệp đích. Làm lại bằng công cụ sửa tệp trực tiếp.

> **Treo ≠ đã chạy.** Phải kiểm **dấu vết**, không suy từ việc lệnh có được gửi đi.

---

## Trạng thái cuối phiên

Production **không đổi** — không deploy, không restart, `QD-041` nguyên vẹn, gói 21/08 **không
thêm không bớt**. Sổ quyết định **0 trôi**.

Lane A/B: **26 cặp / 19 bất đồng** trên ngưỡng 96, nhịp ~10/ngày ⇒ dự kiến **~20/08**.

TanPhatAI cần làm: xem mục cuối `REPORT_V11065.md` — năm việc, quan trọng nhất là ① **cấm ghi
"3/3" trần trụi** (phải kèm nền 0,94/3 và xác suất 2,8%), ③ **cấm gỡ trọng số** dù số nghiêng, và
④ **anti-trap đang co về 0** (+6,4pp → +3,8pp) — đừng ai đọc con số cũ.
