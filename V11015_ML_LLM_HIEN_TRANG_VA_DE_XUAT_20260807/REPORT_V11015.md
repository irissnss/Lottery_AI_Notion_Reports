# REPORT V11015 — ML và LLM: hiện trạng, chỗ thiếu, và đề xuất xử lý

> **Ngày:** 2026-08-07 · **READ-ONLY** — không mutation, không deploy
> **Dữ liệu:** đồng bộ `07/08 00:31` · script đo commit kèm tại `scripts/`

---

## 1. Tóm tắt

Owner hỏi: *"ML và LLM đã làm được gì rồi? hiện tại và tương lai đề xuất là gì… Em làm được gì
và cần gì phải rõ ràng"*.

Soi hai tầng thì ra **bốn chỗ thiếu so với đúng thiết kế owner đã nêu**, trong đó có **một chỗ
mâu thuẫn nội bộ chưa ai phát hiện**: prompt LLM đã gỡ sạch gan/nóng/lạnh, nhưng **ML vẫn còn
6 đặc trưng gan/hot/cold**. Hai tầng đang chạy theo hai niềm tin trái ngược nhau.

## 2. Owner yêu cầu gì (nguyên văn)

> *"ML và LLM đã làm được gì rồi? hiện tại và tương lại đề xuất là gì."*

> *"Với ML ngoài xác xuất thống kê thuần, anh quan tâm đến **đối chứng với rules, bộ lọc** để so
> sánh đối chiếu để output **số chính và nhẹ hơn là số phụ**, với ML cắt retrain tuần thì retrain
> sẽ học lại ở thời điểm nào? làm sao **kiểm soát** nếu sau 1 tháng hoặc 3 tháng mới retrain thì
> làm sao biết nó có hoạt động."*

> *"Với LLM ngoài ngữ cảnh có sẵn, các số học được nhồi nhét cần **biến thành ngữ cảnh thực sự**
> để model đọc hiểu tự phân tích, tự tư duy tự tra soát trong **ngưỡng tự quyết định** output số
> tốt nhất ở số chính và nhẹ hơn là số phụ, tất cả tự nhiên có quy luật có điều kiện, **đừng
> output theo số gò** như thế dẫn đến bầy đàn là đúng rồi, lùa vào 1 bộ số định sẵn trong ngày để
> model quyết định xong thấy bầy đàn."*

> *"==> Em làm được gì và cần gì phải rõ ràng"*

## 3. Đào bới / phát hiện

### 3.1 ML — bốn sự thật · `VERIFIED_CODE` + `VERIFIED_TEST`

| | |
|---|---|
| **39 đặc trưng**, tất cả dẫn xuất từ **số đã ra** | tần suất(5) · gan/vùng(6) · xu hướng(3) · hội tụ(1) · xếp hạng(5) · thứ(2) · lag(5) · chéo miền(1) |
| **0/34 model hơn nền** sau Bonferroni | AUC dao động **0,48–0,56** qua **228 lượt** học lại |
| **KHÔNG đối chứng rules, KHÔNG qua bộ lọc** | 7/7 tệp ML: `mined_rule = 0` · `bộ_lọc = 0` |
| **KHÔNG tự phân biệt chính / phụ** | `secondary` · `top1` · `top2` = **0 lần** trong `ml_predict.py`; ML trả về **danh sách xếp hạng**, tầng gộp bundle mới chọn |

### 3.2 PHÁT HIỆN MỚI — ML và LLM chạy theo hai niềm tin trái ngược · `VERIFIED_CODE`

| tầng | gan / nóng / lạnh |
|---|---|
| **LLM prompt** | **đã gỡ hết** (V11001 + V11007) — còn đúng 1 câu cảnh báo |
| **ML đặc trưng** | **vẫn còn 6**: `gan_score_w` · `gan_days` · `gan_vs_avg` · `zone_encoded` · `freq_x_gan` · `trend_x_zone` |

Owner nói *"gan, cold, hot chả tích sự gì"* và agent đã gỡ khỏi prompt — **nhưng quên ML**.

### 3.3 Nhịp huấn luyện lại và cách kiểm soát hiện có · `VERIFIED_CODE`

