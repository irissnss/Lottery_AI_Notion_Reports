# REPORT V11037 — VÁ CỔNG CÓ THỂ NÓI DỐI OWNER + HAI MỤC VÔ HÌNH

**Ngày:** 2026-08-08 khuya · **Loại:** fix + gate · **Lane test — QD-041 KHÔNG chặn**

---

## 1. Tóm tắt

Owner giao *"tiếp tục theo đề xuất"*. Làm đúng thứ tự đã trình: **FU-357 trước** (cổng có thể
nói dối, hạn 19/08), rồi **FU-353** (hai mục vô hình).

| | |
|---|---|
| **FU-357 ①** | `decide()` ghi «ĐẠT — trình owner duyệt thay official» **không có phép ý nghĩa nào**. Nay bắt buộc **p < 0,05** |
| **FU-357 ②** | `_discordant()` cho ra **số âm** (`both_lose = −1`) và tính `p_value` từ số sai |
| **FU-353** | `FU-317` + `FU-325` có `due_date = None` ⇒ **vô hình với mọi bộ đếm**. Hai gốc khác nhau |
| **Cố ý CHƯA làm** | **FU-360** — hôm nay đã bốn thay đổi, và đó là chỗ **ghi vào bảng khoá** |

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

> Tiếp tục theo đề xuất anh nghĩ em nắm code rõ , ngử canh anh chung cấp em khá nhiều rồi, em
> biết phải làm gì để hệ thống được giám sát và cải tiến tốt nhất

---

## 3. Đào bới / phát hiện

### 3.1 `decide()` — hai số đếm thô, không phép ý nghĩa nào

```python
if new_only > off_only:
    verdict = "ĐẠT — đủ điều kiện trình owner duyệt thay official"
```

Đo 08/08: đo tiến **3 vs 4**. Chỉ cần **HAI ngày may** nữa là **5 vs 4** ⇒ trang báo **«ĐẠT»**,
trong khi McNemar chính xác cho 5-vs-4 ra **p = 1,0**. `DECISION_DATE` = **19/08**, còn 11 ngày.

**Một cổng nói với owner «đủ điều kiện thay đường chính thức» dựa trên 9 lần tung đồng xu là
cổng nói dối.**

### 3.2 `_discordant()` — số ÂM, và p tính từ số sai

```python
diff      = [r for r in rows if r["new_bach_thu"] != r["off_bach_thu"]]   # SỐ khác nhau
both_lose = len(diff) - new_win - off_win                                  # ← ÂM được
```

Hai bên chọn **hai số khác nhau mà CẢ HAI CÙNG TRÚNG** là chuyện có thật — đo được **7 ngày**
(15/06 MT · 16/06 MN · 02/07 MN · 02/07 MT · 04/07 MT · 20/07 MT · …). Chúng bị cộng vào **cả
hai** vế ⇒ `both_lose = −1` trên đo tiến. **Bảng công bố cho owner mà có số âm.**

**Sai nặng hơn:** `p_value` tính từ `(29, 15)` — nhưng McNemar cần **cặp lệch KẾT QUẢ**, tức
**(22, 8)**. *«Số khác nhau»* **không phải** *«kết quả khác nhau»*: hai số khác mà cùng trúng là
cặp **đồng thuận**, không mang thông tin nào về bên nào hơn.

### 3.3 FU-353 — hai gốc khác nhau, không phải một

| mục | gốc |
|---|---|
| **FU-317** | tiêu đề `hạn **21/08**` — dấu `**` chen giữa nên mẫu `hạn\\s+(\\d{2}/\\d{2})` **TRƯỢT** |
| **FU-325** | tiêu đề `cần 10/08` — **không có chữ «hạn»** |

---

## 4. Hướng xử lý và vì sao chọn

**4.1 — Dùng McNemar CHÍNH XÁC, không xấp xỉ chuẩn.** Cặp lệch chỉ có 7 — xấp xỉ chuẩn ở cỡ đó
là sai. Hàm `_mcnemar_p` sẵn có đã dùng nhị thức chính xác.

