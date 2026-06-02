# V10675 — Bảng Tổng Hợp TOÀN BỘ Rules + Nhãn Trạng Thái (Master Labeled)

> **Generated**: 2026-06-02T13:48:22 (sinh tự động từ dữ liệu — không bỏ sót)
> **Trigger**: Owner — "tổng hợp tổng lực đầy đủ chi tiết, không bỏ sót rule nào, gắn nhãn mạnh lên / yếu xuống / tình trạng".
> **DB**: tới 2026-06-01 (đã sync VPS). Đo bằng đúng method V10636-CROSS.

---

## 0. Chú thích nhãn (label legend)

| Nhãn | Ý nghĩa |
|---|---|
| 🟢 **mạnh lên** | Lift nửa sau ≥ nửa đầu **+2pp** (STRENGTHENING) |
| 🟡 **ổn định** | Chênh nửa đầu/sau **< 2pp** (STABLE_OVER_TIME) |
| 🔴 **yếu đi** | Lift nửa sau ≤ nửa đầu **−2pp** (WEAKENING) |
| ⚠️ | **recent-60 < 5pp** — cần canh regime shift (dễ rớt khi audit chạy) |
| **REGISTERED** | Trong tập 28 rule forward-audit 90 ngày |
| **POOL** | Đạt ngưỡng (BH+p<0.01+lift≥8pp+n≥100, temporal-clean) nhưng dưới cutoff top-28 |
| **EXCLUDED** | Vi phạm thứ tự xổ (same-day nguồn xổ sau đích) — đã loại |

**Cách đọc lineage**: `Nguồn:Giải#Bộ:Lag → (Đích, Thứ)`. Ví dụ `MT:G2#1:D-2→(MT,T7)` = đích MT thứ Bảy, lấy LAST2 giải nhì bộ 1 của MT cách 2 ngày.

---

## 1. Tổng quan (toàn bộ 183 rule đạt ngưỡng + 266 bị loại)

| Nhóm | Số lượng | Ghi chú |
|---|---|---|
| ✅ **REGISTERED (forward-audit)** | 28 | đang audit 90 ngày, chưa live |
| 🟡 **SUPPLEMENTARY POOL** | 155 | dự phòng, dưới cutoff |
| **— Tổng qualifying** | **183** | temporal-clean |
| ❌ **EXCLUDED temporal** | 266 | đã loại (mốc miền sai) |

**Phân bố nhãn trạng thái (trên 183 rule):**

| Nhãn | Số rule |
|---|---|
| 🟢 mạnh lên | 69 |
| 🟡 ổn định | 56 |
| 🔴 yếu đi | 58 |
| ⚠️ cần canh (recent<5pp) | 39 |

> Lưu ý: "vs lúc đăng ký" = **không đổi** (28/28 Δ=0) vì DB chưa có data sau mốc 02/06. Nhãn mạnh/yếu dưới đây đo theo **xu hướng lịch sử** (nửa đầu vs nửa sau) — cách duy nhất thấy được "đang lên hay xuống" trước khi audit 90 ngày tích lũy data.

---

## 2. ✅ 28 RULE FORWARD-AUDIT (đã đăng ký) — gắn nhãn từng cái

