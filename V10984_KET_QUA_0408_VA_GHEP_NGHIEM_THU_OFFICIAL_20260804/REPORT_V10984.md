# V10984 — Ghép `/nghiem-thu` với official: đo thẳng thì không cách nào hơn official

**Ngày:** 04/08/2026 · **Giờ VN:** 21:37 → 22:3x · **Trạng thái:** ✅ deploy xong, cổng kiểm đạt hết

**Commit riêng:** `a2a7e61` (chính) + `162412e` (sửa đồng bộ dữ liệu sống) ·
**Commit công khai:** `4ff1651`

> **Phiên bị gián đoạn giữa đường** (owner hết token API) đúng lúc đang chạy vòng kiểm cuối —
> toàn bộ việc thực chất đã xong trước đó (deploy 21:59, hai commit đã push). Sau khi nối lại đã
> chạy lại đủ 5 cổng kiểm và nghiệm thu lại trên VPS: **không có việc nào dở dang**. Ghi lại để
> không ai tưởng có phần bị bỏ giữa.

---

## 1. Tóm tắt

Owner nói *"chán ngán kết quả dự đoán quá tệ"*, muốn kế hoạch triển khai sớm hơn dự kiến, và
quan sát thấy *"official cũng khá tiềm năng"* nên muốn **kết hợp `/nghiem-thu` với official**.

Ba câu trả lời bằng số:

1. **Hôm nay 04/08 official trúng 1/3 miền** — MT bạch thủ **60 TRÚNG** ở Đắk Lắk; MN 22 và MB 71
   trượt. **Lane `/nghiem-thu` trúng 0/3.** MT là ô duy nhất hai luồng ra số khác nhau, và lane
   nghiệm thu chọn 29 — trượt.
2. **Ghép hai luồng KHÔNG hơn official.** Trên toàn bộ 15 ô đo tiến mà lane có (30/07→04/08):
   hai luồng ra **cùng số ở 11/15 ô (trùng lặp 73,33%)**, và ở 4 ô lệch nhau thì **official
   đúng cả 4, nghiệm thu sai cả 4** — không hề bù trừ. Cả ba cách ghép đều tệ hơn official một
   mình. Nhưng cỡ mẫu 15 ô / 35 lượt đặt là **quá nhỏ để kết luận** (z của official chỉ 1,30).
3. **Cảm nhận "official khá tiềm năng" đúng với 7 ngày, sai với 30/90/180 ngày.** 7 ngày gần
   nhất official trúng **9/21 ô miền-ngày = 42,9%** — có cơ sở thật. Nhưng cổng lợi thế
   `QD-013` vẫn **ĐÓNG cả 6 ô**, z cao nhất chỉ 1,20, và 90 ngày thì MN −0,36pp · MT −2,94pp ·
   MB −7,23pp.

Đã dựng và deploy **bảng đo bóng** `ghep_nt_official_daily` + API admin + panel `/monitoring`
(làm mới 60s) + 2 dòng cron tự cập nhật, kèm **ngưỡng hành động viết sẵn**. Kéo **FU-244** (cron
cổng lợi thế) từ 07/08 về **xong 04/08**. 4 bảng khoá hash **giữ nguyên**, `QD-014` còn khớp
7/7.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **04/08/2026 21:35 (giờ VN):**
>
> *"Thực sự quán chán ngán kết quả dự đoán quá tệ anh cần một kế hoạch triển khai sơm hơn dự
> kiến em xem thử dùm anh có triển khai được gì trước không em ? Theo như anh quan sat thấy
> offical cũng khá tiềm năng chứ em, cần 1 sự kết hợp hoàn hảo ở /nghiem-thu và offical nha .
> Kết quả dự đoán ngày hôm nay thế nào em thử tổng lực dùm anh."*

Tách thành ba việc:

| | Yêu cầu |
|---|---|
| **(A)** | Kết quả dự đoán hôm nay 04/08 thế nào — đo tổng lực |
| **(B)** | Kết hợp official + lane `/nghiem-thu` vì quan sát official "khá tiềm năng" |
| **(C)** | Kế hoạch triển khai **sớm hơn dự kiến** — xem có gì làm trước được |

---

## 3. Đào bới / phát hiện

### 3.1 Nguồn số và cách đo

Đồng bộ `data/lottery_ai.db` + `web/backend/prediction_trace.jsonl` từ VPS
(`artifacts/live_sync/20260804_214352/manifest.json`). Trục đo là **theo đài** — đó mới là trục
ra tiền: hoà vốn MN/MT **18,37%**, MB **27,55%** (vốn 18k/27k, thu 98k mỗi điểm trúng, theo
`OD-20260726-A`).

Mặt bằng "đánh bừa" **đo thật** bằng cách thử cả 100 số 00–99 trên chính kết quả những ngày đã
đặt — không dùng con số 1% lý thuyết. Dùng đúng phương pháp của `_v10945_edge_gate` để số so
được trực tiếp với cổng `QD-013`.

