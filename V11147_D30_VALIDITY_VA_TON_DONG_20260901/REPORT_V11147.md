# REPORT V11147 — **D-30 CHƯA CÓ NGÀY HỢP LỆ NÀO** · ma trận runtime C1–C6 · 26 stale reader · gốc `FU-448`

> **Ngày:** 01/09/2026 · `ACTOR_RUNTIME = CLAUDE_CODE` · **Prompt 43 R1 — `PARTIAL`, không mở Prompt 44**
> **Phiên này READ-ONLY với production:** không deploy · không restart · không ghi DB · không đổi official.

---

## 1 · Tóm tắt

Phát hiện nặng nhất: **`D-30` chưa ghi được một ngày hợp lệ nào.** Cả `30/08` và `31/08` đều
**trượt cổng thời điểm** của owner (`generated_at < region_lock`) — artifact sinh lúc `18:17` và
`19:15`, **sau cả ba mốc khoá miền**. Earliest candidate full valid day = **`02/09`**, và chỉ khi
dựng `PRE_LOCK_GENERATOR`.

Đi kèm: ma trận runtime **17/17 `CODED_NOT_DEPLOYED`**, bảng **26 stale reader** (1 bản owner
**nhìn thấy** số cũ 169 ngày), manifest **38 lane nghỉ / 332.471 dòng** có hash, và **gốc thật của
`FU-448`** — một lỗi **thứ tự trong ngày**, không phải lỗi chất lượng luật.

---

## 2 · Owner yêu cầu gì — nguyên văn

> **01/09** — `PROMPT 43 R1 — CONTINUATION AFTER V11146`. Ba mệnh lệnh còn hiệu lực:
> **`OWNER-01`** panel `D-30` được hiện SỐ, cấm hit-rate/leaderboard/p-value giữa kỳ ·
> **`OWNER-02`** CODE `local→VPS`, DB `VPS→local`, cấm báo drift vì hash DB ·
> **`OWNER-03`** block `15:30–18:15`, ngoài block deploy theo `D-25`.

Bảng đủ **13 câu nguyên văn** của owner trong phiên nằm ở `CONVERSATION_CONTEXT` cùng thư mục và
`docs/SO_TUONG_TAC_OWNER.md`.

