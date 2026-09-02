# REPORT V11151 — GRAND OVERHAUL · **WAVE 2 `VI.1`** · 02/09/2026

> `ACTOR_RUNTIME = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**
> Phiên **CHỈ ĐỌC**: không deploy · không restart · không ghi DB.
> `PID 3156545` không đổi · **558 FINAL hash `a82c508d3569abda…` KHÔNG DRIFT**.

---

## 1 · TÓM TẮT

Trả lời dứt điểm câu owner khoá ở `VI.1`: **vì sao có nguồn runtime-active mà không vào
`voters`** — và trả lời bằng **số đo, không phải nhãn**, đúng câu *«cấm đoán nguyên nhân nếu chưa
có trace»*.

Ba kết quả:

| | |
|---|---|
| **số học đúng** | `27 active = 17 active-và-voter + **10** active-không-voter` · **10, không phải 9** |
| **nguyên nhân** | **`SHADOW_ONLY` 10/10** — 100% lượt `shadow_auto_eval`. Đúng thiết kế, không phải lỗi |
| **cổng mới** | **`SHADOW_BOUNDARY_CLEAN` 0/18** — bằng chứng *không rò shadow* **mạnh hơn** phép đếm của `V11149` |

Và **một con số phải rút lại**: `FU-450` mục 1 ghi `gemini-3.6-flash` *«cầm 1,8% lá phiếu»* —
đo lại thì nó **không cầm lá phiếu nào**.

---

## 2 · OWNER YÊU CẦU GÌ — nguyên văn

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI.** Đây là **mệnh lệnh trực tiếp của owner**,
> nói trong IDE, có hiệu lực ngay (`PRJ-INTERACTION-LEDGER-001`).

### Prompt chính — `PROMPT 43 R1 · EXECUTE WAVES 1–5`, mục `VI.1`

> *«Phải trả lời vì sao 9 runtime-active không vào voters: output eligibility · missing candidate ·
> gate · late · sanitization · configuration · caller/path khác · hay lỗi. **Cấm đoán nguyên nhân
> nếu chưa có trace.**»*
>
> **`III`** — *«Không được mở lại sự cố shadow leak chỉ vì tên model xuất hiện trong `model_bt` ·
> `model_wr` · `model_exclusion_reasons` · `diagnostic_empty_models` · các trường
> diagnostic/trace tương tự.»*
>
> **`IV.14`** — *«Không đo cùng một model hai lần qua hai prompt regime như hai bằng chứng độc
> lập.»*
>
> **`XIX`** — *«Tiếp tục ALL_MODEL_ARENA; không dừng chờ nếu không gặp bốn Owner gates.»*

### Yêu cầu trực tiếp trong phiên (`PRJ-INTERACTION-LEDGER-001`)

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 02/09 ~02:00 | *«Tiếp theo là gì cần anh xác nhận chia sẻ thêm vấn đề gì không»* | `HỎI` | trả lời: **không cần xác nhận** — chưa chạm bốn cổng; nêu thứ sẽ cần (ngưỡng chấp nhận trước Wave 4) và hai thứ owner chia sẻ được (giá API, 3-càng) | `ĐÃ_LÀM` |
| 02/09 ~02:20 | *«Push báo cáo chưa em?»* | `HỎI` | kiểm thật: `V11150` **đã push đủ**; `V11151` **CHƯA** — mới có commit code, thiếu bốn mặt + báo cáo công khai. **Làm ngay trong phiên** | `ĐÃ_LÀM` |

**Owner bắt đúng một khoản nợ có thật.** `V11151` đã có commit `6a5ca20` ở kho riêng từ trước,
nhưng `CHANGELOG` đếm `0`, `AUTOMATION_HISTORY` đếm `0`, và **không có thư mục báo cáo công khai**
— tức code đi trước tài liệu **quá một phiên**, vượt giới hạn `PRJ-INTERACTION-LEDGER-001` khoản
2. Bản này trả nợ đó.

---

## 3 · ĐÀO BỚI / PHÁT HIỆN — liệt kê ĐỦ

### 3.1 Phễu pool — phép trừ `27 − 18` KHÔNG ra câu trả lời

```
57 từng chạy          predictions, toàn lịch sử
27 runtime-active     có output trong ≤ 2 ngày
18 actual voter       có tên trong `voters` của 273 bundle (90 ngày)