**Kiểm chéo cách chấm trước khi dùng:** tự tính lại "trúng hay trượt" từ `prizes_json` rồi so
với `bach_thu_status` mà hệ tự ghi — **khớp 3/3 ô** hôm nay. Nên cách chấm dùng trong báo cáo
này là cách chấm của chính hệ, không phải cách riêng.

### 3.2 (A) Kết quả hôm nay 04/08 — kết quả về đủ 3 miền

Thứ Ba: MN 3 đài · MT 2 đài · MB 1 đài — khớp đúng lịch, **không đài nào thiếu**.

| Miền | Đài | Đuôi ĐB | Official bạch thủ | Kết quả | Lane `/nghiem-thu` | Kết quả |
|---|---|---|---|---|---|---|
| MN | Bạc Liêu · Bến Tre · Vũng Tàu | 93 · 20 · 88 | **22** | **TRƯỢT** (0/3 đài) | 22 (giống) | **TRƯỢT** |
| MT | Quảng Nam · Đắk Lắk | 20 · 82 | **60** | **TRÚNG — Đắk Lắk** (1/2 đài) | 29 (**khác**) | **TRƯỢT** |
| MB | Quảng Ninh | 25 | **71** | **TRƯỢT** (0/1 đài) | 71 (giống) | **TRƯỢT** |

**Official 1/3 miền · lane nghiệm thu 0/3.**

Lô và xiên:

| Miền | lô2 | Kết quả | lô3 | xiên2 | xiên3 |
|---|---|---|---|---|---|
| MN | 22 · 72 | **PARTIAL** — 72 về Bến Tre, 22 không về | 122 LOSE | LOSE | N/A |
| MT | 60 · 32 | **WIN** — 60 về Đắk Lắk, 32 về Quảng Nam | 060 LOSE | LOSE | LOSE |
| MB | 71 · 63 | LOSE — cả hai không về | 771 LOSE | LOSE | LOSE |

**Vì sao lô2 MT thắng mà xiên2 MT trượt — đúng luật, không phải lỗi:** 60 về Đắk Lắk, 32 về
Quảng Nam. Lô tính theo miền nên cả hai đều "về"; xiên đòi cùng một đài nên không thành.

`model_daily_eval` đã chấm xong **81 dòng = 27 model/miền** lúc 20:20. Model đúng nhất hôm nay:

| Miền | Model trúng bạch thủ | Số |
|---|---|---|
| MT | `combo-super` (37) · `gemini-3.5-flash` (82) · `gpt-5.4` (31) — đều `hit_count` 2 | 3 model |
| MN | `grok-4.3` (72) — **WIN**, `hit_count` 2 · thêm 6 model `PARTIAL` trúng bạch thủ | 7 model |
| MB | `lstm` (82) · `qwen3-max-thinking` (72) — `PARTIAL` | 2 model |

**Đáng chú ý:** MN số **72** về thật và nằm trong lô2 official, nhưng bạch thủ official chọn
**22** (không về). `grok-4.3` chọn đúng 72. Ở MB, số official chọn (71) **không đài nào có**, và
25/27 model MB đều trượt — hôm nay MB gần như cả bảng sai.

### 3.3 (B) Lane `/nghiem-thu` thật sự có bao nhiêu ngày dùng được

Đây là phát hiện quan trọng nhất của phần (B). Bảng `du_doan_test_bundles` có **8.767 dòng /
123 ngày / 83 experiment**, nhìn qua tưởng nhiều. Nhưng:

| Mode | Dòng | Ngày | Dùng được? |
|---|---|---|---|
| `REALTIME_AVAILABLE_ONLY` | 8.103 | 104 | lane khác, không phải `/nghiem-thu` |
| `POST_CLOSEOUT_DIAGNOSTIC_FULL_25` | 625 | 32 | **KHÔNG** — backfill hồi tố, ghi 03/05 cho ngày 04/04 |
| `SHADOW_LANE` | 21 | 7 | lane de-herd, không phải `/nghiem-thu` |
| **`OFFICIAL_NEW_CANDIDATE`** | **15** | **6** | ✅ đây là `/nghiem-thu` |
| `RETRO_POST_DRAW_BASELINE` | 3 | 1 | **KHÔNG** — hồi tố |

Lane `/nghiem-thu` = `*_NGHIEMTHU_1908_V1`, mode `OFFICIAL_NEW_CANDIDATE`, **đúng 15 ô
(ngày × miền)**: MN 6 ngày · MT 5 · MB 4, từ 30/07 → 04/08.

**Cả 15 ô đều là ĐO TIẾN** — kiểm bằng cách so `created_at` của lane với thời điểm kết quả miền
đó về: ô muộn nhất là MB 04/08 ghi 17:37:01 trong khi kết quả về 18:31:02, sớm hơn 54 phút. Đã
**loại hết** dòng hồi tố, vì bài học `V10655→V10790` là "backtest hứa hẹn rồi rữa".

### 3.4 (B) Từng ô: official vs nghiệm thu vs kết quả thật

