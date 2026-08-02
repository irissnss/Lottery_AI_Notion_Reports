# INDEX_QUYET_DINH_FU_V10971 — QD / FU / CP (02/08/2026)

Nguồn: `docs/OWNER_DECISION_LEDGER.json` · `docs/FOLLOW_UP_TRACKER.md` · V10970 · briefing `_v10920_session_start` 02/08.

Trạng thái **không** lấy từ Notion (đứng đông từ 01/08).

---

## A. Quyết định còn hiệu lực (rút)

| Mã | Mã đọc | Nội dung ngắn | Hạn / cửa sổ | Status |
|---|---|---|---|---|
| **QD-013** | KSLX / KS0808 | Dừng tiền thật tới khi edge ≥3pp & z≥2 (90d) | LX / canh 08/08 | ACTIVE — cổng **ĐÓNG** |
| **QD-014** | DB0808 | Freeze roster 15 / combo-super / override tới hết 08/08 | **08/08** | ACTIVE |
| **QD-015** | XH0808-1 | Sau freeze: shadow MT RF đơn; cắt nếu live↔re &lt;95% 7 ngày | từ 08/08 | ACTIVE (chờ hết freeze) |
| **QD-016** | HT0808-1 | Sau freeze: shadow bỏ ép chọn từ RULES-FIRST | từ 08/08 | ACTIVE (chờ) |
| **QD-017** | HT0808-2 | Sau freeze: A/B hai prompt **cùng model** ≥14 ngày | từ 08/08 | ACTIVE (chờ) |
| **QD-018** | HT0822 | Sau freeze: **B1→B2→B3 tuần tự** 7–14 ngày/bước | B1 22/08… | ACTIVE (kế hoạch) |
| **QD-019** | — | Quy ước mã công việc phương án B (§58) | đã áp | ACTIVE |
| OD-20260801-A | — | Tắt 5 lớp ghi đè; giữ V10640 MN | — | ACTIVE |
| OD-20260801-B | — | 6 lane hết hạn nghỉ (cron) | — | ACTIVE |
| OD-20260801-C | — | Không dựng thêm luồng đo song song khi đủ số | — | ACTIVE |
| OD-20260801-D | DB0808-2 | Tiền đề đóng băng 7 ngày | 08/08 | ACTIVE |
| OD-20260801-E | — | Tra cứu trước hỏi; ledger + session start | — | ACTIVE |
| OD-20260801-F | — | Báo cáo public A55; Notion chỉ đọc | — | ACTIVE |
| OD-20260801-G/H | — | CLAUDE.md + 6 mặt quy tắc đồng bộ | — | ACTIVE |
| OD-20260731-A | — | FINAL MN 15:45 / MT 16:58 / MB 17:58 (đã dời từ 16:53/17:53) | — | ACTIVE |
| OD-20260731-B | — | Biên chốt 2 phút | — | ACTIVE |
| OD-20260731-C | — | Giờ VN nhất quán | — | ACTIVE |
| OD-20260726-A | — | Giá vốn 18k MN/MT · 27k MB · ăn 98k | — | ACTIVE |

### QD-014 — danh sách cấm đụng (freeze)

1. Đổi danh sách **15** model official `OUTPUT_ELIGIBLE`
2. Đổi hằng số / logic bộ lọc **combo-super**
3. Bật/tắt thêm lớp **ghi đè** bạch thủ
4. Promote shadow → official / cắt model vì ngày đẹp

**Pool 15 (local registry 02/08):**  
claude-sonnet-4-6, gemini-2.5-flash, claude-opus-4-6, deepseek-reasoner, gemini-2.5-pro, **gpt-5.4**, **glm-5.1**, **gpt-oss-120b**, meta-learning, lstm, xgboost, random-forest, smart-ensemble, smart-ml, combo-super  
(**không** combo-no-token trong total)

### QD-018 — thứ tự sau 08/08

| Bước | FU | Mã đọc | Việc | Hạn |
|---|---|---|---|---|
| B1 | FU-233 | HT0822-1 | Tắt tối ưu trọng số (optimizer CN 03:00) | 22/08 |
| B2 | FU-234 | DO0905 | Đo 105 luật có giúp số công bố không | 05/09 |
| B3 | FU-235 | HT0919 | Gỡ ép chọn từ list (thực thi QD-016 shadow) | 19/09 |

Không chạy song song ba thay đổi.

---

## B. FU mở — ưu tiên (mã đọc §58)

### Nóng / gần hạn

| FU | Mã đọc | Việc | Hạn | Status |
|---|---|---|---|---|
| FU-225 | UI0803 | Verify UI du-doan-test + filter | **03/08** | DEPLOYED_PENDING_LIVE_VERIFY |
| FU-185 | DD0803 | Lane hết hạn vẫn chạy — tinh gọn | 03/08 | MEASURED_BUT_NOT_FIXED |
| FU-189 | KS0802-1 | Lane nghỉ vắng — đối chiếu | 02/08 | WAIT_LIVE |
| FU-184 | KS0802-2 | MT/MB công bố đúng phiếu | 02/08 | WAIT_LIVE |
| FU-238 | KS0802-3 | Kiểm tổng lực hết live | 02/08 | ĐÓNG (V10969) |
| FU-239 | TK0802 | Báo cáo tổng hợp V10970 | 02/08 | báo cáo xong |

### Cửa sổ 08/08 (freeze + kế hoạch)

