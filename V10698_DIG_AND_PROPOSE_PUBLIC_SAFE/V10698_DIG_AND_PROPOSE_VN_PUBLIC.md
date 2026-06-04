# V10698 — Đào sâu & đề xuất (READ-ONLY) — Region-Day audit follow-up

Public-safe. Ngày T5 2026-06-04. Không sửa code, không deploy, không update Notion, không đụng MB lane (V10694), không đụng MN/MT, không đụng official.

---

## TÓM TẮT KẾT QUẢ

| Hạng mục | Kết luận |
|---|---|
| F1 mốc giờ — gốc rễ + phân loại | Đã làm rõ 3 trục khác nhau (giờ xổ thực / done-flag / cron). 6 chỗ ghi 16:38/17:38/18:38 là di sản cũ, logic chính dùng 16:36/17:36/18:36 đúng. |
| Main.py 3-way (E7) | ✅ **ĐÃ SẠCH** — local hash = VPS hash = `c81ab73644aa8238`, cùng 770390 bytes, VPS == origin/master |
| Ma trận 14/14 contract | ✅ **14/14 PASS** với evidence file:dòng:hàm cụ thể (lưu `evidence/V10698_CONTRACT_MATRIX.json`) |
| Leakage backtest/eval | ✅ **0 vi phạm** — không có ca MB(D)→MN/MT(D), không có MT(D)→MN(D) |
| §36G 04/06 | ⏳ Chờ chu kỳ tự nhiên (MT 17:30, MB 18:30); 03/06 đã chứng minh 4/4 PASS |

---

## 1. F1 — Mốc giờ: đào toàn bộ + phân loại 3 trục + đề xuất

### 1.1 Bảng tất cả nơi nhắc mốc giờ (sau khi grep `web/backend/*.py`)

| File | Dòng | Giá trị | Vai trò |
|---|---|---|---|
| `prompt_registry.py` | 112 | `MN(16:10)→MT(17:10)→MB(18:15)` | (a) Giờ xổ thực tế |
| `gpt_analyzer.py` | 3830 | `MN(16:10) → MT(17:10) → MB(18:15)` | (a) Giờ xổ thực tế |
| `gpt_analyzer.py` | 2447 | "MN xổ xong 16:38, MT xổ xong 17:38, MB xổ xong 18:38" | (b) Done-flag — SAI (legacy) |
| `gpt_analyzer.py` | 2446 | "Sau 18:36 → preview CLOSING" | (b) Done-flag — ĐÚNG |
| `_v10693_mb_perpos_predictor.py` | 97 | "drawn before MB 18:15" | (a) Giờ xổ thực tế |
| `_v10694_install_cron.py` | 3 | "after MB draw 18:15" | (a) Giờ xổ thực tế |
| `filter_2_so_cuoi.py` | 180, 295 | "MN (16:15) → MT (17:15) → MB (18:15)" | (a) Giờ xổ thực tế (15 ≠ 10, drift nhỏ) |
| `main.py` | 3760-3763 | "before 16:38 ... before 17:38 ... before 18:38 ... after 18:38" | (b) Done-flag DOCSTRING — SAI (legacy) |
| `main.py` | 3774-3776 | `mn_done=16:36 mt_done=17:36 mb_done=18:36` | (b) Done-flag LOGIC — ĐÚNG |
| `main.py` | 3790-3798 | `draw_time="16:38"/"17:38"/"18:38"` | (b) Done-flag UI LABEL — SAI (legacy) |
| `main.py` | 6158-6160 | "MN: ~16:38 / MT: ~17:38 / MB: ~18:38" | (b) Done-flag docstring — SAI (legacy) |
| `scheduler.py` | 14-18 | "SCRAPE_PHASE_START MN: 16:30 / MT: 17:30 / MB: 18:30" [V17.11] | (c) Cron anchor |
| `scheduler.py` | 1434 | window `MN: 16:30:00 → 16:42:00`, `MT: 17:30:00 → 17:42:00` | (c) SLA window |
| `scheduler.py` | 7823-7825, 9111-9113, 9131-9137, 9160-9162 | `schedule_mn/mt/mb` = `16:30/17:30/18:30` [V17.11 Owner-Lock] | (c) Cron anchor seeds |
| `scheduler.py` | 7914-7926, 9116-9117, 9133-9136, 9163-9164 | `ai_predict_mt_time=16:42`, `ai_predict_mb_time=17:42` | (c) Cron fallback AI |
| `database.py` | 2506-2507, 4012-4017 | seeds same as scheduler | (c) DB seed |
| `meta_data_collector.py` | 223 | comment "MN(1st ~16:30) → MT(2nd ~17:30) → MB(3rd ~18:30)" | (c) Cron anchor reference |
| `_v96_master_tracker.py` | 69-71 | "16:30 MN cascade / 17:42 MT rerun_post_mn / 18:30 MB rerun_post_mt" | (c) Cron schedule |

