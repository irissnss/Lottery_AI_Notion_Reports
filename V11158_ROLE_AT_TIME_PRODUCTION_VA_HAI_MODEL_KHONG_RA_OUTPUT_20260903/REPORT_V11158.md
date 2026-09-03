# REPORT V11158 — role-at-time vào production · owner báo «2 model không ra output»

> **Ngày:** 03/09/2026 · **Giờ:** 12:40–13:55 (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> **Prompt 43 R1 giữ `PARTIAL`** — không mở Prompt 44 · `POOL_VERDICT = HOLD` · `MODEL_ACTION_BLOCKED`
> **Official không đổi một ký tự prompt** — chứng minh bằng 6 băm, không phải bằng lời hứa.

---

## 1 · Tóm tắt

Phiên này làm hai việc, việc thứ hai do owner cắt ngang giữa chừng và **quan trọng hơn**.

**Việc đã lên lịch** — đưa bản vá *role-at-time* vào production rồi tính lại 540 cặp
`(ngày, miền)`. Xong, idempotent, có sổ before/after 8.287 mục. Nhưng khi đo để chuẩn bị thì lộ
ra bản vá `V11155` **mới dọn được 279 trong 1.058** dòng thua ảo — phải vá nốt họ lỗi (`RM-07`).

**Việc owner giao giữa phiên** — *«2 model này không ra output»*. Tra ra **hai nguyên nhân khác
nhau**, cả hai đều là **lỗi hạ tầng**, và cả hai đang **tự trừ điểm model**: một lượt không ra
số nào vẫn bị chấm `LOSE`. Với `glm-5.2` điều đó ăn mất **10,3 điểm** win-rate 30 ngày.

Bốn bản vá, deploy đủ trước block 15:30. Neo FINAL 558 nguyên qua **tám** lần restart.

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN

> Mục này đọc theo `PRJ-INTERACTION-LEDGER-001`: **prompt chính VÀ mọi yêu cầu trực tiếp trong
> phiên**, nguyên văn + giờ.

| giờ (VN) | NGUYÊN VĂN | loại | trạng thái |
|---|---|---|---|
| (phiên trước) | `PROMPT 43 R1 · CONTINUATION` mục `B` — *«Áp materializer repair vào production theo backup/migration gate… Repair/recompute đúng tập 877 dòng… Giữ before/after audit theo row ID, prediction ID, vai trò cũ/mới, reason code và artifact hash… Rerun phải idempotent… Neo FINAL và dữ liệu lịch sử immutable không drift.»* | `YÊU_CẦU` | `ĐÃ_LÀM` |
| 03/09 ~13:05 | *«⚠️ 🔬 DeepSeek Reasoner 43% 30d · ⚠️ 🤖 GLM 5.2 45% 30d — 2 model này không ra output sẵn kiểm tra dùm anh luôn em»* | `YÊU_CẦU` | `ĐÃ_LÀM` |
| 03/09 ~13:20 | *«fix cho chạy ra output luôn chứ em. Chưa tới giờ block mà em.»* | `YÊU_CẦU` | `ĐÃ_LÀM` |

**Owner đúng ở cả hai câu.** Hai model đó thật sự không ra output — và thời điểm nhắc (13:20)
đúng là còn **2 giờ 10 phút** trước block, đủ cho cả bốn bản vá.

---

## 3 · Đào bới / phát hiện

> Liệt kê **đủ**, kể cả phép đo ra kết quả âm hoặc chưa kết luận được (§57.3).

### 3.1 · Phạm vi recompute — đo trước khi ghi

`540 cặp (ngày, miền)` từ `2026-03-07` đến `2026-09-02`. Bảng chấm trước khi đụng: **12.382**
dòng. Tái lập được đúng **877** dòng owner nêu — bằng phép *«dòng ghi `MISSING_SHADOW_ROW`
NHƯNG thực tế CÓ dòng trong `predictions`»*.

### 3.2 · 🔴 `V11155` mới vá được **279/1.058** thua ảo — phải vá cả họ (`RM-07`)

`V11155` sửa nhánh **CÓ dự đoán** (`_ho()`). Nhánh `_thieu` **vẫn** lấy roster HÔM NAY áp cho
ngày cũ — **cùng một lookahead, chiều ngược lại**. Phân rã 4 lớp trên DB production:

| lớp | dòng | trong đó tính THUA |
|---|---|---|
| `PRE_EXISTENCE_COVERAGE_GAP` — model **chưa ra đời** ngày đó | 2.352 | **760** |
| `ROLE_AT_TIME_CLASSIFICATION_ERROR` — `V11155` đã vá | 877 | 279 |
| `TRUE_MISSING_OUTPUT` | 67 | 19 |
| **cộng** | **3.296** | **1.058** |

Đối chiếu: thua THẬT (có dự đoán, trượt) = **1.423** ⇒ **1.058/2.481 = 42,6% cột
`would_flip_baseline_to_lose` là ẢO**. Nguồn của lớp lớn nhất: **14 model** xuất hiện lần đầu
sau `2026-03-07` (`glm-5.2` từ 05/07, `claude-opus-5-fast` từ 30/07…) nhưng roster hôm nay đem
áp ngược về tận tháng 3.

### 3.3 · Quét ngược người đọc (§60.2/§60.3) — kết quả ÂM, và đó là tin tốt

| chỗ | loại | dùng cột thua? | ảnh hưởng |
|---|---|---|---|
| `_v11102_bang_cong_don.py:99,104,138` | **READER SỐNG** | có | **đã chặn sẵn** `WHERE parse_ok = 1` |
| `_v11102_don_dong_ro.py` · `_v11102_kiem_thuoc_model.py` · `_v10644_shadow_scoreboard.py` | reader | không | không đụng |
| `main.py:19857` · `pnl_router.py:288` · `du-doan-test.html:3601` | reader | **bảng KHÁC** (`shadow_results`, lane, `experimental_preview_shadow`) | không liên quan |
| `_v87_master_board.py:248` | tài liệu | chỉ liệt kê tên metric | không đụng |

Đo trên production: **3.296/3.296** dòng MISSING đều `parse_ok=0` ⇒ bộ gom **chưa bao giờ**
nuốt thua ảo. **Không route `/du-doan` nào, không frontend nào** đọc bảng này (§52 mục 13 an toàn).

### 3.4 · 🟢 `deepseek-reasoner` — chứng minh CƠ CHẾ, không dựa n nhỏ

Gọi **thật** bằng đúng prompt production (`SYSTEM_SERVED` + `USER_PAYLOAD` dump từ hàm đang
phục vụ — `RM-14`):

| miền | `reasoning_tokens` | tổng token | giây | `finish_reason` |
|---|---|---|---|---|
| MB | **40.215** | 53.163 | 336 | `stop` |
| MN | 24.345 | 36.943 | 199 | `stop` |

Trần cũ **32.768**. Lượt MB có **phần suy luận một mình đã vượt trần 7.447 token** — trước cả
khi model kịp viết ký tự JSON đầu tiên. Ở trần cũ lượt đó **chắc chắn** bị cắt. Vết trace 30
ngày khớp: reasoning peak leo từ **13.198** (`V10871`, 28/07) lên **31.391**, gấp **2,4 lần**,
ăn hết chỗ mà `V10871` cố ý chừa ra.

30 ngày production: **5 lượt** `finish_reason=length` trả rỗng (07/08 MT · 15/08 MN · 02/09 MB ·
02/09 MT · **03/09 MN — hôm nay**).

### 3.5 · 🟢 `glm-5.2` — trần đặt theo một ràng buộc ĐÃ HẾT HẠN

Trần `24576` **không chọn theo nhu cầu model**. Chú thích trong mã nói thẳng: *«giữ 24576 GIỐNG
glm-5.1 để so găng 5.1 vs 5.2 công bằng (xét retire **14/07**)»* — một ràng buộc **đo lường**,
phục vụ một quyết định đã qua **gần hai tháng**.

Cái giá, cùng trần, hai model cùng nhà, 30 ngày:

| | lượt rỗng | tỉ lệ |
|---|---|---|
| `glm-5.1` | 3/87 | 3,4% |
| `glm-5.2` | **17/89** | **19,1%** — gấp **5,6 lần** |

Cả 17 lượt đều bị chấm `LOSE`. Ảnh hưởng lên đúng con số owner nhìn thấy:

| model | WR tính CẢ lượt rỗng | WR chỉ lượt CÓ ra số | chênh |
|---|---|---|---|
| `glm-5.2` | **43,8%** | **54,2%** | **+10,3 điểm** |
| `deepseek-reasoner` | 56,8% | 60,2% | +3,4 điểm |
| `glm-5.1` | 60,9% | 63,1% | +2,2 điểm |
| `deepseek-v4-pro-real` | 52,8% | 52,8% | 0 |

⚠️ **Con số 43%/45% owner thấy trên bảng KHÁC với số đo ở đây** (56,8% / 43,8%) — hai thước
khác nhau (bảng UI nhiều khả năng là tỉ lệ **bạch thủ**, còn đây là `WIN+PARTIAL`). Không ghép
hai thước làm một (`RM-21`); điều **chung cho cả hai thước** là lượt rỗng bị tính vào mẫu số.

### 3.6 · 🔴 Nguyên nhân THỨ HAI của `glm-5.2` — và nó bác bỏ giả thuyết đầu của chính em

Sau khi nâng trần, một lượt MB **vẫn hỏng** — nhưng với `finish_reason = stop`, tức model kết
thúc **bình thường**. Điều đó **bác bỏ** giả thuyết «cắt token» cho ca này. Bắt nguyên văn:

```
{\n{"analysis":{"db_tails":["32","23",…
```

Thừa **một dấu `{` mở** rồi mới tới JSON thật. Và một biến thể nữa, nguy hơn vì **im lặng**:

```
{"":{"analysis":{…}}}   ← parse ĐƯỢC, nhưng payload nằm dưới khoá RỖNG
```

Ca thứ hai không sinh lỗi nào để đọc — hạ nguồn tìm `prediction` không thấy và ra rỗng.

### 3.7 · 🟡 Hard-timeout — nửa còn lại, suýt bỏ quên

Nâng trần token mà để timeout cắt là **vá nửa chừng** (§60.1). Cơ chế per-model **đã có sẵn**
từ `V10785`, nhưng hai model này **chưa bao giờ có trong bảng** ⇒ rơi về mốc chung **300s**.

| model | đo được | ghi chú |
|---|---|---|
| `glm-5.2` | n=90 (lane shadow ghi ĐỦ): TB 284s · p50 463s · p95 **553s** · max **641s** · **46/90 lượt (51%) vượt 300s** | phân bố ĐẠI DIỆN |
| `deepseek-reasoner` | ⚠️ DB chỉ có **6 dòng** trong 30 ngày và **cả 6 đều là lượt LỖI** | p95 270s ở đó là p95 của **lượt hỏng** — dùng nó là `RM-21`. Thay bằng 4 lượt gọi thật: **199 · 288 · 307 · 336s** |

### 3.8 · 🟡 Phát hiện phụ — prompt production có chỗ KHÔNG TẤT ĐỊNH

Cổng bất biến official **báo động giả** và gây một lần gỡ về thừa. Đối chứng đúng điều kiện
(hai tiến trình rời, **không deploy gì**): `USER_PAYLOAD` vẫn khác hash, **cùng độ dài**. Diff
ra **đúng một dòng** — `significant_pairs`, nơi các cặp **đồng hạng** (cùng `count`) xếp theo
thứ tự băm của tiến trình, mà `PYTHONHASHSEED` đổi mỗi lần chạy.

Đây là nguồn nhiễu thật cho **mọi** phép so prompt A/B, không riêng cổng này.

### 3.9 · Phép đo cho kết quả ÂM / chưa kết luận được

- **Trần token có phải nguyên nhân của `glm-5.2` không** — hai lượt thử đầu (11.259 và 15.728
  token) **nằm gọn trong trần cũ**, tức KHÔNG tái hiện được lỗi. Chỉ tới lượt xác nhận sau
  deploy mới thấy hai lượt **29.016** và **31.046** token — **vượt trần cũ 24.576**, tức trần cũ
  CÓ chặn thật. Nhưng đó vẫn là **suy luận có số đo hậu thuẫn**, chưa phải chứng minh cơ chế như
  `deepseek-reasoner`.
- **Chỉ mục trace** — phải **chứng minh tương đương** hàm gốc trên 40 mẫu ngẫu nhiên trước khi
  dùng, vì nếu chỉ mục lệch thì mọi con số sau đó vô nghĩa. Lệch **0/40**.

---

## 4 · Hướng xử lý và vì sao chọn

**Vì sao vá cả họ lỗi chứ không chỉ 877 dòng owner nêu.** Nếu recompute mà **không** vá nhánh
`_thieu` trước, thì chính lần recompute đó sẽ **đẻ thêm** ~1.000 dòng thua ảo mới — vì roster
hôm nay (26 model) rộng hơn roster lúc các dòng cũ được ghi. Vá trước rồi mới tính lại là thứ
tự **bắt buộc**, không phải lựa chọn.

**Vì sao `49152` chứ không phải `81920` (đã thử được) hay `393216` (API cho phép).** Mốc chặn
thật của một lượt gọi **không phải** `max_tokens` mà là `AI_MODEL_HARD_TIMEOUT_SEC`. Đo được
~**160 token/giây** ⇒ trong 300s model sinh tối đa ~48.000 token. Đặt cao hơn ngưỡng đó là đặt
một con số **không bao giờ với tới**, và chỉ đổi lỗi `length` lấy lỗi `TIMEOUT`.

**Vì sao KHÔNG đụng `AI_MODEL_HARD_TIMEOUT_SEC` chung mà dùng bảng per-model.** Mốc chung ảnh
hưởng **mọi** model và biên an toàn trước mốc đóng băng. Bảng per-model đã tồn tại từ `V10785`
và đã cấp `glm-5.1` **840s**, `gpt-oss-120b` **900s** trên chính chuỗi official — nên `480s` và
`720s` nằm gọn trong nếp đã có.

**Vì sao gỡ lớp bọc JSON hẹp cỡ đó.** `_go_boc_thua` chỉ gỡ khi lớp ngoài có **đúng một khoá
RỖNG** và lớp trong có khoá quen thuộc (`analysis`/`prediction`); `_tim_json_lech_dau` chỉ thử
`raw_decode` từ **5 vị trí `{` đầu** và chỉ nhận kết quả có khoá quen thuộc. Hẹp cỡ đó thì
không model nào khác vướng, và JSON hỏng thật **vẫn ném** chứ không bị nuốt.

**Vì sao `PRE_EXISTENCE` giữ dòng chứ không xoá.** Xoá là thao tác huỷ, cần cổng owner. Ghi đè
bằng nhãn đúng thì **sửa được 2.352 dòng sai đang tồn tại** mà không xoá gì — và dòng mới trơ
hoàn toàn (`parse_ok=0`, `would_flip=0`, `NO_DATA`).

---

## 5 · Đã làm gì — TRƯỚC / SAU / PHIÊN BẢN / KIỂM (§60.4)

### 5.1 · Materializer role-at-time → production

| | |
|---|---|
| **TRƯỚC** | `_ho()` đối chiếu registry HÔM NAY; module vá `TESTED` nhưng **chưa deploy** |
| **SAU** | `_v11155_vai_tro_theo_thoi_diem.py` + materializer đã vá chạy trong service |
| **PHIÊN BẢN** | `V11158` · deploy `PID 3279630 → 3289958` |
| **KIỂM** | nhập thử **trước** restart (service cũ vẫn chạy): `VAI_TRO=SHADOW_AUTO · OUTPUT=OUTPUT · FAILCLOSED=CO` |

### 5.2 · Vá nốt họ lỗi trong khối `_thieu`

| | |
|---|---|
| **TRƯỚC** | `would_flip_baseline_to_lose = int(baseline_hit)` · `family` khoá cứng `"SHADOW_AUTO"` · `run_source` khoá cứng `"shadow_auto_eval"` · `promotion_bucket = "DROP_CANDIDATE"` |
| **SAU** | cờ thua → **`0`** · `family` → **họ thật (`ho`)** · `run_source` → **`None`** · `PRE_EXISTENCE` → **`NO_DATA`** |
| **PHIÊN BẢN** | `V11158` · deploy `PID 3289958 → 3291704` |
| **KIỂM** | chạy thử trên **bản sao 804 MB** của DB production trước, rồi mới áp thật |

### 5.3 · Recompute 540 cặp vào production

| | trước | sau |
|---|---|---|
| dòng bảng chấm | 12.382 | **16.959** |
| **thua ẢO** | **1.058** | **0** |
| thua THẬT | 1.423 | **2.017** |
| `parse_ok=1` | 8.902 | **12.221** |
| `family` của dòng thiếu | `SHADOW_AUTO 3.296` | `SHADOW_AUTO 3.826` · **`OUTPUT 912`** |

**Sổ before/after 8.287 mục**, mỗi mục có `prediction_id` · `run_source` sự kiện · vai trò
cũ/mới · nhãn cũ/mới · cờ thua cũ/mới · mã lý do:

| mã lý do | dòng |
|---|---|
| `PRE_EXISTENCE_COVERAGE_GAP` | 2.352 |
| `ROLE_AT_TIME_CLASSIFICATION_ERROR` | 851 |
| `STILL_MISSING_FIELDS_FIXED` | 92 |
| `EXISTING_ROW_UPDATED` | 415 |
| `NEW_ROW_RECOVERED_RUN` — **lượt chạy thật được cứu** | **2.632** |
| `NEW_ROW_NO_DATA` — dòng trơ | 1.945 |

**Ba con số phải giải thích được, và đều giải thích được:**

- `877 = 851 sửa được + 8 tạo SAU mốc chốt + 18 lượt `manual`` — **0 dòng chưa giải thích được**.
  Ví dụ ca «sau mốc»: `2026-04-26 MB combo-super` tạo `18:02:53` trong khi mốc chốt `17:58:00`
  — trễ 4 phút 53 giây, `PRJ-SELECTION-WINDOW-001` mục 1 loại **đúng**.
- `415` dòng thường đổi: thực chất **23** dòng đổi trường có nghĩa (chủ yếu lượt `manual` bị
  loại đúng luật — **5 dòng mất `main_number`**, liệt kê đủ trong sổ), phần còn lại chỉ đổi
  trường chẩn đoán hợp đồng.
- Bảng **nở** vì roster hôm nay 26 model rộng hơn roster lúc các dòng cũ được ghi. **2.632/4.577**
  dòng thêm là **lượt chạy THẬT được cứu**; phần còn lại trơ.

**KIỂM:** chạy lại toàn bộ 540 cặp → **khác 0 dòng** (idempotent). Neo 558 **nguyên**.
4 bảng khoá **không đổi**. Sao lưu bảng chấm trước khi ghi:
`artifacts/v11158_scorecard_backup_20260903_125950.db`.

### 5.4 · Trần token

| model | TRƯỚC | SAU | PHIÊN BẢN | KIỂM |
|---|---|---|---|---|
| `deepseek-reasoner` | 32768 | **49152** | `V11158` · `PID 3291704 → 3295643` | gọi thật sau deploy: MN **47.936** token / 288s / `stop` / parse OK / số `96`; MT **46.987** / 307s / `stop` / số `36` — **cả hai vượt trần cũ**, tức trần cũ CÓ chặn |
| `glm-5.2` | 24576 | **49152** | như trên | MN **29.016** token / 177s / `stop` / parse OK / số `96` — **vượt trần cũ 24.576** |
| `glm-5.1` | 24576 | **24576 — KHÔNG đụng** | — | cổng kiểm riêng, xác nhận giữ nguyên |

### 5.5 · Vá lớp bọc JSON

| | |
|---|---|
| **TRƯỚC** | `_parse_ai_json_payload` chỉ đỡ `Extra data`; `{\n{…}` ném `Expecting property name`, `{"":{…}}` parse được nhưng payload bọc dưới khoá rỗng |
| **SAU** | `_go_boc_thua()` (`gpt_analyzer.py:1228`) + `_tim_json_lech_dau()` (`:1252`), áp ở **cả 4 điểm trả về** (`:1296 :1302 :1332 :1337`) |
| **PHIÊN BẢN** | `V11158` · `PID 3295643 → 3297566` |
| **KIỂM** | **9/9 ĐẠT** trên **nguyên văn đã bắt**, gồm 3 ca «không được đổi ca lành» + 1 ca «hỏng thật thì vẫn phải ném» |

### 5.6 · Hard-timeout per-model

| | |
|---|---|
| **TRƯỚC** | hai model không có trong `MODEL_HARD_TIMEOUT_OVERRIDES` ⇒ mốc chung **300s** |
| **SAU** | `deepseek-reasoner` **480s** · `glm-5.2` **720s** (`_v10785_late_fill.py`) |
| **PHIÊN BẢN** | `V11158` · `PID 3298426 → 3299063` |
| **KIỂM** | `IMPORT_OK 480 720 840 300` — hai model mới đúng, `glm-5.1` giữ **840**, model lạ vẫn về **300** (fail-safe) |

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| giờ ngoài block 15:30–18:15 | ✓ mọi deploy trong `12:43–13:50` |
| neo FINAL 558 | ✓ `a82c508d3569abda…` **nguyên qua 8 lần restart** |
| 4 bảng khoá | ✓ `predictions 14080 · final_bundles 562 · lottery_results 15403 · model_daily_eval 13903` — **không đổi** |
| health + PID đổi | ✓ mọi lần |
| nhập thử **trước** restart | ✓ service cũ vẫn chạy khi thử |
| **bất biến prompt official** | ✓ **6 băm khớp** — và cổng **tự thử chặn** mỗi lần (`RM-15`) + **đối chứng 2 lần** để không báo động giả |
| idempotent recompute | ✓ chạy lại 540 cặp → **0 dòng lệch** |
| tương đương chỉ mục trace | ✓ **0/40 mẫu lệch** so hàm gốc |
| test vá JSON | ✓ **9/9** trên nguyên văn thật |
| `_v11044_cong_so_hieu` | ✓ `SO_HIEU_V11044=KHOP` · V11158 trống |
| bốn mặt §63 | ✓ `governance_seq → 474` |

**Gỡ về:** `_v11158_deploy.py --go-ve` (materializer) · `_v11158c/d/e_deploy.py --go-ve`
(gpt_analyzer, late_fill) · bảng chấm khôi phục từ
`artifacts/v11158_scorecard_backup_20260903_125950.db`.

---

## 7 · Vướng vấp — bốn lần, ghi đủ

**🔴 ① Cổng bất biến của chính em BÁO ĐỘNG GIẢ, gây một lần gỡ về thừa.** Bản đầu băm nguyên
văn `USER_PAYLOAD` rồi kết luận *«PROMPT OFFICIAL ĐỔI»* ở cả ba miền — trong khi thay đổi duy
nhất là hai hằng số `max_tokens`, thứ **không liên quan gì** tới dựng prompt. Đối chứng đúng
điều kiện phơi ra thủ phạm: `significant_pairs` xếp theo `PYTHONHASHSEED`. Đây là **lần thứ ba**
cùng một họ lỗi *«dụng cụ đo đứng sai chỗ»* — hai lần trước đã ghi trong `vps_service_env.py`.
**Đã sửa:** cổng nay so `SYSTEM_SERVED` nguyên văn + `USER_PAYLOAD` theo **tập dòng đã sắp**,
và **tự chứng minh** cả hai chiều mỗi lần chạy.

**🔴 ② Giả thuyết đầu về `glm-5.2` SAI — và chính phép đo bác bỏ nó.** Em kết luận *«cả bốn chữ
ký lỗi đều là cắt giữa chừng»*. Lượt xác nhận sau deploy hỏng với `finish_reason = stop`, tức
model kết thúc **bình thường** ⇒ ca đó **không phải** cắt token. Phải đi bắt nguyên văn mới thấy
tật thật là thừa một dấu `{`. **Giữ nguyên nhận định đã sửa:** trần token CÓ chặn thật (đo được
lượt 29.016 và 31.046 token vượt trần cũ), nhưng nó **không phải nguyên nhân duy nhất**.

**🟡 ③ Bước lập sổ before/after treo vì 8.287 truy vấn lẻ.** Mỗi dòng đổi gọi một `SELECT` trên
`predictions` không index ⇒ tiến trình chết giữa chừng, dù phần ghi DB **đã xong và đúng**.
Dựng lại bằng **một lần nạp** toàn bộ khoá `predictions` rồi tra trong bộ nhớ.

**🟡 ④ Hàm trợ giúp của bộ test tự báo HỎNG cho hai ca đúng.** Nhánh `except` gán cứng
`ok = False` nên hai ca *«phải NÉM»* không bao giờ đạt được — lỗi của **thước**, không của vật
đo. Sửa để `mong()` **luôn** được gọi kể cả khi hàm ném → **9/9**.

---

## 8 · Gỡ về

| thứ | cách gỡ | đã thử? |
|---|---|---|
| materializer + module vai trò | `python _v11158_deploy.py --go-ve` | — |
| `gpt_analyzer.py` (trần token + vá JSON) | `python _v11158d_deploy.py --go-ve` | ✓ **đã chạy thật 1 lần** (`GO_VE_OK`) khi cổng báo động giả |
| `_v10785_late_fill.py` (timeout) | `python _v11158e_deploy.py --go-ve` | ✓ **đã chạy thật 1 lần** (`GO_VE_OK`) khi nhập thử hỏng |
| bảng chấm | khôi phục từ `artifacts/v11158_scorecard_backup_20260903_125950.db` | — |

Hai lần gỡ về đều **tự động, sạch**, neo 558 nguyên, health `200`.

---

## 9 · Theo dõi tiếp — liệt kê ĐỦ

| việc | ai chặn / chặn ở đâu | ghi chú |
|---|---|---|
| `SCHEDULED_SHADOW_OUTPUT_PROVEN` | **PENDING** — chờ lượt scheduler `16:00/17:00` | đọc `context_only_regime` trong `prediction_trace` |
| **Đo hiệu lực 4 bản vá, 14 ngày** | chưa có dữ liệu | nền: `glm-5.2` **19,1%** lượt rỗng · `deepseek-reasoner` **5/88** |
| 🟡 `glm-5.2` — trần token có phải nguyên nhân không | **CHƯA chứng minh** (`RM-12`) | mới là *suy luận có số đo hậu thuẫn*. Không giảm sau 14 ngày ⇒ **KHÔNG** phải nguyên nhân |
| 🟡 `significant_pairs` không tất định | chưa xử | làm nhiễu **mọi** phép so prompt A/B, không riêng cổng này |
| `_v10871_deploy.py:86` khẳng định `== 32768` | không phải cổng sống | script deploy một lần của `V10871`; nay sẽ ném nếu chạy lại — **đúng**, vì `V11158` thay thế nó |
| `_thieu` vẫn dựng từ roster HÔM NAY | chưa xử | nay **trơ** (`NO_DATA`, cờ thua `0`), nhưng nguồn gốc lookahead còn đó. Sửa tận gốc cần eligibility-at-time từ git history (`_v11155_counterfactual`) |
| `TRUE_MISSING_OUTPUT` 67 dòng | chưa tra | model tồn tại, có lượt, nhưng không ra số — cùng họ với ca `glm-5.2` vừa vá |
| ALL_MODEL_ARENA → TOTAL_V2 → COMBO_V2 → FINAL_V2 → Cutover Packet | `NOT_STARTED` | Wave 2–5 |
| 16 báo cáo đóng được bằng thêm tiêu đề · 22 cần `GAP_MARKER` · 31 reader cũ cần nhãn | chưa xử | nợ tồn |
| `registry_sha256` vào bundles | **chờ owner** | đụng writer `final_bundles` (§52 mục 13) |

---

## Nguồn ba lớp (§62)

### `OWNER_SAID`

- 03/09 ~13:05 — *«⚠️ 🔬 DeepSeek Reasoner 43% 30d · ⚠️ 🤖 GLM 5.2 45% 30d — 2 model này không
  ra output sẵn kiểm tra dùm anh luôn em»*
- 03/09 ~13:20 — *«fix cho chạy ra output luôn chứ em. Chưa tới giờ block mà em.»*
- (phiên trước) mục `B` — *«Áp materializer repair vào production theo backup/migration gate…
  Rerun phải idempotent… Neo FINAL và dữ liệu lịch sử immutable không drift.»*

### `CODE_DID`

- `_materialize_shadow_promotion_scorecard.py` — `_ho()` gọi `ho_tai_thoi_diem`; khối `_thieu`
  vá 3 lỗi. Bảng chấm `12.382 → 16.959`, thua ảo `1.058 → 0`, idempotent 0 dòng lệch.
- `gpt_analyzer.py:179` `49152` · `:3773` `49152` · `:1228 _go_boc_thua` · `:1252
  _tim_json_lech_dau`. Gọi thật: `deepseek-reasoner` MB `reasoning_tokens=40.215`.
- `_v10785_late_fill.py` — `"glm-5.2": 720` · `"deepseek-reasoner": 480`. Kiểm runtime
  `IMPORT_OK 480 720 840 300`.
- Deploy `PID 3279630 → … → 3299063` (8 lần restart), neo 558 `a82c508d3569abda…` nguyên.
- Artifact: `v11158_so_before_after.json` (8.287 mục) · `v11158_scorecard_backup_20260903_125950.db`
  · `v11158_thu_token.json` · `v11158_xac_nhan.json` · `v11158_raw_glm.json`.

### `DOC_SAID`

- `gpt_analyzer.py:3792` ghi *«glm-5.2: giữ 24576 GIỐNG glm-5.1… (xét retire 14/07)»* —
  **`DOC_SAID` ≠ `CODE_DID` từ V11158**. Đã dán nhãn *«CÂU TRÊN HẾT HIỆU LỰC»* ngay tại chỗ
  thay vì xoá, để giữ dấu vết vì sao trần từng là 24576.
- `_v10785_late_fill.py` đầu bảng ghi *«mốc chung 300s sẽ cắt gần như mọi lần»* — **đúng**, và
  đo được `glm-5.2` **46/90 lượt vượt 300s** chính là ca sách vở của câu đó.
- `CLAUDE.md` `RM-07` *«vá một lỗi không phải vá cả họ lỗi»* — phiên này là ca áp dụng trực tiếp:
  `V11155` vá 279/1.058.

---

TanPhatAI cần làm: ghi **`V11158`** — bốn mặt đã ghi, `governance_seq 474`, công khai bản này. Ghi **materializer role-at-time ĐÃ VÀO PRODUCTION** kèm recompute 540 cặp, idempotent (chạy lại 0 dòng lệch), sổ before/after **8.287 mục** theo `prediction_id` + mã lý do, sao lưu `v11158_scorecard_backup_20260903_125950.db`. Ghi **thua ẢO `1.058 → 0`** và **`V11155` chỉ vá được 279/1.058** (`RM-07`) — lớp lớn nhất là `PRE_EXISTENCE_COVERAGE_GAP` **2.352 dòng / 760 thua ảo**, do roster HÔM NAY áp ngược về ngày cũ. Ghi **owner báo 2 model không ra output** và **hai nguyên nhân khác nhau**: `deepseek-reasoner` `reasoning_tokens=40.215` vượt trần cũ 32.768 (**chứng minh cơ chế**), `glm-5.2` trần 24576 là **ràng buộc so găng đã hết hạn 14/07** + **thừa một dấu `{` mở** trong JSON. Ghi **WR `glm-5.2` 43,8% → 54,2%** nếu bỏ lượt không-ra-số — **10,3 điểm là hỏng hạ tầng**. Ghi **hard-timeout per-model 480s/720s** (`glm-5.2` **46/90 lượt vượt 300s**). Ghi **`RM-12`: với `glm-5.2` nguyên nhân trần token CHƯA chứng minh**, phải đo 14 ngày. Ghi **`RM-21`: KHÔNG dùng p95 latency của `deepseek-reasoner` trong DB** vì cả 6 dòng đều là lượt lỗi. Ghi **phát hiện phụ: prompt production KHÔNG tất định ở `significant_pairs`** — nhiễu cho mọi phép so prompt. Ghi **official không đổi một ký tự prompt** (6 băm khớp) và **neo 558 nguyên qua 8 lần restart**. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.** `POOL_VERDICT` giữ **`HOLD`**.
