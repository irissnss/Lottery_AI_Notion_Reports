# REPORT V11039 — TỔNG HỢP BỐN PHIÊN + BẮT ĐƯỢC HAI TỆP BỊ CẮT CỤT

**Ngày:** 2026-08-08 khuya · **Loại:** audit tổng hợp + sự cố toàn vẹn dữ liệu
15 agent kiểm chéo + phản biện đối kháng · **CHỈ ĐỌC DB**

---

## 1. Tóm tắt

Owner hỏi *"em có đọc được các session khác không"*. Trả lời: **đọc được** — bằng cách **mở tệp
nhật ký phiên**, không phải nhớ sẵn. Mỗi phiên một tệp; agent **không mang ký ức qua phiên**.

| | |
|---|---|
| **Bốn phiên** | 125 lượt owner. Mốc giờ trong nhật ký là **UTC**, phải cộng 7 |
| **Kiểm chéo phiên song song** | 9 lời khai → **5 xác nhận · 3 đúng một phần · 0 bác bỏ** |
| **Ba lỗ hổng** phiên đó chưa nêu | `C23`/`C24` chưa từng chạy · 2 mã đọc vẫn va chạm · lane có **0 dòng đo tiến** |
| **Bốn món nợ tháng 7** | dọn sổ · B1 · B2 · **8 commit không báo cáo** |
| **⚠ SỰ CỐ** | **`CHANGELOG.md` mất 17.453 dòng · `main.py` mất 4.056 dòng, KHÔNG PARSE ĐƯỢC** |
| **Production** | **AN TOÀN** — chỉ bản local hỏng. Đã khôi phục cả hai |

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

> em có đọc được các secsion khác của em không ? hãy tổng hợp lại và báo cáo dùm anh

---

## 3. Đào bới / phát hiện

### 3.1 Bốn phiên

| phiên | khoảng (giờ VN) | ngày | lượt owner | dung lượng |
|---|---|---|---|---|
| `0157ff2f` · làm quen dự án | 03/07 19:18 → 25/07 19:29 | 2 | 5 | 0,56 MB |
| `32021ea4` · giao diện UI v2 | 25/07 10:03 → 26/07 01:56 | 2 | 25 | 5,69 MB |
| **`b3fc6f6a` · SONG SONG** | **08/08 18:42 → 20:29** | 1 | 4 | 2,28 MB |
| `d2a0e7e5` · chính (đang chạy) | 01/08 13:35 → 08/08 21:42 | 7 | 91 | 30,23 MB |

Commit hôm nay: **10 của phiên chính · 2 của phiên song song** (`207404c` 20:16 · `5b22997`
20:28), **xen kẽ nhau**.

### 3.2 Kiểm chéo phiên song song — 9 lời khai, **0 bác bỏ**

**229 bản ghi đài Miền Trung bị gán nhãn MN** — đếm lại **độc lập bằng SQL thuần**, không gọi
module của họ: **đúng 229**, 14 đài đều là đài Miền Trung, **218/229 (95,2%) rơi vào 2021**,
**0 dòng ngoài vùng** đã khai.

Lane `v11037_g2mb_lane`: **549 dòng = 9 mục × 61 ngày**, cờ `(0,1,0,1)` đồng nhất cả 549 dòng.
Cron `35 19 * * *` dùng đúng venv. API `/api/admin/v11037-g2mb-lane` trả **401** — route sống
trong tiến trình đang chạy (`main.py` mtime 20:09:52 **trước** giờ khởi động 20:19:01).

#### Ba lỗ hổng phiên đó chưa nêu

| # | lỗ hổng | tầng đúng |
|---|---|---|
| **a** | **`C23`/`C24` CHƯA BAO GIỜ chạy trong cron thật** — guard deploy **20:09**, lượt 18:05 hôm nay chỉ ghi **22 phép** | `DEPLOYED`, **chưa** `RUNTIME_PROVEN` |
| **b** | **Hai mã đọc cấp lại VẪN va chạm**: `FU-366·KS1208` trùng `FU-348` · `FU-368·SC1308` trùng `FU-278` | *"mỗi mã một việc"* đúng ở tầng **số FU**, sai ở tầng **mã đọc §58** |
| **c** | **549 dòng là MỘT lượt nạp lùi** — `la_do_lui=1` cả 549, `created_at` cùng mốc 20:11. Lane có **0 dòng đo tiến**; cron 19:35 **chưa nổ lượt nào** | dễ đọc nhầm thành *"61 ngày bằng chứng tiến"* |

