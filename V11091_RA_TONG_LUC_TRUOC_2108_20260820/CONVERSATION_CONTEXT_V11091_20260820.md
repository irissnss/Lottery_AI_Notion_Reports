# CONVERSATION CONTEXT — V11091 · 20/08/2026 · rà tổng lực trước ngày mở gói

## Owner nói gì (NGUYÊN VĂN)

> *«Đã xem kỹ tổng lực toàn bộ chưa? lâu quá nên nhiều cái nó mơ hồ, không rõ ràng và có thể rơi
> rớt em cần xem kỹ dùm anh lại 1 lần nữa nha em»*

---

## Câu trả lời thật là: **chưa**

Các phiên trước soi **từng việc được giao** — GĐ-0 tới GĐ-5, rồi bốn quyết định, rồi hai ngưỡng.
Mỗi phiên làm xong việc của nó. Nhưng **không phiên nào rà ngang** để hỏi *«14 mục gói ngày mai
có thật sự chạy được không?»*

Owner hỏi đúng chỗ. Rà ngang ra ngay hai thứ sẽ làm hỏng ngày mai.

---

## Phát hiện 1 — bốn mục sẽ chạy mai mà **không ai canh**

Rà đủ 14 mục × trạng thái trong sổ theo dõi:

```
#2   D2             KHÔNG có mã theo dõi
#3   D3             KHÔNG có mã theo dõi
#8   FU-290A        KHÔNG có mã theo dõi
#12  latency_score  KHÔNG có mã theo dõi
```

Nghĩa là bốn mục này **không có trạng thái, không có điểm gỡ về ghi trong sổ, không ai canh**.
Chúng nằm trong bảng gói như 10 mục kia — nhìn thì y hệt.

Và khi truy đích thật của từng mục thì lộ thêm: **`FU-290A` chỉ là một NHÃN**. Nó xuất hiện
trong văn xuôi (`SSOT:761` — *«FU-290A HOÃN tới 21/08»*) nhưng **không có nội dung thiết kế nào**.
`§59` đòi trả lời **ba câu** trước khi trình một đề xuất cắt model — **chưa câu nào** được trả lời.

---

## Phát hiện 2 — `D3` chưa đủ để chạy, và nó sắp lặp lại đúng lỗi cũ

`D3` mô tả gọn: *«gỡ `RR §11` + `§18`»*. Nghe như một việc dứt khoát.

Đọc kỹ hai mục đó thì cả hai **đều dạy model dùng khối `🎯 RULE TAILS`**:

```
§11  🔥STRONG (≥3 rules): CẦN xem xét nghiêm túc, nên có trong top-2
     ⚡MED (2 rules): tham khảo tốt
     💡LIGHT (1 rule): chỉ tham khảo, KHÔNG đủ để chọn đơn lẻ
     KHÔNG tự tạo số mới nếu Rule Tails đã có gợi ý mạnh

§18  Nếu Rule Tails có 🔥STRONG suggestion → dùng nó, đừng bịa số mới
```

Rồi kiểm khối dữ liệu: **nó vẫn được bơm**, `gpt_analyzer.py:4836`, **không có cổng shadow nào**.

Và bốn mục khác vẫn trỏ tới nó: `§9` (cross-region → tín hiệu MẠNH) · `§10` (tails từ ĐB/G1 tin
hơn) · `§20` (đếm rule tails để xếp PRIMARY) · `§25` (định nghĩa `near_miss_shortlist`).

**Chỗ nặng nhất:** khối phát ra đúng ba nhãn `🔥STRONG` / `⚡MED` / `💡LIGHT`, và **`§11` là nơi
duy nhất giải nghĩa chúng**. Gỡ `§11` thì model nhận ba nhãn **không có định nghĩa** — nó sẽ tự
đoán nghĩa.

Và `§18` là **rào chắn chống bịa số**. Gỡ rào mà **giữ nguyên** khối dữ liệu là bỏ phanh mà giữ
nguyên dốc.

Đây **đúng vết `§60.1`**: V11001 gỡ 8 khối gan/nóng/lạnh rồi báo xong, hôm sau quét lại còn
**10 chỗ** vẫn dạy model dùng thứ vừa gỡ. Cùng một lỗi, **sắp lặp lại**, và lần này biết trước.

---

## Ba lần suýt báo động giả — và vì sao chúng đáng kể hơn cả hai phát hiện trên

Trong lúc rà, có **ba** con số/kết quả trông như phát hiện lớn. Cả ba **sai**, và cả ba tự bắt
được **trước khi trình owner**.

### (a) *«`RR §11`/`§18` KHÔNG TỒN TẠI»*