### 1.2 Bảng giờ canonical 3 trục (HARDLOCK đề xuất)

| Trục | MN | MT | MB | Nguồn truth |
|---|---|---|---|---|
| **(a) GIỜ XỔ THỰC TẾ** (đài công bố) | 16:10 | 17:10 | 18:15 | `prompt_registry.py:112`, `gpt_analyzer.py:3830`, `_v10693:97` |
| **(b) DONE-FLAG** (mốc state machine coi đã xổ xong) | **16:36** | **17:36** | **18:36** | `main.py:3774-3776` (LOGIC ĐÚNG), `gpt_analyzer.py:2446` |
| **(c) GIỜ CRON ANCHOR** (V17.11 L3 Owner-Lock) | 16:30 | 17:30 | 18:30 | `scheduler.py:7823-7825`, `database.py:4012-4017`, `.Antigravityrules.md §36H` |
| **(c') GIỜ CRON FALLBACK AI PREDICT** | (—) | **16:42** (AI predict MT sau MN scrape) | **17:42** (AI predict MB sau MT scrape) | `scheduler.py:9116-9117`, `database.py:4016-4017` |

**Mối liên hệ**: scrape_anchor (16:30) → ~6 phút retry/verify → done-flag (16:36) → fallback AI cron (16:42).

### 1.3 main.py 3-way conflict (E7) — XÁC NHẬN ĐÃ SẠCH

- LOCAL `web/backend/main.py`: `sha256=c81ab73644aa8238` mtime 2026-06-04 11:28:35, bytes 770390
- VPS runtime `web/backend/main.py`: `sha256=c81ab73644aa8238` mtime 2026-06-04 09:13:11, bytes 770390
- VPS git: HEAD `94242fb`; `git diff origin/master -- main.py` = sạch
- → **3-way KHỚP byte-for-byte.** Audit V10697 trên đúng bản runtime đang phục vụ live.

### 1.4 ĐỀ XUẤT F1 (chưa làm, chờ owner OK)

**Vấn đề thực**: 6 chỗ trong `main.py` (dòng 3760-3763 docstring, 3790-3798 UI label, 6158-6160 docstring) + 1 chỗ trong `gpt_analyzer.py:2447` ghi `16:38/17:38/18:38` là **di sản cũ**, không khớp logic state-machine `mn_done=16:36`. Cosmetic drift, không ảnh hưởng prediction.

**3 phương án:**

| Phương án | Mô tả | Rủi ro | File / dòng đụng | Rollback | Vì sao an toàn |
|---|---|---|---|---|---|
| **A. Sửa lẻ ngay (chỉ F1)** | Edit 6 chỗ trong `main.py` + 1 trong `gpt_analyzer.py` thay `38 → 36` | ⚠️ Trung — `main.py` 770KB, dù VPS=local đang khớp, nếu upload đè cả file mà có bất kỳ thay đổi runtime khác từ MN/MT chạy sáng đè lên → mất dữ liệu | `main.py` ~7 dòng, `gpt_analyzer.py` 1 dòng | git revert + restart | Có thể, nhưng phải dùng StrReplace từng dòng + sftp đúng file thay đổi |
| **B. GỘP vào lần đối soát main.py kế tiếp** | Khi nào có việc khác cần sửa main.py thì gộp F1 cùng commit | ✅ Thấp nhất — không có deploy riêng | Same | Same | Tránh tách deploy nhỏ, giảm bề mặt rủi ro |
| **C. Bỏ qua (không sửa)** | Cosmetic 16:38 vs 16:36 không ảnh hưởng accuracy. Giữ nguyên. | ✅ 0 rủi ro | 0 | N/A | Logic chính xác; chỉ owner đọc UI thấy không nhất quán 2 phút |

**Khuyến nghị: PHƯƠNG ÁN B** (gộp vào lần đụng main.py kế tiếp).
**Lý do**: 
- `main.py` 770KB là file shared với chat MB (`MB_MANUAL_EXPERIMENT_ENABLE` flag) — bất kỳ thay đổi riêng nào cũng có rủi ro merge conflict tương lai.
- Cosmetic 2 phút không tác động prediction → không khẩn.
- Nguyên tắc "no partial fix" `.Antigravityrules.md` — sửa khi có cơ hội batch.
- Khi sửa, dùng **StrReplace từng dòng vùng giờ** (không upload đè cả file) để tránh ghi đè dữ liệu runtime MN/MT đang chạy.

**Cách tránh ghi đè sai bản main.py:**
1. Trước sửa: `sha256sum` local + VPS phải khớp (đã có proof 1.3).
2. Khi deploy: dùng StrReplace cho từng dòng cụ thể qua sftp file mới (KHÔNG `git pull` đè).
3. Sau deploy: `git diff origin/master -- main.py` phải sạch + 4 official tables zero drift + service restart smoke test.

---

## 2. MA TRẬN CONTRACT 14/14 (đầy đủ evidence file:dòng:hàm)

Chi tiết JSON tại `evidence/V10698_CONTRACT_MATRIX.json`. Tóm tắt:

| # | Hạng mục | Code evidence | Status |
|---|---|---|---|
| C1 | `predictions.date == target_date_vn` | `database.py` schema (no `target_date` column) | ✅ PASS |
| C2 | MN target chỉ dùng D-1 | `gpt_analyzer.py:5080` `_PRIOR_REGIONS["MN"]=[]` | ✅ PASS |
| C3 | MT target dùng D-1 + MN(D) | `gpt_analyzer.py:5081` + `scheduler.py:5674-5676` | ✅ PASS |
| C4 | MB target dùng D-1 + MN(D) + MT(D) | `gpt_analyzer.py:5082` + `scheduler.py:5677-5681` | ✅ PASS |
| C5 | ML cross-region momentum draw-order guard | `meta_data_collector.py:231-254` (V10671) | ✅ PASS |
| C6 | mined_rules same-day matrix hợp lệ | DB live: MN→MT n=4, MN→MB n=6, MT→MB n=3, 0 vi phạm chiều ngược | ✅ PASS |
| C7 | mined_rules self-D = invalid | 0 self-D rows | ✅ PASS |
| C8 | Verified KHÔNG shift D thành D-1 | `final_bundles.date` + `verified_at` separate; `daily_evaluation.py:113-141` không re-label | ✅ PASS |
| C9 | Preview state machine 4 states + VERIFIED | `main.py:3755-3819` `/api/mined-rules/preview-state` | ✅ PASS |
| C10 | KPI verified-only | `daily_evaluation.py:113-141` JOIN day_governance | ✅ PASS |
| C11 | `context_integrity` tag | 03/06 live: MN auto_daily=`provisional`; MT/MB rerun_post_*=`clean` | ✅ PASS |
| C12 | `day_governance` per-region lifecycle | 14-col schema; 03/06 MN+MT VALID, MB DEGRADED (14/15) | ✅ PASS |
| C13 | Backtest walk-forward draw order | `_v10680_*lane.py` train 60d→30d, test 30d→0d non-overlap | ✅ PASS |
| C14 | `source_offset` ∈ {D, D-1} | DB DISTINCT = ['D','D-1'] only | ✅ PASS |

**14/14 PASS** — không hạng mục nào FAIL hoặc PARTIAL hoặc UNKNOWN.

---

## 3. LEAKAGE BACKTEST/EVAL — Đào sâu

### 3.1 Eval/backtest dùng `source_lag=0` (same-day) đúng order

**Code**: `mined_rule_eval.py:68-72`
```
def _get_source_date(target_date_str, source_offset):
    if source_offset == 'D-1':
        return (td - timedelta(days=1))...
    return target_date_str  # D = same day
```

Eval **không kiểm tra order trong loop** vì `mined_rules` đã được lọc sạch tại lớp mining (V10668 fix 266 violations). Mọi hàng same-day trong DB hiện tại đã hợp lệ chiều.

**Live verify**: DB query `SELECT COUNT(*) FROM mined_rules WHERE source_offset='D' AND source_region IN ('MB','MT') AND target_region='MN'` = **0** → không có dữ liệu sai chiều có thể được eval dùng.

### 3.2 Walk-forward V10693/V10694 MB (E3 bơm MN(D)/MT(D))

**`_v10693_mb_perpos_predictor.py:60,67,97`**:
```
STRUCT_REGIONS = ('MN', 'MT')
BOARD_REGIONS = ('MN', 'MT')
# L97: "Same-day MN(D)/MT(D) special-prize tails (causal: drawn before MB 18:15)."
```

- Chỉ MN+MT làm source same-day; MB không bao giờ là source cho MN/MT.
- Comment ghi rõ `causal: drawn before MB 18:15` → MN/MT xổ trước MB → an toàn.

**`_v10694_install_cron.py:14`**: cron `55 23 * * *` (23:55) — chạy SAU MB xổ 18:15 và sau settle, chỉ ghi MB-only/shadow tables.

→ **Không có khả năng MB(D)→MN(D)/MT(D) trong V10693/V10694.**

### 3.3 Count ca MB(D)→MN/MT(D) trong toàn bộ DB

**Live query trên VPS:**
| Query | Kết quả | Verdict |
|---|---|---|
| `MB(D)→MN/MT(D)` trong `mined_rules` | **0** | ✅ PASS |
| `MT(D)→MN(D)` trong `mined_rules` | **0** | ✅ PASS |
| Same-day matrix toàn bộ (MN→MT n=4, MN→MB n=6, MT→MB n=3, MB→? n=0, MT→MN n=0) | 0 vi phạm | ✅ PASS |

→ **Toàn bộ pipeline leakage = 0. Không có nhìn trộm tương lai.**

---

## 4. §36G FULL_CLOSURE 04/06 — Ngữ nghĩa + lịch verify

### 4.1 Làm rõ ngữ nghĩa (tránh hiểu nhầm)

> **FULL_CLOSURE_PASS = chu kỳ pipeline chạy đúng phase + dữ liệu sạch/non-empty.**
> **KHÔNG phải = MB đoán trúng.**

**Bằng chứng tránh hiểu nhầm — 03/06**:
- §36G C3 PASS: 7 model MB có `run_source='rerun_post_mt'` đúng phase sau MT xổ 17:30.
- §36G C4 PASS: 7 model no-token MB đều có `pre_result_numbers` non-empty + `context_integrity='clean'`.
- → **FULL_CLOSURE_PASS = TRUE**.
- Nhưng kết quả 7/7 model đều LOSE/PARTIAL (BT trượt) — chỉ 1 model PARTIAL (random-forest).
- → **PASS pipeline ≠ PASS accuracy.** Đường ống chạy đúng quy trình, nhưng predict trúng hay trượt là chuyện khác.

### 4.2 Kế hoạch verify tự động (không cần owner action)

| Mốc | Việc | SQL READ-ONLY |
|---|---|---|
| **17:45 hôm nay** | Verify §36G C3 cho 04/06 | `SELECT target_region, run_source, COUNT(*), context_integrity FROM predictions WHERE date='2026-06-04' AND target_region='MB' AND run_source='rerun_post_mt' GROUP BY 1,2,4` |
| **18:35 hôm nay** | Verify §36G C4 cho 04/06 | `SELECT ai_model, main_numbers, pre_result_numbers, context_integrity FROM predictions WHERE date='2026-06-04' AND target_region='MB' AND ai_model IN (7 no-token models)` |
| **18:40 hôm nay** | Tuyên bố FULL_CLOSURE_PASS hay PARTIAL_READY cho 04/06 + push V10697.1 public | (báo cáo bổ sung) |

---

## 5. BẢNG ĐỀ XUẤT XỬ LÝ TỔNG HỢP

| # | Việc | Phương án an toàn nhất | Rủi ro | File/dòng | Rollback | Owner cần OK (Y/N)? | Thứ tự |
|---|---|---|---|---|---|---|---|
| 1 | F1 mốc giờ 16:38→16:36 | **Gộp vào lần sửa main.py kế tiếp** (StrReplace từng dòng, không upload đè) | Thấp nếu gộp; Trung nếu sửa lẻ | `main.py` 7 dòng + `gpt_analyzer.py` 1 dòng | git revert + restart | **Y** — chọn A/B/C | Khi nào batch khác có việc đụng main.py |
| 2 | Verify §36G C3 cho 04/06 | Em tự chạy SQL READ-ONLY 17:45 | 0 | 0 | N/A | N (auto) | Hôm nay 17:45 |
| 3 | Verify §36G C4 cho 04/06 | Em tự chạy SQL READ-ONLY 18:35 | 0 | 0 | N/A | N (auto) | Hôm nay 18:35 |
| 4 | Tuyên bố FULL_CLOSURE 04/06 | Em surface 18:40 public V10697.1 | 0 | 0 | N/A | N (auto) | Hôm nay 18:40 |
| 5 | Contract matrix 14/14 | ✅ ĐÃ ĐÓNG (PASS toàn bộ) | 0 | 0 | N/A | N | (đóng) |
| 6 | Leakage scan MB(D)→MN/MT(D) | ✅ ĐÃ ĐÓNG (= 0) | 0 | 0 | N/A | N | (đóng) |
| 7 | E7 main.py 3-way | ✅ ĐÃ ĐÓNG (local=VPS=origin) | 0 | 0 | N/A | N | (đóng) |

---

## 6. CÂU HỎI CHO OWNER

Em chốt kế hoạch code tiếp theo dựa trên trả lời của anh cho 1 câu duy nhất:

> **F1 — Chọn cách xử lý mốc giờ 16:38→16:36?**
> - **A**: Sửa lẻ ngay (em deploy 7-dòng StrReplace, kèm sha256 + zero-drift check + rollback path).
> - **B**: Gộp vào batch sau (khuyến nghị — chờ lần đụng `main.py` kế tiếp).
> - **C**: Bỏ qua (cosmetic 2 phút, không ảnh hưởng accuracy).

Các việc 2-4 em tự fire (READ-ONLY) đúng mốc thời gian, không cần OK.

---

## 7. TRẠNG THÁI

`PUBLIC_SAFE` · **READ-ONLY** · official KHÔNG đụng · MN/MT **bất biến** · MB lane V10694 **không đụng** · 4 official tables hash IDENTICAL.

3-way HEAD: Local = GitHub = VPS = `94242fb`. main.py local sha256 = VPS sha256 = `c81ab73644aa8238`.
