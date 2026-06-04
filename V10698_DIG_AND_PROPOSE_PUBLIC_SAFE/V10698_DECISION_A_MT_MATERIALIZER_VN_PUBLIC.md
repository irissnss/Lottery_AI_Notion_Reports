# V10698 — Quyết định A cho MT materializer (17:22 04/06)

Public-safe. Phụ lục V10698 sau khi owner chốt phương án.

## Quyết định owner

**Việc:** Panel "Test Challenger" trên `/du-doan-test` cho MT trống "Chưa có dữ liệu" liên tục từ 03/06.

**Phương án owner chọn: A — gộp fix vào batch Plan B kế tiếp** (cùng việc sửa mốc giờ clock-drift). KHÔNG sửa lẻ trước live, KHÔNG ảnh hưởng chu kỳ live hôm nay.

## Tóm tắt sự việc

### Triệu chứng
Panel song song "TEST CHALLENGER" trên trang `/du-doan-test` cho MT hiển thị toàn "Chưa có dữ liệu — Bundle test chưa sẵn sàng" cho cả 5 hạng mục (Bạch Thủ / Lô 2 / Lô 3 Càng / Xiên 2 / Xiên 3).

### Nguyên nhân tìm được
7 thí nghiệm cũ cho MT (`MT_ADAPTIVE_BUDGET_SELECTOR_V1`, `MT_AI_CHAIN_PRESERVATION_V1`, `MT_NO_TOKEN_HERD_REDUCTION_V1`, `MT_STRENGTH_WEIGHTED_V52_5_2`, `MT_PRIOR_REGION_CONTEXT_SAFE_V1`, `MT_SPECIALIST_ROSTER_V1`, `MT_OFFICIAL_BASELINE_CONTROL`) đã ngừng tạo từ ngày 2026-06-03 (last run = 2026-06-02).

Lỗi nằm trong logic của job tự động `_run_du_doan_test_pre_result_trigger`:
- Bước trước (sáng) đã tạo 1 row của thí nghiệm `ADAPTIVE_EXPLOIT_V1`.
- Vì đã có 1 row trong bảng `du_doan_test_bundles` cho MT, logic check `if existing` cho rằng "đã có dữ liệu rồi" → nhảy thẳng vào nhánh "refresh nhẹ" → KHÔNG chạy materialize tạo 7 thí nghiệm chính.
- Đến chiều khi MT xổ xong (17:30) thì điều kiện chặn `actual already present` kích hoạt → vĩnh viễn mất cơ hội tạo trong ngày đó.

### Hậu quả cho live hôm nay 04/06

| Bộ phận | Tác động |
|---|---|
| Dự đoán chính thức MT (`/du-doan` BT/Lô 2/Lô 3/Xiên 2/Xiên 3) | KHÔNG ảnh hưởng — `final_bundle` MT vẫn sinh đầy đủ 5 hạng mục |
| Predictions models MT (28 model dự đoán) | KHÔNG ảnh hưởng |
| Card "Output Lane Test MT" mới (BT + số phụ 1 + số phụ 2) | KHÔNG ảnh hưởng — vẫn hiện BT 56 / số phụ 1=28 / số phụ 2=42 |
| 3 thí nghiệm lane mới (`MT_FULL_POOL_D_W06_V1`, `MT_TOPK10_W04_V2`, `MT_OUTPUT_V1`, `MT_DIR*_V1`) | KHÔNG ảnh hưởng — đường ống riêng vẫn tạo bình thường |
| Panel "Test Challenger" 5 hàng | Bị ảnh hưởng (trống) — chỉ UX |

→ Live cycle 04/06 vẫn sẵn sàng 100%.

## Plan B batch — danh sách action gộp cuối cùng

Sẽ thực hiện trong 1 lần deploy duy nhất khi owner OK thời điểm:

| # | Việc | File | Loại |
|---|---|---|---|
| 1-5 | F1 clock-drift: `16:38/17:38/18:38 → 16:36/17:36/18:36` (6 chỗ trong `main.py` + 1 trong `gpt_analyzer.py`) | `main.py`, `gpt_analyzer.py` | StrReplace từng dòng |
| 6 | **Fix MT materializer**: sửa logic `if existing:` trong job pre-result trigger để chỉ skip khi 7 thí nghiệm chính đã có (không phải chỉ adaptive_exploit) | `scheduler.py:6740-6776` | Logic refactor |
| 7 | Advance VPS git HEAD pointer (drift finding cũ) | VPS git | `git reset --soft origin/master` |

**Pre-deploy required:**
- Backup sha256 cả 3 file.
- Verify local sha256 = VPS sha256 trước edit.

**Post-deploy required:**
- py_compile cả 3 file PASS.
- 4 bảng chính thức (predictions / final_bundles / lottery_results / model_daily_eval) hash GIỐNG HỆT trước/sau.
- Khởi động lại service + health check + log error trống.
- Verify chu kỳ live kế tiếp sau MT 16:40 phải có 7 thí nghiệm cũ MT trong `du_doan_test_bundles`.

**Rollback:** `git revert` + restart service.

## Tại sao gộp thay vì sửa lẻ

- `main.py` 770KB là file shared với phiên MB (`MB_MANUAL_EXPERIMENT_ENABLE` flag) — giảm bề mặt rủi ro merge conflict tương lai.
- `scheduler.py` cũng là file lớn dùng cho tất cả cron — nên đụng cùng 1 batch có pre/post zero-drift đầy đủ.
- Nguyên tắc "no partial fix" của governance.
- 3 việc trên đều cosmetic/UX, không ảnh hưởng accuracy → có thể chờ thời điểm thuận lợi.

## Trạng thái

`PUBLIC_SAFE` · official KHÔNG đụng · MN/MT bất biến · MB lane V10694 không đụng · 4 bảng chính thức hash GIỐNG HỆT. Đã ghi vào DECISION_LOG private.

**Live hôm nay 04/06 vẫn sẵn sàng**. Em không cần làm gì tiếp đến chiều — các tự verify §36G C3 (17:45) + C4 (18:35) + push V10697.1 (18:40) đã set sẵn lịch.
