# REPORT V11110 — THẺ CHÍNH `/du-doan` TRỐNG **100%** VỚI NGƯỜI XEM ẨN DANH · 24/08/2026

> **Phiên READ-ONLY** theo lệnh owner (prompt 32). Ngoại lệ duy nhất đã thực hiện ở phiên trước
> và owner ký trực tiếp: gỡ prompt về `V11106`.
>
> **Chín tác nhân đọc-only:** 1,71 triệu token · 585 lượt gọi công cụ · 0 lỗi.
> Bảy làn đo + **hai làn phản biện**; phản biện bác **13 kết luận**, trong đó **một cái lật
> chính bản rút lại của `V11108`**.
>
> **Prompt production đang serve:** `SP-4.4` · `RR-16.5` · `CTX-18.6` · `PB-20.1`.
> Lượt production `05:00` ngày 24/08 **chưa xảy ra** ⇒ `V11106` **`WAIT_LIVE`**.

---

## 1 · TÓM TẮT

| # | điều | số |
|---|---|---|
| 1 | 🔴 **Thẻ chính `/du-doan` TRỐNG với mọi người xem ẩn danh** | **372/372 = 100%** số ngày họ mở được, suốt **77 ngày** |
| 2 | 🔴 **RÚT LẠI lần thứ ba** trên cùng một câu hỏi | *«chưa bao giờ lên trang»* → thật ra *«chưa bao giờ lên **thẻ chính**»* |
| 3 | 🔴 **`−90,3tr` không phải con số cố định** | hai mô hình tiền **đổi dấu**: `−30,9tr` vs `+1,9tr` |
| 4 | **Prompt production thật lớn hơn em từng báo** | **50.241 / 51.636 / 55.926** ký tự, không phải 34k/36k/40k |
| 5 | **Thang mất mát: pipeline không mất gì trước `ranked[0]`** | model→pool→PP1 giữ **98–100%**; sụp toàn bộ ở **một tầng** |
| 6 | **Cổng `PUBLIC_REPORT_SAFETY` chưa từng tồn tại** | đã dựng · thử chặn **11/11** · kho cũ lộ IP/đường dẫn máy chủ |

---

## 2 · OWNER YÊU CẦU GÌ (NGUYÊN VĂN)

> *«PROMPT TỔNG LỰC LẦN 32 — MASTER WORK PACKAGE … PROMPT 31 = VOID»* ·
> *«Cấm tự quyết thay model, bật PP5, tắt lớp ghi đè MN, đổi publish gate hoặc timeout»* ·
> *«Cấm đổi ngưỡng sau khi thấy số»* · *«Giữ nguyên các mốc khoa học 30/09 và 06/11 nếu dữ liệu
> thực sự chưa đủ; cấm "hoàn tất giả"»*.

---

## 3 · ĐÀO BỚI / PHÁT HIỆN

### 3.1 · 🔴 RÚT LẠI LẦN THỨ BA — *«chưa bao giờ lên trang»* là SAI

**Chỗ gốc:** `REPORT_V11108.md` §1b và dòng tóm tắt #9 · mục `V11108` trong `CHANGELOG` và
`SSOT` của kho riêng — **đã công bố, đã đẩy lên remote**.

**Nguyên văn câu sai:**

> *«**Bạch thủ `10` thắng thật, nhưng CHƯA BAO GIỜ lên trang `/du-doan`.** Owner nói «MN không
> có bạch thủ 10» — **owner ĐÚNG**.»*

**Vì sao sai:** em chỉ soi **MỘT endpoint**. Trang gọi **ba** endpoint số.
`/api/final-bundle/history` **KHÔNG có tham số `request`** ⇒ **về mặt vật lý không thể** gọi
hàm đóng băng viewer; thân hàm chỉ đọc lịch sử rồi trả — **không có cổng publish**. Docstring
của chính nó ghi *«No auth required (public-facing, same as /du-doan)»*, và trang **có fetch nó**.

**Đo thật, ẩn danh, trên production — cùng người gọi, cùng ngày, hai endpoint cùng một trang:**