| FU | Mã đọc | Việc | Hạn | Status |
|---|---|---|---|---|
| FU-215 | DB0808 | Đóng băng đường ra số (QD-014) | 08/08 | OWNER_LOCK |
| FU-208 | KSLX / KS0808 | Cổng lợi thế — chỉ đặt tiền khi mở | LX / 08/08 | OWNER_LOCK |
| FU-209 | XHLX-209 | Dừng thêm/cắt model tới cổng mở | LX | OWNER_LOCK |
| FU-216 | XH0808-1 | Shadow MT RF đơn (QD-015) | 08/08 | OWNER_LOCK |
| FU-231 | HT0808-1 | Bỏ ép RULES-FIRST shadow (QD-016) | 08/08 | OWNER_LOCK |
| FU-226 | HT0808-2 | A/B hai prompt cùng model (QD-017) | 08/08 | OWNER_LOCK |
| FU-210 | DO0808-1 | Tháng 6 mất lợi thế MT | 08/08 | MEASURED_BUT_NOT_FIXED |
| FU-217 | SC0808-1 | LSTM live lệch suy luận | 08/08 | MEASURED_BUT_NOT_FIXED |
| FU-207 | DP0808 | Mốc an toàn deploy | 08/08 | MEASURED (+ V10968 guard) |
| FU-203 | DO0808-2 | gemini-3.5 hồi phong độ | 08/08 | WAIT_LIVE |

### Trung hạn (15/08…)

| FU | Mã đọc | Việc | Hạn | Status |
|---|---|---|---|---|
| FU-237 | DP0815 | Canh chốt giờ cấm deploy | 15/08 | DEPLOYED_PENDING_LIVE_VERIFY |
| FU-213 | HT0815 | Phép so AUC lệch cửa sổ | 15/08 | MEASURED_BUT_NOT_FIXED |
| FU-228 | DO0815-4 | Đo hiệu quả cơ chế học | 15/08 | MEASURED_BUT_NOT_FIXED |
| FU-229 | SC0815-2 | Champion selector cron | 15/08 | MEASURED_BUT_NOT_FIXED |
| FU-230 | DO0815-3 | Đồng bộ WR vs BT | 15/08 | MEASURED_BUT_NOT_FIXED |
| FU-232 | SC0815-3 | V10938 nửa còn (trọng số WR) | 15/08 | OWNER_LOCK |
| FU-204 | KS0815-1 | gpt-5.4 gọi về đúng | 15/08 | (theo dõi) |
| FU-224 | UI0809 | Dọn frontend trùng | 09/08 | OWNER_LOCK |
| FU-222 | HT0822 | Bóc RULES-FIRST (liên QD-016) | 22/08 | MEASURED → xếp sau B1/B2 |
| FU-223 | HT0810 | Chéo prompt GĐ4 | 10/08 | OWNER_LOCK → FU-226 |
| FU-221 | TKLX-221 | Notion D-11 lỗi thời | LX | OWNER_LOCK (chỉ lịch sử) |

### Sau 08/08 (chuỗi QD-018)

FU-233 · FU-234 · FU-235 — xem bảng QD-018.

---

## C. FU / CP đã đóng gần đây (đừng mở lại)

| Mục | Ghi chú |
|---|---|
| FU-211 | Job CN 02:00 ghi AUC — ĐÓNG V10953 |
| FU-212 | Đo tín hiệu rơi — chuyển QD-015/FU-216 |
| FU-219 | FINAL 16:58 khớp — ĐÓNG V10962 |
| FU-220 | Bù A55 — ĐÓNG V10962 |
| FU-194 / FU-199 | Nghiệm thu hạn mới / bấm nút sau MB |
| FU-227 | Quy ước mã B — CLOSED sau chọn |
| CP-X.1, CP-2.2, CP-4.0, CP-R4 | Owner đóng di sản — thay bằng edge gate |
| Briefing 02/08 | **0** checkpoint ACTIVE quá hạn (đã dọn) |

---

## D. Roadmap ACTIVE còn file

| File | STATUS | Ghi chú handoff |
|---|---|---|
| `ACTIVE_ROADMAP_LEAN_HARVEST_20260619.md` | ACTIVE | Đọc CP trước khi hỏi owner |
| `ACTIVE_ROADMAP_OUTPUT_TOTAL_ADVANCED.md` | ACTIVE (đợi A/B…) | Không đụng official trong freeze |
| `ACTIVE_ROADMAP_STANDARDIZATION_ACCURACY.md` | ACTIVE | — |
| `ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md` | (không STATUS rõ / di sản đã đóng CP) | Không hỏi lại CP đã đóng |

---

## E. Ngưỡng số không được quên

| Ngưỡng | Giá trị |
|---|---|
| Mở cổng tiền (QD-013) | lợi thế ≥ **+3,0pp** và **z ≥ 2,0** (90 ngày) |
| Hòa vốn MN/MT | ~**18,37%** (18k → 98k) |
| Hòa vốn MB | ~**27,55%** (27k → 98k) |
| Bừa ước | MN/MT ~16,5% · MB ~23,8% |
| QD-015 cắt shadow | live↔re top-1 **&lt;95%** trong 7 ngày đầu |
| 3/3 WIN 90d | **1/91** ngày (02/08) — nhiễu, không mở tiền |
| Edge 02/08 ~18:48 | MN −0,38 · MT −2,02 · MB −7,21 pp — **ĐÓNG** |
