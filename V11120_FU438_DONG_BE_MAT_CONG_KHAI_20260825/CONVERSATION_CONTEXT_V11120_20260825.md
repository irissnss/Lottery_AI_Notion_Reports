# CONVERSATION CONTEXT — V11120 · 25/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ là **giờ Việt Nam (UTC+7)**.

## 1 · Owner nói gì — nguyên văn

Prompt 36, mục `V. P0 SECURITY — FU-438`:

> *« 1. Vẽ route → handler → auth middleware cho: `/du-doan`, `/api/final-bundle`,
> `/api/final-bundle/history`, `/api/final-bundle/selection-delta` **và mọi endpoint trả
> bundle/rank/voter**. 2. Xác nhận `file:hàm:dòng` khiến history bỏ qua auth. 3. **Patch common
> admin gate fail-closed.** 4. Test: anonymous; user thường; admin; thiếu request context; auth
> backend lỗi; endpoint chị em; response field allowlist. 5. **Anonymous/non-admin phải 401/403
> hoặc redirect login. Admin Owner phải thấy full current/history.** … 9. Nếu thiếu quyền deploy:
> dừng tại `READY_TO_DEPLOY_FU438` và hỏi Owner **đúng một câu** duyệt deploy. »*

Và mục `III`: *« Owner đã khóa `ADMIN_ONLY`/`CLOSE_VIEWER`; không hỏi lại chính sách này. »*
Mục `I`: `AUTHORIZED_LAYER = LOCAL_CODE_GIT_DB_COPY_TEST_VPS_READ`.

## 2 · Agent làm gì — theo trình tự

| # | việc | kết quả |
|---|---|---|
| 1 | Liệt kê **mọi** route trả bundle/rank/voter | 27 route, chấm trạng thái auth từng cái |
| 2 | Đọc chữ ký ba hàm được nêu đích danh | `history` và `selection-delta` **không có `request`**; `final-bundle` **có** |
| 3 | Đo **ẩn danh** trên production (`RM-13`) | phát hiện bề mặt rò **~678 KB**, không phải 39,7 KB |
| 4 | Đo `/api/final-bundle` với 3 ngày ≤ mốc đóng băng | `1.711 B`, **không** rò — nhưng đọc mã thì lý do là **cổng publish rỗng**, không phải lọc trường |
| 5 | Truy `get_bundle_history` | `database.py:4977` `SELECT … source_predictions_json` — đây là vector rò |
| 6 | Backup `main.py` | `backups/main.py.pre_FU438_20260825`, `1.007.440 B`, khớp `md5` |
| 7 | Viết cổng chung **fail-closed** + danh sách cho phép | `+169 / −10` dòng |
| 8 | Quét ai đang gọi từng đường ở frontend | `/api/predictions` nuôi **trang công khai** ⇒ xử **khác** |
| 9 | Viết bộ thử 7 ca + thử hai chiều | **17/17 ĐẠT**, mã thoát 0 |
| 10 | `py_compile` + kiểm import (`Request`, `status`, `Dict`, `Any`) | **OK** |
| 11 | Commit release candidate | `c8d87a5` → gỡ blob backup → `731a10a` |
| 12 | **Dừng tại `READY_TO_DEPLOY_FU438`** | `AUTHORIZED_LAYER = VPS_READ` |

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · Bộ quét route của chính agent bỏ sót bản vá vừa viết
Cửa sổ quét 14 dòng, mà docstring mới dài hơn ⇒ báo nhầm *«chưa gắn cổng»* cho cả ba đường vừa vá.
Quét lại với cửa sổ 34 dòng: **đã gắn đủ**.
**Hậu quả nếu bỏ qua:** báo cáo sai về chính bản vá của mình.

### V2 · Giả thuyết sai, phải tự bác trước khi trình
Agent định kết luận `/api/final-bundle` *«chặn đúng theo trường»*. Đo thật thì không rò — **nhưng
đọc mã thì lý do là nhánh `WAIT_MODEL_COUNT` rỗng**, không phải lọc trường. Nếu dừng ở phép đo thì
đã bỏ sót một **rò tiềm tàng** cùng nhóm trường.

### V3 · Quyết định phạm vi — không vá bừa
Bốn đường (`model-selection` · `prediction-advisory` · `model-ranking` · `repredict-quality`) **không
có auth** nhưng phép đo **không thấy** trường nhạy cảm. Agent **không vá** — chỉ khai `FU-440` để
owner quyết. Vá cái chưa chứng minh là rò thì đúng lỗi *«đổi mù»*.

### V4 · `/api/predictions` — chỗ dễ làm hỏng trang công khai nhất
Nếu áp `require_admin` như bốn đường kia thì `/user-view` **tắt hẳn** ⇒ phá luật sản phẩm *«luôn xuất
số»*. Đã tra `user-view.js:466-487` đếm **đúng** trường trang đọc, rồi lọc theo danh sách cho phép —
**đúng khuôn `V11042`** đã chọn cho `/api/status`.

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| **Deploy** | `AUTHORIZED_LAYER = VPS_READ`. Mục `V.9` quy định rõ: dừng tại `READY_TO_DEPLOY_FU438` |
| Vá 4 đường chưa chứng minh rò | không có bằng chứng ⇒ khai `FU-440`, để owner quyết |
| Đóng cứng `/api/predictions` | phá trang công khai |
| Đụng `/du-doan` (trang) | nó là `FileResponse` tĩnh; dữ liệu nằm ở API — đóng API là đủ |
| Hỏi owner bằng mã ngắn | prompt 36 cấm; câu hỏi deploy viết bằng lời thường trong Decision Packet |

## 5 · Trạng thái cuối

| | |
|---|---|
| tệp sửa | `web/backend/main.py` · `+_v11120_thu_chan_fu438.py` |
| deploy | **KHÔNG** |
| restart | **KHÔNG** |
| ghi DB | **KHÔNG** |
| chạm `/du-doan` | **KHÔNG** |
| production | 🔴 **vẫn đang rò ~678 KB** cho tới khi owner ký deploy |

**TanPhatAI cần làm:** đọc `REPORT_V11120 §9` — `FU-438` là `CODE_PUSHED`, **chưa** `DEPLOYED`.
