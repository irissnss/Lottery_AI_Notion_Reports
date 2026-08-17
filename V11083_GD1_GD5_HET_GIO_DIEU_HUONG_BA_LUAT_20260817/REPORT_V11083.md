# REPORT V11083 — GĐ-1/VÁ-2 · GĐ-2 · GĐ-3 · GĐ-4 · GĐ-5

**Ngày:** 2026-08-17 · **Mã đọc:** `LU1708-2` · **Quyết định:** `QD-068`
**Production KHÔNG đổi** — không DB · không deploy · không Notion · `QD-041` nguyên vẹn.

---

## 1. Tóm tắt

Năm chặng, và **bốn việc CHỜ OWNER** ở cuối. Số nào cũng chạy lại được.

| chặng | kết quả |
|---|---|
| **GĐ-1/vá-2** | `_v10920` tách **HẾT GIỜ** khỏi **TRÔI** (`RM-12`) · thử chặn **6/6 ĐẠT** · verdict **ổn định** |
| **GĐ-5** | hàm dùng lại `_v11062.bu()` · bù `V11077` + `V11079` theo **phương án (a)** · `K1` **3 → 2** |
| **GĐ-2** | 5 tệp điều hướng kho báo cáo nay **sinh từ thư mục thật** (363 thư mục) |
| **GĐ-3** | ba luật `PRJ-*` vào **đủ sáu mặt ngay từ đầu**, cùng một tiêu đề |
| **GĐ-4** | **K8 đỏ vì owner đã ra lệnh cho nó đỏ** — trình ba lối, **không tự xử** |

**Con số đáng chú ý nhất:** phép trôi **3 → 4**, và phép thứ tư là **hệ quả của chính bản vá
V11082 phiên này**. Ghi ra, không giấu.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **12:54 · 17/08** — *«TẠM DỪNG mọi lane khác — phiên này là lane DUY NHẤT; toàn bộ công sức
> dồn cho hoàn thiện luật. (Các lane đo chạy bằng cron trên server không bị ảnh hưởng — CẤM đụng
> chúng.)»*

> **12:57 · 17/08** — *«V11077/V11079 theo phương án (a) — CHỈ phiên gốc viết bù từ bản ghi của
> chính nó (RM-17). Nếu không còn truy cập bản ghi gốc → DỪNG mục này, báo owner; CẤM tự chuyển
> sang soạn từ commit message hay nguồn khác.»*

> **17/08** — *«không đẩy báo cáo lên ah để anh còn phân tích đánh giá và ra lệnh xử lý mới em»*

---

## 3. Đào bới / phát hiện

### 3.1 · GĐ-1/vá-2 — hết giờ bị đếm thành trôi

```python
_v10920_decision_ledger.py:194  (bản cũ)
    except Exception as ex:
        return False, f"KHÔNG CHẠY ĐƯỢC: ..."     ← MỌI ngoại lệ, kể cả hết giờ
```

Sai tầng đúng như `RM-12` cấm. Hậu quả nặng hơn chuyện chữ nghĩa: trần 300s phụ thuộc **tải
máy**, nên cùng một kho, cùng một commit, **hai lần chạy có thể ra hai verdict**.

### 3.2 · GĐ-2 — năm tệp điều hướng **nói dối im lặng**

| tệp | cập nhật lần cuối | đang nói gì |
|---|---|---|
| `REPORT_INDEX.md` | **27/07** | *«Latest: V10861»* |
| `LATEST_REPORT.json` | **27/07** | `latest_version: V10861` |
| `NEXT_ACTION.md` | **27/07** | *«On 28/07, re-read PB-18.1, M2s, K15…»* |
| `DELTA_INDEX.md` | **08/05** | dừng ở `V91 → V92` |
| `CHECKSUMS_SHA256.txt` | **08/05** | 10 mã băm — **cả 10 đều SAI** |

Trong khi kho có **363 thư mục báo cáo**. Không tệp nào **hỏng theo kiểu báo lỗi** — người đọc
(và `TanPhatAI`) mở ra thấy mục lục trông hợp lệ rồi tin bản mới nhất là `V10861`, lệch **21
ngày**.

### 3.3 · GĐ-4 — K8: hai quyết định owner **ngược nhau, cùng ACTIVE**

```
QD-066 (12/08) → FU-360/FU-389 GIỮ nhãn DEPLOYED_LIVE_VERIFIED, KHÔNG đóng,
                 KHÔNG đăng ký nhãn vào DONG_STATUSES
                          ↓ hệ quả BẮT BUỘC
                 hai mục VĨNH VIỄN là "mồ côi"
                          ↓ va thẳng vào
QD-021 (04/08) → K8 đòi 0 mồ côi đến hạn trong 2 ngày tới
```

