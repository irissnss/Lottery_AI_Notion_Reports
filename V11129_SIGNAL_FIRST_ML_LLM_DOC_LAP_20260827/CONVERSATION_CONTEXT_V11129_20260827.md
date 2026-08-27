# CONVERSATION CONTEXT — V11129 · 27/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — nguyên văn

Prompt tổng lực lần 42, hiệu lực **27/08/2026 21:32 ICT** · `D-28 SIGNAL_FIRST_GENERATION`:

> *« Mục tiêu cao nhất: Tìm và chứng minh tín hiệu thật ở tầng SINH SỐ. ML phải thuần số học.
> LLM phải thuần ngữ cảnh. »*
>
> *« KHÔNG CÓ SIGNAL THÌ KHÔNG TỐI ƯU RANKING. Có signal mới mở N1/N2/N3 ở shadow. »*
>
> *« K phải được chọn bằng lý do kỹ thuật trước khi đọc outcome. Cấm thay K sau khi thấy kết quả
> để làm đẹp coverage. »*
>
> *« Cấm đọc coverage mà không điều chỉnh theo K. Coverage cao nhưng đúng bằng random expectation
> không phải signal. »*
>
> *« Random pool phải: có seed được ghi trước kết quả; có snapshot/hash; không sinh lại sau khi
> biết kết quả. »*
>
> *« Backtest chỉ dùng: tìm lỗi, ước lượng power, soạn giả thuyết. Cấm dùng retrospective result
> để tự promote. »*
>
> *« Nếu chưa đủ live sample: ghi `INSUFFICIENT_POWER` hoặc `WAIT_LIVE`. Không biến thành thất
> bại. Không biến thành thành công. »*
>
> *« Nếu evidence bác tiền đề, được dừng chỉ thị sai. Phải ghi rõ lý do và chọn hành động an toàn
> hơn. »*
>
> *« Không ghi `RUNTIME_PROVEN` khi mới chỉ `RUNTIME_LOADED`. »*
>
> *« LLM "thuần ngữ cảnh" KHÔNG có nghĩa cấm LLM trả số. Nó có nghĩa: LLM không được nhận sẵn
> shortlist/ranking/FINAL của ML. »*

---

## 2 · Agent làm gì

| GĐ | việc | kết quả |
|---|---|---|
| 0 | preflight | runtime khớp cả V11127 lẫn V11128 · DB tươi 21:50 |
| 7.1 | lượt scorer 20:20 hôm nay | 🟢 **81 bản ghi, 0 trùng** — khớp 81 dòng đã settle |
| 9 | FINAL bất biến | 🟢 payload không đổi, 1 dòng/(ngày,miền), 0 trùng 7 ngày |
| 1 | **khoá hợp đồng đo** | hash `8a163adc…` · **giờ lấy từ máy chủ** 21:56:05 |
| 2/4 | tách pool ML / LLM tại `K=10` | ML 33,33 % · LLM 34,77 % · **ngẫu nhiên 34,25 %** |
| 5 | GO/NO-GO | 🔴 **`NO-GO`** — không nguồn nào qua gate |
| — | tính cỡ mẫu cần | **+3 điểm cần 867 ngày** |
| 3 | dump prompt từ hàm đang serve | `gpt_analyzer.py` · **46 dấu vết phải gỡ** |
| — | phát hành | báo cáo này |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · 🔴 Agent nghi FINAL bị ghi đè, và **đọc nhầm chính dữ liệu của mình**

Thấy `max(id)` của `final_bundles` đổi `778 → 782` và `bundle_version` của MN từ `1 → 2`, agent
nghi FINAL MN bị viết lại sau khoá — tức vi phạm bất biến.

**Sai.** `782` là max **toàn bảng** (do MT/MB được thêm sau), còn id của MN **vẫn là 778**.
`bundle_version 1→2` là settlement ghi trạng thái, và `BT = 61` **không đổi** giữa 13:33 và 22:00.

Nếu không tự kiểm, agent sẽ báo một **vi phạm bất biến không tồn tại** — đúng loại `RM-13`:
nguồn đọc sai thì mọi kết luận sai.

### V2 · 🔴 Con số công suất **lật ngược cách đọc toàn bộ kết quả**

Khoá hợp đồng **trước** khi đo, agent tính ra: với `n=273`, hiệu ứng nhỏ nhất phát hiện được là
**+9,3 điểm** (sau Bonferroni).

Nếu **không** tính con số này trước, kết quả `ML −0,54 · LLM +0,90` sẽ được đọc thành
*«LLM tốt hơn ML»* hoặc *«model vô dụng»*. Cả hai đều **sai**: chênh 1,44 điểm giữa hai nguồn
nằm **sâu bên trong** vùng không phân biệt được.

Đây chính là lý do `RM-03` bắt buộc **tính sức mạnh TRƯỚC**, và `RM-04` cấm đổi
`INSUFFICIENT_POWER` thành *«yếu»*.

