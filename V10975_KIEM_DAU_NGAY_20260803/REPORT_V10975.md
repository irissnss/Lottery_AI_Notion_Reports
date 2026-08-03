# REPORT V10975 — Kiểm đầu ngày 03/08/2026

> Phiên: sáng 03/08/2026 (giờ Việt Nam) · Loại: **kiểm / đo / tài liệu** · **Không deploy, không đụng production**
> Đóng băng QD-014 còn hiệu lực tới hết 08/08 — phiên này chỉ đọc.

---

## 1. Tóm tắt

Owner bảo *"kiểm tra đầu ngày dùm anh"*. Kết quả: **hệ sạch, không có gì quá hạn, không có quyết định nào bị trôi.**

Ba cổng đầu phiên đều xanh: **0 checkpoint quá hạn**, **0 roadmap chờ archive**, **79 mục theo dõi treo nhưng 0 mục quá hạn**, và sổ quyết định **19/19 khớp code, 0 TRÔI**. Máy chủ khoẻ: `/api/health` = **200**, service `lottery` **active** ở **PID 645169**, chạy liên tục từ 02/08 18:13:33 không restart lần nào; nhật ký hôm nay **0 traceback, 0 dòng CRITICAL**. Bộ tự kiểm nhất quán lần chạy gần nhất (02/08 18:05) đạt **16/16**.

Miền Nam **đã chốt lúc 05:20:15** với **đủ 15/15 model**, bạch thủ **64**, không phải bản dự phòng. Kết quả ngày 02/08 đã về đủ (MN 3 đài · MT 3 · MB 1 — khớp đúng 6 Chủ Nhật gần nhất) và đã chấm xong toàn bộ: 27 model × 3 miền, **0 dòng chưa chấm**. Đáng chú ý: bạch thủ 02/08 **thắng cả 3 miền** (MN 43 · MT 69 · MB 52).

**Cổng lợi thế vẫn ĐÓNG cả ba miền** — tính tươi hôm nay trên cửa sổ 90 ngày: MN **−0,21pp** (z −0,09) · MT **−2,81pp** (z −1,12) · MB **−7,04pp** (z −1,57). Không miền nào tới gần ngưỡng owner đặt (hơn bừa ≥3pp **và** z ≥2).

Đào thêm ra **ba chỗ hở** mà báo cáo hôm qua chưa chạm tới: (A) cổng lợi thế **không hề có bản ghi hằng ngày** vì không ai gọi nó theo lịch; (B) tìm ra **đúng thủ phạm** khiến lane hết hạn vẫn ghi — không phải cron mà là một file `.sh`; (C) **hook đầu phiên im lặng suốt 2 ngày** mà không ai biết.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **"Kiểm tra đầu ngày dùm anh"**

Kèm khung việc do phiên điều phối giao: chạy briefing đầu phiên và sổ quyết định; kiểm trạng thái sống hôm nay 03/08 (health, PID, cron sáng, MN đã chốt chưa, journal, bộ tự kiểm, kết quả 02/08, cổng lợi thế); xử các việc tới hạn 03/08 (FU-225, FU-185); đối chiếu việc đã đóng hôm qua trong `REPORT_V10974.md`, đặc biệt canh FU-243; rồi ghi nhận và đẩy báo cáo công khai.

Ràng buộc owner đã ký trước đó và còn hiệu lực trong phiên này:

> **QD-014** — *"Đóng băng đường ra số công bố tới hết 2026-08-08"*: cấm đổi 15 model official, hằng số lọc combo-super, các cờ ghi đè, writer `/du-doan`, writer `final_bundles`.

> **§57 (A55)** — *"Notion MCP dùng để tham khảo tài liệu khi cần không được cập nhật vào Notion nha em."*

---

## 3. Đào bới / phát hiện

### 3.1 Cách đo

Toàn bộ số trong báo cáo này đọc trực tiếp từ VPS `14.225.224.89` qua SSH, DB `/root/Lottery_AI_Test/data/lottery_ai.db`, bằng 6 script probe **chỉ đọc** viết riêng cho phiên (`_v10975_dau_ngay_probe*.py`, `_v10975_fe_diff.py`, `_v10975_edge_lane_final2.py`, `_v10975_lane_rescan.py`, `_v10975_who_fires.py`, `_v10975_result_sanity.py`). Không script nào ghi vào DB. Mốc giờ chụp: **03/08/2026 08:51:20 +07**.

### 3.2 Cổng đầu phiên và sổ quyết định

| Phép | Kết quả |
|---|---|
| Checkpoint quá hạn | **0** |
| Roadmap xong chưa archive | **0** |
| Mục theo dõi treo | 79 · **quá hạn 0** |
| Quyết định owner tới hạn rà soát | **0** / 19 đang hiệu lực |
| Sổ quyết định — code có trôi không | **19/19 khớp · 0 TRÔI** |
| Ba mặt quy tắc lệch nhau | **không** (lần sửa gần nhất `fd77cad` 02/08) |
| Mục thiếu `ma_doc` (§58) | **không có cảnh báo** |
| Playbook §5 lịch pending-verify | 1 dòng ngày đã qua: `2026-07-28` — mục lịch sử V10870/CP-L6, owner đã ký hoãn 13:48 hôm đó |