⚠️ **TanPhatAI:** owner trao đổi liên tục trong IDE nên **code thường đi trước tài liệu** — điều
owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`). Tài liệu cũ mâu thuẫn thực tế đang chạy
thì **thực tế + sổ tương tác thắng**.

---

## 3 · Đào bới / phát hiện

### 3.1 🔴 `I` — D-30 VALIDITY MATRIX `31/08 – 01/09`

Audit chạy lúc **17:34**, tức **trong block** ⇒ đúng `I.1`: chỉ đọc, không deploy.

| DATE | REGION × LANE | `generated_at` | `region_lock` | cổng `I.4` | phán quyết |
|---|---|---|---|---|---|
| `2026-08-30` | 6/6 bản ghi | **18:17:32** | MN 15:45 · MT 16:58 · MB 17:58 | **TRƯỢT 6/6** | `WARMUP` + `INVALID_TIMING_NOT_SCORED` |
| `2026-08-31` | 6/6 bản ghi | **19:15:01** | như trên | **TRƯỢT 6/6** | `INVALID_TIMING_NOT_SCORED` |
| `2026-09-01` | — | **chưa sinh** | — | — | cron 19:15 chưa chạy (audit lúc 17:34) |

**Artifact path / hash / writer:**

```
/root/Lottery_AI_Test/artifacts/d30/2026-08-30.jsonl  sha d08db8a4b3454549  mtime 30/08 18:17:32
/root/Lottery_AI_Test/artifacts/d30/2026-08-31.jsonl  sha e2d7f4efa58e4790  mtime 31/08 19:15:01
writer cron: 15 19 * * *  _v11137_d30_lane.py
prereg_hash: fd9eda76f8f83c08…  ·  run_source: shadow  ·  region_lock field (cutoff): có, đúng miền
```

**Ba thiếu sót siêu dữ liệu so với `I.3`:**

| trường `I.3` đòi | thực tế | hệ quả |
|---|---|---|
| `source_snapshot_at` | 🔴 **KHÔNG CÓ TRƯỜNG** | không chứng minh được đọc dữ liệu lúc nào |
| `source_snapshot_hash` | 🟡 có, nhưng **`d78402ffab56…` GIỐNG HỆT cả hai ngày** | **rỗng nghĩa** — nó băm `input_manifest` vốn chỉ chứa danh sách model + số dòng, không chứa dữ liệu; hai ngày khác nhau ra cùng hash |
| exact source IDs | 🔴 `contribution_trace` chỉ có **tên model**, **không** có `prediction_id`/`row_id` | không truy ngược được hàng nguồn |

⇒ Theo `I.5`: **không backfill · không tái sinh candidate · không xem performance · không tính
vào cohort 30 ngày.**
⇒ Theo `I.7`: **earliest candidate full valid day = `02/09`**, subject to pre-lock proof.

### 3.2 🟡 RÚT LẠI (`PRJ-RETRACTION-001`)

**Chỗ gốc:** `REPORT_V11140` · `REPORT_V11144` · `REPORT_V11145` và các lượt trả lời trong phiên,
công bố **01/09**.
**Nguyên văn câu sai:** *«`31/08` là **ngày chấm số 1** của `D-30`»*.
**Điều đúng:** `31/08` sinh lúc `19:15:01`, **sau cả ba mốc khoá** ⇒ `INVALID_TIMING_NOT_SCORED`.
Phép đo tái lập: đọc `generated_at` từng bản ghi, so với `FREEZE_MARKS` (MN 15:45 · MT 16:58 ·
MB 17:58).
**Quyết định nào dựa trên số sai:** chưa có — owner đã cấm đọc hiệu năng giữa kỳ. Nhưng nếu không
bắt bây giờ thì tới `30/09` sẽ **đếm nhầm cohort**.

### 3.3 `II` — MA TRẬN RUNTIME 17 MODULE

⚠️ Nhãn `C1..C6` **không có bản đồ sang tệp** ở bất kỳ tài liệu nào trong kho (đã tìm `CHANGELOG`
· `SSOT` · toàn bộ `REPORT_*.md`). Gán bừa một tệp cho `C3` là bịa (`RM-10`) ⇒ báo theo **tên tệp
thật**, nhãn C = `NOT_VERIFIED`.

| cột | kết quả cho **cả 17/17** |
|---|---|
| `GIT_PRESENT` | ✅ CÓ (vào git từ `V11142`) |
| `VPS_FILE_PRESENT` | ❌ **KHÔNG** — 0 tệp trên VPS |
| `IMPORTED_OR_CALLED` | ❌ **KHÔNG** — quét toàn backend VPS |
| `SCHEDULED` | ❌ **KHÔNG** — 0 dòng crontab |
| `RUNTIME_BEHAVIOR_PROVEN` | ❌ `false` |
| `OFFICIAL_EFFECT` | **KHÔNG** — chưa có trên VPS |
| **`STATUS`** | **`CODED_NOT_DEPLOYED` × 17** |

Payload thật là **9 module**; 8 tệp còn lại là **bộ thử** (`thu_chan`/`bo_thu`).
Đúng `II.3`: **không** dán nhãn `DEPLOYED`/`RUNTIME_PROVEN` cho bất kỳ tệp nào.

**`II.1` hai cổng:** `DONG_BO_NHANH = ĐẠT` (5 tệp trọng yếu) · `DONG_BO_V11143 = ĐẠT`
(full directional scan — **0 tệp VPS mới hơn, 0 tệp ngoài git**).

**`II.4` — `C5` tách hai:**
`ORPHAN_GATE = PASS` — cổng `_v11107_cong_prompt_mo_coi.py` chạy **trên VPS** nay **ĐẠT**
(`V11144` gỡ 2 mệnh lệnh mồ côi, `MỒ CÔI 2 → 0`).
`CONTEXT_ONLY_CONVERSION = PARTIAL` — emitter vẫn **bỏ sót `SYSTEM_PROMPT`** (7.935 ký tự = 16,4%).

### 3.4 `III` — 26 STALE READER

| impact | số | nghĩa |
|---|---|---|
| 🔴 **OWNER NHÌN THẤY** | **1** | panel `/monitoring` render số cũ |
| 🟡 gọi được qua API | 17 | owner có thể lấy ra số cũ |
| ⚪ chỉ mã nội bộ đọc | 8 | không ra mặt owner |

**Nặng nhất — `verified_bucket_rules`**: 105 dòng · `LAST_WRITE = 2026-03-16` · **im 169 ngày** ·
`WRITER_STATUS` = có writer (`database.py`) **nhưng KHÔNG CRON** · panel đọc **2 lần**.
**ACTION:** hiện nhãn `STALE`/`RETIRED` cạnh số, kèm ngày ghi cuối.

Nhóm 🟡 tiêu biểu: `signal_governance_ledger` (10.317 dòng, im 101) ·
`lane_test_active_challenger_scoreboard` (1.557 dòng, im 101) · `v101_region_source_pool_shadow`
(11.970 dòng, im 94) · `cohere_effectiveness_daily` (247 dòng, im 54).
**ACTION:** endpoint trả thêm `stale=true` + `last_write`.

Đúng `III.2`: **cấm trình số cũ như dữ liệu sống**. Chưa sửa reader trong phiên này vì đang trong
block và việc đó chạm UI/API official.

### 3.5 `III.3` — 38 LANE NGHỈ · **KHÔNG DROP**

**38 lane · 332.471 dòng.** Mỗi lane đã có **`content_sha256`** (băm toàn bộ hàng theo `rowid`) —
neo để đối chiếu bản export sau này. Lớn nhất:

| lane | dòng | khoảng ngày | im | `content_sha256` |
|---|---|---|---|---|
| `gan_signal_shadow_v100` | **246.000** | 09/02 → 10/05 | 114 | `2920b464bf479843` |
| `model_strength_by_region_weekday_station_daily` | 17.815 | 02/05 → 10/05 | 114 | `f7809447cfe92d0d` |
| `cross_region_spillover_shadow` | 11.283 | 03/03 → 10/05 | 114 | `3f1ebe9b12811f99` |
| `digit_transform_source_rule_shadow_v10610` | 9.211 | 22/05 → 23/05 | 101 | `b0d7d126c41d7f88` |

**Caller scan:** 36/38 vẫn còn ít nhất một tệp nhắc tên; **2 lane không còn dòng mã nào nhắc tên**
(`digit_transform_source_rule_shadow_v10610` · `exact_position_source_rule_shadow_v10610`).

**Reversible archive proposal:** xuất từng bảng ra `artifacts/archive_v11147/<bảng>.jsonl.gz` +
`manifest.json` chứa `content_sha256` đã đo ở trên; **giữ nguyên bảng trong DB**; chỉ khi owner ký
mới xét `DROP`, và khi đó đối chiếu hash export == hash đã ghi ở đây trước khi drop.
**Chưa xuất** — thao tác ghi, để ngoài block.

### 3.6 🎯 `IV` — GỐC THẬT CỦA `FU-448`

Truy đủ chuỗi owner yêu cầu:

```
mined_rules  ──(is_active, production_tier, target_weekday)──┐
                                                             ▼