*(Code lane tự ghi đúng điều (c): `KHONG_DUNG_DE_QUYET`. Chỉ câu tóm tắt là mỏng.)*

### 3.3 Số học phiên song song — tái lập ĐÚNG TỪNG CHỮ SỐ

**Câu 1 — bộ số đuôi trùng miền cùng ngày (869, 617):**

| | |
|---|---|
| lưới | **225 tổ hợp** trên 1.976 ngày sạch |
| tổ hợp THẬT | 21,31% · +1,23σ · hạng **25/225** |
| ý owner *"MN trước 3 hôm"* | **19,41%** · −0,86σ · hạng **180/225** — **tệ hơn trung bình** |
| bằng chứng quyết định | sd giữa 225 ô **0,89%** ≈ se lý thuyết **0,90%** ⇒ **toàn bộ là nhiễu** |
| ô cao nhất | +2,84σ < ngưỡng kỳ vọng cực đại **+3,29σ** khi thử 225 phép |

**Câu 2 — đuôi giải nhì MB → MN/MT hôm sau:**

| | |
|---|---|
| 14 ngày gần nhất | **6 lần bạch thủ** — **owner nhìn ĐÚNG** |
| 1.973 ngày | MN bạch thủ **5,2%** vs nền **6,1%** (z **−1,67**) |
| cái bẫy lớn nhất | *"MN hoặc MT bất kỳ vị trí"* **85,8%** — **hai số BẤT KỲ** cũng trúng **85,6%** |
| lag 1 **thấp nhất** | 9,5% vs kỳ vọng 10,4%; lag 2–7 đều 10,0–10,5% |

**Không phải quy luật — là số đông.** MN+MT mỗi ngày có hơn 100 con số.

### 3.4 Hai phiên tháng 7 — bốn món nợ

`0157ff2f`: **đọc-và-tư-vấn thuần**, **0 commit, 0 ssh**.
`32021ea4`: **thay áo UI v2**, **8 commit** (V10846 → V10854), deploy bằng `scp` + so md5,
**không restart, không đụng backend/DB/cron**.

| # | món nợ | trạng thái hôm nay |
|---|---|---|
| 1 | **dọn sổ FOLLOW_UP** đề xuất 03/07 | **chưa bao giờ chạy** — sổ **304 → 749 mục** · tệp **767 KB → 1.314 KB** |
| 2 | **B1 «luôn xuất số»** `/du-doan` | `main.py:10704` vẫn `bundle=None, empty=True`. Đúng thiết kế, chờ chữ ký, **không có mã FU** |
| 3 | **B2 viewer-safe API** | `/api/status` vẫn `SELECT *` **không auth**; chỉ giấu bằng **CSS** |
| 4 | **8 commit 25/07 không có báo cáo công khai** | `.cursorrules` **tại chính commit đó** đã ghi `§52D_DRIFT_VIOLATION` |

Thêm: `_v10848_drift_audit.py` đăng ký playbook §2 nhưng **lần chạy cuối 28/07**.

### 3.5 ⚠ BÁC BỎ khung chẩn đoán 03/07

*"MB là lỗi PHỦ, MN/MT là lỗi CHỌN"* — đo lại trên pool **15 model official**:

| báo cáo 03/07 | thật |
|---|---|
| *"3/25 lọt pool 15 model"* | **2/25** — 3/25 chỉ ra khi **gộp 13 model shadow** |
| *"MT 39 = 6 vote"* | **1 phiếu**, hạng **10/10** |
| *"MN 34 = 5 vote"* | **4 phiếu** |
| *"54 nằm sẵn trong pool"* | **0 phiếu official** |

Chuẩn hoá theo nền: MB lift **0,67** · MN **0,99** · MT **1,11** — cả ba quanh 1, chênh nằm
trọn trong nhiễu Poisson của **n = 1 ngày**.
**65 ngày ĐẢO NGƯỢC nhãn:** MT **0,93** (kém nhất) · MB **0,96** · MN **1,02**; pool cả ba miền
chứa số trúng **14/14 ngày**.

### 3.6 ⚠⚠ SỰ CỐ TOÀN VẸN — hai tệp bị cắt cụt

Đang ghi tài liệu thì `CHANGELOG.md` báo **2.190.908 → 1.144.532** ký tự *trước khi* ghi.
Tệp không tự nhỏ đi được.