Chi tiết 19 quyết định: 16 mục 🟢 khớp toàn phần (tổng 57 mệnh đề kiểm code đều đạt), 2 mục ⚪ không kiểm được bằng máy (`OD-20260801-C` không dựng thêm luồng đo song song, `OD-20260801-D` đóng băng đường ra số — cả hai là mệnh đề phủ định về hành vi tương lai, không có biểu thức code để chấm), 1 mục... không có mục nào 🔴.

### 3.3 Trạng thái sống 03/08 lúc 08:51

| Mục | Số đo |
|---|---|
| `/api/health` | **200** · `V20.3.36` · `expected_model_count=15` · `runtime_model_count=26` |
| Service | `lottery` **active** |
| PID | **645169** · khởi động **02/08 18:13:33 +07** · đã chạy **14h37m**, không restart |
| Journal hôm nay | 181 dòng · **0** khớp `traceback|critical|unhandled` |
| `scheduler_logs` hôm nay | **0** dòng `ERROR`/`CRITICAL` · watchdog `WATCHDOG_OK` đều đặn mỗi 15 phút |
| Cron sáng | chạy đủ nhịp: 06:25 champion_selector · 06:30 retrain_guard · 07:00 weekly_guard · 07:05 + 08:05 system_health · 07:30 verify_0607 · 08:10 timetable_selfcheck |
| Tự kiểm `_v10900_consistency_guard` | gần nhất **02/08 18:05:01** → **16/16 OK** (C1–C16 đều `OK`). Lượt 03/08 theo lịch 18:05, chưa tới |

### 3.4 Miền Nam đã chốt chưa

**Rồi — 05:20:15, đủ 15/15.**

| Trường | Giá trị |
|---|---|
| `date` / `region` | 2026-08-03 / MN |
| `model_count` | **15** |
| `bach_thu` | **64** |
| `lo2` | `["64", "25"]` |
| `generation_method` | `weighted_voting_wr` |
| `consensus_level` | `strong` |
| `is_fallback` | **0** |
| `status` | `ACTIVE` |
| `created_at` | **2026-08-03 05:20:15** |

Phía `predictions`, MN hôm nay có **27** model: **16** dòng `run_source='auto_daily'` (15 model official + `combo-super` là bộ gộp) và **11** dòng `shadow_auto_eval`. Vậy 15 model đóng phiếu → bundle 15. Khớp.

MT và MB hôm nay mới có **7** model mỗi miền, đều ghi lúc 05:00 — đó là 7 model máy không tốn token (`smart-ensemble`, `smart-ml`, `meta-learning`, `lstm`, `xgboost`, `random-forest`, `combo-no-token`). **Đây là đúng lịch, không phải thiếu**: model gọi API chạy sát giờ xổ từng miền (02/08 MT dòng cuối 16:52, MB dòng đầu 17:30).

### 3.5 Kết quả 02/08 và chấm điểm

| Miền | Số đài về | 6 Chủ Nhật gần nhất | Đủ? |
|---|---|---|---|
| MN | **3** | 3 · 3 · 3 · 3 · 3 · 3 | ✅ |
| MT | **3** | 3 · 3 · 3 · 3 · 3 · 3 | ✅ |
| MB | **1** | 1 · 1 · 1 · 1 · 1 · 1 | ✅ |

Chấm điểm `model_daily_eval` ngày 02/08: **27 dòng × 3 miền = 81 dòng**, ghi lúc **20:20**, **0 dòng `hit_count` còn NULL**. Số model trúng: MN 20/27 · MB 20/27 · MT 19/27.

Bạch thủ 02/08 — **thắng cả ba miền**: MN `43` WIN (đóng dấu 16:34:35) · MT `69` WIN (17:30:01) · MB `52` WIN (18:32:04).

### 3.6 Cổng lợi thế — số tươi hôm nay

Gọi thẳng `_v10945_edge_gate.tinh(con, n)` trên VPS, **không** gọi `ghi()` nên không thêm dòng nào vào bảng (đã kiểm lại sau: bảng vẫn đúng 3 dòng cũ).

**Cửa sổ 90 ngày:**

| Miền | Kỳ | Đài đặt | Đài trúng | Hệ | Đánh bừa | Lợi thế | z | Hoà vốn | Còn thiếu | Cổng |
|---|---|---|---|---|---|---|---|---|---|---|
| MN | 90 | 283 | 46 | 16,25% | 16,46% | **−0,21pp** | −0,09 | 18,37% | 2,11pp | **ĐÓNG** |
| MT | 90 | 219 | 30 | 13,70% | 16,51% | **−2,81pp** | −1,12 | 18,37% | 4,67pp | **ĐÓNG** |
| MB | 90 | 90 | 15 | 16,67% | 23,71% | **−7,04pp** | −1,57 | 27,55% | 10,88pp | **ĐÓNG** |

**Cửa sổ 30 ngày:** MN −0,53pp (z −0,14) · MT −4,45pp (z −1,03) · MB −0,13pp (z −0,02) — **cả ba ĐÓNG**.