| Rule (nguồn:giải:lag→đích,thứ) | Lift | Hit% | Nửa đầu | Nửa sau | Recent-60 | Nhãn trạng thái |
|---|---|---|---|---|---|---|
| MT:G2#1:D-2->(MT,T7) | 15.5 | 86.3% | 15.1 | 16.0 | 22.4 | 🟡 ổn định |
| MT:G2#1:D-2->(MT,T5) | 14.8 | 70.6% | 9.2 | 20.5 | 20.9 | 🟢 mạnh lên |
| MB:G4#2:D-1->(MT,T5) | 14.4 | 48.2% | 13.8 | 15.0 | 14.6 | 🟡 ổn định |
| MN:G5#1:D->(MT,T5) | 13.8 | 84.3% | 15.1 | 12.6 | 11.3 | 🔴 yếu đi |
| MB:G4#2:D-3->(MT,T7) | 13.8 | 47.5% | 15.9 | 11.7 | 16.2 | 🔴 yếu đi |
| MT:DB#1:D-1->(MT,T5) | 13.6 | 69.6% | 14.7 | 12.5 | 13.9 | 🔴 yếu đi |
| MT:G5#1:D-2->(MT,T7) | 13.4 | 83.9% | 12.3 | 14.4 | 21.1 | 🟢 mạnh lên |
| MB:G1#1:D-3->(MN,T7) | 13.3 | 56.1% | 13.6 | 13.0 | 8.8 | 🟡 ổn định |
| MB:G2#2:D-3->(MT,T7) | 13.2 | 46.9% | 18.4 | 8.0 | 2.9 | 🔴 yếu đi ⚠️ |
| MB:G6#3:D-3->(MT,T7) | 13.2 | 46.9% | 10.4 | 15.9 | 17.9 | 🟢 mạnh lên |
| MN:G3#2:D-3->(MT,T5) | 13.2 | 83.3% | 12.9 | 13.5 | 15.7 | 🟡 ổn định |
| MB:G2#1:D-3->(MT,T5) | 13.0 | 46.8% | 11.3 | 14.7 | 16.2 | 🟢 mạnh lên |
| MB:G2#2:D-1->(MN,T7) | 13.0 | 55.8% | 4.4 | 21.6 | 12.2 | 🟢 mạnh lên |
| MT:G7#1:D-3->(MT,T5) | 12.8 | 68.7% | 5.2 | 20.5 | 15.9 | 🟢 mạnh lên |
| MT:G5#1:D-1->(MT,T5) | 12.8 | 68.4% | 7.4 | 18.3 | 16.2 | 🟢 mạnh lên |
| MT:G1#1:D-1->(MT,T5) | 12.7 | 68.4% | 14.4 | 10.9 | 15.6 | 🔴 yếu đi |
| MN:G8#1:D-3->(MT,T7) | 12.4 | 82.4% | 11.7 | 13.2 | 14.7 | 🟡 ổn định |
| MT:DB#1:D-3->(MT,T7) | 12.4 | 68.4% | 10.5 | 14.3 | 7.2 | 🟢 mạnh lên |
| MT:G5#1:D-2->(MT,T5) | 12.3 | 68.2% | 8.9 | 15.6 | 22.2 | 🟢 mạnh lên |
| MB:G1#1:D-2->(MT,T7) | 12.3 | 46.0% | 14.1 | 10.4 | 9.6 | 🔴 yếu đi |
| MT:G5#1:D-3->(MT,T7) | 12.2 | 67.8% | 8.0 | 16.4 | 19.5 | 🟢 mạnh lên |
| MN:G8#1:D-1->(MT,T5) | 12.1 | 82.1% | 15.3 | 9.0 | 4.7 | 🔴 yếu đi ⚠️ |
| MB:G7#1:D-3->(MT,T5) | 12.1 | 45.9% | 11.3 | 12.9 | 2.9 | 🟡 ổn định ⚠️ |
| MB:G6#1:D-2->(MN,T7) | 12.1 | 54.9% | 9.3 | 14.8 | 12.2 | 🟢 mạnh lên |
| MT:DB#1:D-2->(MT,T7) | 12.0 | 82.7% | 11.1 | 13.0 | 15.9 | 🟡 ổn định |
| MB:G6#1:D-1->(MT,T5) | 12.0 | 45.7% | 12.6 | 11.4 | 11.2 | 🟡 ổn định |
| MB:DB#1:D-1->(MT,T7) | 11.9 | 45.7% | 13.5 | 10.4 | 12.9 | 🔴 yếu đi |
| MT:G8#1:D-1->(MT,T7) | 11.9 | 67.9% | 8.8 | 15.0 | 18.9 | 🟢 mạnh lên |

---

## 3. 🟡 155 RULE POOL DỰ PHÒNG (đạt ngưỡng, chưa đăng ký) — gắn nhãn đầy đủ

> Đây là phần đuôi cùng phân phối (lift 8–11.9pp), đa số cùng họ (MT self-lag, đích T5/T7). Liệt kê đầy đủ để **không bỏ sót**.

### 3.1. 🟢 Mạnh lên (57 rule)

