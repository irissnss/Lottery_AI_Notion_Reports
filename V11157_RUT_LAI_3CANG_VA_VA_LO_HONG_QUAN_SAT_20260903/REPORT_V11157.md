# REPORT V11157 — 🔴 **RÚT LẠI `NO_VALID_3CANG`** · vá lỗ hổng quan sát · 03/09/2026

> `CURRENT_ACTOR = CLAUDE_CODE` · `SCOPE = RIÊNG — LOTTERY AI`
> **`PROMPT_STATE` = PROMPT 43 R1 · `PARTIAL`** — không mở Prompt 44.
> **`POOL_VERDICT = HOLD`** · **official chưa đổi một ký tự** · `NOTION_MUTATION = FORBIDDEN`.

---

## 1 · QUICK SUMMARY

Owner correction sáng nay **lật kết luận `V11156` của tôi**, và đọc lại mã thì bộ chọn prefix
**tốt hơn hẳn** những gì tôi đã báo. Ba việc trong phiên:

| | |
|---|---|
| 🔴 **rút lại** | `NO_VALID_3CANG` — prefix + BT **CHÍNH LÀ** thiết kế owner, không phải vi phạm |
| 🟢 **verdict sửa** | `3CANG_PIPELINE = SUBSTANTIALLY_VALID`, thiếu **tầng lineage/trace** |
| 🔴 **`SCHEDULED_SHADOW_OUTPUT_PROVEN` = PENDING** | scheduler **đã nổ** 11 lượt thật, nhưng **không quan sát được** prompt sạch ⇒ vá instrument rồi deploy |

---

## 2 · ACTIVE PLAN · STATUS · GOAL · NEXT · BLOCKER

| | |
|---|---|
| **ACTIVE_PLAN** | `PLAN-20260723-lottery-doc-restructure` |
| **STATUS** | Wave 4 deploy xong · Wave 5 đang làm · Prompt 43 R1 **`PARTIAL`** |
| **GOAL** | đóng `SCHEDULED_SHADOW_OUTPUT_PROVEN`, rồi 3-càng lineage, rồi Arena → Total v2 |
| **NEXT** | đọc `prediction_trace` sau lượt shadow **16:00/17:00 hôm nay** để đóng `A` |
| **BLOCKER** | không có blocker owner; chờ **lịch**, không ép gọi tay |

---

## 3 · OWNER CORRECTION — nguyên nghĩa

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI.** Mệnh lệnh trực tiếp trong IDE, hiệu lực
> ngay (`PRJ-INTERACTION-LEDGER-001`).

**03/09 ~09:00 ICT, nguyên văn:**

> *«3 càng anh đang xây dựng với số đuôi bạch thủ.»*
> *«Vấn đề anh cần ở đây là đơn model có cần output không?»*

**Nghĩa đã khoá:**

1. 3-càng **KHÔNG** phải bộ sinh trực tiếp trên `000–999`.
2. 3-càng = **prefix một chữ số + BT hai chữ số** của **đúng lane**.
3. **Đơn model KHÔNG bắt buộc** output 3-càng.
4. Đơn model tiếp tục output **ranked BT top-K** + confidence/strength + provenance theo `UCC`.
5. Bộ chuyên trách nhận BT đã chọn → **xếp hạng prefix 0–9** → ghép.
6. Mọi wording *«direct 3-digit generator»* ⇒ **`VOID / DO NOT EXECUTE`**.
7. **Không** lấy trúng hai số đuôi để gọi là trúng 3-càng.
8. **Không** biến 3-càng thành voter độc lập trong `TOTAL`.

### 🟢 Trả lời trực tiếp câu owner hỏi

**Không. Đơn model KHÔNG cần output 3-càng.** Và `UCC` **không cần sửa** — `ranked top-K adapter`
(`_v11156_ranked_adapter.py`, đã xong hôm qua) **vốn đã** đúng hợp đồng này: mỗi model xuất
**ranked BT top-K** + `confidence` + `provenance`, **không có trường 3-càng nào**. Bộ thử `13/13`
gồm phép *«model không có field 3-càng vẫn `PASS` `UCC`»*.

---

## 4 · SCHEDULED RUNTIME PROOF 05:00 — **PENDING**, kèm bằng chứng

### Cái ĐÃ chứng minh được