Ngưỡng owner ký 01/08 là **hơn bừa ≥3pp VÀ z ≥2**. Không ô nào trong sáu ô đạt. Cả sáu đều **âm**, tức hệ vẫn thua mặt bằng đánh bừa.

### 3.7 Phát hiện A — cổng lợi thế không có bản ghi hằng ngày

Bảng `edge_gate_daily` chỉ có **3 dòng, đều ngày 2026-08-01 22:01:25**. Hôm nay là 03/08 — **hai ngày trắng**.

Truy nguyên: `crontab -l | grep -c 10945` = **0**, không có lịch nào gọi. Chỗ duy nhất nạp module là `main.py:15417` trong `/api/admin/edge-gate`, và hàm đó gọi `compute_view()` — mà `compute_view()` **chỉ tính, không ghi**; chỉ `main()` mới gọi `ghi()`.

Hệ quả cần nói cho đúng mức: panel `/monitoring` **vẫn hiện số đúng** vì nó tính tươi mỗi lần mở, nên **không có chuyện màn hình nói sai**. Cái mất là **chuỗi ngày để nhìn xu hướng**, và lời tự nhận trong chính docstring của module — *"tự chấm mỗi ngày, hiện lên màn hình — không phụ thuộc trí nhớ ai"* — hiện **chưa đúng với thực tế**.

### 3.8 Phát hiện B — thủ phạm thật khiến lane hết hạn vẫn ghi (FU-185 / FU-189)

V10974 hôm qua đóng FU-189 ở trạng thái `CLOSED_FAIL` vì thấy `MB_FULL_POOL_D_W06_V1` và `MB_TOPK10_W04_V2` vẫn ghi 1 dòng ngày 02/08 lúc 17:43, dù cron đã cắt. Hôm nay tìm ra **vì sao**.

Mọi dòng cron của `_v10679` và `_v10680` **đã comment sạch** từ V10919 (kiểm lại: không còn dòng nào sống). Nhưng file `web/backend/_mb_advanced_lane_daily.sh` vẫn chứa:

```bash
$PY _v10679_full_pool_d_w06_lane.py --region MB --date "$TODAY"
$PY _v10680_topk_strength_lane.py --region MB --date "$TODAY"
```

Và file `.sh` này có cron `43 17 * * *` — **đúng khớp** dấu thời gian 17:43 của các dòng bị phát hiện. Log `mb_advanced_lane.log` ngày 02/08 xác nhận nguyên văn:

```
[v10679_lane_d_w06] region=MB date=2026-08-02 exp=MB_FULL_POOL_D_W06_V1 status=OK BT=73 ... errors=0
[v10680_topk_lane]  region=MB date=2026-08-02 exp=MB_TOPK10_W04_V2 K=10 status=OK BT=73 ... errors=0
=== 2026-08-02T17:43:06+07:00 MB advanced lane daily DONE ===
```

Tức **cắt cron trực tiếp không cắt được đường này** — script driver gọi thẳng. Bản MT (`_mt_advanced_lane_daily.sh`) **không** có hai dòng đó, nên chỉ MB bị.

Thêm một chỗ thừa phát hiện luôn: `_mb_advanced_lane_daily.sh` có **hai** dòng cron — `43 17` (dòng 52) và `38 17` (dòng 66) — nên nó **chạy 2 lần mỗi ngày**.

**Mức hại: thấp.** Log ghi rõ `official_tables_touched: 0`, `output_impact: False`; mọi dòng ghi ra đều `output_eligible=0`. Chỉ tốn compute và làm nhiễu bảng thí nghiệm, không chạm số công bố.

Xu hướng số dòng lane hết hạn ghi vào các bảng `du_doan_test_*`:

| Ngày | Số dòng | Lane còn ghi |
|---|---|---|
| 31/07 | **68** | MN+MT+MB: DIR1/2/3, FULL_POOL, TOPK, DOCTRINE, PROMPT_V2 |
| 01/08 | **19** | MN DIR1/2/3 + MN_DOCTRINE + PROMPT_V2 (buổi sáng, trước khi V10919 cắt) + MB FULL_POOL/TOPK |
| 02/08 | **10** | **chỉ còn** MB_FULL_POOL_D_W06_V1 + MB_TOPK10_W04_V2 |
| 03/08 | **0** tính tới 08:51 | lane MB chạy 17:43 chiều nay, dự kiến +10 |

*(Ghi chú phương pháp: lượt quét đầu tiên của em trả về 0 và suýt kết luận sai là "đã sạch". Nguyên nhân ở mục 7.)*

### 3.9 Phát hiện C — hook đầu phiên im 2 ngày

`docs/_BRIEFING_DAU_PHIEN.txt` mang dấu `# Sinh tự động lúc 2026-08-01 23:05:00`, nội dung bên trong còn ghi *"KIỂM ĐẦU PHIÊN — 2026-08-01 · 4 checkpoint quá hạn · 38 mục treo"*. Chạy tay bộ kiểm hôm nay ra **0 quá hạn · 79 mục treo**. Nghĩa là hook `sessionStart` **không chạy ít nhất 2 ngày** (02/08 và 03/08).

