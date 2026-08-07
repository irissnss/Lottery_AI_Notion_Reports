# REPORT V11016 — SỐ THÀNH LỜI KỂ (L-A) + NGƯỠNG TỰ QUYẾT (L-B)

> **Ngày:** 2026-08-07 · **Owner chốt:** *"Làm ngay luôn đi em."*
> **Đã deploy** · PID `974549 → 979960` · 4 bảng khoá Y HỆT · `/api/health` 200

---

## 1. Tóm tắt

Owner chốt làm ngay việc L-A. Agent sửa **một** khối, đo lại thì prompt **dài thêm 1.336 ký tự**
mà dòng rổ số **9 → 12** — vì **ba khối khác vẫn in đúng bộ số đó** dưới ba hình thức khác.

Gỡ cả bốn. Chỗ thứ tư — chỗ **neo mạnh nhất**, vừa xếp hạng vừa khuyên chọn — suýt bị bỏ sót và
**cổng deploy bắt được**, dừng trước khi restart.

Kết quả: **cặp khối trình lại cùng một bộ số MB 10 → 4 · MT 7 → 3**. Prompt dài thêm ~1.000–1.400
ký tự — nói thẳng, vì lời kể dài hơn danh sách.

## 2. Owner yêu cầu gì (nguyên văn)

> *"Làm ngay luôn đi em."*

Trả lời câu agent hỏi cuối phiên trước: *"L-A làm ngay hay chờ 21/08? Làm ngay ⇒ FU-284 thành đo
gộp ba biến, hết tách nhân quả. Chờ ⇒ giữ phép đo sạch nhưng đợi thêm 2 tuần."*

Việc gốc owner giao cùng ngày:

> *"các số học được nhồi nhét cần biến thành ngữ cảnh thực sự để model đọc hiểu tự phân tích, tự
> tư duy tự tra soát trong ngưỡng tự quyết định output số tốt nhất ở số chính và nhẹ hơn là số
> phụ, tất cả tự nhiên có quy luật có điều kiện, đừng output theo số gò như thế dẫn đến bầy đàn
> là đúng rồi, lùa vào 1 bộ số định sẵn trong ngày để model quyết định xong thấy bầy đàn."*

## 3. Đào bới / phát hiện

### 3.1 Sửa một khối thì SỐ ĐI SAI HƯỚNG · `VERIFIED_TEST`

Sau khi đổi khối `RULES-FIRST` thành lời kể, đo bằng cùng một thước trên cả hai bản:

| chỉ số | trước | sau bản sửa 1 khối |
|---|---|---|
| ký tự MB | 10.379 | **11.715** (+1.336) |
| dòng rổ số MB | 9 | **12** (+3) |
| cặp khối trùng ≥60% | 10 | **10** (không đổi) |

**Đi ngược mục tiêu.** Nguyên nhân: rổ số vẫn còn ở ba chỗ khác.

### 3.2 BỐN chỗ cùng một bộ số · `VERIFIED_CODE`

| # | chỗ | hình thức | mức neo |
|---|---|---|---|
| 1 | `RULES-FIRST` | rổ hợp nhất `trỏ tới 10 đuôi: 13 31 32 …` | cao |
| 2 | `EVIDENCE TABLE` › `Rule candidates` | rổ **ĐÃ XẾP HẠNG** `🔥 35: boost=0.180 CONV×2` ×8 | **rất cao** — chỉ luôn số nào đứng đầu |
| 3 | `EVIDENCE TABLE` › trace | rổ trần `← ✅ Hà Nội G6+G7 → tails=[13,35,69,84,88,89,95]` ×5 | cao |
| 4 | `OWNER ANTI-TRAP CHECK` › `FRESH candidates` | **vừa xếp hạng vừa khuyên chọn** — `boost=0.100` + *"prefer if doctrine support is also strong"* | **cao nhất** |

Đo trùng lặp: khối #2 trùng **100%** bộ số với `Block 3 — Candidate Convergence` và **68%** với
khối kể sự kiện. Cùng một bộ số, bốn lần, bốn nhãn khác nhau — đúng lời owner: *"các tầng điều
nhồi tương tượng na ná nhau liên tục"*.