| Rule (nguồn:giải:lag→đích,thứ) | Lift | Hit% | Nửa đầu | Nửa sau | Recent-60 | Nhãn trạng thái |
|---|---|---|---|---|---|---|
| MB:G4#3:D-2->(MN,T7) | 11.2 | 54.0% | 9.3 | 13.0 | 10.5 | 🟢 mạnh lên |
| MN:DB#1:D-1->(MT,T5) | 11.0 | 81.2% | 9.2 | 12.9 | 5.9 | 🟢 mạnh lên |
| MT:G1#1:D-3->(MN,T7) | 10.9 | 77.8% | 8.7 | 13.0 | 7.7 | 🟢 mạnh lên |
| MB:G4#2:D-3->(MT,T5) | 10.9 | 44.6% | 5.1 | 16.6 | 19.6 | 🟢 mạnh lên |
| MN:G3#2:D-2->(MT,T7) | 10.8 | 81.5% | 9.2 | 12.5 | 14.3 | 🟢 mạnh lên |
| MT:G7#1:D-1->(MT,T5) | 10.7 | 66.6% | 9.5 | 12.0 | 8.9 | 🟢 mạnh lên |
| MT:G2#1:D-3->(MT,T5) | 10.7 | 66.6% | 9.3 | 12.1 | -4.1 | 🟢 mạnh lên ⚠️ |
| MB:G4#1:D-2->(MT,T5) | 10.7 | 44.5% | 8.0 | 13.5 | 14.6 | 🟢 mạnh lên |
| MB:DB#1:D-2->(MN,T7) | 10.7 | 53.5% | 9.6 | 11.8 | 8.8 | 🟢 mạnh lên |
| MT:G3#2:D-1->(MT,T5) | 10.7 | 66.6% | 3.8 | 17.6 | 14.2 | 🟢 mạnh lên |
| MB:DB#1:D-1->(MN,T7) | 10.5 | 53.4% | 3.2 | 17.9 | 28.8 | 🟢 mạnh lên |
| MN:G2#1:D-2->(MT,T7) | 10.5 | 81.2% | 8.5 | 12.5 | 10.1 | 🟢 mạnh lên |
| MB:G4#1:D-1->(MT,T7) | 10.4 | 44.2% | 8.6 | 12.3 | 17.9 | 🟢 mạnh lên |
| MN:G7#1:D-2->(MT,T7) | 10.3 | 80.8% | 5.7 | 14.9 | 7.6 | 🟢 mạnh lên |
| MT:G5#1:D-3->(MT,T5) | 10.3 | 66.3% | 8.7 | 11.9 | 10.6 | 🟢 mạnh lên |
| MN:G1#1:D-1->(MT,T7) | 10.3 | 80.3% | 8.1 | 12.4 | 12.6 | 🟢 mạnh lên |
| MT:G7#1:D-2->(MT,T5) | 10.2 | 66.1% | 7.4 | 13.1 | 14.2 | 🟢 mạnh lên |
| MB:G6#2:D-1->(MT,T5) | 10.2 | 43.9% | 7.7 | 12.6 | 9.6 | 🟢 mạnh lên |
| MN:DB#1:D->(MT,T5) | 10.1 | 80.7% | 8.3 | 11.8 | 9.3 | 🟢 mạnh lên |
| MB:G2#2:D-3->(MN,T7) | 9.9 | 52.8% | 8.7 | 11.2 | 10.5 | 🟢 mạnh lên |
| MT:G8#1:D-3->(MT,T5) | 9.9 | 65.7% | 7.0 | 12.7 | 14.2 | 🟢 mạnh lên |
| MN:DB#1:D-2->(MN,T7) | 9.8 | 90.9% | 8.6 | 11.0 | 10.5 | 🟢 mạnh lên |
| MT:DB#1:D-1->(MT,T7) | 9.7 | 65.5% | 6.6 | 12.7 | 14.5 | 🟢 mạnh lên |
| MN:G1#1:D->(MT,T5) | 9.6 | 80.1% | 6.6 | 12.6 | 7.6 | 🟢 mạnh lên |
| MB:G7#1:D-3->(MT,T7) | 9.5 | 43.2% | 7.3 | 11.7 | 2.9 | 🟢 mạnh lên ⚠️ |
| MB:G2#1:D-1->(MN,T7) | 9.3 | 52.1% | 8.1 | 10.5 | 8.8 | 🟢 mạnh lên |
| MB:G4#4:D-2->(MN,T7) | 9.3 | 52.1% | 7.5 | 11.2 | 8.8 | 🟢 mạnh lên |
| MN:G7#1:D-3->(MT,T5) | 9.3 | 79.3% | 3.5 | 15.0 | 12.4 | 🟢 mạnh lên |
| MT:G1#1:D-1->(MT,T7) | 9.3 | 65.2% | 7.2 | 11.3 | 12.2 | 🟢 mạnh lên |
| MB:G4#1:D-1->(MT,T5) | 9.2 | 43.0% | 7.7 | 10.8 | 7.9 | 🟢 mạnh lên |
| MN:G3#1:D-3->(MT,T5) | 9.2 | 79.3% | 7.9 | 10.5 | 6.1 | 🟢 mạnh lên |
| MN:G7#1:D-1->(MT,T7) | 9.2 | 79.1% | 7.7 | 10.7 | 4.5 | 🟢 mạnh lên ⚠️ |
| MB:G4#2:D-1->(MN,T7) | 9.0 | 51.8% | 6.9 | 11.2 | 7.2 | 🟢 mạnh lên |
| MN:G3#1:D-1->(MT,T7) | 9.0 | 79.1% | 7.2 | 10.7 | 6.3 | 🟢 mạnh lên |
| MT:G7#1:D-3->(MN,T7) | 8.9 | 76.0% | 5.0 | 12.9 | 7.7 | 🟢 mạnh lên |
| MB:G4#4:D-2->(MT,T5) | 8.9 | 42.6% | 6.7 | 11.0 | 6.2 | 🟢 mạnh lên |
| MB:G7#1:D-1->(MT,T7) | 8.9 | 42.6% | 1.2 | 16.6 | 17.9 | 🟢 mạnh lên |
| MB:G7#4:D-3->(MT,T5) | 8.7 | 42.5% | 1.4 | 15.9 | 17.9 | 🟢 mạnh lên |
| MB:G1#1:D-2->(MN,T7) | 8.7 | 51.5% | 6.2 | 11.2 | 7.2 | 🟢 mạnh lên |
| MB:G6#3:D-2->(MN,T7) | 8.7 | 51.5% | 6.2 | 11.2 | 10.5 | 🟢 mạnh lên |
| MT:G1#1:D-2->(MT,T5) | 8.7 | 64.5% | 6.8 | 10.6 | 12.2 | 🟢 mạnh lên |
| MN:G3#2:D-2->(MN,T7) | 8.6 | 89.7% | 6.1 | 11.1 | 12.2 | 🟢 mạnh lên |
| MN:G2#1:D->(MT,T5) | 8.6 | 79.2% | 5.7 | 11.4 | 6.8 | 🟢 mạnh lên |
| MN:DB#1:D->(MB,T2) | 8.4 | 63.2% | 6.5 | 10.4 | 9.9 | 🟢 mạnh lên |
| MT:G3#2:D-3->(MT,T5) | 8.4 | 64.4% | 7.4 | 9.4 | 12.2 | 🟢 mạnh lên |
| MB:G4#4:D-3->(MN,T7) | 8.4 | 51.2% | 6.2 | 10.5 | 12.2 | 🟢 mạnh lên |
| MB:G6#3:D-1->(MN,T7) | 8.4 | 51.2% | 2.0 | 14.8 | 0.5 | 🟢 mạnh lên ⚠️ |
| MB:G7#3:D-2->(MN,T7) | 8.4 | 51.2% | 6.2 | 10.5 | 13.8 | 🟢 mạnh lên |
| MB:G7#4:D-1->(MN,T7) | 8.4 | 51.2% | 3.8 | 13.0 | 8.8 | 🟢 mạnh lên |
| MT:G3#1:D-2->(MN,T7) | 8.4 | 89.4% | 5.7 | 11.0 | 12.2 | 🟢 mạnh lên |
| MN:G2#1:D-3->(MT,T5) | 8.3 | 78.4% | 5.4 | 11.2 | 9.3 | 🟢 mạnh lên |
| MB:G7#1:D-2->(MT,T7) | 8.3 | 42.0% | 6.1 | 10.4 | 7.9 | 🟢 mạnh lên |
| MT:G2#1:D-1->(MT,T7) | 8.2 | 64.2% | 5.7 | 10.8 | 9.2 | 🟢 mạnh lên |
| MN:G2#1:D-1->(MT,T7) | 8.2 | 78.2% | 5.3 | 11.2 | 13.0 | 🟢 mạnh lên |
| MT:DB#1:D-1->(MN,T5) | 8.2 | 75.4% | 4.8 | 11.6 | 9.3 | 🟢 mạnh lên |
| MT:G3#1:D-2->(MT,T7) | 8.2 | 78.7% | 6.4 | 9.9 | 7.6 | 🟢 mạnh lên |
| MB:G7#2:D-3->(MT,T5) | 8.1 | 41.9% | 6.4 | 9.8 | 12.9 | 🟢 mạnh lên |