Chính sổ theo dõi đã viết — mà **không cổng nào đọc được câu đó**:
`FOLLOW_UP_TRACKER.md:239` *«Hai mục này vẫn hiện là mồ côi trong briefing; **đó là chủ ý**,
không phải lỗi.»*

**Đo được, không đoán** (`--hom-nay` từng ngày):

| ngày | K8 |
|---|---|
| 14/08 · 15/08 | **ĐẠT** |
| **16/08** | **TRƯỢT** ← ngày đổi màu |
| 17/08 · 18/08 · **21/08** · 22/08 | **TRƯỢT** ← **không tự hết** |

Qua **21/08 vẫn đỏ** vì lúc đó mục đã **quá hạn**. Đỏ liên tục **≥6 ngày** — đúng thứ owner đã
cấm khi nói về `CHECKSUMS`: *«đỏ 100% thì tệ hơn là không có»*.

**Ba phát hiện kèm:**
① cổng `RM-19` `_v11034` báo **`SẠCH`** — nó chỉ so **trong cùng chủ đề**, mà `QD-021` và
`QD-066` khác chủ đề nên **không bao giờ được đem ra so**;
② ngày `18/08` lái K8 là **ngày đọc nhầm nhãn** — thân bảng ghi `| **hạn** | 14/08 |` *(owner ký,
`RM-06`)*, bộ đọc nhận 4 nhãn (`due` · `- Hạn:` · `hạn mới` · `deadline`) còn sổ dùng nhãn **thứ
năm** ⇒ rơi xuống tiêu đề. **Vá nhãn KHÔNG cứu được K8** — ngày đúng còn quá hạn sâu hơn;
③ bản `NEXT_ACTION` mới (vừa dựng ở GĐ-2) **lộ ra `FU-348` hạn HÔM NAY**: *«CỔNG K8 ĐANG XANH
GIẢ — `MO_COI_TRAN` chưa hạ»*. Ghép lại: K8 **không hề chặt hơn** — nó từng xanh vì **trần nới
gấp 7 lần** ngưỡng `FU-258` tự khai (15 thay vì 2). Và mồ côi nay **đúng bằng 2** ⇒ **hạ trần
15 → 2 hôm nay là ĐẠT, không vỡ gì**.

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao `bu()` phải là HÀM, không phải script nháp.** Gốc bệnh của §63 ghi ngay đầu
`_v11062`: *«không có công cụ dùng lại — mỗi phiên agent tự viết một script nháp mới»*. Đợt bù
12 bản ngày 16/08 **lại đúng như vậy**. Việc bù lặp lại sau **một ngày** ⇒ nếu không thành hàm
thì lần thứ ba sẽ là script nháp thứ ba.

**Vì sao `DELTA_INDEX` RÚT LẠI chứ không sinh tiếp.** Nội dung *«V(n−1) → V(n)»* là **nhận định
của người viết**, không suy ra được từ kho. Sinh giả bằng cách chép tiêu đề commit là **chế dữ
liệu** (`RM-17`). Không xoá vì đường dẫn đã nằm trong `AUTOMATION_STATE.json`.

**Vì sao mã `PRJ-` chứ không đánh số `§` mới.** Owner **khoá đổi tiền tố `§` tới sau 21/08**. Ba
luật này **không chờ được** — mỗi luật sinh từ một sai lầm **đã xảy ra nhiều lần**.

**Vì sao KHÔNG tự xử K8.** Ba lối sửa đều đụng thứ owner đã ký: thêm `DEPLOYED_LIVE_VERIFIED` vào
`DONG_STATUSES` (**`QD-066` cấm thẳng**) · đổi nhãn/đóng hai mục (**cấm thẳng**) · miễn trừ khỏi
K8 (**nới cổng để cổng khỏi kêu**). Và `GĐ-4` viết rõ: **TRÌNH owner, cấm tự đóng**.

---

## 5. Đã làm gì

**GĐ-1/vá-2** — tách `TimeoutExpired` ⇒ `None`. Ngoại lệ **khác** (thiếu tệp) **vẫn TRÔI**, giữ
chủ ý V10976 *«hỏng cổng cũng là mất kiểm soát»*.

**KHÔNG bỏ nửa chừng (§60):** sửa cả đường **HIỂN THỊ** —