| Ngày | Miền | Đài | Official | Nghiệm thu | Giống? | Official trúng | NT trúng | Ai hơn |
|---|---|---|---|---|---|---|---|---|
| 30/07 | MN | 3 | 86 | 86 | giống | 0/3 | 0/3 | bằng |
| 31/07 | MB | 1 | 19 | 19 | giống | 0/1 | 0/1 | bằng |
| 31/07 | MN | 3 | 09 | 09 | giống | **2/3** | **2/3** | bằng |
| 31/07 | MT | 2 | 68 | 68 | giống | 0/2 | 0/2 | bằng |
| 01/08 | MB | 1 | 90 | 90 | giống | **1/1** | **1/1** | bằng |
| 01/08 | MN | 4 | 16 | 38 | **KHÁC** | **1/4** | 0/4 | **OFFICIAL** |
| 01/08 | MT | 3 | 55 | 55 | giống | 0/3 | 0/3 | bằng |
| 02/08 | MB | 1 | 52 | 73 | **KHÁC** | **1/1** | 0/1 | **OFFICIAL** |
| 02/08 | MN | 3 | 43 | 39 | **KHÁC** | **1/3** | 0/3 | **OFFICIAL** |
| 02/08 | MT | 3 | 69 | 69 | giống | **2/3** | **2/3** | bằng |
| 03/08 | MN | 3 | 64 | 64 | giống | 0/3 | 0/3 | bằng |
| 03/08 | MT | 2 | 64 | 64 | giống | 0/2 | 0/2 | bằng |
| 04/08 | MB | 1 | 71 | 71 | giống | 0/1 | 0/1 | bằng |
| 04/08 | MN | 3 | 22 | 22 | giống | 0/3 | 0/3 | bằng |
| 04/08 | MT | 2 | 60 | 29 | **KHÁC** | **1/2** | 0/2 | **OFFICIAL** |

**Ba con số nói hết:**

1. **Độ trùng lặp 73,33%** — 11/15 ô hai luồng ra **cùng số**. Ở những ô đó "kết hợp" không tạo
   thêm gì cả, chỉ là một số nhân đôi.
2. **4 ô lệch nhau: official đúng 4/4, nghiệm thu đúng 0/4.** **Không hề bù trừ** — không có ô
   nào nghiệm thu cứu được official. Một chiều hoàn toàn.
3. Nghiệm thu trúng ở đâu thì đúng những ô nó **giống** official (31/07 MN, 01/08 MB, 02/08 MT).
   Tức là nó **chưa từng** trúng ở một ô mà nó tự chọn khác.

### 3.5 (B) Năm cách ghép — chấm bằng tiền, trục theo đài

| Cách ghép | Ô chơi | Đài đặt | Trúng | Tỷ lệ | Hơn bừa | Hơn official | z | Hoà vốn cần | Lãi mô phỏng |
|---|---|---|---|---|---|---|---|---|---|
| **OFFICIAL** | 15 | 35 | 9 | **25,71%** | +8,34pp | — | 1,30 | 19,42% | **+216.000đ** |
| NGHIEM_THU | 15 | 35 | 5 | 14,29% | −3,09pp | **−11,43pp** | −0,48 | 19,42% | −176.000đ |
| HOP_HAI_SO (chơi cả 2 số) | 15 | 45 | 9 | 20,00% | +2,63pp | **−5,71pp** | 0,47 | 19,39% | +27.000đ |
| CHI_KHI_KHOP (chỉ chơi ngày trùng) | 11 | 25 | 5 | 20,00% | +2,63pp | **−5,71pp** | 0,35 | 19,47% | +13.000đ |
| UU_TIEN_NHIEU_MODEL | 15 | 35 | 6 | 17,14% | −0,23pp | **−8,57pp** | −0,04 | 19,42% | −78.000đ |

Mặt bằng đánh bừa trên chính 15 ô này: **17,37%**.

**Đọc bảng này:**

- **Hợp hai số không cứu được gì.** Trúng vẫn đúng 9 lượt như official, nhưng số lượt đặt tăng
  35 → 45 vì 4 ô phải mua thêm một số. Lãi từ +216k tụt xuống **+27k**. Chi phí gấp đôi, thu
  không thêm.
- **Nghiệm thu một mình 14,29% — thấp hơn cả đánh bừa 17,37%.** z âm.
- **Ưu tiên bên nhiều model là cách TỆ NHẤT** (−78k): lane nghiệm thu luôn khai `model_count=15`
  còn official MT 13 / MB 14, nên luật này tự động đổi sang nghiệm thu ở MT và MB — đúng hai
  miền nghiệm thu sai.

### 3.6 (C) "Official khá tiềm năng" — kiểm bằng số 7/30/90/180 ngày

| Cửa sổ | MN | MT | MB |
|---|---|---|---|
| **7 ngày** | 22,73% (5/22) · **+6,55pp** · z **0,83** | 17,65% (3/17) · +0,83pp · z 0,09 | 42,86% (3/7) · **+19,29pp** · z **1,20** |
| 30 ngày | 15,46% (15/97) · −0,84pp · z −0,22 | 12,00% (9/75) · −4,64pp · z −1,08 | 22,58% (7/31) · −0,90pp · z −0,12 |
| 90 ngày | 16,08% (46/286) · −0,36pp · z −0,17 | 13,57% (30/221) · −2,94pp · z −1,18 | 16,48% (15/91) · −7,23pp · z −1,62 |
| 180 ngày | 16,50% (82/497) · −0,05pp · z −0,03 | 17,19% (66/384) · **+0,67pp** · z 0,35 | 22,15% (35/158) · −1,59pp · z −0,47 |

