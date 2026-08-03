# Bảng kết quả V10975 — kiểm đầu ngày 03/08/2026

Chụp lúc **2026-08-03 08:51:20 +07** từ VPS `14.225.224.89`, DB
`/root/Lottery_AI_Test/data/lottery_ai.db`. Mọi script đều **chỉ đọc**.

## Cổng đầu phiên

| Phép | Kết quả |
|---|---|
| Checkpoint quá hạn | 0 |
| Roadmap chờ archive | 0 |
| Mục theo dõi treo | 79 (quá hạn 0) |
| Quyết định tới hạn rà soát | 0 / 19 |
| Sổ quyết định TRÔI | **0** (19/19 khớp) |
| Ba mặt quy tắc lệch | không (fd77cad 02/08) |

## Trạng thái sống

| Mục | Giá trị |
|---|---|
| `/api/health` | 200 · V20.3.36 |
| Service | `lottery` active |
| PID | 645169 (từ 02/08 18:13:33, 14h37m) |
| Journal traceback hôm nay | 0 / 181 dòng |
| `scheduler_logs` ERROR hôm nay | 0 |
| Tự kiểm nhất quán | 16/16 OK (02/08 18:05:01) |

## Bundle và kết quả

| Ngày | Miền | model_count | bach_thu | trạng thái |
|---|---|---|---|---|
| 2026-08-03 | MN | **15** | 64 | ACTIVE, fallback=0, chốt 05:20:15 |
| 2026-08-02 | MN | 15 | 43 | **WIN** |
| 2026-08-02 | MT | 13 | 69 | **WIN** |
| 2026-08-02 | MB | 14 | 52 | **WIN** |

Kết quả 02/08: MN 3 đài · MT 3 · MB 1 — khớp đúng 6 Chủ Nhật gần nhất
(26/07 · 19/07 · 12/07 · 05/07 · 28/06).
Chấm điểm 02/08: 27 model × 3 miền, **0 dòng chưa chấm**.

## Cổng lợi thế — tính tươi 03/08 (không ghi bảng)

| Cửa sổ | Miền | Hệ | Bừa | Lợi thế | z | Còn thiếu | Cổng |
|---|---|---|---|---|---|---|---|
| 90 ngày | MN | 16,25% | 16,46% | **−0,21pp** | −0,09 | 2,11pp | ĐÓNG |
| 90 ngày | MT | 13,70% | 16,51% | **−2,81pp** | −1,12 | 4,67pp | ĐÓNG |
| 90 ngày | MB | 16,67% | 23,71% | **−7,04pp** | −1,57 | 10,88pp | ĐÓNG |
| 30 ngày | MN | 15,79% | 16,32% | −0,53pp | −0,14 | 2,58pp | ĐÓNG |
| 30 ngày | MT | 12,16% | 16,61% | −4,45pp | −1,03 | 6,21pp | ĐÓNG |
| 30 ngày | MB | 23,33% | 23,47% | −0,13pp | −0,02 | 4,22pp | ĐÓNG |

Ngưỡng owner: hơn bừa **≥3pp VÀ z ≥2**. Không ô nào đạt.
Bảng `edge_gate_daily` sau khi đọc vẫn **3 dòng, ngày 2026-08-01 22:01:25** — không ghi thêm.

## Lane hết hạn còn ghi (FU-185)

| Ngày | Số dòng | Lane |
|---|---|---|
| 31/07 | 68 | MN+MT+MB: DIR1/2/3, FULL_POOL, TOPK, DOCTRINE, PROMPT_V2 |
| 01/08 | 19 | MN DIR1/2/3 + DOCTRINE + PROMPT_V2 + MB FULL_POOL/TOPK |
| 02/08 | **10** | chỉ còn MB_FULL_POOL_D_W06_V1 + MB_TOPK10_W04_V2 |
| 03/08 | **0** (tính tới 08:51) | lane MB chạy 17:43 chiều nay |

Thủ phạm: `web/backend/_mb_advanced_lane_daily.sh` gọi thẳng
`_v10679_full_pool_d_w06_lane.py` và `_v10680_topk_strength_lane.py`.
Cron của hai script đó **đã comment hết** từ V10919 — cắt cron không cắt được đường này.
File `.sh` còn có **2 dòng cron trùng**: `43 17` (dòng 52) và `38 17` (dòng 66).

## FU-225 — file frontend

| Phép | Kết quả |
|---|---|
| `difflib` VPS vs local | **0 dòng khác / 4002 dòng** |
| Dung lượng | VPS 221.956 · local 217.954 — lệch 4002 byte = đúng số dòng → CRLF vs LF |
| Marker V10964 | `pageDateAnchor` ×2 · `blocked_test_bundle` ×3 · `display_date_anchor` ×4 (cả hai bên) |
| `/filter` | 200 + `Cache-Control: no-store, no-cache, must-revalidate, max-age=0` |
| `/du-doan-test` | 401 (đúng thiết kế trang admin) |

## Hash 4 bảng khoá (mốc 03/08 08:51)

| Bảng | Dòng | SHA256 (20 ký tự đầu) |
|---|---|---|
| `predictions` | 11.592 | `0b84203853b2aeba70a2` |
| `final_bundles` | 469 | `85dd4a7840a576f7473b` |
| `lottery_results` | 15.201 | `06e0bbf0e4da50c8f1bb` |
| `model_daily_eval` | 11.415 | `dcfad896d0328071def7` |