| chỗ | TRƯỚC | SAU |
|---|---|---|
| console | 2 khớp + 1 hết giờ hiện `🟢 khớp 2/2` | `🟡 khớp 2 · ⏱ 1 hết giờ`, in từng phép |
| bản `.md` | `🟢 KHỚP (2/2 phép)` | `🟡 KHỚP 2 phép · ⏱ 1 phép HẾT GIỜ` |
| sentinel | `__HET_GIO__` lọt ra bản người đọc | bỏ, đổi nhãn |
| mã thoát | `2` hoặc `0` | `2` TRÔI · `1` hết giờ · `0` sạch |

Tách hàm `phan_tang()` dùng chung cho **cả hai** nơi — một hàm thì **thử được bằng máy**, hai
đoạn viết lặp chỉ thử được một nửa rồi tưởng đã thử cả.

**GĐ-5** — `_v11062.bu()`, khác `ghi()` ở bốn chỗ: không đụng `CHANGELOG`/`SSOT` (prepend bản cũ
làm thứ tự nói dối) · không đụng `STATE.last_version` (`K4` sẽ báo sai) · bắt buộc trường
`nguon_ban_ghi` để **kiểm được** giao kèo phương án (a) · đã có dòng thì **bỏ qua**.

**GĐ-2** — `_v11083_sinh_dieu_huong.py`, hai chế độ: sinh, và `--thu` **đối chiếu** với thư mục
thật.

**GĐ-3** — ba luật vào `CLAUDE.md` · `.Antigravityrules.md` · `.AGENT.md` · `.cursorrules`, rồi
sinh lại `AGENTS.md` + `GEMINI.md`.

**GĐ-4** — `docs/K8_TRINH_OWNER_20260817.md`, ba lối **A/B/C** kèm *được gì / mất gì*.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| thử chặn `HẾT GIỜ ≠ TRÔI` | **✓ 6/6 ĐẠT** — `T2` chứng minh khuyết tật cũ **có thật** |
| ổn định verdict | **✓** hai lần chạy · `exit=2` · danh sách quyết định **diff rỗng** |
| `--thu` đối chiếu điều hướng | **✓** trước: 2 mặt LỆCH → sau: `DIEU_HUONG_KHOP_THU_MUC=DAT` |
| `_v10925_rule_sync_check` | **✓** SÁU MẶT ĐỒNG BỘ, đã sinh lại 2 mặt sinh |
| `_v11027_so_muc_quan_tri` | **✓** không mục nào biến mất · điều mới **đủ sáu mặt** |
| `_v10921_report_gate` V11077 · V11079 | **✓ ĐẠT cả hai** |
| `_v11062 --kiem` | **✗ ĐỎ ĐÚNG** — còn **`V11080b`**, thứ agent **bị cấm** tự bù |
| `_v10920_decision_ledger` | **✗ 4 phép trôi** — xem mục 7 |

> **Không ghi «mọi cổng xanh».** Hai cổng đang **ĐỎ ĐÚNG**, và một trong hai đỏ vì **chính bản vá
> của phiên trước trong ngày**.

**Thử chặn — sáu phép, `T2` là phép quan trọng nhất:**

```
T1 hết giờ ⇒ None (KHÔNG_KIỂM_ĐƯỢC)            ✓
T2 dựng lại BẢN CŨ ⇒ False  = KHUYẾT TẬT CÓ THẬT ✓  ← không phải suy đoán từ đọc code
T3 lỗi khác (thiếu tệp) VẪN TRÔI                ✓  ← không vá lố
T4 chạy tốt vẫn KHỚP                            ✓  ← không vỡ đường thường
T5 phân tầng 0 trôi · 2 khớp · 1 hết giờ        ✓
T6 bản .md hiện HẾT GIỜ, không lọt sentinel     ✓  ← đường HIỂN THỊ, không chỉ đường tính
```

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **12:54 17/08** | *«TẠM DỪNG mọi lane khác — phiên này là lane DUY NHẤT… CẤM đụng [lane cron trên server]»* |
| **12:57 17/08** | *«CHỈ phiên gốc viết bù từ bản ghi của chính nó (RM-17)… CẤM tự chuyển sang soạn từ commit message hay nguồn khác»* |
| **12/08** (`QD-066`) | *«Tạm thời để nguyên tới 21/08 luôn em, đâu ảnh hưởng gì đến dự đoán mà clear vội em, để càng lâu càng rõ ràng chứ em»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| hết giờ bị đếm thành TRÔI | `_v10920_decision_ledger.py:194` (bản cũ) |
| sau vá: hết giờ ⇒ `None`, lỗi khác vẫn `False` | `_v11083_thu_chan_het_gio.py` — 6/6 |
| verdict **ổn định** | hai lần chạy: `exit=2`, `diff` danh sách = rỗng |
| K8 đổi màu **16/08**, **không tự hết** | `_v10981_kiem_lich.py --hom-nay <ngày>` |
| cổng `RM-19` không thấy va chạm | `_v11034_kiem_cheo_quyet_dinh.py` → `KIEM_CHEO_QD=SACH` |
| `18/08` là ngày **kế thừa** từ lần nhắc cũ | `_v10958_fu_reader.py:371-380` · nhãn: `:70-82` |
| điều hướng lệch thư mục thật | `--thu` trước khi sinh: `LATEST_REPORT` khai `V10861_OUTPUT_CONTRACT` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| `FOLLOW_UP_TRACKER.md:239` *«mồ côi… đó là chủ ý, không phải lỗi»* | **khớp** owner — nhưng **không cổng nào đọc được** |
| `FU-348` *«CỔNG K8 ĐANG XANH GIẢ»* | **khớp** — và bổ sung đúng nửa còn thiếu của bức tranh |
| `_v10920` docstring cũ *«script hỏng ⇒ TRÔI»* | **đã cập nhật** — nay ba tầng, hết giờ tách riêng |
| `REPORT_INDEX.md` *«Latest: V10861»* | **LỆCH 21 ngày** — đã sinh lại |