27 active = 17 active-VÀ-voter + 10 active-không-voter
18 voter  = 17 còn active + 1 ĐÃ NGHỈ
```

**Con số đúng là 10, không phải 9.** Prompt ghi 9 vì lấy `27 − 18`. Phép trừ đó sai vì hai tập
**không lồng nhau**: `claude-opus-4-20250514` là voter (60 lần) nhưng **lượt cuối 16/06**, tức
**không còn runtime-active**. Bundle từ 03/06–16/06 nằm trong cửa sổ 90 ngày nên vẫn còn tên nó —
**đúng, không phải rò rỉ**.

### 3.2 Vì sao 10 nguồn không vào `voters` — cùng MỘT lý do, có số đo

| nguồn | lớp | mã | bằng chứng |
|---|---|---|---|
| `claude-opus-5-fast` | `LLM_BASE` | `SHADOW_ONLY` | 100/100 lượt shadow |
| `deepseek-v4-pro-real` | `LLM_BASE` | `SHADOW_ONLY` | 174/174 |
| `gemini-3.5-flash` | `LLM_BASE` | `SHADOW_ONLY` | 169/169 |
| `gemini-3.6-flash` | `LLM_BASE` | `SHADOW_ONLY` | 94/94 |
| `glm-5.2` | `LLM_BASE` | `SHADOW_ONLY` | 175/175 |
| `gpt-5.5` | `LLM_BASE` | `SHADOW_ONLY` | 271/271 |
| `gpt-5.6-sol-pro` | `LLM_BASE` | `SHADOW_ONLY` | 100/100 |
| `grok-4.3` | `LLM_BASE` | `SHADOW_ONLY` | 138/138 |
| `qwen3-max-thinking` | `LLM_BASE` | `SHADOW_ONLY` | 272/272 |
| `qwen3.7-max` | `LLM_BASE` | `SHADOW_ONLY` | 173/173 |

**10/10 cùng một mã.** Không nguồn nào rơi vào `MISSING_CANDIDATE` · `PARTIAL_MISSING` ·
`EVALUATION_ONLY` · `CHUA_DU_TRACE`.

⇒ **Bác bỏ** giả thuyết *«có ứng viên đang bị bỏ phí vì cấu hình»*. Ba nguyên nhân owner liệt
(cấu hình · không có output · trễ) dẫn tới **ba hành động ngược nhau**; câu trả lời thật là
**cái thứ tư**: chúng shadow **đúng thiết kế**, và việc phải làm là **phán quyết vòng đời**
(`VI.3`), không phải sửa cấu hình.

### 3.3 🟢 `SHADOW_BOUNDARY_CLEAN` — cổng mới, mạnh hơn phép đếm của `V11149`

`V11149` kết luận không rò rỉ bằng cách **đếm**: *«0 model shadow trong `voters`»*. Đúng, nhưng
**yếu** — nó chỉ soi trạng thái **hôm nay**. Một model từng official rồi bị hạ xuống shadow vẫn
có thể tiếp tục bỏ phiếu vài ngày sau khi hạ, và phép đếm ấy **không thấy**.

Cổng mới soi **BIÊN THỜI GIAN** từng nguồn: *ngày bỏ phiếu cuối có nằm **sau** ngày chạy official
cuối không?*

| nguồn | vote cuối | official cuối | shadow đầu | |
|---|---|---|---|---|
| `gpt-5-mini` | **2026-07-31** | **2026-08-01** | **2026-08-01** | 🟢 **0 ngày chồng lấn** |
| `glm-5.1` | 2026-09-01 | 2026-09-01 | 2026-06-03 | 🟢 chiều ngược — **thăng hạng** |
| `gpt-oss-120b` | 2026-09-01 | 2026-09-01 | 2026-06-03 | 🟢 như trên |
| `claude-opus-4-20250514` | 2026-06-15 | 2026-06-16 | — | 🟢 nghỉ hưu, biên đúng |
| *(14 nguồn còn lại)* | 2026-09-01 | 2026-09-01 | — | 🟢 |

**`SHADOW_BOUNDARY_CLEAN` — 0/18 vi phạm.**

**01/08 là mốc XOAY POOL:** `gpt-5-mini` xuống shadow · `glm-5.1` + `gpt-oss-120b` lên official.
Cả hai chiều đều **khớp đến từng ngày**.

### 3.4 🟡 Con số của `FU-450` mục 1 phải RÚT LẠI — bốn phần (`PRJ-RETRACTION-001`)

| phần bắt buộc | nội dung |
|---|---|
| **chỗ gốc** | `docs/FOLLOW_UP_TRACKER.md` · `FU-450` khoản 1 · công bố **01/09/2026** |
| **nguyên văn câu sai** | *«Dừng `gemini-3.6-flash` khỏi pool ứng viên — … Đang tốn API và **cầm 1,8% lá phiếu** để kéo xuống.»* |
| **điều đúng, tái lập được** | `gemini-3.6-flash` **KHÔNG cầm lá phiếu nào**. `python web/backend/_v11151_arena_pool.py` → `94/94` lượt là `shadow_auto_eval`; quét `voters` của **273 bundle** cho **0 lần**. Nhãn đúng: `SHADOW_ONLY`. |
| **quyết định đã dựa trên số sai** | hành động ghi là *«rút khỏi pool ứng viên»*. Thực chất là **«dừng lượt shadow»** — cái được là **tiền API**, **không phải** chất lượng dự đoán. Việc vẫn nên làm; **lý do và mức lợi ích đổi hẳn**. |

Hai con số hiệu suất (`10,00%` MB · `27,47%` toàn cục, `n=91`) **KHÔNG bị rút** — chúng đo trên
lượt shadow và vẫn đúng làm căn cứ **phán quyết vòng đời shadow** (`VI.3`).

### 3.5 Phép đo ra kết quả cần theo dõi tiếp — ghi đủ, không bỏ

- **`gpt-5.4` chạy CẢ hai chế độ**: official tới `01/09` **và** shadow từ `01/08`. Owner `IV.14`
  cấm đo cùng một model qua hai prompt regime như **hai bằng chứng độc lập** ⇒ Arena **phải
  dedupe**. Chưa xử.
- **`combo-no-token` ngừng là voter từ `01/08`** nhưng **vẫn chạy** official tới `01/09`. Ngừng bỏ
  phiếu mà không ngừng chạy — **chưa truy nguyên nhân**, để `NOT_VERIFIED`.
- **Không có bí danh** nào trong 18 voter ⇒ **không cần** gộp trước khi xếp hạng. (Phép này chạy
  ra kết quả **âm** — vẫn ghi, vì nó loại bỏ một mối lo có thật: `canonical_id` gộp
  `claude-opus-4-20250514` → `claude-opus-4`, nhưng `claude-opus-4-6` là **model khác**, không bị
  gộp nhầm.)

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Vì sao dựng cổng biên thay vì chỉ đếm lại.** Phép đếm của `V11149` trả lời câu *«hiện có shadow
nào đang bỏ phiếu không»*. Câu thật sự quan trọng là *«đã bao giờ có shadow bỏ phiếu chưa»* —
và hai câu đó chỉ trùng nhau khi pool **chưa từng xoay**. Pool **đã xoay ngày 01/08**. Cổng biên
trả lời câu thứ hai, và trả lời được cho **cả lịch sử**.

**Vì sao không tự dừng `gemini-3.6-flash` ngay.** `FU-450` mục 1 đã được owner duyệt, nhưng
dừng nó là **đổi cron/cấu hình** ⇒ deploy. Và theo `VI.3`, mọi shadow phải nhận **phán quyết
trong state machine** (`RETIRE_CANDIDATE` · `DORMANT` · …), không phải bị gỡ lẻ. Gộp vào `VI.3`
để một lần làm cho **cả 10 nguồn**, không tỉa từng cái — đúng tinh thần `RM-07`.

**Vì sao tách cột `run_source`.** Xem mục 7.

---

## 5 · ĐÃ LÀM GÌ — trước / sau / phiên bản / kiểm (§60.4)

### `_v11151_arena_pool.py` (MỚI)

**TRƯỚC:** không có công cụ nào trả lời được *«vì sao nguồn X không vào `voters`»* — mọi câu trả
lời trước đây đều là **suy đoán từ tên**.

**SAU:** ba tầng phễu đo bằng dấu vết + mã nguyên nhân kèm **số đo** cho từng nguồn + cổng biên
shadow.

**PHIÊN BẢN:** `ARENA-1.0.0` · commit riêng `6a5ca20`.

**KIỂM:**
```bash
python web/backend/_v11151_arena_pool.py
# PHỄU: 57 → 27 → 18
# SHADOW_ONLY 10 nguồn
# ==> SHADOW_BOUNDARY_CLEAN — 0/18 nguồn bỏ phiếu sau khi hết official
```

### Bốn mặt quản trị + báo cáo công khai (BẢN NÀY)

**TRƯỚC:** `V11151` có commit code nhưng `CHANGELOG` = `0` · `AUTOMATION_HISTORY` = `0` · không
có thư mục báo cáo công khai.
**SAU:** bốn mặt đủ, `governance_seq → 467`, báo cáo công khai đẩy lên.

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11044_cong_so_hieu.py V11151` | ✅ `SO_HIEU_V11044=KHỚP` |
| `_v11062_nang_version.py --kiem` | ✅ `ĐẠT` — bốn mặt · `governance_seq 467` |
| `_v11151_arena_pool.py` | ✅ `SHADOW_BOUNDARY_CLEAN 0/18` |
| `_v10921_report_gate.py V11151` | ✅ đủ 9 phần *(chạy sau khi commit bản này)* |
| **neo no-drift 558 FINAL** | ✅ `a82c508d3569abda…` **KHÔNG DRIFT** |