7 ngày gần nhất theo ô miền-ngày: **9/21 = 42,9%** (02/08 trúng cả 3 miền, 01/08 trúng 2).

**Kết luận thẳng:** cảm nhận của owner **có cơ sở thật trên 7 ngày** — MN +6,55pp và MB
+19,29pp là số dương thật. Nhưng:

- **Không ô nào có z ≥ 2.** Cao nhất là MB z=1,20, mà MB chỉ có **7 lượt đặt** trong 7 ngày.
- **Cửa sổ dài thì âm.** 30 ngày cả 3 miền âm; 90 ngày cả 3 âm; 180 ngày chỉ MT dương +0,67pp
  với z=0,35.
- **Cổng lợi thế `QD-013` ĐÓNG cả 6 ô.** Còn thiếu để hoà vốn (30 ngày): MN **+2,90pp** · MT
  **+6,37pp** · MB **+4,97pp**.

Đây đúng là tình huống `_v10945_edge_gate` được viết ra để chặn. Docstring của chính nó ghi sẵn
từ 01/08: *"Quyết định này rất dễ trôi. Vài tuần nữa có một tuần đẹp là lại muốn đặt lại."*

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 Yêu cầu (B) — ba phương án, chọn phương án 3

| # | Phương án | Chọn? | Vì sao |
|---|---|---|---|
| 1 | Ghép hai luồng vào `/du-doan` official ngay | ❌ **loại** | `QD-014` đóng băng đường ra số tới hết 08/08, cấm đích danh `/du-doan` writer và bộ chọn model. Và số đo cho thấy ghép **tệ hơn** official. |
| 2 | Backtest 90 ngày cách ghép rồi bật cái tốt nhất | ❌ **loại** | Lane `/nghiem-thu` chỉ tồn tại từ 30/07 nên "90 ngày" chỉ có được bằng dòng backfill hồi tố. Đúng cái bẫy V10655→V10672→V10677→V10753→V10789→V10790 — sáu lần đều rữa. |
| 3 | **Bảng đo bóng chấm 5 cách ghép, ngưỡng viết sẵn** | ✅ **chọn** | Dùng được NGAY vì không phạm `QD-014` (chỉ đọc bảng official, ghi vào bảng chẩn đoán riêng). Trả lời được câu hỏi của owner bằng số thật. Và giữ đường đo tiến cho tới khi đủ mẫu. |

### 4.2 Vì sao chọn 5 cách ghép này

Không chọn bừa — mỗi cách trả lời một giả thuyết cụ thể mà owner có thể đang nghĩ tới:

| Cách | Giả thuyết nó kiểm |
|---|---|
| `OFFICIAL` · `NGHIEM_THU` | mốc so sánh — từng bên một mình được bao nhiêu |
| `HOP_HAI_SO` | *"chơi cả hai số thì xác suất trúng cao hơn"* — đúng về xác suất, nhưng có bù được chi phí gấp đôi không? |
| `CHI_KHI_KHOP` | *"chỉ chơi khi hai bên đồng ý thì chắc hơn"* — đồng thuận có phải tín hiệu tốt? |
| `UU_TIEN_NHIEU_MODEL` | *"bên nào nhiều model hơn thì tin bên đó"* |

### 4.3 Vì sao ngưỡng đặt ở 60 ô, không phải "khi nào thấy tốt"

Ngưỡng phải viết **trước** khi nhìn số, nếu không sẽ tự nới. Bốn điều kiện đồng thời:

| # | Điều kiện | Hiện tại |
|---|---|---|
| 1 | ≥ **60** ô đo tiến | 15/60 |
| 2 | ≥ **150** lượt đặt theo đài | 35/150 |
| 3 | Hơn đường official ≥ **3pp** | tốt nhất là −5,71pp |
| 4 | Hơn bừa ≥ **3pp** VÀ z ≥ **2** (giữ nguyên `QD-013`, không nới) | +8,34pp nhưng z 1,30 |

---

## 5. Đã làm gì

### 5.1 File × thay đổi

