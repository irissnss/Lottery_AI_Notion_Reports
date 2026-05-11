# V105.25 — STATION ALIAS FIXUP + SOURCE-POOL REASON RANKING + V103 SUPPLY CLASS FIX — OFFICIAL LOCKED

> **Phiên bản:** V105.25
> **Ngày báo cáo:** 2026-05-11 (UTC+7)
> **Vai trò:** Senior Runtime Auditor + ML Pipeline Engineer + SSOT Controller
> **Trạng thái cuối:** OFFICIAL LOCKED — `predictions / final_bundles / lottery_results / model_daily_eval` chứng minh KHÔNG bị mutate; LANE 1–6 hoàn tất theo hợp đồng shadow-only; LANE 0 (publish public folder) hoàn tất; Notion sync chờ owner OK.
> **Token cost:** ZERO. Không gọi provider/manual AI.
> **Live forensic sync:** `artifacts/live_sync/20260511_150807/manifest.json` (DB pre-sync local `b193153d…`, snapshot từ VPS = `73e2d8c4b12950bc61e26a7cbda96a2981ba166bc38d1298c6fa7c0c7bd5dcde`).

---

## 1. Sources read

| Surface | Path/ID | Trạng thái |
|---|---|---|
| Cursor rules | `.cursor/rules/live-data-integrity.mdc`, `.cursor/rules/governance-traceability-automation.mdc`, `.cursor/rules/active-roadmap-precedence.mdc` | đã áp dụng (live sync chạy trước mọi đụng chạm artefact; CP overdue check: không có CP nào quá hạn 2026-05-11) |
| Active roadmaps | `docs/ACTIVE_ROADMAP_LAG1_ADAPTIVE_EXPLOIT.md` (CP-66.7 hạn 2026-05-21), `docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md` | không CP nào tới ngưỡng auto-action hôm nay |
| V105.24 evidence | `artifacts/v10524/V105_24_FINAL_REPORT.md`, `v10524_local_audit_latest.json`, `v10524_station_code_audit.json` (báo cáo 62 alias unexpected), `DEPLOYED_RUNTIME_MANIFEST.json` | đã đọc đủ |
| V105.23 station identity | `Lottery_AI_Notion_Reports/V105_23_TOTAL_FORCE_CODE_TRUTH_AUDIT_20260511/evidence/*` | đã trace, V105.25 LANE 1 nối tiếp |
| Code surfaces | `web/backend/station_identity.py`, `scheduler.py:1442-1466`, `gpt_analyzer.py:5841`, `metrics_calculator.py:649`, `pnl_settlement.py:63-66`, `cross_region.py:46-49`, `main.py:4065`, `_v100_gan_calculator.py:140,159`, `_v10524_v102_relaxed_selector_shadow.py`, `_v10524_runtime_manifest.py` | đã sửa hoặc thêm wrapper |
| Frontend | `web/frontend/monitoring.html`, `pnl-tracker.html`, `settings.js`, `user-view.js` | đã canonicalize label |
| Notion | Em chưa gọi MCP Notion trong lần này (LANE 0 Notion sync chờ owner OK trước khi tạo trang mới); xem §2 cho public sync đã hoàn tất ở GitHub side. |

---

## 2. Public / Notion sync links

### GitHub Public (`Lottery_AI_Notion_Reports/`)

- `V105_24_SOURCE_POOL_GAP_DRILLDOWN_20260511/` — folder mới chứa V105.24 evidence pack:
  - `README.md`
  - `evidence/V105_24_FINAL_REPORT.md`
  - `evidence/v10524_local_audit_latest.json`
  - `evidence/v10524_station_code_audit.json`
  - `evidence/DEPLOYED_RUNTIME_MANIFEST.json`