| endpoint | MN 22/08 |
|---|---|
| `/api/final-bundle` — **thẻ chính** | `bundle=None` · `empty=True` · ngày bị kéo về `2026-06-07` |
| `/api/final-bundle/history` — **bảng lịch sử** | **`BT='10'` · `lo2=['10','77']` · `WIN` · `mc=14`** |

⇒ Bạch thủ `10` **CÓ lên trang**, ở bảng lịch sử, **công khai, không cần đăng nhập**.

### 3.2 · Và điều thật sự hỏng thì lớn hơn nhiều — `FU-437`

```
Ngày đóng băng viewer = 2026-06-07 ⇒ cả ba miền 14/15, THIẾU claude-opus-4-6 ⇒ CHẶN
Mọi ngày viewer có thể mở (≤ 07/06):  qua cổng 0  ·  BỊ CHẶN 372  =  100,0%
```

Đo không truyền `date` (đúng cách trang gọi lần đầu):

| thành phần | MN | MT | MB |
|---|---|---|---|
| **thẻ chính** | `bundle=None` · date→`2026-06-07` | `bundle=None` | `bundle=None` |
| **bảng lịch sử ngay bên dưới** | 23/08 `BT=73` | 23/08 `BT=15` **WIN** | 23/08 `BT=54` |

**Trang tự mâu thuẫn với chính nó.** Thẻ chính trống, bảng lịch sử ngay dưới đầy dữ liệu hôm nay.

**Nguyên nhân — HAI quyết định owner đã ký, KHÔNG cái nào sai khi đứng một mình:**

| | |
|---|---|
| **đóng băng viewer** (owner ký 08/06) | người xem ẩn danh bị kéo về `≤ 2026-06-07` |
| **cổng publish 15/15** | áp bằng roster **ĐỌC LÚC PHỤC VỤ** = roster **HÔM NAY** |
| **chồng nhau** | `claude-opus-4-6` vào roster **SAU** 07/06 ⇒ mọi ngày lịch sử 14/15 ⇒ chặn sạch |

Ý định lệnh đóng băng là *«viewer thấy ≤07/06»*. Cổng biến nó thành *«viewer không thấy gì»*.
**Không ai ký điều đó.**

**Ba khuyết tật của cổng publish, đọc từ mã** — mỗi cái đứng riêng đã là lỗi:

| # | khuyết tật | hậu quả |
|---|---|---|
| ① | roster nạp **lúc phục vụ** rồi áp cho **ngày cũ** | **chính production** vi phạm `PRJ-SELECTION-WINDOW-001` mục 1 |
| ② | câu SQL **không có mốc `created_at`** | một dòng về muộn **hôm nay** có thể **MỞ** cổng cho ngày đã qua |
| ③ | `run_source` được `SELECT` nhưng **không dùng để lọc** | dòng shadow/chạy lại vẫn được đếm là output |

**Decision Gate `FU-437` — bốn lối, ⛔ agent KHÔNG tự chọn:**

| lối | được | mất / rủi ro |
|---|---|---|
| **A. giữ nguyên** | không đụng gì | thẻ chính **tiếp tục trống 100%** |
| **B. cổng dùng roster CỦA NGÀY ĐÓ** | sửa đúng gốc ① | phải dựng lịch sử roster; là **đổi hành vi publish** |
| **C. bỏ đóng băng viewer** | hết mâu thuẫn trong trang | **đảo một quyết định owner ký 08/06** |
| **D. thẻ chính rơi về `last-known valid`** kèm nhãn ngày | luôn có gì để xem | người xem thấy số **cũ** mà tưởng mới nếu nhãn không rõ |

⚠️ `B` và `D` **giao với `FU-435`** — phải đọc cùng lúc, đừng quyết hai lần ngược nhau.

### 3.3 · Ba lần rút lại trên cùng một câu hỏi — khuôn chung

| lần | em nói | thật ra |
|---|---|---|
| `V11104` | *«MN 22/08 BT=10 WIN»* | **đúng** — nhưng chỉ ở tầng DB |
| `V11108` | *«bác bỏ ở tầng DB»* → rồi *«owner ĐÚNG, chưa bao giờ lên trang»* | một cái **sai tầng**, một cái **sai vì chỉ soi một endpoint** |
| `V11110` | thẻ chính trống **100%**, bảng lịch sử **có** hiện | *(bản này)* |

