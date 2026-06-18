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

## 5. Cập nhật P1.1 + 1b + 3 (2026-06-18 20:55)

Owner soi "nên chơi hôm nay hơi tệ, xui hay tính sai?" → verify 18/06 phát hiện **BUG hiển thị**:

- **BUG:** board `today_bt` luôn lấy official kể cả khi play=LANE. MB khuyến cáo LANE chốt **75 = WIN** nhưng board hiện official **57 = LOSE** → tưởng trật. MN/MT OFFICIAL 99/62 LOSE là **xui thật** (variance ~33-45%/miền).
- **Fix P1.1:** `today_bt` theo đúng luồng (LANE → `du_doan_test_results`; else official) + `today_source` + UI màu WIN/LOSE. VPS: MB src=LANE 75 WIN.
- **Phase 1b:** board guard KHÔNG khuyến cáo method frozen (ép OFFICIAL) + hiện danh sách đã ẩn (method lane chết không có panel cũ riêng → enforce ở tầng quyết định).
- **Phase 3:** `GET /api/admin/region-weekday-strength` + panel "SỨC MẠNH MIỀN × THỨ" (90d, tier tương đối). MN khỏe T2/T3/CN (TB 47%), MT đỉnh T5, MB chỉ T3 (TB 22%) → size cược theo miền×thứ (accuracy đã ở trần).
- **An toàn:** 4 bảng official hash IDENTICAL; health 200; board+rwd 401 unauth; private push 42e2793.

## 6. Phase A — EV 1 SỐ vs SONG THỦ (khai thác số phụ, 2026-06-18 21:10)

Owner phản biện đúng: "trần" sai từ — tín hiệu **CÓ**, nằm ở **số phụ**, bị giấu vì chỉ xuất 1 số.

- **Bằng chứng:** 2-số coverage 30d MB 41.9% / MN 58.1% / MT 58.1% (vs 1-số 22.6/45.2/32.3). "Trần thật" (cả 2 trượt) MN/MT chỉ ~32-42% ngày.
- **Đo EV** bằng đúng mô hình owner (cost 18k/điểm, payout 98k/điểm/nháy, per-đài): `ev_song_thu_shadow` + `/api/admin/ev-song-thu` + panel /monitoring.
- **Kết quả 90d (nuanced):** MN T2/T3→1 số (phụ −EV), T5-CN→song thủ; MT T2 phụ +151% / T6T7→1 số; MB T3→1 số (+109%), CN→song thủ +318%, T5/T7 song thủ.
- **Caveat:** payout 1-ăn-98 hơi rộng + n~13/thứ → directional. SHADOW (output_eligible=0), chưa đụng ví/official.
- **An toàn:** 4 bảng official hash IDENTICAL; health 200; ev 401; private push 73101a9.

## 7. PA.1 — Gắn cặp SONG THỦ vào bảng NÊN CHƠI (2026-06-18 21:20)

Owner soi ảnh hỏi "song thủ thì board hiện cặp + khuyến cáo gì" → tích hợp EV vào board.

- Mỗi miền hiện thêm **số phụ + cặp** + dòng "Hôm nay Tx: 🎯 SONG THỦ a–b (ROI...)" hoặc "CHỈ 1 SỐ" theo EV của thứ hôm nay. Nguồn phụ: LANE→`test_lo2_json`, OFFICIAL→`final_bundles.lo2`.
- **Live T5:** MN SONG THỦ **99–03** (ROI +18.7% / phụ +53.6%); MT **62–73** (+67.5% / +81.5%); MB **75–57** (+109% / +193%).
- An toàn: 4 bảng official hash IDENTICAL; health 200; board 401; private push f1ee754.

## 8. Phase B — Theo dõi P&L FORWARD 2-3 tuần (2026-06-18 21:45)

Owner: trộn-2-đầu +tiền nhưng không bền → GO dựng tracker. Verify **giá lô ĐÚNG: MB 27k, MN/MT 18k**.

- **Trộn-2-đầu KHÔNG bền** (56d chẻ cửa sổ 14d): ngày lỗ > ngày lãi cả 3 miền; dấu đảo +/−/+/−; MN +tiền chủ yếu do ADAPTIVE leakage ảo + cửa sổ may; MB cả 56d thực ra −1.85M.
- Dựng `pnl_forward_track_shadow` + `/api/admin/pnl-forward-track` + panel + **cron 22:30**. 6 chiến lược, 50 điểm, giá lô đúng, cờ leakage + max chuỗi lỗ.
- **Readout 22d:** EV-gate +30M / max chuỗi lỗ 3 / sạch = **tốt nhất**; Song-thủ-LANE +50.3M nhưng **leakage ảo + forward −3.7M**; 1 số −17.9M; Best-flow max chuỗi lỗ 12.
- Khuyến nghị: **KHÔNG đổi board theo trộn-2-đầu**; theo dõi cột forward 2-3 tuần.
- An toàn: 4 bảng official hash IDENTICAL; health 200; pnl 401; SHADOW; private push d0f018b.

## 9. Next

- Theo dõi cột "forward" 2-3 tuần (từ 18/06). EV-gate đang dẫn (rủi ro thấp nhất).
- Sau 2-3 tuần đủ mẫu forward sạch → mới quyết promote chiến lược nào.