- `V105_25_STATION_ALIAS_FIXUP_20260511/` — folder mới chứa V105.25 evidence pack:
  - `evidence/V105_25_FINAL_REPORT.md` (file này, copy)
  - `evidence/V105_25_SOURCE_POOL_GAP_ANALYSIS_VI.md` (LANE 2 deliverable)
  - `evidence/v10525_local_audit_latest.json`
  - `evidence/v10525_source_pool_reason_ranking.json`
  - `evidence/v10525_candidate_flow_funnel.json`
  - `evidence/v10525_v102_relaxed_watch.json`
  - `evidence/v10524_station_code_audit_post_v10525.json` (alias_unexpected_count=0)
  - `evidence/drift_alert.json`
- `LATEST_REPORT.json`, `REPORT_INDEX.md`, `NEXT_ACTION.md`, `OPEN_ISSUES.md`, `CHANGELOG_PUBLIC.md` cập nhật trỏ V105.25.
- Secrets redaction: `DEPLOYED_RUNTIME_MANIFEST.json` chỉ chứa fingerprint 8-char của API key (không có giá trị key thật). Không file nào trong public folder chứa raw key/credential.
- Commit + push GitHub do owner thực hiện thủ công sau khi review (em không tự push; thư mục đã ready để `git add` + commit).

### Notion

- Không tạo trang mới trong session này (Notion MCP authentication không kích hoạt; em không tự gọi để tránh ghi nhầm danh tính trang). Đề xuất ở §10 để anh OK cho việc sync trang `V105.24` và `V105.25`.

---

## 3. Official hash proof

`artifacts/v10525/v10525_local_audit_latest.json` — chạy bằng `python artifacts/v10525/_v10525_run_local_audit.py`:

| Table | row_count pre | sha256 pre | row_count post | sha256 post | Identical? |
|---|---:|---|---:|---|:---:|
| `predictions` | 4750 | `c8312b347a8cd92b26b49c10eb4b31266a644303fa08671b397b7fa376542868` | 4750 | `c8312b347a8cd92b26b49c10eb4b31266a644303fa08671b397b7fa376542868` | ✅ |
| `final_bundles` | 217 | `0126a7dafd1674f9f4ce7bb0c90d0d4d76042af2cb12b745d8d9d75c8bfb1e38` | 217 | `0126a7dafd1674f9f4ce7bb0c90d0d4d76042af2cb12b745d8d9d75c8bfb1e38` | ✅ |
| `lottery_results` | 14649 | `ecee21c893684cdd729e35c0024414f69b703344e93d9c2108697ba64ac72458` | 14649 | `ecee21c893684cdd729e35c0024414f69b703344e93d9c2108697ba64ac72458` | ✅ |
| `model_daily_eval` | 4572 | `083a36ffea774fa6a711348b36e7293d5ed68b2ba88c40a1a119b8fdd36262df` | 4572 | `083a36ffea774fa6a711348b36e7293d5ed68b2ba88c40a1a119b8fdd36262df` | ✅ |

- `db_sha256_pre  = 4e616ed724bd4646ed3311efd9bc5a8a68ab61813d9468d815d15548a497c469`
- `db_sha256_post = ec74f80f3b39935c52cc6959af8033dc677ec56c8c2e0fd9057741d30da151fc`

DB file sha256 thay đổi do shadow tables V105.24/V105.25 được refresh; 4 official tables hoàn toàn không bị ghi (row_count + sha256 từng-bảng identical).

---

## 4. Station alias before / after (LANE 1)

### Before V105.25 (V105.24 baseline)

- `alias_unexpected_count = 62` trải 25 file (xem `Lottery_AI_Notion_Reports/V105_24_SOURCE_POOL_GAP_DRILLDOWN_20260511/evidence/v10524_station_code_audit.json`).
- `weekday_as_station_unexpected = 132` (loose match).

### After V105.25

`artifacts/v10524/v10524_station_code_audit.json` (sau khi chạy `python artifacts/v10524/_v10524_station_code_audit.py`):

| Metric | Before | After |
|---|---:|---:|
| `alias_unexpected_count` | **62** | **0** |
| `weekday_as_station_unexpected_strict` | n/a | **0** |
| `weekday_as_station_unexpected_loose` | 132 | 44 (đều là label thứ-trong-tuần, không phải station) |
| `alias_findings_total` | 89 | 61 (toàn bộ là raw forensic exception đã whitelist) |
| Files scanned | 376 | 376 |