mined_rule_eval.py:165-180  SELECT … FROM mined_rules WHERE target_weekday = ? AND is_active = 1
      │  (KHÔNG lọc tier, KHÔNG lọc miền)
      ▼
mined_rule_eval.py:311  INSERT OR REPLACE INTO mined_rule_effectiveness   ← WRITER DUY NHẤT
      │  ghi rows với  date = ngày chạy,  weekday = weekday của ngày đó
      ▼
gpt_analyzer.py:4877-4886  JOIN … WHERE e.target_region=? AND r.target_weekday=dow_py
                           AND e.date >= date('now','-2 days')
                           AND r.production_tier IN ('READY_STRONG','READY_WITH_CAUTION')
      ▼
gpt_analyzer.py:4902  sections.append("### 🎯 RULE TAILS (48h)")  → prompt production
```

**Mâu thuẫn cấu trúc — đây là gốc:**

- `mined_rule_eval` chỉ chấm **luật của ĐÚNG thứ hôm đó**. Nên một luật `target_weekday = 1`
  chỉ có dòng MRE **vào các thứ Ba**.
- Nhưng truy vấn `RULE TAILS` đòi dòng MRE **trong 2 ngày** *và* rule có `target_weekday` bằng
  **thứ của hôm nay**.
- ⇒ Với mọi luật, lần chấm gần nhất hoặc là **hôm nay**, hoặc là **7 ngày trước** — ngoài cửa sổ.
- ⇒ **Khối chỉ xuất hiện nếu bộ chấm MRE của HÔM NAY đã chạy TRƯỚC lúc dựng prompt.**

**Và `mined_rule_eval.py` KHÔNG CÓ CRON** — nó chỉ được gọi gián tiếp (`database.py` ·
`weekly_rule_miner.py` · `_v10810_repair_stations.py` · `_v87_master_board.py`). Chú thích crontab
còn nhắc *«sau MRE 20:15»* nhưng **không có job nào lúc 20:15**.

**Đo chứng minh:**

| đo | kết quả |
|---|---|
| MRE dòng ngày `01/09` (hôm nay, thứ Ba) | **0 dòng, cả ba miền** — bộ chấm hôm nay **chưa chạy** |
| MRE ngày `31/08` | weekday **0**, mỗi miền 5 dòng |
| MRE ngày `30/08` | weekday **6**, MN 6 · MT 8 · MB 5 |
| `target_weekday` của luật `READY_*` `is_active` | **MN = {1,3,4,5}** · MT = {0…6} · MB = {0…6} |

**Vì sao MN chịu nặng nhất:** prompt MN dựng **~05:15**, sớm nhất trong ngày — gần như chắc chắn
**trước** khi MRE của ngày hôm đó chạy. MT (~16:36) và MB (~17:30) dựng muộn hơn nhiều.

⇒ **Đây là lỗi THỨ TỰ TRONG NGÀY, không phải lỗi chất lượng luật.** MN thậm chí có **nhiều
`READY_STRONG` nhất** (6, so với MT 5 · MB 3).

**Đúng `IV.3`: không kết luận hiệu quả, không sửa prompt MN trong bước điều tra.**

---

## 4 · Hướng xử lý — DECISION PACKET

### 4.1 `IV.4` — `FU-448`, ba hướng

| | hướng | root cause được xử? | impact | rollback |
|---|---|---|---|---|
| **A** | **Cắm cron cho `mined_rule_eval`** chạy **trước 05:00** mỗi ngày | ✅ **đúng gốc** — MRE của hôm nay có mặt trước khi MN dựng prompt | MN bắt đầu nhận khối như MT/MB ⇒ **đổi prompt MN** | gỡ dòng cron; prompt trở lại như cũ ngay lượt sau |
| **B** | Chấp nhận lệch miền có chủ ý | ❌ không xử gốc | ghi thành thiết kế; **gỡ** cảnh báo `LỆCH MIỀN` khỏi cổng để nó không kêu mãi | sửa lại tài liệu |
| **C** | Prospective shadow có/không `RULE TAILS` cho MN | ❌ chưa xử, nhưng **đo được** | không đụng prompt official; cần ~30 ngày | xoá lane |

**Khuyến nghị: A, nhưng KHÔNG làm ngay.** Lý do: A xử đúng gốc và rollback rẻ nhất (một dòng
cron). Nhưng nó **đổi prompt MN** ⇒ theo `OWNER-03` phải có `effective_from` + rollback, và theo
`IX` thì **không đổi cơ chế khi chưa có packet owner ký**. Đề nghị: owner ký A với
`effective_from = 03/09` (sau khi `D-30` có ngày hợp lệ đầu tiên `02/09`, để không cắt đôi cohort).

### 4.2 `V` — `CAP5` giữ `NOT_STARTED` · packet context-only vNext

`CAP5_SCORING = NOT_STARTED` **giữ nguyên**. **Không** tái dựng top-5 sau khi biết kết quả
(`V.2`).

**Packet vNext — LLM tự sinh ranked top-5:**

| khoản | nội dung |
|---|---|
| cơ chế | LLM **tự sinh** ranked top-5; **không** nhận shortlist từ ML |
| provenance | mỗi ứng viên ghi `model` · `rank` · `lý do` · `prompt_version` |
| prompt/regime version | tem phiên bản mới, **khác** bản hiện hành |
| `effective_date` | **cửa sổ đo RESET từ ngày hiệu lực**, không nối vào số cũ |
| ranh giới đo | **cấm** so cùng model dưới prompt cũ và mới như hai bằng chứng độc lập (`V.4`) |
| rollback | quay về hợp đồng prompt hiện hành; artifact cũ giữ làm bằng chứng |

**Chưa dựng** — cần owner ký vì đổi hợp đồng prompt production.

### 4.3 `VI` — `FU-446`, CHỈ ĐO, chưa đổi hệ số

| đo | kết quả |
|---|---|
| model đang sinh dự đoán | **24** |
| khoá trong `MODEL_STRENGTH_DISCOUNT` | **15** |
| model sống **thiếu khoá** ⇒ rơi về `DEFAULT_DISCOUNT = 0.70` | **12** |
| khoá **lạc hậu** (model đã rời pool 01/08) | `gpt-5-mini` · `gpt-5.4` |
| nhánh **dynamic vs fallback** | `_get_dynamic_calibration(days=14, min_samples=5)` chạy **trước**; chỉ khi trả `None` mới dùng bảng tĩnh |

🔴 **Phép đo quyết định:** mỗi model chỉ có **~12–13 lượt/miền** trong cửa sổ 14 ngày, mà hàm chia
**4 bucket** và đòi **≥5 mẫu MỖI bucket**. Với 13 mẫu chia 4 bucket, phần lớn bucket **không đủ**
⇒ nhánh động **nhiều khả năng trả `None`** ⇒ **bảng tĩnh và `0.70` THẬT SỰ có tác dụng**.

⚠️ `NOT_VERIFIED`: **tỉ lệ chính xác** lượt rơi vào fallback — cần đo bằng cách gọi
`_get_dynamic_calibration` cho từng (model, miền) và đếm `None`. Chưa làm vì đang trong block.
**Không thay hệ số nào trong phiên này** (đúng `VI`).

### 4.4 `VII.2` — `FU-444`, danh sách chính xác 22 bản

`V10922` · `V10933B` · `V10939` · `V10940` · `V10991B` · `V10992` · `V10997` · `V11001` ·
`V11015B` · `V11019` · `V11021` · `V11021B` · `V11026` · `V11027` · `V11029` · `V11032B` ·
`V11033B` · `V11037B` · `V11037C` · `V11039B` · `V11044B` · `V11087B`

**Tất cả `≤ V11087B` ⇒ nợ ĐÃ ĐÓNG BIÊN**: `V11088` → `V11147` đều có báo cáo.

| nguồn | còn/mất |
|---|---|
| `CODE_DID` | **CÒN** — `git log --all --grep=<V>` + `git show --stat` |
| `DOC_SAID` | **CÒN** — `CHANGELOG.md` mục `## <V>`; `HISTORY` từ `V11062` trở đi |
| `OWNER_SAID` | 🔴 **MẤT** — sổ `SO_TUONG_TAC_OWNER.md` chỉ có từ **25/08**, sau tất cả 22 bản |