### 3.3 Cổng deploy cứu một lần · `VERIFIED_TEST`

Bản đầu chỉ sửa 1/4 chỗ. Cổng trước restart kiểm bằng chuỗi thật trên VPS:

```
MB: ro_hop_nhat_da_het=True · ke_su_kien=True · nguong_tu_quyet=True
    · ro_xep_hang_da_het=False ← TRƯỢT · ep_chon_da_het=True
✗ DỪNG — prompt trên VPS không đúng như mong đợi, KHÔNG restart
```

**Cả ba miền trượt, script dừng trước khi restart.** Không có cổng đó thì đã deploy một bản làm
nửa vời và báo "xong".

## 4. Hướng xử lý và vì sao chọn

**Gỡ cả bốn, không gỡ ba.** §60.1 nói rõ: *"bỏ nửa chừng còn tệ hơn không làm"*. Gỡ ba chỗ mà để
lại chỗ neo mạnh nhất thì phép đo 14 ngày sẽ đang đo một thay đổi làm nửa vời.

**Giữ cái gì:** thông tin **LOẠI TRỪ** giữ nguyên — «đuôi này miền ra trước đã tiêu rồi», «bao
nhiêu luật cùng chỉ một chỗ ⇒ rủi ro bầy đàn cao hơn». Đó là căn cứ để **TRÁNH**, ngược hẳn với
rổ để **CHỌN**.

**Bỏ cái gì:** mọi **xếp hạng** (`boost=`) và mọi **lời khuyên chọn** (*"prefer if…"*). Điểm xếp
hạng đó do chính bộ luật đã đo ra **ngang luật giả** sinh ra.

**Vì sao đưa hồ sơ kèm CÁCH ĐỌC thay vì giấu hồ sơ:** con số `12 tuần trúng 10/12` là thật, giấu
đi là bớt ngữ cảnh. Nhưng nó chấm **ngược** trên chính cửa sổ đã đào ra luật. Nên đưa cả hai —
con số **và** lý do nó bị thổi phồng. Đó mới là ngữ cảnh thật.

## 5. Đã làm gì

### 5.1 Khối mới — nguyên văn model đọc

```
### 📖 BỐI CẢNH SOI CẦU (kể lại sự kiện — KHÔNG có danh sách số chốt sẵn)
Kho luật của bucket MB/Thứ Sáu hiện có 3 luật đang hoạt động. Mỗi luật là một mệnh đề
dạng «đuôi ra ở đài nguồn tại giải nguồn thường quay lại ở MB vào Thứ Sáu».
Dưới đây là những gì ĐÃ THỰC SỰ XẢY RA ở phía nguồn:

  1) thứ Năm 06/08, đài Hà Nội (MB) ra ở G6+G7 các đuôi: 13 35 69 84 88 89 95.
     Luật nối chỗ này với hôm nay có hồ sơ: 12 tuần gần nhất trúng 10/12 · 16 tuần
     trúng 14/16 — đọc mục CÁCH ĐỌC bên dưới trước khi tin con số này.
  2) thứ Năm 06/08, đài Hà Nội (MB) ra ở G1+G7 các đuôi: 35 60 69 89 95.
     …

CÁCH ĐỌC CON SỐ HỒ SƠ Ở TRÊN — đọc kỹ trước khi tin (đo 07/08/2026):
  · Tỉ lệ 12/16 tuần đó chấm NGƯỢC trên chính cửa sổ đã đào ra luật, nên nó cao là
    đương nhiên — không phải thành tích.
  · Đo TIẾN (sau ngày đào, luật không được nhìn trước): z = −0,33 / +0,26 — tức
    NGANG BẰNG luật giả sinh ngẫu nhiên.
  · 0/105 luật đủ mẫu qua cổng đo tiến (cần ≥20 lượt/luật, hiện tối đa 3).
  ⇒ Nói thẳng: hồ sơ «trúng 10/12» ở trên KHÔNG dự báo được 83% cho hôm nay.

⇒ Đây là BỐI CẢNH để bạn phân tích, KHÔNG phải kết luận. Không có danh sách số chốt
  sẵn nào ở tầng này. Bạn tự rút số từ các sự kiện trên nếu thấy có lý, hoặc bỏ qua
  hẳn tầng này nếu phân tích riêng của bạn dẫn tới chỗ khác.

NGƯỠNG TỰ QUYẾT — tự cân mức tin trước khi chốt:
- Trong analysis, ghi một dòng «MỨC TIN: cao | vừa | thấp» kèm một câu vì sao.
- Chỉ ra SỐ PHỤ khi mức tin là CAO và số phụ có đường lập luận ĐỘC LẬP với số chính.
- Mức tin VỪA hoặc THẤP ⇒ chỉ ra SỐ CHÍNH, để secondary_number="" và
  secondary_reason="NO_SECONDARY". Ra ít mà chắc hơn ra đủ cho đẹp.
```