**4.2 — Ngưỡng ghi BẰNG SỐ ngay trong hàm** (`NGUONG_P = 0.05`), không giấu trong đầu ai —
RM-03 đòi đăng ký ngưỡng TRƯỚC.

**4.3 — Khi chưa đủ sức, chữ phải nói ĐÚNG điều đó.** Không viết «ĐẠT» rồi để owner tự hiểu là
đã chứng minh được. Verdict mới nói thẳng *«CHƯA ĐƯỢC PHÉP KẾT LUẬN — official đang hơn (3 vs 4)
nhưng p=1.0 ≥ 0.05»* (RM-04).

**4.4 — Giữ tên khoá `new_win`/`official_win`** để trang không vỡ, nhưng **nội dung nay là cặp
lệch thật**. Thêm khoá mới `both_win`.

**4.5 — KHÔNG nới regex bắt mọi `DD/MM`.** Sẽ vơ nhầm ngày trong câu kể (*"không phải 08/08"*,
*"dựng xong sớm 07/08"*). Mục thiếu chữ «hạn» thì **sửa mục**, đừng làm hỏng bộ đọc.

**4.6 — Hoãn FU-360 có chủ ý.** Xem §7.

---

## 5. Đã làm gì

**TRƯỚC:** `decide()` so hai số đếm thô · `_discordant()` ra `both_lose = −1` và p từ (29,15) ·
`FU-317`/`FU-325` `due_date = None`.
**SAU:** `decide()` bắt buộc `p < 0,05` · `_discordant()` bốn nhóm phủ kín + `assert >= 0` ·
hai mục có `due_date` đúng.
**PHIÊN BẢN:** V11037 · 08/08/2026 · `_v10879_nghiemthu_lane.py` md5 `bdaf2b02…` →
**`40e269c89248bb717d3e5ad6cd7693de`**.
**KIỂM:** `python web/backend/_v11037_kiem_decide.py` → `DECIDE_V11037=DAT`

### Luật mới chặn được gì

| cặp lệch | p | luật CŨ | **luật MỚI** |
|---|---|---|---|
| 3 vs 4 | 1,0 | TRƯỢT | CHƯA ĐƯỢC PHÉP KẾT LUẬN |
| **5 vs 4** | **1,0** | **ĐẠT** ⚠ | **CHƯA ĐƯỢC PHÉP KẾT LUẬN** |
| 8 vs 2 | 0,109 | ĐẠT ⚠ | **CHƯA ĐƯỢC PHÉP KẾT LUẬN** |
| 9 vs 1 | 0,021 | ĐẠT | ĐẠT ✓ |
| 10 vs 0 | 0,002 | ĐẠT | ĐẠT ✓ |

### `_discordant()` trước/sau, trên dữ liệu thật

| | TRƯỚC | SAU |
|---|---|---|
| đo tiến `both_lose` | **−1** | **0** |
| backfill `new_win` / `official_win` | 29 / 15 | **22 / 8** |
| backfill `both_win` | *(không có)* | **7** |
| backfill `both_lose` | 33 | **40** |
| backfill `p_value` | từ số sai | **0,01612** |

> ⚠ Backfill `p = 0,01612` **nghe như có ý nghĩa** — nhưng đó là **chấm ngược**. `decide()`
> **chỉ** nhận `forward`, đúng thiết kế. Trích số backfill làm bằng chứng «bản mới hơn official»
> chính là **dấu vân tay thiên vị chọn**.

### FU-353

