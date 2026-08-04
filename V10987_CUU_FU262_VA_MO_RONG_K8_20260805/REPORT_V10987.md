# V10987 — CỨU `FU-262` KHỎI MỒ CÔI TRƯỚC BRIEFING SÁNG 05/08 + MỞ RỘNG PHÉP `K8`

> **Phiên:** V10987 · **Ngày:** 2026-08-05, ~00:2x → 00:5x (giờ Việt Nam)
> **Loại:** công cụ + tài liệu, chạy ở máy local
> **KHÔNG deploy · KHÔNG restart `lottery` · KHÔNG đụng đường ra số** (`QD-014` còn hiệu lực hết 08/08)

---

## 1. Tóm tắt một đoạn

`FU-262` đến hạn **05/08 (hôm nay)** nhưng đang **mồ côi** — nhãn `FIXED_PENDING_LIVE_VERIFY` là
nhãn **tự chế**, không nằm trong `TREO_STATUSES` (9 nhãn) lẫn `DONG_STATUSES` (7 nhãn) của
`_v10958_fu_reader`, nên mục rơi khỏi mọi bộ đếm và **briefing đầu phiên không hiện nó**. Phép
`K8` lẽ ra bắt được nhưng nó **chỉ soi 14 mã của nhóm lịch cuốn chiếu** nên vẫn báo ĐẠT — đây là
lỗi "xanh giả" **thứ 8** cùng họ, còn hở sau ngày 04/08. Phiên này: (1) trả nhãn hợp lệ cho **3
mục** mồ côi đến hạn trong 3 ngày tới — `FU-262` (05/08), `FU-250` (06/08), `FU-256` (06/08) —
đưa tổng mồ côi **18 → 15**; (2) mở rộng `K8` soi **toàn sổ** theo 3 phần, kèm **trần bậc thang**
`MO_COI_TRAN = 15` chỉ được hạ; (3) **thử ngược 3/3 ca đạt** — cổng TRƯỢT và **gọi đúng tên** mã
mồ côi, trong khi 7 phép còn lại vẫn ĐẠT. `FU-262` **đã hiện trong briefing** ở mục *"ĐẾN HẠN HÔM
NAY"*. Năm cổng kiểm đều đạt: hai cổng lịch **8/8**, sổ quyết định **0 TRÔI**, cổng báo cáo **bản
quét toàn bộ exit 0**.

---

## 2. Owner yêu cầu gì — nguyên văn

Phiên này nhận việc từ **agent cha**, không phải trực tiếp từ owner. Nguyên văn yêu cầu:

> *"Viec nho nhung gap: **cuu `FU-262` khoi tinh trang mo coi TRUOC briefing sang 05/08**, va
> **mo rong pham vi phep `K8`**."*

> *"`FU-262` den han 05/08 (HOM NAY) nhung dang MO COI → briefing dau phien **khong hien** no →
> nguy co troi mat dung cai kieu owner ghet nhat."*

> *"**Thu nguoc de chung minh cong co tac dung**: co tinh tao mot muc mo coi tam (hoac dung chinh
> trang thai truoc khi sua) → K8 phai **TRUOT** va **in dung ten ma** bi mo coi → roi tra lai
> trang thai dung. Ghi ket qua thu nguoc vao evidence. **Day la buoc bat buoc** — 4/9 loi xanh gia
> trong ngay 04/08 chi lo ra nho thu nguoc."*

> *"**Tra danh sach nhan hop le TRUOC khi ghi** — dung tao nhan la (V10981 tung gan `SCHEDULED`
> lam 11/14 muc thanh mo coi)"*

> *"Muc nao **den han trong 3 ngay toi (05-07/08)** thi **bo sung du truong ngay trong phien nay**
> de khong troi. Muc nao han xa hon thi gom vao `FU-258`"*

**Quyết định owner đứng phía sau phiên này** (đã có trong `docs/OWNER_DECISION_LEDGER.md`, §56 cấm
hỏi lại):

- **`QD-021`** (owner ký 04/08 10:29): *"Giãn ra cuốn chiếu tới hết ngày 10/08 phải hoàn thành,
  làm lần lượt những vấn đề nào xác thực rõ ràng, đơn giản làm trước tới cuối cùng 10/08 phải xong"*
- **`QD-014`** (đóng băng đường ra số tới hết 08/08) — phiên này **không chạm** 5 thứ bị cấm đích danh.
- **§56 (A54)** (owner ký 01/08 10:41): *"Anh không muốn nhắc tới nhắc lui hoài những vấn đề mà em
  có thể tra ra, có thể kiểm soát được đâu?"* — chính tinh thần của việc cứu mục mồ côi.

---

## 3. Đào bới / phát hiện

### 3.1 Vì sao `FU-262` vô hình

