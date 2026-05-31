# V10642 — Kiến trúc PER-SLICE: nhãn sức khỏe realtime (P1) + config độc lập (P2)

**Ngày:** 2026-05-31. **Chain:** … → V10640 → V10641 → **V10642**. **Backup:** đã chụp DB nhất quán (integrity ok) + file official + git HEAD trước khi làm.

Mục tiêu (owner): mọi thứ ĐỘC LẬP theo miền×thứ×đài (chỉnh 1 lát không ảnh hưởng lát khác); lát yếu VẪN chạy nhưng có NHÃN + cảnh báo realtime (cập nhật thường xuyên); cắt model AI vô-edge để đỡ đốt token; total-output sau cắt phải rõ.

---

## 🆕 CẬP NHẬT V10642B — nhãn tới cấp ĐÀI + đo tiến bộ model (giảm≠tắt) [đã LIVE]

Owner phản hồi: nhãn phải tới **từng ĐÀI** realtime (đừng chỉ T7/CN); ta đang **GIẢM chứ chưa TẮT HẲN**; làm sao **đo model bị giảm có tiến bộ tương lai**. 3 việc đã làm (đều shadow, official KHÔNG đổi):

**(A) Nhãn per-ĐÀI** (region×thứ×đài). Sự thật về dữ liệu: BT là per-MIỀN, verify trên GỘP các đài → base miền ~42% bị "ảo" cao; chơi 1 đài thì base thật ~16-18% (MN/MT), ~23% (MB). Tính lại: BT miền có rơi vào tails của ĐÀI đó không, so với base của đài. → **67 dòng** (per-đài + rollup ALL). Lộ ra điều nhãn miền che giấu:
- **MN CN**: gộp=STRONG(67%) nhưng **Kiên Giang=WEAK(0%)**, Tiền Giang=WATCH, **Đà Lạt=STRONG(50%)**.
- **MT T5**: gộp=STRONG nhưng Bình Định/Quảng Bình=WEAK, chỉ **Quảng Trị=STRONG**.

**(B) Đo tiến bộ model** — bảng `model_progress` (138 dòng, cron 09:05). Mỗi (miền×model): top1 hit 30 ngày gần vs 30 ngày trước (xu hướng) vs nền, cờ "đã giảm", trạng thái KEEP/RECOVERING/REDUCED_WATCHING/WATCH_CUT. **Phát hiện:** vài model trong danh sách giảm đang **HỒI PHỤC** → MT gpt-5-mini (41% > nền 35%, +14.7pp), gpt-5.5 (+37.9pp), gpt-oss-120b (+26.7pp). ⇒ danh sách cắt tĩnh 90 ngày đã cũ; **bắt buộc giảm + tiếp tục đo, không tắt hẳn**.

**(C) Semantic GIẢM≠TẮT**: slice_policy `mode='REDUCE'` (loại khỏi vote official, KHÔNG ngừng chạy). Model bị giảm vẫn chạy + được chấm điểm → BẬT LẠI khi RECOVERING. enabled=0 (chưa wire official).

**(D) UI**: thêm `GET /api/model-progress` (read-only). `/du-doan` + `/du-doan-test` hiện **pill theo từng ĐÀI hôm nay** + gộp miền. `/monitoring`: panel per-đài + panel "Tiến bộ model (GIẢM≠TẮT)" (refresh 60s). Deploy git `d49068a` 3-way, service active, 2 endpoint verified.

## ✅ P1 — Nhãn sức khỏe REALTIME per (miền×thứ) [SHADOW, an toàn, đã LIVE]
Bảng `slice_health` + materializer (cron mỗi ngày 09:00): mỗi lát tính **rolling hit-rate (6 lần gần nhất của thứ đó) vs BASE-RATE** → nhãn:
- 🟢 STRONG (≥ base+8pp) · 🟡 WATCH · 🔴 WEAK (< base = dưới ngẫu nhiên → "cân nhắc KHÔNG chơi").
- Tự cập nhật mỗi ngày (rolling → "tuần này tốt/xấu" tự đổi). Lát yếu **vẫn chạy ra số**, chỉ gắn nhãn.

Nhãn hiện tại (khớp audit V10641): **MT T7/CN = WEAK**, MN T4/T6/T7 = WEAK, MN CN/T2/T3 = STRONG, MT T3/T4/T5 = STRONG, MB hầu hết WEAK.

## ✅ P2 — Config ĐỘC LẬP per-slice [đã tạo, CHƯA wire official = reversible]
Bảng `slice_policy(region, weekday, selector, blocked_models, enabled, reason)`. Mỗi lát chỉnh RIÊNG, không đụng lát khác. Đã nạp danh sách cắt **data-driven** (AI-token, n≥30, hit90 < base-rate của lát):
| Miền | base | CẮT (AI-token dưới ngẫu nhiên) | selector |
|---|:---:|---|---|
| MN | 42% | chỉ **gpt-5-mini** (MN AI-token hầu hết TRÊN base → giữ) | specialist |
| MT | 33% | **8**: gpt-5-mini, kimi-k2.5, gpt-5.5, grok-4.20, gpt-oss-120b, qwen3-coder, deepseek-v4-pro, qwen3.6-plus | no_token_combo_main |
| MB | 24% | **10**: deepseek-reasoner, grok-4.20, gpt-5-mini, qwen3-coder, gpt-oss-120b, gemini-2.5-pro, gemini-2.5-flash, deepseek-v4-pro, qwen3-max-thinking, kimi-k2.5 | vote_sum |

`enabled=0` → **chưa áp vào official** (config SSOT + nền độc lập; official KHÔNG đổi tới khi wire + bật từng lát).

## TOTAL OUTPUT sau cắt (đã trả lời)
BT tính lại từ model CÒN LẠI của lát. **MT:** BT vốn đã bỏ AI-token qua override → cắt = **tiết kiệm token, BT không đổi**. **MB:** ~trung tính (gần ngẫu nhiên). Không đổi số official phiên này.

## ✅ P4 — UI nhãn cảnh báo realtime [đã LIVE, owner chọn làm P4 trước cho an toàn]
- Endpoint read-only `GET /api/slice-health` (defensive: lỗi/thiếu bảng → ẩn badge, không bao giờ throw/mutate, không provider/ví).
- **`/du-doan`** (trang chính): badge dưới tên miền, đúng (miền hiện tại × thứ hôm nay). VD: 🔴 T7: YẾU · trúng gần đây 33% (nền 51%) · cân nhắc không chơi.
- **`/du-doan-test`**: badge dưới header.
- **`/monitoring`**: bảng đầy đủ miền×thứ + auto-refresh 60s.
- Deploy qua git (HEAD `5fc8e54`, 3-way nhất quán) + restart service (active, /login 200, endpoint trả nhãn OK). Lát YẾU vẫn chạy, chỉ hiện cảnh báo.

## ⏳ P3 — bước kế (owner hoãn tới khi xem nhãn live vài ngày; đụng LIVE tiền/provider → không rush)
wire `slice_policy` vào đường GỌI model → bỏ gọi model bị block per-slice = **tiết kiệm token thật** (cần validate no-lookahead per-slice + cờ reversible). Nguyên tắc: careful, backup + validate + reversible từng bước.

*Public-safe: không chứa code private / DB rows / API keys / VPS internals. Tên model là công khai.*
