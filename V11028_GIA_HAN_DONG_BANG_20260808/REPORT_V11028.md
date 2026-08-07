# REPORT V11028 — GIA HẠN ĐÓNG BĂNG (QD-041) + BẢNG QUY HOẠCH SÁU MẶT + A5 + A6

> **Ngày:** 2026-08-08 · **Không deploy** · không đụng prompt · không đụng 4 bảng khoá
> **Verdict:** `REPORT_PUBLISHED`

---

## 1. Tóm tắt

Owner chốt **gia hạn đóng băng**. Agent làm bốn việc: ghi **sổ sáu lần đổi prompt** (trả lời câu
owner hỏi bằng bằng chứng), ghi **QD-041** với phạm vi **mở rộng sang prompt**, viết lại **bảng
quy hoạch sáu mặt** cho đúng sự thật, và làm **A5 + A6** — hai việc duy nhất trong tầm tay mà
**không chạm prompt**.

## 2. Owner yêu cầu gì (nguyên văn)

> *"Làm tiếp đi kiểm tra lại nội dung quy hoạch rewiter lại 1 bảng đầy đủ nhất toàn vẹn nhất
> chuản chỉnh nhất để sync nhất quán đi nào? FU215 anh nghĩ nên gia hạn thêm để đo đạt kỹ hơn đi
> em, dù gì cũng đã chồng 6 lần rồi, **Nhưng không rõ em còn lưu trữ và nắm rõ các lần em đã làm
> gì chứ?** Làm tiếp cho xong các vấn đề trong tầm tay một cách tỉ mỉ cẩn thận đi"*

## 3. Đào bới / phát hiện

### 3.1 Trả lời câu «còn lưu trữ và nắm rõ không» · `VERIFIED_TEST`

**Có.** Sáu lần đổi, mỗi lần có **commit + md5 + bản sao lưu**:

| # | Lúc | Commit | Bản | md5 `gpt_analyzer.py` |
|---|---|---|---|---|
| 1 | 06/08 19:52 | `381d9da` | PB-18.2 | `1e9df12c5ee25901b738d2b1d5a6333e` |
| 2 | 06/08 21:44 | `38fe600` | PB-18.3 | `50f99eb82ce4dbc5497bb51e2c2d5eb6` |
| 3 | 06/08 22:12 | `bf910d6` | PB-18.4 | `5eb260812641125669bc921eb16dc680` |
| 4 | 07/08 11:01 | `9510886` | PB-19.0 | `11bef4ecca4c81360a10405e3c7f7d72` |
| 5 | 07/08 13:41 | `e69c44c` | PB-20.0 | `96f6073cadafa73fb1542fe6e9c8e0b6` |
| 6 | 07/08 19:41 | `7ec3cc3` | **PB-20.1** | `6b28f0baa7aeceac0e9fd2b75a741a81` |

**Chín bản sao lưu** trong `backups/v1xxxx_pre/` — gỡ về được **bất kỳ mốc nào**.
Lập thành `docs/SO_SAU_LAN_DOI_PROMPT.md`, kèm lệnh tái lập.

### 3.2 Ba việc trong sáu lần đó CHƯA XONG

| việc | tình trạng |
|---|---|
| **V11001 chưa gỡ hết gan/hot** — `format_condensed_stats` vẫn sinh `TOP 5 GỢI Ý (Score/Zone/Trend/Gan)` + `⏳ GAN CAO` + `🔥 HOT`; `gpt_analyzer.py:2229` vẫn bơm khi `prediction_mode=='HYBRID'` | **A3 — chờ 21/08** |
| **`WEEKDAY SCAN` chết** — SELECT cột `predicted_numbers` không tồn tại; prompt in `⚠️ SP-4.0 scan error` cho model đọc | **A4 — chờ 21/08** |
| **M4 không tái lập được** — bảng gốc đã bị lần đồng bộ 18:51 xoá | **A6 — làm được, đã làm** |

### 3.3 Bảng quy hoạch sáu mặt — câu cũ SAI hai chỗ · `VERIFIED_TEST`

*"BỘ ĐỒNG BỘ NĂM FILE — sửa một file là phải kiểm và sửa ba file kia"*:

| sai chỗ nào | sự thật |
|---|---|
| **sai số** | **sáu** mặt, không phải năm |
| **sai bản chất** | **7/97** mục có đủ cả sáu · **79** mục chỉ có ở MỘT mặt — và **đó là ĐÚNG thiết kế** |

Câu đó khiến phiên sau dễ đi *"sửa cho bằng"* rồi **phá mất 79 mục một-bản-duy-nhất**.

## 4. Hướng xử lý và vì sao chọn

**Gia hạn y như cũ thì vô nghĩa.** Cửa sổ 02→08/08 thất bại **không phải** vì 5 thứ cũ bị đụng —
mà vì **prompt bị đổi sáu lần**. Đóng băng thứ không ai đụng thì không mua được gì.
⇒ QD-041 **mở rộng phạm vi** sang `gpt_analyzer.py`.

**Mốc 21/08** trùng ngày chốt FU-284 ⇒ **một cửa sổ phục vụ cả ba phép đo** (FU-284 kết quả ·
FU-325 bầy đàn · FU-331 bộ đếm đo tiến) thay vì ba cửa sổ chồng nhau.

**Bảng quy hoạch: KHÔNG chép cho sáu mặt bằng nhau** — thế là phá thiết kế. Ghi rõ **vai trò
từng mặt** và ba luật: không cần giống nhau · **cấm để mất mục** · quy tắc MỚI vào đủ sáu.

**A3/A4 phải chờ** dù chúng là lỗi thật. Làm bây giờ là **phá cửa sổ đo lần thứ bảy** — đúng cái
owner vừa quyết chấm dứt.

## 5. Đã làm gì

| việc | kết quả |
|---|---|
| `docs/SO_SAU_LAN_DOI_PROMPT.md` | sổ sáu lần đổi, có commit + md5 + đường gỡ về |
| **QD-041** vào sổ quyết định | gia hạn 08/08 → **21/08**, phạm vi **+`gpt_analyzer.py`**; `QD-014` → `SUPERSEDED_BY_QD041` |
| **Bảng quy hoạch sáu mặt** | vào `CLAUDE.md` + 3 mặt sửa tay · băm khối `ad4bceb67be60018` **giống hệt** · hai mặt sinh tự động theo nguồn |
| **A5** | đính chính `84/84` → **`80/84`**, có script tái lập |
| **A6** | dựng lại M4 **tất định**, chạy hai lần ra y hệt |

### A5 — đo lại độc lập trên CSV tươi ở VPS

Local **cũ hơn VPS** (1,02 MB vs 1,53 MB) — đó là lý do hai lần đo trước ra hai số khác nhau.

```
KẾT QUẢ: 80/84 khoảng tin cậy CHỨA 0,50 · 4 KHÔNG chứa
  MN  convergence_score   AUC 0.4878  KTC [0.4774, 0.4982]
  MN  dow_sin             AUC 0.4819  KTC [0.4715, 0.4923]
  MT  dow_sin             AUC 0.4677  KTC [0.4569, 0.4784]
  MT  dow_cos             AUC 0.4791  KTC [0.4683, 0.4899]
```

**Kết luận M3 GIỮ NGUYÊN** — cả 4 khoảng lệch đều nằm **DƯỚI** 0,50, tức phân biệt được nhưng
**ngược hướng**. **Chỉ con số sai, không phải kết luận sai.**

### A6 — M4 dựng lại, tái lập được

Luật giả **tất định** từ `sha256(rule_key|date|i)`, so từng cặp cùng ngày bằng **McNemar**.

| giai đoạn | n | b (thật hơn) | c (giả hơn) | cặp lệch | z |
|---|---|---|---|---|---|
| `KHONG_XAC_MINH_DUOC` | 2.437 | 471 | 201 | 672 | **+10,41** |
| `KHONG_RO_LUAT` | 792 | 199 | 125 | 324 | **+4,11** |
| **`DO_TIEN`** | **0** | — | — | — | — |

## 6. Cổng kiểm