`grep "§11"` trong `gpt_analyzer.py` và `prompt_registry.py` ra **rỗng**. Các `§` tìm thấy là
`§5 §10 §24 §25 §26 §60` — không có 11, không có 18.

Kết luận hiển nhiên: *«đích của `D3` không tồn tại, mục này vô nghĩa»*. Rất muốn báo ngay.

Đào thêm một bước thì rulebook đánh số **`### 11.`**, không phải chuỗi `§11`. **Chúng tồn tại,**
ở dòng 593 và 635.

Nếu báo ngay thì owner đã đi kiểm hộ một cảnh báo sai — và tệ hơn, có thể đã bỏ `D3` khỏi gói vì
tưởng nó vô nghĩa.

### (b) *«`_v11044` cũng dính lỗi hậu tố»*

Sau khi vá `_v11062` (V11087), việc đúng theo `RM-07` là hỏi *«còn cổng nào cùng họ lỗi?»*.
Kiểm ba cổng: `_v10921` **có** luật lọc hậu tố, `_v11062` **có**, `_v11044` **không có**.

Trông như tìm thấy cái thứ ba. Nhưng đọc mã thì `_v11044` chỉ lưu **phần số**
(`V.add(int(m.group(1)))`) ⇒ `V11080b` → `11080`, tập hợp **tự gộp**.

**Miễn nhiễm theo thiết kế.** Không phải may — nó không bao giờ giữ hậu tố để mà sai.

### (c) *«287/554 tệp khai READ-ONLY mà có ghi»*

Đây là con số đáng sợ nhất, và là con số **sai nguy hiểm nhất**.

Nó **đúng về số học**. Nhưng trong danh sách có `_v11088_cuu_ban_sao.py` — **tệp của chính phiên
trước**, và nó ghi rõ ngay trong docstring: *«chỉ **đọc** kho và chỉ **ghi** vào
`artifacts/v11087_ban_va/`»*. Nó **không nói dối** gì cả.

Đúng bẫy `RM-09`: **cấm đếm chuỗi thô**. Khuyết tật `_v11057` thật là **khai READ-ONLY + ghi đè
artifact bằng tên CỐ ĐỊNH** — chứ không phải «có bất kỳ lệnh ghi nào».

Lọc đúng điều kiện đó (và loại tệp có dấu thời gian — vì dấu thời gian chính là cách `V11079` đã
sửa): **0 tệp**.

**Món nợ `RM-07` giờ đã trả, và kết quả là sạch.**

---

## Điểm chung của ba ca

Cả ba con số đầu tiên đều **đúng** và đều **dẫn tới kết luận sai**.

Thứ cứu được không phải là cẩn thận chung chung, mà là **một câu hỏi cụ thể**:
*«con số này thật sự đang đếm cái gì?»*

- `grep "§11"` đếm **chuỗi `§11`**, không đếm **mục số 11**.
- «không có luật lọc hậu tố» đếm **sự vắng mặt của một đoạn mã**, không đếm **hành vi sai**.
- `287/554` đếm **tệp có lệnh ghi**, không đếm **tệp nói dối**.

---

## Năm món nợ chưa làm — đo bằng máy, không nhớ theo cảm giác

```
✗  cổng máy cho lớp lỗi ">/dev/null" che stderr    (tái phạm 3 lần — quá ngưỡng §61)
✗  cổng RM-19 so cả cặp KHÁC chủ đề                (_v11034 đang báo SẠCH SAI)
✗  bộ đọc nhận nhãn "| **hạn** |" dạng ô bảng      (đang đọc nhầm ngày ít nhất 1 mục)
✗  FU-407 đo lo3/xien cùng khuôn
✗  bộ chấm T-B lên VPS                             (vùng cấm deploy)
```

Món gấp nhất là **cổng `RM-19`** — nó đang **báo `SẠCH` sai**, tức đang cho cảm giác an toàn giả.

---

## Trạng thái cuối phiên

Production **không đổi**. `QD-041` nguyên vẹn tới 21/08. Cổng đầy đủ xanh.

Đã khai **`FU-410`** ghi đủ bốn mục thiếu mã + cảnh báo `D3` + ba lối A/B/C — để mai không ai
phải nhớ lại từ đầu.

**Không thêm mục nào vào gói** — `QD-064` khoá *«không thêm không bớt»*, và bốn mục kia **đã nằm
trong gói**, chỉ là thiếu khối theo dõi.

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11091.md` — quan trọng nhất là ① **`D3` chọn lối
A/B/C** (khuyến nghị **C: hoãn**), ② **`FU-290A` chưa có nội dung**, ③ **ký hai ngưỡng**.