Bộ đọc sổ theo dõi `_v10958_fu_reader` chia nhãn thành hai bộ:

| Bộ | Số nhãn | Nhãn |
|---|---|---|
| `TREO_STATUSES` | 9 | `WAIT_LIVE` `OWNER_LOCK` `MEASURED_BUT_NOT_FIXED` `DEPLOYED_PENDING_LIVE_VERIFY` `AWAITING_OWNER_OK` `BLOCKED` `MEASURED_ROOT_CAUSE` `MEASURED_ROOT_CAUSE_FOUND` `DEPLOYED_PENDING_OWNER_VERIFY` |
| `DONG_STATUSES` | 7 | `CLOSED` `CLOSED_PASS` `CLOSED_FAIL` `CLOSED_REPORT` `RESOLVED` `DONE` `CANCELLED` |

Nhãn **ngoài cả hai bộ** = mục rơi khỏi mọi bộ đếm: không tính là treo, không bị kêu quá hạn,
không bị soi thiếu mã đọc — nhưng cũng chưa ai đóng. `FU-262` mang
`FIXED_PENDING_LIVE_VERIFY`, **không có trong bộ nào**.

Điểm quan trọng: `FU-262` **KHÔNG thiếu `ma_doc`, KHÔNG thiếu ô hạn, KHÔNG thiếu nhãn tiếng Việt**
— nó có đủ `SC0805`, `hạn 05/08`, `due 2026-08-05`. **Chỉ nhãn trạng thái sai.** Đây là điểm cần
nói rõ vì giả thuyết ban đầu (thiếu `ma_doc` §58 / thiếu ô hạn) **không đúng**.

### 3.2 Vì sao cổng `K8` không bắt được — đọc từ code

Bản `K8` trước phiên (`web/backend/_v10981_kiem_lich.py`):

```python
mo_coi = [f"{f}={(rows[f].get('status') or '?')}" for f in xep
          if f in rows and _la_mo_coi(rows[f].get("status"))]
```

`xep = {x["fu"]: x for x in LICH}` — **chỉ 14 mã** của nhóm lịch cuốn chiếu. `FU-262` không thuộc
nhóm 14 (nó là "tải sẵn của phiên khác" ngày 05/08) nên **không có trong `xep`** → K8 không soi →
**vẫn ĐẠT**. Cổng xanh trong khi mục đến hạn hôm nay đang trôi.

### 3.3 Đo tổng mồ côi — 18/145 mã

Dò bằng `web/backend/_v10987_probe.py` (chỉ đọc), mốc 05/08/2026:

| Mã | Nhãn | Hạn | Vì sao mồ côi |
|---|---|---|---|
| `FU-262` | `FIXED_PENDING_LIVE_VERIFY` | **05/08** | nhãn tự chế |
| `FU-250` | *(ô status RỖNG)* | **06/08** | khối cập nhật V10978 bỏ hẳn bảng `field`/`value` |
| `FU-201` | `READY_NOT_DEPLOYED` | 08/08 | nhãn cũ |
| `FU-205` | `READY_NOT_DEPLOYED` | 15/08 | nhãn cũ |
| `FU-256` | *(ô status RỖNG)* | *(không đọc được)* | khối V10979 chỉ ghi nhãn trong câu văn, tiêu đề **mất luôn chữ `hạn 06/08`** |
| `FU-001` | `[One` | — | nhãn rác từ bản mẫu |
| `FU-117` | `WAIT_CLOSEOUT` | — | nhãn V54 |
| `FU-119` | `READY_TO_BUILD_MEASUREMENT_ONLY` | — | nhãn V54 |
| `FU-121` `FU-122` | `READY_TO_BUILD_UI_TEST_ONLY` | — | nhãn V54 |
| `FU-129` | `READY_TO_BUILD_UI_TEST_ONLY` | — | nhãn V55 |
| `FU-150` | `DELIVERED_AUDIT_DOCS_ONLY` | — | nhãn V84 |
| `FU-151` | `DELIVERED_INVENTORY_DOCS_ONLY` | — | nhãn V85 |
| `FU-157` | `DELIVERED_DOCS_RECONCILIATION` | — | nhãn V91 |
| `FU-158` | `DELIVERED_DOCS_ONLY` | — | nhãn V92 |
| `FU-161` | `DEPLOYED_DOCS_ONLY` | — | nhãn cũ |
| `FU-171` | `FALSE_NEGATIVE` | — | kết luận đo dùng làm nhãn |
| `FU-173` | `DEFER` | — | hoãn có chủ ý |

**Cỡ mẫu: 145 mã FU trong sổ, 18 mồ côi (12,4%).** Phổ nhãn: 27 nhãn khác nhau đang dùng, trong đó
**11 nhãn** không thuộc bộ nào.

