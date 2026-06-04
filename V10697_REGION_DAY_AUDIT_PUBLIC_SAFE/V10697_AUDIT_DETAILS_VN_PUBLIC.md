# V10697 — Báo cáo audit Canonical Region-Day Contract (READ-ONLY) — chi tiết các vấn đề chờ xác nhận

Public-safe. Ngày T5 2026-06-04. Không endpoint riêng, không IP, không khoá riêng.

## 1. Tổng quan

Owner yêu cầu audit tổng hợp xem hệ thống có vận hành đúng quy ước Region-Day không (`D` / `D-1` / `D-2`, same-day upstream `MN → MT → MB`, preview vs verified). Audit READ-ONLY, không sửa code.

Kết quả tổng: **đúng quy ước 14/14 hạng mục**. Không có rò rỉ chéo miền, không có chuyện gán nhầm D verified thành D-1, không trộn preview vào KPI đã chốt. Báo cáo này chi tiết hoá 3 hạng mục mà owner cần xác nhận: F1 và 2 mục thuộc §36G.

---

## 2. F1 — Mốc giờ trong endpoint `/api/mined-rules/preview-state`

### 2.1 Phát hiện chi tiết

Trong file `web/backend/main.py` đoạn 3755–3819 có 3 chỗ nhắc tới giờ xổ:

| Loại | Dòng | Giá trị | Đúng/Sai |
|---|---|---|---|
| **Logic chuyển trạng thái** (`mn_done` / `mt_done` / `mb_done`) | 3774–3776 | `16:36 / 17:36 / 18:36` | **ĐÚNG** — khớp quy ước "MN xổ xong 16:36, MT xổ xong 17:36, MB xổ xong 18:36" |
| **Docstring** | 3760–3763 | `16:38 / 17:38 / 18:38` | **SAI** — di sản cũ chưa cập nhật |
| **Nhãn UI banner** (`draw_time`, `done_at`) | 3790–3798 | `16:38 / 17:38 / 18:38` | **SAI** — di sản cũ chưa cập nhật |

### 2.2 Ảnh hưởng

- Logic chuyển trạng thái dùng số đúng (16:36/17:36/18:36) → state machine vẫn chính xác.
- Chỉ có docstring + nhãn UI ghi 16:38 → owner đọc thấy không đồng nhất.
- KHÔNG ảnh hưởng đến: prediction logic, scheduler timing, evaluation, KPI verified.

### 2.3 Đề xuất (chờ owner OK)

Sửa **3 dòng docstring + 6 string trong UI label** thành `16:36 / 17:36 / 18:36` để khớp logic.

- Phạm vi: 1 file `web/backend/main.py`.
- Loại change: read-only API metadata + docstring.
- Rủi ro: 0 (không đụng logic, không đụng prediction, không đụng official tables).
- Rollback: 1 dòng git revert.

### 2.4 Lý do chờ owner

Không khẩn, không ảnh hưởng accuracy. Có thể chờ lúc owner OK gộp vào batch khác. Hoặc owner có thể chốt KHÔNG sửa vì 16:36 vs 16:38 chỉ chênh 2 phút.

---

## 3. §36G — P0 MB FULL-CLOSURE & LIVE-READY GATE

Quy ước (§36G `.Antigravityrules.md`) yêu cầu **đồng thời đủ 4 điều kiện** mới được gọi `FULL_CLOSURE_PASS`:

| # | Điều kiện | Kiểm tra thế nào |
|---|---|---|
| 1 | Bản patch lock-guard theo phase đã nằm trong canonical repo | Code search `phase_run_source` + LOCK guard trong `scheduler.py` |
| 2 | Runtime production đang chạy bản đã deploy (health OK) | Service active + `/api/health` 200 + `/login` 200 |
| 3 | Day-new sau phiên MT có `run_source='rerun_post_mt'` cho MB | Query `predictions` ngày mới: phải có hàng `target_region='MB'` + `run_source='rerun_post_mt'` |
| 4 | Day-new MB no-token `DD Sau KQ` không trống (`pre_result_numbers` non-empty) | 7 no-token model (smart-ensemble, smart-ml, combo-no-token, meta-learning, lstm, random-forest, xgboost) cho MB ngày mới phải có `pre_result_numbers` non-empty |

### 3.1 Trạng thái hôm nay 04/06 (lúc 11:00)

| Điều kiện | Trạng thái hôm nay 04/06 |
|---|---|
| 1. Lock-guard patch | ✅ ĐÃ CÓ (verify code) |
| 2. Runtime health | ✅ Service active, /api/health 200, /login 200 |
| 3. MB rerun_post_mt cho 04/06 | ⏳ **CHƯA THỂ KIỂM TRA** — MT xổ 17:30 hôm nay, cron rerun 17:42 hôm nay |
| 4. MB no-token pre_result hôm nay | ⏳ **CHƯA THỂ KIỂM TRA** — đợi sau MT xổ |

→ Hôm nay 04/06 KHÔNG THỂ tuyên bố `FULL_CLOSURE_PASS` ngay vì điều kiện 3 và 4 đang chờ chu kỳ live tự nhiên (MT xổ → MB rerun → MB xổ).

### 3.2 Bằng chứng từ chu kỳ 03/06 (HÔM QUA — đã đủ chu kỳ)

Em verify trên hôm qua để CHỨNG MINH chu kỳ sản xuất chạy đúng §36G:

**Điều kiện 3 — MB rerun_post_mt ngày 03/06:**