| File | Loại | Thay đổi |
|---|---|---|
| `web/backend/_v10984_ghep_lane_official.py` | **mới** | Chấm 5 cách ghép; bảng `ghep_nt_official_daily` (`output_eligible=0 diagnostic_only=1 owner_approved=0 shadow_only=1`); ngưỡng hành động hằng số; `compute_view()` cho API |
| `web/backend/_v10984_kiem.py` | **mới** | 14 phép kiểm máy, in `V10984_GHEP_SHADOW_OK` — dùng làm `chay_lenh` của `QD-024` |
| `web/backend/_v10984_evidence.py` | **mới** | Sinh JSON + 3 CSV bằng chứng |
| `web/backend/_v10984_deploy.py` | **mới** | Deploy khớp matcher hook, tự chặn khung giờ cấm |
| `web/backend/_v10984_verify.py` | **mới** | 11 nhóm nghiệm thu sau deploy trên VPS |
| `web/backend/main.py` | sửa | Thêm `GET /api/admin/ghep-nghiem-thu-official` (`require_admin` + `Cache-Control: no-store`) |
| `web/frontend/monitoring.html` | sửa | Thêm panel *GHÉP /nghiem-thu VỚI OFFICIAL (V10984)*; đăng ký trong `loadAllSections()` **và** `setInterval(60s)` |
| `web/_sync_live_forensic_inputs.py` | **sửa lỗi thật** | Đồng bộ đang TRƯỢT 100% vì băm tệp đang chạy rồi tải riêng (đua ghi). Nay đóng băng bản chụp trên máy chủ trước: `sqlite3 .backup` cho DB, `cp -p` cho jsonl |
| `web/backend/_v10982_kiem_lich9.py` | **sửa lỗi thật** | Phép `J8` chỉ soi `TREO_STATUSES` nên mục làm xong sớm bị báo MỒ CÔI — trái chú thích của chính nó. Nay chấp nhận `DONG_STATUSES` |
| `web/backend/_v10982_lich9.py` · `_v10981_trang_lich.py` | sửa | Thêm trường `xong_som` + mục §8.6 *"Đã LÀM XONG SỚM"* vào trang lịch do máy sinh |
| `docs/OWNER_DECISION_LEDGER.json` | sửa | Thêm **`QD-024`** — 5 mệnh đề máy kiểm được |
| `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` · `docs/FOLLOW_UP_TRACKER.md` | prepend | Ghép đầu bằng `_doc_prepend.prepend()` (+5.886 · +3.004 · +2.861 ký tự) |
| `docs/AUTOMATION_STATE.json` · `AUTOMATION_HISTORY.jsonl` | sửa | `governance_seq` → **393** |

**Backup:** `backups/v10984_pre/` (local, 7 file) · `/root/Lottery_AI_Test/backups/v10984_pre_20260804_215937` (VPS).

### 5.2 Deploy

Lúc **21:59:37 giờ VN** — **ngoài** khung cấm 05:00–06:30 và 15:30–18:15. Script tự kiểm giờ
trước khi động tay.

| | |
|---|---|
| Service | **`lottery`** (không phải `lottery-ai`) |
| **PID trước → sau** | **770947 → 801640** ✅ đã đổi thật |
| `py_compile` | COMPILE_OK (3 file) |
| Chạy thử trên VPS trước khi cắm cron | đạt — ghi 15 dòng |
| `systemctl is-active` | active |
| Journal sau restart | **0 Traceback · 0 ERROR** |

**Cron thêm 2 dòng**, cả hai chạy **sau cả ba mốc FINAL** (15:45 · 16:58 · 17:58) nên không chen
vào khung ra số:

```
0  19 * * *  _v10945_edge_gate.py            → FU-244, cổng lợi thế ghi hằng ngày
10 19 * * *  _v10984_ghep_lane_official.py   → FU-264, bảng đo bóng tự cập nhật
```

### 5.3 Hash 4 bảng khoá — trước/sau

| Bảng | Dòng | SHA256 (32 ký tự đầu) trước | sau | |
|---|---|---|---|---|
| `predictions` | 11.713 | `7b27df5056380737e6129c7cc0094c6b` | `7b27df5056380737e6129c7cc0094c6b` | ✅ |
| `final_bundles` | 474 | `a8f4570db97f09dcdebad48ca62ea38e` | `a8f4570db97f09dcdebad48ca62ea38e` | ✅ |
| `lottery_results` | 15.213 | `92ccf706553921288f2105f96e2a399b` | `92ccf706553921288f2105f96e2a399b` | ✅ |
| `model_daily_eval` | 11.577 | `c559a75ad34b78ed89ed7d265dca3e13` | `c559a75ad34b78ed89ed7d265dca3e13` | ✅ |

**Giống hệt cả 4.** Chi tiết: `artifacts/v10984_deploy.json`.

### 5.4 Trả lời yêu cầu (C) — cái gì kéo lên sớm được

**Đã kéo lên và làm xong trong phiên này:**

| Mã | Hạn đã xếp | Xong | Việc | Bao lâu | Rủi ro | Đo bằng gì |
|---|---|---|---|---|---|---|
| `FU-244` · `KS0807` | 07/08 | **04/08** | Cắm cron 19:00 cho cổng lợi thế | ~5 phút | **thấp** — chỉ đọc bảng official, ghi bảng shadow riêng, chạy sau mốc FINAL | `crontab -l \| grep -c '_v10945_edge_gate'` = **1** (trước = 0) · `edge_gate_daily` có **3 dòng 2026-08-04** (trước: 3 dòng, đều 01/08) |
| *(mới, không có mã cũ)* | — | **04/08** | Bảng đo bóng ghép lane — chính là yêu cầu (B) | ~40 phút | **thấp** — bảng chẩn đoán, không module official nào đọc | `_v10984_kiem.py` **14/14** · bảng 15 dòng, 4 cờ đúng |
| *(sửa lỗi)* | — | **04/08** | `_sync_live_forensic_inputs.py` đang trượt 100% | ~10 phút | **thấp** — công cụ đọc, không chạm runtime | chạy exit 0, manifest mới sinh |

