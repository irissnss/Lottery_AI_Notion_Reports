# Đề xuất quy ước mã công việc dễ đọc (V10965)

> Chỉ đề xuất. **Chưa đổi** mã đang dùng. Owner phải duyệt trước khi đổi hàng loạt.  
> Ngày viết: 02/08/2026 (giờ Việt Nam).

Owner hỏi nguyên văn:

> *"Số hiệu công việc cần quy chuẩn chứ kiểu như PL6 gì đó khó nhận biết quá. Số hiệu phải viết tắt đầu mục công việc và hạn ngày, ví dụ Kiểm Soát 08/08 thì số hiệu viết tắt phải viết là TH0808 chẳng hạn, thế dễ đọc hơn."*

---

## 1. Hiện trạng — đang có những hệ mã nào

| Hệ | Nghĩa | Số đang sống | Nhìn vào biết việc gì? | Nhìn vào biết hạn? |
|---|---|---:|---|---|
| **FU-xxx** | Theo dõi (`FOLLOW_UP_TRACKER.md`) | **72** treo (parser); ~24 có hạn thật, ~48 không hạn / cũ) | Không | Chỉ khi mở tracker |
| **QD-xxx** | Quyết định owner (sổ mới) | **5** (QD-013…017; QD-001–012 không tồn tại) | Không | Một phần có hạn rà |
| **OD-YYYYMMDD-X** | Quyết định owner (kiểu cũ) | **12** — tất cả ACTIVE | Không | Có ngày trong mã, không phải hạn |
| **DEC-xxx** | Nhật ký quyết định cũ | **22** (append-only) | Không | Không |
| **CP-xxx** / CP-Lx / CP-OTx / CP-Xx | Checkpoint roadmap | **~18–23** còn mở trên 4 roadmap ACTIVE | Một phần (L=lean, OT=output total) | Phải mở roadmap |
| **G0/S/A/P/C/D** | Checkpoint Standardization | Vài mục còn chạy | Không | Không |
| **D-01…D-12** | Quyết định Notion | 12 (đóng băng từ 01/08, chỉ lịch sử) | Không | Không |
| **Vxxxxx** | Phiên bản làm việc | Hàng trăm (CHANGELOG) | Không | Không — đây là số phiên, không phải ticket |
| **PL-1 / PL-2** | Nhãn kế hoạch ad-hoc | 2 | Không | Không — đúng cái owner phàn nàn |

**Vấn đề cụ thể vừa xảy ra hôm nay:** mã **FU-225** bị dùng hai nghĩa khác nhau trong cùng tracker (một dòng = xác minh UI V10964, một dòng = QD-016 RULES-FIRST). Parser chỉ giữ bản trên cùng → dễ đọc nhầm. Đây là triệu chứng của mã số thuần tuý không gắn nội dung.

Công cụ đang bám mã cũ:

- `_v10958_fu_reader.py` — regex `FU-\d+[A-Za-z]?`
- `_v10920_decision_ledger.py` — đọc `id` JSON (QD/OD)
- `_v10920_session_start.py` — gọi hai cái trên + quét roadmap
- `_v10921_report_gate.py` — khoá theo `Vxxxxx`

Đổi regex hàng loạt mà không sửa parser = briefing đầu phiên gãy.

---

## 2. Quy ước đề xuất (đúng ý owner)

### 2.1 Dạng mã

```
<VIẾT_TẮT><DDMM>[YY][-n]
```

Ví dụ owner đưa: **Kiểm soát hạn 08/08** → `TH0808`  
(Nếu sang năm dễ trùng thì dùng `TH080826` = 08/08/2026.)

### 2.2 Bảng viết tắt nhóm việc thường gặp

| Viết tắt | Nhóm việc | Ví dụ |
|---|---|---|
| **TH** | Theo dõi / kiểm soát tiến độ | TH0808 |
| **KS** | Kiểm soát / cổng kiểm / self-check | KS0808 |
| **DO** | Đo lường / shadow measurement | DO0815 |
| **SC** | Sửa lỗi (sửa code) | SC0803 |
| **QD** | Quyết định owner (giữ hai chữ quen thuộc) | QD0808-1 |
| **DP** | Deploy / restart / verify live | DP0802 |
| **BC** | Báo cáo / A55 / tài liệu | BC0802 |
| **DB** | Đóng băng / không đụng đường ra số | DB0808 |
| **XH** | Xếp hạng / roster / cắt-giữ model | XH0808 |
| **HT** | Học / train / retrain / prompt | HT0815 |
| **UI** | Giao diện | UI0803 |
| **RM** | Roadmap checkpoint | RM0808 |