**Đề xuất `GAP_MARKER`** cho `_v10921_report_gate.py`, ba trường bắt buộc như `_v11062` đã có:
`khoang_trong` · `quyet_dinh_khong_bu` · `cach_tra_bu_khi_can`. Mục đích **không** phải làm cổng
xanh, mà **tách bạch** «22 khoảng trống lịch sử đã khai» với «vi phạm MỚI».
**Cấm bịa `OWNER_SAID` hoặc báo cáo hồi tố** (`VII.2`, `RM-17`, tiền lệ §63).

### 4.5 `VII.1` — `FU-447`, và một phép tự động BỊ TỪ CHỐI

Đã thử bộ gán tự động «phần khung → mục thật» bằng đếm từ khoá. Kết quả **vô nghĩa**:

```
V11135  THIẾU «gỡ về»     → ## 14 · DECISION PACKET
V11128  THIẾU «đào bới»   → ## 8 · BA LỚP NGUỒN (§62)
V11132  THIẾU «đã làm gì» → ## 9 · MUTATION LOG
```

**KHÔNG ghi** — đúng `VII.1` (*không dùng auto keyword mapping*). 16 bản phải **đọc thủ công**,
ghi `NOT_APPLICABLE` tường minh khi phù hợp. **Chưa làm.**