### 3.4 `FU-256` — mất cả nhãn LẪN hạn

Nặng hơn hai mục kia. Khối cập nhật V10979 đặt tiêu đề *"… — ĐÃ DỰNG CỔNG (cập nhật V10979)"*:
**bỏ bảng field** (chỉ ghi nhãn trong một câu văn), và tiêu đề **mất chữ `hạn 06/08`**. Kết quả:
`status=""` **và** `due_date=None` → mục vừa không nhãn vừa không hạn. Khối gốc V10978 (còn trong
sổ, phía dưới) ghi rõ `| **hạn** | 06/08 |` và `MEASURED_BUT_NOT_FIXED`, và mã đọc `DO0806` tự nó
đã nói hạn 06/08.

### 3.5 Việc còn thiếu thật của `FU-262` — đo lại bằng máy

Ngưỡng `FU-262` tự viết: *"tới 05/08 thêm một phép kiểm tính toàn vẹn giao diện (có đủ thẻ đóng ·
kích thước không tụt quá 10% so với lần trước) vào `_v10900_consistency_guard`"*.

Đọc `web/backend/_v10900_consistency_guard.py` hôm nay: có `C19_bien_han_du_rong` (480s) ·
`C20_bien_han_khong_troi` (720s) · `C21_co_thong_bao_da_xong` — **không phép nào kiểm tính toàn
vẹn file giao diện**. Ngưỡng **CHƯA THOẢ**. Đây là lý do mục phải giữ mở, không được đóng.

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 Nhãn mới cho `FU-262` — cân ba phương án

| Phương án | Vì sao chọn / loại |
|---|---|
| Thêm `FIXED_PENDING_LIVE_VERIFY` vào `TREO_STATUSES` | **LOẠI.** Nới bộ nhãn để cổng xanh là đúng loại "nới cổng cho đẹp". Nhãn này là biến thể thứ 4 của cùng một ý (`DEPLOYED_PENDING_LIVE_VERIFY` đã có) — thêm vào là nuôi thêm dị bản. |
| `DEPLOYED_PENDING_LIVE_VERIFY` | **LOẠI.** Nói quá: phần **chưa xong** của FU-262 là *dựng phép canh C22*, mà phép đó **chưa có trong code**, chưa deploy. Gọi là `DEPLOYED_*` là báo xanh sai. |
| **`MEASURED_ROOT_CAUSE`** | **CHỌN.** Nhãn hợp lệ, đúng sự thật: căn nguyên đã tìm ra và **file đã vá**, nhưng **phép canh chưa dựng** → phần HÀNH ĐỘNG chưa xong. |

### 4.2 Giữ hay dời hạn `FU-262`?

**GIỮ 05/08.** Lý do: (a) agent cha yêu cầu đích danh *"han 05/08"*; (b) dời hạn thì phải cập nhật
`_v10982_lich9.TAI_PHIEN_KHAC_DO_DUOC[05/08]` nếu không `J5` TRƯỢT; (c) quan trọng nhất — **dời hạn
để tránh quá hạn chính là cách giấu việc**. Giữ 05/08 nghĩa là nếu hết hôm nay chưa dựng `C22` thì
briefing 06/08 **sẽ bêu tên nó ở mục quá hạn**, và đó chính là tác dụng cần có.

### 4.3 Có nên dựng luôn `C22` trong phiên này?

**KHÔNG.** `_v10900_consistency_guard.py` chạy cron **18:05 trên VPS**; thêm phép vào nó là việc
**phải deploy**. Phạm vi phiên này được giao rõ: *"KHONG deploy, KHONG restart `lottery` — day la
phien cong cu chay o may local + tai lieu"*. Viết code rồi để đó không deploy là đúng loại "xanh
trên giấy" mà `FU-259` đang mở để canh. Nên: ghi rõ **xong nghĩa là gì (3 điều kiện đo bằng số)**
và **ngưỡng escalate**, để phiên có khe deploy làm tiếp.

### 4.4 Vì sao xử luôn `FU-256` dù hạn nó đọc ra `None`

Theo lệnh *"muc nao den han trong 3 ngay toi (05-07/08) thi bo sung du truong ngay"*, `FU-256` đọc
ra `hạn —` nên **về mặt máy** nó thuộc nhóm "hạn xa / không hạn" → đáng lẽ gom vào `FU-258`. Nhưng
**mã đọc `DO0806` và khối gốc V10978 đều nói hạn 06/08** — tức hạn thật nằm trong cửa sổ 3 ngày,
chỉ bị **mất do lỗi ghi**. Gom nó vào `FU-258` là hợp quy tắc nhưng **để lọt một mục đến hạn ngày
mai**. Chọn xử ngay.

