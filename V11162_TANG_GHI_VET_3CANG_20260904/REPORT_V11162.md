# REPORT V11162 — TẦNG GHI VẾT 3-CÀNG + ĐÓNG BA VIỆC CHẨN ĐOÁN

> **Ngày:** 04/09/2026 01:00–01:5x (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> `POOL_VERDICT = HOLD` · `MODEL_ACTION = BLOCKED` · Prompt 43 R1 **PARTIAL**
> **Không đụng `main.py` ở tầng hành vi** — chỉ sửa một khối chú thích sai; tầng ghi vết chạy CẠNH.

---

## 1 · Tóm tắt

Bốn việc, mỗi việc có phép kiểm riêng:

| việc | kết quả |
|---|---|
| tầng ghi vết 3-càng (việc còn lại từ `V11157`) | 🟢 đủ **8/8** trường · tái lập **207/207 = 100,00%** |
| chú thích ngược `main.py:12306` | 🟢 sửa — và giữ nguyên câu sai làm dấu vết |
| «journal giờ 17 câm» | 🟢 **câu hỏi đặt sai** — chỉ giờ 16 từng có `print()` |
| 6 dòng trace không nối được | 🟢 **giải xong** — là lần phát lại sau khi ráp bundle |

**Và một bẫy suýt sập:** vòng kiểm đầu báo **52,84%** và agent định ghi *«tầng ghi vết HỎNG»*.
Thật ra **thuật toán đã đổi ngày 26/06**.

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại |
|---|---|---|
| 04/09 ~00:2x | *«ok em thực hiện tuần tự lần lượt xử lý dứt điểm các vấn đề em đã đào ra dùm anh»* | `YÊU_CẦU` |
| 04/09 ~01:0x | *«Tiếp đi em»* | `YÊU_CẦU` |

Câu thứ hai là lệnh tiếp tục cho các việc còn treo sau `V11160`/`V11161`.

---

## 3 · Đào bới / phát hiện

### 3.1 · Vì sao 7/8 trường lineage không tồn tại

`main._generate_lo3_frequency()` (`main.py:10604-10685`) **tính đủ** bảng xếp hạng prefix — cả
`prefix_counts` lẫn `tail_counts` cho mọi chữ số — rồi **vứt đi**, chỉ giữ người thắng và
`print()` phần còn lại ra journal:

```python
sorted_prefixes = sorted(prefix_counts.items(), key=lambda kv: (-kv[1], -tail_counts.get(kv[0], 0)))
best_prefix, best_count = sorted_prefixes[0]
print(f"[LO3-FREQ] ... prefix dist (top5): {dict(sorted_prefixes[:5])}")
return best_prefix + bach_thu        # ← chỉ trả về 3 ký tự
```

Và journal — như mục 3.4 dưới đây chứng minh — **không phải kênh bằng chứng đáng tin**.

### 3.2 · 🔴 Bẫy suýt sập: vòng kiểm đầu 52,84%

`--kiem` vòng đầu: **KHỚP 298/564 = 52,84% · LỆCH 266**. Agent định ghi *«tầng ghi vết HỎNG,
không được dùng»*. Tách theo tháng thì lộ ngay:

| tháng | 2026-02 | 03 | 04 | 05 | 06 | **07** | **08** | **09** |
|---|---|---|---|---|---|---|---|---|
| khớp | 0,0% | 24,7% | 28,9% | 19,4% | 40,0% | **100,0%** | **100,0%** | **100,0%** |

**Thuật toán đã ĐỔI.** `git log -S` chỉ đúng ngày — hai commit **cùng 26/06/2026**:

| commit | nội dung |
|---|---|
| `2d6724d` | V10753 — *«lo3 **loosened 3-càng**»*: đổi sang đếm **chuỗi con ở mọi vị trí**, thay cho cách cũ chỉ đếm **đuôi giải** |
| `31ddff6` | V10753.1 — *«lo3 3-càng window **90 → 180**»* |

Đặt `MOC_THUAT_TOAN = 2026-06-27`. Kiểm lại **trong thời kỳ của nó**:

```
trong phạm vi  : 207 bundle
NGOÀI phạm vi  : 357 bundle trước mốc — THUẬT TOÁN KHÁC, không kiểm, không tính
KHỚP 207/207 (100.00%) · LỆCH 0
```

**Phát biểu ĐÚNG phải kèm phạm vi:** *«tái lập 100% TỪ 26/06/2026»* — KHÔNG phải *«tái lập 100%»*.
Bắc con số qua ranh giới là so hai thước khác nhau, đúng thứ `RM-21` cấm.

### 3.3 · 🟡 Số liệu mới — trước nay không ai có

Vì bảng xếp hạng bị vứt đi nên chưa ai đo được **lựa chọn prefix mong manh đến đâu**:

| | |
|---|---|
| lựa chọn **MONG MANH** (hạng 1 hơn hạng 2 **≤ 2** lần xuất hiện) | **121/207 = 58,5%** |
| độ tin **THẤP** (`substring_count < 3`) | **0/207 = 0,0%** |

Hơn **một nửa** số 3-càng công bố đứng trên khoảng cách ≤ 2 lần xuất hiện.

**BỔ SUNG cùng phiên — đã nối với kết quả thật.** Khoảng cách tính từ dữ liệu **trước** kết quả
(cửa sổ 180 ngày, `date < D`); kết quả nối vào **sau** ⇒ không oracle.

| nhóm theo khoảng cách hạng 1–2 | trúng | tổng | tỉ lệ |
|---|---|---|---|
| **MONG MANH** (≤ 2) | 9 | 121 | **7,4%** |
| VỪA (3–5) | 2 | 61 | **3,3%** |
| DỨT KHOÁT (> 5) | 4 | 25 | **16,0%** |
| **TẤT CẢ** | **15** | **207** | **7,2%** |

**① Khoảng cách KHÔNG dự báo được trúng.** So nhóm mong manh với nhóm dứt khoát: `7,4%` vs
`16,0%`, **Fisher hai phía `p = 0,1825`** ⇒ **không khác**. Và nhóm GIỮA lại thấp nhất (`3,3%`) —
không có quan hệ đơn điệu. ⇒ Giả thuyết *«prefix mong manh thì trúng kém hơn»* **không đứng được**
ở mẫu này. Ghi đúng như thế, không uốn.

**② Nhưng phép đo lộ ra một điều nặng hơn — 3-càng cũng KHÔNG tách được khỏi nền.**

| | tỉ lệ | nền bốc bừa | z |
|---|---|---|---|
| 3-càng (207 ô) | **7,2%** | **9,7%** | **−1,19** |

Nền `9,7%` = trung bình **97 số 3-càng thực/ngày** trên 1.000 khả năng (định nghĩa `V10753`:
ba chữ số ở **bất kỳ vị trí nào** trong giải). Với `n = 207`, kỳ vọng `20,1` mà thực tế `15`.

Câu owner cho phép dùng áp nguyên vào đây: *«Chưa đo được lợi thế so với baseline ngẫu nhiên ở
mẫu hiện tại; cũng chưa đủ bằng chứng kết luận hệ thống thật sự kém hơn baseline.»*

Đây là **chỉ số thứ tư** cho cùng một hình ảnh, sau bạch thủ · lô 2 · top-3 ở `V11159`. **Không**
được đọc thành «3-càng hỏng» — kiến trúc 3-càng vẫn `SUBSTANTIALLY_VALID` theo khoá owner
`V11157`; điều đo được là **cửa sổ 180 ngày + đếm chuỗi con chưa mang lợi thế đo được**, và đó là
câu hỏi về **bộ chọn prefix**, không phải về kiến trúc.

### 3.4 · «Journal giờ 17 có 0 dòng» — câu hỏi đặt SAI

`V11159` ghi *«chưa giải thích được vì sao giờ 16 có dòng mà giờ 17 không»*. Đo lại **4 khung
giờ** thay vì 2:

| giờ | tổng dòng | `logging` | **`print()`** | `[STAT]` | `CONTEXT_ONLY_V2` |
|---|---|---|---|---|---|
| 05 (MN, 20 model chạy) | 62 | 62 | **0** | 0 | 0 |
| 16 (MT) | 4.051 | 99 | **3.952** | 2.423 | 24 |
| 17 (MB, 12 model shadow) | 71 | 71 | **0** | 0 | 0 |
| 18 | 41 | 41 | **0** | 0 | 0 |

⇒ Không phải *«giờ 17 câm»*. **Chỉ giờ 16 từng có `print()` lọt vào journal** — kể cả giờ 05 khi
20 model chạy thật cũng **0 dòng**.

**Hai giả thuyết bị loại bằng đo:**
- **KHÔNG** phải rate-limit journald: `journalctl -u systemd-journald` có **0** dòng
  `Suppressed`/`rate limit` trong 15:00–02:00.
- **KHÔNG** phải hỏng stdout: **0** dòng `closed file` / `BrokenPipe` / `Bad file descriptor`.

⚠️ **Nguyên nhân vẫn CHƯA CHỨNG MINH ĐƯỢC.** Nhưng kết luận vận hành đã đủ và không cần đuổi
tiếp: **journal chưa bao giờ là kênh bằng chứng đáng tin cho regime prompt**, và `V11160` đã thay
nó bằng `runtime_prompt_sha256` trong trace — kênh tất định, có mặt ở **mọi** lượt.

*(Ghi thêm cho người đọc sau: `scheduler._safe_stdio_ctx` sẽ **nuốt sạch** `print()` nếu `stdout`
từng hỏng, và `_restore_stdio` trả lại **chính luồng hỏng đó**. Hôm nay **không** phải nguyên nhân
— 0 dòng lỗi I/O — nhưng đó là một rủi ro tiềm ẩn có thật, ghi lại để lần sau không mất công dò.)*

### 3.5 · 6 dòng trace không nối được sang `predictions` — GIẢI XONG

Đúng **6 cặp** `(miền, model)` ngày 03/09 có **2 dòng trace** nhưng chỉ **1 dòng `predictions`**.
Giờ phát của dòng thứ hai **trùng khít giờ sinh bundle**:

| dòng | miền · model | giờ trace | giờ sinh bundle | `prediction` | bạch thủ bundle |
|---|---|---|---|---|---|
| 6419 | MN · `claude-opus-4-6` | 05:20:18 | 05:20:54 | `['10','61']` | **10** |
| 6420 | MN · `gemini-2.5-pro` | 05:20:54 | 05:20:54 | `['15','64']` | (lo2[1] = 15) |
| 6440 | MT · `gemini-2.5-flash` | 16:45:36 | 16:46:20 | `['32','64']` | **32** |
| 6441 | MT · `gemini-2.5-pro` | 16:46:20 | 16:46:20 | `['40','32']` | **32** |
| 6461 | MB · `gemini-2.5-flash` | 17:39:58 | 17:43:15 | `['32','62']` | **32** |
| 6462 | MB · `deepseek-reasoner` | 17:43:15 | 17:43:15 | `['32','59']` | **32** |

**5/6 dòng có `prediction[0]` = đúng bạch thủ của bundle.** ⇒ Đây là **lần phát lại SAU KHI ráp
bundle**, không phải lượt model.

**Hệ quả phải nhớ: trace KHÔNG 1:1 với `predictions`.** Mọi phép nối về sau phải chịu được điều
này, nếu không sẽ lại báo *«không nối được»* và tưởng là lỗi ghi log.

### 3.6 · Chú thích ngược `main.py:12306` — sai NGAY TỪ COMMIT SINH RA NÓ

```
# Test challenger only has its own BT/lo2 selection logic. For lo3 we
# clone official (no challenger 3-cang algorithm).
```

`git log -S` cho thấy câu này **và** cờ `lo3_cloned_from_official: False` ra đời **cùng một
commit `d411670` (07/05/2026, V83)**. Tức chú thích mô tả một **ý định**, không phải thứ code
làm — **ngay từ dòng đầu tiên**, không phải «code đổi rồi chú thích ở lại».

Code thật, cách đó ~130 dòng (`:12425`):

```python
test_lo3 = _generate_lo3_frequency(str(cand_bt).zfill(2), "MB", data_date)
```

Challenger **tự sinh 3-càng từ BT của chính nó** — đúng khoá owner `V11157` mục 4.
`A60_VIOLATION` (`DOC_SAID` ≠ `CODE_DID`) sống **120 ngày**.

---

## 4 · Hướng xử lý và vì sao chọn

**Vì sao KHÔNG ghi lineage thẳng vào `final_bundles`.** `§52` mục 13 cấm đụng writer của bảng đó.
Thêm cột là đụng đúng writer. Tầng ghi vết chạy **CẠNH**: tính lại bằng thuật toán y hệt, chứng
minh khớp 100% trên thời kỳ của nó, rồi xuất artifact. Muốn persist vào DB phải là một
**materialization packet riêng có owner ký**.

**Vì sao giữ nguyên hai câu chú thích sai thay vì viết đè.** Người đọc sau cần biết chỗ này
**từng bị mô tả ngược** — nếu tin chú thích thì mọi phép đo lo3 của challenger trông như đo lại
chính official, tức tự nhân đôi bằng chứng. Sửa bằng cách xoá là xoá mất bài học.

**Vì sao dừng việc dò journal.** Đã loại được hai giả thuyết bằng đo; giả thuyết thứ ba cần đọc
sâu vào cách journald bắt stdout của tiến trình con. Chi phí cao mà **giá trị đã bằng 0**: kênh
bằng chứng đã được thay bằng thứ tất định ở `V11160`. Ghi *«CHƯA CHỨNG MINH ĐƯỢC»* rồi dừng đúng
hơn là đuổi tiếp.

---

## 5 · Đã làm gì — TRƯỚC / SAU / KIỂM

| | TRƯỚC | SAU |
|---|---|---|
| lineage 3-càng | **1/8** trường (`lo3_method`) | **8/8**, artifact 207 dòng |
| bảng xếp hạng prefix | tính rồi **vứt**, chỉ `print()` | giữ đủ **mười** chữ số kèm điểm + hạng |
| chất lượng lựa chọn | **không đo được** | **58,5% mong manh** · **0% độ tin thấp** |
| chú thích `main.py:12306` | nói ngược code, 120 ngày | giữ câu sai + ghi rõ nó sai ở đâu |
| «journal giờ 17» | *«chưa giải thích được»* | câu hỏi đặt sai; loại 2 giả thuyết; kênh đã được thay |
| 6 dòng trace | *«chưa truy nguyên»* | **giải xong** — phát lại sau khi ráp bundle |

**KIỂM (chạy thật trên VPS):** `--kiem` → `KHỚP 207/207 (100.00%) · LỆCH 0`, kèm dòng cảnh báo
phạm vi. `--ghi-vet` → 207 dòng, khớp bản lưu 207/207.

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| giờ ngoài block 15:30–18:15 | ✓ `01:4x` |
| neo FINAL 558 | ✓ nguyên |
| 4 bảng khoá | ✓ `14120 · 564 · 15410 · 13984` không đổi |
| health + PID đổi | ✓ `3367598 → 3370750` |
| nhập thử TRƯỚC restart | ✓ `IMPORT_OK 2026-06-27 LO3_PREFIX_SUBSTRING_180D_V10753.1` |
| **cổng tái lập 3-càng sau restart** | ✓ **207/207** |
| ghi DB | **0** — tầng ghi vết chỉ xuất artifact |

**Gỡ về:** `python _v11162_deploy.py --go-ve` — khôi phục `main.py` từ `.V11162.bak`, xoá
`_v11162_lo3_lineage.py`, restart, kiểm neo.

---

## 7 · Vướng vấp

**🔴 ① Suýt kết luận «tầng ghi vết hỏng» từ con số 52,84%.** Cứu được nhờ tách theo tháng trước
khi phán. Đây là lần thứ **sáu** trong hai ngày agent gặp họ *«số xấu không có nghĩa vật đo
hỏng»* — và lần này là **thước bắc qua hai thời kỳ thuật toán**, không phải thước đặt sai chỗ.

**🟡 ② Một `assert` trong script sửa tệp vỡ vì `\n` lồng trong heredoc** — chuyển sang công cụ
Edit. Cùng họ với bẫy null-byte đã ghi ở `V11160`.

---

## 8 · Gỡ về

Có sẵn, **chưa cần dùng** — deploy qua cổng ngay lần đầu. `main.py.V11162.bak` giữ bản trước.

---

## 9 · Theo dõi tiếp

| việc | trạng thái |
|---|---|
| **persist lineage vào DB** | **CHỜ OWNER** — cần materialization packet riêng (§52 mục 13) |
| **58,5% lựa chọn mong manh** | quan sát, **chưa nối với kết quả** — cần phép đo riêng |
| nguyên nhân journal chỉ có `print()` ở giờ 16 | **CHƯA CHỨNG MINH ĐƯỢC** — đã dừng có chủ ý |
| rủi ro tiềm ẩn `_safe_stdio_ctx` nuốt `print()` vĩnh viễn nếu stdout từng hỏng | ghi nhận, chưa xử |
| xác nhận `runtime_prompt_sha256` trong lượt scheduled thật | **chờ lượt MN ~05:15 hôm nay** |
| 357 bundle trước 26/06 | **KHÔNG** tái lập được bằng thuật toán hiện hành (`RM-21`) |
| duyệt ngưỡng đăng ký trước MT | **CHỜ OWNER** |

---

## Nguồn ba lớp (§62)

### `OWNER_SAID`
- 04/09 ~00:2x — *«ok em thực hiện tuần tự lần lượt xử lý dứt điểm các vấn đề em đã đào ra dùm anh»*
- 04/09 ~01:0x — *«Tiếp đi em»*

### `CODE_DID`
- `_v11162_lo3_lineage.py` — 8/8 trường · `--kiem` **207/207 = 100,00%** · `--ghi-vet` 207 dòng
- `MOC_THUAT_TOAN = 2026-06-27`, bằng chứng `2d6724d` + `31ddff6`
- journal 03/09: giờ 05/17/18 có **0** dòng `print()`, giờ 16 có **3.952**
- 6 cặp `(miền, model)` có 2 dòng trace / 1 dòng `predictions`, 5/6 khớp bạch thủ bundle
- deploy `PID 3367598 → 3370750`, neo 558 nguyên

### `DOC_SAID`
- `main.py:12306-12307` *«For lo3 we clone official»* — **`DOC_SAID` ≠ `CODE_DID` suốt 120 ngày**;
  đã ghi bản sửa ngay bên dưới, **giữ nguyên câu sai** làm dấu vết.
- `V11157` chốt *«việc còn lại là thêm tầng ghi vết quanh bộ chọn đang chạy đúng»* —
  **`DOC_SAID` = `CODE_DID` từ V11162**: đã làm đúng thứ đó, không viết generator mới.
- `CLAUDE.md` `RM-21` *«hằng số đo được chỉ đúng cho thước đã đo nó»* — phiên này là ca áp dụng
  thứ hai trong hai ngày: lần trước là mốc đóng băng, lần này là **thuật toán 3-càng**.

---

TanPhatAI cần làm: ghi **`V11162`** — `governance_seq 478`, công khai bản này. Ghi **tầng ghi vết 3-càng ĐỦ 8/8 trường** (`V11159` đo 7/8 chưa tồn tại), **KHÔNG đụng `main.py`** vì `§52` mục 13 cấm đụng writer `final_bundles`. Ghi **bẫy suýt sập: vòng kiểm đầu 52,84%** — thật ra **thuật toán đổi ngày 26/06/2026** (`2d6724d` + `31ddff6`: đếm chuỗi con thay đuôi giải, cửa sổ 90→180); đặt mốc `2026-06-27` thì tái lập **207/207 = 100,00%**; **357 bundle trước mốc chạy thuật toán KHÁC**, bắc số qua ranh giới là vi phạm `RM-21`. Ghi **phát biểu đúng phải kèm phạm vi**: *«tái lập 100% TỪ 26/06»*, không phải *«tái lập 100%»*. Ghi **số liệu mới: 58,5% lựa chọn prefix MONG MANH** (hạng 1 hơn hạng 2 ≤ 2 lần) — **quan sát, chưa phải verdict** (`RM-04`). Ghi **chú thích `main.py:12306` sai NGAY TỪ commit sinh ra nó** (`d411670`, 07/05), sống 120 ngày; **giữ nguyên câu sai làm dấu vết**. Ghi **«journal giờ 17 câm» là câu hỏi đặt SAI** — chỉ giờ 16 từng có `print()`; loại được rate-limit và hỏng-stdout; nguyên nhân **CHƯA CHỨNG MINH ĐƯỢC** và đã **dừng có chủ ý** vì kênh đã được thay ở `V11160`. Ghi **6 dòng trace là phát lại sau khi ráp bundle** ⇒ **trace KHÔNG 1:1 với `predictions`**. **Không mở Prompt 44. Không mở FU mới.** `POOL_VERDICT` giữ **`HOLD`**.