Đây là chỗ đáng lo hơn con số của nó: hook này dựng ra **chính để chặn** lỗi sáng 01/08 (agent đi hỏi owner việc đã ký trong roadmap từ 25/06). Lưới an toàn tự tắt mà không kêu — đúng loại "xanh giả" mà quy tắc phòng.

### 3.10 FU-225 — UI `/du-doan-test` và `/filter`

| Phép kiểm | Kết quả |
|---|---|
| Nội dung `du-doan-test.html` VPS vs local | **0 dòng khác / 4002 dòng** (`difflib.unified_diff`) |
| Lệch dung lượng | 4002 byte (VPS 221.956 · local 217.954) — **đúng bằng số dòng** → VPS lưu CRLF, local lưu LF. **Không phải trôi nội dung** |
| Marker V10964 (cả hai bên) | `pageDateAnchor` ×2 · `blocked_test_bundle` ×3 · `display_date_anchor` ×4 |
| `/filter` | **200** + `Cache-Control: no-store, no-cache, must-revalidate, max-age=0` ✅ đúng bản vá V10964b |
| `/du-doan-test` | **401** khi gọi trần — đúng thiết kế trang admin, không phải lỗi |
| Tiến trình phục vụ | **PID 645169**, khởi động **02/08 18:13:33** = đúng mốc deploy V10964b |

Phần thuộc về hệ **đã đạt hết**. Còn đúng một việc máy không làm thay được: owner hard-refresh và xác nhận mắt thấy.

### 3.11 FU-243 — canh bundle thiếu phiếu

**MN hôm nay không bị lọc phiếu.** `final_bundles.model_count = 15`; `predictions` `run_source='auto_daily'` có 16 model riêng (15 official + `combo-super`). Đủ 15/15, `is_fallback=0`.

| Ngày | MN | MT | MB |
|---|---|---|---|
| 03/08 | **15** ✅ | chờ chiều | chờ chiều |
| 02/08 | 15 ✅ | **13** (thiếu 2: `meta-learning` bt_gate + `gemini-2.5-pro` MT_top13) | **14** (thiếu 1: `random-forest` bt_gate) |
| 01/08 | 13 | 13 | 14 |

Ngưỡng FU-243 là *"≥3 ngày/tuần incomplete cùng pattern mà không ghi exclusion → escalate"*. **Chưa chạm.**

### 3.12 Đối chiếu V10974 — bốn mục đã đóng hôm qua

Đọc `REPORT_V10974.md` rồi soi lại `docs/FOLLOW_UP_TRACKER.md`: cả bốn đều đã ghi đúng.

| Mục | Trạng thái trong tracker | Khớp report? |
|---|---|---|
| FU-184 · KS0802-2 | `CLOSED_PASS`, đóng 02/08, bằng chứng `exclusion_reasons.json` → `fu184_ballot_eq` MT/MB 01–02/08 `ranked0==bach_thu` True cả 4 dòng | ✅ |
| FU-189 · KS0802-1 | `CLOSED_FAIL`, đóng 02/08, ghi rõ phần pass và phần fail, `next` trỏ sang FU-185 | ✅ |
| FU-242 · KS0805 | `CLOSED_PASS`, đóng 02/08 | ✅ |
| FU-243 · SC0805 | `MEASURED_ROOT_CAUSE`, hạn 05/08, có ngưỡng bằng số | ✅ |

Hôm nay bổ sung đúng phần V10974 còn để ngỏ: FU-189 fail **vì sao** — đã trả lời ở mục 3.8.

---

## 4. Hướng xử lý và vì sao chọn

Ba phát hiện mới đều **không sửa trong phiên**. Lý do cho từng cái, và phương án đã cân nhắc rồi loại:

**A — cổng lợi thế không ghi ngày.** Cách sửa hiển nhiên là thêm một dòng cron gọi `_v10945_edge_gate.py` mỗi tối. Loại vì hai lẽ: (1) đụng crontab production trong cửa sổ đóng băng **QD-014**; (2) owner giao phiên này là *kiểm tra đầu ngày*, không phải phiên thay đổi. Cân nhắc phương án nhẹ hơn — gọi API `/api/admin/edge-gate` để nó tự ghi — nhưng đọc code thấy `compute_view()` không ghi, nên cách đó **không có tác dụng**. Và quan trọng nhất: **thiệt hại thực tế bằng không** vì panel vẫn tính tươi, bảng này là bảng chẩn đoán (`diagnostic_only=1`, `shadow_only=1`, `output_eligible=0`), không có đường nào ra số công bố. Hoãn được → hoãn, ghi **FU-244** hạn 10/08 kèm gợi ý mốc 20:30 (sau khi chấm điểm 20:20).

**B — lane hết hạn còn ghi.** Sửa là bỏ 2 dòng trong `_mb_advanced_lane_daily.sh` và gộp 2 dòng cron trùng. Loại vì đúng lý do trên: đụng file và crontab production trong cửa sổ đóng băng, mà mức hại đã đo được là **thấp** (`official_tables_touched: 0`, `output_impact: False`). Xu hướng cũng đang tự đi xuống đúng hướng (68 → 19 → 10). Ghi root cause thật cụ thể vào **FU-185**, dời hạn sang 10/08 để làm gọn một lượt sau freeze.