### 3.2. 🟡 Ổn định (48 rule)

| Rule (nguồn:giải:lag→đích,thứ) | Lift | Hit% | Nửa đầu | Nửa sau | Recent-60 | Nhãn trạng thái |
|---|---|---|---|---|---|---|
| MB:G4#1:D-2->(MN,T7) | 11.8 | 54.6% | 11.8 | 11.8 | 7.2 | 🟡 ổn định |
| MN:G3#2:D->(MT,T5) | 11.6 | 82.2% | 11.2 | 12.0 | 7.6 | 🟡 ổn định |
| MT:G8#1:D-1->(MT,T5) | 11.5 | 67.5% | 12.3 | 10.8 | 5.9 | 🟡 ổn định |
| MN:G5#1:D-2->(MT,T5) | 11.4 | 81.5% | 12.3 | 10.4 | 12.6 | 🟡 ổn định |
| MN:G5#1:D-2->(MT,T7) | 11.0 | 81.5% | 10.0 | 11.9 | 6.3 | 🟡 ổn định |
| MB:G6#2:D-1->(MN,T7) | 10.8 | 53.7% | 11.8 | 9.9 | 8.8 | 🟡 ổn định |
| MT:G3#1:D-2->(MT,T5) | 10.8 | 66.7% | 10.3 | 11.4 | 13.9 | 🟡 ổn định |
| MN:G3#1:D-1->(MT,T5) | 10.8 | 80.8% | 10.4 | 11.2 | 6.1 | 🟡 ổn định |
| MT:G5#1:D-3->(MN,T7) | 10.8 | 77.5% | 10.8 | 10.7 | 15.0 | 🟡 ổn định |
| MT:G7#1:D-2->(MT,T7) | 10.7 | 80.8% | 9.7 | 11.6 | 18.0 | 🟡 ổn định |
| MB:G7#3:D-1->(MT,T7) | 10.4 | 44.2% | 9.8 | 11.0 | 4.6 | 🟡 ổn định ⚠️ |
| MT:G7#1:D-1->(MN,T7) | 10.4 | 77.6% | 11.1 | 9.7 | 12.7 | 🟡 ổn định |
| MN:G3#2:D->(MT,T7) | 10.2 | 90.0% | 10.3 | 10.1 | 8.1 | 🟡 ổn định |
| MB:G2#2:D-2->(MT,T7) | 10.1 | 43.9% | 9.2 | 11.0 | 9.6 | 🟡 ổn định |
| MB:G4#1:D-2->(MT,T7) | 10.1 | 43.9% | 9.2 | 11.0 | -7.1 | 🟡 ổn định ⚠️ |
| MB:G4#2:D-2->(MT,T5) | 10.1 | 43.9% | 9.8 | 10.4 | 7.9 | 🟡 ổn định |
| MT:G3#2:D-2->(MT,T7) | 10.1 | 80.5% | 9.9 | 10.3 | 4.5 | 🟡 ổn định ⚠️ |
| MN:G7#1:D-3->(MT,T7) | 10.1 | 80.2% | 10.2 | 9.9 | 10.7 | 🟡 ổn định |
| MN:G3#1:D->(MT,T5) | 10.0 | 80.4% | 9.6 | 10.4 | 4.5 | 🟡 ổn định ⚠️ |
| MB:G1#1:D-1->(MT,T7) | 9.8 | 43.6% | 9.2 | 10.4 | 7.9 | 🟡 ổn định |
| MN:G2#1:D-3->(MT,T7) | 9.8 | 79.9% | 10.6 | 8.9 | 4.9 | 🟡 ổn định ⚠️ |
| MN:G7#1:D-2->(MT,T5) | 9.7 | 79.7% | 9.3 | 10.0 | -0.7 | 🟡 ổn định ⚠️ |
| MN:DB#1:D-2->(MT,T7) | 9.6 | 80.2% | 9.9 | 9.3 | 5.9 | 🟡 ổn định |
| MB:G7#1:D-1->(MT,T5) | 9.5 | 43.3% | 10.2 | 8.9 | 1.2 | 🟡 ổn định ⚠️ |
| MT:G2#1:D-1->(MT,T5) | 9.5 | 65.3% | 9.0 | 10.1 | 10.6 | 🟡 ổn định |
| MB:G2#1:D-2->(MT,T7) | 9.5 | 43.2% | 9.2 | 9.8 | 14.6 | 🟡 ổn định |
| MB:G4#4:D-1->(MT,T7) | 9.5 | 43.2% | 10.4 | 8.6 | 6.2 | 🟡 ổn định |
| MB:G7#3:D-3->(MT,T5) | 9.3 | 43.1% | 10.1 | 8.6 | 6.2 | 🟡 ổn định |
| MN:DB#1:D-1->(MN,T7) | 9.1 | 89.7% | 9.6 | 8.6 | 7.2 | 🟡 ổn định |
| MT:DB#1:D-3->(MN,T7) | 9.1 | 76.3% | 9.6 | 8.6 | 2.7 | 🟡 ổn định ⚠️ |
| MB:G7#2:D-1->(MN,T7) | 9.0 | 51.8% | 9.9 | 8.1 | 3.8 | 🟡 ổn định ⚠️ |
| MN:G7#1:D->(MT,T7) | 9.0 | 88.8% | 9.7 | 8.3 | 4.5 | 🟡 ổn định ⚠️ |
| MN:G3#2:D-3->(MT,T7) | 8.9 | 79.0% | 9.7 | 8.2 | 0.7 | 🟡 ổn định ⚠️ |
| MN:DB#1:D-3->(MT,T7) | 8.9 | 79.0% | 9.2 | 8.7 | 12.6 | 🟡 ổn định |
| MB:G1#1:D-2->(MT,T5) | 8.9 | 42.6% | 9.8 | 8.0 | 12.9 | 🟡 ổn định |
| MN:G7#1:D-1->(MT,T5) | 8.8 | 79.0% | 8.4 | 9.3 | 10.7 | 🟡 ổn định |
| MT:G8#1:D-3->(MN,T7) | 8.8 | 76.0% | 9.0 | 8.7 | 6.3 | 🟡 ổn định |
| MN:DB#1:D-3->(MN,T7) | 8.8 | 89.4% | 9.0 | 8.6 | 7.2 | 🟡 ổn định |
| MN:DB#1:D-1->(MT,T7) | 8.7 | 78.8% | 8.6 | 8.8 | 7.6 | 🟡 ổn định |
| MB:G6#3:D-1->(MT,T5) | 8.6 | 42.4% | 8.9 | 8.3 | 12.9 | 🟡 ổn định |
| MB:G4#1:D-3->(MT,T7) | 8.6 | 42.3% | 8.6 | 8.6 | 14.6 | 🟡 ổn định |
| MB:G7#2:D-2->(MT,T7) | 8.6 | 42.3% | 9.2 | 8.0 | 9.6 | 🟡 ổn định |
| MT:DB#1:D-1->(MN,T7) | 8.5 | 75.5% | 8.8 | 8.2 | 8.3 | 🟡 ổn định |
| MN:G1#1:D-2->(MT,T5) | 8.3 | 78.2% | 7.8 | 8.9 | 10.1 | 🟡 ổn định |
| MN:G5#1:D-3->(MN,T7) | 8.3 | 89.1% | 8.2 | 8.5 | 10.5 | 🟡 ổn định |
| MB:G7#3:D-2->(MT,T7) | 8.3 | 42.0% | 8.0 | 8.6 | 2.9 | 🟡 ổn định ⚠️ |
| MB:G7#4:D-3->(MT,T7) | 8.3 | 42.0% | 9.2 | 7.3 | -2.1 | 🟡 ổn định ⚠️ |
| MT:G3#2:D-2->(MN,T7) | 8.2 | 89.1% | 7.4 | 8.9 | 9.0 | 🟡 ổn định |

