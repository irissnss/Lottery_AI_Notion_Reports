# V10674 — Thực Nghiệm Đo Lại Độ Mạnh Rules Trên DB Hiện Tại (Re-Measurement)

> **Generated**: 2026-06-02 13:40 VN
> **Trigger**: Owner — "các rules đã verify tới hiện tại có rule nào thay đổi độ mạnh / tăng trưởng / bổ sung / vướng các bug mốc trước-sau miền hoặc ngày Day? Thực nghiệm kiểm tra + tổng hợp đầy đủ."
> **Phương pháp**: Chạy LẠI đúng công thức đo của V10636-CROSS (hit = nguồn ∩ đích ≠ ∅; lift = rate − baseline) trên **DB vừa sync từ VPS**, gắn cờ temporal, đối chiếu 28 rule đã đăng ký + đo xu hướng theo thời gian (nửa đầu vs nửa sau) + dò rule mới.
> **DB max date**: 2026-06-01 · **Registry built**: 2026-06-02 00:27.

---

## 0. TL;DR — trả lời 4 câu hỏi của anh

| Câu hỏi của anh | Trả lời thực nghiệm |
|---|---|
| **Có rule nào thay đổi độ mạnh (so với lúc đăng ký)?** | ❌ KHÔNG — cả **28/28 STABLE, Δ=0.00pp**. Vì DB chưa có data mới sau mốc (max 01/06; 02/06 chưa xổ). Tái hiện **100%** → đáng tin về reproducibility. |
| **Có rule nào tăng trưởng?** | ✅ CÓ (xu hướng theo thời gian): **12 rule STRENGTHENING** (nửa sau mạnh hơn nửa đầu), 8 ổn định, **8 WEAKENING**. |
| **Có rule nào bổ sung?** | 🟡 Ngoài 28 top đã đăng ký, có **155 cell khác cũng đạt cùng ngưỡng** (BH + p<0.01 + lift≥8pp + n≥100, temporal-clean) — pool dự phòng (đa số cùng họ, cần lọc trùng). |
| **Có rule nào vướng bug temporal/ngày?** | ❌ KHÔNG — **0/28** vướng. 266 cell vi phạm thứ tự xổ vẫn bị loại đúng (gồm cái mạnh nhất +16.68pp). |

→ **Tập 28 rule forward-audit sạch + tái hiện chính xác.** Chưa có thay đổi vs mốc đăng ký (đợi data sau 02/06); nhưng xét lịch sử thì 12 rule đang mạnh lên, 8 đang yếu đi (cần theo dõi).

---

## 1. Bối cảnh — vì sao "chưa đổi" là đúng

- Registry 28 rule lập **02/06 00:27** từ data đến **01/06**. DB sync lại lúc 12:20 hôm nay vẫn max **01/06** (02/06 các đài xổ 16:10+ → chưa có).
- ⇒ Đo lại trên cùng tập data → lift y hệt từng số lẻ. Đây là **bằng chứng reproducibility** (không phải vô nghĩa): xác nhận script + registry khớp tuyệt đối.
- **Forward audit 90 ngày CHƯA bắt đầu tích lũy** ngày out-of-sample (anchor = hôm nay). Muốn thấy "tăng/giảm thật so với đăng ký" phải đợi data **sau 02/06** (mid-audit 02/07, closeout 31/08).

---

## 2. Đối chiếu 28 rule: lift gốc vs lift đo lại (toàn bộ STABLE)

| # | Rule | Lift gốc | Lift đo lại | Δ | Temporal |
|---|---|---|---|---|---|
| Tất cả 28 | (xem mục 3) | = | = | **+0.00** | ✅ 0 vi phạm |

→ Không một rule nào lệch dù 0.01pp. `days_evaluated` cũng không đổi. **Tập verified ổn định tuyệt đối trên data hiện có.**

---

## 3. Xu hướng theo thời gian (nửa đầu vs nửa sau lịch sử) — tín hiệu "tăng trưởng" thật