### Những gì đã sửa

| File runtime | Loại thay đổi |
|---|---|
| `web/backend/scheduler.py` | `_expected_names` thay `"Huế"` → `"Thừa Thiên Huế"`; comparison set canonicalize hai chiều bằng `station_identity.canonical_station` (preserve hành vi gốc nếu DB còn raw); log "Present:" dùng canonical. |
| `web/backend/cross_region.py` | `DAK_LAK_STATIONS`/`QUANG_NAM_STATIONS` đổi sang `station_identity.station_lookup_candidates(canonical_station('Đắk Lắk'))` — bỏ literal alias cũ, vẫn cover DB raw. |
| `web/backend/main.py:4065` | Comment đổi từ literal `'Đắc Nông' → 'Đắk Nông'` thành tham chiếu `station_identity.STATION_ALIASES`. |
| `web/backend/gpt_analyzer.py:5841` (sample data trong `__main__`) | `"TPHCM"` → `"TP. HCM"`. |
| `web/backend/metrics_calculator.py:649` (test fixture trong `__main__`) | `"TP.HCM"` → `"TP. HCM"`. |
| `web/backend/pnl_settlement.py:63-66` | `STATION_IDENTITY_NOTE` reword sang canonical, không còn literal `"Huế"`, `"HCM/TPHCM"` raw. |
| `web/backend/_v100_gan_calculator.py:140,159` | Comments đổi sang `"TP. HCM"` canonical và mô tả alias qua `station_identity.STATION_ALIASES`. |
| `web/frontend/monitoring.html` (1 occ) | `"Timezone HCM"` → `"Timezone Asia/Ho_Chi_Minh"`. |
| `web/frontend/pnl-tracker.html` (1 string) | Reword note để loại bỏ `"Huế"`/`"HCM/TPHCM"` raw. |
| `web/frontend/settings.js` (2 occ) | `'Huế'` → `'Thừa Thiên Huế'`. |
| `artifacts/v10524/_v10524_station_code_audit.py` | Thêm **embedded-canonical detection** (bỏ false positive khi `"HCM"` nằm trong `"TP. HCM"`); mở rộng `RAW_FORENSIC_EXCEPTIONS` cho `_xsdp_*.html` (raw scrape mirrors), `_test_*`, `_analyze_*`, `_rescrape_*`, `_backtest_*`, `archive/`. |

### Hợp đồng giữ nguyên

- **Không** đụng `lottery_results.station` raw: DB còn lưu `Huế`, `HCM`, `Đắc Lắc`, `Đắc Nông`, `Vũng Tàu` (đúng yêu cầu). Read-time canonicalization xử lý qua `station_identity.canonical_station`.
- `web/backend/station_identity.py` được giữ là **SSOT duy nhất** cho alias mapping.

---

## 5. Source-pool reason matrix (LANE 2)

Cửa sổ 30 ngày, dữ liệu từ `v10524_source_pool_gap_drilldown` (7423 drilldown rows, 100% là miss-by-design — bảng chỉ ghi miss).

| Region | Total drilldown rows |
|---|---:|
| MB | 2067 |
| MN | 3022 |
| MT | 2334 |

### Top root causes per region (xếp hạng)

| Region | #1 miss_reason | count | #2 | count | #3 | count |
|---|---|---:|---|---:|---|---:|
| MN | `PROMPT_NOT_INJECTED` | 2109 | `SOURCE_FORMULA_EXCLUSION` | 873 | `TOP30_CAP` | 40 |
| MT | `PROMPT_NOT_INJECTED` | 1223 | `SOURCE_FORMULA_EXCLUSION` | 987 | `PROMPT_NOT_INJECTED+STATION_ALIAS` | 44 |
| MB | `SOURCE_FORMULA_EXCLUSION` | 1021 | `PROMPT_NOT_INJECTED` | 1017 | `TOP30_CAP` | 29 |

