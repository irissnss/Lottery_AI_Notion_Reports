# REPORT V11038 — NHẬN LỘ TRÌNH 10 NGÀY (QD-047) + VÁ 64 MỤC MẤT HẠN

**Ngày:** 2026-08-08 khuya · **Loại:** nhận lộ trình + fix tooling · **CHỈ ĐỌC DB**

---

## 1. Tóm tắt

| | |
|---|---|
| **⚠ Va chạm mã** | Brief ký `QD-046` — **đã dùng lúc 20:10**. Lộ trình ghi thành **`QD-047`**. **Lần thứ BA trong hai ngày** |
| **FU-370** | **64 mục** treo mất hạn — không phải 2 như tưởng sáng nay. Đã vá, còn **57** |
| **FU-372** | Hai phiên **cùng dùng số V11037**. Kiểm md5: bản vá **còn nguyên**, không mất gì |
| **GĐ-0 V1** | **ĐẠT** — 0 lượt hỏng SAU deploy |

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

> PROMPT TỔNG LỰC LẦN 2 — LỘ TRÌNH 10 NGÀY (08/08 → 18/08) "CẢI TIẾN THẬT · NĂNG LỰC THẬT ·
> TỪ DỄ ĐẾN KHÓ" … OWNER SIGNATURE: QD-046 … NUMBERING: … quyết định từ QD-046.
> QD-043/QD-044 đã dùng — cấm tái sử dụng mã.

---

## 3. Đào bới / phát hiện

### 3.1 ⚠ Va chạm mã NGAY TRONG BRIEF — lần thứ BA

Brief ký `QD-046`. Nhưng **`QD-046` đã dùng lúc 20:10 cùng ngày** cho mở khoá `NO_ANSWER`
(FU-355). Ghi đè là **mất một quyết định của owner**.

| lần | brief cấp | thực tế |
|---|---|---|
| 07/08 | `QD-028` | đã dùng — bắt kịp nhờ phép kiểm trong script |
| 08/08 sáng | `QD-043` | đã dùng cho ngưỡng FU-284 ⇒ ghi `QD-044` |
| **08/08 khuya** | **`QD-046`** | **đã dùng cho NO_ANSWER ⇒ ghi `QD-047`** |

Brief nói *"QD-043/QD-044 đã dùng"* nhưng **bỏ sót `QD-045` và `QD-046`** — cả hai cũng đã dùng
tối 08/08.

**`FU-369` (cổng cấp số hiệu quét BA nơi) chính là thứ sinh ra để chặn việc này — và nó CHƯA
được dựng.** Ba lần trong hai ngày là đủ: nhắc suông đã thất bại, phải là cổng máy.

### 3.2 FU-370 — hạn im lặng biến mất: **64 mục**, không phải 2

Sáng nay vá `FU-353` (2 mục). Tối nay đo lại: **64 mục treo** không có hạn.

**Cơ chế:** `FOLLOW_UP_TRACKER.md` ghi mới ở **ĐẦU** tệp ⇒ *"lần nhắc mới nhất"* = lần đầu gặp.
`load_fu_latest()` lấy lần đó rồi **vứt hết lần cũ**. Vậy **nhắc lại một mã FU trong khối phiên
bản sau mà không chép lại hạn = XOÁ HẠN**.

**Nạn nhân gồm chính agent:** `FU-341` · `FU-344` · `FU-345` · `FU-355` — đều đã ghi hạn rõ ở
khối gốc rồi bị **chính agent nhắc lại làm mất**.

**Và agent phạm đúng lỗi đó ngay tối nay:** `FU-357`/`FU-360` tạo lúc 20:25 **không có hạn trong
tiêu đề** — vài giờ sau khi vừa vá đúng lỗi này cho FU-317/FU-325.

### 3.3 Phiên song song — cùng dùng số V11037

`207404c` (20:16, lane G2-MB) và `dec1c33` (20:25, FU-357) **cùng mang số V11037**.
Kiểm md5 toàn bộ: `_v10879_nghiemthu_lane.py` `40e269c8…` · `combo_super.py` `1c477876…` ·
`gpt_analyzer.py` `c60ab13b…` — **local = VPS cả ba**. `NGUONG_P` và `assert both_lose >= 0`
**còn nguyên**. **Không mất gì.**

