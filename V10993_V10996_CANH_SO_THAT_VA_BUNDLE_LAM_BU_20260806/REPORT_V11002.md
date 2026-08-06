# REPORT V11002 — Làm rõ M1 · đo bộ đào luật · bài toán tốc độ phản hồi

> **Ngày:** 2026-08-06 · **Quyết định owner:** QD-038
> **Mã việc:** FU-285 · FU-286 · FU-287
> **Báo cáo gộp cùng V11001:** [`REPORT_V11001_V11002.md`](./REPORT_V11001_V11002.md)

---

## 1. Tóm tắt

Owner nêu ba chuyện agent nói chưa rõ. Đo xong thì **hai trong ba câu hỏi hoá ra không có đáp
án** — không phải vì thiếu dữ liệu, mà vì bản thân câu hỏi dựa trên một giả định sai.

Câu thứ ba — *"1 tháng mới biết thì quá tệ"* — là điều quan trọng nhất cả phiên.

## 2. Owner yêu cầu gì (nguyên văn)

> *"M1 Vẫn chưa hiểu lắm ah em. thôi không huấn luyện tuần khác với huấn luyện tháng và nạp dữ
> liệu samday sau mỗi chu kỳ xổ verify chỗ nào phải làm rõ chỗ này đã. Rồi cơ chế học tập tích
> lũy xếp hạng rules thì sao? Scan theo Miền mỗi miền có số tuần scan khác nhau như thế nào
> phương pháp tốt nhất là gì scan tuần có hiệu quả không và scan tháng nó hiệu quả không?"*

> *"Việc thay đổi cần ghi nhận cập nhật, theo dõi chứ nếu có thay đổi mà 1 tuần hoặc 1 tháng mới
> hành động thì làm sao biết nó có hoạt động hoàn hảo hay không đợi 1 tháng mới biết sau đó fix
> sửa rồi đợi 1 tháng nữa thì quá tệ đó em"*

> *"Rồi cái em đệ nghị ngày mai là lúc nào khi nào bây giờ hệ thống rảnh không bị block mắc gì
> không làm? lý do là gi"*

## 3. Đào bới / phát hiện

### 3.1 M1 — "tuần hay tháng" không có đáp án · `VERIFIED_TEST`

Nhịp thật: **CN 02:00 hằng tuần** (`scheduler.py`) + `_v10646_retrain_guard.py` chạy **06:30
mỗi ngày**, ép huấn luyện nếu model cũ quá **8 ngày** (`THRESHOLD_DAYS = 8`).

93 lần huấn luyện lại có ghi cả AUC mới lẫn cũ:

| | |
|---|---|
| AUC tốt lên | **47/93 = 51%** ← đúng bằng tung đồng xu |
| Chênh trung bình | **+0,00027 AUC** · độ lệch 0,01381 · **z = +0,19** |
| `meta-learning` | 47% tốt lên · +0,00163 |
| `xgboost` | 47% · **−0,00050** |
| `random-forest` | 53% · **−0,00086** |
| AUC hiện tại | 0,4464 – **0,5136** – 0,5623 |

**Việc huấn luyện lại không đổi gì**, nên đổi nhịp là đổi một biến chưa biết có tác dụng.

### 3.2 Samday — không có chỗ verify vì tính năng chưa bật · `VERIFIED_CODE`

`include_same_day=False` cho **tất cả** trong production; chỉ tệp sandbox/shadow mới bật.
**Samday chưa bao giờ được nạp** nên không tồn tại chỗ verify nào.

### 3.3 Bộ đào luật — 2.908 tổ hợp, giữ 105 · `VERIFIED_CODE`

Đếm từ `_seed_rules.py`: mỗi miền 3–5 cấu hình nguồn × 7 thứ × số đài × (giải đơn + cặp giải).

| Miền | Tổ hợp quét |
|---|---|
| MN | 729 |
| MT | 1.081 |
| MB | 1.098 |
| **Tổng** | **2.908** → giữ **105** = **3,61%** = **1/27** |

**Nếu tất cả 2.908 chỉ là nhiễu**, con tốt nhất vẫn có `z ≈ +3,58` — với n=52 và nền ~34%
tương đương tỉ lệ trúng **~58%**. Nên **lift 1,07 trên n=52 nằm gọn trong may rủi**.

### 3.4 "Quét tuần hay tháng" — KHÔNG ĐO ĐƯỢC · `VERIFIED_TEST`

Vòng đầu: `4w +0,629 · 8w +0,805 · 12w +0,939 · 16w` **+0,996**. Con số 0,996 quá đẹp nên phải
kiểm — và nó **vòng tròn**:

| Cửa sổ | Bắt đầu | Dòng đánh giá nằm TRONG cửa sổ |
|---|---|---|
| 4 tuần | 06/07 | 450/3.203 = 14% |
| 8 tuần | 08/06 | 870/3.203 = 27% |
| 12 tuần | 11/05 | 1.290/3.203 = 40% |
| **16 tuần** | 13/04 | **1.710/3.203 = 53%** |

Loại cửa sổ ra → **0 luật** còn ≥10 dòng đánh giá. **Hệ chưa bao giờ chấm luật ngoài chính cửa
sổ đã đào ra nó.**

### 3.5 Tốc độ phản hồi — điều owner nêu · `VERIFIED_TEST`

| Đo ở tầng | Mẫu/ngày | Thấy chênh 5 điểm sau |
|---|---|---|
| Bundle chính thức | 3 | **~120 ngày** |
| Từng model | 114, bầy đàn ăn 3,8× → ~30 hiệu dụng | **~12 ngày** |
| **Cơ chế** | mỗi lượt gọi | **cùng ngày** |

## 4. Hướng xử lý và vì sao chọn

**Không đổi nhịp huấn luyện.** Thay vào đó **đóng băng một bản đối chứng**: không tốn gì, không
đụng bản đang chạy, và sau 3 tháng trả lời dứt điểm câu *"huấn luyện lại có ích không"* — thay
vì đổi nhịp rồi vẫn không biết.

**Chuyển sang đo cơ chế.** Kết quả trả lời *"có trúng hơn không"* — hàng trăm ngày. Cơ chế trả
lời *"thay đổi có ăn vào không"* — biết ngay hôm sau. Từ nay mọi thay đổi khai báo **hai** phép
đo, thiếu phép đo cơ chế thì không được deploy (FU-287).

## 5. Đã làm gì

Đóng băng **12 tệp model + `DOC.txt`** tại `<VPS_ROOT>/data/models_dong_bang_20260806/` (46 MB).
**Không đổi nhịp tuần, không đụng bản đang chạy** (12 tệp vẫn nguyên).
Thêm `_v11002_kiem_dong_bang.py` — cổng kiểm chạy mỗi phiên.

## 6. Cổng kiểm

`[cong] DONG_BANG=DAT` — bản đối chứng 12 tệp + `DOC.txt` nguyên vẹn, bản đang chạy 12 tệp
không bị đụng. Sổ quyết định **không mục nào trôi**. `J5` **ĐẠT** sau khi thêm FU-287 vào bảng
mốc tải 07/08.

## 7. Vướng vấp

**Suýt báo cáo nhầm:** tương quan `16w +0,996` là **tự so với chính mình**. Phát hiện được vì
con số quá đẹp nên đi kiểm thay vì mừng — đây là lần thứ ba trong tuần một con số đẹp hoá ra
là lỗi phép đo.

**Owner bắt đúng một chỗ agent làm sai:** *"cái em đề nghị ngày mai là lúc nào, bây giờ hệ
thống rảnh mắc gì không làm?"* — **hai trong ba việc làm được ngay**, và agent đã làm ngay
trong phiên. Agent nói "mai" theo thói quen chứ không có ràng buộc nào.

Chỉ **một** việc thật sự phải chờ: đo cơ chế của V11001. Lý do: prompt mới deploy **19:50**,
**sau khi cả ba miền đã sinh số hôm nay** (MN 05:20 · MT 16:43 · MB 17:45) — chưa tồn tại
output nào từ prompt mới để so.

## 8. Gỡ về

Xoá thư mục `data/models_dong_bang_20260806` trên VPS. Không ảnh hưởng gì khác — chỉ là bản sao
chép, không có dữ liệu nào bị ghi đè.

## 9. Theo dõi tiếp

| Mã | Nội dung | Hạn |
|---|---|---|
| **FU-285** | 06/11 chấm bản đóng băng trên 3 tháng dữ liệu mới, so với bản đang chạy. Ngang nhau ⇒ **cắt hẳn huấn luyện lại hằng tuần** | 06/11 |
| **FU-286** | Tách bảng đánh giá luật thành hai cột **trong** / **ngoài** cửa sổ đào. Chỉ cột thứ hai được dùng xếp hạng | 13/08 |
| **FU-287** | Mọi thay đổi khai báo hai phép đo: **cơ chế** (1 ngày) và **kết quả** (N ngày). Thiếu cơ chế ⇒ cổng chặn | 07/08 |

**Con số cần nhớ:** RULES-FIRST thực chất chỉ lái **19%** con số cuối (58/303), **65% rớt ở
`BUNDLE_SKEW`**.