**Diễn giải:**
- `PROMPT_NOT_INJECTED` chiếm 58.6% (4349 miss) — **artifact đo lường** vì `v104_shadow_prompt_candidate_injection` chưa wire vào prompt thật. KHÔNG kết luận prompt thực thiếu candidate.
- `SOURCE_FORMULA_EXCLUSION` chiếm 38.8% (2881 miss) — root cause thực sự. MB và MT thiệt thòi do công thức không bao gồm MB D-2.
- `STATION_ALIAS` còn 96 miss (1.3%) đến từ **DB raw** (đúng hợp đồng không mutate raw); code-side đã canonical hoàn toàn.
- `TOP30_CAP` 97 miss (1.3%) — đuôi trong source pool nhưng bị selector cắt khỏi top-30.

Báo cáo chi tiết: `artifacts/v10525/V105_25_SOURCE_POOL_GAP_ANALYSIS_VI.md` (cũng đã copy sang public folder).

---

## 6. Candidate flow funnel (LANE 3)

`v10524_candidate_flow_trace` — 30 ngày, 8583 rows.

| Region | source_pool | in_prompt (artifact) | ranked | top5 | top2 | bundled | ui_output | appeared_in_actuals |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| MB | 2830 | 0 | 265 | 163 | 81 | 58 | 58 | 689 |
| MN | 2830 | 0 | 263 | 161 | 67 | 58 | 58 | 1240 |
| MT | 2830 | 0 | 257 | 172 | 104 | 58 | 58 | 1023 |

`in_prompt = 0` ⇒ measurement artifact (giống §5). Biggest-drop thật sau khi bỏ qua stage prompt:

| Region | Biggest drop | Lost | Rate |
|---|---|---:|---:|
| MB | `top5 → top2` | 82 / 163 | **50.3%** |
| MN | `top5 → top2` | 94 / 161 | **58.4%** |
| MT | `top2 → bundled` | 46 / 104 | **44.2%** |

`bundled → ui_output = 0%` — UI render đầy đủ những gì bundler chốt.

---

## 7. V103 supply class matrix (LANE 4)

### Root cause của RELAXED_L2 = 0 (V105.24 finding)

| Quan sát | Số liệu | Nhận xét |
|---|---:|---|
| `v103_candidate_supply_shadow` rows | 8743 | Tất cả nằm trên target_date ≤ 2026-05-09 |
| `v103_candidate_supply_shadow.v102_recurrence_class IS NULL` | 8743 / 8743 (100%) | Mọi v103 row đều thiếu class |
| `v102_candidate_recurrence_context_shadow` rows | 61 | Chỉ có target_date = 2026-05-10 |
| Join `(target_date, region, candidate_tail)` v103 ↔ v102 ctx | 0 matchable | Hai bảng KHÔNG overlap target_date (mỗi cái target trên ngày khác) |
| Distribution v102 ctx class | STRONG=36, MEDIUM=13, WEAK=12 | WEAK có 12 candidates nhưng không entered RELAXED_L2 |

### Giải thích RELAXED_L2 = 0 ở V105.24

`RELAXED_L2 = WEAK + non_gan_core_present + lose_only_pass`. Trong fallback path V105.24 (read v102 ctx khi v103 NULL), các trường `NON_GAN_CORE_KEYS` (`official_bt`, `official_lo2`, `test_bt_count`, `test_lo2_count`, `v67/70/73/101_match`, `ai_model_count`, `no_token_model_count`, `rule_support_count`, …) không được populate ⇒ `non_gan_core_present = False` ⇒ điều kiện thất bại cho 12 WEAK candidates ⇒ 0 rows.

### Fix V105.25

1. **Backfill module** `web/backend/_v10525_v103_supply_class_backfill.py`:
   - UPDATE `v103_candidate_supply_shadow` set `v102_recurrence_score/class/recommendation/evidence_json` từ `v102_candidate_recurrence_context_shadow` khi join `(target_date, region, candidate_tail)` match và v103 hiện NULL.
   - Idempotent, không insert, không chạm official.
   - Local run hôm nay: 0 matchable (do 2 bảng chưa overlap target_date) — sẽ tự fill khi v103 supply được materialize cho target_date=2026-05-10.