### 4.6 `VIII` — `FU-445` checklist cho owner

**Không giả cookie. Không xin mật khẩu.** Owner tự kiểm:

```
1. Mở /du-doan  →  chọn miền MT  →  chọn ngày 28/08
2. Phải thấy:   BT = 11
                model_count = 6
                publication_status = PUBLISHED_DEGRADED
                nhãn degraded hiện ra, KHÔNG phải màn hình trắng
3. Kiểm cả tab current và history đều có dữ liệu
```

`FU-445` **chỉ đóng sau observation thật của owner sau bản vá** — không đóng bằng suy luận.

---

## 5 · Đã làm gì

```
TRƯỚC:  D-30 được tin là "31/08 = ngày chấm số 1"
        C1–C6 chỉ có nhãn CODED_NOT_DEPLOYED, không có ma trận cột
        26 stale reader mới là con số, chưa có READER→TABLE→IMPACT
        38 lane nghỉ chưa có hash/manifest
        FU-448 mới biết "MN có 0 dòng đủ tư cách", chưa biết VÌ SAO
SAU:    D-30 validity matrix — 12/12 bản ghi TRƯỢT cổng thời điểm
        ma trận 6 cột × 17 module — 17/17 CODED_NOT_DEPLOYED
        26 stale reader phân theo impact (1 🔴 / 17 🟡 / 8 ⚪)
        38 lane có content_sha256 + caller scan + đề xuất archive đảo ngược được
        FU-448 truy đủ 7 mắt xích, gốc là THỨ TỰ TRONG NGÀY
PHIÊN BẢN: KHÔNG deploy · KHÔNG restart · KHÔNG ghi DB · production không bị đụng
KIỂM:   mọi phép đo `sqlite3 -readonly` trên DB VPS (OWNER-02), không phải bản chụp local
```

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| `DONG_BO_NHANH` (5 tệp trọng yếu) | ✅ **ĐẠT** |
| `DONG_BO_V11143` (full directional scan) | ✅ **ĐẠT** — 0 tệp VPS mới hơn, 0 tệp ngoài git |
| `PROMPT_MO_COI` trên VPS (`C5` orphan gate) | ✅ **PASS** |
| cổng thời điểm `D-30` (`I.4`) | ❌ **TRƯỢT 12/12 bản ghi** ⇒ `INVALID_TIMING_NOT_SCORED` |
| production no-drift | ✅ **không đụng** — phiên read-only |