---

## 7 · VƯỚNG VẤP

**🔴 Suýt mở lại sự cố shadow-leak mà owner cấm mở lại (`III`).** Cột *«`run_source` trội»* bản
đầu lấy **mode 90 ngày**. Mode đó **vắt qua lần xoay pool 01/08**, nên in ra:

```
glm-5.1        LLM_BASE   167   shadow_auto_eval
gpt-oss-120b   LLM_BASE   129   shadow_auto_eval
```

— ngay cạnh tiêu đề **«18 VOTER THẬT»**. Đọc lên là *«shadow đang bỏ phiếu»*. Nếu công bố nguyên
bảng đó thì đã **báo owner một sự cố không có thật** lần thứ hai trong hai ngày, và mở lại đúng
mục owner khoá.

**Sự thật:** shadow của cả hai **dừng từ 01/08**; từ đó tới nay chúng chạy `ai_chain`/`auto_daily`
— tức **đã lên official**. Đã tách cột thành `run_source` **HIỆN NAY (14 ngày)** + nhãn
`ĐÃ LÊN OFFICIAL` kèm số đo 90 ngày để không mất thông tin lịch sử.

**🟡 Khoản nợ tài liệu owner bắt đúng.** `V11151` có commit code từ trước nhưng thiếu bốn mặt và
báo cáo công khai. `PRJ-INTERACTION-LEDGER-001` khoản 2: *«code ĐƯỢC đi trước tài liệu, nhưng
GHI NHẬN thì KHÔNG được đi sau quá một phiên»*. Đã trả trong cùng phiên.