| | |
|---|---|
| Lịch | `retrain_day = 'sun'` · `retrain_time = '02:00'` |
| Chốt chặn | `_v10646_retrain_guard.THRESHOLD_DAYS = 8` — ép học nếu model cũ quá 8 ngày |
| Lần gần nhất | **02/08** · 4 model, mỗi model 57 lượt |
| Kiểm soát hiện có | **chỉ có lịch và chốt chặn tuổi model** — không có phép nào đo *"model còn khớp dữ liệu không"* |

### 3.4 LLM — đã làm và chưa làm · `VERIFIED_TEST`

**Đã làm (V11014, 07/08):** mệnh lệnh **23→18** · cặp khối trùng **5→3** · cả ba miền
`ép_chọn = False`.

**Chưa làm — chính là ý cốt lõi của owner.** Agent mới **bỏ mệnh lệnh**, còn **số vẫn là số**:

```
Các luật của bucket MB/Thứ Sáu hôm nay trỏ tới 10 đuôi: 13 31 32 35 60 69 84 88 89 95
  • Hà Nội G6+G7 (D-1): 13 35 69 84 88 89 95
```

Vẫn là **một rổ số dọn sẵn**, chỉ khác là không bắt buộc. Model đọc xong vẫn thấy danh sách ⇒
**vẫn dễ bầy đàn**, đúng như owner nói *"lùa vào 1 bộ số định sẵn trong ngày để model quyết định
xong thấy bầy đàn"*.

## 4. Hướng xử lý và vì sao chọn

### Bốn việc cho ML

| mã | việc | vì sao |
|---|---|---|
| **M-A** | **Tầng đối chứng ML × rules × bộ lọc** — bảng so ba nguồn mỗi ngày. Ba nguồn cùng chỉ một số ⇒ ứng viên **số chính**; chỉ một nguồn ⇒ cùng lắm **số phụ** | Chính là thứ owner hỏi. Đo **shadow**, không đụng số official ⇒ làm được ngay |
| **M-B** | **Chính/phụ theo BIÊN, không theo thứ hạng** — số chính chỉ chốt khi biên xác suất hạng 1 vs hạng 2 vượt ngưỡng; biên hẹp ⇒ **chỉ ra một số** | Đúng ý *"số chính và nhẹ hơn là số phụ"*. Hiện ML đưa top-1/top-2 mà **không nói cách nhau bao nhiêu** |
| **M-C** | **Học lại theo TRÔI, không theo lịch** — ba lớp kiểm soát | Trả lời trực tiếp câu hỏi owner về kiểm soát |
| **M-D** | **Bỏ 6 đặc trưng gan/hot/cold khỏi ML** | Cho ML nhất quán với prompt |

**M-C chi tiết — ba lớp trả lời câu *"1 tháng mới retrain thì làm sao biết nó hoạt động"*:**

| lớp | nhịp | trả lời câu gì |
|---|---|---|
| **Canh trôi đặc trưng** | **hằng ngày** | phân bố đầu vào có lệch khỏi lúc huấn luyện không ⇒ **kích hoạt học lại khi cần**, không đợi lịch |
| **Diễn tập đường huấn luyện** | **hằng ngày** | code huấn luyện còn chạy được không (đã có — DT-01) |
| **Bản đóng băng đối chứng** | **hằng tháng** 07/09 · 07/10 · 07/11 | học lại có ích thật không (FU-285) |

⇒ **Không bao giờ phải chờ một tháng mới biết.** Biết trong **1 ngày** rằng cơ chế còn sống, và
**hằng tháng** rằng nó có tác dụng.

### Ba việc cho LLM

| mã | việc |
|---|---|
| **L-A** | **Đổi số thành lời kể có nguồn gốc.** Thay danh sách bằng câu chuyện dữ liệu: *"Hôm qua thứ Năm, Hà Nội ra giải 6 đuôi 35, giải 7 đuôi 69. Trong 6 tuần qua cặp G6+G7 của Hà Nội vào thứ Sáu MB trúng 6/6 — nhưng toàn bộ 6 lần đều chấm ngược, chưa lần nào đo tiến."* Model đọc **sự kiện + bối cảnh + độ tin**, tự rút số ⇒ **cắt gốc bầy đàn** |
| **L-B** | **Ngưỡng tự quyết** — bắt model tự khai mức tin trước khi chốt; dưới ngưỡng thì **chỉ ra một số chính, không ra phụ** |
| **L-C** | **Gỡ nốt hai khối nhồi số** — `EVIDENCE TABLE` (1.549) · `OWNER ANTI-TRAP CHECK` (1.550), chuyển sang dạng kể như L-A |