**Mỗi lần em đo MỘT LỚP rồi kết luận cho CẢ HỆ.** Nguồn đều đúng; **phạm vi** thì sai.

### 3.4 · 🔴 `−90,3tr` không phải con số duy nhất, và cũng không phải con số của «60 ngày»

Tái lập đúng `−90,3tr` **chỉ ở cửa sổ 61 ngày**; gọi đúng **60 ngày** hôm nay ra **`−89,4tr`** —
hàm dùng **cửa sổ trượt neo vào thời điểm gọi**, nên con số **đổi mỗi ngày**.

**Hai mô hình tiền lệch tới mức ĐỔI DẤU** — cửa sổ 30 ngày:

| mô hình | P&L 30 ngày | nền của **cùng một ván bạc** |
|---|---:|---|
| đánh phẳng | **`−30,9tr`** | `−9,9% … −14,5%` vốn |
| bảng tiền có mức cược `0 / ½ / 1` | **`+1,9tr`** | **đúng `−2,0%`** mọi cửa sổ, mọi miền |

**Nguyên nhân đo được:** mô hình thứ nhất đếm trúng bằng tập hợp ⇒ **tối đa 1 lần/đài**; mô hình
thứ hai đếm **nháy** (lặp). ⇒ **8–12 điểm phần trăm lỗ là HIỆN VẬT CỦA QUY ƯỚC ĐẾM**, không phải
của chiến lược.

**Nhưng nó KHÔNG gỡ được bế tắc `FU-183`:** cách đọc **A** (P&L tuyệt đối) ⇒ **TẮT** dưới **cả
hai** mô hình; cách đọc **B** (chênh so với phiếu bầu) ⇒ **GIỮ** dưới **cả hai**.
**Chọn mô hình tiền không quyết được gì — chỉ chọn CÁCH ĐỌC mới quyết được.**

### 3.5 · Ba con số khác của em bị sửa

| em ghi | đo lại | vì sao |
|---|---|---|
| prompt production **34.774 / 36.169 / 40.459** ký tự | **50.241 / 51.636 / 55.926** | bản dump của em **thiếu `REASONING_RULEBOOK`** (15.465 ký tự), vốn được nối **vô điều kiện** |
| *«15.155 ký tự vùng chết»* | **15.154** | chênh 1, tuỳ có tính ký tự xuống dòng trước fence |
| *«95 mục thiếu hạn»* | **156/429** | em chỉ đếm mục **còn mở**; tổng trên toàn bộ 429 mã là 156 |

### 3.6 · Thang mất mát: pipeline KHÔNG mất gì trước `ranked[0]`

Thước bạch thủ tái lập **531/531 bundle, 0 lệch**. Tỉ lệ công bố trúng **đúng bằng nền ở CẢ BỐN
cửa sổ** (`+2,2 / −0,5 / −2,8 / +0,5` điểm phần trăm; `|z| ≤ 0,31` sau khi đo lại hệ số cụm
**cho chính thước này**).

Tầng model→pool→PP1 giữ **98–100%**. Toàn bộ sụp ở **đúng một tầng: `ranked[0]`, còn ≈33%**.

### 3.7 · `_SPECIALIST_MIN_HITRATE = 0,35` nằm DƯỚI nền MN (0,430)

Cổng *«specialist»* ở MN **nhận cả model chạy dưới mức ngẫu nhiên** — ngày 23/08 có **25 model**
qua cổng. Và lớp ghi đè chỉ **BẬT ở MN** — đúng miền cổng vô nghĩa nhất.

### 3.8 · Nhãn `family` ghi cứng — ĐANG SỐNG, không phải chỉ dữ liệu cũ

**774 dòng** bị dán nhãn `SHADOW_AUTO` trong khi model thuộc registry OUTPUT-15; **100% đến từ
một nhánh duy nhất**. Và **3.315 dòng** nhánh đó còn bị ghi cứng luôn trường `run_source`.
Đường chấm điểm gọi thẳng hàm này ⇒ **lỗi đang chạy trong production**.

### 3.9 · Cánh tay đối chứng cho phép đo 06/11 nằm trên MỘT máy duy nhất