```
scheduler nổ thật : 11 lượt shadow · 05:22:48 → 05:32:12 ngày 03/09
PID               : 3249633 — KHÔNG restart giữa chừng
env               : PYTHONUNBUFFERED=1 LLM_CONTEXT_ONLY_V2_LANE=shadow
health            : 200
official          : 30 lượt mới, KHÔNG đổi hành vi
final_bundles     : +1 (2026-09-03 MN bt=10, cron 05:20:54)
neo 558 FINAL     : a82c508d3569abda… KHỚP
```

Mẫu lượt: `qwen3-max-thinking MN ["02","73"]` · `gpt-5-mini MN ["78","12"]` ·
`claude-opus-5-fast MN ["86","15"]` …

### 🔴 Cái KHÔNG chứng minh được — và vì sao

| đường | kết quả |
|---|---|
| `journalctl -u lottery` | chỉ bắt output module `logging`, **không bắt `print()`** ⇒ **0 dòng** `[Phase 14A][CONTEXT_ONLY_V2]` **cả ngày** |
| `prompt_layers` trong trace | **giống hệt** ở cả bốn nhóm: `{"context_pack":"CTX-18.6","prompt_bundle":"PB-20.1","reasoning_rulebook":"RR-16.5","system_prompt":"SP-4.4"}` |
| so độ dài prompt | **nhiễu** — sai phân đôi `−799` ký tự (shadow `−130`, official `+669`) trong khi khối bảng xếp hạng đo được là **`~1.281`** |

**Nhãn tách đúng ba tầng theo mục `A`:**

| nhãn | trạng thái |
|---|---|
| `DEPLOYED` | ✅ **ĐẠT** — 02/09 22:46:51 |
| `SERVICE_ENV_RUNTIME_PROVEN` | ✅ **ĐẠT** — `/proc/3249633/environ` có `LANE=shadow`; định tuyến `shadow→True` `official→False` |
| `SCHEDULED_SHADOW_OUTPUT_PROVEN` | 🔴 **PENDING** — có lượt thật nhưng **chưa quan sát được** prompt sạch |

**Không pass-wash.** Đây là **lỗ hổng quan sát**, không phải lỗi deploy — và đã vá (mục 8).

---

## 5 · ROLE-AT-TIME REPAIR — tách rõ từng tầng

| tầng | trạng thái |
|---|---|
| **code** | ✅ `_v11155_vai_tro_theo_thoi_diem.py` + vá `_ho()` trong materializer production |
| **test** | ✅ **19/19** META, gồm phép chống lookahead kiểm bằng **chữ ký hàm** |
| **đo tác dụng** | ✅ trên **bản sao DB 799 MB**: `8.853 → 12.967` lượt được phân loại (**+46,5%**); cứu **4.132** lượt bị bỏ im lặng, loại đúng **18** lượt `manual` đếm nhầm |
| **deploy** | 🔴 **CHƯA** — mã đã sửa nhưng chưa lên VPS |
| **runtime** | 🔴 **CHƯA** |
| **migration/recompute 877 dòng** | 🔴 **CHƯA** — artifact trước/sau đã có, chưa áp |

---

## 6 · CURRENT-STATE MAP CỦA 3-CÀNG

| khâu | thực tế đo được |
|---|---|
| **OWNER TERM** | «3 càng» |
| **BUSINESS INTENT** | prefix 1 chữ số + BT 2 chữ số của đúng lane |
| **UI LABEL** | thẻ «Lô 3 Càng» trên `/du-doan`; có cả trên `/choi` |
| **CODE SYMBOL** | `_generate_lo3_frequency(bach_thu, region, date_str)` — `main.py:10587` |
| **CALLER official** | `main.py:10307` — **SAU** chuỗi override `10228–10302` ⇒ bám **`bach_thu` thực sự công bố** ✅ đúng `D.2` |
| **CALLER test** | `main.py:12425` (MB cứng) · `main.py:15568` (theo region) — dùng `cand_bt` riêng ✅ không clone |
| **CALLER backfill** | `_backfill_bundles.py:130` |
| **INPUT BT** | `str(bach_thu).strip().zfill(2)[-2:]` — **giữ số 0 đầu** ✅ |
| **PREFIX SELECTOR** | đếm **(prefix+BT) xuất hiện như chuỗi con ở BẤT KỲ vị trí nào** trong giải, **180 ngày**; tiebreak tất định bằng đếm đuôi-giải. `V10753.1` backtest **118 ngày**: thắng cửa sổ 90 ngày ở **cả ba miền** (MT `14,4%` vs `8,5%`) |
| **NO-LOOKAHEAD** | ✅ `WHERE date >= cutoff AND date < date_str` — **chặt**, không lấy chính ngày đích |
| **DB OBJECT** | cột `final_bundles.lo3` + `final_bundles.lo3_status` |
| **WRITER** | `database.py:4649` (`save_final_bundle`) · `:4702` đặt `lo3_status = 'PENDING' if lo3 else 'N/A'` |
| **PERSIST trước lock?** | ✅ ghi cùng lúc lưu bundle |
| **SCORER** | `database.py:~4886` — gom `str(val)[-3:]` của **mọi giải, mọi đài**, so **chuỗi**; `WIN` chỉ khi khớp đủ 3 chữ số |
| **hai số đuôi có ăn gian?** | ✅ **không** — chú thích ghi rõ đã sửa lỗi cũ *«lo3=446 → tail=46 → matched BT=46 → false WIN»* |
| **kết quả rỗng** | ✅ `PENDING`, **không** tự `LOSE` |
| **CURRENT STATUS** | **`SUBSTANTIALLY_VALID`** cho thiết kế owner |