Đây là cách đo "độ mạnh có đang tăng/giảm" mà KHÔNG cần đợi data mới: chia đôi chuỗi lịch sử của mỗi rule.

### 3.1. 🟢 12 rule ĐANG MẠNH LÊN (STRENGTHENING — nửa sau > nửa đầu ≥ +2pp)

| Rule | Nửa đầu | Nửa sau | Recent-60 | Ghi chú |
|---|---|---|---|---|
| MB:G2#2:D-1→(MN,T7) | 4.4 | **21.6** | 12.2 | tăng mạnh nhất |
| MT:G7#1:D-3→(MT,T5) | 5.2 | **20.5** | 15.9 | |
| MT:G2#1:D-2→(MT,T5) | 9.2 | **20.5** | 20.9 | top rule, recent rất mạnh |
| MT:G5#1:D-1→(MT,T5) | 7.4 | **18.3** | 16.2 | |
| MT:G5#1:D-3→(MT,T7) | 8.0 | **16.4** | 19.5 | |
| MB:G6#3:D-3→(MT,T7) | 10.4 | 15.9 | 17.9 | |
| MT:G8#1:D-1→(MT,T7) | 8.8 | 15.0 | 18.9 | |
| MB:G6#1:D-2→(MN,T7) | 9.3 | 14.8 | 12.2 | |
| MB:G2#1:D-3→(MT,T5) | 11.3 | 14.7 | 16.2 | |
| MT:G5#1:D-2→(MT,T7) | 12.3 | 14.4 | 21.1 | |
| MT:DB#1:D-3→(MT,T7) | 10.5 | 14.3 | 7.2 | recent yếu hơn |
| MN:G8#1:D-3→(MT,T7)* | 11.7 | 13.2 | 14.7 | (gần ngưỡng) |

### 3.2. 🟡 8 rule ỔN ĐỊNH theo thời gian (chênh < 2pp)

MB:G4#2:D-1→(MT,T5) · MT:G2#1:D-2→(MT,T7) · MN:G3#2:D-3→(MT,T5) · MT:DB#1:D-2→(MT,T7) · MB:G1#1:D-3→(MN,T7) · MB:G6#1:D-1→(MT,T5) · MB:G7#1:D-3→(MT,T5)† · MN:G8#1:D-3→(MT,T7)

### 3.3. 🔴 8 rule ĐANG YẾU ĐI (WEAKENING — nửa sau < nửa đầu ≥ −2pp)

| Rule | Nửa đầu | Nửa sau | Recent-60 | Cảnh báo |
|---|---|---|---|---|
| MB:G2#2:D-3→(MT,T7) | 18.4 | 8.0 | **2.9** | ⚠️ recent rất yếu |
| MN:G8#1:D-1→(MT,T5) | 15.3 | 9.0 | **4.7** | ⚠️ recent yếu |
| MB:G4#2:D-3→(MT,T7) | 15.9 | 11.7 | 16.2 | recent hồi |
| MB:G1#1:D-2→(MT,T7) | 14.1 | 10.4 | 9.6 | |
| MN:G5#1:D→(MT,T5) | 15.1 | 12.6 | 11.3 | same-day MN→MT (hợp lệ) |
| MT:G1#1:D-1→(MT,T5) | 14.4 | 10.9 | 15.6 | recent hồi |
| MT:DB#1:D-1→(MT,T5) | 14.7 | 12.5 | 13.9 | |
| MB:DB#1:D-1→(MT,T7) | 13.5 | 10.4 | 12.9 | |

**⚠️ 3 rule cần theo dõi regime-shift** (recent-60 < 5pp dù lịch sử mạnh): `MB:G2#2:D-3→MT T7` (2.9), `MB:G7#1:D-3→MT T5` (2.9), `MN:G8#1:D-1→MT T5` (4.7). Đây là ứng viên dễ rớt khi forward-audit chạy.

---

## 4. Có rule nào "bổ sung"?