Bộ model **đóng băng 02/08** — **13 tệp, 45,6 MB** — làm đối chứng cho phép đo cadence hẹn
**06/11**. `DOC.txt` của chính nó ghi *«KHÔNG XOÁ. KHÔNG GHI ĐÈ.»*

| | |
|---|---|
| trên máy chủ | ✅ 13 tệp |
| trong git | ❌ **0 tệp** |
| bản sao nơi khác | ❌ **không có** |

**Đã kéo bản sao về, đối chiếu 13/13 khớp từng byte**, và ghi manifest băm vào kho riêng để kiểm
toàn vẹn mà không phình kho.

⚠️ **Tầng thứ hai:** `.gitignore` chặn `*.pkl` và `*.pt` — **đúng hai đuôi của hai model đang
THIẾU** trong bộ đóng băng (xem `FU-432`, hạn **30/08**). Ai làm đúng `FU-432` mà chỉ chép tệp
vào thư mục thì **git vẫn lặng lẽ bỏ qua** — cánh tay đối chứng **vẫn không được sao lưu**.

### 3.10 · Ba điều phản biện bắt được về chính kho quản trị

| # | điều |
|---|---|
| ① | `LUAT_CHUNG.md` **không có dòng khai danh tính ở dòng 1** ⇒ **7/8** mặt, không phải 8/8. Theo `FAILURE: BLOCK_MUTATION` của chính điều luật, tệp này đang ở trạng thái **cấm sửa** |
| ② | Sổ sự kiện `AUTOMATION_HISTORY.jsonl` **bị `.gitignore` khớp** — sống sót **chỉ vì đã nằm trong index**, không lớp bảo vệ nào |
| ③ | `CLAUDE.md` §63 ghi *«sổ sự kiện im từ 31/07»* — thật ra **08/07**, lệch **23 ngày**, khoảng im nay **47 ngày**. Cổng `K2` không bắt vì nó đo tuổi dòng **mới nhất toàn tệp**; nửa version còn sống **che** nửa sự kiện đã chết |

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Không đụng production.** Phiên READ-ONLY. Mọi phát hiện đều thành **thiết kế** hoặc
**Decision Gate**, không thành thay đổi.

**Không tự chọn ở bất kỳ Decision Gate nào** — owner khoá *«Cấm tự quyết … đổi publish gate»*.

**Không dọn kho báo cáo công khai.** Viết lại lịch sử git một kho công khai là thao tác **phá
huỷ** ⇒ quyết định của owner.

**Không đưa 45,6 MB nhị phân vào git** — đó là hình dạng kho, thuộc về owner. Trước mắt: bản sao
+ manifest băm.

---

## 5 · ĐÃ LÀM GÌ