### 3.3. 🔴 Yếu đi (50 rule)

| Rule (nguồn:giải:lag→đích,thứ) | Lift | Hit% | Nửa đầu | Nửa sau | Recent-60 | Nhãn trạng thái |
|---|---|---|---|---|---|---|
| MN:G1#1:D-3->(MT,T5) | 11.9 | 81.8% | 13.9 | 10.0 | 5.9 | 🔴 yếu đi |
| MB:G2#1:D-2->(MN,T7) | 11.8 | 54.6% | 13.6 | 9.9 | 20.5 | 🔴 yếu đi |
| MT:G1#1:D-2->(MT,T7) | 11.7 | 82.4% | 13.6 | 9.8 | 7.8 | 🔴 yếu đi |
| MT:G3#1:D-3->(MN,T7) | 11.6 | 78.7% | 14.7 | 8.6 | 7.7 | 🔴 yếu đi |
| MB:G7#3:D-1->(MN,T7) | 11.5 | 54.3% | 13.0 | 9.9 | 8.8 | 🔴 yếu đi |
| MT:G3#1:D-3->(MT,T7) | 11.3 | 67.2% | 14.9 | 7.6 | 12.2 | 🔴 yếu đi |
| MB:G1#1:D-3->(MT,T5) | 11.2 | 44.9% | 13.2 | 9.2 | 7.9 | 🔴 yếu đi |
| MB:G6#1:D-1->(MN,T7) | 11.2 | 54.0% | 15.4 | 6.9 | -2.8 | 🔴 yếu đi ⚠️ |
| MN:G2#1:D->(MT,T7) | 11.0 | 90.9% | 12.2 | 9.9 | 12.9 | 🔴 yếu đi |
| MN:G5#1:D-3->(MT,T7) | 10.9 | 81.2% | 12.0 | 9.8 | 5.9 | 🔴 yếu đi |
| MT:G3#2:D-2->(MT,T5) | 10.8 | 66.7% | 13.4 | 8.2 | 3.9 | 🔴 yếu đi ⚠️ |
| MT:G3#2:D-1->(MN,T7) | 10.8 | 77.9% | 12.3 | 9.3 | 14.7 | 🔴 yếu đi |
| MN:G3#1:D-2->(MT,T7) | 10.7 | 81.2% | 13.0 | 8.5 | 4.5 | 🔴 yếu đi ⚠️ |
| MT:G2#1:D-3->(MT,T7) | 10.7 | 66.6% | 12.0 | 9.4 | 12.2 | 🔴 yếu đi |
| MN:G1#1:D-2->(MT,T7) | 10.6 | 81.2% | 14.3 | 7.0 | 9.3 | 🔴 yếu đi |
| MT:DB#1:D-3->(MT,T5) | 10.6 | 66.6% | 13.0 | 8.1 | 3.9 | 🔴 yếu đi ⚠️ |
| MB:G7#2:D-2->(MN,T7) | 10.5 | 53.4% | 13.6 | 7.5 | -4.5 | 🔴 yếu đi ⚠️ |
| MT:G8#1:D-2->(MT,T7) | 10.2 | 80.8% | 11.8 | 8.8 | 9.5 | 🔴 yếu đi |
| MB:G6#3:D-3->(MN,T7) | 10.2 | 53.1% | 15.4 | 5.0 | 0.5 | 🔴 yếu đi ⚠️ |
| MT:DB#1:D-2->(MN,T7) | 9.8 | 90.9% | 11.0 | 8.6 | 10.5 | 🔴 yếu đi |
| MT:G7#1:D-1->(MT,T7) | 9.8 | 65.8% | 12.6 | 6.9 | 8.9 | 🔴 yếu đi |
| MN:G8#1:D-1->(MN,T7) | 9.7 | 90.3% | 10.8 | 8.6 | 3.7 | 🔴 yếu đi ⚠️ |
| MT:G8#1:D-3->(MT,T7) | 9.7 | 65.7% | 12.3 | 7.1 | 9.2 | 🔴 yếu đi |
| MN:G8#1:D-2->(MT,T7) | 9.7 | 80.2% | 11.0 | 8.4 | 11.6 | 🔴 yếu đi |
| MB:G7#4:D-1->(MT,T5) | 9.5 | 43.3% | 10.8 | 8.3 | 17.9 | 🔴 yếu đi |
| MN:G3#2:D-1->(MT,T5) | 9.5 | 79.6% | 13.9 | 5.1 | -0.9 | 🔴 yếu đi ⚠️ |
| MN:G3#2:D-1->(MT,T7) | 9.3 | 79.4% | 13.7 | 5.0 | 4.1 | 🔴 yếu đi ⚠️ |
| MN:G7#1:D->(MT,T5) | 9.3 | 79.8% | 11.4 | 7.2 | 7.6 | 🔴 yếu đi |
| MT:G8#1:D-2->(MT,T5) | 9.2 | 65.2% | 10.9 | 7.5 | 7.2 | 🔴 yếu đi |
| MT:G3#1:D-1->(MT,T5) | 9.2 | 65.0% | 10.7 | 7.6 | 3.9 | 🔴 yếu đi ⚠️ |
| MB:G4#3:D-3->(MT,T5) | 9.0 | 42.8% | 10.1 | 8.0 | 12.9 | 🔴 yếu đi |
| MB:G4#2:D-3->(MN,T7) | 9.0 | 51.8% | 11.2 | 6.9 | 13.8 | 🔴 yếu đi |
| MB:G6#1:D-2->(MT,T7) | 8.9 | 42.6% | 14.1 | 3.7 | 7.9 | 🔴 yếu đi |
| MN:DB#1:D-2->(MT,T5) | 8.7 | 78.5% | 11.0 | 6.4 | 2.8 | 🔴 yếu đi ⚠️ |
| MT:G3#2:D-1->(MT,T7) | 8.7 | 64.5% | 12.0 | 5.3 | 9.2 | 🔴 yếu đi |
| MB:G2#1:D-2->(MT,T5) | 8.6 | 42.3% | 10.4 | 6.7 | 4.6 | 🔴 yếu đi ⚠️ |
| MB:G4#3:D-3->(MT,T7) | 8.6 | 42.3% | 12.9 | 4.3 | 14.6 | 🔴 yếu đi |
| MN:G1#1:D-2->(MN,T7) | 8.4 | 89.4% | 9.9 | 6.9 | 8.9 | 🔴 yếu đi |
| MB:G6#1:D-3->(MT,T5) | 8.4 | 42.1% | 9.5 | 7.3 | 6.2 | 🔴 yếu đi |
| MB:G6#2:D-2->(MN,T7) | 8.4 | 51.2% | 13.6 | 3.2 | 0.5 | 🔴 yếu đi ⚠️ |
| MB:G7#2:D-3->(MN,T7) | 8.4 | 51.2% | 9.9 | 6.9 | 2.2 | 🔴 yếu đi ⚠️ |
| MB:G2#1:D-1->(MT,T5) | 8.3 | 42.1% | 12.0 | 4.7 | 6.2 | 🔴 yếu đi |
| MN:G3#2:D-2->(MT,T5) | 8.3 | 78.2% | 12.8 | 3.8 | -2.2 | 🔴 yếu đi ⚠️ |
| MB:G6#2:D-1->(MT,T7) | 8.3 | 42.0% | 10.4 | 6.1 | 12.9 | 🔴 yếu đi |
| MB:G6#3:D-2->(MT,T5) | 8.3 | 42.0% | 11.0 | 5.5 | -0.4 | 🔴 yếu đi ⚠️ |
| MB:G6#3:D-2->(MT,T7) | 8.3 | 42.0% | 9.8 | 6.7 | 6.2 | 🔴 yếu đi |
| MN:G3#2:D-1->(MN,T7) | 8.2 | 88.8% | 12.9 | 3.7 | -1.3 | 🔴 yếu đi ⚠️ |
| MN:G8#1:D->(MT,T7) | 8.2 | 88.2% | 10.3 | 6.2 | 9.7 | 🔴 yếu đi |
| MN:G5#1:D-1->(MT,T5) | 8.2 | 78.4% | 12.0 | 4.4 | 0.9 | 🔴 yếu đi ⚠️ |
| MN:G5#1:D->(MT,T7) | 8.1 | 87.9% | 9.8 | 6.4 | 3.3 | 🔴 yếu đi ⚠️ |

