# V10670 — Quy Ước Nguồn (Source Semantics) — RÕ RÀNG CHO MỌI TOOL AI

> **Generated**: 2026-06-02 11:20 VN
> **Trigger**: Owner 02/06 — "MN D = MT D-1 giải đặc biệt nhưng MT D-1 hôm đó có 3 đài thì làm sao? ... b1 là gì? ... tool AI đọc làm sao? phải rõ ràng nhất quán ai đọc cũng hiểu ngay".
> **Mục đích**: Giải thích chính xác ý nghĩa của notation nguồn, để bất kỳ tool AI nào đọc cũng hiểu ngay.

---

## 1. Cấu trúc 1 rule

```
[Miền nguồn] : [Giải] # [Bộ] : [Lag]  →  ([Miền đích], [Thứ])
```

Ví dụ: `MT:DB#1:D-1 → (MN, T3)` đọc là:
- **Miền nguồn** = MT (Miền Trung)
- **Giải** = DB (Giải Đặc Biệt)
- **Bộ** = #1 (bộ thứ 1)
- **Lag** = D-1 (ngày hôm trước)
- **Đích** = MN ngày Thứ 3

---

## 2. "#Bộ" nghĩa là gì? (làm rõ điểm anh hỏi)

**`#Bộ` = VỊ TRÍ bộ số trong 1 giải, KHÔNG PHẢI tên đài.**

| Giải | Số bộ | Ý nghĩa #Bộ |
|---|---|---|
| MB G.4 | 4 bộ | #1=top-left, #2=top-right, #3=bottom-left, #4=bottom-right |
| MB G.6 | 3 bộ | #1, #2, #3 (trái → phải) |
| MB G.7 | 4 bộ | #1, #2, #3, #4 (trái → phải) |
| MB G.2 | 2 bộ | #1 (trái), #2 (phải) |
| MB G.ĐB, G.1 | 1 bộ | #1 = bộ duy nhất |
| MN/MT G.3 | 2 bộ | #1 (trái), #2 (phải) |
| MN/MT G.ĐB, G.1, G.2, G.5, G.7, G.8 | 1 bộ | #1 = bộ duy nhất |

→ Với **giải ĐB của MN/MT mỗi đài chỉ có 1 bộ** nên `DB#1` = bộ duy nhất đó. **`#1` KHÔNG phải đài Bình Định hay đài nào** — nó là "bộ thứ nhất của giải ĐB".

---

## 3. ⭐ TRẢ LỜI CÂU HỎI: "MT D-1 có 3 đài thì lấy đài nào?"

**Rule GOM (union) giá trị của TẤT CẢ đài miền nguồn xổ ngày đó.**

Ví dụ rule `MT:DB#1:D-2 → (MT, T7)`:
- Đích = MT Thứ 7. Source date = D-2 = **Thứ 5**.
- MT Thứ 5 có **3 đài**: Bình Định, Quảng Trị, Quảng Bình.
- → `MT:DB#1:D-2` = **GOM LAST2 giải ĐB của cả 3 đài** = {LAST2(Bình Định ĐB), LAST2(Quảng Trị ĐB), LAST2(Quảng Bình ĐB)} = 3 giá trị.
- **Hit** = nếu BẤT KỲ 1 trong 3 giá trị đó xuất hiện trong đuôi giải MT ngày Thứ 7.

→ KHÔNG phải 1 đài. Là **hợp của tất cả đài cùng giải cùng bộ**. Baseline đã tính theo số giá trị gom (avg_src_size).

### Để biết đài NÀO đóng góp nhiều nhất

Mỗi rule có bảng **per-source-station breakdown** (file `V10670_SOURCE_STATION_BREAKDOWN.json`). Ví dụ rule trên:

| Đài source (Thứ 5) | Hit rate riêng đài | n |
|---|---|---|
| Bình Định | 46.81% | 329 |
| Quảng Trị | 44.07% | 329 |
| Quảng Bình | 41.03% | 329 |

→ Nếu anh muốn dùng RIÊNG 1 đài (vd chỉ Bình Định ĐB) thì hit rate ~46.8%. Nếu gom cả 3 thì aggregate 86.32% (vì 3 cơ hội).

---

## 4. ⭐ LỊCH ĐÀI THEO THỨ (verified từ DB thực tế 2026-06-02)

Đây là bảng tra cứu để biết "Miền X ngày Thứ Y có đài nào". Tool AI dùng bảng này để resolve nguồn.

### Miền Bắc (MB) — ⚠️ MỖI THỨ 1 ĐÀI TỈNH KHÁC NHAU (không phải "MB chung")

| Thứ | Đài MB |
|---|---|
| T2 (Mon) | **Hà Nội** |
| T3 (Tue) | **Quảng Ninh** |
| T4 (Wed) | **Bắc Ninh** |
| T5 (Thu) | **Hà Nội** |
| T6 (Fri) | **Hải Phòng** |
| T7 (Sat) | **Nam Định** |
| CN (Sun) | **Thái Bình** |