**C — hook đầu phiên.** Chỗ này khác hai chỗ trên: nó **không** thuộc production, chỉ là file cấu hình công cụ ở máy local. Nhưng em vẫn **không sửa** `.cursor/hooks.json` vì **chưa biết nguyên nhân** — script hook chạy tay thì tốt, `hooks.json` khai báo đúng, nên vấn đề nằm ở phía Cursor có gọi hay không, sửa mò lúc này chỉ tạo thêm biến. Việc làm được ngay và đã làm: **chạy tay để file tươi lại**. Ghi **FU-245** hạn 04/08 với phép thử rõ ràng — sáng mai xem dấu thời gian trong file có phải ngày hôm đó không.

Nguyên tắc chung áp dụng cho cả ba: playbook cho phép *"lỗi rõ ràng có bằng chứng thì sửa ngay trong phiên"*, nhưng cả ba đều là **hở về khả năng quan sát, không phải lỗi làm sai số**, và đều rơi trúng cửa sổ đóng băng. Đo cho chắc rồi xếp hàng có ngưỡng bằng số là đúng hơn là chen vào sửa.

---

## 5. Đã làm gì

**Không deploy. Không restart. Không sửa file nào trên VPS. Không ghi dòng nào vào DB.**

### 5.1 Script mới (chỉ đọc, chạy từ máy local)

| File | Việc |
|---|---|
| `web/backend/_v10975_dau_ngay_probe.py` | Chụp health · service/PID · cron · journal · hash 4 bảng |
| `web/backend/_v10975_dau_ngay_probe2.py` | Lấy schema thật 4 bảng (vòng 1 query sai cột) |
| `web/backend/_v10975_dau_ngay_probe3.py` | Query lại đúng cột: bundle · predictions · results · MDE · consistency · edge gate |
| `web/backend/_v10975_fe_diff.py` | So từng dòng `du-doan-test.html` local vs VPS (FU-225) |
| `web/backend/_v10975_edge_lane_final2.py` | Tính tươi cổng lợi thế 30d/90d **không ghi bảng** |
| `web/backend/_v10975_lane_rescan.py` | Quét lane hết hạn còn ghi, có cột `run_date` |
| `web/backend/_v10975_who_fires.py` | Truy ai còn gọi `_v10679`/`_v10680` lúc 17:43 |
| `web/backend/_v10975_result_sanity.py` | Đối chiếu số đài 02/08 với 6 Chủ Nhật gần nhất |
| `web/backend/_v10975_docs_update.py` | Ghi 3 tài liệu quản trị bằng `_doc_prepend.prepend()` |

### 5.2 Tài liệu đã ghi (đều dùng `prepend()`, không dùng chế độ `"w"`)

| File | Trước | Sau | Thêm |
|---|---|---|---|
| `CHANGELOG.md` | 1.924.059 | 1.927.157 | +3.098 |
| `docs/CURRENT_TRUTH_SSOT.md` | 918.246 | 919.408 | +1.162 |
| `docs/FOLLOW_UP_TRACKER.md` | 982.551 | 989.619 | +7.068 |

Cả ba đều **dài ra**, không file nào ngắn đi — `prepend()` sẽ ném `DocShrinkError` nếu ngắn đi.

### 5.3 Mục theo dõi đã đổi

| Mục | Trước | Sau |
|---|---|---|
| FU-185 · DD0803 | `MEASURED_BUT_NOT_FIXED` hạn 03/08 | **`MEASURED_ROOT_CAUSE`** hạn 10/08 + root cause cụ thể |
| FU-225 · UI0803 | `DEPLOYED_PENDING_OWNER_VERIFY` | **giữ nguyên** + bằng chứng máy đã đạt hết |
| FU-243 · SC0805 | `MEASURED_ROOT_CAUSE` | **giữ nguyên** + số canh ngày 03/08 |
| FU-244 · KS0810 | — | **mới** — cổng lợi thế không ghi ngày, hạn 10/08 |
| FU-245 · SC0804 | — | **mới** — hook đầu phiên im 2 ngày, hạn 04/08 |

### 5.4 Việc sửa duy nhất trong phiên

Chạy tay `python .cursor/hooks/session_start_briefing.py` → `docs/_BRIEFING_DAU_PHIEN.txt` tươi lại từ **01/08 23:05** thành **03/08 09:00**, nội dung đúng (0 quá hạn · 79 mục treo). Đây là file tóm tắt ở máy local, không phải production.

### 5.5 Mốc hash 4 bảng khoá (03/08 08:51)

| Bảng | Số dòng | SHA256 (20 ký tự đầu) |
|---|---|---|
| `predictions` | 11.592 | `0b84203853b2aeba70a2` |
| `final_bundles` | 469 | `85dd4a7840a576f7473b` |
| `lottery_results` | 15.201 | `06e0bbf0e4da50c8f1bb` |
| `model_daily_eval` | 11.415 | `dcfad896d0328071def7` |

Phiên chỉ đọc nên không có hash "sau" để so — mốc này ghi lại làm chuẩn cho phiên chiều.

---

## 6. Cổng kiểm

