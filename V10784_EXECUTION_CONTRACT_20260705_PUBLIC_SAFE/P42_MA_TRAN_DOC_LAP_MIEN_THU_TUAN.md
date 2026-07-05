# V10784 P4.2 — MA TRẬN ĐỘC LẬP MIỀN × THỨ × TUẦN

Ngày 05/07/2026. Phạm vi: mọi tham số chuỗi prompt → model → total → UI → /choi.
Nhãn: **GLOBAL** / **per-MIỀN** / **per-MIỀN×THỨ** / **per-TUẦN** (+ per-NGÀY nếu áp dụng).
Nguyên tắc: default kế thừa GLOBAL → per-MIỀN → per-MIỀN×THỨ; CHỈ tách khi có evidence, không tách máy móc.

## 1. LỚP PROMPT

| Tham số | Nơi ở | Nhãn hiện tại | Đánh giá |
|---|---|---|---|
| SYSTEM_PROMPT (SP-4.1) | gpt_analyzer | GLOBAL | ĐÚNG — kỷ luật TOP1-FIRST là bất biến toàn hệ |
| core_policy (CP-7.9) | gpt_analyzer | GLOBAL, có nhánh per-MIỀN bên trong (MB ceiling) | ĐÚNG — ceiling MB đã tách đúng chỗ |
| reasoning_rulebook (RR-16.4) | gpt_analyzer | GLOBAL (§24 BT North Star) | ĐÚNG |
| context_pack (CTX-16.4) | build_context_pack() | per-MIỀN (build riêng mỗi region, data trong pack per-MIỀN×THỨ) | ĐÚNG — trục canonical |
| Station calendar (V10781) | _v10781_station_calendar | per-MIỀN×THỨ | ĐÚNG — đây là trục chuẩn region+weekday |
| rules toggles (cluster/mirror/cross/…) | settings `rules` | GLOBAL | GIỮ — bật/tắt kỹ thuật phân tích, không phải tham số hiệu chỉnh |
| rule_skip_threshold / rule_confirm_threshold | settings `rules` | GLOBAL | ĐỀ XUẤT #1 (dưới) |
| rule_min_strength_for_chot_{MN,MT,MB} | settings `rules` | per-MIỀN (MB=6 strict, MN/MT=5) | ĐÚNG — đã tách sẵn với default kế thừa |
| rule_custom_prompt | settings `rules` | GLOBAL, ARCHIVE_ONLY (không inject runtime) | GIỮ — trace applied_text đã log từ V10784 P1.2 |
| Prompt V2 lane (V10781) | _v10781_prompt_v2_lane | lane-test riêng | GIỮ — không đụng official |

## 2. LỚP MODEL

| Tham số | Nơi ở | Nhãn hiện tại | Đánh giá |
|---|---|---|---|
| OUTPUT_ELIGIBLE_MODELS (15) | model_registry | GLOBAL (allowed_regions per model nhưng hiện đều 3 miền) | ĐỀ XUẤT #2 (dưới) |
| SHADOW_AUTO_EVAL_MODELS (11) | model_registry | GLOBAL + first_run_date per lane (gate V10784 P3) | ĐÚNG |
| API keys per model | env + settings ai_keys | GLOBAL | ĐÚNG — hạ tầng, không phải hiệu chỉnh |
| max_tokens per model | gpt_analyzer | GLOBAL per model | GIỮ — giới hạn kỹ thuật của model |
| Reasoning effort cohort (E3 high) | gpt_analyzer `_MODELS_REASONING_HIGH` | GLOBAL per model | GIỮ + ĐO — reasoning_tokens per miền giờ đã log (V10784 P1), đủ dữ liệu để xét per-MIỀN sau 14 ngày nếu chênh lệch rõ |
| learned_weights | get_learned_weights(region, dow) | per-MIỀN×THỨ | ĐÚNG — đã ở trục canonical |
| weight_optimizer | optimize_and_save(region) | per-MIỀN | ĐÚNG |

## 3. LỚP TOTAL / BUNDLE

| Tham số | Nơi ở | Nhãn hiện tại | Đánh giá |
|---|---|---|---|
| generate_final_bundle | scheduler | per-MIỀN×NGÀY | ĐÚNG |
| FREEZE_MARKS (15:55/16:55/17:55) | _v10782_freeze | per-MIỀN | ĐÚNG |
| T-10 single-flight cron (15:45/16:45/17:45) | scheduler | per-MIỀN | ĐÚNG |
| FREEZE_EXEMPT_TAGS (whitelist) | _v10782_freeze | GLOBAL | ĐÚNG — semantics lane không phụ thuộc miền |
| Ensemble aggregation (combo-super v.v.) | combo_super | per-MIỀN (dùng weights per region) | ĐÚNG |