| phép | kết quả |
|---|---|
| băm khối **BẢNG QUY HOẠCH** × 4 mặt sửa tay | ✓ `ad4bceb67be60018` **giống hệt** |
| băm khối **§61 RM** × 6 mặt | ✓ `6e75ca884cfc77e0` giống hệt |
| `_v10925_rule_sync_check` | ✓ **SÁU MẶT ĐỒNG BỘ** |
| `_v11027_so_muc_quan_tri` (cổng mất mục) | ✓ **không mục nào biến mất** |
| A6 chạy **hai lần** | ✓ ra **y hệt** — tất định |
| cổng cắt cụt · ghi tệp · đoán tên | ✓ cả ba |
| 4 bảng khoá | **không đụng** — phiên này không ghi DB ngoài bảng shadow mới |
| prompt | **KHÔNG đụng** — `SP-4.4 · RR-16.5 · CTX-18.1 · PB-20.1` đứng yên |

## 7. Vướng vấp

**`QD-028` đã tồn tại** — agent suýt ghi đè lên quyết định cũ của owner (*"Một quy tắc cỡ mẫu
chung + hiệu chỉnh so sánh bội, N_min = 12"*). Kịch bản dừng lại vì có phép kiểm `if any(id ==
...)`, rồi đổi sang **`QD-041`** (số kế tiếp thật). **Nếu không có phép kiểm đó thì một quyết
định owner đã bị xoá.**

**Tệp quản trị dùng CRLF, mẫu trong script dùng LF** ⇒ `str.count()` ra 0 và phép thay **im lặng
không làm gì**. Phải thêm hàm hợp kiểu xuống dòng. Đây là kiểu hỏng không báo lỗi — cùng họ với
những lỗi đã ghi trong §61 RM.

## 8. Gỡ về

Phiên này **không deploy**, **không đụng prompt**, **không đụng 4 bảng khoá**.

```bash
git revert <commit>                          # tài liệu + bảng quy hoạch
# QD-041: đổi trang_thai về SUPERSEDED và khôi phục QD-014 → ACTIVE
# bảng shadow mới: DROP TABLE m4_doi_chung_v11028
```

## 9. Theo dõi tiếp

### LOCK-IN

| | |
|---|---|
| **L1** | Cửa sổ đo sạch **08/08 → 21/08**. `gpt_analyzer.py` **đóng băng**, `PB-20.1` đứng yên |
| **L2** | `80/84` KTC chứa 0,50 — **kết luận M3 giữ nguyên**, 4 cái lệch đều dưới 0,50 |
| **L3** | Sáu mặt quản trị **không cần giống nhau**; chỉ **cấm để mất mục** |

### OPEN ITEMS

| Mã | Việc | Trạng thái | Hạn |
|---|---|---|---|
| **FU-336** | Canh cửa sổ đóng băng không bị phá lần thứ bảy | `WAIT_LIVE` | **21/08** |
| **FU-337** | **A3 + A4** — hai lỗi thật trong prompt, bị đóng băng chặn | `BLOCKED` | **21/08** |
| **FU-338** | Đọc M4 nhóm `DO_TIEN` khi đủ ≥25 cặp lệch | `WAIT_LIVE` | 21/08 |
| **FU-331** | Xác minh lần đào 10/08 không xoá bằng chứng | `WAIT_LIVE` | **11/08** |
| **FU-335** | (đã làm ở V11028) bảng vai trò sáu mặt | `CLOSED_PASS` | — |
| **A2** | Cổng thăng hạng 55% dưới nền — 71/105 luật | **chờ owner ký** | — |
| **A7** | R7/R8 làm lại trên prompt VPS thật + 43% chưa động | chưa | — |

### NEXT ACTION — MỘT bước

**Sáng 11/08: chạy `FU-331`** — sau lần đào thật thứ Hai 10/08 00:30, đếm
`SELECT giai_doan, COUNT(*) FROM mined_rule_effectiveness GROUP BY 1`.
Số dòng **không được giảm** và `DO_TIEN` **không được về 0**. Đây là phép kiểm quyết định của A1;
sai một trong hai ⇒ gỡ về `backups/v11025_pre/` ngay.

---

**Điều owner cần biết:** `z = +10,41` trong bảng M4 **KHÔNG phải tin tốt**. Nó nằm ở nhóm
`KHONG_XAC_MINH_DUOC` — nhóm **chấm ngược**, đúng nhóm mà V11024 R2 đo được lift **1,084 trong
cửa sổ chọn** và **1,000 ngoài cửa sổ**. Luật thắng luật giả mạnh ở đây là **thiên vị chọn**,
không phải kỹ năng dự đoán. Con số đáng chờ là nhóm `DO_TIEN` — hiện **0 dòng local · 15 VPS**.