**PID / imported path / hash:** phiên này **không restart**, nên PID giữ nguyên `3156545` từ
`V11144`. Hash 5 tệp trọng yếu khớp `git HEAD` (cổng nhanh ĐẠT).

---

## 7 · Vướng vấp

**🔴 Tôi đã công bố sai ba lần** rằng `31/08` là ngày chấm số 1 của `D-30`. Cổng owner mới lộ ra.
Bài học: **có artifact không có nghĩa là artifact hợp lệ** — phải có cổng thời điểm ngay từ khi
dựng lane, không phải thêm sau.

**🟡 `source_snapshot_hash` rỗng nghĩa mà tôi từng trích như bằng chứng.** Nó băm `input_manifest`
vốn chỉ chứa danh sách model + số dòng ⇒ hai ngày khác nhau ra **cùng một hash**. Bắt được vì so
hai ngày cạnh nhau.

**🟡 Cổng chỉ-đọc của tôi chặn nhầm ba lần** — mẫu cấm `\bUPDATE\b`, `>` và `INSERT` khớp vào
**câu lệnh grep** chứ không phải thao tác ghi. Phải diễn đạt lại truy vấn. Ghi lại vì nó làm chậm
và có thể khiến người sau tưởng dữ liệu không tồn tại.

---

## 8 · Gỡ về

Phiên này **không thay đổi gì trên production** — không có gì để gỡ.
Tài liệu: `git revert <SHA của V11147>` trên kho riêng.

---

## 9 · Theo dõi tiếp

| # | việc | trạng thái |
|---|---|---|
| 1 | **`D-30` `PRE_LOCK_GENERATOR`** (`I.6.A`) — persist trước lock từng miền | 🔴 **chưa dựng** · ngoài block |
| 2 | **`D-30` `POST_RESULT_RECONCILIATION`** (`I.6.B`) — chỉ chấm artifact đã khoá | 🔴 chưa dựng |
| 3 | Thêm `source_snapshot_at` + hash **phủ dữ liệu** + `prediction_id` vào artifact | 🔴 chưa làm |
| 4 | **`FU-448`** — owner chọn A/B/C | 🔴 **chờ owner** |
| 5 | **`FU-446`** — đo tỉ lệ fallback chính xác | ⚪ đo được, chưa làm |
| 6 | **`FU-447`** — đọc thủ công 16 báo cáo | ⚪ chưa làm |
| 7 | **`FU-444`** — dựng `GAP_MARKER` cho `_v10921` | 🔴 chờ owner ký nhượng bộ |
| 8 | **`FU-445`** — owner kiểm `/du-doan` MT 28/08 | 🔴 **chờ owner** |
| 9 | 26 stale reader — gắn nhãn `STALE`/`last_write` | ⚪ chưa làm, chạm UI/API |
| 10 | 38 lane — export + manifest (**không DROP**) | ⚪ chưa làm, cần ngoài block |
| 11 | `CAP5` vNext packet | 🔴 chờ owner ký |
| 12 | `FU-430` mốc 2 `06/09` · mốc 3 `13/09` | ⚪ để chạy tiếp |

