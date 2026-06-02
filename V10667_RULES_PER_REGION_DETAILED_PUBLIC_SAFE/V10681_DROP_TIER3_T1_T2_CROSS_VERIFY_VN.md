# V10681 — Bỏ Tầng 3, dùng T1+T2 cross-verify per weekday (đính chính V10680)

> **Generated**: 2026-06-03 01:15 VN
> **Quyết định**: BỎ Tầng 3 (V10626 pre-register) khỏi cơ chế MB rule stack.
> **Trạng thái**: code-only sửa local, KHÔNG deploy code, KHÔNG đụng official.
> **Đính chính**: thay thế phần Tầng 3 trong [V10680](V10680_MB_RULE_STACK_CLARIFICATION_AND_NEXT_STEPS_VN.md). V10680 vẫn đúng cho T1/T2/gates/test-lane.

---

## 0. Vì sao bỏ Tầng 3

Owner đặt 4 câu hỏi sắc về T3 — em verify thực tế và thừa nhận T3 hiện tại không đủ chuẩn:

| Vấn đề | Bằng chứng |
|---|---|
| Quyền chốt số? | KHÔNG: 19/19 rule có `live_eligible=False`, `status=PRE_REGISTER_ONLY` |
| Trung thực thống kê? | 19/19 mang cờ `BH_FAIL_GLOBAL` + `SELECTION_BIAS_RISK` + `FORWARD_90D_INSUFFICIENT` |
| Có duplicate? | Có. `MN:TP.HCM:G1#1:P4P1` lặp 3 lần; `MN:TP.HCM:G2#2:TAIL_HEAD` lặp 2 lần |
| Có gắn weekday không? | KHÔNG. CSV không có cột `target_weekday` |
| Có cơ chế tích lũy? | KHÔNG. Số liệu là one-shot tại thời điểm đào (~21/05/2026), không rolling |
| Sample size | 12–60 ngày (vs T1: 365 ngày MRE) |

→ T3 không đáp ứng nguyên tắc cross-verify per-weekday mà MB cần.

---

## 1. Cấu trúc mới: 2 tầng cross-verify per weekday

| Tầng | ID | Nguồn | Số rule MB | Có gắn weekday? | Drive score? |
|---|---|---|---:|:---:|:---:|
| 1 | `MB-T1-DYN8W` | 35 production `mined_rules` MB-target | 35 | Có (`target_weekday`) | Có |
| 2 | `MB-T2-SOI` | V10667 + V10636-DIG/LAGS sau dedup, MB-target | 77 | Có (T2/T3/.../CN) | Không (CONFIRM) |

Cả hai tầng:
- Re-rank lại mỗi ngày
- Mỗi rule gắn cụ thể 1 thứ trong tuần
- Đối chiếu nhau cho cùng 1 thứ

### Cross-verify hoạt động thế nào

1. AI dự đoán cho thứ `wd`.
2. T1: lấy 5 rule production MB cho weekday `wd` (đã re-rank theo MB-tuned 8W) — đã cộng vào `number_scores` runtime.
3. T2: lấy top 8 rule manual MB cho cùng `wd` (CSV V10667 đã có T2/T3/T4/T5/T6/T7/CN).
4. Prompt yêu cầu AI:
   - **Đồng thuận hướng** giữa T1 & T2 → tin tưởng cao hơn cho số liên quan.
   - **Nghịch hướng** → giảm độ tự tin / cân nhắc SKIP.
   - Không double-weight: T1 đã trong score; T2 chỉ giải thích.

---

## 2. Code đã sửa local

### `web/backend/mb_rule_ranker.py`
- `run_daily_mb_rerank()` không gọi `_rerank_tier3` nữa.
- `_store_layers()` chỉ ghi `TIER2_CONFIRM` payload.
- `_rerank_tier3` và bảng `mb_t3_prereg_daily` được **giữ lại trong code/DB cho audit lịch sử**, KHÔNG xoá; chỉ không được prompt đọc.
- Log ghi rõ `T3=DROPPED_V10681`.

