# V10640 — MN per-slice BT override vào OFFICIAL (reversible) + honest re-assessment

**Ngày:** 2026-05-30 (tối) · **Chain:** ... → V106.38-R8G → **V10640**
**Public push:** owner requested for cross-AI analysis.

> ⚠ **Đây là gói ĐẦU TIÊN có thay đổi production** (mọi gói trước = "0 production change").
> Thay đổi: **reversible** (1 cờ tắt được tức thì), backtest-justified, **CHƯA** chứng minh live.
> **KHÔNG** claim `OFFICIAL_IMPROVED` / `MN_FIXED` — chỉ backtest no-lookahead +5.4pp, **chờ forward**.

---

## 0. Bối cảnh
Owner yêu cầu cải thiện chất lượng dự đoán + thành thật, sau khi nhiều phiên trước "đo nhưng không áp vào official" (0 production change). Phiên này: re-assess trung thực toàn bộ + áp đúng 1 edge đã qua cổng kiểm tra nghiêm.

## 1. Sự thật về bài toán (xác nhận audit 91 ngày)
- Xổ số phần lớn **gần ngẫu nhiên**; "win ~44%" near-random cho MN/MB → **không** kỳ vọng đột phá lớn từ bất kỳ method/AI nào.
- Edge thật đều **NHỎ + mẫu nhỏ**. AI-token models: **không** edge cho độ chính xác BT.
- Gốc loạn (đã biết từ lâu, **chưa từng đưa vào official**): models là chuyên gia theo **thứ/đài**, nhưng weighting **region-global**.

## 2. Tự đính chính (minh bạch)
Trong phiên có 2 lần phóng đại — đã sửa:
- "lane thắng official +8~16pp" → thực ra **trộn nhiều experiment + artifact**; edge sạch chỉ **+2.5~7.7pp**.
- "oracle 90-100% = dư địa selection khổng lồ" → oracle là **HẬU NGHIỆM** (nhiều model đoán tản mạn, 1 cái trúng do may); ex-ante **không** chọn được tin cậy.

## 3. Bản đồ "chảy máu tiền" theo THỨ (official, 90 ngày)
| Miền | Thứ yếu (thắng thấp) | Thứ mạnh (giữ nguyên) |
|---|---|---|
| MN | T4 ~23%, T6 ~31%, T7 ~31% | CN/T2/T3 ~62% |
| MT | T6 ~23%, T2 ~31% | T5 ~77% |
| MB | yếu đều ~15-31% | (không có lát mạnh) |

## 4. Cổng kiểm tra NO-LOOKAHEAD (91 ngày) — chỉ MN qua
So sánh "đổi cách chọn BT" vs official, specialists tính **strict date < today** (không lookahead):

| Miền | Chooser | Official | Override | Δ | Ghi chú |
|---|---|---|---|---|---|
| **MN** | specialist roster | 45.1% | **50.5%** | **+5.4pp** | net +5; chỉ override ~13/91 ngày (thận trọng) → **ĐẠT** |
| MT | ai_chain | 45.1% | 41.8% | −3.3pp | override 64/91, tệ hơn → **RỚT** |
| MT | no_token_herd | 45.1% | 47.3% | +2.2pp | net +2 → nhiễu |
| MB | specialist | 24.2% | 25.3% | +1.1pp | net +1 → nhiễu |

→ Cổng này **chặn được** việc promote nhầm MT/ai_chain (sẽ làm official TỆ hơn).

## 5. Đã triển khai: V10640 (reversible, MN only)
- Override BT official cho **MN** dùng "specialist roster" (model có hit-rate ≥35% trong 60 ngày gần, tính no-lookahead), tái dùng đúng hàm chooser của lane (single source of truth).
- **Defensive:** mọi lỗi/empty → giữ official top1 (không bao giờ crash).
- **Reversible:** 1 cờ per-miền (MN ON, MT/MB OFF).
- Deploy có backup → compile → **dry-run verify trước restart** → restart → health 200 → rollback-ready. Verify: 6 ngày MN gần nhất override = top1 (đồng thuận, không phá); MT/MB = disabled.
- **Lane v2 (per-miền)**: phát hiện **half-baked** (commit nhưng chưa deploy + import vỡ) → đã sửa import + chạy như **challenger so sánh** (đo: KHÔNG hơn official → không promote).

## 6. Tồn đọng (chưa làm, sequence riêng — tránh chồng thay đổi)
1. Monitor MN override 10-14 ngày live; rollback nếu xấu.
2. Refresh rule set (đông cứng ~26 ngày).
3. MB AI freeze/limit (data ủng hộ vì AI-token vô dụng → tiết kiệm token).
4. 3-way gap: 1 dependency runtime còn untracked (consistency risk).
5. MT/MB override: re-test khi đủ forward data.

## 7. Câu hỏi cho các AI khác phân tích giúp owner
- Với domain gần-ngẫu-nhiên + edge nhỏ: cách chọn BT **per-(miền×thứ)** nào tối ưu hơn "specialist roster"? Có nên ensemble + shrinkage thay vì single-best?
- MB official rất thấp (~10-19% gần đây) dù trần oracle ~90% (hậu nghiệm): có selector ex-ante nào khai thác được phần này một cách **bền** (out-of-sample)?
- Tiêu chí dừng/đảo ngược MN override sau bao nhiêu ngày live + ngưỡng nào là hợp lý thống kê (mẫu nhỏ)?

---
*Public-safe: không chứa private code, DB rows, API keys, hay VPS internals. Số liệu là thống kê tổng hợp từ backtest read-only.*