---

## 4. Hướng xử lý và vì sao chọn

**4.1 — Ghi `QD-047`, KHÔNG ghi đè `QD-046`.** Ghi đè là mất một quyết định của owner. Nêu rõ
chỗ lệch trong `ghi_chu` để owner xác nhận lại mã.

**4.2 — Kế thừa hạn thay vì bắt viết lại.** Luật đúng: lần nhắc sau **không lặp hạn** là **cập
nhật nội dung**, không phải **xoá hạn**. Bắt mọi khối phải chép lại hạn là đẩy gánh nặng sang
người viết và sẽ hỏng lại ngay lần sau.

**4.3 — Hạn MỚI luôn thắng.** Kế thừa **chỉ** khi lần mới nhất **không có** hạn — nếu không thì
việc dời hạn sẽ bị bản cũ đè lên, hỏng ngược.

**4.4 — KHÔNG tự đặt hạn cho 57 mục còn lại.** Chúng **chưa từng có hạn ở bất kỳ lần nhắc nào**
(FU-165 … FU-209, toàn mục cũ). Agent tự đặt hạn là **RM-06** — đặt hạn cho có. Đó là việc phải
hỏi owner.

**4.5 — Đọc V1 theo Ý ĐỊNH, không theo chữ.** Brief viết *"số lượt = 64 phải BẰNG 0"*. Tính cả
ngày 08/08 thì **là 12**, nhưng cả 12 đều **trước** deploy. Điều kiện thật cần kiểm là **0 lượt
SAU deploy** — và điều đó **ĐẠT**. Đọc chữ theo nghĩa đen sẽ dừng lộ trình một cách vô lý.

---

## 5. Đã làm gì

**TRƯỚC:** `load_fu_latest()` lấy lần nhắc mới nhất, vứt hết lần cũ ⇒ **64 mục treo** không hạn;
`FU-357`/`FU-360` (do chính agent tạo) cũng không hạn.
**SAU:** hạn **kế thừa** từ lần nhắc cũ hơn khi lần mới nhất không ghi; mã đọc §58 kế thừa theo
cùng luật; hạn mới **luôn thắng**.
**PHIÊN BẢN:** V11038 · 08/08/2026 · `_v10958_fu_reader.py` — sao lưu `backups/v11038_pre/`.
**KIỂM:** `python web/backend/_v11038_kiem_han_ke_thua.py` → `HAN_KE_THUA_V11038=DAT`

| | TRƯỚC | SAU |
|---|---|---|
| mục treo thiếu hạn | **64** | **57** |
| hạn kế thừa lại được | 0 | **16** |
| briefing «đến hạn hôm nay» | 9 | **12** |

Sửa thêm tiêu đề `FU-357` (`hạn 19/08`) và `FU-360` (`hạn 14/08`) — lỗi của chính agent.
Ghi **QD-047** cho lộ trình 10 ngày.

### Cổng `_v11038_kiem_han_ke_thua.py` — 4 phép, thử trên sổ GIẢ

| phép | kết quả |
|---|---|
| kế thừa hạn khi lần mới nhất không ghi | ✓ `FU-901 due=2026-09-01` |
| **hạn MỚI thắng, kế thừa không đè lên** | ✓ `FU-902 due=2026-09-30` |
| mã đọc §58 cũng kế thừa | ✓ `AB0109` |
| số mục thiếu hạn **không tăng** (trần 57) | ✓ |

Thử trên **thư mục tạm**, sổ thật **không bị đụng** ⇒ không cần khôi phục.

### GĐ-0 · V1 — ĐẠT