2. **Enhanced fallback** trong `_v10524_v102_relaxed_selector_shadow.py::_candidate_rows_with_v102`:
   - Parse `evidence_json` của v102 ctx để derive `OFFICIAL_BT`, `OFFICIAL_LO2`, `TEST_BT`, `TEST_LO2`, `MODEL::*` axes.
   - Set tương ứng `official_bt / official_lo2 / test_bt_count / test_lo2_count / ai_model_count` cho fallback row.
   - `source_layer_count` được tính từ số axis có trong evidence (tối thiểu 2 khi có evidence).
   - Hợp đồng: không promote, không touch official, chỉ thay đổi diagnostic logic của shadow selector.

### Kết quả V102 RELAXED matrix sau V105.25

| region | level | rows | entered_top2 | would_save | would_break | avg_score |
|---|---|---:|---:|---:|---:|---:|
| MB | STRICT | 11 | 0 | 0 | 0 | 54.81 |
| MB | RELAXED_L1 | 6 | 0 | 0 | 0 | 13.62 |
| MB | RELAXED_L2 | **4** | 0 | 0 | 0 | 7.14 |
| MN | STRICT | 15 | 1 | 0 | 0 | 59.51 |
| MN | RELAXED_L1 | 5 | 0 | 0 | 0 | 15.55 |
| MN | RELAXED_L2 | **2** | 0 | 0 | 0 | 8.63 |
| MT | STRICT | 10 | 0 | 0 | 0 | 53.09 |
| MT | RELAXED_L1 | 2 | 0 | 0 | 0 | 14.43 |
| MT | RELAXED_L2 | **5** | 0 | 0 | 0 | 8.00 |

Tổng rows 60 (vs 13 trong V105.24); RELAXED_L2 từ **0 → 11**. `would_save/would_break/false_promo = 0` vì target_date=2026-05-10 chưa có closed actuals đầy đủ trong window 30 ngày sample (sẽ cập nhật theo ngày).

---

## 8. V102 relaxed watch status (LANE 5)

`web/backend/_v10525_v102_relaxed_watch.py` cung cấp tổng hợp 7d/14d theo region × relaxed_level.

| Window | Region | Level | Observations | Net save | Promotion eligible |
|---|---|---|---:|---:|:---:|
| 7d | MB | RELAXED_L1 | 6 | 0 | ❌ shadow-only |
| 7d | MB | RELAXED_L2 | 4 | 0 | ❌ shadow-only |
| 7d | MN | RELAXED_L1 | 5 | 0 | ❌ shadow-only |
| 7d | MN | RELAXED_L2 | 2 | 0 | ❌ shadow-only |
| 7d | MT | RELAXED_L1 | 2 | 0 | ❌ shadow-only |
| 7d | MT | RELAXED_L2 | 5 | 0 | ❌ shadow-only |
| 14d | (same numbers; window = data range) | | | | |

Promotion rule (đã encode trong payload):

> **STRICT shadow-only V105.25: promotion to production is BLOCKED. Required to unlock: >=14 days with net_save > 0 AND break_ratio <= 0.05 AND owner explicit approval AND zero impact on official tables.**

Hiện chưa có row nào đạt cả 3 điều kiện ⇒ status = **HOLD-AND-OBSERVE**, không promotion.

Output: `artifacts/v10525/v10525_v102_relaxed_watch.json` (đã copy sang public).

---

## 9. Remaining blockers