### 5.2 L-B an toàn vì hợp đồng ĐÃ CHO PHÉP từ trước

Kiểm 5 tệp tiêu thụ: `combo_super.py` · `ensemble_voting.py` · `advanced_modes.py` ·
`main.py` · `gpt_analyzer.py` — tất cả đều lọc rỗng an toàn
(`numbers = [n for n in [main_num, sec_num] if n]`) và mọi chỗ đọc `numbers[1]` đều có
`if len(numbers) > 1`. Hợp đồng JSON đã có sẵn `secondary_number=""` +
`secondary_reason="NO_SECONDARY"` trong QUY ƯỚC FALLBACK. **Chưa chỗ nào nói KHI NÀO được dùng
quyền đó** — V11016 nói rõ.

### 5.3 Sửa một câu trỏ vào thứ đã gỡ

`CONVERGENCE TRAP ALERT` từng ghi *"Tìm SỐ THAY THẾ từ **DANH SÁCH MINED RULES**"* — danh sách đó
vừa bị gỡ. Để nguyên là ra lệnh cho model dùng một thứ **không còn tồn tại** (đúng lỗi §60.1 của
V11001). Nay trỏ vào *"các sự kiện ở khối «BỐI CẢNH SOI CẦU»"*.

## 6. Cổng kiểm

### 6.1 Đo TRƯỚC / SAU — cùng một thước, chạy cả hai bản

| chỉ số | MB trước→sau | MT trước→sau | MN trước→sau |
|---|---|---|---|
| ký tự | 10.387 → **11.401** | 8.903 → **10.298** | 8.370 → **9.818** |
| số hai chữ số | 252 → **235** | 209 → **206** | 195 → **198** |
| **cặp khối trùng ≥60%** | 10 → **4** | 7 → **3** | 1 → **1** |
| mệnh lệnh | 0 → 0 | 1 → 1 | 1 → 1 |

### 6.2 §60.3 — KHÔNG kết luận bằng đếm thô

Chỉ số *"dòng ≥6 số"* MB tăng 9 → 10. Đọc từng dòng thì:

| loại | số dòng |
|---|---|
| **tỉ lệ phần trăm / cửa sổ** (`12W=83.3% \| 16W=81.2%`, `1W(7d):19/35=54%`) | 2 |
| **ngày tháng** (`07-31:4% \| 07-24:0%`) | 1 |
| **ví dụ minh hoạ** (`đảo vị trí 34→43`, `±1: 34→35/33/44/24`) | 1 |
| **hồ sơ luật** (`12 tuần trúng 10/12 · 16 tuần trúng 14/16`) | 3 |
| **ĐUÔI THẬT — sự kiện có đài + ngày + giải** | **2** |
| **ĐUÔI THẬT — pool đã tiêu (thông tin loại trừ)** | **1** |

⇒ Chỉ **2 dòng** thật sự là đuôi dùng để chọn, và cả hai **đã gắn nguồn**. Bộ đếm thô nhận nhầm
7 dòng còn lại.

### 6.3 Deploy