### V3 · 🔴 Pool sinh **NGẪU NHIÊN** xếp trên pool ML — và seed đã ghi trước nên không chối được

`34,25 %` vs `33,33 %`. Seed `20260827` được ghi vào hợp đồng **trước khi đo**, hash lại, nên
không thể nói đây là may rủi của một lần bốc thuận lợi.

Nhưng cũng **không** được đọc thành *«ML tệ hơn ngẫu nhiên»* — chênh 0,92 điểm cũng nằm trong
nhiễu.

### V4 · 🔴 ML và LLM **không sinh nổi 10 ứng viên phân biệt**

Đặt `K=10` thì ML chỉ đạt **8,2**, LLM **6,8**. Đây là phát hiện **không** nằm trong giả thuyết
ban đầu: vấn đề không chỉ là *chất lượng* ứng viên mà còn là **độ đa dạng nguồn**.

Điểm tốt: đây là thứ **đo được ngay**, không cần chờ mẫu như phần enrichment.

### V5 · 🔴 Con số prompt trong đề bài và con số đo được **là hai đại lượng khác nhau**

Đề bài nêu *«create_analysis_prompt khoảng 18.200 ký tự»*. Agent đo được **50.741** — nhưng đó là
**độ dài MÃ NGUỒN của hàm**, không phải chuỗi prompt phát ra.

Nếu báo *«prompt dài 50.741, đề bài sai»* thì đó là so hai thứ khác nhau. Agent ghi rõ cả hai và
để phần *«prompt phát ra dài bao nhiêu»* ở nhãn **`NOT_VERIFIED`**, vì chưa emit được (cần ngữ
cảnh DB đầy đủ của một lượt sinh).

### V6 · Lỗi định dạng chuỗi Python khi in số có dấu phẩy

`"%,d"` không hợp lệ trong Python. Xử bằng `format(int(n), ",")`.

---

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| dựng/tối ưu `TOTAL-N1/N2/N3` | 🔴 **`NO-GO`** theo gate đã đăng ký trước — Owner khoá *«không có signal thì không tối ưu ranking»* |
| chuyển đổi prompt sang context-only | `§60.1` cấm nửa vời (46 dấu vết / 38 điểm bơm); chưa emit được prompt thật nên **không quét ngược được**; và mục 5 cho thấy hiệu quả **không kiểm chứng được** dưới 9,3 điểm |
| persist hai namespace shadow ML/LLM | `NO-GO` ⇒ chưa có regime mới để lưu |
| promote hay retire model nào | retrospective **cấm** dùng để promote; và **0** model qua gate |
| đổi `K` sau khi thấy kết quả | cấm tường minh — `K=10` khoá trong hợp đồng có hash |
| sinh lại pool ngẫu nhiên | seed `20260827` ghi trước, dùng đúng một lần |
| nâng scorer lên `RUNTIME_PROVEN` | ba mốc 28/08 **chưa nổ** ⇒ `WAIT_LIVE` |
| ghi vào production DB | mọi truy vấn `-readonly` + chặn từ khoá ghi phía client |
| deploy bất cứ thứ gì | không có thay đổi nào cần deploy trong phiên này |
| CLASS C | chặn ở `RECOVERY_PATH = NOT_VERIFIED` |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| mutation | **KHÔNG CÓ** — phiên đọc và đo |
| production DB | không ghi một dòng |
| prediction · FINAL · M0 · roster · prompt | **KHÔNG ĐỔI** |
| runtime | `main.py` `ec254033…` · `scheduler.py` `a6c8bfff…` — khớp hai deploy trước |
| GO/NO-GO | 🔴 **`NO-GO`** |
| scorer | 20:20 27/08 **ĐẠT** · mốc 28/08 **`WAIT_LIVE`** |
| 3-càng | vẫn `MISSING_PIPELINE / NOT_SCORABLE` |

---

TanPhatAI cần làm: ghi **`NO-GO` cho ranking** kèm `prereg_hash 8a163adc…` và giờ khoá **21:56:05 lấy từ máy chủ**. Ghi bốn con số cạnh nhau: **ML 33,33 % · LLM 34,77 % · kết hợp 34,13 % · pool NGẪU NHIÊN 34,25 % · nền 33,87 %**. **Đừng** đọc thành *«LLM hơn ML»* hay *«model vô dụng»* — ngưỡng phát hiện **+9,3 điểm**, mọi chênh đều **dưới 1,5 điểm** ⇒ **`INSUFFICIENT_POWER`**. Ghi con số định hình chương trình: **+3 điểm cần 867 ngày**. Ghi phát hiện mới: **ML chỉ sinh 8,2 và LLM 6,8 ứng viên phân biệt**, không đạt `K=10` — đây là vấn đề **đo được ngay**. Ghi **scorer 20:20 hôm nay ĐẠT (81/81, 0 trùng)**, mốc 28/08 **`WAIT_LIVE`**. Ghi **46 dấu vết prompt phải gỡ**, và **chuyển đổi cố ý chưa làm**. **Phiên này không mutation gì cả.**