- Tập đăng ký = **top 28** (chọn theo lift cao nhất, cap 35 → trừ 7 temporal).
- Đo lại thấy tổng cộng **183 cell** đạt cùng ngưỡng (BH-pass + p<0.01 + lift≥8pp + n≥100, **temporal-clean**).
- ⇒ Còn **155 cell khác** nằm dưới cutoff top-28 (lift 8.0–11.9pp) — **pool bổ sung tiềm năng**.
- **Lưu ý trung thực**: 155 cell này **KHÔNG phải tín hiệu mới từ data mới** (data chưa đổi) mà là phần đuôi cùng phân phối chưa đăng ký vì cap top-35. Đa số là **biến thể cùng họ** (MT self-lag, đích T5/T7) → cần lọc trùng/độc lập trước khi mở rộng audit. Top vài cái: MN:G1#1:D-3→MT T5 (+11.91), MB:G2#1:D-2→MN T7 (+11.77), MT:G1#1:D-2→MT T7 (+11.70).
- **0 rule bị rớt** khỏi ngưỡng (dropped = 0).

---

## 5. Bug temporal/ngày (mốc trước-sau miền hoặc D/D-1) — kiểm lại bằng thực nghiệm

| Kiểm | Kết quả |
|---|---|
| 28 rule có rule nào vi phạm thứ tự xổ? | **0** ✅ |
| Tổng cell vi phạm trong grid (đo lại) | 266 (gồm 36 BH-pass) — **vẫn bị loại đúng** |
| Cell vi phạm mạnh nhất (đã loại) | `MB:G7#1:D → (MN,T7)` +16.68pp BH-pass → đúng là cái owner từng thấy, MB xổ SAU MN cùng ngày = data tương lai |
| Lag dùng trong 28 rule | D-1/D-2/D-3 (hợp lệ) + vài same-day **MN→MT** (MN xổ trước MT, hợp lệ) |

→ Việc đo lại (chạy độc lập trên DB mới) **tái xác nhận**: tập 28 hoàn toàn sạch temporal; bug chỉ ở các cell đã loại.

---

## 6. Kết luận cho anh

1. ✅ **Chưa có rule nào đổi độ mạnh so với lúc đăng ký** — vì DB chưa có data mới sau mốc (forward-audit chưa chạy ngày nào). Đo lại tái hiện **100%** → registry chuẩn xác.
2. 🟢 **Xét lịch sử: 12 rule đang mạnh lên, 8 ổn định, 8 yếu đi.** 3 rule recent-60 rất yếu (<5pp) → ứng viên dễ rớt, cần theo dõi.
3. 🟡 **Bổ sung**: có 155 cell khác đạt ngưỡng (pool dự phòng) — chưa đăng ký vì cap top-28; KHÔNG phải tín hiệu mới, đa số cùng họ.
4. ✅ **0/28 vướng bug temporal/ngày.** 266 cell vi phạm vẫn loại đúng.
5. ⏳ **Bước kế**: forward-audit thật bắt đầu khi có data **sau 02/06**; mid-audit 02/07, closeout 31/08 — lúc đó mới đo được "thay đổi vs đăng ký" trên data out-of-sample.

> **Một câu cho anh:** Tập rule đã verify **đứng vững và sạch** trên data hiện có (28/28 tái hiện chính xác, 0 vướng bug mốc miền/ngày). Chưa có data mới để nói "tăng/giảm so với đăng ký", nhưng xét lịch sử thì **12 rule đang lên, 8 đang xuống** — em đã đánh dấu 3 cái yếu nhất gần đây để canh khi audit 90 ngày chạy.

---

**Dữ liệu máy đọc**: `machine_readable/V10674_REMEASURE_FORWARD_AUDIT.json` (đối chiếu từng rule + timeline + 155 pool + 266 cell vi phạm).
**Script tái lập**: `scripts/_remeasure_forward_audit_current_db.py`.

**STATUS**: V10674 RE-MEASUREMENT — 28/28 reproducible (Δ=0), 0 temporal violations, time-trend 12↑/8=/8↓, 155 supplementary pool, 266 violations still excluded. DB max 2026-06-01 (forward-audit pending post-anchor data).