| phép | kết quả |
|---|---|
| md5 local = VPS | ✓ `96f6073cadafa73fb1542fe6e9c8e0b6` |
| `py_compile` trên VPS (venv) | ✓ OK |
| cổng prompt 3 miền | ✓ `rổ_hợp_nhất_đã_hết · kể_sự_kiện · ngưỡng_tự_quyết · rổ_xếp_hạng_đã_hết · ép_chọn_đã_hết` = True |
| PID | `974549 → 979960` ✓ ĐÃ ĐỔI |
| `/api/health` | **200** |
| 4 bảng khoá | ✓ **Y HỆT** — `11916\|25692` · `481\|661` · `15226\|15330` · `11739\|11739` |
| cổng gan/nóng/lạnh | `PROMPT_SACH=DAT` |
| cổng chặn cắt cụt | ✓ sạch |
| J5 mốc tải | ✓ khớp sổ thật |

Phiên bản: `SP-4.4` · `RR-16.5` · **`CTX-17.0→18.0`** · **`PB-19.0→20.0`**

## 7. Vướng vấp

**Agent lại suýt làm nửa việc — lần thứ hai trong hai ngày.** Sửa một khối, thấy chuỗi kiểm
`ép_chọn=False` là tưởng xong. Chỉ vì **chạy phép đo trước/sau** mới thấy prompt đi ngược mục
tiêu, và chỉ vì **cổng deploy chặn** mới thấy chỗ thứ tư.

Bài học: **chuỗi kiểm có mặt/vắng mặt không đủ.** `ép_chọn=False` đúng mà việc vẫn chưa xong —
vì câu hỏi thật không phải *"còn câu ép chọn không"* mà *"model còn được đưa một rổ số dọn sẵn
không"*. Phải đo **hình thù dữ liệu**, không chỉ dò chuỗi.

**Prompt dài thêm.** Không giấu: MB +1.014, MT +1.395, MN +1.448 ký tự. Lời kể dài hơn danh sách.
Owner xin **ngữ cảnh**, không xin ngắn — nhưng nếu owner muốn ngắn lại thì phải nói, vì đây là
đánh đổi thật.

## 8. Gỡ về

```bash
# VPS
cp /root/Lottery_AI_Test/backups/gpt_analyzer.py.v11016_pre \
   /root/Lottery_AI_Test/web/backend/gpt_analyzer.py && systemctl restart lottery
# local
cp backups/v11016_pre/gpt_analyzer.py.pre web/backend/gpt_analyzer.py
```

Bản trước md5 `f8b428ece9d90181642806e095ced195` (= PB-19.0, V11014). Gỡ về ~2 phút.

## 9. Theo dõi tiếp

| Mã | Nội dung | Trạng thái | Hạn |
|---|---|---|---|
| **FU-321** (gộp FU-322) | Số thành lời kể + ngưỡng tự quyết | **`DEPLOYED_PENDING_LIVE_VERIFY`** | 07/08 |
| **FU-284** | **Đếm lại lần BA** — nay đo gộp **ba** thay đổi prompt | `WAIT_LIVE` | **21/08** |
| **FU-316** | Còn `D-1 cross-region tail pool` — 12 đuôi **chưa gắn nguồn** | `MEASURED_ROOT_CAUSE` (đã thu hẹp) | 14/08 |
| **FU-317** M-A | Tầng đối chứng ML × rules × bộ lọc | agent làm được ngay | 10/08 |
| **FU-318** M-C | Học lại theo TRÔI | agent làm được ngay | 11/08 |
| **FU-319/320** M-B/M-D | Chính-phụ theo biên · bỏ 6 đặc trưng gan khỏi ML | **chờ owner** | 14/08 |

**Hệ quả owner đã chấp nhận:** FU-284 nay đo **gộp ba biến** — gỡ gan (06/08) + thôi ép chọn
(07/08) + số thành lời kể (07/08). Không tách được nhân quả giữa ba phần. Agent trình rõ đánh
đổi, owner chốt *"Làm ngay luôn đi em"*.

**Ngưỡng gỡ về:** đo tiến 14 ngày từ 07/08 ⇒ chốt **21/08**. Tụt ≥5 điểm bền ⇒ gỡ về `v11016_pre`.