Không bắt buộc dùng hết — owner có thể rút còn 6–8 mã hay dùng nhất.

### 2.3 Ngày trong mã: `DDMM` hay `DDMMYY`?

| Cách | Ưu | Nhược |
|---|---|---|
| **DDMM** (0808) | Ngắn, đúng ví dụ owner | Sang năm 2027 sẽ trùng `0808` |
| **DDMMYY** (080826) | Không trùng năm | Dài hơn 2 ký tự |

**Khuyến nghị:** dùng **DDMM** trong giao tiếp hàng ngày; khi lưu sổ / JSON chính thức dùng **DDMMYY**. Hiển thị có thể rút: `TH0808 (2026)`.

### 2.4 Các tình huống thực tế

| Tình huống | Cách xử lý |
|---|---|
| Hai việc cùng nhóm cùng hạn | Thêm hậu tố `-1`, `-2`… ví dụ `TH0808-1`, `TH0808-2` |
| Việc không có hạn cố định | Dùng `0000` hoặc chữ `LX` (liên tục): `KS0000` / `KSLX` — **khuyến nghị `LX`** cho dễ đọc |
| Việc bị dời hạn | **KHÔNG đổi mã**. Ghi hạn mới ở trường `han` / nhãn cạnh. Đổi mã = mất dấu vết trong CHANGELOG |
| Việc xong | Giữ mã, đổi trạng thái. Không tái sử dụng mã cho việc khác (tránh lỗi kiểu FU-225 kép) |

### 2.5 Ví dụ đọc được ngay

| Việc | Mã đề xuất |
|---|---|
| Đóng băng đường ra số tới 08/08 (QD-014) | `DB0808` (cũ: QD-014 / FU-215) |
| Shadow bỏ ép RULES-FIRST sau 08/08 | `HT0808-1` (cũ: QD-016 / FU-225) |
| A/B hai prompt cùng model từ 08/08 | `HT0808-2` (cũ: QD-017 / FU-226) |
| Phép so AUC lệch cửa sổ, hạn 15/08 | `HT0815` (cũ: FU-213) |
| Xác minh UI /du-doan-test sau V10964, hạn 03/08 | `UI0803` (cũ: FU-225 bản V10964) |

---

## 3. Bảng chuyển đổi mã đang sống

Quy tắc chuyển: **mã mới = nhóm + hạn**; luôn ghi `(cũ: …)` cạnh ít nhất một giai đoạn song song.

### 3.1 Quyết định owner (QD + OD) — 17 mục

| Mã cũ | Mã mới đề xuất | Hạn / ghi chú |
|---|---|---|
| QD-013 | `DBLX-1` hoặc `QDLX-1` | Liên tục — dừng tiền thật tới khi có edge |
| QD-014 | `DB0808` | Hết hạn rà 08/08 |
| QD-015 | `XH0808-1` | Shadow MT RF đơn từ 08/08 |
| QD-016 | `HT0808-1` | Bỏ ép RULES-FIRST shadow |
| QD-017 | `HT0808-2` | A/B hai prompt |
| OD-20260726-A | `QDLX-2` | Quy đổi điểm tiền — không hạn |
| OD-20260731-A | `QDLX-3` | Mốc FINAL (đã cập nhật 16:58/17:58) |
| OD-20260731-B | `QDLX-4` | Biên 2 phút |
| OD-20260731-C | `QDLX-5` | Giờ Việt Nam |
| OD-20260801-A…H | `QDLX-6` … `QDLX-13` | Bộ quyết định 01/08 (an toàn / dọn lane / GitHub / đồng bộ quy tắc…) |

*(Chi tiết từng OD-20260801-X giữ nguyên tiêu đề trong sổ; mã mới chỉ để gọi nhanh.)*

### 3.2 Theo dõi có hạn (ưu tiên chuyển trước) — ~24 FU