08/08: **12 lượt** `context_pack_chars=64`, **tất cả ở 05:17–05:41 tức TRƯỚC deploy V11032**
(10:27:34). Sau deploy **0 lượt** · 16h min **10.584** · 17h min **15.474**.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| Tuổi dữ liệu | **ĐẠT** |
| `HAN_KE_THUA_V11038` | **ĐẠT** — 4/4 |
| `KIEM_CHEO_QD` | **SACH** — sau khi ghi QD-047 |
| `DONG_BANG_QD041` | **CON_NGUYEN** |
| `DECIDE_V11037` · `NO_ANSWER_V11036` | **ĐẠT** |
| md5 local = VPS (3 tệp then chốt) | **ĐẠT** |
| 4 bảng khoá | **không đụng** — V11038 không ghi DB |
| Số hiệu mới | `QD-047` · `FU-370/371/372` — **quét trước khi cấp** |

---

## 7. Vướng vấp

**7.1 — Agent phạm ĐÚNG lỗi vừa vá, cách nhau vài giờ.** Sáng vá FU-353 (mục mất hạn); tối tạo
`FU-357`/`FU-360` **không có hạn**. Vá một cơ chế không tự động sửa được **thói quen viết**.
Đó là lý do phải có **cổng**, không phải chỉ có bản vá.

**7.2 — Bẫy CRLF lại chặn một lần.** `str.replace` khớp **0 lần** vì tệp dùng CRLF còn mẫu dùng
LF — đúng bẫy `CLAUDE.md` đã ghi. Phải dùng công cụ sửa hiểu ngữ cảnh thay vì thay chuỗi thô.

**7.3 — Brief tự mâu thuẫn về mã.** Nói *"cấm tái sử dụng mã"* rồi cấp một mã **đã dùng**. Agent
**không im lặng làm theo** — ghi `QD-047` và nêu rõ. Nếu owner muốn mã khác, sửa được ngay.

**7.4 — Lộ trình đặt GĐ-0 vào «sáng 09/08»**, nhưng V1 là **chỉ đọc** và là **cổng chặn của mọi
thứ sau nó** ⇒ chạy luôn tối 08/08. Không có lý do gì để một phép chỉ đọc phải chờ tới sáng.

---

## 8. Gỡ về

```bash
cp backups/v11038_pre/_v10958_fu_reader.py web/backend/
# QD-047: xoá mục khỏi docs/OWNER_DECISION_LEDGER.json
# tiêu đề FU-357/FU-360: khôi phục từ commit dec1c33
```

`_v10958_fu_reader.py` là **thư viện local**, **không có trên VPS** ⇒ không cần deploy, không
cần restart.

---

## 9. Theo dõi tiếp

| mã | nhãn | hạn | trạng thái |
|---|---|---|---|
| **FU-370 · SC0908-3** | hạn im lặng biến mất — đã vá, 09/08 kiểm briefing | 09/08 | `DEPLOYED_PENDING_LIVE_VERIFY` |
| **FU-371 · HT0809** | va chạm mã lần thứ ba — **FU-369 chưa dựng** | 09/08 | `MEASURED_ROOT_CAUSE` |
| **FU-372 · KS0809** | hai phiên cùng số V11037 | 09/08 | `MEASURED_BUT_NOT_FIXED` |
| **FU-360 · SC1408-2** | `verify_prediction` không lọc `run_source` | 14/08 | `MEASURED_BUT_NOT_FIXED` |

### LOCK-IN

- Lộ trình 10 ngày = **`QD-047`**, không phải QD-046
- Hạn của mục theo dõi **không còn im lặng biến mất** — có cổng chặn
- Bản vá V11036/V11037 **còn nguyên** sau phiên song song, md5 local = VPS
- **GĐ-0 V1 ĐẠT** ⇒ được sang GĐ-1

### OPEN — cần owner một dòng

1. **Xác nhận mã `QD-047`** cho lộ trình (thay `QD-046` trong brief).
2. **57 mục chưa từng có hạn** (FU-165 … FU-209) — đóng hàng loạt hay cấp hạn? Agent **không tự
   đặt** (RM-06).

### NEXT ACTION — một bước

**Dựng `FU-369`: cổng cấp số hiệu quét BA nơi (số V · mã FU · mã QD), kèm thử allow/deny.**
Ba lần va chạm trong hai ngày, và lần thứ ba nằm ngay trong brief của chính owner.
Đây là mục GĐ-1 số 3, hạn 11/08 — nhưng nên làm **trước tiên** vì mọi mục sau đều cấp mã mới.
