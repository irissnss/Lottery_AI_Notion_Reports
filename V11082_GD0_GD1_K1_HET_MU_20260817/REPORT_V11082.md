# REPORT V11082 — GĐ-0 ĐO TRƯỚC + GĐ-1/VÁ-1: `_v11062` K1 HẾT MÙ

**Ngày:** 2026-08-17 · **Mã đọc:** `LU1708` · **Quyết định:** `QD-068`
**PHIÊN ĐANG CHẠY** — bản này đẩy sớm theo yêu cầu owner *«không đẩy báo cáo lên ah để anh còn
phân tích đánh giá và ra lệnh xử lý mới»*. Phần còn lại (`GĐ-1/vá-2` → `GĐ-5`) mang số riêng.

**Production KHÔNG đổi** — không DB, không deploy, không Notion. `QD-041` nguyên vẹn.

---

## 1. Tóm tắt

**Xong:** `GĐ-0` (đo trước) + `GĐ-1/vá-1` (`K1` hết mù, thử chặn hai chiều **ĐẠT**).

**Ba việc CHỜ OWNER, không tự quyết:**

| # | việc | vì sao dừng |
|---|---|---|
| 1 | **Cảnh báo an ninh** — subagent đề xuất **tự cắm hook `SessionStart`** vào `.claude/settings.json` | thêm mã **tự chạy mỗi phiên**, owner **chưa cho phép** |
| 2 | **Phiên khác đã sửa kho** — 10 commit, 30 tệp, +2.439 dòng, **sửa 3 cổng đang dùng** | **48 bản vá** dựng lúc 19:00 ngày 16/08 nay **có thể đã cũ** |
| 3 | **`K8` / `QD-021`** | `GĐ-4` quy định **chỉ TRÌNH**, cấm tự xử |

---

## 2. Owner yêu cầu gì (nguyên văn)

> **12:54 · 17/08** — *«TẠM DỪNG mọi lane khác — phiên này là lane DUY NHẤT; toàn bộ công sức dồn
> cho hoàn thiện luật. (Các lane đo chạy bằng cron trên server không bị ảnh hưởng — CẤM đụng
> chúng.)»*

> **12:57 · 17/08** — *«V11077/V11079 theo phương án (a) — CHỈ phiên gốc viết bù từ bản ghi của
> chính nó (RM-17). Nếu không còn truy cập bản ghi gốc → DỪNG mục này, báo owner; CẤM tự chuyển
> sang soạn từ commit message hay nguồn khác.»*

> **17/08 (sau GĐ-1/vá-1)** — *«không đẩy báo cáo lên ah để anh còn phân tích đánh giá và ra lệnh
> xử lý mới em»*

---

## 3. Đào bới / phát hiện

### 3.1 · GĐ-0 — trạng thái sau V11081

| | |
|---|---|
| số hiệu (cổng `_v11044`, **không đoán**) | **V11082 · FU-405 · QD-068** |
| năm cổng `I1`–`I5` | `I1` = `_v11080_i1_cong_tu_kiem.py` · `I3+I5` = `_v11080_i3i5_chan_lan_du_an.py` · `I2`/`I4` = **vá vào cổng sẵn có** |
| `LUAT_CHUNG.md` | có — bản sao repo **Doc V1.0.1**, SSOT Notion `HDAI-V4.0.35` |
| phép trôi | **3** — `QD-021` · `QD-046` · `QD-056` |

**Ba phép trôi là gì:**

```
QD-021  K8: MỒ CÔI ĐẾN HẠN ≤19/08: ['FU-360(18/08=DEPLOYED_LIVE_VERIFIED)']   ← chính là K8
QD-046  2 model rớt sàn — MẤT ỨNG VIÊN, phải xem lại sàn
QD-056  RM-01: dữ liệu cũ hơn 6 giờ ⇒ bộ đo TỪ CHỐI CHẠY
```

### 3.2 · Hai lỗi treo — xác nhận, và một ĐÍNH CHÍNH

**Lỗi 1 — `_v11062` K1 mù: ĐÚNG y mô tả.**

```python
_v11062_nang_version.py:159
    tu_moc = sorted([v for v in cl if _doc_v(v) >= MOC_THI_HANH], ...)   # cl = CHỈ CHANGELOG
```

**Lỗi 2 — `_v10920` verdict không ổn định: CƠ CHẾ ĐÚNG, TRIỆU CHỨNG KHÔNG TÁI HIỆN.**

```python
_v10920_decision_ledger.py:194
    except Exception as ex:
        return False, f"KHÔNG CHẠY ĐƯỢC: ..."      ← hết giờ trả FALSE = đếm thành TRÔI
```