## 5. Đã làm gì

**Không sửa gì.** Chỉ đọc mã nguồn và truy vấn read-only. Viết 1 script đo mới
(`ml_llm_hientrang.py`), commit kèm báo cáo theo E4.

## 6. Cổng kiểm

| | |
|---|---|
| Tuổi dữ liệu | đồng bộ `07/08 00:31` |
| 4 bảng khoá | **không đụng** — chỉ `SELECT`, mở `mode=ro` |
| Đếm đặc trưng ML | `FEATURE_COLUMNS` — **39** |
| Đếm tham chiếu rules trong ML | 7/7 tệp = **0** |
| Lịch sử huấn luyện | **228 lượt** · 4 model × 57 |

## 7. Vướng vấp

**Agent gỡ gan khỏi prompt mà quên ML.** V11001 và V11007 làm rất kỹ ở tầng LLM — quét ngược,
phân loại, cổng kiểm — nhưng **chưa hề soi tầng ML**. Đúng lỗi **§60.2 câu 1**: *"ai còn trỏ tới
thứ này?"* — soi thiếu một tầng.

**Và agent mới làm nửa việc LLM.** Bỏ mệnh lệnh là cần nhưng chưa đủ: chừng nào prompt còn đưa
một **rổ số dọn sẵn** thì model vẫn bị neo vào đó. Owner nói đúng bản chất — *"lùa vào 1 bộ số
định sẵn trong ngày để model quyết định xong thấy bầy đàn"*.

## 8. Gỡ về

Không có gì để gỡ — READ-ONLY.

## 9. Theo dõi tiếp

| Mã | Nội dung | Trạng thái | Hạn |
|---|---|---|---|
| **FU-317** | **M-A** — tầng đối chứng ML × rules × bộ lọc, đo shadow | agent làm được **ngay**, không cần owner | 10/08 |
| **FU-318** | **M-C** — canh trôi đặc trưng hằng ngày, kích hoạt học lại theo trôi thay vì theo lịch | agent làm được **ngay** | 11/08 |
| **FU-319** | **M-B** — chính/phụ theo BIÊN | **chờ owner** — đổi cách chọn số | 14/08 |
| **FU-320** | **M-D** — bỏ 6 đặc trưng gan/hot/cold khỏi ML | **chờ owner** — đổi đặc trưng ⇒ phải huấn luyện lại | 14/08 |
| **FU-321** | **L-A** — đổi số thành lời kể có nguồn gốc | **CHỜ OWNER QUYẾT: làm ngay hay chờ 21/08?** | anh chốt |
| **FU-322** | **L-B** — ngưỡng tự quyết | đi cùng L-A | anh chốt |
| **FU-316** | **L-C** — gỡ nốt 2 khối nhồi số | đã mở, sau khi V11014 có ≥7 ngày đo | 14/08 |
| **FU-290** | cắt model theo tốc độ | **chờ owner ký** — §59 bắt nói rõ «bỏ cờ» hay «dừng hẳn» | **08/08** |

**Câu hỏi duy nhất agent cần owner trả lời:** **L-A làm ngay hay chờ 21/08?**
Làm ngay ⇒ đúng ý owner nhưng FU-284 thành đo **gộp ba biến**, hết tách nhân quả.
Chờ 21/08 ⇒ giữ phép đo sạch nhưng đợi thêm 2 tuần.
**Agent nghiêng về làm ngay** — phép đo đã gộp hai biến rồi, thêm biến thứ ba không tệ hơn nhiều,
mà đổi được đúng thứ owner cần.

**Ba con số cần nhớ:** ML **39 đặc trưng · 6 vẫn là gan/hot/cold** · ML đối chứng rules
**0/7 tệp** · prompt vẫn đưa **rổ 10 số dọn sẵn**.