| tệp | trên đĩa | trong git HEAD | mất | cắt tại |
|---|---|---|---|---|
| `CHANGELOG.md` | 1.150.783 ký tự · 13.169 dòng | 2.190.908 · 30.622 dòng | **17.453 dòng** | giữa chừng, cụt ở `## V20.3` |
| **`web/backend/main.py`** | 775.176 ký tự · **17.148 dòng** | 964.243 · **21.204 dòng** | **4.056 dòng** | **đúng 786.432 byte = 768 KiB** |

**`main.py` KHÔNG PARSE ĐƯỢC** — `SyntaxError` dòng 17149, cụt giữa `for n in (7, 14, 30, 60):`.

**Production AN TOÀN:** VPS **976.303 byte · 21.204 dòng · PARSE OK** · service `active` ·
health **200**. Chỉ bản **local** hỏng — nhưng ai deploy từ đó là **đưa tệp không chạy được lên
production**.

---

## 4. Hướng xử lý và vì sao chọn

**4.1 — Kiểm lời khai bằng KHO THẬT, không đọc lại lời phiên kia.** Báo cáo chỉ kể lại là vô
giá trị. Con số 229 được đếm lại bằng **SQL thuần**, không gọi module của họ (RM-13).

**4.2 — Khôi phục `CHANGELOG.md` bằng cách GHÉP, không `git checkout`.** Khối V11039 vừa viết
là nội dung mới, `checkout` sẽ xoá mất. Ghép **khối mới + nguyên bản HEAD**, rồi kiểm
`lai.endswith(head) == True`.

**4.3 — `main.py` thì `git checkout` được** vì bản local **không có gì mới** — nó chỉ là bản
HEAD bị cắt. Xác nhận bằng md5 local = VPS sau khôi phục.

**4.4 — Giữ lại bản cụt làm bằng chứng** ở thư mục tạm phiên, không xoá.

---

## 5. Đã làm gì

**TRƯỚC:** `CHANGELOG.md` 1.150.783 ký tự (mất 17.453 dòng) · `main.py` 775.176 ký tự
(mất 4.056 dòng, `SyntaxError`).
**SAU:** `CHANGELOG.md` **2.199.918** ký tự · **351 mục `## V`** · `HEAD` là hậu tố ·
`main.py` **964.243** ký tự · **21.204 dòng** · **PARSE OK** · md5 **`778a6e317c85d76e1411a1a464e7e76b`** = md5 VPS.
**PHIÊN BẢN:** V11039 + V11039b · 08/08/2026.
**KIỂM:** `python web/backend/_v11015_cong_chan_cat_cut.py` → *«không tệp nào ngắn đi bất thường»*

| việc | kết quả |
|---|---|
| Đọc 4 nhật ký phiên | bảng thời gian + 125 lượt owner |
| Kiểm chéo 9 lời khai | 5 xác nhận · 3 đúng một phần · **0 bác bỏ** |
| Đếm lại 229 độc lập | **đúng 229**, 218/229 rơi 2021 |
| Tái lập số học phiên song song | **khớp từng chữ số** |
| Bóc hai phiên tháng 7 | 4 món nợ + bác bỏ khung 03/07 |
| **Phát hiện + khôi phục 2 tệp cắt cụt** | production an toàn, md5 local = VPS |
| Ghi 3 mặt tài liệu | `CHANGELOG` · `SSOT` · `FOLLOW_UP` (FU-373 → FU-378) |

**KHÔNG làm:** không sửa cổng chống cắt cụt (FU-378) — xem §7.3.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| Tuổi dữ liệu | **ĐẠT** |
| `_v11015_cong_chan_cat_cut` sau khôi phục | **ĐẠT** — không tệp nào ngắn bất thường |
| `main.py` parse | **OK** · md5 local = VPS |
| `CHANGELOG.md` toàn vẹn | `HEAD` là **hậu tố**, 0 mục mất, +1 mục mới |
| VPS service | `active` · PID 1094233 · health **200** |
| 4 bảng khoá | **không đụng** — V11039 không ghi DB |
| Số hiệu mới | `FU-373` → `FU-378` — quét trước khi cấp |

---

## 7. Vướng vấp

**7.1 — Agent tự tay xoá mất bằng chứng máy đọc được.** Agent **prepend V11039 trước khi
kiểm**, nên `CHANGELOG.md` từ chỗ *là tiền tố của HEAD* thành *không còn là tiền tố* — đúng thứ
cổng dùng để nhận diện cắt cụt.

**7.2 — CỔNG CHỐNG CẮT CỤT MÙ VỚI TỆP CRLF.** Hai lỗ hổng:

| # | lỗ hổng | hậu quả |
|---|---|---|
| ① | `cu.startswith(moi)` so bản đĩa (**CRLF**) với `git show` (**LF**) ⇒ **không bao giờ khớp** | `main.py` mất 4.056 dòng mà cổng chỉ nói *«ngắn đi nhiều nhưng không phải cắt cụt — kiểm tay rồi commit»*, **thoát 0** |
| ② | `BIEN_NGHI` thiếu **768 KiB** (chỉ có 64·128·256·512·1024·2048) | dấu vân tay rõ nhất bị bỏ qua |

Chính docstring của cổng đã ghi về sự cố 07/08: *«`_doc_prepend` chỉ so với bản TRÊN ĐĨA (đã cụt
sẵn)»* — và **lỗi lặp lại y nguyên sau một ngày**.

**7.3 — CỐ Ý CHƯA vá cổng.** Đây là cuối một phiên rất dài, và bản vá phải đụng logic so sánh
của chính cổng đang bảo vệ mọi thứ. Hạn **09/08**, làm đầu phiên với đầu óc tỉnh.

**7.4 — `_doc_prepend` ném lỗi lệch ĐÚNG 1 ký tự** khi ghi V11039b — do tệp còn sót **1 CRLF**
giữa 30.788 LF. Nội dung ghi **đúng và đủ**; chỉ phép đọc-lại bị lệch. Vẫn là bẫy CRLF.

**7.5 — Agent quên đẩy báo cáo công khai.** Ghi 3 mặt tài liệu + commit riêng rồi **báo xong** —
owner phải hỏi *"đẩy báo cáo đầy đủ chi tiết chưa em?"* mới lộ ra `A55_VIOLATION_REPORT_MISSING`.
Chính tệp này là bản bù.

---

## 8. Gỡ về

Phiên này **khôi phục**, không phá. Bản cụt giữ làm bằng chứng:
`CHANGELOG_cut_cut.md` · `main_py_cut_cut.py` trong thư mục tạm phiên.

```bash
git checkout HEAD -- web/backend/main.py     # nếu cần làm lại
```

---

## 9. Theo dõi tiếp

| mã | nhãn | hạn | trạng thái |
|---|---|---|---|
| **FU-378 · SC0908-4** | **cổng chống cắt cụt mù với tệp CRLF** | 09/08 | `MEASURED_ROOT_CAUSE` |
| **FU-373 · KS1208-2** | `C23`/`C24` chưa từng chạy trong cron thật | 12/08 | `DEPLOYED_PENDING_LIVE_VERIFY` |
| **FU-374 · HT0809-2** | mã đọc §58 vẫn va chạm sau khi đổi số | 09/08 | `MEASURED_ROOT_CAUSE` |
| **FU-375 · BC0908** | 8 commit 25/07 không có báo cáo công khai | 09/08 | `MEASURED_BUT_NOT_FIXED` |
| **FU-376 · DD0918** | bốn món nợ tháng 7 | 18/09 | `AWAITING_OWNER_OK` |
| **FU-377 · TK0809** | đính chính khung «MB phủ / MN-MT chọn» | 09/08 | `MEASURED_ROOT_CAUSE` |

### LOCK-IN

- Agent đọc được phiên khác **bằng cách mở tệp**, không phải nhớ. Mốc giờ **UTC + 7**
- Phiên song song: **0 lời khai bị bác bỏ**; 229 bản ghi sai nhãn **đếm lại độc lập là đúng**
- Hai câu owner hỏi về quy luật số: **cả hai đều là nhiễu**, đã có bằng chứng số
- `CHANGELOG.md` và `main.py` **đã khôi phục đủ**; production **chưa bao giờ bị ảnh hưởng**

### OPEN — cần owner một dòng

1. **57 mục chưa từng có hạn** (FU-165…FU-209) — đóng hàng loạt hay cấp hạn?
2. **Bốn món nợ tháng 7** — dọn sổ FOLLOW_UP trước (nó đang che mọi bộ đếm), hay B1/B2 trước?
3. Xác nhận mã **`QD-047`** cho lộ trình 10 ngày.

### NEXT ACTION — một bước

**Vá `FU-378`: chuẩn hoá `CRLF → LF` cả hai bên trước khi so, thêm mọi bội 256 KiB vào
`BIEN_NGHI`, và bắt `_doc_prepend` gọi cổng TRƯỚC khi ghi.**
Hôm nay cổng này để lọt **4.056 dòng của một tệp production không parse được**. Nếu không vá, lần
sau nó vẫn im.