Sai tầng đúng như `RM-12` cấm. **Nhưng** chạy **hai lần liên tiếp** đều ra `3 PHÉP TRÔI` ⇒
verdict **đang ổn định**, không lung lay như mô tả trong V11081 mục 9.

> Ghi đúng như **đo được**, không chép lại mô tả cũ. Vá vẫn cần (cơ chế sai), nhưng **không được
> ghi là «đã tái hiện»** khi nó không tái hiện.

### 3.3 · GĐ-1/vá-1 — `K1` hợp `CHANGELOG ∪ git log`

Áp **đúng cách đã vá `_v10921`** (V11080/`I4`) — không sáng chế cách thứ hai.

**Bằng chứng lỗ hổng là thật:** `V11077` (`a33b86a`) và `V11079` (`4a7ee6d`) trôi **34 phút sau**
khi vừa bù xong 12 bản, mà cổng vẫn **báo xanh**.

**Sau vá:** `K1` bắt **đúng 3 bản** — `V11080b` · `V11079` · `V11077`.
`V11080b` là của **phiên khác** ⇒ cổng bắt **cả hai bên**, đúng như nó phải làm.

**Agent tự sửa mình — `K1b` hạ xuống GHI CHÚ:** bản đầu đặt `K1b` báo đỏ cho **15 bản**. Nhưng
**12 bản trong đó ĐÃ có dòng `HISTORY`** — chúng được ghi **gộp** trong khối `V11076`, cách ghi
hợp lệ. Báo đỏ ở đây ⇒ cổng **đỏ vĩnh viễn** ⇒ **mất sạch giá trị cảnh báo**, đúng nguyên tắc
owner áp cho `CHECKSUMS` trong chính prompt này.

---

## 4. Hướng xử lý và vì sao

**Vì sao dùng `BO_QUA_CONG_COMMIT=1` cho commit `d72ebc7`:** cổng đang **ĐỎ vì chính lỗi mà
commit đó đi vá** (3 bản chưa có dòng HISTORY). Không bỏ qua thì **không commit được bản vá**.
Đã **ghi lý do vào commit message** — đúng giao kèo của cổng.

**Vì sao chưa áp 48 bản vá:** phiên khác đã sửa **30 tệp** sau khi các bản vá đó được dựng. Áp mù
có thể **đè mất việc của phiên kia**. Phải **kiểm lại từng bản trên kho hiện tại** — bản nào đoạn
`trước` không còn khớp thì **loại**, không sửa mò.

---

## 5. Đã làm gì

| # | việc | bằng chứng |
|---|---|---|
| 1 | `GĐ-0` đo trước, read-only | mục 3.1 |
| 2 | Xác nhận lỗi 1, **đính chính** lỗi 2 | mục 3.2 |
| 3 | Vá `K1` hợp `CHANGELOG ∪ git log` | commit `d72ebc7` |
| 4 | Hạ `K1b` xuống ghi chú | tránh cổng đỏ 100% |
| 5 | **Thử chặn hai chiều** | `THU_CHAN_K1_HOP_GITLOG=ĐẠT` |
| 6 | Nâng bốn mặt qua `_v11062.ghi()` | `governance_seq → 411` |

**Thử chặn — bốn bước, bằng cách thay hàm, không đụng tệp thật:**

```
[1] bản vá (có hợp git log)          → ĐỎ   thấy được
[2] giả lập bản CŨ (git log = rỗng)  → XANH = CHỨNG MINH chỗ mù cũ là THẬT
[3] giả lập đã bù đủ 3 bản           → XANH cho qua
[4] khôi phục nguyên trạng           → ĐỎ   (đúng, vì thật sự còn thiếu)
```