| Phép | Kỳ vọng | Thực tế | Đạt |
|---|---|---|---|
| Briefing đầu phiên chạy trước khi trả lời | bắt buộc | đã chạy 08:49 | ✅ |
| Checkpoint quá hạn | 0 | **0** | ✅ |
| Sổ quyết định TRÔI | 0 | **0** / 19 | ✅ |
| `/api/health` | 200 | **200** | ✅ |
| Service `lottery` | active | **active** PID 645169 | ✅ |
| Journal traceback hôm nay | 0 | **0** | ✅ |
| `scheduler_logs` ERROR hôm nay | 0 | **0** | ✅ |
| Tự kiểm nhất quán | 16/16 | **16/16** (02/08 18:05) | ✅ |
| MN chốt đúng 15 model | 15 | **15** | ✅ |
| MN không phải bản dự phòng | `is_fallback=0` | **0** | ✅ |
| Kết quả 02/08 đủ 3 miền | 3/3/1 đài | **3/3/1** | ✅ |
| Chấm 02/08 xong | 0 dòng NULL | **0** | ✅ |
| Cổng lợi thế còn ĐÓNG | ĐÓNG 3 miền | **ĐÓNG 6/6 ô** (30d + 90d) | ✅ |
| Đọc cổng lợi thế không ghi thêm dòng | vẫn 3 dòng 01/08 | **3 dòng, 2026-08-01 22:01:25** | ✅ |
| FU-225 file VPS ≡ local | 0 dòng khác | **0 / 4002** | ✅ |
| `/filter` có `no-store` | có | **có** | ✅ |
| Không đụng production | 0 thay đổi | **0** | ✅ |
| Không ghi Notion (§57) | 0 lệnh ghi | **0** | ✅ |
| 3 tài liệu quản trị đã ghi | dài ra | **+3.098 / +1.162 / +7.068** | ✅ |
| Báo cáo công khai đủ 9 phần | đủ | file này | ✅ |
| `_v10921_report_gate.py V10975` | PASS | xem mục 6.1 | — |

### 6.1 Kết quả cổng báo cáo

Nguyên văn hai lượt chạy lưu ở `evidence/report_gate_V10975.txt`.

**Lượt soát riêng V10975 — ĐẠT, mã thoát 0:**

```
V10975  ✓ V10975_KIEM_DAU_NGAY_20260803   đủ 9 phần, đã commit
        evidence/: 10 tệp
commit chưa push: KHÔNG
✓ MỌI PHIÊN BẢN ĐỀU CÓ BÁO CÁO ĐẦY ĐỦ VÀ ĐÃ PUSH
```

**Lượt soát toàn bộ — mã thoát 1, nhưng lỗi không thuộc phiên này:**

```
V10976  ✗ KHÔNG CÓ BÁO CÁO — A55_VIOLATION_REPORT_MISSING
V10975  ✓ đủ 9 phần, đã commit
V10974  ✓ ... V10969 ✓   (7 phiên bản trước đều đạt)
```

**V10976 là việc của một phiên khác đang chạy song song** trong cùng workspace sáng nay — phiên sửa 5 lỗi *"xanh giả"* nằm trong chính các cổng tự kiểm (do Bugbot rà ra). Phiên đó đã viết mục V10976 vào `CHANGELOG.md` nhưng chưa đẩy báo cáo công khai, nên cổng bắt đúng. Xem mục **7.7** — phiên này đã vô tình commit kèm mục CHANGELOG đó.

Điều đáng ghi nhận: cổng bắt được V10976 **chính là nhờ** bản vá L4 của phiên V10976 — trước đó `_v10921_report_gate.py` in ra *"✗ thiếu"* xong vẫn **luôn thoát 0**. Nay thoát 1. Lượt chạy này là bằng chứng cổng đã thật sự chặn được.

### 6.2 Commit và push

| Repo | Commit | Push |
|---|---|---|
| Riêng `Lottery_AI_Test` | `cf7ec2d` | `ac8ef4e..cf7ec2d master -> master` ✅ |
| Công khai `Lottery_AI_Notion_Reports` | `1ecba64` | `0692b57..1ecba64 main -> main` ✅ |

Quét khoá API trước khi push: **0 khoá** trên 12 tệp (khuôn dò `sk-ant-` · `sk-proj-` · `AIza…` · `gsk_` · `xai-` · `ghp_` · `PRIVATE KEY` · `api_key=…`).

---

## 7. Vướng vấp

**7.1 — Quét lane hết hạn lần đầu trả về 0, suýt kết luận sai là "đã sạch".** Script quét của em nhận diện cột ngày theo danh sách `("date", "date_str", "target_date", "day")` — **thiếu `run_date`**, mà đó đúng là cột các bảng `du_doan_test_*` dùng. Kết quả: 0 dòng, trong khi thực tế có 97 dòng từ 31/07. Nếu không đối chiếu ngược với `fu189_retired_detail.json` của V10974 thì đã báo cáo với owner rằng FU-189 đã tự sạch — **sai hoàn toàn, và sai theo hướng trấn an**, loại sai nguy hiểm nhất. Đã quét lại với `run_date` và ra đúng 97 dòng. *Hậu quả nếu bỏ qua:* FU-185 bị đóng nhầm, hai lane MB tiếp tục chạy vô hạn không ai canh.