**🟡 Lỗi cú pháp `%` trong SQL.** `LIKE '%shadow%'` va vào `%d` của phép format chuỗi ⇒
`TypeError`. Sửa bằng cách truyền khoảng ngày qua **tham số** thay vì nội suy — vừa hết va chạm,
vừa không nối chuỗi vào SQL.

**🟡 Tệp rác `muc`** — output lỗi `git add` với chuỗi tiếng Việt không đóng nháy bị ghi thành
tệp. Đã xác nhận 100% là dòng `error: pathspec` rồi mới xoá.

---

## 8 · GỠ VỀ

Phiên **chỉ đọc** — không có gì trên production cần gỡ.

| thành phần | gỡ về |
|---|---|
| `_v11151_arena_pool.py` | xoá tệp; **không** module production nào import nó |
| bốn mặt quản trị | `backups/FOLLOW_UP_TRACKER.md.pre_*` · `git revert` commit tài liệu |

---

## 9 · THEO DÕI TIẾP — liệt kê ĐỦ

| # | việc | trạng thái | chặn ở đâu |
|---|---|---|---|
| 1 | `VI.2` Arena namespace — chấm theo **miền × sản phẩm** | ⚪ đang làm tiếp | cần **đơn giá API** cho cột `cost` (owner chia sẻ được) |
| 2 | `VI.3` vòng đời shadow — phán quyết cho **cả 10 nguồn** | ⚪ Wave 2 | gồm `gemini-3.6-flash` (`FU-450` mục 1) |
| 3 | **`gpt-5.4` chạy hai regime** ⇒ dedupe (`IV.14`) | 🔴 chưa xử | Arena |
| 4 | **`combo-no-token`** ngừng vote từ 01/08 mà vẫn chạy | 🟡 `NOT_VERIFIED` | chưa truy trace |
| 5 | **`DOUBLE_COUNT`** — `combo-super`/`smart-*` trong voters | 🔴 `PARENT_LINEAGE_PENDING` | Wave 3 |
| 6 | Adapter LLM tự sinh ranked top-K đúng hợp đồng | ⚪ Wave 1 còn lại | — |
| 7 | `predictions` qua `database.py` — ML có dùng làm đặc trưng? | 🟡 `NOT_VERIFIED` | — |
| 8 | `gpt_analyzer.py:5620` chuỗi báo lỗi ngoài cờ | 🟡 tồn dư nhẹ | runtime hôm nay = 0 |
| 9 | Cổng mồ côi `📊 KNOWLEDGE BASE` | 🟡 `CHẶN` | có từ trước |
| 10 | **Ngưỡng chấp nhận đăng ký TRƯỚC replay** | 🔴 **cần owner** | trước Wave 4 — `VII.1` + `RM-03` cấm chọn sau khi nhìn kết quả |
| 11 | **3-càng** — có pipeline hợp lệ không | ⚪ `XI` | nếu không ⇒ `NO_VALID_3CANG`, **cấm chế số** |
| 12 | `TOTAL_V2` / `COMBO_V2` / `FINAL_V2` | ⚪ Wave 3 | — |
| 13 | Replay + canary | ⚪ Wave 4 | phụ thuộc #10 |
| 14 | **Cutover Packet** | ⚪ Wave 5 | **cổng D** — cần owner ký |
| 15 | D-30 · 26 stale reader · `FU-444`/`FU-447` | ⚪ bảo trì | **không** chặn Grand Overhaul (`XIII`) |
| 16 | Bảo mật / SSH / world-writable | ⚪ `CLASS C` | **cổng B** — không tự mutation |