Bước `[2]` là phần quan trọng nhất: nó **chứng minh bản cũ mù thật**, không phải suy đoán.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11044_cong_so_hieu.py` | **✓** — V11082 · FU-405 · QD-068 |
| `_v11062 --kiem` sau vá | **✗ ĐỎ ĐÚNG** — `K1` nêu 3 bản thiếu HISTORY |
| thử chặn `K1` hai chiều | **✓ ĐẠT** |
| `_v10920_decision_ledger` | **✗ 3 phép trôi** — `QD-021`/`QD-046`/`QD-056` |

> **Không ghi «mọi cổng xanh».** Hai cổng đang **ĐỎ ĐÚNG**: `_v11062` đỏ vì 3 bản chưa bù
> (`GĐ-5` sẽ xử), `_v10920` đỏ vì 3 phép trôi thật.

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **12:54 17/08** | *«TẠM DỪNG mọi lane khác — phiên này là lane DUY NHẤT… Các lane đo chạy bằng cron trên server không bị ảnh hưởng — CẤM đụng chúng»* |
| **12:57 17/08** | *«V11077/V11079 theo phương án (a) — CHỈ phiên gốc viết bù từ bản ghi của chính nó (RM-17)… CẤM tự chuyển sang soạn từ commit message hay nguồn khác»* |
| 17/08 | *«không đẩy báo cáo lên ah để anh còn phân tích đánh giá và ra lệnh xử lý mới em»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| `K1` lấy worklist chỉ từ CHANGELOG | `_v11062_nang_version.py:159` |
| hết giờ bị đếm thành TRÔI | `_v10920_decision_ledger.py:194` |
| verdict **ổn định** hai lần chạy | cả hai lần ra `3 PHÉP TRÔI` |
| sau vá, `K1` bắt đúng 3 bản | `V11080b` · `V11079` · `V11077` |
| phiên khác sửa 30 tệp / +2.439 dòng | `git diff --stat 4a7ee6d..HEAD` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| V11081 mục 9: *«`_v10920` verdict không ổn định»* | **⚠ LỆCH** — cơ chế đúng nhưng **triệu chứng không tái hiện** hôm nay |
| `RM-12` *«cấm gộp tầng»* | **khớp** — và `_v10920:194` đang vi phạm |
| prompt owner: *«đỏ 100% = mất giá trị cảnh báo»* | **khớp** — nên hạ `K1b` xuống ghi chú |

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` ≠ `CODE_DID`:** V11081 mô tả verdict *«không ổn định»*; đo hai lần liên tiếp thì
**ổn định**. Cơ chế sai vẫn có thật, nhưng **mô tả triệu chứng đã cũ** — vá vì cơ chế, không vá
vì triệu chứng.

---

## 7. Vướng vấp

| # | vấp | xử |
|---|---|---|
| 1 | `K1b` bản đầu báo đỏ 15 bản, trong đó **12 bản đã ghi đúng** | hạ xuống ghi chú |
| 2 | Biến `chi_git_va_thieu` **dùng trước khi định nghĩa** ⇒ `UnboundLocalError` | chuyển định nghĩa lên trước; bắt được vì **chạy có nhìn output** |
| 3 | Commit bị chính cổng mới chặn | dùng cờ bỏ qua **có ghi lý do**, đúng giao kèo |

---

## 8. Gỡ về

```bash
git revert d72ebc7      # vá K1 — độc lập, không kéo theo gì
```

---

## 9. Theo dõi tiếp

| mã | việc | mốc |
|---|---|---|
| **`GĐ-1/vá-2`** | tách `KHÔNG_KIỂM_ĐƯỢC` khỏi `TRÔI` trong `_v10920` | phiên này |
| **`GĐ-2`…`GĐ-5`** | tách ba tầng · ba luật riêng · K8 · bù V11077/79 | phiên này |
| **`GĐ-3` (đổi tiền tố §)** | **KHOÁ tới sau 21/08** theo `QD-041` | sau 21/08 |
| **`K8` / `QD-021`** | hạn **≤18/08** — chỉ **TRÌNH**, chờ owner ký | **ngày mai** |
| **48 bản vá** từ đợt đào | phải **kiểm lại trên kho hiện tại** trước khi áp | chờ owner |

**Verdict tách hai dòng:**
- **`CODE_PUSHED`** = `d72ebc7` (vá K1)
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **`V11082`** — `GĐ-0` + `GĐ-1/vá-1` xong, `K1` nay hợp
`CHANGELOG ∪ git log`, **thử chặn hai chiều ĐẠT**; ② ghi **ĐÍNH CHÍNH**: lỗi *«verdict không ổn
định»* có **cơ chế đúng** nhưng **triệu chứng KHÔNG tái hiện** (hai lần chạy cùng ra 3 phép trôi)
— đừng chép lại mô tả cũ; ③ ghi **`K1b` cố ý KHÔNG báo lỗi** với 15 bản ghi gộp — ai thấy nó im
thì đó là **chủ ý**, không phải hỏng; ④ **CHỜ OWNER ba việc**: cảnh báo an ninh hook `SessionStart`
· 48 bản vá cũ do phiên khác đã sửa 30 tệp · `K8` chỉ trình; ⑤ ghi rõ **hai cổng đang ĐỎ ĐÚNG**
(`_v11062` vì 3 bản chưa bù, `_v10920` vì 3 phép trôi) — **cấm ghi «mọi cổng xanh»**.
