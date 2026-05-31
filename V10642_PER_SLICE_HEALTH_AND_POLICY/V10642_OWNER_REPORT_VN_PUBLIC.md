# V10642 — Kiến trúc PER-SLICE: nhãn sức khỏe realtime (P1) + config độc lập (P2)

**Ngày:** 2026-05-31. **Chain:** … → V10640 → V10641 → **V10642**. **Backup:** đã chụp DB nhất quán (integrity ok) + file official + git HEAD trước khi làm.

Mục tiêu (owner): mọi thứ ĐỘC LẬP theo miền×thứ×đài (chỉnh 1 lát không ảnh hưởng lát khác); lát yếu VẪN chạy nhưng có NHÃN + cảnh báo realtime (cập nhật thường xuyên); cắt model AI vô-edge để đỡ đốt token; total-output sau cắt phải rõ.

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