---

## 4. ❌ 266 CELL BỊ LOẠI (vi phạm thứ tự xổ) — top 20

> Same-day nguồn xổ SAU đích (MT/MB→MN, MB→MT). Đã loại khỏi mọi tập dùng được. Liệt kê top để minh bạch.

| Rule | Lift (ảo) | BH-pass | Trạng thái |
|---|---|---|---|
| MB:G7#1:D->(MN,T7) | 16.7 | ✓ | ❌ EXCLUDED |
| MB:G7#3:D->(MT,T5) | 14.3 | ✓ | ❌ EXCLUDED |
| MB:G4#1:D->(MN,T7) | 13.0 | ✓ | ❌ EXCLUDED |
| MB:G2#1:D->(MT,T7) | 12.9 | ✓ | ❌ EXCLUDED |
| MB:G4#1:D->(MT,T7) | 12.6 | ✓ | ❌ EXCLUDED |
| MB:G6#1:D->(MT,T7) | 12.3 | ✓ | ❌ EXCLUDED |
| MB:G2#2:D->(MT,T7) | 11.9 | ✓ | ❌ EXCLUDED |
| MB:G4#1:D->(MT,T5) | 11.8 | ✓ | ❌ EXCLUDED |
| MB:G7#3:D->(MT,T7) | 11.0 | ✓ | ❌ EXCLUDED |
| MB:G2#1:D->(MN,T7) | 10.5 | ✓ | ❌ EXCLUDED |
| MB:G6#1:D->(MN,T7) | 10.5 | ✓ | ❌ EXCLUDED |
| MB:G1#1:D->(MT,T5) | 10.3 | ✓ | ❌ EXCLUDED |
| MB:G2#1:D->(MT,T5) | 10.3 | ✓ | ❌ EXCLUDED |
| MB:G6#2:D->(MN,T7) | 10.2 | ✓ | ❌ EXCLUDED |
| MB:G7#1:D->(MT,T7) | 10.1 | ✓ | ❌ EXCLUDED |
| MB:G1#1:D->(MN,T7) | 9.9 | ✓ | ❌ EXCLUDED |
| MB:G7#4:D->(MT,T7) | 9.5 | ✓ | ❌ EXCLUDED |
| MT:G5#1:D->(MN,T7) | 9.4 | ✓ | ❌ EXCLUDED |
| MT:G3#1:D->(MN,T7) | 9.3 | ✓ | ❌ EXCLUDED |
| MB:G6#3:D->(MN,T7) | 9.3 | ✓ | ❌ EXCLUDED |