```
MB run_source='rerun_post_mt'  n=7  first@17:30  last@17:30  ✓ PASS
```

7 model rerun cho MB ngay sau khi MT xổ lúc 17:30 ngày 03/06. Đúng phase, đúng số lượng.

**Điều kiện 4 — MB no-token pre_result_numbers ngày 03/06:**

| Model | `main_numbers` (sau xổ MB) | `pre_result_numbers` (trước xổ MB) | Trạng thái | `context_integrity` |
|---|---|---|---|---|
| combo-no-token | `["40","12"]` | `["57","29"]` | LOSE | **clean** ✅ |
| lstm | `["75","14"]` | `["86","57"]` | LOSE | **clean** ✅ |
| meta-learning | `["29","24"]` | `["24","29"]` | LOSE | **clean** ✅ |
| random-forest | `["29","35"]` | `["29","35"]` | PARTIAL | **clean** ✅ |
| smart-ensemble | `["40","29"]` | `["40","29"]` | LOSE | **clean** ✅ |
| smart-ml | `["40","29"]` | `["29","57"]` | LOSE | **clean** ✅ |
| xgboost | `["12","29"]` | `["12","29"]` | LOSE | **clean** ✅ |

→ **Tất cả 7 model có `pre_result_numbers` non-empty và `context_integrity='clean'`. PASS.**

### 3.3 Kết luận §36G

- **Chu kỳ 03/06: FULL_CLOSURE_PASS = TRUE** (4/4 điều kiện thoả mãn — đã chứng minh).
- **Chu kỳ 04/06: PARTIAL_READY** (giữ trạng thái cho đến khi MT/MB xổ xong và verify điều kiện 3+4).
- Theo quy tắc "no pass-washing" của §36G, không được tuyên bố hôm nay FULL_CLOSURE khi day-new evidence chưa có.

---

## 4. Verify rerun_post_mt cho MB ngày 04/06 — kế hoạch tự động

### 4.1 Khi nào kiểm tra được

- **MT xổ:** 17:30 hôm nay 04/06.
- **MB rerun cron:** 17:42 hôm nay (chained sau MT verify).
- **MB xổ:** 18:30 hôm nay.

### 4.2 Cách kiểm tra (sau 17:45)

Em sẽ chạy lệnh đọc (READ-ONLY, không sửa) trên VPS:

```sql
-- Kiểm tra điều kiện 3
SELECT target_region, run_source, COUNT(*) AS n,
       substr(MIN(created_at),12,5) AS first_at,
       substr(MAX(created_at),12,5) AS last_at,
       context_integrity
FROM predictions
WHERE date='2026-06-04' AND target_region='MB' AND run_source='rerun_post_mt'
GROUP BY target_region, run_source, context_integrity;
-- Kỳ vọng: n=7, first_at gần 17:30, integrity='clean'
```

```sql
-- Kiểm tra điều kiện 4
SELECT ai_model, main_numbers, pre_result_numbers, pre_result_status, context_integrity
FROM predictions
WHERE date='2026-06-04' AND target_region='MB'
  AND ai_model IN ('smart-ensemble','smart-ml','combo-no-token','meta-learning',
                    'lstm','random-forest','xgboost')
ORDER BY ai_model;
-- Kỳ vọng: 7 hàng, pre_result_numbers tất cả non-empty, integrity='clean'
```

### 4.3 Sau khi thu thập

Em sẽ surface kết quả tự động sau 17:45 và sau 18:35 (MB xổ xong), cập nhật một báo cáo bổ sung V10697.1 và đẩy lên GitHub public chờ owner xác nhận `FULL_CLOSURE_PASS` cho 04/06.

---

## 5. Tổng kết

### Các kết luận ĐÃ CHỐT (audit READ-ONLY 10:58 sáng 04/06)

- ✅ Hệ thống vận hành đúng canonical Region-Day contract (14/14 hạng mục).
- ✅ §36G điều kiện 1 + 2: PASS tại thời điểm hiện tại.
- ✅ Chu kỳ 03/06: PASS toàn bộ 4 điều kiện §36G (chứng minh chu kỳ sản xuất hoạt động đúng).
- ✅ Không có rò rỉ chéo miền, không có nhầm D verified thành D-1.

### Các kết luận CHỜ owner xác nhận

| # | Việc | Trạng thái | Cần làm |
|---|---|---|---|
| F1 | Sửa mốc giờ docstring + UI label `16:38 → 16:36` (3 + 6 chỗ trong `main.py`) | Đề xuất chờ owner OK | Owner quyết: sửa hay giữ |
| §36G C3 | MB rerun_post_mt cho 04/06 | Chưa thể verify | Em tự verify sau 17:45 hôm nay |
| §36G C4 | MB no-token pre_result cho 04/06 | Chưa thể verify | Em tự verify sau 18:35 hôm nay |
| §36G FULL_CLOSURE 04/06 | Tổng kết | Chưa thể tuyên bố | Em surface sau 18:35 hôm nay |

### Hard rules tuân thủ

- KHÔNG sửa code/runtime trong audit này.
- KHÔNG deploy.
- KHÔNG cập nhật Notion.
- Mọi kết luận accuracy đều dùng VPS live DB qua truy cập SSH chuẩn.

---

## 6. Trạng thái

`PUBLIC_SAFE` — không IP, không endpoint riêng, không khoá. Mọi câu hỏi owner có thể trả lời dựa trên báo cáo này. Em chờ xác nhận F1 và tự surface kết quả §36G chu kỳ 04/06 sau 18:35 hôm nay.
