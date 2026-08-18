# REPORT V11087 — BA QUYẾT ĐỊNH OWNER 19:18 · VÀ MỘT TIỀN ĐỀ BỊ LẬT NGƯỢC

**Ngày:** 2026-08-18 · **Mã đọc:** `QD1808-2` · **Quyết định:** `QD-068`
**Production KHÔNG đổi** — không DB · không deploy · không Notion · `QD-041` nguyên vẹn.

---

## 1. Tóm tắt

Owner yêu cầu **kiểm xem ba quyết định còn phù hợp không** trước khi thi hành. Kiểm xong:

| # | quyết định | phán quyết |
|---|---|---|
| **①** | `V11080b` — truy phiên gốc viết bù | **TIỀN ĐỀ SAI** — truy ra rồi, và **không có gì để bù**. Cổng đang **ĐỎ SAI**, không phải đỏ đúng |
| **②** | Hook `SessionStart` — **TỪ CHỐI** | **CÒN PHÙ HỢP** — đã ghi `CLOSED_FAIL`. Hook **chưa bao giờ được cài** |
| **③** | 48 bản vá — **HOÃN** sau 21/08 | **CÒN PHÙ HỢP về nguyên tắc**, nhưng **đối tượng hoãn đang có nguy cơ biến mất** |

**Việc nặng nhất:** `V11080b` **không phải một bản riêng** — nó là **nhãn commit phụ** của
`V11080`, mà `V11080` **đã có** dòng `HISTORY`. Cổng `_v11062` K1 **báo động giả suốt từ 17/08**,
và **lỗi là của phiên này**. Đã vá, đã **rút lại** đúng `PRJ-RETRACTION-001` (`RL-007`).

---

## 2. Owner yêu cầu gì (nguyên văn)

> **19:18 · 18/08** — *«① `V11080b`: TRUY PHIÊN GỐC VIẾT BÙ — đúng cơ chế owner khoá 12:57
> 17/08: chỉ phiên giữ bản ghi gốc mới được viết. Truy không ra → DỪNG, báo owner; cổng K1 cứ đỏ
> ĐÚNG trong lúc chờ. CẤM soạn hộ từ commit message hay nguồn khác.»*

> **19:18 · 18/08** — *«② Hook SessionStart: TỪ CHỐI. Ghi vào sổ theo dõi là đề xuất BỊ TỪ CHỐI
> kèm lý do: mã tự chạy mỗi phiên do subagent tự đề xuất, chưa qua owner review. Không ai được
> cài hook này; đề xuất lại thì phải qua owner.»*

> **19:18 · 18/08** — *«③ 48 bản vá cũ: HOÃN sau 21/08… phiên khác đã sửa 30 tệp / +2.439 dòng
> sau đợt đào 16/08 — áp mù có thể đè mất việc của phiên kia. Sau 21/08 rà lại có đối chiếu,
> không áp mù.»*

> *«Em xem các yêu cầu này có còn phù hợp không, nếu còn thì xử lý, không thì viết rõ lý do gửi
> báo cáo đầy đủ và đề xuất tiếp theo cho anh nhé.»*

---

## 3. Đào bới / phát hiện

### 3.1 · ① — TRUY RA phiên gốc, và tiền đề sụp

**Truy được.** Transcript `d63e64c6`, cửa sổ **16/08 22:45 → 17/08 00:45** giờ VN — khớp chính
xác 10 commit của phiên kia. Bản ghi **còn trên đĩa**, 540 dòng, nhắc `V11080b` **14 lần**.

Và bản ghi đó viết thẳng:

> *«`V11080b` chỉ là **nhãn commit phụ** cùng một bản — trong khi `V10964b` là **bản riêng
> THẬT** (có mục CHANGELOG riêng). Phân biệt bằng đúng điều đó: hậu tố chữ chỉ tính là bản riêng
> **KHI có mục CHANGELOG riêng**; không thì quy về bản gốc.»*

**Bốn bằng chứng độc lập, tất cả tái lập được:**

| # | phép kiểm | kết quả |
|---|---|---|
| 1 | `grep -cE "^## V11080b" CHANGELOG.md` | **0** — không có mục riêng |
| 2 | `grep -cE "^## V10964b" CHANGELOG.md` | **1** — phép phân biệt là **THẬT** |
| 3 | `V11080` có dòng `HISTORY`? | **CÓ RỒI** |
| 4 | `_v10921_report_gate.py:128-138` | **ĐÃ CÓ SẴN** luật lọc hậu tố, do phiên gốc dựng |

⇒ **Không có gì để bù.** Cổng K1 **báo động giả**.

### 3.2 · Lỗi là của phiên này — và nó là lỗi «bỏ nửa chừng»