→ Quan trọng: trước đây tài liệu ghi "MB_BOARD" là SAI/mơ hồ. MB mỗi ngày là 1 đài tỉnh cụ thể. Ví dụ rule `MB:G4#2:D-1 → (MT, T5)`: source date = D-1 của T5 = T4 = **đài Bắc Ninh**. Vậy rule này thực chất là "G4 bộ 2 của đài Bắc Ninh".

### Miền Trung (MT) — 2-3 đài/thứ

| Thứ | Đài MT |
|---|---|
| T2 | Thừa Thiên Huế, Phú Yên (2 đài) |
| T3 | Đắk Lắk, Quảng Nam (2 đài) |
| T4 | Đà Nẵng, Khánh Hòa (2 đài) |
| T5 | Bình Định, Quảng Trị, Quảng Bình (3 đài) |
| T6 | Gia Lai, Ninh Thuận (2 đài) |
| T7 | Đà Nẵng, Quảng Ngãi, Đắk Nông (3 đài) |
| CN | Khánh Hòa, Kon Tum, Thừa Thiên Huế (3 đài) |

### Miền Nam (MN) — 3-4 đài/thứ

| Thứ | Đài MN |
|---|---|
| T2 | TP. HCM, Đồng Tháp, Cà Mau (3 đài) |
| T3 | Bến Tre, Vũng Tàu, Bạc Liêu (3 đài) |
| T4 | Đồng Nai, Cần Thơ, Sóc Trăng (3 đài) |
| T5 | Tây Ninh, An Giang, Bình Thuận (3 đài) |
| T6 | Vĩnh Long, Bình Dương, Trà Vinh (3 đài) |
| T7 | TP. HCM, Long An, Bình Phước, Hậu Giang (4 đài) |
| CN | Tiền Giang, Kiên Giang, Đà Lạt (3 đài) |

---

## 5. Cách resolve source date → đài cụ thể (cho tool AI)

```
1. Rule có: target_weekday (T_đích), lag (số ngày)
2. source_weekday_index = (target_weekday_index - lag) mod 7
   (T2=0, T3=1, T4=2, T5=3, T6=4, T7=5, CN=6)
3. Tra bảng Mục 4 → đài nguồn xổ ngày đó
4. Source value = GOM LAST2 của [Giải#Bộ] từ tất cả đài đó
```

**Ví dụ cụ thể** rule `MT:G2#1:D-2 → (MT, T7)`:
- target_weekday = T7 = 5
- lag = 2
- source_weekday = (5 − 2) mod 7 = 3 = **T5**
- Đài MT Thứ 5 = Bình Định, Quảng Trị, Quảng Bình
- Source = gom Giải 2 bộ 1 của 3 đài đó ngày source date

---

## 6. Ví dụ áp dụng thực tế (ngày cụ thể)

Giả sử hôm nay là **Thứ 7 ngày 06/06/2026**, em dự đoán MT Thứ 7 bằng rule `MT:G2#1:D-2`:
1. Source date = 06/06 − 2 ngày = **04/06/2026 (Thứ 5)**.
2. MT Thứ 5 = Bình Định, Quảng Trị, Quảng Bình.
3. Lấy Giải 2 bộ 1 (số 5 chữ số) của cả 3 đài ngày 04/06, lấy 2 số cuối mỗi đài → 3 giá trị (vd: "34", "71", "08").
4. Kỳ vọng 1 trong 3 giá trị này xuất hiện trong đuôi giải MT Thứ 7 ngày 06/06.

---

## 7. Lưu ý nhất quán cho tool AI

1. **`#Bộ` luôn là vị trí trong giải**, không bao giờ là tên đài.
2. **Source luôn gom TẤT CẢ đài** của miền nguồn xổ ngày source date (trừ MB chỉ 1 đài/ngày).
3. **MB đài đổi theo thứ** — phải tra bảng Mục 4 để biết đài tỉnh cụ thể.
4. **Tên đài chính xác theo DB**: dùng "Thừa Thiên Huế" (không phải "Huế"), "TP. HCM", "Đà Lạt", v.v.
5. **Per-source-station breakdown** trong `V10670_SOURCE_STATION_BREAKDOWN.json` cho biết đài nào carry signal mạnh nhất.

---

## 8. Reference

- Per-source-station breakdown chi tiết 28 rule: `machine_readable/V10670_SOURCE_STATION_BREAKDOWN.json`
- Bộ numbering (vị trí bộ trong giải): `V10667_BO_NUMBERING_LEGEND.md`
- Temporal causality (thứ tự xổ): `V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md`
- Verify đầy đủ: `V10669_TEMPORAL_VERIFICATION_REPORT_VN.md`

---

**STATUS**: Source semantics legend — station-by-weekday verified from DB, source aggregation explained, #Bộ vs đài clarified. AI-tool readable.