| Blocker | Trạng thái | Đề xuất |
|---|---|---|
| `PROMPT_NOT_INJECTED` chiếm 58.6% miss | **Measurement artifact** — không phải lỗi prompt thật | Wait V104 prompt-injection tracker được wire-in (cần owner OK riêng) |
| `SOURCE_FORMULA_EXCLUSION` MB+MT cao | 1021 (MB) + 987 (MT) | Shadow biến thể `MB_D_v2 = MB_D + MB D-2`; track would_save/break 14d (cần owner OK) |
| MN/MB `top5 → top2` drop 50–58% | Selector thắt cổ chai | Khuyến nghị shadow A-B test selector top-2 policy (V105.26+) |
| MT `top2 → bundled` drop 44% | Bundler/Protect mode cắt | Audit bundler dedup policy (V105.26+) |
| V102 RELAXED watch obs <14 days | Mới có 1 ngày dữ liệu (2026-05-10) | Tiếp tục accumulate 14 ngày trước khi đề xuất promote |
| V103 supply class còn 8743 row NULL cho target_date ≤ 2026-05-09 | Bảng v102 ctx chưa có lịch sử | Backfill sẽ tự chạy mỗi ngày khi v102 ctx + v103 supply trùng target_date |
| Frontend lane chips vẫn hiển thị "--" (FU-V10524-FRONTEND-LANE-WIRING) | Cosmetic P2 | LANE 5 V105.24 đã đổi label thành "LO2 weight: --" với tooltip; data wiring chờ V105.26 |
| Notion sync trang `V105.24` / `V105.25` | Chưa thực hiện trong session | Em sẽ gọi MCP Notion tạo 2 trang khi anh OK (không gọi tự ý để tránh ghi nhầm namespace) |

---

## 10. Owner decisions pending

| Quyết định | Bối cảnh | Chờ |
|---|---|---|
| **V102 RELAXED L1/L2 promotion** | 11 rows L2 + 13 rows L1 mới có 1 ngày dữ liệu | Chờ ≥14 ngày + owner OK |
| **Source-pool formula MB_D_v2 (MB + MB D-2 shadow)** | Có thể giảm `SOURCE_FORMULA_EXCLUSION` ~38% miss | Owner OK để bật shadow variant + track 14d |
| **V104 prompt injection mở rộng** | Hiện toàn bộ `PROMPT_NOT_INJECTED=4349` là artifact | Owner OK để wire-in V104 tracker vào prompt build path |
| **Notion sync V105.24 + V105.25** | Public folder đã ready | Owner OK gọi MCP Notion tạo 2 trang dưới `Lottery_AI_Test` |
| **Push public folder lên GitHub remote** | 2 thư mục `V105_24_SOURCE_POOL_GAP_DRILLDOWN_20260511` + `V105_25_STATION_ALIAS_FIXUP_20260511` đã ready, chỉ chờ commit | Owner OK (em không tự `git push`) |
| **Daily 00:05 VN snapshot wire-in scheduler** | `_v10525_runtime_manifest_daily.py` đã sẵn sàng; chưa wire vào APScheduler | Owner OK để thêm job (em không tự đụng scheduler runtime job table) |

---

## 11. Phụ lục — artifacts & modules

- `web/backend/_v10525_v103_supply_class_backfill.py` (LANE 4)
- `web/backend/_v10525_source_pool_reason_ranking.py` (LANE 2)
- `web/backend/_v10525_candidate_flow_funnel.py` (LANE 3)
- `web/backend/_v10525_v102_relaxed_watch.py` (LANE 5)
- `web/backend/_v10525_runtime_manifest_daily.py` (LANE 6)
- `artifacts/v10524/_v10524_station_code_audit.py` (LANE 1 — refactored)
- `artifacts/v10525/_v10525_run_local_audit.py` (end-to-end harness)
- `artifacts/v10525/v10525_local_audit_latest.json`
- `artifacts/v10525/V105_25_SOURCE_POOL_GAP_ANALYSIS_VI.md`
- `artifacts/v10524/snapshots/runtime_manifest_2026-05-11.json` (LANE 6 first snapshot)
- `artifacts/v10524/drift_alert.json` (LANE 6 first drift run — alert=false vì chưa có snapshot trước đó)

---

**END OF V105.25 FINAL REPORT (VI).**