### 4.5 Thiết kế `K8` mở rộng — vì sao không "0 mồ côi toàn sổ"

Cách đơn giản nhất là bắt `K8` đòi **0 mồ côi toàn sổ**. **LOẠI** vì còn 15 mục nhãn cũ thời
V54–V92 không thể phân loại trong một phiên đêm; cổng sẽ đỏ vĩnh viễn → thành cổng bị bỏ qua, tệ
hơn cổng xanh giả. Chọn **ba phần**, mỗi phần nhắm một rủi ro khác nhau:

| Phần | Đòi gì | Chặn rủi ro nào |
|---|---|---|
| (a) | nhóm 14 sạch | như cũ, không mất tác dụng đang có |
| (b) | **0 mồ côi quá hạn hoặc đến hạn trong 2 ngày tới** | **chính cái bắt được `FU-262`.** Mồ côi hạn còn xa thì còn thời gian phân loại; mồ côi hạn tới rồi là trôi mất thật |
| (c) | tổng ≤ `MO_COI_TRAN = 15`, **luôn in tên** | chặn mục mới rơi thành mồ côi (tổng vượt trần → TRƯỢT ngay), và không cho ai im lặng bỏ rơi thêm |

Phần (b) dùng **ngày thật** (`dt.date.today()`), không dùng mốc ghim 04/08 của K1–K7. Nghĩa là cổng
**tự siết dần theo thời gian**: ngày 06/08 cửa sổ thành 06→08/08, `FU-201` (08/08) rơi vào và cổng
đỏ — buộc phải xử trước khi nó thành nợ. Đó là tính năng, không phải bẫy: `FU-258` hạn 06/08 chính
là mục theo dõi việc phân loại này.

Trần (c) là **bậc thang chỉ được hạ**, ghi thẳng trong code kèm số trước/sau (18 → 15).

---

## 5. Đã làm gì

### 5.1 Bảng file × thay đổi

| File | Thay đổi | Kích thước |
|---|---|---|
| `docs/FOLLOW_UP_TRACKER.md` | khối V10987: 3 mục được trả nhãn hợp lệ + thân `FU-258` cập nhật danh sách 15 mồ côi đích danh | 1.100.786 → **1.112.128** ký tự (+11.342) |
| `CHANGELOG.md` | khối V10987 | 1.988.053 → **1.993.473** (+5.420) |
| `docs/CURRENT_TRUTH_SSOT.md` | khối V10987 | 957.491 → **959.983** (+2.492) |
| `docs/LICH_CUON_CHIEU_DEN_10082026.md` | **sinh lại từ máy** (không sửa tay) | **38.160 byte** · 247 dòng |
| `web/backend/_v10981_kiem_lich.py` | `K8` mở rộng 3 phần · thêm `--so` / `--hom-nay` để thử ngược | sửa |
| `web/backend/_v10982_lich9.py` | `TAI_PHIEN_KHAC_DO_DUOC[06/08]` += `FU-256` | sửa |
| `web/backend/_v10987_thu_nguoc_k8.py` | **mới** — bộ thử ngược 3 ca | mới |
| `web/backend/_v10987_ghi_so.py` | **mới** — ghi sổ, có cổng tự chặn nhãn tự chế | mới |
| `web/backend/_v10987_probe.py` | **mới** — dò mồ côi (chỉ đọc) | mới |
| `web/backend/_v10987_governance.py` | **mới** — prepend CHANGELOG + SSOT | mới |
| `artifacts/v10981_lich_cuon_chieu.json` · `artifacts/v10982_gian_9_muc.json` | sinh lại | 20.316 · 20.344 byte |

### 5.2 Ba mục được cứu — tra nhãn TRƯỚC khi ghi

`_v10987_ghi_so.py` có **cổng tự chặn**: đối chiếu nhãn định ghi với
`TREO_STATUSES ∪ DONG_STATUSES` và `sys.exit()` nếu là nhãn tự chế. Kết quả in ra:
`✓ tra trước khi ghi: 3/3 nhãn nằm trong danh sách hợp lệ`.

