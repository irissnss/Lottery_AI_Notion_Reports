# V10730 — Audit toàn diện live + Phase 1 "BẢNG NÊN CHƠI" (public-safe)

- **Ngày:** 2026-06-18 (Asia/Ho_Chi_Minh, UTC+7)
- **Phạm vi:** Audit read-only + UI/admin consolidation. KHÔNG đụng official `/du-doan`, final_bundles writer, model selector.
- **An toàn:** 4 bảng official hash IDENTICAL pre/post; admin endpoint no-store + 401 unauth; freeze method đảo ngược được.

## Owner directive (verbatim)

> "Đã nhiều ngày anh để yên hệ thống chạy live và kết quả quá chán đó em. Em kiểm tra toàn bộ, toàn diện dùm anh, các luồng hỗn tạp quá không biết đâu mà chơi. các đơn model quá ư là dao động không ổn định, card thì có số đúng, total output bắt tính hiệu tổng hợp kiểu gì lane test, hay office gì mà bữa trúng bữa trật liên tục khó quá khó em."

> "Tất cả mọi thứ từ A, B, C, D, E rồi đưa ra đề xuất thật phù hợp mạnh mẽ nhất cho anh. Mong muốn là tinh gọn, chính xác cải thiện dự đoán."

> "ok go phase 1"

## 1. Audit — 4 phát hiện (data-backed, VPS thật)

1. **Coverage TỐT (nhân quả):** ~30-31/31 ngày có ≥1 model chốt TRÚNG lô. Dàn model gần như ngày nào cũng có số đúng.
2. **Conversion = TRẦN:** official BT (bạch thủ lô) 30d MN 45% / MT 32% / MB 23% ≈ NGANG model mạnh nhất (combo-super 50%). Tổng hợp KHÔNG vứt số — đã ở trần ex-ante. "Bữa trúng bữa trật" của 1 con BT là bản chất → nhìn 14-30d.
3. **Lane KHÔNG có edge bền (chống overclaim):** rolling scoreboard khoe MN ADAPTIVE_EXPLOIT 66.7% NHƯNG leakage_risk 60/60 runs. Bằng chứng SẠCH `champion_selector_shadow` (settled-forward 28d): MN champ 13 = official 13 (HÒA), MT 7 < official 10 (THUA), MB 7 > official 5 (nhỉnh). → con 66.7% là ẢO; settled thật = ngang official. Khớp recommender (MN/MT→OFFICIAL, MB→LANE).
4. **Opus đã sống lại** sau fix V10729 (`claude-opus-4-20250514` EOL 404 → `claude-opus-4-6`): 16/06 strength=0 → 17-18/06 strength 3.8-5.5 thật.

**Kết luận:** Không có "phép màu" accuracy. Đòn bẩy thật = tinh gọn + rõ ràng (1 chỗ quyết định) + ống kính ổn định 14-30d.

## 2. Phase 1 — Deliverables (owner GO)

- **Board "NÊN CHƠI"** (`GET /api/admin/play-decision-board`, require_admin, no-store) + panel ĐẦU trang `/monitoring` (auto-refresh 60s): gom official/lane + băng win-rate 14/30d + bằng chứng settled sạch + cờ leakage + số BT gần nhất.
- **Tinh gọn:** freeze 7 method lane chết (<=2 win/30d: 6 MB + MN_PRIOR_REGION) — đảo ngược qua `app_settings('lane_lean','frozen_methods')`, KHÔNG xoá data, KHÔNG tắt materializer. 57 → 50 method active.
- **Stability lens:** board nhắc "nhìn 14-30 ngày, đừng soi từng ngày".

## 3. Khuyến cáo LIVE (độc lập miền)

| Miền | NÊN CHƠI | Official 30d | Settled sạch (champ vs off) |
|---|---|---|---|
| MN | OFFICIAL | 43-45% | 13 = 13 (ngang) |
| MT | OFFICIAL | 33% | 7 < 10 (official hơn) |
| MB | LANE (PRIOR_REGION 34.5%) | 21-23% | 7 > 5 (lane nhỉnh) |

## 4. Verify (LIVE_PROVEN)

- remote py_compile OK · service active · health 200 · board 401 unauth (locked).
- 4 bảng official hash IDENTICAL pre/post = `5b179fff7dcb7b71`.
- KHÔNG promote lane→official (evidence không bền).

## 5. Next

- Live-verify board mỗi ngày 2-3 tuần.
- Cân nhắc Phase 1b (ẩn frozen khỏi panel lane cũ) + Phase 3 (chọn miền×thứ).