### 🟡 Thiếu — tầng lineage/trace (mục `V`)

| mục `V` đòi | có? |
|---|---|
| `parent_bt` · `three_digit` · persist · scorer · `status` | ✅ |
| `ranked_prefixes` (10 chữ số kèm điểm) | ❌ chỉ lưu **người thắng** |
| `prefix_method_version` | ❌ |
| `parent_bt_source` · `parent_bt_finality` · `lane` | ❌ |
| `cutoff_at` · provenance hash · `official_output` | ❌ |

⇒ **Việc còn lại KHÔNG phải viết generator mới** — mà là **thêm tầng ghi vết** quanh bộ chọn
đang chạy đúng. Chỉ `(bach_thu[0]+1) % 10` khi không có dữ liệu là **tuỳ tiện**, nhưng đó là
fallback chứ không phải đường chính.

---

## 7 · RECONCILIATION — vì sao `V11128` không tìm thấy pipeline

`V11128` ghi *«không tìm thấy writer/cột persistent 3-càng trong `final_bundles` và 253 bảng»*.
Đo lại hôm nay: **có** cột `lo3` và `lo3_status`, **có** writer `database.py:4649`.

Cách đọc thẳng thắn: `V11128` tìm theo **tên** (`3cang` · `three_cang` · `ba_cang`) — và
**không tên nào tồn tại**; 3-càng nằm dưới tên `lo3`. Đây đúng `RM-10` — **kết luận theo tên
đoán**. Phép quét `sqlite_master` cho `0 hit` là **đúng sự thật về tên**, nhưng **sai kết luận
về nghiệp vụ**.

Bài học ghi lại: tìm theo **nghĩa nghiệp vụ + caller + writer + reader**, không chỉ theo tên —
đúng điều mục `III` của prompt hiện hành khoá là `DO_NOT_CREATE_DUPLICATES`.

---

## 8 · FILES CHANGED

| tệp | thay đổi |
|---|---|
| `web/backend/gpt_analyzer.py` | thêm 3 khoá regime vào `prediction_trace`; thêm 2 tham số tuỳ chọn cho `log_prediction_trace`; nối từ điểm gọi `:6623` |
| `docs/FOLLOW_UP_TRACKER.md` · `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` · `AUTOMATION_STATE/HISTORY` | bốn mặt `V11157`, `governance_seq → 473` |

**Không** đổi schema. **Không** đụng writer `final_bundles`. **Không** thêm bảng/route/generator.

---

## 9 · SCHEMA/OBJECT BEFORE/AFTER

**Không có thay đổi schema.** Ba khoá mới nằm trong `prediction_trace.jsonl` — tệp
**append-only**, không phải bảng DB:

```
+ context_only_regime         : "CONTEXT_ONLY_V2" | "LEGACY_PROMPT"
+ context_only_lane_mode      : "off" | "shadow" | "all"
+ context_only_is_shadow_lane : bool
```

---

## 10 · TESTS VÀ RAW RESULT COUNTS

| bộ thử | kết quả |
|---|---|
| `_v11152_test_lane.py` | ✅ **11/11** |
| `_v11150_contamination_gate.py --meta` | ✅ **17/17** |
| `_v11150_test_contract.py` | ✅ **37/37** |
| `_v11156_ranked_adapter.py --tu-kiem` | ✅ **13/13** |
| `_v11155_test_vai_tro.py` | ✅ **19/19** |
| `_v11062_nang_version.py --kiem` | ✅ `ĐẠT` · `seq 473` |
| **tổng** | **97 phép, 0 hỏng** |

---