**Bắt buộc chờ — `QD-014` cấm đích danh, không né được:**

| Mã | Việc | Vì sao phải chờ | Kết luận sớm nhất |
|---|---|---|---|
| `FU-192` · `XH0809` | Promote `glm-5.1` / `gpt-oss-120b` | Đổi roster 15 model official | 09/08 (owner quyết trước 07/08) |
| `FU-193` · `XH0807` | Sàn chất lượng combo-super | Đổi bộ lọc combo-super | **16/08** |
| `FU-216` · `XH0809-1` | Shadow MT bạch thủ = random-forest | Ăn vào nhánh ML đường dự đoán | **15/08** |
| `FU-217` · `SC0809` | Sửa key `lstm_probability` | Đổi cách cộng phiếu → đổi số công bố | **16/08** |
| `FU-231` · `HT0810-1` | Shadow bỏ ép RULES-FIRST | `QD-016` ghi rõ "sau 08/08" | **23/08** |
| `FU-226` · `HT0810-2` | A/B hai prompt cùng model | `QD-017` ghi rõ "sau 08/08" | **23/08** |
| `FU-215` · `DB0808` | Chốt mở hay gia hạn đóng băng | Chính là cái đóng băng | 08/08 (owner quyết) |

**Nói thẳng:** lịch cuốn chiếu đã được giãn **ba lần trong chính ngày 04/08** (V10981 lúc 10:29,
V10982 lúc 11:0x, V10982b lúc 12:4x) và §3 của `docs/LICH_CUON_CHIEU_DEN_10082026.md` **đã kéo
sẵn 5 mục** lên trước 08/08. Phần còn lại không phải là chậm trễ hành chính — nó là **cửa sổ đo
7–14 ngày mà chính owner đã ký** trong `QD-015` → `QD-018`. Rút ngắn cửa sổ đo là quay lại đúng
cái bẫy đã làm rữa sáu lần.

---

## 6. Cổng kiểm

| Cổng | Kiểm gì | Kết quả |
|---|---|---|
| `_v10984_kiem.py` (local) | 14 phép: 4 cờ chẩn đoán · ngưỡng không bị nới · API `require_admin` + `no-store` · panel đăng ký `setInterval` · 15 model official | ✅ **14/14 — `V10984_GHEP_SHADOW_OK`** |
| `_v10984_kiem.py` (**trên VPS**) | như trên, chạy trên chính máy chạy thật | ✅ **14/14** |
| `_v10920_decision_ledger.py` | 26 quyết định, `QD-024` mới | ✅ **0 TRÔI** · `QD-024` khớp **5/5** · `QD-014` khớp **7/7** |
| `_v10981_kiem_lich.py` | nhóm 14 mục, 8 phép | ✅ **8/8 — `LICH_CUON_CHIEU_DAT`** |
| `_v10982_kiem_lich9.py` | nhóm 9 mục, 8 phép | ✅ **8/8 — `GIAN_9_MUC_DAT`** · mồ côi toàn sổ **19 → 18** |
| Hash 4 bảng khoá | trước/sau deploy | ✅ **giống hệt cả 4** |
| Smoke endpoint | `/api/health` · 2 endpoint admin | ✅ `health=200` · `ghep_admin=401` · `edge_admin=401` |
| PID | trước/sau restart | ✅ **770947 → 801640** |
| Journal | Traceback/ERROR sau restart | ✅ **0 / 0** · service active |
| `/du-doan` official | roster + model_count hôm nay | ✅ `OUTPUT_ELIGIBLE_MODELS` = **15** · MN=15 MT=13 MB=14 (không đổi) |
| Bảng đo bóng trên VPS | 4 cờ trên **mọi** dòng | ✅ `15 \| Σoutput_eligible=0 \| Σdiagnostic=15 \| Σapproved=0 \| Σshadow=15` |
| Panel | khối + 3 chỗ đăng ký + trong `setInterval(60s)` | ✅ `sectionGhepNghiemThu`=1 · `loadGhepNghiemThu()`=3 · trong khối 60s=1 |
| Cách chấm trúng/trượt | tự tính lại từ `prizes_json` so `bach_thu_status` | ✅ **khớp 3/3 ô** hôm nay |
| `_v10921_report_gate.py V10984` | báo cáo đủ 9 phần, đã commit + push | xem §9 |

---

## 7. Vướng vấp

### 7.1 Đồng bộ dữ liệu sống TRƯỢT 100% — và đó là lỗi thật của công cụ

Quy tắc bắt buộc chạy `web/_sync_live_forensic_inputs.py` trước mọi việc accuracy. Nó **trượt cả
hai lần** với `Hash mismatch`, và hash khác nhau giữa hai lần chạy (`8f1328e5…` rồi `4f204e41…`).

