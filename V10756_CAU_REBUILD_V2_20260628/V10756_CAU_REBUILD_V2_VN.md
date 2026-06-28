# V10756 — SOI-CẦU REBUILD v2 (per miền × THỨ) + học hằng tuần + tinh gọn /monitoring (SHADOW)

**Thời điểm:** 2026-06-28T13:40:00+07:00 · **Phạm vi:** SHADOW thuần, ZERO official impact · **FU:** FU-V10754-CAU-MINING

## Owner yêu cầu (verbatim)
> "Có nhiều cái em vẫn chưa tư duy tới... top 3 độc lập theo miền thứ chứ em... nay CN top 3 của MN D / MT D / MB D là rules nào, số tương ứng là gì anh phải theo dõi bằng mắt... cơ chế học tập tích lũy xếp hạng rules xây dựng như thế nào (hàng tuần/tháng/ngày)... /monitoring nhìn cả 1 rừng đo lường, tinh gọn lại dùm anh."
> "Chờ kết quả MN D hoặc MT D... chạy trigger khi đã xổ xong index ra số xếp hạng 1,2,3 (ví dụ 76-86-03). Sẵn dọn dẹp rebuild xem có bug, có chỉ số đáng giá không. Tiến hành hết A+B+C luôn em."

## Đã làm (A + B + C + D)

### A + D — Registry per (miền × THỨ), rank 1-2-3, chờ same-day
- `cau_registry` = **63 cầu** = 3 miền × 7 thứ × top-3. Mỗi THỨ đài xổ khác → cầu khác nhau (độc lập).
- **Chờ same-day + trigger:** cầu lấy nguồn cùng ngày (MT ← MN-D; MB ← MN-D + MT-D) hiển thị **"⏳ chờ xổ"**, chỉ ra số **sau khi đài nguồn xổ xong** (điền dần qua closeout MN → MT → MB). MN chỉ dùng D-1 (không có nguồn same-day trước MN) — nhân-quả đúng.
- **Rank 1-2-3 theo điểm**; xuất số xếp hạng (vd MN Chủ Nhật `03-76-86`).

### B — Cơ chế học tích lũy (re-rank hằng tuần)
- `rerank()` mine cửa sổ cuộn 320 ngày + blend forward khi đủ mẫu (forward_n ≥ 10: 0.4 in-sample + 0.6 forward), cập nhật registry.
- Cron mới: **Thứ 2 04:50** (`auto_cau_weekly_rerank`, shadow).

### C — Tinh gọn /monitoring
- Thanh lọc nhóm + chú thích (legend) + badge tự gán: 🟢 Official · 🔭 Shadow · 📊 Đo lường · 🗄️ Cũ.
- **Mặc định chỉ hiện ⭐ Trọng tâm (Official + Shadow)**; nút "📋 Tất cả" mở lại. Additive — không xê dịch panel nào (52 panel).

## Chỉ số đáng giá (owner hỏi "có chỉ số nào đáng giá không")
Holdout out-of-sample cho cách per-weekday (mine nửa cũ, đo nửa mới, gộp 21 slice):

| | Train (chọn) | **Test (out-of-sample)** | Nền |
|---|---|---|---|
| Gộp mọi (miền×thứ) | 60-72% | **32.5%** (n=1432) | 34.1% (n=47900) |

- **LIFT out-of-sample = −1.6pp (ÂM).** Chỉ **6/21** slice có lift>0.
- Slicing theo thứ làm mẫu/cầu còn ~45 → **overfit NẶNG HƠN** structural (xác nhận lại V10754.1).
- ⇒ **Tuyệt đối KHÔNG feed official**; chỉ forward-test minh bạch. Đây là chỉ số bảo vệ owner khỏi đặt cược vào nhiễu.

## Rà bug (rebuild)
- Chuỗi nguồn causal đúng (MN chỉ D-1; MT thêm MN-D; MB thêm MN-D + MT-D — mọi nguồn xổ TRƯỚC đích).
- Upsert idempotent (gọi 3×/ngày sau mỗi closeout không nhân đôi).
- Không phát hiện bug ghi official.

## An toàn (hard contract)
- diagnostic_only=1, output_eligible=0, owner_approved=0, shadow_only=1.
- **Hash-guard 4 bảng official IDENTICAL pre/post:** predictions `0330ef5b4c7d568d` (8731), final_bundles `187a14f2fa1b2364` (361), lottery_results `37c13fc19d183d7c` (14964), model_daily_eval `a8b3e491230c9cc9` (8553).
- health=200, endpoint=401, /monitoring=401 (admin-gated). registry=63, forward=7.

## Files
- `web/backend/_v10755_cau_forward_shadow.py` (viết lại v2, registry-driven)
- `web/backend/main.py` (API `/api/admin/cau-forward-shadow` viết lại)
- `web/backend/scheduler.py` (cron re-rank Thứ 2 04:50)
- `web/frontend/monitoring.html` (panel viết lại + thanh lọc/legend/badge)
- Artifact: `artifacts/cau_mining_20260628/CAU_MINING_FINDINGS.md` §6