## 11 · PRE/POST HASHES · PID · NO-DRIFT

```
PRE   PID 3249633 · gpt_analyzer f83e6f3c1eca2f08 · env LANE=shadow · health 200
POST  PID 3279630 · gpt_analyzer ff1e1a9f8c66db68 · env LANE=shadow · health 200
      /proc/3279630/environ có LANE=shadow : CÓ
      định tuyến: LANE=shadow · shadow→True · official→False
neo 558 FINAL  a82c508d3569abda…  KHÔNG DRIFT (trước và sau)
4 bảng khoá    predictions 14.080 · final_bundles 562 · lottery_results 15.403
               · model_daily_eval 13.903 — KHÔNG mất dòng
```

Backup bốn lớp chạy lại trước deploy: 6 tệp mã/cấu hình + **DB đầy đủ**
(`integrity_check = ok`) + mốc.

---

## 12 · LINEAGE EXAMPLES

| ca | bằng chứng |
|---|---|
| **official** | `main.py:10307` gọi sau override ⇒ `lo3` bám `bach_thu` **đã công bố**, không phải `ranked[0]` |
| **override** | 78 lần lịch sử `bach_thu ≠ ranked[0]`; hiện chỉ **MN** còn override (~1/3 số ngày) ⇒ MN là miền duy nhất mà phân biệt này còn hiệu lực |
| **shadow/test** | `main.py:12425` · `:15568` dùng `cand_bt` **riêng** ⇒ **không clone** 3-càng official |
| **leading zero** | `zfill(2)[-2:]` ở đầu hàm ⇒ BT `"07"` giữ nguyên `"07"`, ghép prefix `"0"` ra `"007"` |
| **derived per-model** | 🔴 **chưa có** — cần nhãn `DERIVED_FROM_MODEL_BT` theo `D.3` |

---

## 13 · ROLLBACK ĐÃ KIỂM

`python web/backend/_v11154_deploy.py --go-ve` — **một lệnh**, tự kiểm lại health + neo.
**Đã chứng minh chạy được thật** đêm 02/09 (`GO_VE_OK`, neo nguyên, không mất dòng nào), không
phải chỉ viết ra.

Kho backup: `backups/V11154_deploy_context_only_shadow/` — DB `integrity_check = ok`.

---

## 14 · COMPLETION RECONCILIATION

| hạng mục | trạng thái |
|---|---|
| context-only lane shadow | **`RUNTIME_LOADED`** (chưa `RUNTIME_PROVEN` ở tầng scheduled output) |
| instrument regime vào trace | **`DEPLOYED`** — chờ lượt 16:00/17:00 để thành `RUNTIME_PROVEN` |
| role-at-time repair | **`TESTED`** — chưa `DEPLOYED` |
| recompute 877 dòng | **`NOT_STARTED`** |
| ranked top-K adapter | **`TESTED`** |
| 3-càng audit | **`AUDITED_ONLY`** |
| 3-càng lineage/trace | **`NOT_STARTED`** |
| Arena · Total v2 · Combo v2 · Final v2 | **`NOT_STARTED`** |
| Cutover Packet | **`BLOCKED`** — cổng `XV.D`, cần owner |

---

## 15 · OWNER_SAID / CODE_DID / NOT_VERIFIED

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| 03/09 ~09:00 | *«3 càng anh đang xây dựng với số đuôi bạch thủ.»* |
| 03/09 ~09:00 | *«Vấn đề anh cần ở đây là đơn model có cần output không?»* |

### `CODE_DID`

- `main.py:10587-10640` bộ chọn prefix: `zfill(2)` · `date < date_str` · đếm chuỗi con 180 ngày
- `main.py:10307` gọi **sau** override `10228–10302`
- `database.py:4649` writer · `:4702` `lo3_status` · `:~4886` scorer exact 3 chữ số
- scheduler nổ **11 lượt shadow** `05:22–05:32` · `PID 3249633`
- deploy instrument: `PID 3249633 → 3279630` · `ff1e1a9f8c66db68`
- 97 phép thử, 0 hỏng · `governance_seq 473`
- commit riêng `f93f498` · `4087728`

### `NOT_VERIFIED`

- **prompt shadow 05:00 có thật sự sạch không** — chờ lượt 16:00/17:00 với instrument mới
- role-at-time repair trên **runtime production**
- `ranked_prefixes` · `prefix_method_version` · `parent_bt_source` — **chưa tồn tại**
- 3-càng phạm vi đài/miền: scorer gom **mọi đài** trong `station_results`; **chưa** kiểm nó có
  đúng bộ đài của miền hay không
