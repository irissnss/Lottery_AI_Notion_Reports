# V105.25 — Source-Pool Gap Analysis (VI)

Phiên bản: 2026-05-11 VN
Phạm vi cửa sổ: 30 ngày gần nhất, target_date kết thúc 2026-05-11.
Nguồn dữ liệu: `v10524_source_pool_gap_drilldown` + `v10524_candidate_flow_trace` (shadow tables, sinh ra local từ DB live đã sync VPS lúc 2026-05-11T15:08 VN).
Tính chất: **shadow-only**, không gọi provider/model, không ghi vào `predictions / final_bundles / lottery_results / model_daily_eval`.

---

## 1. Cấu trúc dữ liệu

`v10524_source_pool_gap_drilldown` ghi 1 dòng cho mỗi `(target_date, region, weekday, station_raw, station_canonical, actual_tail, source_prize, source_formula_stage)`. Đây là quan sát hậu kiểm: mỗi `actual_tail` (số thật sự xổ về) được trace ngược qua các tầng của pipeline:

1. `source_available` — nguồn dữ liệu cần thiết có sẵn ở D-1 / D-2 hay không.
2. `source_result_complete` — bộ kết quả nguồn đầy đủ hay bị thiếu.
3. `in_source_pool` — đuôi thuộc source pool theo công thức MN/MT/MB.
4. `in_prompt` — đuôi có được V104 shadow prompt-injection tracker ghi nhận hay không.
5. `ranked` — đuôi xuất hiện trong `experimental_preview_shadow.candidate_ranked_json`.
6. `top5` / `top2` — vị trí trong ranking shadow.
7. `bundled` — đuôi vào `final_bundles`.
8. `ui_output` — đuôi xuất hiện trong UI cuối.

`miss_reason` cô đặc tổ hợp các phép kiểm tra trên thành một nhãn root-cause duy nhất.

---

## 2. Tổng quan miss

| Region | Drilldown rows (toàn miss) | Miss rate |
| --- | --- | --- |
| MB | 2067 | 100% |
| MN | 3022 | 100% |
| MT | 2334 | 100% |
| **Tổng** | **7423** | **100%** |

Lưu ý: `v10524_source_pool_gap_drilldown` chỉ ghi miss, không ghi HIT — vì vậy `miss_rate = 1.0` là tính chất schema, không phải kết quả thật của pipeline. Số tuyệt đối các miss là chỉ số quan trọng.

---

## 3. Xếp hạng root-cause theo region

### MN
| Hạng | miss_reason | Số miss |
| --- | --- | --- |
| 1 | `PROMPT_NOT_INJECTED` | 2109 |
| 2 | `SOURCE_FORMULA_EXCLUSION` | 873 |
| 3 | `TOP30_CAP` | 40 |

### MT
| Hạng | miss_reason | Số miss |
| --- | --- | --- |
| 1 | `PROMPT_NOT_INJECTED` | 1223 |
| 2 | `SOURCE_FORMULA_EXCLUSION` | 987 |
| 3 | `PROMPT_NOT_INJECTED+STATION_ALIAS` | 44 |
| 4 | `SOURCE_FORMULA_EXCLUSION+STATION_ALIAS` | 36 |
| 5 | `TOP30_CAP` | 28 |
| 6 | `TOP30_CAP+STATION_ALIAS` | 16 |

### MB
| Hạng | miss_reason | Số miss |
| --- | --- | --- |
| 1 | `SOURCE_FORMULA_EXCLUSION` | 1021 |
| 2 | `PROMPT_NOT_INJECTED` | 1017 |
| 3 | `TOP30_CAP` | 29 |

---

## 4. Diễn giải từng root-cause

### `PROMPT_NOT_INJECTED` (4349 miss — chiếm 58.6%)
- Định nghĩa: `actual_tail` có mặt trong `in_source_pool` nhưng KHÔNG nằm trong tập `v104_shadow_prompt_candidate_injection` của ngày đó.
- Bản chất hiện tại: `v104_shadow_prompt_candidate_injection` là bảng shadow để nghiên cứu, chưa được runtime ghi nhận tự động cho prompt thật → mọi `actual_tail` đều bị đếm là không injected. Đây là **giới hạn đo lường (measurement artifact)**, KHÔNG phải là lỗi prompt thật.
- Khi đánh giá pipeline thật, cần coi nhãn này là "không có bằng chứng injection" thay vì "prompt thiếu candidate". Mức độ thật chỉ có thể đo sau khi V104 được wire-in (hiện vẫn đợi owner approval).

### `SOURCE_FORMULA_EXCLUSION` (2881 miss — chiếm 38.8%)
- Định nghĩa: `actual_tail` không có trong `in_source_pool` vì source-formula đang dùng (`MN_D / MT_D / MB_D`) không khai thác station/prize chứa đuôi đó tại D-1/D-2.
- Vị trí xuất hiện cao nhất ở **MB** (1021) và **MT** (987 + 36 alias). Đặc trưng MB cao là do công thức `MB_D = (MN+MT+MB) D-1 + MN D + MT D` không bao gồm MB D-2 — nhiều đuôi MB chỉ xuất hiện ở MB D-2 vẫn bị bỏ.
- Phương án thử nghiệm an toàn: thêm shadow biến thể `MB_D_v2 = MB_D + MB D-2` (shadow-only, không promote) và so sánh would_save vs would_break trên 7d/14d. Đây là pending owner approval (V105.24 đã gắn cờ).

