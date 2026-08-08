# REPORT V11032 — VÁ LỖI CÂM 67 NGÀY + HAI CỔNG MỚI

**Ngày:** 2026-08-08 · **Loại:** fix + gate · **Owner ký:** QD-042 (mở khoá) · QD-043 (ngưỡng FU-284)

---

## 1. Tóm tắt

Owner trả lời ba câu agent hỏi sáng nay:

| câu | owner chọn | hệ quả |
|---|---|---|
| 1 · FU-341 | **(a) mở khoá vá ngay** | vá 3 chỗ, `CTX-18.1 → CTX-18.2`, cửa sổ đo tính lại từ 09/08 |
| 2 · FU-343 | *"chưa rõ là vấn đề gì"* | agent dựng **bộ kiểm quyết định × quyết định** đầu tiên của kho + diễn giải |
| 3 · FU-344 | **giữ hạn 21/08** | ngưỡng phải đổi **5 → 9,33 điểm**, script đã commit trước ngày chốt |

**Và chính cổng nghiệm thu của việc vá lại lôi ra một lỗi CÙNG HỌ, PHẠM VI RỘNG HƠN** —
`⚠️ SP-4.0 scan error` bơm vào prompt của **cả 15 model official**, không phải 1.
**Chưa vá — cần chữ ký riêng.** Đây đúng **RM-07**.

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

> 1/ (a) mở khoá vá ngay
> 2/ chưa rõ là vấn đề gì cần diễn giải cụ thể
> 3/ giữ hạn

---

## 3. Đào bới / phát hiện

### 3.1 Vá BA chỗ, không phải một

Ba chỗ là **ba lớp của cùng một lỗi**: hỏng · không kêu · không ai bắt.
Vá mình chỗ 1 thì **lần vỡ SAU vẫn câm y hệt**. Đó là §60 *"cấm bỏ nửa chừng"*.

| # | vai | chỗ | TRƯỚC | SAU |
|---|---|---|---|---|
| 1 | **GỐC** | `:4761` | mở **10** biến cho `rules` **11 cột** ⇒ `ValueError` | mở **11** biến |
| 2 | **CÂM** | `:5576` | `except: return f"…Lỗi: {e[:60]}"`, **không in gì** | in đủ vết + `traceback` + trả **cờ** `CTX_PACK_LOI` |
| 3 | **MÙ** | `:6271` | `if _ctx_pack and len(_ctx_pack) > 50:` | bắt **cờ** trước, rồi `> CTX_PACK_SAN` (**500**) |

**Vì sao chèn `_r_legacy`:** bản hỏng thiếu **đúng một** biến giữa `_r_sc` và `_r_tier` —
`legacy_score`. Chèn vào đúng khe đó ⇒ **mọi tên còn lại giữ nguyên ý nghĩa**, không phải sửa
một dòng nào phía dưới. `_cls_state(_r_hr12, _r_hr4, _r_hr16, _r_verdict)` vẫn đúng.

Chọn cách này thay vì đổi tên loạt biến vì **ít bề mặt sai nhất** — đúng tinh thần QD-018.

### 3.2 Quét ngược (§60.3) — phân loại, không đếm chuỗi thô

| loại | kết quả |
|---|---|
| ai gọi `build_context_pack` trong **production** | **đúng 1** — `gpt_analyzer.py:6265`. Còn lại backup/audit, đều `shadow_mode=False` |
| ai dựa vào chuỗi báo lỗi **CŨ** | **0** |
| ai dùng ngưỡng `> 50` cho ngữ cảnh | **0** ngoài chỗ vừa sửa |
| ai đọc `context_pack_chars` | 6 nơi — chỉ **tổng hợp/hiển thị**; nay nhận **0** thay vì 64 khi vỡ ⇒ **thật hơn** |

### 3.3 ⚠ RM-07 — A4 CÒN SỐNG VÀ RỘNG HƠN

Cổng nghiệm thu in ra ở **cả 6 ô**, kể cả `shadow_mode=False`:

```
⚠️ SP-4.0 scan error: no such column: predicted_numbers
```

`gpt_analyzer.py:5384` SELECT cột `predicted_numbers` — **không tồn tại** (cột thật
`main_numbers`). `:5475` bắt lỗi rồi **`sections.append(...)`** ⇒ **bơm thẳng vào prompt**.

| | FU-341 (vừa vá) | A4 / FU-345 |
|---|---|---|
| model dính | **1** (`gpt-oss-120b`) | **cả 15 official** |
| tần suất | 42,9% số lượt | **mọi miền, mọi ngày** |
| chế độ | chỉ `shadow_mode=True` | **cả hai chế độ** |

**Không vá.** `QD-042` chỉ mở khoá cho FU-341, và tự ghi *"cấm dùng làm cớ mở khoá cho lần sửa
SAU"*. Cần chữ ký riêng.

### 3.4 Câu 2 — vấn đề FU-343 là gì, nói cho cụ thể

Ba mảnh giấy dán trên cùng một cái tủ lạnh, **không mảnh nào bị gỡ xuống**:

| ngày | mã | owner nói | chiều | trạng thái trong sổ |
|---|---|---|---|---|
| 01/08 | `OD-20260801-D` | *"Chờ ít nhất 7 ngày… rồi mới động tiếp"* | **ĐÓNG** | `ACTIVE` |
| 02/08 | `QD-014` | *"cần một tuần yên"* | ĐÓNG | `SUPERSEDED_BY_QD041` ✓ |
| 05/08 | `QD-029` | *"vướng mắc 2: **mở** nha em"* | **MỞ** | `ACTIVE` |
| 08/08 | `QD-041` | *"gia hạn thêm để đo đạt kỹ hơn"* | **ĐÓNG** tới 21/08 | `ACTIVE` |

Owner **ký đúng ở từng thời điểm** — đóng, rồi mở, rồi đóng lại. Không có gì sai ở đó.
**Sai ở chỗ SỔ không ghi mảnh nào đã bị mảnh nào thay.** Ai tra sổ hôm nay sẽ thấy **ba câu
trả lời** cho một câu hỏi, hai trong ba đã hết hiệu lực.

**Lỗi lược đồ:** sổ có **34 trường**, **không trường nào** là `thay_boi`/`superseded_by`.
`QD-014` phải nhét quan hệ ấy vào **trạng thái** (`SUPERSEDED_BY_QD041`) — nên chỉ đúng một mục
làm được, và máy không lần ngược được.

**Nó đã gây hại thật, không phải rủi ro giả định:** cả **sáu** lần đổi prompt (V11001…V11022)
đều diễn ra **SAU** khi `QD-029` mở khoá ⇒ trên giấy đều hợp lệ. Nhưng chính sáu lần đó phá hỏng
cửa sổ đo và buộc phải ký `QD-041`. Nếu sổ có nói *"QD-029 thay OD-D, và nó mở đúng những gì"*
thì việc *"đổi sáu lần trong một cửa sổ mở"* đã lộ ra sớm hơn nhiều.

---

## 4. Hướng xử lý và vì sao chọn

**4.1 — Vá ba chỗ chứ không một.** Xem 3.1.

**4.2 — Nâng `CTX-18.1 → CTX-18.2`, ba lớp kia đứng yên.** Bản vá **đổi thật** nội dung prompt
cho nhóm shadow-gate (64 → ~13.000 ký tự). Không nâng số phiên bản là để phép đo FU-284 không
phân biệt được trước/sau. Chỉ nâng **lớp ngữ cảnh** vì chỉ nó đổi.

**4.3 — Cổng đóng băng dời BẢN KHOÁ, không huỷ cửa sổ.** `QD-042` **không huỷ** `QD-041`:
cửa sổ vẫn tới 21/08, chỉ cho **đúng một** commit mang chữ `V11032`; commit khác đụng
`gpt_analyzer.py` vẫn là **phá cửa sổ**.

**4.4 — Không vá A4 dù đã thấy rõ.** Owner mở khoá cho FU-341, không cho cả họ lỗi. Vá thêm là
**tự nới chữ ký** — đúng thứ `QD-042` cấm ở dòng `khong_duoc`.

**4.5 — Ngưỡng FU-284 phải đổi vì owner giữ hạn.** Ngưỡng cũ *"≥5 điểm"* cần **44–50 ngày**;
cửa sổ 14 ngày chỉ thấy **≥9,33 điểm**. Giữ hạn thì **không giữ được ngưỡng** — hai thứ không
cùng tồn tại.

---

## 5. Đã làm gì

**TRƯỚC:** `gpt_analyzer.py` md5 `6b28f0baa7aeceac0e9fd2b75a741a81`, `CTX-18.1`,
`build_context_pack(shadow_mode=True)` trả **64 ký tự** ở MN và MB.
**SAU:** md5 **`e6578ff6564632ec017dc746078540db`**, `CTX-18.2`, trả **13.199 / 12.775 ký tự**.
**PHIÊN BẢN:** V11032 · 08/08/2026 · `SP-4.4 · RR-16.5 · CTX-18.2 · PB-20.1`.
**KIỂM:** `python web/backend/_v11032_kiem_va.py`

| miền | shadow=False | shadow=True TRƯỚC | shadow=True SAU |
|---|---|---|---|
| MN | 9.935 | **64** ✗ | **13.199** ✓ |
| MT | 9.948 | 12.927 ✓ | 12.927 ✓ |
| MB | 9.610 | **64** ✗ | **12.775** ✓ |

### Bốn tệp mới

| tệp | việc |
|---|---|
| `_v11032_kiem_va.py` | **cổng nghiệm thu** — chạy hàm production, 3 miền × 2 chế độ, mã thoát 1 nếu còn vỡ |
| `_v11033_verdict_fu284.py` | **bộ tính verdict** — ngưỡng ghi bằng số **trong tệp**, commit **trước** ngày chốt |
| `_v11034_kiem_cheo_quyet_dinh.py` | **bộ kiểm quyết định × quyết định** — cái đầu tiên của kho |
| `_v11032_deploy.py` | deploy có so md5 hai đầu + so PID + nghiệm thu **trên chính máy chủ** |

### Ngưỡng FU-284 đã đăng ký (QD-043)