- `DERIVED_FROM_MODEL_BT` per-model — chưa có

---

## 16 · ATTRIBUTION LEDGER

| việc | ai |
|---|---|
| correction 3-càng = prefix + BT | **owner**, 03/09 ~09:00 |
| phát hiện `journalctl` không bắt `print()` | agent |
| phát hiện `NameError` trong bản vá của chính agent | agent (kiểm tầm biến trước khi deploy) |
| rút lại `NO_VALID_3CANG` | agent, sau correction của owner |
| `V10753.1` backtest 118 ngày `substring_180` | **có sẵn trong mã**, không phải phát hiện mới |

---

## 17 · CROSS-LAYER MATRIX

| tầng | 3-càng | context-only shadow | role-at-time |
|---|---|---|---|
| code | ✅ có, đúng thiết kế | ✅ | ✅ |
| test | 🟡 chưa có bộ thử riêng | ✅ 11/11 + 17/17 | ✅ 19/19 |
| deploy | ✅ đang chạy từ lâu | ✅ 02/09 + 03/09 | ❌ chưa |
| runtime | ✅ ghi `lo3` mỗi bundle | 🟡 env proven, output PENDING | ❌ |
| lineage | ❌ thiếu | ✅ 3 khoá mới | ✅ artifact 877 dòng |
| UI | ✅ `/du-doan` · `/choi` | — | — |

---

## 18 · PUBLIC SAFETY GATE

Không có credential · không có khoá API · không có đường dẫn nhạy cảm ngoài đường dẫn dự án đã
công bố từ trước · không có dữ liệu cá nhân · **không** dán mã production. Số liệu đều là số đếm
và hash rút gọn.

---

## 19 · PUSH

Riêng `f93f498` · `4087728`. Công khai: bản này.

---

## 20 · MỘT NEXT ACTION DUY NHẤT

**Đọc `prediction_trace` sau lượt shadow 16:00/17:00 hôm nay**, xác nhận
`context_only_regime = "CONTEXT_ONLY_V2"` cho lane shadow và `"LEGACY_PROMPT"` cho official —
để đóng `SCHEDULED_SHADOW_OUTPUT_PROVEN`.

---

## Trạng thái cuối — bắt buộc ghi rõ

- **Prompt 43 R1 vẫn `PARTIAL`** — còn `SCHEDULED_SHADOW_OUTPUT_PROVEN` và role-at-time runtime.
- **`POOL_VERDICT = HOLD`.**
- **Official chưa đổi.**
- **3-càng:** `SUBSTANTIALLY_VALID` cho thiết kế prefix+BT, nhưng **chưa gọi là hợp lệ đầy đủ**
  vì thiếu `ranked_prefixes` · `prefix_method_version` · `parent_bt_source/finality` ·
  `cutoff_at`.
- **Không mở Prompt 44. Không mở FU mới** — umbrella `FU-449`/`FU-450`.

---

TanPhatAI cần làm: ghi **`V11157`** — riêng `f93f498` + `4087728`, `seq 473`. Ghi **RÚT LẠI `NO_VALID_3CANG`** của `V11156`: owner xác nhận **prefix + BT CHÍNH LÀ thiết kế**, wording *«direct 3-digit generator»* nay **`VOID`**; ba lựa chọn A/B/C **HUỶ** vì tiền đề sai. Ghi **verdict sửa: `3CANG_PIPELINE = SUBSTANTIALLY_VALID`** — không lookahead (`date < date_str`), giữ số 0 đầu, prefix chọn bằng **đếm chuỗi con 180 ngày có backtest `V10753.1`**, official bám **`bach_thu` sau override**, scorer **exact 3 chữ số mọi giải**, rỗng ⇒ `PENDING`; **thiếu tầng lineage/trace**. Ghi **trả lời câu owner: đơn model KHÔNG cần output 3-càng**, và **`UCC` không cần sửa** — ranked adapter vốn đã đúng hợp đồng. Ghi **`SCHEDULED_SHADOW_OUTPUT_PROVEN = PENDING`** — scheduler **đã nổ 11 lượt thật** nhưng `journalctl` **không bắt `print()`** và `prompt_layers` giống hệt bốn nhóm ⇒ **cấm pass-wash**; đã vá bằng 3 khoá regime trong `prediction_trace` và deploy (`PID 3249633 → 3279630`). Ghi **`V11128` kết luận theo TÊN** (`RM-10`) — 3-càng vốn nằm dưới tên `lo3`. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