**Nguyên nhân:** script `sha256sum` tệp DB đang chạy ở một thời điểm, rồi `sftp.get` cùng tệp đó
ở thời điểm khác. Production ghi vào giữa hai lần → không bao giờ khớp. Với DB sống thì phép
kiểm toàn vẹn đó **không thể đúng** — nó là tung đồng xu.

**Đã sửa:** đóng băng bản chụp trên máy chủ trước (`sqlite3 .backup` cho DB — nhất quán theo
giao dịch; `cp -p` cho jsonl), rồi mới băm và tải bản đã đóng băng.

**Hậu quả nếu bỏ qua:** mọi phiên accuracy/forensic sau này đều không chạy được bước tiền đề
bắt buộc, buộc agent phải **đi vòng** quy tắc toàn vẹn dữ liệu sống — hoặc tệ hơn, dùng bản
local cũ mà tưởng là bản mới.

### 7.2 Cổng lịch `J8` báo TRƯỢT khi làm xong việc sớm — lỗi do chính agent phát hiện khi tự làm hỏng

Sau khi ghi `FU-244` là xong, `_v10920_decision_ledger.py` báo **`QD-022` TRÔI 1/9** với
`J8: MỒ CÔI trong nhóm: ['FU-244=?']`.

Hai lỗi ghép lại:

1. **Lỗi của agent:** khối `FU-244` đầu tiên viết dạng gạch đầu dòng, **không có trường
   `status`** → bộ đọc trả `?`. Đã viết lại đúng khuôn bảng `| **status** | CLOSED_PASS |`.
2. **Lỗi của cổng:** `J8` chỉ soi `TREO_STATUSES`, nên **bất kỳ** mục nào làm xong sớm với nhãn
   đóng hợp lệ (`CLOSED_PASS`) đều bị báo MỒ CÔI. Trái với **chú thích của chính nó** ngay bên
   trên (*"Nhãn ngoài TREO_STATUSES và ngoài DONG_STATUSES"*) và trái định nghĩa gốc trong
   `trang_thai_mo_coi()` (loại cả nhãn treo **lẫn** nhãn đóng).

**Đã sửa** `J8` dùng `TREO_STATUSES | DONG_STATUSES`. **Không phải nới cổng** — chỉ chặn nhãn
không thuộc bộ nào, đúng ý định đã viết. Sau sửa: 8/8, mồ côi toàn sổ **giảm** 19 → 18.

**Hậu quả nếu bỏ qua:** cổng sẽ **phạt việc hoàn thành sớm** — đúng thứ owner vừa yêu cầu. Mọi
mục trong hai nhóm 14 + 9 làm xong trước hạn đều làm cổng trượt, và cách "chữa" dễ nhất là để
mục treo vô thời hạn cho cổng xanh. Đó là cổng dạy agent làm sai.

### 7.3 Suýt tuyên bố `FU-244` xong trước khi thật sự xong

Khối governance viết `FU-244` "ĐẠT" **trước khi** deploy chạy, tức cron chưa cắm và
`edge_gate_daily` chưa có dòng mới. Đúng nghĩa "hứa lảo". Đã đảo lại thứ tự: deploy → chạy cổng
lợi thế trên VPS → **rồi mới** ghi ĐẠT kèm số đo thật.

**Hậu quả nếu bỏ qua:** sổ theo dõi ghi xong trong khi thực tế chưa xong — loại sai nguy hiểm
nhất vì nó làm mất niềm tin vào toàn bộ sổ.

### 7.4 Ba lỗi nhỏ tự gây, đã sửa trong phiên

| Lỗi | Hậu quả nếu bỏ qua |
|---|---|
| Nhồi lồng dấu nháy trong f-string (`f"{t['x']}"` trong f-string) — chỉ chạy được từ Python 3.12 | Module chết trên VPS nếu venv là 3.11 |
| Thêm `dt.date` vào dữ liệu lịch → `_v10981_trang_lich.py` chết `TypeError: Object of type date is not JSON serializable` khi xuất JSON. **Trang MD đã ghi xong nhưng JSON thì không** — dạng hỏng nửa vời | Trang lịch và bản JSON máy đọc lệch nhau âm thầm |
| Gõ sai tên trường khi sửa (`vi_saoO_khong_som`) | May là StrReplace báo không tìm thấy; nếu gõ vào file thì phép `J7` mất một mục mà không ai biết |

### 7.5 Giới hạn phải nói rõ, không được che

- **Cỡ mẫu 15 ô / 35 lượt đặt.** Mọi kết luận ở §3.4–3.5 là **hướng**, không phải bằng chứng
  thống kê. Một ô đổi chiều là bảng đổi mặt.
- **Cần ~536 ngày nữa** mới đủ mẫu phát hiện chênh 3pp ở trục theo đài (α=5%, power=80%,
  p=17,37%, ~2,3 đài/ô). Mốc 60 ô (~21/08) chỉ đủ loại những cách ghép **tệ rõ ràng**, chưa đủ
  chứng minh cách nào tốt.
- **Lane `/nghiem-thu` còn mất ngày:** MB chỉ có 4/6 ngày (thiếu 30/07 và 03/08). Mỗi ngày mất
  là mẫu chậm thêm. `FU-252` đang theo dõi riêng việc này.