### `web/backend/gpt_analyzer.py`
- `_build_mb_layered_section()`: bỏ block "TẦNG 3 — WATCH". Header đổi `MB 3-TIER RULE STACK` → `MB 2-TIER RULE STACK (... weekday-bound cross-verify)`.
- `MB_EXPERT_DOCTRINE`: thay phần "3 TẦNG" bằng "CROSS-VERIFY 2 TẦNG theo từng thứ" + ghi rõ Tier-3 đã DROP.

### `web/backend/prompt_registry.py`
- `CTX-MB-1.0` bump version `MB-1.0` → `MB-1.1`. Doctrine list cập nhật cross-verify, ghi nhận drop Tier-3.

### Không đụng
- `rule_engine.py`, `scheduler.py`: không sửa thêm.
- MN/MT path: không thay đổi.
- Production tables (`predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`): không chạm.

---

## 3. Verify

| Mục | Kết quả |
|---|---|
| `py_compile` 5 file | PASS |
| ReadLints | 0 errors |
| Harness MN/MT 108 chữ ký | **108/108 IDENTICAL** sau khi sửa |
| Full verify suite | **54/54 PASS, 0 FAIL** |
| Smoke MB context pack | T1 5 rule + T2 8 rule + cross-verify note; KHÔNG còn TẦNG 3 |
| Ranker run | `tier3_count=0`, note `Tier-3 dropped (V10681)` |

---

## 4. Mặt hạn chế còn lại (trung thực)

- **T2 trend STATIC**: hit_rate/lift_pp của 77 manual rule là số gốc V10667; lifecycle suy ra từ strength + significance, không phải half-split động theo ngày như T1. → cần rolling re-measure ở pha sau.
- **T3 không xoá khỏi DB**: bảng `mb_t3_prereg_daily` còn 19 dòng lịch sử để audit; không ai đọc, không ai update. Nếu sau này có rolling re-measure đủ chuẩn (gắn weekday, tái đo mỗi tuần) thì có thể bật lại.
- **Cron MB ranker** vẫn thuộc nhánh chưa deploy. Báo cáo này không đổi điều đó.

---

## 5. Đề xuất bước tiếp theo (sau khi anh chốt)

1. AI tools đọc V10681 + V10680 (trừ phần T3 đã đính chính).
2. Lập kế hoạch shadow `/du-doan-test`:
   - `MB_RULE_STACK_T2_BHPASS_SHADOW_V1` — chỉ promote 5 BH-pass T2 drive nhẹ.
   - `MB_RULE_STACK_T2_TOP_PER_WEEKDAY_SHADOW_V1` — promote top 3-5 T2/thứ.
   - `MB_RULE_STACK_T2_MULT_030_SHADOW_V1` — toàn bộ T2 drive multiplier nhỏ.
3. Rolling re-measure 77 manual T2 hàng tuần để có lifecycle thật.
4. Forensic MB official gates (`min_bt=12`, `min_wr=26`, d_w06 override, AI LIMIT planner).
5. Owner quyết định promote/rollback dựa trên dữ liệu `/du-doan-test`.

---

## 6. Trạng thái

| Hạng mục | Status |
|---|---|
| Code deploy VPS | NO |
| Official mutation | NO |
| Public report | YES (file này) |
| Tier-3 trong runtime | DROPPED |
| Tier-3 trong DB | KEPT (audit lịch sử, không refresh) |
| MN/MT bất biến | PROVEN 108/108 |
| Full verify | 54/54 PASS |

**Bottom line**: T1 + T2 đều weekday-bound + dynamic, đủ để cross-verify per thứ. T3 hiện tại quá yếu (BH_FAIL + không weekday + không tích lũy) → bỏ là đúng. Không cần xây xiên aggregator riêng (UI đã có xiên qua `generate_final_bundle`).