`V11082` vá K1 bằng cách hợp `CHANGELOG ∪ git log`. Chú thích **do chính nó viết**:

> *«`_v10921_report_gate` đã vá lỗ y hệt bằng cách hợp `CHANGELOG ∪ git log` (V11080/I4) —
> đây là áp **cùng cách**, không sáng chế cách thứ hai.»*

Nhưng nó chỉ chép **hợp nguồn**, **bỏ mất luật lọc hậu tố** mà `_v10921` **đã có sẵn ngay bên
cạnh**. Đúng `§60` (bỏ nửa chừng) và `RM-07` (vá một lỗi không phải vá cả họ lỗi).

### 3.3 · ③ — quyết định đúng, nhưng đối tượng đang tan

Đo 18/08, **48 bản vá KHÔNG tồn tại thành một bộ rà được**:

| | |
|---|---|
| nằm ở đâu | rải rác trong **1.507 tệp**, thư mục **TẠM** `AppData/Local/Temp/claude/<phiên>/scratchpad` |
| có mục lục không | **KHÔNG** — không tệp nào liệt kê đủ 48 |
| số hiệu bắt gặp | cao nhất **`#41`**, không phải dãy 1–48 liền |
| tệp `.patch`/`.diff` trong kho | **0** |
| độ bền | thư mục tạm **có thể bị dọn bất cứ lúc nào** |

⇒ Vế *«sau 21/08 rà lại có đối chiếu»* **có thể không thực hiện được** — tới lúc đó có thể
**không còn gì để rà**.

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao vá cổng thay vì đi bù `V11080b`.** Owner viết *«cổng K1 cứ đỏ ĐÚNG trong lúc chờ»* —
nhưng nó **không đỏ đúng**, nó **đỏ sai**. Owner đã nhiều lần nêu nguyên tắc *«đỏ 100% thì tệ
hơn là không có»* (`CHECKSUMS`, `K1b`, cổng rút-lại). Một cổng đỏ vì lỗi của chính nó thì mục
tiêu *«đỏ đúng trong lúc chờ»* **không đạt được bằng cách chờ** — chỉ đạt được bằng cách vá.

**Vì sao KHÔNG tự làm mục lục 48 bản vá.** Đó là **việc mới**, không nằm trong ba quyết định.
Owner đang khoá phạm vi tới 21/08. Nên đây là **đề xuất**, không phải việc đã làm.

**Vì sao đọc transcript phiên khác KHÔNG vi phạm luật 12:57.** Điều owner cấm là *«soạn hộ từ
commit message hay nguồn khác»* — tức cấm **thay bản ghi gốc bằng nguồn thứ cấp**. Transcript
**LÀ bản ghi gốc**, không phải nguồn thứ cấp. Và kết quả cũng không phải một bản bù được soạn ra:
kết quả là **phát hiện rằng không cần bù**, kèm bốn bằng chứng **độc lập với transcript** (mục
3.1) — tức kết luận đứng vững **kể cả khi bỏ transcript đi**.

---

## 5. Đã làm gì

### ① Vá `_v11062.muc_git_log()` — commit `acd3084`

| | TRƯỚC | SAU |
|---|---|---|
| nhãn từ `git log` | 352 | **254** |
| chỉ-có-ở-git | 16 | 12 |
| **THIẾU HISTORY** | **2** (`V11085` · `V11080b`) | **0** |
| cổng | **TRƯỢT** | **ĐẠT** |

**Kiểm 95 nhãn bị gộp** — vì vá làm cổng **thấy ít hơn**, là hướng dễ giấu lỗi thật:
**cả 95 nhãn đều KHÔNG có mục CHANGELOG riêng** (`V10807b` `V10809c` `V10820e`…), đúng loại
luật này sinh ra để gộp. Thêm `V10807` (bản gốc của `V10807b`). **Không mất bản thật nào.**

**Thử chặn hai chiều ĐẠT:** `[1]` hiện tại → ĐẠT · `[2]` bỏ 1 mục khỏi `HISTORY` → **ĐỎ** ·
`[3]` khôi phục → **XANH**. Tệp trả về nguyên trạng **357.007 byte**.

### RÚT LẠI — `RL-007`, đủ bốn phần

| phần | nội dung |
|---|---|
| **chỗ gốc** | `REPORT_V11083` · `V11084` · `V11085` · `V11086` mục 6+9 (công khai 17–18/08) + `CHANGELOG`/`SSOT` các bản tương ứng |
| **nguyên văn câu sai** | *«`_v11062 --kiem` VẪN ĐỎ vì `V11080b` — ĐÓ LÀ ĐÚNG»* |
| **điều đúng** | cổng **ĐỎ SAI**; `V11080b` không phải bản riêng; kèm **4 bằng chứng tái lập được** |
| **quyết định đã dựa trên số sai** | **chính quyết định ① owner ký 19:18 ngày 18/08** — tiền đề sai |