```
FU-325  due_date=2026-08-10  hạn='10/08'  mã đọc='SC1008'
FU-317  due_date=2026-08-21  hạn='21/08'
```

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| Tuổi dữ liệu | **ĐẠT** — 1,58 giờ |
| `_v11037_kiem_decide.py` local | **ĐẠT** — 7/7 |
| `_v11037_kiem_decide.py` **trên VPS** | **ĐẠT** — 7/7 |
| md5 local = VPS | **ĐẠT** |
| PID trước/sau | **ĐỔI** `1092764 → 1094233` |
| `/api/health` · `/nghiem-thu` | **200** · **401** (đúng, cần admin) |
| `NO_ANSWER_V11036` | **ĐẠT** |
| `DONG_BANG_QD041` | **CON_NGUYEN** |
| `KIEM_CHEO_QD` | **SACH** |
| hook `git commit` | **allow** |
| 4 bảng khoá | **không đụng** — V11037 không ghi DB |

---

## 7. Vướng vấp

**7.1 — Agent suýt chỉ vá `decide()`.** Nhưng `_discordant()` mới là chỗ **đang in số âm ra
trang cho owner đọc**. Hai lỗi ở hai hàm khác nhau, cùng một gốc: **lẫn «số khác nhau» với «kết
quả khác nhau»**. Vá một cái là bỏ nửa chừng (§60).

**7.2 — FU-353 tưởng một gốc, thật ra HAI.** FU-317 là lỗi **bộ đọc** (regex); FU-325 là lỗi
**dữ liệu** (tiêu đề thiếu chữ «hạn»). Nếu chỉ sửa regex thì FU-325 vẫn vô hình; nếu nới regex
đủ rộng để bắt cả FU-325 thì sẽ vơ nhầm ngày trong câu kể.

**7.3 — CỐ Ý HOÃN FU-360.** `database.py:2986` `UPDATE predictions ... WHERE date=? AND
target_region=? AND ai_model=?` **không lọc `run_source`**. Bẫy **chưa nổ** (0 khoá trùng/30
ngày) nhưng **sẽ nổ đúng lúc `QD-015/016/017` chạy 21/08**.

**Vì sao để lại:** hôm nay đã có **bốn** thay đổi (V11032 · V11033 · V11036 · V11037). Đây là
`database.py` — **ghi vào bảng khoá `predictions`**. Vá một chỗ ghi DB ở cuối một phiên dài là
đúng thứ sổ RM đã ghi nhiều lần. Hạn **14/08** — còn thừa thời gian làm đầu phiên.

---

## 8. Gỡ về

```bash
cp backups/v11037_pre/_v10879_nghiemthu_lane.py web/backend/
# VPS:
cp /root/Lottery_AI_Test/backups/v11037_pre/_v10879_nghiemthu_lane.py \
   /root/Lottery_AI_Test/web/backend/ && systemctl restart lottery
```

Bản trước vá: md5 `bdaf2b0206dc9f2a7e7cc0ff94f2e916`. Sao lưu **cả hai đầu**.
Tiêu đề FU-325 trong tracker: khôi phục từ commit trước.

---

## 9. Theo dõi tiếp

| mã | nhãn | hạn | trạng thái |
|---|---|---|---|
| **FU-357 · KS1908** | `decide()` + `_discordant()` — đã vá, 19/08 đọc lại verdict | 19/08 | `DEPLOYED_PENDING_LIVE_VERIFY` |
| **FU-353 · SC0908-2** | hai mục vô hình — đã hiện lại | — | `CLOSED_PASS` |
| **FU-360 · SC1408-2** | `verify_prediction` không lọc `run_source` — **cố ý hoãn** | 14/08 | `MEASURED_BUT_NOT_FIXED` |

### LOCK-IN

- `/nghiem-thu` **không còn ghi «ĐẠT» được** khi p ≥ 0,05
- `_discordant()` **không bao giờ ra số âm** — có `assert` chặn
- Backfill `p = 0,01612` là **chấm ngược**, cấm trích làm bằng chứng
- `FU-317` và `FU-325` **hiện lại** trong briefing đầu phiên

### NEXT ACTION — một bước

**Đầu phiên sau: vá FU-360** — thêm `AND COALESCE(run_source,'') = ?` vào câu UPDATE ở
`database.py:2986`, kèm thử chặn thật (RM-15). **Phải xong trước 21/08.**