**7.2 — Ba vòng query đầu sai tên cột.** Em đoán schema (`predictions.region`, `final_bundles.bundle_json`, `v10900_consistency_guard.created_at`, `scheduler_logs.status`) thay vì đọc `pragma_table_info` trước. Bốn query trả `Error: no such column`. Mất một vòng. Tên thật là `target_region`, `source_predictions_json`, `computed_at_vn`, `log_level`. *Bài học:* lấy schema trước khi viết query, đừng đoán.

**7.3 — Hash 4 bảng vòng đầu ra `e3b0c44298fc1c14` cho cả bốn bảng.** Đó là SHA256 của **chuỗi rỗng** — heredoc `.mode csv` trong `sqlite3` không nuốt được lệnh, nên `sha256sum` băm rỗng. Bốn giá trị giống hệt nhau lẽ ra phải làm em nghi ngay. Đã sửa sang `sqlite3 -csv` và ra bốn hash khác nhau. *Hậu quả nếu bỏ qua:* ghi vào báo cáo bốn hash giả, lần sau so sẽ ra "không đổi" một cách vô nghĩa.

**7.4 — Hai lần chạy `python -c` với chuỗi qua `json.dumps` bị `SyntaxError`.** Ký tự `\n` vào tới shell thành hai ký tự literal. Đã chuyển sang upload script tạm vào `/tmp` qua SFTP rồi chạy, xoá sau. *Bài học:* đúng như bảng mẹo trong `CLAUDE.md` — viết ra file script, đừng nhồi vào `python -c`.

**7.5 — `Get-Content` hiển thị tiếng Việt thành ký tự lạ**, làm em thoáng tưởng đã ghi hỏng `_BRIEFING_DAU_PHIEN.txt`. Thực ra file hoàn toàn đúng UTF-8, chỉ là PowerShell 5.1 đọc theo bảng mã ANSI. Đọc lại bằng công cụ đọc file thì bình thường. *Bài học:* đừng kết luận file hỏng dựa trên hiển thị của PowerShell.

**7.6 — Hai lệnh đầu phiên dùng `&&` bị PowerShell từ chối.** Không phải bash. Nhỏ, nhưng mất một lượt.

**7.7 — Vô tình commit kèm việc của một phiên khác đang chạy song song.** Sáng nay có **hai phiên cùng làm trong workspace này**: phiên của em (V10975, kiểm đầu ngày) và một phiên V10976 sửa 5 lỗi *"xanh giả"* trong các cổng tự kiểm. Phiên V10976 đã ghi mục của họ vào `CHANGELOG.md`, `docs/CURRENT_TRUTH_SSOT.md` và `docs/FOLLOW_UP_TRACKER.md` nhưng **chưa commit**. Em chạy `git add CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md docs/FOLLOW_UP_TRACKER.md` để đưa phần của mình vào, và **cuốn luôn phần của họ** vào commit `cf7ec2d` mang tên V10975.

Kiểm lại cụ thể: `git log -S'## V10976' -- CHANGELOG.md` chỉ ra đúng `cf7ec2d` — tức mục V10976 vào lịch sử qua commit của em. `docs/CURRENT_TRUTH_SSOT.md` có 3 dòng nhắc V10976, `docs/FOLLOW_UP_TRACKER.md` có 5 dòng.

*Mức hại:* thấp và **không mất gì** — nội dung của họ được commit chứ không bị đè hay bị bỏ. Các file **code** của phiên V10976 (`_v10921_report_gate.py`, `_v10920_decision_ledger.py`, `_v10920_session_start.py`, `_v10925_rule_sync_check.py`) em **không** thêm vào, vẫn nằm nguyên chưa commit trong thư mục làm việc để họ tự xử.

*Hệ quả duy nhất:* mục V10976 nay nằm trong CHANGELOG đã commit mà chưa có báo cáo công khai → cổng A55 chạy toàn bộ báo `A55_VIOLATION_REPORT_MISSING` cho V10976 cho tới khi phiên đó đẩy báo cáo.

*Đã cân nhắc rồi loại:* gỡ mục V10976 ra khỏi commit. Loại vì phiên kia đang chạy — đụng vào file họ đang sửa dở thì rủi ro hỏng việc của họ cao hơn hẳn cái lợi của một lịch sử commit gọn gàng.

*Bài học:* trong workspace có thể có phiên khác chạy song song, `git add <file>` trên tài liệu quản trị dùng chung là **không an toàn**. Lần sau phải `git status` và `git diff` từng file trước khi add, hoặc dùng `git add -p` để chỉ lấy đúng khối của mình.

**7.8 — Chưa tìm ra vì sao hook `sessionStart` không chạy.** Đã kiểm: `.cursor/hooks.json` khai báo đúng, script chạy tay ra kết quả đúng. Nguyên nhân nằm ở phía Cursor có gọi hook hay không — nằm ngoài chỗ em soi được trong phiên. Đã ghi FU-245 kèm phép thử cho sáng mai thay vì sửa mò.

---

## 8. Gỡ về

Phiên này **không deploy, không đụng production**, nên không có gì trên VPS phải gỡ. Chỉ có thay đổi ở máy local:

```powershell
# Gỡ 3 tài liệu quản trị về trạng thái trước phiên
cd E:\Lottery_AI_Test
git checkout -- CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md docs/FOLLOW_UP_TRACKER.md

# Gỡ file briefing (nếu muốn về bản 01/08)
git checkout -- docs/_BRIEFING_DAU_PHIEN.txt

# Xoá 9 script probe của phiên (đều chỉ đọc, xoá không ảnh hưởng gì)
Remove-Item web\backend\_v10975_*.py

# Xoá thư mục báo cáo công khai
Remove-Item -Recurse E:\Lottery_AI_Notion_Reports\V10975_KIEM_DAU_NGAY_20260803
```

Thời gian gỡ: **dưới 1 phút**. Không cần restart gì, không cần khôi phục DB.

Trên VPS có 2 file tạm từng được tạo trong `/tmp` (`_v10975_edge.py`, `_v10975_scan.py`, `_v10975_scan2.py`) — **đã tự xoá ngay sau khi chạy** bằng `rm -f` trong chính script.

---

## 9. Theo dõi tiếp

| Mã máy | Mã đọc | Nhãn | Hạn | Trạng thái | Ngưỡng hành động bằng số |
|---|---|---|---|---|---|
| **FU-245** | **SC0804** | Hook đầu phiên im 2 ngày | **04/08** | `MEASURED_ROOT_CAUSE` | Sáng 04/08 mở `docs/_BRIEFING_DAU_PHIEN.txt`: nếu dấu thời gian **không phải 04/08** → hook hỏng thật, chuyển sang gọi bộ kiểm thẳng trong quy trình |
| **FU-225** | **UI0803** | Xác minh UI du-doan-test + filter | **03/08 → chờ owner** | `DEPLOYED_PENDING_OWNER_VERIFY` | Owner hard-refresh `/du-doan-test` (MN/MT/MB) + `/filter?tab=overview` → `CLOSED_PASS`. Tới **05/08** owner chưa xem thì nhắc lại, **không tự đóng** |
| **FU-243** | **SC0805** | Canh incomplete bundle do gate | **05/08** | `MEASURED_ROOT_CAUSE` | MN 03/08 **15/15 sạch**. Canh MT/MB chiều nay. Chạm **≥3 ngày/tuần** incomplete cùng pattern mà không ghi exclusion → escalate |
| **FU-185** | **DD0803 → hạn 10/08** | Tinh gọn lane hết hạn vẫn chạy | **10/08** | `MEASURED_ROOT_CAUSE` | Sau 08/08: bỏ 2 dòng gọi lane trong `_mb_advanced_lane_daily.sh` + gộp 2 dòng cron trùng (`43 17` / `38 17`). Nếu 04–05/08 vẫn đúng 10 dòng/ngày thì khỏi đo thêm |
| **FU-244** | **KS0810** | Cổng lợi thế không ghi ngày | **10/08** | `MEASURED_ROOT_CAUSE` | Sau 08/08: thêm cron `_v10945_edge_gate.py` lúc **20:30** (sau chấm điểm 20:20). Tới 10/08 vẫn không có dòng cho ngày mới → escalate |
| **FU-215** | **DB0808** | Đóng băng đường ra số (QD-014) | 08/08 | `OWNER_LOCK` | Hết 08/08 mới mở; trước đó mọi thay đổi đường ra số đều bị chặn |

### Việc của phiên khác, không thuộc V10975 nhưng đang treo

- **V10976 chưa có báo cáo công khai** → cổng A55 chạy toàn bộ báo `A55_VIOLATION_REPORT_MISSING`, mã thoát 1. Mục CHANGELOG của V10976 đã nằm trong lịch sử qua commit `cf7ec2d` (xem mục 7.7), nên vi phạm này sẽ còn hiện cho tới khi phiên V10976 đẩy thư mục báo cáo của họ. **Phiên này không viết thay báo cáo đó** — không đủ ngữ cảnh về việc họ làm, viết thay là bịa.

### Việc cần canh ngay trong hôm nay

- **MT chốt ~16:41** và **MB chốt ~17:37** — kiểm `model_count` có đủ 15 không, hay lại 13/14 như 02/08 (FU-243).
- **Lane MB 17:43** — dự kiến ghi thêm 10 dòng lane hết hạn (FU-185). Nếu **không** ghi thì có thứ khác đã đổi, phải tìm hiểu.
- **Tự kiểm nhất quán 18:05** — kỳ vọng 16/16.
- **Chấm điểm 20:20** — kỳ vọng 27 model × 3 miền, 0 dòng NULL.

### Không áp dụng trong phiên này

- **Deploy / restart / hash sau:** không áp dụng vì phiên chỉ đọc, không thay đổi gì trên VPS.
- **Panel `/monitoring` mới theo §52:** không áp dụng vì phiên không dựng bảng đo shadow mới — hai FU mới (244, 245) là hở về khả năng quan sát của bộ đã có, không phải phép đo mới.
- **Notion:** không áp dụng — §57/A55 cấm mọi thao tác ghi; phiên này không gọi hàm ghi Notion nào.

---

*Báo cáo lập 03/08/2026 · mọi mốc giờ là giờ Việt Nam (`Asia/Ho_Chi_Minh`, UTC+7).*