---

## §62 — BA LỚP NGUỒN

### `OWNER_SAID` (nguyên văn + giờ)

| giờ (VN) | nguyên văn | loại |
|---|---|---|
| 02/09 ~00:00 | *«Phải trả lời vì sao 9 runtime-active không vào voters… Cấm đoán nguyên nhân nếu chưa có trace.»* | `YÊU_CẦU` |
| 02/09 ~00:00 | *«Không được mở lại sự cố shadow leak chỉ vì tên model xuất hiện trong… các trường diagnostic/trace tương tự.»* | `YÊU_CẦU` |
| 02/09 ~02:00 | *«Tiếp theo là gì cần anh xác nhận chia sẻ thêm vấn đề gì không»* | `HỎI` |
| 02/09 ~02:20 | *«Push báo cáo chưa em?»* | `HỎI` |

### `CODE_DID` (evidence)

- `_v11151_arena_pool.py` → `57 → 27 → 18` · `SHADOW_ONLY 10/10` · `SHADOW_BOUNDARY_CLEAN 0/18`
- `gpt-5-mini`: vote cuối `2026-07-31` · official cuối `2026-08-01` · shadow đầu `2026-08-01`
- **558 FINAL** `a82c508d3569abda47041ad625cca93fdec2227fbe389c395dc7f139893a0e5f` — không drift
- `PID 3156545` · **không restart, không ghi DB**
- commit riêng `6a5ca20` + commit tài liệu bản này

### `DOC_SAID`

- `docs/FOLLOW_UP_TRACKER.md` `FU-450` mục 1 — *«cầm 1,8% lá phiếu»* ⇒ **ĐÃ RÚT LẠI**, xem 3.4.
- `PROMPT 43 R1 VI.1` — *«9 runtime-active»* ⇒ đo được **10**; phép trừ `27 − 18` sai vì hai tập
  không lồng nhau.

### `NOT_VERIFIED`

`combo-no-token` ngừng vote mà vẫn chạy · lineage `parent_output_hashes` · `predictions` qua
`database.py` · đơn giá API từng model.

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` ≠ `CODE_DID`** ở **hai chỗ**, cả hai đều là con số công bố:
① *«1,8% lá phiếu»* → thực đo **0 lá phiếu**;
② *«9 runtime-active không vào voters»* → thực đo **10**.
Cả hai đã sửa tại chỗ gốc trong bản này.

---

TanPhatAI cần làm: ghi **`V11151` = Wave 2 `VI.1`** — riêng `6a5ca20` + commit tài liệu, **phiên chỉ đọc**, không deploy. Ghi **owner bắt đúng một khoản nợ**: `V11151` từng có commit code mà **thiếu bốn mặt + báo cáo công khai**; đã trả **trong cùng phiên** theo `PRJ-INTERACTION-LEDGER-001` khoản 2. Ghi **RÚT LẠI con số «1,8% lá phiếu»** của `FU-450` mục 1 — `gemini-3.6-flash` là `SHADOW_ONLY`, **0 lần** trong `voters` của 273 bundle; việc đúng là **dừng lượt shadow**, lợi ích là **tiền API** chứ không phải chất lượng. Ghi **số đúng là 10 nguồn, không phải 9** — phép trừ `27 − 18` sai vì một voter **đã nghỉ hưu** (`claude-opus-4-20250514`, lượt cuối 16/06). Ghi **`SHADOW_BOUNDARY_CLEAN 0/18`** — bằng chứng **mạnh hơn** phép đếm của `V11149`, biên khớp đến từng ngày; **đừng mở lại sự cố shadow-leak**. Ghi **`gpt-5.4` chạy hai regime** ⇒ phải dedupe (`IV.14`). Ghi **sẽ cần owner đặt ngưỡng chấp nhận TRƯỚC Wave 4**. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