| Mã | Mã đọc §58 | Nhãn cũ | Nhãn mới | Hạn | Xong nghĩa là gì (đo bằng số) |
|---|---|---|---|---|---|
| `FU-262` | `SC0805` | `FIXED_PENDING_LIVE_VERIFY` | **`MEASURED_ROOT_CAUSE`** | **05/08** (giữ) | `_v10900_consistency_guard` có thêm `C22_giao_dien_toan_ven` kiểm 3 điều kiện trên `monitoring.html`: đủ `</script>` `</body>` `</html>` · kích thước không tụt > **10%** so với lần trước · còn ≥ **1** vòng `setInterval(`. Thử ngược trên bản cắt cụt cố ý phải cho `LECH` |
| `FU-250` | `KS0806` | *(rỗng)* | **`MEASURED_ROOT_CAUSE`** | **06/08** (giữ) | **3/3** tệp (`_v10861_runtime_contract_audit` · `_v10921_rule_a55` · `_v10958_fu_reader`) có docstring nói rõ mã thoát không mang nghĩa cổng — `grep -c` = **3** → đóng `CLOSED_PASS`. Nếu soát lại tìm ra ≥1 nơi đọc mã thoát → đi nhánh ngược, sửa cho thoát 1 khi trượt |
| `FU-256` | `DO0806` | *(rỗng)* | **`DEPLOYED_PENDING_LIVE_VERIFY`** | **06/08** (trả lại) | `C19` + `C20` có mặt và ra trạng thái (`OK`/`LECH`, không vắng) trong **≥2 ngày** liên tiếp (05 và 06/08). `OK` cả hai → `CLOSED_PASS` kèm biên thật MT/MB. Nền so: MT **10,8 phút** · MB **13,1 phút** (03/08) |

**Không mục nào bị dời hạn** → `K4`/`J4` không lệch.

### 5.3 Bảng mốc tải phải cập nhật cùng phiên

Trả lại hạn 06/08 cho `FU-256` làm nó xuất hiện trong `tai_phien_khac_that()`. Nếu không cộng vào
`TAI_PHIEN_KHAC_DO_DUOC[2026-08-06]` thì `J5` **TRƯỢT ngay** — đúng như thiết kế V10982b. Đã cập
nhật, và sinh lại trang lịch. Tải mỗi ngày sau phiên:

| Ngày | 04/08 | 05/08 | 06/08 | 07/08 | 08/08 | 09/08 | 10/08 |
|---|---|---|---|---|---|---|---|
| Tải thật | 3 | 5 | **7** ↑ | 5 | **6** ↑ | 8 | **3** |

06/08 lên 7 vì `FU-256` có lại hạn; 08/08 lên 6 vì `FU-267` (mở ở V10986). Ngày chốt 10/08 **không
đổi, vẫn 3 mục**.

### 5.4 Deploy

**KHÔNG deploy, KHÔNG restart `lottery`.** Phiên chỉ đọc/ghi file `.md` và `.py` ở máy local.

### 5.5 Hash 4 bảng khoá

**Không áp dụng theo nghĩa đo hash** — phiên này **không mở kết nối nào tới `lottery_ai.db`**, cả
local lẫn VPS. Không có đường ghi nào tới `predictions` · `final_bundles` · `lottery_results` ·
`model_daily_eval`. Bằng chứng gián tiếp: `QD-014` vẫn khớp **7/7** phép `kiem_code` sau phiên
(xem §6), và 7 phép đó chính là bộ canh đường ra số.

---

## 6. Cổng kiểm

Chạy **tách riêng từng lệnh** (gộp lại từng bị cắt mất kết quả):

| # | Lệnh | Kết quả | Thoát |
|---|---|---|---|
| 1 | `python web/backend/_v10920_session_start.py` | **`FU-262` hiện ở "ĐẾN HẠN HÔM NAY"** · mồ côi **18 → 15** · đến hạn hôm nay **4 → 5** · treo **99 → 102** · quá hạn **1** (`FU-225`, không đổi) | **0** |
| 2 | `python web/backend/_v10981_kiem_lich.py` | **ĐẠT 8/8** · `LICH_CUON_CHIEU_DAT` · K8 in đủ tên 15 mồ côi còn lại | **0** |
| 3 | `python web/backend/_v10982_kiem_lich9.py` | **ĐẠT 8/8** · `GIAN_9_MUC_DAT` · `J5` mốc tải khớp sổ thật **7/7 ngày** · `J8` mồ côi 15 (trước phiên 19, **giảm 4**) | **0** |
| 4 | `python web/backend/_v10920_decision_ledger.py` | **0 quyết định TRÔI** · 27 quyết định khớp `kiem_code` · `QD-014` **7/7** · `QD-025` **11/11** | **0** |
| 5 | `python web/backend/_v10921_report_gate.py` (**bản quét toàn bộ**) | mọi phiên bản đủ 9 phần và đã push | **0** |
| 6 | `python web/backend/_v10987_thu_nguoc_k8.py` | **THỬ NGƯỢC ĐẠT 3/3 ca** · `K8_CO_TAC_DUNG` | **0** |

### 6.1 THỬ NGƯỢC — bước bắt buộc, chi tiết

**Ca thật (chạy trên sổ CHƯA vá, đúng trạng thái đầu phiên):** `K8` **TRƯỢT**, thoát **1**, in:

```
MỒ CÔI ĐẾN HẠN ≤07/08: ['FU-262(05/08=FIXED_PENDING_LIVE_VERIFY)',
                        'FU-250(06/08=ô status RỖNG)'] ·
tổng toàn sổ 18 (trần 15) · danh sách: FU-262(05/08) FU-250(06/08) … FU-256(—)
```

**7 phép còn lại vẫn ĐẠT** (K1…K7) → việc mở rộng chỉ làm đúng một phép đổi trạng thái, không làm
đổ phép khác.

**Bộ thử ngược tái lập được** — `_v10987_thu_nguoc_k8.py` ghim ngày 05/08, sao sổ ra tệp tạm, cố ý
dựng lại tình huống mồ côi, rồi chạy **chính cổng thật** qua `--so` (không dựng lại phép kiểm):

| Ca | Dựng lại tình huống | Kỳ vọng | Thật | Có gọi đúng tên? |
|---|---|---|---|---|
| **A** | `FU-262` mang lại nhãn tự chế `FIXED_PENDING_LIVE_VERIFY` | thoát 1 · 7 phép ĐẠT | thoát **1** · **7** ĐẠT | **CÓ** — `FU-262(05/08=FIXED_PENDING_LIVE_VERIFY)` |
| **B** | `FU-256` bị xoá ô `status` (đúng như khối V10979 để lại) | thoát 1 · 7 phép ĐẠT | thoát **1** · **7** ĐẠT | **CÓ** — `FU-256(06/08=ô status RỖNG)` |
| **C** | sổ nguyên trạng đã vá | thoát 0 · 8 phép ĐẠT | thoát **0** · **8** ĐẠT | — |

**3/3 ca đúng kỳ vọng.** Bộ thử tự kiểm luôn rằng **sổ theo dõi THẬT không đổi một byte** trong
lúc chạy (`✓ sổ theo dõi THẬT không đổi một byte nào`). Bằng chứng:
`evidence/thu_nguoc_k8.json` · `evidence/thu_nguoc_k8_ketqua.txt` ·
`evidence/k8_thu_nguoc_TRUOC_khi_va.txt` · `evidence/k8_SAU_khi_va.txt`.

**Ca thứ tư — chạy cổng trên đúng bản `HEAD` của sổ** (`evidence/k8_chay_tren_ban_HEAD.txt`):
`_v10987_evidence.py` lấy bản sổ trước phiên bằng `git show HEAD:docs/FOLLOW_UP_TRACKER.md`
(**không chép tay, byte-exact**) rồi chạy cổng với `--so`. **Mã thoát = 1**, TRƯỢT đúng kỳ vọng.

### 6.3 Đối chiếu TRƯỚC / SAU — máy đo, không chép tay

`_v10987_evidence.py` chạy **chính các hàm đếm mà briefing dùng** (`treo_items` ·
`trang_thai_mo_coi` · `thieu_ma_doc`) trên **cả hai** bản sổ — bản `HEAD` và bản hiện tại.
Bằng chứng: `evidence/doi_chieu_TRUOC_SAU.json`.

| Chỉ số | TRƯỚC | SAU |
|---|---|---|
| **`FU-262` có trong "đến hạn hôm nay"** | **`False`** | **`True`** |
| **`FU-262` còn mồ côi** | **`True`** | **`False`** |
| Mồ côi toàn sổ | **18** | **15** |
| Mục theo dõi còn treo | 99 | **102** |
| Đến hạn hôm nay | 4 | **5** |
| Quá hạn | 1 | 1 (không đổi) |
| Tổng mã FU trong sổ | 145 | 145 (không mã nào mất) |
| Đã cứu | — | **`FU-250` · `FU-256` · `FU-262`** |

### 6.2 Điều KHÔNG kiểm được và nói thẳng

- **`C22` chưa dựng** → ngưỡng gốc của `FU-262` **chưa thoả**. Mục giữ mở, hạn 05/08.
- **13/15 mồ côi còn lại chưa phân loại** → theo dõi dưới `FU-258` (hạn 06/08).
- **Không đo hash 4 bảng khoá** vì phiên không mở kết nối DB nào (xem §5.5).

---

## 7. Vướng vấp

### 7.1 Giả thuyết ban đầu SAI — và hậu quả nếu tin theo

Yêu cầu đầu phiên đặt giả thuyết: *"xem no thieu gi ma bi mo coi (thieu `ma_doc` §58? thieu o han?
nhan khong nam trong `TREO_STATUSES`?)"*. Hai giả thuyết đầu **sai**: `FU-262` có đủ `SC0805` và
`hạn 05/08` / `due 2026-08-05`. Chỉ giả thuyết thứ ba đúng.