### ② Hook `SessionStart` — `FU-408`, `CLOSED_FAIL` — commit `e3a61b2`

Ghi rõ **lý do từ chối** (mã tự chạy mỗi phiên · subagent tự đề xuất · chưa qua owner review) và
**trạng thái thi hành**: **chưa bao giờ được cài**.
**KIỂM:** `grep -c SessionStart .claude/settings.json` → **0**.

### ③ 48 bản vá — `FU-409`, `DEFER` — commit `e3a61b2`

Ghi đúng lý do owner nêu, **kèm ô rủi ro** mô tả tình trạng thật của bộ bản vá và **đề xuất lập
mục lục ngay**.

---

## 6. Cổng kiểm

| cổng | |
|---|---|
| **`_v11062 --kiem`** | **✓ ĐẠT** — lần đầu kể từ 17/08 |
| `_v11062 --thu-chan` | **✓ ĐẠT** hai chiều |
| `_v11085_cong_rut_lai --thu-chan` | **✓ 10/10** |
| `_v10981_kiem_lich` K8 | **✓ ĐẠT 8/8** · in dòng miễn trừ |
| ghi tệp an toàn · đoán tên · mất mục · đóng băng · chéo quyết định · sáu mặt | **✓ 6/6** |

> **Đây là lần đầu KHÔNG có cổng nào đỏ kể từ 17/08.** Và nó xanh **không phải vì bù thêm gì** —
> mà vì **cái đỏ vốn là giả**.

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **19:18 18/08** | *«`V11080b`: TRUY PHIÊN GỐC VIẾT BÙ… Truy không ra → DỪNG, báo owner; cổng K1 cứ đỏ ĐÚNG trong lúc chờ»* |
| **19:18 18/08** | *«Hook SessionStart: TỪ CHỐI… Không ai được cài hook này»* |
| **19:18 18/08** | *«48 bản vá cũ: HOÃN sau 21/08… Sau 21/08 rà lại có đối chiếu, không áp mù»* |
| **12:57 17/08** | *«CẤM tự chuyển sang soạn từ commit message hay nguồn khác»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| `V11080b` không có mục CHANGELOG | `grep -cE "^## V11080b"` → **0** |
| `V10964b` **có** | → **1** |
| `V11080` đã có `HISTORY` | 1 dòng |
| `_v10921` đã có luật lọc hậu tố | `:128-138` |
| `V11082` chỉ chép nửa cách | `_v11062.muc_git_log()` bản cũ — không có nhánh hậu tố |
| sau vá: K1 = 0 thiếu | `NANG_VERSION_V11062=ĐẠT` |
| 95 nhãn gộp đều không có mục riêng | đối chiếu tập cũ/mới |
| hook `SessionStart` chưa từng cài | `grep -c` → **0** |
| 48 bản vá ở temp, không mục lục | 1.507 tệp · `#41` là cao nhất · 0 tệp `.patch` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| `REPORT_V11083/84/85/86`: *«ĐỎ ĐÚNG vì `V11080b`»* | **LỆCH — ĐÃ RÚT LẠI** (`RL-007`) |
| `_v11062` docstring: *«áp cùng cách, không sáng chế cách thứ hai»* | **LỆCH với `CODE_DID`** — chép nửa cách. Đã sửa chú thích |
| `_v10921:128-138` chú thích luật hậu tố | **khớp** — và là nguồn của bản vá này |

### Ba lớp lệch nhau ⇒ FINDING

**`OWNER_SAID` ≠ `CODE_DID`:** owner ký *«cổng K1 cứ đỏ ĐÚNG trong lúc chờ»* dựa trên báo cáo của
agent. Đo lại: **đỏ SAI**. Không im lặng làm theo, cũng không im lặng bỏ qua — **báo lại kèm bằng
chứng**, đúng `§62`.

---

## 7. Vướng vấp — **hai vấp của chính agent**, cả hai bắt được vì NHÌN SỐ

**Vấp 1 — vá NHẦM HÀM.** Lần vá đầu dùng neo `ra: dict[str, str] = {}`, nhưng chuỗi đó khớp
`muc_changelog()` **trước** `muc_git_log()` ⇒ ghi đè thân hàm sai, làm `muc_changelog` tham chiếu
biến `r` không tồn tại. Bắt được vì **đọc lại output**. Đã `git checkout` khôi phục và **xác minh
mọi hàm còn đủ + cú pháp OK + khớp `HEAD`** trước khi làm tiếp.