| # | việc | bằng chứng |
|---|---|---|
| 1 | **Context7** — trigger vào **đủ sáu mặt**, `T1`–`T4` đạt | verdict `SAFE_AND_USEFUL` · `docs/CONTEXT7_SMOKE_TEST_20260824.md` |
| 2 | **Backup `FAIL_CLOSED`** — hàm dùng chung + bản từ xa | thử chặn **8/8 local** + **hai chiều trên máy chủ** |
| 3 | **Cổng `PUBLIC_REPORT_SAFETY`** — chưa từng tồn tại, đã dựng | thử chặn **11/11** |
| 4 | **Kéo bản sao cánh tay đối chứng 06/11** | 13/13 khớp byte + manifest |
| 5 | `FU-437` · `FU-437b` mới | đều có **hạn + ngưỡng + Decision Gate** |
| 6 | **Rút lại ba con số** đã công bố | §3.1 · §3.4 · §3.5 |

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11062_nang_version.py --kiem` | ✓ **ĐẠT** (V11110) |
| `_v11044_cong_so_hieu.py` | ✓ `SO_HIEU_V11044=KHOP` |
| `_v10981_kiem_lich.py` | ✓ **ĐẠT 8/8** — 0 mồ côi |
| `_v10925_rule_sync_check.py` | ✓ **SÁU MẶT ĐỒNG BỘ** |
| `_v11027_so_muc_quan_tri.py` | ✓ không mục nào biến mất |
| `_v11110_backup_an_toan.py --thu-chan` | ✓ **8/8** |
| `_v11110_cong_bao_cao_cong_khai.py --thu-chan` | ✓ **11/11** |

---

## 7 · VƯỚNG VẤP

### 7.1 · Cổng an toàn báo cáo công khai **chưa từng tồn tại**

Prompt 32 bắt chạy `PUBLIC_REPORT_SAFETY_GATE`. Quét kho: **không tệp nào cài nó** — tên nghe
như đã có. Đã dựng, thử chặn **11/11**.

**Và bản đầu của chính cổng đó MÙ HOÀN TOÀN VỚI IP.** Danh sách ngoại lệ có một dòng tha *«số
phiên bản»* dạng `\d+.\d+.\d+.\d+` — **địa chỉ IPv4 cũng khớp đúng khuôn đó**, nên ngoại lệ nuốt
sạch thứ cổng sinh ra để bắt. Phép thử `[1]` đỏ ngay lần chạy đầu. **Không có bài thử thì cổng
này sẽ luôn báo xanh** — đúng ca cổng đóng băng từng mù suốt từ lúc dựng.

> **Bài học ghi thẳng:** ngoại lệ phải **HẸP HƠN** thứ nó tha. Số phiên bản ba thành phần
> **không bao giờ** khớp regex IP (regex đòi đủ **bốn** octet), nên nó **không cần** ngoại lệ nào.

### 7.2 · Kho báo cáo công khai **đã lộ từ trước**

Chạy cổng lên **1.599 tệp** `.md` hiện có:

| loại | số lần | số tệp |
|---|---:|---:|
| 🔴 địa chỉ máy chủ | **1.137** | **86** |
| 🔴 đường dẫn tuyệt đối trên máy chủ | **681** | **151** |
| 🔴 chuỗi đăng nhập `user@host` | **40** | **22** |
| ✅ credential · khoá riêng · chuỗi kết nối CSDL | **0** | **0** |

**Không khoá nào lộ.** Nhưng đây là kho **CÔNG KHAI** — địa chỉ máy chủ nằm đó nghĩa là bất kỳ
ai cũng biết **đúng máy nào** đang chạy dịch vụ.

⛔ **Agent KHÔNG tự dọn.** Viết lại lịch sử git một kho công khai là **phá huỷ** ⇒ owner quyết.
Cổng chặn tệp **MỚI**; tệp **CŨ** chỉ được **BÁO**.

### 7.3 · Em vá **2/7** điểm backup mà tiêu đề commit đọc như xong cả họ

Còn **5 điểm chưa vá**. Đúng khuôn `RM-07` *«vá một lỗi không phải vá cả họ lỗi»* — và lần này
là về **chính commit của em**.

### 7.4 · Bảy làn có kết luận bị phản biện bác

**13 kết luận bị bác.** Nặng nhất: làn đo tuyên bố *«byte đang chạy production nằm trong git
HEAD»* — sai ở mức byte, vì `core.autocrlf=true` khiến `git diff HEAD` so **sau khi chuẩn hoá**.
Câu đúng: *«nội dung SAU CHUẨN HOÁ được neo ở HEAD; byte thô thì KHÔNG»*. Khác biệt này quyết
định mọi cổng nghiệm thu khôi phục bằng băm **nói thật hay báo động giả**.

---

## 8 · GỠ VỀ

| việc | cách |
|---|---|
| luật Context7 | gỡ khối khỏi bốn mặt sửa tay rồi chạy lại bộ sinh |
| hàm backup an toàn | công cụ mới, không ai gọi trong production ⇒ xoá tệp là xong |
| cổng báo cáo công khai | công cụ mới, chưa nối hook ⇒ xoá tệp là xong |
| bản sao model đóng băng | chỉ là bản sao trong `backups/` ⇒ xoá thư mục |

**Không có thay đổi production nào trong phiên này để gỡ.**

---

## 9 · THEO DÕI TIẾP

| ngày | việc | verdict nếu ngưỡng đạt |
|---|---|---|
| **24/08** | kiểm lượt 05:00 đóng dấu `CTX-18.6` | `RUNTIME_PROVEN` |
| **26/08** | `FU-429` · `FU-434` | `0/N` vi phạm |
| **27/08** | `FU-435` · `FU-436` · **`FU-437`** · `FU-437b` | **cần owner ký** |
| **30/08** | `FU-432` — **trước 02:00**, kèm bẫy `.gitignore` | đủ 12/12 tệp **và** được sao lưu |
| **31/08** | 🔴 **`FU-183` tự nổ** — hai cách đọc ngược nhau, không có cron | **cần owner phán trước ngày đó** |
| **13/09** | ML MB ba lần liên tiếp | BỎ CỜ |
| **15/09** | **MILESTONE** | mọi root fix · observability · context conversion · provenance |
| **30/09** | `smart-ml` vs `random-forest` | `MEASURING_WITH_REGISTERED_GATE` |
| **06/11** | cadence retrain | `MEASURING_WITH_REGISTERED_GATE` |

---

## §62 (A60) — BA LỚP NGUỒN

### `OWNER_SAID`

> *«PROMPT TỔNG LỰC LẦN 32 — MASTER WORK PACKAGE»* · *«Cấm tự quyết thay model, bật PP5, tắt
> lớp ghi đè MN, đổi publish gate hoặc timeout»* · *«cấm "hoàn tất giả"»* · và câu hỏi mở phiên:
> *«em đã push báo cáo githubs chưa em?»*

### `CODE_DID`

| điều | bằng chứng |
|---|---|
| thẻ chính trống 100% | gọi ẩn danh hai endpoint trên production, ba miền, có/không tham số ngày |
| ngày đóng băng tự nó trượt cổng | ba miền đều 14/15, thiếu đúng một model |
| hai mô hình tiền đổi dấu | chạy lại cả hai trên bản sao DB |
| prompt thật 50k ký tự | dump từ hàm đang serve, có nối lớp luật suy luận |
| cổng an toàn báo cáo | thử chặn 11/11, kho cũ 1.137 + 681 + 40 lần |

### `DOC_SAID`

| nguồn | ghi gì | lệch không |
|---|---|---|
| `REPORT_V11108.md` §1b | *«chưa bao giờ lên trang»* | 🔴 **LỆCH** — đã rút lại §3.1 |
| `SSOT V11107` | prompt 34.774/36.169/40.459 ký tự | 🔴 **LỆCH** — thiếu một lớp, thật là 50k |
| `CHANGELOG` §63 | sổ sự kiện im từ 31/07 | 🔴 **LỆCH** — thật là 08/07 |
| `DOC.txt` bộ đóng băng | *«KHÔNG XOÁ. KHÔNG GHI ĐÈ.»* | ✓ khớp — nhưng **không có bản sao nào** |

**Ba lớp lệch nhau ⇒ finding bắt buộc báo:** ba mục trên, đã rút lại đúng chỗ công bố.

---

**TanPhatAI cần làm:** ghi vào sổ **`FU-437`** (thẻ chính `/du-doan` trống **100%** với người
xem ẩn danh suốt 77 ngày — **hai quyết định owner ký chồng nhau**, Decision Gate bốn lối, **giao
với `FU-435`** nên phải đọc cùng lúc) và **`FU-437b`** (cánh tay đối chứng cho phép đo 06/11 chỉ
nằm trên một máy — đã có bản sao + manifest, cần owner quyết cách lưu lâu dài, kèm **bẫy
`.gitignore` sẽ làm `FU-432` thất bại thầm lặng**); **sửa lại trong sổ ba con số đã công bố sai**
— `−90,3tr` không cố định (hai mô hình **đổi dấu**), prompt thật **50k** không phải 34k, thiếu
hạn **156/429** không phải 95; ghi **rút lại lần ba** cho câu *«bạch thủ 10 chưa bao giờ lên
trang»*; ghi **ba điều về chính kho quản trị** (`LUAT_CHUNG.md` thiếu dòng khai danh tính và
đang ở trạng thái cấm sửa · sổ sự kiện bị `.gitignore` khớp · `CLAUDE.md` §63 ghi sai ngày, lệch
23 ngày); và ghi **một mục mới cho owner quyết**: kho báo cáo công khai đang lộ **địa chỉ máy chủ
1.137 lần / 86 tệp** và **đường dẫn máy chủ 681 lần / 151 tệp** (không khoá nào lộ) — dọn hay
không là quyết định của owner vì phải viết lại lịch sử git.