```
TRUOC = ("2026-07-23", "2026-08-05")   # prompt đứng yên · n = 214/miền
LOẠI  =  2026-08-06 → 2026-08-08       # đổi 6 lần + vá V11032
SAU   = ("2026-08-09", "2026-08-21")   # CTX-18.2 đứng yên
NGUONG_DIEM = 9.33 · NGUONG_Z = 1.96 · N_TOI_THIEU = 150 · VIF = 2.92
```

So **lệch-so-với-nền** của hai cửa sổ, **không so tỉ lệ thô** — nền hai cửa sổ khác nhau vì số
đài mỗi thứ khác nhau.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| Cú pháp + đọc lại sau ghi | **ĐẠT** — `ast.parse` + so nguyên văn |
| Tệp không ngắn đi | **ĐẠT** — 349.979 → 351.765 ký tự |
| `_v11032_kiem_va.py` (local) | **ĐẠT** — `VA_V11032=DAT`, 6/6 ô |
| `_v11032_kiem_va.py` (**trên VPS**) | **ĐẠT** |
| `_v11028_cong_dong_bang.py` | **ĐẠT** — `DONG_BANG_QD041=CON_NGUYEN`, bản khoá CTX-18.2 |
| md5 local = VPS, 5 tệp | **ĐẠT** |
| PID trước/sau | **ĐỔI** — `1004216` → PID mới |
| `/api/health` | **200** |
| 4 bảng khoá trước/sau | **GIỮ NGUYÊN** |
| Không đưa runtime artifact | **ĐẠT** — script tự chặn `.db .jsonl .log .bak` |

---

## 7. Vướng vấp

**7.1 — Neo vá trượt hai lần.** `PROMPT_VERSIONS = {` xuất hiện **2 lần**; `CTX_PACK_LOI` đếm ra
**4** chứ không phải 3 (1 định nghĩa + 1 chỗ trả + **2** chỗ ở cổng canh). Cả hai lần đều **dừng
trước khi ghi** nhờ `assert`, nên tệp không hỏng. Đây là lý do cổng phải nằm **trước** `os.replace`.

**7.2 — Bộ kiểm quyết định dựng SAI HAI LƯỢT.**

| lượt | sai gì | vì sao |
|---|---|---|
| 1 | bắt **thừa** `QD-020/021/022` | từ khoá quá rộng (`chờ`, `không đổi`) — chúng là **giãn hạn**, chỉ *nhắc tới* đóng băng (**RM-09**) |
| 2 | bắt **sót** `QD-029` | chỉ đọc lời owner, mà owner nói gọn *"mở nha em"* |
| 3 ✓ | đúng 3 mục | đọc cả `ghi_chu` nhưng **bỏ từng CÂU nhắc mã quyết định khác** |

**Đổi báo-thừa lấy báo-sót là tệ hơn** — một cổng báo sót là cổng không tồn tại. Ghi lại đây
để phiên sau không lặp.

**7.3 — Nạp `gpt_analyzer` mất ~7 phút** và in hàng trăm dòng `RULE_ENGINE`, làm kết quả trôi
mất. Cổng nghiệm thu phải **nuốt stdout** khi nạp và khi gọi.

---

## 8. Gỡ về

```bash
cp backups/v11032_pre/gpt_analyzer.py.pre web/backend/gpt_analyzer.py
# trên VPS:
cp /root/Lottery_AI_Test/backups/v11032_pre/gpt_analyzer.py.pre \
   /root/Lottery_AI_Test/web/backend/gpt_analyzer.py && systemctl restart lottery
```

Bản trước vá: md5 `6b28f0baa7aeceac0e9fd2b75a741a81` (CTX-18.1). Có bản sao **cả hai đầu**.

---

## 9. Theo dõi tiếp

| mã | nhãn | hạn | trạng thái |
|---|---|---|---|
| **FU-341 · SC2108** | đã vá — 24h sau đọc trace, phải **0 lượt** `context_pack_chars=64` | 09/08 | `DEPLOYED_PENDING_LIVE_VERIFY` |
| **FU-345 · SC0808** | **A4** — `SP-4.0 scan error` vào prompt **cả 15 model** | 08/08 | `OWNER_DECISION_NEEDED` |
| **FU-343 · QD0811** | đóng `QD-029` + `OD-20260801-D` · thêm trường `thay_boi` | 11/08 | `OWNER_DECISION_NEEDED` |
| **FU-344 · DO2108-2** | đọc verdict `python _v11033_verdict_fu284.py 2026-08-21` | 21/08 | `WAIT_LIVE` |

### Hai câu cần owner ký

1. **FU-345** — *"A4 cùng họ lỗi với cái vừa vá, nhưng chạm **cả 15 model official** chứ không
   phải 1. Vá luôn hôm nay — vì 08/08 đã bị loại khỏi cả hai cửa sổ đo nên **không tốn thêm
   ngày đo nào** — hay chờ 21/08?"*
2. **FU-343** — *"Đóng `QD-029` và `OD-20260801-D`, giữ mình `QD-041`; và cho thêm trường
   `thay_boi` vào lược đồ sổ — anh duyệt không?"*