| Mã cũ | Hạn | Tiêu đề ngắn | Mã mới đề xuất |
|---|---|---|---|
| FU-189 | 02/08 | Xác minh lane nghỉ vắng | `TH0802-1` |
| FU-184 | 02/08 | MT/MB công bố đúng phiếu? | `TH0802-2` |
| FU-185 | 03/08 | Tinh gọn lane hết hạn vẫn chạy | `TH0803-1` |
| FU-225 (UI V10964) | 03/08 | Xác minh /du-doan-test + /filter | `UI0803` |
| FU-216 | 08/08 | Shadow MT RF đơn (QD-015) | `XH0808-1` |
| FU-217 | 08/08 | LSTM live lệch | `SC0808-1` |
| FU-215 | 08/08 | Đóng băng QD-014 | `DB0808` |
| FU-210 | 08/08 | Tháng 6 mất lợi thế MT | `DO0808-1` |
| FU-207 | 08/08 | Mốc an toàn deploy | `DP0808` |
| FU-203 | 08/08 | gemini-3.5-flash hồi phong độ? | `DO0808-2` |
| FU-191 | 08/08 | Cắt model an toàn combo-super | `XH0808-2` |
| FU-192 | 08/08 | Shadow 110 ngày 0 promote | `XH0808-3` |
| FU-193 | 08/08 | combo-super thiếu sàn chất lượng | `XH0808-4` |
| FU-187 | 08/08 | Tra cứu trước khi hỏi | `KS0808` |
| FU-186 | 08/08 | 7 ngày sau tắt ghi đè | `TH0808-1` |
| FU-202 | 09/08 | gemini lọt top-2? | `DO0809-1` |
| FU-200 | 09/08 | Đo đổi total trước combo | `DO0809-2` |
| FU-188 | 10/08 | Tồn đọng báo cáo A55 | `BC0810` |
| FU-213 | 15/08 | Phép so AUC lệch cửa sổ | `HT0815` |
| FU-204 | 15/08 | gpt-5.4 gọi về đúng? | `TH0815-1` |
| FU-197 | 15/08 | Đo gemini sau thoát 503 | `DO0815-1` |
| FU-195 | 15/08 | Ngưỡng gỡ glm-5.1 | `XH0815` |
| FU-196 | 15/08 | Đo hoán đổi model | `DO0815-2` |
| FU-183 | 31/08 | Lớp V10640 MN rà | `TH0831` |
| FU-198 | 01/09 | So gemini-3.5 vs 3.6 | `DO0901` |
| FU-226 | 08/08 (lock) | A/B hai prompt | `HT0808-2` |
| FU-225 (QD-016) | 08/08 | Bỏ ép RULES-FIRST | `HT0808-1` |
| FU-222 | (sau DB) | Bóc RULES-FIRST | `HT0808-3` |

### 3.3 FU không hạn / cũ (khoảng 45–50 mục)

**Không đổi mã từng cái ngay.** Đề xuất một lần:

- Gắn nhãn `CŨ:` + trạng thái `CHO_DONG` hoặc đóng hàng loạt các `DEPLOYED_PENDING_LIVE_VERIFY` từ FU-118…FU-168 nếu owner xác nhận đã xong lịch sử.
- Nếu giữ mở: mã mới dạng `THLX-<số cũ>` ví dụ `THLX-118`, vẫn tra được ngược.

### 3.4 Checkpoint roadmap còn mở (rút gọn)

| Mã cũ | Mã mới đề xuất | Ghi chú |
|---|---|---|
| CP-L1 | `RM-L1` hoặc `XH-L1` | RE-PLANNING cắt shadow |
| CP-L3 | `RM-L3` | Drop bảng chết — chờ owner |
| CP-L4 | `RMLX-L4` | Thu hoạch giữ — liên tục |
| CP-L6 | `XH0808-5` | Lean roster — resume sau 08/08 |
| CP-OT4 / OT5 | `RM-OT4` / `RM-OT5` | HOLD |
| CP-1.4, 2.4, 2.5, 3.x, X.x | `RM-…` giữ đuôi cũ | Roadmap leakage — nhiều mục lâu |

Roadmap Standardization (A1/A4/A5/C1/C2): đổi thành `RM-A1`… hoặc giữ nguyên tới khi roadmap đó đóng.

### 3.5 D-01…D-12 (Notion)