(... tổng 266 cell, xem `machine_readable/V10675_ALL_RULES_LABELED.json`)

---

## 5. Các nhóm rule KHÁC trong cả hành trình (gắn nhãn trạng thái)

Để không bỏ sót, đây là các nhóm đã đào nhưng không cùng schema cross-region (chi tiết trong [V10673_SESSION_RULE_DIGGING_JOURNEY_VN.md](./V10673_SESSION_RULE_DIGGING_JOURNEY_VN.md)):

| Nhóm | Số rule | Nhãn trạng thái |
|---|---|---|
| V10626 pre-register panel (FU1-3) | 58 | 🟡 PRE-REGISTER (chờ, chưa live) |
| V10626 FU4 (MB G4/G6/G7) | 13 | 🟡 PRE-REGISTER STABLE_ALL |
| V106.04/05/06 broad mining | ~hàng nghìn | ⚠️ WEAK — V107 null-test bác (0/153k BH) → **không dùng** |
| MB D = MB D-2 GĐB self | — | ❌ REJECTED (FU1 + V10635, −3.7pp) |
| Production `mined_rules` | 105 | ✅ LIVE (cơ chế riêng, verify sạch V10672) |

---

## 6. Kết luận

- **Không bỏ sót**: 183 rule qualifying + 266 cell loại đều đã gắn nhãn; các nhóm khác (pre-register 71, weak, rejected, production) tham chiếu mục 5.
- **Trạng thái tổng**: 🟢 69 mạnh lên · 🟡 56 ổn định · 🔴 58 yếu đi · ⚠️ 39 cần canh.
- **0 rule** trong tập dùng được vướng bug temporal/ngày; 266 cell vi phạm đã loại đúng.
- Tài liệu này sinh **tự động từ JSON** nên đồng bộ tuyệt đối với số liệu đo.

**Dữ liệu máy đọc**: `machine_readable/V10675_ALL_RULES_LABELED.json` (toàn bộ 183 rule + 266 excluded, đầy đủ trend).

**STATUS**: V10675 MASTER LABELED — 183 qualifying rules labeled (69↑/56=58↓, 39 watch) + 266 excluded. No rule omitted.