## 4. LỚP UI

| Tham số | Nơi ở | Nhãn hiện tại | Đánh giá |
|---|---|---|---|
| Cards /du-doan | frontend | per-MIỀN | ĐÚNG |
| surface=official filter | API + user-view.js | GLOBAL param | ĐÚNG |
| History filters + pagination (V10784 P4.1) | index.html/app.js/user-view.js | GLOBAL (lọc theo miền là 1 chiều lọc) | ĐÚNG |
| Viewer freeze date (M7.2) | main.py | GLOBAL | GIỮ |

## 5. LỚP /CHOI (QUẢN LÝ VỐN)

| Tham số | Nơi ở | Nhãn hiện tại | Đánh giá |
|---|---|---|---|
| Method lock | money_board_lock (region, week_start) | per-MIỀN×TUẦN | ĐÚNG — trục chuẩn của method |
| Daily số lock (songthu/BT) | money_board_daily_lock (date, region) | per-MIỀN×NGÀY | ĐÚNG |
| Risk adjust theo thứ (hạ verdict/nửa vốn/nghỉ) | _v10759_money_board | per-MIỀN×THỨ (downside-only) | ĐÚNG — thiết kế chủ đích |
| Method per-(miền×thứ)? | — | KHÔNG tách | ĐÚNG THEO EVIDENCE — train/test V10759: per-weekday method OVERFIT (MN region-level +18.9M vs per-weekday +5.4M out-of-sample). Method giữ region-level; linh hoạt theo thứ CHỈ ở lớp rủi ro |
| Retired methods gate | _v10759 `_retired_methods` theo week_start | per-TUẦN | ĐÚNG |

## 6. ĐỀ XUẤT TÁCH (chờ chữ ký owner — KHÔNG tự áp)

**ĐX-1. `rule_skip_threshold` / `rule_confirm_threshold`: GLOBAL → per-MIỀN (default kế thừa GLOBAL).**
- Evidence: `rule_min_strength_for_chot` đã phải tách per-MIỀN từ trước (MB=6 strict hơn) — chứng tỏ ngưỡng strength có phân phối khác nhau theo miền; skip/confirm threshold cùng họ tham số nhưng còn GLOBAL → không nhất quán.
- Cách làm an toàn: thêm key `rule_skip_threshold_MB` v.v., đọc per-MIỀN nếu có, fallback GLOBAL. Zero thay đổi hành vi cho tới khi owner chỉnh giá trị.
- Rủi ro nếu không tách: chỉnh ngưỡng cho MB kéo theo MN/MT.

**ĐX-2. OUTPUT_ELIGIBLE per model: GLOBAL → per-MIỀN (dùng field `allowed_regions` sẵn có).**
- Evidence sơ bộ: `model_daily_eval` per region cho thấy hiệu năng model phân hóa theo miền (bucket region+weekday là trục đọc chuẩn theo .cursorrules). Registry ĐÃ có field `allowed_regions` — hạ tầng tách có sẵn, hiện chưa dùng để phân hóa.
- Điều kiện: cần bảng đo 14 ngày per model×miền trước khi rút model khỏi miền nào (tránh phản ứng theo nhiễu). KHÔNG áp trước khi có evidence + chữ ký.

**ĐX-3. Reasoning effort: GIỮ GLOBAL, đo thêm 14 ngày.**
- V10784 P1 đã ghi `reasoning_tokens` per prediction row → sau 14 ngày có phân phối reasoning per model×miền×thứ. Nếu model X reasoning gấp 3 ở MB mà accuracy không hơn → xét hạ effort per-MIỀN. Chưa đủ evidence để tách bây giờ.

**Không đề xuất tách:** method /choi per-thứ (evidence chống — overfit), rules toggles per miền (kỹ thuật phân tích chung), API keys/max_tokens (hạ tầng).

## 7. KẾT LUẬN

Chuỗi hiện tại đã đứng đúng trục canonical `region + weekday (+ station-set)` ở các điểm quan trọng nhất (context pack, station calendar, learned weights, method lock, risk adjust). 3 đề xuất trên là các điểm GLOBAL còn sót — cả 3 đều theo mô hình "tách key, default kế thừa, zero behavior change cho tới khi owner chỉnh" — gom vào bảng chờ ký ở báo cáo tổng V10784.
