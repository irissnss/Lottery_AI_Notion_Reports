# V10784 P4.4 — MA TRẬN TRÙNG LẶP MỤC ĐÍCH → GIỮ / HỢP NHẤT / ĐỀ XUẤT BỎ

Ngày 05/07/2026. Phạm vi: bảng / endpoint / card monitoring / script.
**Nguyên tắc: CHỜ KÝ — không xóa gì trong phiên này.** "BỎ" = đề xuất archive (tắt loader + giữ data), không drop bảng.

Hiện trạng đo được: ~60 admin endpoint, ~48 loader card /monitoring, ~250 script `_v*` trong web/backend.

## CỤM 1 — Đo accuracy model (7 surfaces cùng trả lời "model nào đúng")

| Surface | Mục đích | Đề xuất |
|---|---|---|
| `/api/admin/model-daily-accuracy` | accuracy per model per ngày | **GIỮ** (nguồn chuẩn từ model_daily_eval) |
| `/api/admin/three-layer-scoreboard` | 3 lớp official/shadow/test | **GIỮ** (board tổng hợp chính V10773) |
| `/api/admin/model-bt-by-region` | BT hit per model×miền | **HỢP NHẤT** → thành tab trong three-layer |
| `/api/admin/model-family-bt` | BT hit per family | **HỢP NHẤT** → tab trong three-layer |
| `/api/admin/region-weekday-strength` | strength miền×thứ | **GIỮ** (trục canonical riêng) |
| `loadRanking` (monitoring) | ranking model | **HỢP NHẤT** → three-layer |
| `/api/admin/master-board` (V87) | board tổng thời V87 | **ĐỀ XUẤT BỎ** (concluded era, data giữ) |

## CỤM 2 — Master boards theo thời kỳ (5 boards "command center" chồng lịch sử)

| Surface | Đề xuất |
|---|---|
| `/api/admin/v98-command-center` + card | **GIỮ** (mới nhất, đang dùng) |
| `/api/admin/v96-master-tracker` + card | **ĐỀ XUẤT BỎ** (superseded by v98) |
| `/api/admin/v95-dashboard` + card | **ĐỀ XUẤT BỎ** (superseded) |
| `/api/admin/v82-monitor` + card | **ĐỀ XUẤT BỎ** (concluded) |
| `loadV87MasterIndex` + card | **ĐỀ XUẤT BỎ** (concluded) |

## CỤM 3 — Lane test /du-doan-test (7 surfaces)

| Surface | Đề xuất |
|---|---|
| `/api/admin/test-lane-history` | **GIỮ** (lịch sử lane test chuẩn) |
| `/api/admin/test-lane-metrics` | **GIỮ** |
| `/api/admin/v10605-lane-test-scoreboard` | **HỢP NHẤT** → test-lane-metrics (cùng câu hỏi "lane test ăn official không") |
| `/api/admin/test-lane-readiness` | **GIỮ** (điều kiện chạy, khác mục đích) |
| `/api/admin/test-lane-diff-vs-official` | **HỢP NHẤT** → test-lane-metrics |
| `/api/admin/v10622-parallel-live-board` | **ĐỀ XUẤT BỎ** (era V10622 concluded) |
| `/api/admin/parallel-shadow-proof` | **ĐỀ XUẤT BỎ** (proof một lần, đã kết luận) |

## CỤM 4 — Boards quyết định chơi (4 surfaces cùng trả lời "hôm nay chơi gì")

| Surface | Đề xuất |
|---|---|
| `/choi` (money-board + method lock) | **GIỮ** — nguồn chuẩn quyết định chơi (V10759/V10782) |
| `/api/admin/play-decision-board` (monitoring) | **GIỮ** (view admin của /choi — cùng nguồn compute_board) |
| `/api/admin/play-recommendation` | **HỢP NHẤT** → play-decision-board (trùng mục đích) |
| `/api/admin/v10615-tomorrow-decision-board` | **ĐỀ XUẤT BỎ** (era concluded, thay bằng /choi lock tuần) |
| `/api/admin/live-day-controller` | **GIỮ** (điều phối ngày sống, khác mục đích) |

## CỤM 5 — Signal governance một thời (4 surfaces era V10606–V10613)

| Surface | Đề xuất |
|---|---|
| `/api/admin/v10606-signal-governance` | **ĐỀ XUẤT BỎ** (concluded, giữ data) |
| `/api/admin/v10607-signal-pruning` | **ĐỀ XUẤT BỎ** (concluded) |
| `/api/admin/v10610-remediation-board` | **ĐỀ XUẤT BỎ** (concluded) |
| `/api/admin/v10613-safe-shadow-application` | **ĐỀ XUẤT BỎ** (concluded) |

## CỤM 6 — Consensus/shadow trackers đang sống (giữ nguyên nhóm này)

`consensus-freeshadow`, `output-final-lab`, `ev-song-thu`, `pnl-forward-track`, `cau-forward-shadow`, `cycle-scan` (mới V10784), `mb-rf-shadow`, `rescue-candidate-monitor`, `signal-quality-skip`, `pattern-reasoning`, `aggregation-signal` — **GIỮ TẤT CẢ** (forward đang tích lũy, mỗi cái đo 1 câu hỏi riêng owner đã duyệt). Lưu ý: khi 1 tracker kết thúc chu kỳ đo → chuyển nhóm CŨ (đã có cơ chế panel filter V10773).

## CỤM 7 — Scripts `_v*` một lần (~250 file trong web/backend)

| Nhóm | Đề xuất |
|---|---|
| Scripts phiên hiện hành (_v10784_*) | **GIỮ** tới khi phiên đóng |
| Scripts deploy/probe các phiên đã đóng (_v10781_*, _v10782_*, _v10783_* đã xong) | **HỢP NHẤT** → move `backups/script_archive/<version>/` (giữ git history, dọn thư mục runtime) |
| Materializers đang chạy cron (_materialize_*, _v10733_, _v10755_...) | **GIỮ** (runtime thật) |
| Scripts `.bak_*`, `.pre` trong backend | **ĐỀ XUẤT BỎ** khỏi thư mục runtime → move backups/ (không nằm cạnh code sống) |

## TÁC ĐỘNG NẾU KÝ

- Giảm ~14 endpoint + ~12 card monitoring (nhóm CŨ/concluded) → giảm lag /monitoring thêm một nấc (tiếp nối V10773 đã giảm 39→17 loader auto-refresh).
- KHÔNG mất data: mọi bảng giữ nguyên; chỉ tắt loader + đánh dấu endpoint deprecated (410 hoặc ẩn khỏi UI).
- Rollback: bật lại loader/endpoint từ git.

## BẢNG CHỜ KÝ (gom về báo cáo tổng V10784)

| # | Hành động | Mức rủi ro |
|---|---|---|
| S1 | BỎ 5 master boards cũ (v82/v87/v95/v96→v98 giữ) | Thấp (readout-only) |
| S2 | HỢP NHẤT cụm accuracy (3 endpoint → three-layer tabs) | Trung bình (cần 1 phiên UI) |
| S3 | HỢP NHẤT cụm lane test (2 endpoint) | Thấp |
| S4 | BỎ 4 boards signal-governance era | Thấp |
| S5 | Archive scripts phiên đã đóng + .bak khỏi backend/ | Thấp (move file, git giữ) |