### `STATION_ALIAS` (96 miss — chiếm 1.3%, đều ở MT)
- Tổ hợp: `PROMPT_NOT_INJECTED+STATION_ALIAS=44`, `SOURCE_FORMULA_EXCLUSION+STATION_ALIAS=36`, `TOP30_CAP+STATION_ALIAS=16`.
- Sau LANE 1 (V105.25 station alias fixup), `alias_unexpected_count` toàn workspace = 0 ⇒ các `STATION_ALIAS` còn lại là do **DB raw** (lottery_results.station) còn lưu `Huế`, `HCM`, `Đắc Lắc`, `Đắc Nông` (đúng hợp đồng — không mutate raw). Khi station_identity.canonical_station được dùng đầy đủ ở read-time, các nhãn alias trong drilldown sẽ tự co lại sau lần materialize tiếp theo.

### `TOP30_CAP` (97 miss — chiếm 1.3%)
- Định nghĩa: `actual_tail` thuộc source pool, nhưng không vào ranked top-30 của adaptive selector ⇒ bị cắt trước khi vào top5.
- Đây là dạng "đã có dữ liệu, nhưng selector ưu tiên đuôi khác". Có thể là cơ hội cho meta/V67-V101 boost. Theo dõi qua `v10524_v102_relaxed_selector_shadow` (LANE 4 V105.25).

---

## 5. Top stations bị miss nhiều nhất

Tổng hợp `region × station_canonical` (HIT loại bỏ), trích 10 station có miss cao nhất mỗi region:

(Xem chi tiết tại `artifacts/v10525/v10525_source_pool_reason_ranking.json` — phần `top_station_root_causes`.)

Lưu ý: nhiều miss tập trung ở các đài có vòng đời thưa (D-2 mới xuất hiện) hoặc đài có alias raw cũ trong DB. Không có station nào có miss bất thường do alias mismatch trong CODE — toàn bộ alias trong code đã được canonicalize (xem `v10524_station_code_audit.json`, `alias_unexpected_count = 0`).

---

## 6. Candidate flow funnel — LANE 3 V105.25

Từ `v10524_candidate_flow_trace`, conversion theo region (cửa sổ 30 ngày):

| Region | source_pool | in_prompt | ranked | top5 | top2 | bundled | ui_output |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MB | 2830 | 0 | 265 | 163 | 81 | 58 | 58 |
| MN | 2830 | 0 | 263 | 161 | 67 | 58 | 58 |
| MT | 2830 | 0 | 257 | 172 | 104 | 58 | 58 |

- `in_prompt = 0` ⇒ measurement artifact (giống mục 4, V104 shadow chưa wire). Bỏ qua bước này khi xác định biggest-drop thật.
- Drop thực theo region (sau khi bỏ qua stage `prompt`):

| Region | source_pool → ranked | ranked → top5 | top5 → top2 | top2 → bundled | bundled → ui_output |
| --- | --- | --- | --- | --- | --- |
| MB | -90.6% | -38.5% | -50.3% | -28.4% | 0% |
| MN | -90.7% | -38.8% | -58.4% | -13.4% | 0% |
| MT | -90.9% | -33.1% | -39.5% | -44.2% | 0% |

**Biggest-drop thật theo region** (loại bỏ measurement artifact):

| Region | Biggest drop | Số bị mất | Tỷ lệ |
| --- | --- | --- | --- |
| MB | `top5 → top2` | 82 / 163 | 50.3% |
| MN | `top5 → top2` | 94 / 161 | 58.4% |
| MT | `top2 → bundled` | 46 / 104 | 44.2% |

- MN và MB: thắt cổ chai ở giai đoạn rút ngắn top5 → top2 (selector top-2 đang loại bỏ hơn 50% candidate đáng theo).
- MT: thắt cổ chai ở giai đoạn `top2 → bundled` (bundle builder bỏ 44% candidate đã vào top2). Đây là dấu hiệu của bundle dedup/policy cắt đặc thù MT (Protect mode).

`bundled → ui_output = 0%`: UI render đầy đủ những gì bundle đã chốt (không drop thêm).

---

## 7. Kết luận hành động cho V105.25

1. **Không vi phạm gì ở mức code/station**: LANE 1 fixup khẳng định `alias_unexpected_count=0`, các STATION_ALIAS miss còn lại bắt nguồn từ DB raw (đúng hợp đồng không mutate raw).
2. **Root cause #1 thực sự** = `SOURCE_FORMULA_EXCLUSION` (38.8%). MB và MT là hai region có cơ hội cao nhất nếu mở rộng nguồn (shadow only, chờ owner OK).
3. **Root cause #2 thực sự** = `top5 → top2` cho MN/MB và `top2 → bundled` cho MT — đây là điểm cần regression/A-B test trên selector + bundler ở chế độ shadow.
4. **`PROMPT_NOT_INJECTED` dominance** là artifact đo lường — không kết luận prompt sai; phải đợi V104 wire-in để có dữ liệu thật.

---

## 8. Tham chiếu

- `artifacts/v10525/v10525_source_pool_reason_ranking.json`
- `artifacts/v10525/v10525_candidate_flow_funnel.json`
- `artifacts/v10524/v10524_station_code_audit.json` (alias_unexpected_count=0 sau LANE 1)
- `artifacts/v10524/V105_24_FINAL_REPORT.md` (bối cảnh các shadow tables)
- `web/backend/_v10525_source_pool_reason_ranking.py`
- `web/backend/_v10525_candidate_flow_funnel.py`
- `web/backend/_v10524_source_pool_gap_drilldown.py`
- `web/backend/_v10525_v103_supply_class_backfill.py` (LANE 4 V105.25)
- `web/backend/_v10524_v102_relaxed_selector_shadow.py` (đã thêm evidence-derived non_gan_core)