### Ba lớp lệch nhau ⇒ FINDING BẮT BUỘC BÁO

**`OWNER_SAID` vs `OWNER_SAID`:** `QD-021` (04/08) và `QD-066` (12/08) **ngược nhau mà cùng
`ACTIVE`** — `RM-19`. Đây **không phải** mã trôi khỏi quyết định; đây là **hai quyết định va
nhau**, và không cổng nào đang soi cặp này.

**`DOC_SAID` ≠ `CODE_DID`:** sổ theo dõi **biết** hai mục mồ côi là chủ ý, nhưng cổng `K8`
**không có cách nào đọc được** câu đó ⇒ nó cứ đỏ.

---

## 7. Vướng vấp — **sáu vấp của chính agent**, cả sáu đều ghi lại

| # | vấp | bắt được bằng cách nào |
|---|---|---|
| 1 | `chi_git_va_thieu` dùng trước khi định nghĩa ⇒ `UnboundLocalError` | **chạy có nhìn output** |
| 2 | khoá sắp xếp ép `V105_60` thành một số ⇒ `V10756_3` **nhảy lên trên** `V11082`; chỉ nhận **248/365** thư mục | nhìn kết quả `--thu` |
| 3 | `NEXT_ACTION` bản đầu in 12 mục **đều đã `CLOSED`** — trang «việc kế tiếp» toàn chuyện đã xong, **trông rất hợp lệ** | **đọc nội dung sinh ra**, không tin dòng `✓` |
| 4 | cắt danh sách chung ở N mục ⇒ tồn đọng cũ **ăn hết chỗ**, mục đến hạn **ngày mai** không bao giờ hiện | đọc bảng, thấy thiếu 18/08 |
| 5 | ghi đè `REPORT_INDEX.md` **594 → 385 dòng**, nuốt mất **38 câu tóm tắt VIẾT TAY** | **nhìn SỐ DÒNG** |
| 6 | ba luật mới đặt **bốn tiêu đề khác nhau** ⇒ cổng `I2(a)` đọc thành **bốn điều riêng** | cổng `_v11027` bắt |

**Vấp 2 là `RM-10`:** kho có **bốn** họ tên thư mục (`V11082_..._20260817` · `V10756_3_...` ·
`V105_60_..._PUBLIC_SAFE` · `V106_28R0A_...`), agent giả định **một**.

**Vấp 5 nặng nhất, và đáng nói vì nó gần lọt.** «594 → 385 dòng» nghe như *gọn hơn* — bản mới phủ
**363** bản trong khi bản cũ chỉ có ~50. Nhưng bản cũ giữ **38 câu tóm tắt do người viết**, không
suy ra được từ tên thư mục. Đã khôi phục, và thêm bước **cất bản viết tay** trước khi ghi đè.
Cùng tinh thần §63 *«từ chối nếu tệp ngắn đi»*: bản máy sinh **được phép thay** bản viết tay,
**không được phép nuốt** nó.

**Và một phép trôi mới do chính phiên này tạo ra.** Phép trôi **3 → 4**; phép thứ tư là `QD-062`
*«Cổng chứng minh chặn được (RM-15)»* — hệ quả của **bản vá V11082 sáng nay**: `K1` bắt 3 bản
thiếu `HISTORY` ⇒ `_v11062` đỏ ⇒ `--thu-chan` không chạy nổi bước `[1]` (cần trạng thái sạch để
chứng minh chiều **cho qua**). Nay còn `V11080b` nên **vẫn đỏ**.