**Hậu quả nếu bỏ qua:** nếu ghi thêm `ma_doc` "cho đủ" mà không đổi nhãn thì mục **vẫn mồ côi** và
briefing vẫn không hiện — sửa xong vẫn hỏng, mà báo cáo lại ghi "đã bổ sung đủ trường". Đúng loại
"xanh giả" đang chữa.

### 7.2 Suýt để lọt `FU-256` — mục mất CẢ nhãn LẪN hạn

Theo đúng chữ của lệnh, `FU-256` đọc ra `hạn —` nên thuộc nhóm "gom vào `FU-258`". Nhưng mã đọc
`DO0806` và khối gốc V10978 đều nói **hạn 06/08**.

**Hậu quả nếu bỏ qua:** một mục đến hạn **ngày mai** bị đẩy sang danh sách "hạn xa", tiếp tục vô
hình. Cùng loại lỗi đang chữa, chỉ khác là **nặng hơn** vì mất cả hạn nên không bộ đếm nào — kể cả
phần (b) mới của `K8` — nhìn thấy được. **Bài học: đừng chỉ tin `due_date` máy đọc ra; đối chiếu
với `ma_doc` và khối gốc.**

### 7.3 Lỗi do chính agent gây ra trong phiên — bẫy regex `**status**`

Khối V10987 lúc đầu có câu văn giải thích: ``Bộ đọc chỉ nhận `| **status** |` hoặc
`- **Trạng thái:**` ``. Chuỗi đó chứa `**status**` **liền sau là dấu `|`**, đúng khớp regex
`_STATUS = \*\*status\*\*\s*\|\s*`?([^`|\n]+)`?`. Thử ngược ca B lộ ra ngay: khi xoá ô status thật,
bộ đọc **nhảy xuống câu văn** và lấy nhãn `= "hoặc"` thay vì rỗng.

Đã sửa: viết lại thành ``ô `**status**` trong bảng field, hoặc gạch đầu dòng `- **Trạng thái:**` ``
— bỏ dấu `|` liền sau. Chạy lại thử ngược: ca B in đúng `FU-256(06/08=ô status RỖNG)`.

**Hậu quả nếu bỏ qua:** không sai ngay hôm nay (ô status thật nằm **trước** câu văn nên `re.search`
lấy đúng), nhưng thành **bẫy nằm chờ**: phiên sau viết khối cập nhật thiếu bảng field thì bộ đọc
lấy nhãn `"hoặc"` — một nhãn tự chế mới, mồ côi thêm một mục, và **lần này còn khó tìm hơn** vì nó
đến từ chính câu văn tài liệu. Chính thử ngược bắt được, đúng như lệnh đã cảnh báo *"4/9 loi xanh
gia trong ngay 04/08 chi lo ra nho thu nguoc"*.

### 7.4 `desktop.ini` của Google Drive — `FU-266`, đã dọn trước khi push

Quét `.git` kho báo cáo công khai: **267 tệp `desktop.ini`** (`.git/objects/**` và **4 tệp trong
`.git/logs/refs/**`**). Chưa có tệp nào trong `.git/refs/` nên `git fetch` còn chạy được, nhưng đó
đúng là đường đi tới lỗi `fatal: bad object refs/desktop.ini` mà `FU-266` ghi. Đã xoá sạch **267 →
0**, `git fetch` **exit 0**.

**Hậu quả nếu bỏ qua:** `git fetch` chết → `origin/main` local đứng yên → cổng báo cáo so
`origin/main..HEAD` thấy rỗng và **báo xanh dù chưa push**. Vì vậy phiên này **không tin
`git status`**, mà xác minh bằng `git ls-tree -r origin/main` (xem §6 và mục cuối).

### 7.5 Bốn tệp `desktop.ini` **được Git theo dõi** trong kho công khai

`git status` kho công khai báo 4 tệp `desktop.ini` **đã commit từ trước** (trong
`V105_25_STATION_ALIAS_FIXUP_20260511/` và `V105_27_TOTAL_FORCE_CONTROL_20260511/`) đang bị sửa.
**Không stage, không commit** — không thuộc phạm vi phiên, và lệnh cấm `git add -A`. Ghi lại để
phiên sau biết: đây là rác Google Drive **đã lọt vào lịch sử Git**, cần một mục dọn riêng.

### 7.6 PowerShell không có `find` / `tail` / `wc`

Lệnh gợi ý `find .git -name desktop.ini -delete` là cú pháp Unix; trên PowerShell nó gọi
`Out-File` và lỗi `Could not find a part of the path 'E:\dev\null'`. Đã đổi sang
`Get-ChildItem -Recurse -Force -Filter desktop.ini | Remove-Item -Force`.

---

## 8. Gỡ về

Phiên **không đụng runtime**, gỡ về chỉ là gỡ tài liệu và hai tệp công cụ:

```bash
cd E:\Lottery_AI_Test
git checkout HEAD -- docs/FOLLOW_UP_TRACKER.md docs/CURRENT_TRUTH_SSOT.md CHANGELOG.md
git checkout HEAD -- docs/LICH_CUON_CHIEU_DEN_10082026.md
git checkout HEAD -- web/backend/_v10981_kiem_lich.py web/backend/_v10982_lich9.py
del web\backend\_v10987_*.py
python web/backend/_v10920_session_start.py    # phải về lại 18 mồ côi
python web/backend/_v10981_kiem_lich.py        # phải về lại 8/8 (K8 bản chỉ soi 14 mã)
```

**Thời gian gỡ: dưới 1 phút.** Không cần restart service, không cần deploy, không cần khôi phục DB.

Bản sao lưu liên quan có sẵn từ phiên trước: `backups/v10979_pre/monitoring.html.cut_20260804_100331`
(bản `monitoring.html` cắt cụt 262.144 byte, để đối chứng nếu cần dựng `C22`).

---

## 9. Theo dõi tiếp

| Mã | Mã đọc | Nhãn | Hạn | Ngưỡng hành động bằng số |
|---|---|---|---|---|
| **`FU-262`** | `SC0805` | `/monitoring` từng bị cắt cụt mà không cổng nào biết | **05/08** | Hết ngày 05/08 chưa có `C22_giao_dien_toan_ven` trong `_v10900_consistency_guard.py` **trên VPS** → mục QUÁ HẠN, briefing 06/08 bêu tên. Quá hạn ≥2 ngày (tới 07/08) → chuyển `BLOCKED` + ghi `DECISION_LOG.md` xin owner một khe deploy |
| **`FU-250`** | `KS0806` | Soát nốt cổng còn thoát 0 khi trượt | **06/08** | `grep -c` docstring "mã thoát không mang nghĩa cổng" trên 3 tệp = **3** → `CLOSED_PASS`. Tìm ra ≥1 nơi đọc mã thoát → sửa cho thoát 1 khi trượt |
| **`FU-256`** | `DO0806` | Biên giờ chốt MT/MB co lại | **06/08** | `C19` + `C20` ra trạng thái (không vắng) **≥2 ngày** liên tiếp 05–06/08. `OK` cả hai → `CLOSED_PASS` kèm biên thật. Có `LECH` → dời lượt vá muộn thêm 2 phút |
| **`FU-258`** | `KS0806-1` | Cổng đếm giấu mất hạn và giấu mục mồ côi | **06/08** | `K8` cho **tổng mồ côi ≤ 2** (chỉ còn `FU-201` `FU-205` chờ hết đóng băng) và hạ `MO_COI_TRAN` **15 → 2** cùng phiên |
| `FU-201` | `TDLX-201` | Canh bộ lọc combo-super sau khi mở pool | 08/08 | **`QD-014` chặn** tới hết 08/08 — không được động trước 09/08 |
| `FU-205` | `TDLX-205` | Bộ lọc chấm bạch thủ | 15/08 | cùng vùng đóng băng |
| `FU-266` | `DD1208` | Google Drive đẻ `desktop.ini` vào `.git` | 12/08 | Thêm: **4 tệp `desktop.ini` đã lọt vào lịch sử Git** kho công khai (`V105_25_…`, `V105_27_…`) — cần `git rm --cached` + `.gitignore` |

### 9.1 Việc phiên sau phải làm ngay (hạn 05–06/08)

1. **Dựng `C22_giao_dien_toan_ven`** trong `_v10900_consistency_guard.py` + deploy + thử ngược trên
   bản cắt cụt `backups/v10979_pre/monitoring.html.cut_20260804_100331` → đóng `FU-262`.
2. **Phân loại 13 nhãn cũ** (3 họ: `READY_TO_BUILD_*` 4 mục · `DELIVERED_*`/`DOCS_ONLY` 5 mục ·
   một-nhãn-một-mục 4 mục) — hoặc thêm làm bút danh vào `TREO_STATUSES`/`DONG_STATUSES` như V10980
   đã làm với 3 nhãn, hoặc viết lại nhãn từng mục → hạ `MO_COI_TRAN` 15 → 2 → đóng `FU-258`.

### 9.2 Hạn rà soát cổng mới

`K8` phần (b) dùng **ngày thật** nên tự siết dần: **06/08** cửa sổ thành 06→08/08 và `FU-201`
(08/08) rơi vào → cổng sẽ ĐỎ nếu chưa phân loại. Đây là hành vi có chủ ý, cùng hạn với `FU-258`.
Nếu đến 06/08 chưa xử được thì phải **nói thẳng trong báo cáo phiên đó**, không được nới cửa sổ.