- **Header `Cache-Control: no-store` chỉ xuất hiện trên phản hồi 200 đã đăng nhập**, không có
  trên phản hồi 401 — giống hệt endpoint `edge-gate` có sẵn. Không phải lỗi, nhưng nói rõ để
  lần sau không ai tưởng cổng hỏng.
- **Mặt bằng "đánh bừa" 17,37% ở §3.5 là số gộp** ba miền trên 15 ô đó (MB có mặt bằng cao hơn
  MN/MT). So sánh **giữa các cách ghép** vẫn công bằng vì cùng bộ ô, nhưng đừng đem con số
  17,37% đó so với 16,5%/23,8% của từng miền.

---

## 8. Gỡ về

```bash
# 1. Xoá bảng đo bóng (không module official nào đọc nó)
sqlite3 /root/Lottery_AI_Test/data/lottery_ai.db "DROP TABLE IF EXISTS ghep_nt_official_daily;"

# 2. Gỡ 2 dòng cron
crontab -l | grep -v -E '_v10945_edge_gate|_v10984_ghep_lane_official' | crontab -

# 3. Khôi phục API + panel trên VPS (bản trước deploy)
cd /root/Lottery_AI_Test/backups/v10984_pre_20260804_215937
cp -p main.py monitoring.html /root/Lottery_AI_Test/web/backend/  # monitoring.html -> web/frontend/
systemctl restart lottery && systemctl show -p MainPID --value lottery

# 4. Khôi phục local
#    backups/v10984_pre/ có: main.py · monitoring.html · CHANGELOG.md ·
#    CURRENT_TRUTH_SSOT.md · FOLLOW_UP_TRACKER.md · OWNER_DECISION_LEDGER.json ·
#    _sync_live_forensic_inputs.py

# 5. Huỷ quyết định: đổi QD-024 trang_thai -> SUPERSEDED trong
#    docs/OWNER_DECISION_LEDGER.json rồi:
python web/backend/_v10920_decision_ledger.py
```

**Mất bao lâu:** ~5 phút. **Trạng thái sau khi gỡ:** đúng như trước 21:37 hôm nay. Đường ra số
công bố **không bị ảnh hưởng ở bất kỳ bước nào** — phiên này chưa từng chạm `/du-doan`, writer
`final_bundles`, hay bộ chọn model production, nên gỡ về không cần chạm runtime dự đoán.

---

## 9. Theo dõi tiếp

### `FU-264` · `DO0811` · Đo bóng ghép `/nghiem-thu` × official · hạn **11/08**

| Mốc | Ngưỡng **bằng số** | Hiện tại |
|---|---|---|
| **11/08** (quy trình) | Bảng có dòng của **≥7 ngày liên tiếp** 04→10/08 **và** `_v10984_kiem.py` còn **14/14** | 6 ngày (30/07→04/08) · 14/14 |
| **~21/08** (đủ mẫu tối thiểu) | ≥ **60** ô đo tiến **và** ≥ **150** lượt đặt theo đài | **15** ô · **35** lượt |
| **Được đề xuất vào official khi** | hơn đường official ≥ **3pp** **và** hơn bừa ≥ **3pp** **và** z ≥ **2** | tốt nhất −5,71pp · z 0,47 |

**Ai quyết:** ngưỡng do agent đặt trong phiên này, **không nới** ngưỡng `QD-013` của owner.
Việc đưa bất kỳ cách ghép nào vào official vẫn cần owner chốt, và chỉ sau khi đủ 4 điều kiện.

**Hạn rà soát `QD-024`: 11/08/2026.**

### Mục liên quan đang treo

| Mã | Nhãn | Hạn | Vì sao dính tới phiên này |
|---|---|---|---|
| `FU-252` · `KS0810-5` | Canh lane Nghiệm Thu ra số đủ 3 miền | 10/08 | Lane mất ngày là mẫu của `FU-264` chậm thêm. MB đang 4/6 ngày |
| `FU-215` · `DB0808` | Chốt mở hay gia hạn đóng băng `QD-014` | 08/08 | Mọi việc làm đổi chất lượng dự đoán đứng sau câu trả lời này |
| `FU-192` · `XH0809` | Promote `glm-5.1` / `gpt-oss-120b` | 09/08 | **Owner cần quyết trước 07/08.** 110 ngày / 3.778 lượt / 0 promote |
| `FU-244` · `KS0807` | Cổng lợi thế ghi hằng ngày | 07/08 | ✅ **ĐÓNG — xong sớm 04/08** trong phiên này |

### Ba mục đến hạn hôm nay 04/08 (nêu theo quy tắc đầu phiên)

`FU-187` · `KS0804-1` Nghiệm thu hook tra cứu đầu phiên · `FU-191` · `XH0804` Khoá luật cắt
model an toàn combo-super · `FU-212` · `DO0804` MT tín hiệu rơi ở gộp phiếu. Phiên này **chưa
xử** ba mục đó vì owner yêu cầu việc khác — nói rõ để không trôi mất.