**Không chuyển.** Notion đã đóng băng (§57). Chỉ ghi trong bảng tra cứu lịch sử: `D-11 (Notion, đóng băng)`.

---

## 4. Rủi ro nếu đổi quy ước

| Rủi ro | Mức | Hệ quả nếu bỏ qua |
|---|---|---|
| Đứt tham chiếu trong CHANGELOG (~1,9 triệu ký tự) + hàng trăm báo cáo công khai | Cao | Mất khả năng lần ngược “FU-213 là gì” |
| Hai hệ mã song song gây rối | Cao (giai đoạn chuyển) | Người đọc không biết mã nào đúng |
| Parser `_v10958_fu_reader.py` chỉ bắt `FU-\d+` | Cao | Briefing đầu phiên báo sai / bỏ sót việc treo |
| Session start / report gate / ledger | Cao | Cổng tự động gãy |
| Tái sử dụng số (đã xảy ra với FU-225) | Đang xảy ra | Hai việc một mã |

---

## 5. Ba phương án để owner chọn

### Phương án A — Đổi mã hàng loạt (đúng chữ owner nhất)

- Mọi việc mới + việc đang sống đổi sang `TH0808` kiểu mới.
- Sửa parser, tracker, sổ quyết định, roadmap trong cùng vài phiên.
- Giữ `(cũ: FU-xxx)` trong ngoặc 90 ngày.

**Ưu:** Đúng ý “nhìn mã là biết việc và hạn”.  
**Nhược:** Chi phí lớn, rủi ro đứt lịch sử, dễ loạn khi hai agent song song.

### Phương án B — Giữ mã cũ, bắt buộc kèm nhãn + hạn (nhẹ nhất) ★ khuyến nghị

- Mã máy vẫn `FU-213`, `QD-014`, `CP-L6`.
- **Bắt buộc** mọi chỗ người đọc (tracker, báo cáo, câu trả lời owner) viết dạng:

  `FU-213 · HT0815 · Phép so AUC lệch cửa sổ · hạn 15/08`

  hoặc ngắn: `FU-213 (HT0815 — AUC lệch, 15/08)`.

- Việc mới: vẫn cấp FU/QD số, nhưng **đồng thời** cấp mã đọc `TH…` làm “tên gọi”.
- Sửa nhẹ template tracker + báo cáo A55; **chưa** đụng regex parser.

**Ưu:** Đạt mục tiêu dễ đọc ngay; không gãy công cụ; không mất lịch sử.  
**Nhược:** Vẫn còn số FU trong máy — owner phải chấp nhận hai lớp (máy / người).

### Phương án C — Lai: việc mới dùng mã đọc; việc cũ chỉ gắn phụ đề

- Từ ngày owner duyệt: việc mới **chỉ** dùng `TH0808-1` (không cấp FU mới).
- Việc cũ: giữ FU/QD, thêm một dòng `ten_goi: HT0815` trong tracker.
- Từ từ sửa parser chấp nhận cả hai dạng.

**Ưu:** Tiến dần, đúng hướng owner.  
**Nhược:** Giai đoạn song song dài; phải sửa parser sớm hơn phương án B.

---

## 6. Khuyến nghị của em

Chọn **phương án B** trong 1–2 tuần cửa sổ đóng băng (tới 08/08):

1. Không đổi mã máy, không đụng parser.
2. Chuẩn hoá cách viết: luôn có **mã đọc + hạn + tiêu đề ngắn** cạnh mã cũ.
3. Cấm tái sử dụng FU số (bài học FU-225 kép hôm nay).
4. Sau 08/08, nếu owner thấy mã đọc hữu ích, nâng lên phương án C (việc mới chỉ dùng mã đọc) rồi mới cân nhắc A.

Nếu owner muốn làm mạnh ngay theo ví dụ `TH0808`, chọn **C** chứ đừng nhảy thẳng **A** — vì CHANGELOG và công cụ tự động chưa sẵn sàng đổi hàng loạt trong một phiên.

---

## 7. Việc chưa làm (cố ý)

- Chưa sửa `FOLLOW_UP_TRACKER.md` / ledger / roadmap sang mã mới.
- Chưa sửa `_v10958_fu_reader.py`.
- Chưa đổi Notion (đã cấm ghi).

Chờ owner chọn A / B / C.