---

## 8. Gỡ về

```bash
git revert 3cb342d   # GĐ-3 · ba luật PRJ-* (nhớ chạy lại _v10925 để sinh lại 2 mặt sinh)
git revert 43485fd   # GĐ-2 · bộ sinh điều hướng + bản trình K8
git revert f346cd6   # GĐ-5 · hàm bu() + 2 dòng HISTORY
git revert 9afe827   # GĐ-1/vá-2 · hết giờ ≠ trôi
```

Kho báo cáo công khai: `git revert 8757cd9` trả lại bộ điều hướng cũ *(bản viết tay vẫn còn ở
`REPORT_INDEX_VIET_TAY_DEN_20260727.md`)*.

---

## 9. Theo dõi tiếp

### CHỜ OWNER — bốn việc, agent **không tự quyết**

| # | việc | vì sao dừng |
|---|---|---|
| 1 | **Cảnh báo an ninh** — subagent đề xuất **tự cắm hook `SessionStart`** | thêm mã **tự chạy mỗi phiên**, owner **chưa cho phép**. **KHÔNG ÁP** |
| 2 | **48 bản vá** từ đợt đào 16/08 | phiên khác đã sửa **30 tệp / +2.439 dòng** sau đó ⇒ áp mù có thể **đè mất việc của phiên kia** |
| 3 | **`V11080b`** chưa có dòng `HISTORY` | của **phiên khác**; agent này không giữ bản ghi gốc ⇒ đúng câu owner dặn: **dừng, báo owner** |
| 4 | **K8** — chọn lối **A / B / C**, và **`FU-348`** hạ `MO_COI_TRAN` **15 → 2** | cả hai đều là **nới/siết cổng**; `FU-348` **hạn HÔM NAY** |

**Khuyến nghị cho ④:** lối **A** — miễn trừ **CÓ THỜI HẠN**, gắn mã `QD-066`, tự hết **21/08**.
Cổng xanh lại mà **không đóng lén** mục nào, và miễn trừ **tự hết** nên không thành cửa sau.

### Việc còn nợ

| việc | ghi chú |
|---|---|
| bộ đọc nhận thêm nhãn `\| **hạn** \|` dạng ô bảng | đang **đọc nhầm ngày** ít nhất một mục |
| cổng `RM-19` so **cả cặp khác chủ đề** | hiện báo `SẠCH` trong khi có va chạm thật |
| quét họ lỗi *tự-khai-READ-ONLY* ở các bộ đo khác | `RM-07` — từ `V11079`, chưa làm |
| lớp lỗi `>/dev/null` che stderr | **tái phạm lần 3** ⇒ tới ngưỡng phải dựng **cổng máy** |

**Verdict tách hai dòng:**
- **`CODE_PUSHED`** = `9afe827` (GĐ-1/vá-2) · `f346cd6` (GĐ-5) · `43485fd` (GĐ-2 + trình K8) ·
  `3cb342d` (GĐ-3) · kho công khai `8757cd9`
- **`REPORT_PUBLISHED`** = bản này · và `V11077` + `V11079` đã bù (`fb79d8f`)

---

TanPhatAI cần làm: ① ghi **`V11083`** — năm chặng xong, **thử chặn 6/6 ĐẠT**, verdict **ổn định**;
② ghi **`FU-316` ĐÓNG nhánh 2** (không neo) và **`FU-348` hạn HÔM NAY** chưa xử; ③ ghi **ba luật
mới** `PRJ-RETRACTION-001` · `PRJ-SELECTION-WINDOW-001` · `PRJ-PROMPT-COHERENCE-001` đã vào **đủ
sáu mặt**; ④ ghi **K8 KHÔNG phải lỗi kỹ thuật** — `QD-021` vs `QD-066` **ngược nhau cùng ACTIVE**
(`RM-19`), cổng `RM-19` đang **mù** với cặp khác chủ đề; ⑤ **CHỜ OWNER bốn việc** (cảnh báo an
ninh hook `SessionStart` · 48 bản vá cũ · `V11080b` · K8 chọn A/B/C + `FU-348`); ⑥ ghi **hai cổng
đang ĐỎ ĐÚNG** — `_v11062` vì `V11080b`, `_v10920` vì 4 phép trôi (một phép là **hệ quả của chính
bản vá V11082**) — **cấm ghi «mọi cổng xanh»**.