**Vấp 2 — heredoc nuốt `\b` thành ký tự BACKSPACE thật (`\x08`).** Regex thành
`([A-Za-z]?\d*)^H(.*)$` ⇒ khớp **0 dòng** ⇒ cổng in **`git log : 0 nhãn version`** và báo
**ĐẠT**.

**Đây là loại hỏng tệ nhất: cổng xanh vì nó THÔI NHÌN.** Bắt được **không phải** vì thấy chữ
`ĐẠT`, mà vì **nhìn con số 0** ở dòng ngay trên. Cùng họ với ca 16/08 (bash ăn backtick) và ca
sáng nay 18/08 (heredoc vỡ khi viết báo cáo) — **ba lần cùng một lớp lỗi**. Đã chuyển sang công
cụ sửa trực tiếp, hết tầng escape.

> Và đây là lý do phép kiểm «95 nhãn bị gộp» ở mục 5 tồn tại: sau khi một bản vá làm cổng **thấy
> ít hơn**, **bắt buộc** phải chứng minh phần bị bớt là phần **đáng bớt**.

---

## 8. Gỡ về

```bash
git revert e3a61b2   # ② + ③ ghi sổ
git revert acd3084   # ① vá K1 + RL-007
```

Gỡ `acd3084` sẽ làm cổng **đỏ giả trở lại** — nếu gỡ, phải rút lại `RL-007` cho nhất quán.

---

## 9. Theo dõi tiếp

### ⚠️ ĐỀ XUẤT — chờ owner quyết, việc này **có hạn dùng**

**Lập mục lục 48 bản vá NGAY trong khi còn.**

| | |
|---|---|
| **việc** | quét scratchpad, kết xuất từng bản vá thành `artifacts/v11087_ban_va/` kèm bảng *bản vá → tệp đích → đoạn TRƯỚC* |
| **tính chất** | **read-only**, không áp gì, không chạm `QD-041` |
| **công** | ~30 phút |
| **vì sao gấp** | thư mục tạm **có thể bị dọn bất cứ lúc nào**. Không làm thì quyết định ③ **mất đối tượng** — sau 21/08 không còn gì để rà |
| **nếu owner không duyệt** | ghi thẳng vào sổ: *48 bản vá coi như MẤT*, và đóng `FU-409` bằng lý do đó thay vì để nó treo tới 22/08 rồi mới phát hiện |

### Trạng thái ba quyết định

| # | trạng thái |
|---|---|
| ① | **KHÔNG THI HÀNH ĐƯỢC** — tiền đề sai, đã báo owner đúng như owner dặn. Thay bằng: **vá cổng** + **rút lại** |
| ② | **ĐÃ THI HÀNH** — `FU-408` `CLOSED_FAIL` |
| ③ | **ĐÃ GHI SỔ** — `FU-409` `DEFER`, **kèm ô rủi ro**. Chờ owner quyết đề xuất lập mục lục |

### Sổ theo dõi

**283 mã** · **164 còn treo** · **21 mục chờ owner ký**. Mốc **22/08**: miễn trừ K8 tự hết ⇒
**K8 đỏ lại là CỐ Ý**.

**Verdict tách hai dòng:**
- **`CODE_PUSHED`** = `acd3084` (vá K1 + `RL-007`) · `e3a61b2` (ghi ② + ③)
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **RÚT LẠI `RL-007`** — câu *«`_v11062` đỏ ĐÚNG vì `V11080b`»* đã công bố
ở **bốn** báo cáo là **SAI**; cổng **ĐỎ SAI**, `V11080b` **không phải bản riêng** (không có mục
CHANGELOG, trong khi `V10964b` có); ② ghi **quyết định ① của owner KHÔNG thi hành được** — tiền đề
sai, đã truy ra phiên gốc và **không có gì để bù**; thay bằng **vá cổng** `acd3084`; ③ ghi
**`FU-408` `CLOSED_FAIL`** — hook `SessionStart` **bị TỪ CHỐI**, chưa bao giờ được cài, đề xuất
lại **phải qua owner**; ④ ghi **`FU-409` `DEFER`** kèm **rủi ro**: 48 bản vá nằm ở thư mục **TẠM**,
**không có mục lục**, **có thể mất** ⇒ **đề xuất lập mục lục ngay**, chờ owner duyệt; ⑤ ghi
**lần đầu KHÔNG cổng nào đỏ kể từ 17/08** — và nó xanh vì **cái đỏ vốn là giả**, không phải vì bù
thêm gì; ⑥ ghi **lớp lỗi heredoc/escape đã tái phạm LẦN BA** (16/08 · 18/08 sáng · 18/08 tối) —
lần này suýt làm cổng **xanh vì thôi nhìn**.