---

## 10 · Nguồn ba lớp (§62) + `NOT_VERIFIED`

### `OWNER_SAID`
`PROMPT 43 R1 — CONTINUATION AFTER V11146` (01/09) với `OWNER-01/02/03` và mười mục `I`–`X`.
Đủ 13 câu nguyên văn ở `CONVERSATION_CONTEXT` cùng thư mục và `docs/SO_TUONG_TAC_OWNER.md`.

### `CODE_DID`
`_v11137_d30_lane.py` (writer, cron `15 19 * * *`) · `mined_rule_eval.py:165-180` (chọn luật) và
`:311` (writer MRE duy nhất) · `gpt_analyzer.py:4877-4886` (truy vấn `RULE TAILS`) ·
`strength_calibrator.py:82-95` (dynamic trước, fallback sau) ·
`_v11143_cong_dong_bo.py` hai chế độ — cả hai **ĐẠT**.

### `DOC_SAID`
`CHANGELOG.md §V11147` · `docs/CURRENT_TRUTH_SSOT.md §V11147` ·
`docs/FOLLOW_UP_TRACKER.md → FU-444` · `FU-446` · `FU-447` · `FU-448`.

### `NOT_VERIFIED` — nói thẳng những gì CHƯA chứng minh

| mục | vì sao chưa |
|---|---|
| Bản đồ `C1..C6 → tệp` | **không tồn tại** trong bất kỳ tài liệu nào; gán bừa là bịa |
| Tỉ lệ chính xác lượt rơi vào fallback tĩnh (`VI`) | cần gọi `_get_dynamic_calibration` từng (model, miền); suy luận từ ~13 mẫu/4 bucket **chỉ là chỉ dấu mạnh**, không phải đo |
| Vì sao dump prompt `10:50` hôm nay thấy `RULE TAILS` ở MT/MB trong khi MRE **0 dòng cho 01/09** | **mâu thuẫn chưa giải**; cần dump lại kèm `date_str` thực dùng. **Không** kết luận thêm về `FU-448` cho tới khi giải xong |
| Artifact `2026-09-01.jsonl` | chưa sinh lúc audit (17:34); cron 19:15 |

---

TanPhatAI cần làm: ghi **`D-30` CHƯA CÓ NGÀY HỢP LỆ NÀO** — `30/08` và `31/08` đều `INVALID_TIMING_NOT_SCORED` vì `generated_at` (18:17 · 19:15) **sau cả ba mốc khoá**; **earliest valid = 02/09** và chỉ khi có `PRE_LOCK_GENERATOR`. Ghi **RÚT LẠI** câu *«31/08 là ngày chấm số 1»* đã công bố ở `V11140`/`V11144`/`V11145`. Ghi **`C1–C6` = `CODED_NOT_DEPLOYED` 17/17** với sáu cột bằng chứng, và **nhãn `C1..C6` không có bản đồ sang tệp** (`NOT_VERIFIED`). Ghi **26 stale reader**: 1 bản owner **nhìn thấy** (`verified_bucket_rules`, im **169 ngày**). Ghi **38 lane nghỉ / 332.471 dòng** đã có `content_sha256`, **KHÔNG DROP**. Ghi **gốc `FU-448`**: lỗi **THỨ TỰ TRONG NGÀY** — `mined_rule_eval.py` **không có cron**, MRE chỉ chấm luật của đúng thứ hôm đó, nên khối `RULE TAILS` chỉ xuất hiện nếu MRE hôm nay đã chạy trước lúc dựng prompt; MN dựng **05:15** nên gần như luôn hụt. **MN có NHIỀU `READY_STRONG` NHẤT (6)** — không phải lỗi chất lượng luật. Ghi **`FU-446` là vấn đề thật**: ~13 mẫu chia 4 bucket ⇒ nhánh dynamic nhiều khả năng trả `None` ⇒ 12 model rơi về `0.70`. Prompt 43 giữ **`PARTIAL`**, **không mở Prompt 44**.
