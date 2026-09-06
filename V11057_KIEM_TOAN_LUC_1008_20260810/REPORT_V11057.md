# REPORT V11057 — KIỂM TOÀN LỰC DỰ ĐOÁN NGÀY 10/08/2026 + ĐỀ XUẤT NÂNG CHẤT LƯỢNG

**Ngày:** 2026-08-10 tối · **Mã đọc:** `KS1008` · **Phương pháp:** 12 tác nhân (6 kiểm + 6 phản biện đối kháng), 1,56 triệu token, 485 lượt gọi công cụ
**Production KHÔNG đổi** — không deploy, không restart, `QD-041` nguyên vẹn · PID `1286954` · health 200

---

## 1. Tóm tắt

**Vận hành ngày 10/08: SẠCH.** Ba miền chốt đúng hạn, 26 phép tự kiểm chạy 18:05, ba cron tối chạy đúng phút, journal **0 traceback / 0 ERROR / 0 CRITICAL**, 4 bảng khoá nguyên vẹn (đã tính lại **81/81 dòng** `model_daily_eval`, lệch 0).

**Kết quả: 1/3 bạch thủ** — MN `75` TRÚNG · MT `28` trượt · MB `74` trượt.

**Nhưng con số quan trọng nhất không phải của hôm nay.** Đo trên **164 ngày / 492 miền-ngày** với nền đúng:

> Bạch thủ công bố **34,3%** · nền ngẫu nhiên đúng **34,0%** ⇒ **lợi thế +0,34pp · CI95 [−3,8 … +4,5]**

Toàn bộ dây chuyền — 27 model, prompt 4 tầng, bộ luật, chấm điểm có trọng số — **không tách được khỏi phép bốc ngẫu nhiên một số**. Và CI đủ hẹp để **loại trừ mọi lợi thế trên +4,5pp**.

**NĂM lần agent tự bắt mình sắp kết luận sai** (mục 7) — trong đó **một lỗi nằm trong báo cáo V11055 đã push sáng nay**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Hôm nay anh bận quá chưa xử lý gì thêm nha em, Giờ em tiến hành kiểm tra toàn lực dự đoán ngày hôm nay, sau đó tổng hợp lại đầy đủ chi tiết nhất đề xuất hướng xử lý an toàn nâng cao cải thiện dự đoán, push lên githubs nha em»* — 10/08

---

## 3. Đào bới / phát hiện

### 3.1 · Vận hành — tất cả cổng ĐẠT

| mốc §55 | hạn | chốt thật | còn lại |
|---|---|---|---|
| MN | 15:45 | **05:24:35** | 620 phút |
| MT | 16:58 | **16:47:06** | **10,9 phút** ← mỏng nhất |
| MB | 17:58 | **17:34:29** | 23,5 phút |

- Bộ tự kiểm **18:05:02, đủ 26 phép**: 23 OK · 3 LỆCH. Nhưng **C18/C19 trỏ về MT ngày 04/08** (còn trong cửa sổ 7 ngày, tự rơi khỏi cửa sổ 12/08) — **không phải lỗi hôm nay**. Chỉ **C25** là của hôm nay và chỉ dính **3 cặp model SHADOW** (`gpt-5-mini/MB`, `gpt-5-mini/MT`, `grok-4.3/MN`), không dính đường official nào.
- Cổng hạn 18:02: **62 mục · trễ 0 · chưa có 1**. Mục thiếu là `MT choi_lock` — truy ra là **cố ý**: gate V10828 chặn số `01` vì 0 phiếu model canon ⇒ không khoá vốn. **Cơ chế đúng thiết kế, không phải cron hỏng.**
- Ba cron tối chạy đúng phút: **19:05:01** bầy đàn · **19:35:01** lane G2-MB (9 mục, `la_do_lui=0`) · **21:40:03** P4 (V11055, đủ 3 miền).
- Journal: 5.822 dòng, **0 `Traceback`**, **0 ` - ERROR - `**, **0 `CRITICAL`**. 31 dòng khớp `-i error` là **30 dòng `SCRAPE_FAIL`** (vòng thử lại khi **cào kết quả xổ**, đã thành công) + **1 dòng `errors=0` trong thông báo THÀNH CÔNG** — đúng bẫy RM-09.
- Restart: **`NRestarts=0`**, đúng 1 lần khởi động 10:22:41 theo kế hoạch, PID sống liên tục 11h37.

**Điểm cần theo dõi (phản biện bổ sung):** nhánh **SHADOW của MT trễ thật 57 giây** và `contract_status` ghi `SHADOW_INCOMPLETE_BY_DEADLINE`. Và `TOPK_STALE_POOL_HOLE` xuất hiện **20/21 miền-ngày** trong 7 ngày — không phải sự cố hôm nay mà là **trạng thái thường trực**.

### 3.2 · Khâu SINH — không tạo được lợi thế nào đo được

Độ phủ hôm nay (tự tính lại, khớp tuyệt đối, và đã đối chiếu **48/48 dòng** với cột `predictions.hit_count` của chính production, lệch 0):

| miền | pool hợp nhất | trúng | / tổng đuôi ra |
|---|---|---|---|
| MN | 17 số | 4 | 4/39 |
| MT | 18 số | 6 | 6/31 |
| MB | 14 số | 2 | 2/23 |

Trên **30 ngày** (n đủ theo RM-04): pool hợp nhất trúng **393** lần so với nền ngẫu nhiên **399,6** ⇒ **điểm ước lượng nằm gần như đúng trên nền**. Không một model nào trong 51 cặp model-miền vượt nền có ý nghĩa.

### 3.3 · Khâu CHỌN — chỉ MT là thất bại thật, MB thì KHÔNG

| miền | BT chọn | số trúng nằm hạng | luật «nhiều phiếu nhất» sẽ chọn |
|---|---|---|---|
| MN | 75 (#1) ✓ | #1 | 75 — **cùng kết quả** |
| **MT** | 28 (#1) ✗ | **19 ở #2** | **19 — sẽ TRÚNG** |
| MB | 74 (#1) ✗ | 78 ở #5 | **74 — cũng trượt** |

**MB KHÔNG phải lỗi khâu chọn:** 74 dẫn phiếu thật (5 thô / 4 sau cộng) so với 78 (4 thô / 3). Luật nhiều-phiếu-nhất **cũng chọn 74**.

**Cơ chế thật của MT — và nó không phải «trọng số lật ngược 6 phiếu bằng 3 phiếu»:**

Ba cổng lọc chạy **TRƯỚC** khi chấm điểm đã gỡ đúng ba model bỏ phiếu `19`:

| model bị gỡ | lý do |
|---|---|
| `combo-no-token` | `output_eligible=False` |
| `meta-learning` | `max_voters_cap` — `MT_top13_only_V10752_weakest_dropped` |
| `smart-ensemble` | `max_voters_cap` — cùng cổng |

Thế 6–3 thành **hoà 3–3**, rồi trọng số mới bẻ về `28`.

### 3.4 · Một học thuyết của owner đang bị chính hệ bỏ qua

MT hôm nay, hệ **tự ghi cảnh báo này rồi vẫn công bố**:

```
main_number_anti_trap = {"tail":"28", "level":"FULL_SPENT", "hit_in_regions":["MN"]}
main_number_anti_trap_warning = "bundle bach_thu 28 was already emitted in ALL prior
                                 same-day regions (MN) — owner anti-trap owner-doctrine flag"
```

Đây là **§60 «bỏ nửa chừng»**: học thuyết được **dạy trong prompt** (`gpt_analyzer.py:755` — *«Main pick KHÔNG được là tail ở FULL_SPENT trừ khi có override_reason rõ + confidence bị giảm 1 bậc»*) nhưng **bộ ráp bundle chỉ tính cờ SAU khi đã chọn xong** (`main.py:10205`) rồi ghi cảnh báo — **không có nhánh nào đổi số**.

Thành tích của cờ, **phân tầng theo miền** (gộp thô là bẫy Simpson vì nền lệch 12,7% vs 38,4%):

| miền | FULL_SPENT | FRESH | chênh |
|---|---|---|---|
| MB | **0/12 = 0,0%** | 7/55 = 12,7% | **−12,7pp** |
| MT | 10/39 = 25,6% | 28/73 = 38,4% | **−12,7pp** |
| **gộp MH** | | | **−12,7pp · CI95 [−26,2 … +0,7] · z=−1,02** |

**51 lần** cờ bật và bị bỏ qua. Hai miền nền khác hẳn nhau cho chênh **giống hệt đến một chữ số thập phân**.

**Nhưng phải nói nốt vế kia:** phản thực thay số chỉ được **12/47 vs 9/47 = +6,4pp**, McNemar **z=+0,49**. Lý do: số thay thế nằm tận hạng **#2,4** — mất lợi thế xếp hạng. **Biết một số kém KHÔNG đồng nghĩa có số tốt hơn để thay.**

### 3.5 · Bầy đàn AI — CÓ THẬT và CÓ Ý NGHĨA THỐNG KÊ

Đo bằng **tỉ lệ đồng thuận từng cặp** (thước không phụ thuộc cỡ mẫu), 90 lượt miền-ngày:

| cụm | đồng thuận cặp |
|---|---|
| **AI** | **0,2929** |
| ML | 0,1519 |
| chênh | **+0,1411 · z = +3,10** |

**Đây là kết quả duy nhất trong cả phiên vượt ngưỡng z ≥ 1,96.**

Nhưng **bầy đàn CHƯA chứng minh được gây thiệt hại**: tỉ lệ trúng hai cụm gần như bằng nhau (AI 33,27% vs ML 32,22%, chênh cặp −0,66pp, z=−0,10), **cả hai đều nằm đúng trên nền**.

*(Phản biện chỉ ra kho **đã có sẵn** bảng `convergence_cluster_pattern_daily` — 1.067 dòng, có cột `herd_voter_count`/`ai_voters`/`ml_voters`. **Không cần dựng bảng mới.**)*

### 3.6 · Luật đang tác động — con số công bố là TRẦN, không phải thực tế

`MINED_RULES_MODE='soft'` · `APPLY_TO='all'` — local và VPS **giống hệt** (md5 `main.py` `059edb84…` khớp hai đầu), và **RUNTIME_PROVEN** qua journal: `[RULE_ENGINE_V2] MB_T2 @ 2026-08-10 [soft]`.

**Nhưng câu «đang cộng +0,15 cho mọi luồng» (CHANGELOG.md:222) là TRẦN.** Hôm nay là **T2**, và **không luật `READY_STRONG` nào active cho T2** (cả 8 luật rơi vào T3/T4/T5/T7/CN). Boost thật đo được:

| miền | boost thật hôm nay |
|---|---|
| MN | `86 +0,0242` |
| MB | `86 +0,1000` · `68 +0,0226` · `74 +0,01` |
| **MT** | **đúng bằng 0** (cả 5 luật MT-T2 đều `COMBO_ONLY`, không phải khoá trong `BOOST_TABLE`) |

*(Phản biện chưa loại trừ được nhánh **CHỐT GẤP** dùng bảng riêng `soft: 0.40` tại `combo_super.py:1901` — cần đo tiếp.)*

### 3.7 · THƯỚC ĐO CHÍNH — và nó trả lời thẳng câu «làm sao nâng chất lượng»

Nền đúng cho một số bất kỳ ngày đó = `(số đuôi ra ngày đó)/100` (RM-18).

**VIF: phản biện sửa phương pháp của agent.** `VIF=2,92` đo ở V11030 là cho **thước khác** (16 model cùng đoán một ngày). VIF thực nghiệm cho thước bạch thủ, cụm = ngày, 164 ngày:

```
phương sai nếu độc lập 106,36  ·  phương sai quan sát 94,60  ⇒  VIF = 0,889
```

Nên dùng **VIF = 1** (bảo thủ vừa đủ). Kết quả trên **toàn bộ 164 ngày / 492 miền-ngày**:

| | |
|---|---|
| bạch thủ công bố | **169/492 = 34,3%** |
| nền ngẫu nhiên đúng | **34,0%** |
| **lợi thế** | **+0,34pp** |
| **CI95** | **[−3,8 … +4,5]pp** |

**Đọc đúng:** hệ **không tệ hơn** ngẫu nhiên (con số −2,2pp mà agent tính ở cửa sổ 120 ngày là **window-shopping**, dấu đổi theo cửa sổ). Hệ **không tách được khỏi** ngẫu nhiên, và CI đủ hẹp để **loại trừ mọi lợi thế trên +4,5pp**.

**Số cần biết để lập kế hoạch:**

| muốn chứng minh lợi thế | cần |
|---|---|
| +10pp | **29 ngày** (0,9 tháng) |
| +8pp | **45 ngày** (1,5 tháng) |
| **+5pp** | **115 ngày (3,8 tháng)** |
| +3pp | 319 ngày (10,5 tháng) |

*(Các con số này đã tính bằng **VIF đúng của thước này = 1,0** — chặn dưới của VIF thực nghiệm
0,889. Bản nháp đầu dùng nhầm `VIF=2,92` của thước khác và ra 11 tháng cho +5pp, tức **nặng hơn
3 lần thực tế**. Đây là lần thứ năm agent tự bắt mình trong phiên — xem 7.5.)*

**Và một điều phải nói rõ:** bốn cửa sổ gần nhất đều **âm** (30d −4,06 · 60d −4,56 · 90d −4,25 ·
120d −2,23) trong khi cửa sổ đầy đủ 163 ngày là **+0,34**. Không cửa sổ nào đạt `|z|≥1,96`, nên
**không được kết luận «đang xuống»** — nhưng hình dạng đó nhất quán với việc **giai đoạn đầu tốt
hơn giai đoạn gần đây**, và đó là thứ đáng theo dõi chứ không đáng công bố.

> **Đây là lời giải VẬT LÝ cho sáu lần «hứa rồi rữa»** (V10655→V10672→V10677→V10753→V10789→V10790): các phép đo đó **chưa bao giờ đủ sức mạnh** để thấy thứ chúng đi tìm. **Không phải ý tưởng sai — THIẾT KẾ ĐO sai.**

---

## 4. Hướng xử lý và vì sao chọn — ĐỀ XUẤT AN TOÀN

Nguyên tắc chi phối mọi đề xuất dưới đây: **không đề xuất nào đụng prompt / đường chọn số / roster trước 21/08** (`QD-041`), và **không đề xuất nào được duyệt bằng backtest**.

### 4.1 · LÀM NGAY — an toàn tuyệt đối, 0 đồng, không đụng production

| # | việc | vì sao | đo bằng gì |
|---|---|---|---|
| **A1** | **Sửa nhãn tầng trong V11055** — `_apply_hot_cold_post_filter` tác động ở tầng **output từng model**, KHÔNG phải tầng ráp bundle | báo cáo đã push sáng nay gọi **sai tầng** (mục 7.1) | grep 4 điểm gọi → đều trong `run_combo_super()` / `_make_prediction()` |
| **A2** | **Ghi VIF đúng theo từng thước** vào sổ RM-18 | `VIF=2,92` đang bị dùng như hằng số toàn cục; thực nghiệm cho bạch thủ là **0,889** | script đo VIF thực nghiệm, commit kèm |
| **A3** | **Ghi con số n-cần vào mọi phép đo đang treo** | FU-284 · DEHERD_V1 · P4 đều chưa khai «bao lâu mới đủ» | bảng ở mục 3.7 |

### 4.2 · CHỈ ĐO SHADOW — dựng phép đo tiến, KHÔNG bật gì

| # | việc | ngưỡng **đăng ký trước** | bao lâu thấy |
|---|---|---|---|
| **B1** | **Đo tiến luật tôn trọng anti-trap**: khi BT là `FULL_SPENT`, ghi song song số thay thế cao nhất không-spent | McNemar `\|z\| ≥ 1,96` gộp MT+MB | ~13 cặp lệch/47 ngày ⇒ cần **~200 cặp** |
| **B2** | **Đo tiến P4 gan hội tụ** (đã dựng V11055, hôm nay ghi ngày đầu) | McNemar `\|z\| ≥ 1,96` gộp 3 miền | đang tích luỹ |
| **B3** | **Dùng bảng bầy đàn CÓ SẴN** `convergence_cluster_pattern_daily` thay vì dựng mới | — | bảng đã có 1.067 dòng |
| **B4** | **Đo `MINED_RULES` nhánh CHỐT GẤP** (`soft: 0.40`) — chưa loại trừ được | boost thật vs 0 | 30 ngày |

**Vì sao tất cả đều là đo, không phải bật:** vì mục 3.7 nói rõ — **muốn thấy +5pp phải chạy 3,8 tháng**. Bật một thứ rồi «thấy tốt sau 2 tuần» là **đúng cái đã rữa sáu lần**.

### 4.3 · PLAN 21/08 — chờ owner ký, đã có `FU-395`

| # | việc | trạng thái |
|---|---|---|
| **C1** | Nối anti-trap vào bộ ráp bundle (hiện chỉ tính rồi ghi cảnh báo) | chạm đường chọn số ⇒ **PLAN** |
| **C2** | Rà `max_voters_cap` V10752 — bật bằng backtest +9,3pp, đo tiến 47 ngày **không thấy** | chạm đường chọn số ⇒ **PLAN** |
| **C3** | Ghi điểm chọn combo-super (C1 của V11056) | chạm module sinh số ⇒ **PLAN** |
| **C4** | Chữ ký owner cho `SP-4.3`/`SP-4.4` + gỡ khoá lạc hậu `SP-4.1`/`SP-4.0` trong mã sống | **PLAN** |

### 4.4 · Điều em phải nói thẳng về «nâng cao chất lượng dự đoán»

Với lợi thế đo được là **+0,34pp ± 4,2pp** trên 164 ngày, thứ **KHÔNG** nên làm là thêm model, thêm luật, thêm tầng prompt — vì:

1. **Không đo được.** Mọi thay đổi dưới +4,5pp nằm trong nhiễu; thêm thứ mới chỉ tạo thêm chỗ để tin nhầm.
2. **Đã thử rồi.** 27 model, prompt 4 tầng, 105 luật khai mỏ, cross-region, gan/hot/cold — tổng lợi thế vẫn là 0.

Thứ **NÊN** làm, theo thứ tự:

1. **Sửa thiết kế đo trước, không sửa hệ.** Mọi phép đo mới phải **gộp 3 miền**, khai **n-cần** ngay từ đầu, và **đăng ký ngưỡng trước**. Không đủ n thì ghi *«chưa được phép kết luận»*, không ghi *«có vẻ tốt»*.
2. **Ưu tiên thứ có CƠ CHẾ rõ, không phải thứ có SỐ ĐẸP.** Anti-trap có cơ chế (số đã ra ở miền trước) và cho chênh **giống hệt −12,7pp ở hai miền nền khác nhau** — đó là dấu hiệu cơ chế thật, đáng đo tiến. Ngược lại, mọi «luật» khai mỏ đều **0/105 qua cổng**.
3. **Cắt bớt thứ không có căn cứ** — nhưng **chỉ sau 21/08 và chỉ khi đo tiến xác nhận**.

⚠️ [ĐÍNH CHÍNH · ĐÃ RÚT LẠI RL-002: vế «0/105 qua cổng» ở mục 2 trên là SAI — thực tế 8/105 luật
đạt `READY_STRONG` (đúng số cũng đã có ngay ở dòng 126 phía trên: "cả 8 luật rơi vào
T3/T4/T5/T7/CN"). Câu đúng phải là «0/105 kiểm NGOÀI MẪU» — hai mệnh đề khác nhau. Xem
docs/SO_RUT_LAI.json, bản rút V11073_DINH_CHINH_0_TREN_105_20260815.]

---

## 5. Đã làm gì

| # | việc | bằng chứng |
|---|---|---|
| 1 | Đồng bộ dữ liệu tươi từ production 21:52 | `artifacts/live_sync/20260810_215244/manifest.json` |
| 2 | 12 tác nhân kiểm + phản biện đối kháng 6 mặt | 1,56 triệu token · 485 lượt gọi công cụ |
| 3 | Đo lại độc lập: xếp hạng số trúng · anti-trap · V10752 · bầy đàn · thước đo chính | các script trong mục 6 |
| 4 | Bốn lần tự chặn kết luận sai | mục 7 |

**KHÔNG đụng production:** không deploy · không restart · không sửa prompt/đường chọn số/roster · 4 bảng khoá nguyên.

---

## 6. Cổng kiểm — xác minh

| cổng | kết quả |
|---|---|
| RM-01 tuổi dữ liệu | manifest 21:52, tuổi **0,0 giờ** ⇒ ĐẠT |
| RM-10 đối chiếu hàm thật | `database.get_all_tails` — lệch 0 trên mọi phép |
| `model_daily_eval` tính lại | **81/81 dòng**, lệch 0 ở `bt_hit`, `hit_count`, `hit_numbers`, `status` |
| 4 bảng khoá | `predictions` 81 dòng = 81 cặp phân biệt · `final_bundles` 3 · `lottery_results` 6 đài |
| `_v10900_consistency_guard` 18:05 | 26 phép · 23 OK · 3 LỆCH (2 là dữ liệu 04/08 cũ) |
| `_v11055_canh_chan_cheo_lane.py` | **0 dòng · 0 chặn nhầm** — 11,8 giờ vào cửa sổ 24h |
| `_v11044_cong_so_hieu.py` | V11057 · FU-396 · QD-057 là số trống |

**Cảnh báo cho việc chốt FU-360 sáng mai:** **MN chạy 05:00–05:36, TRƯỚC lần restart 10:22:41**, nên hôm nay **chỉ MT/MB thực sự chạy dưới cổng chặn chéo lane**. Chưa phải `RUNTIME_PROVEN` đủ ba miền — phải ghi đúng tầng khi đóng (RM-12).

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **10/08 (tối)** | *«Hôm nay anh bận quá chưa xử lý gì thêm nha em, Giờ em tiến hành kiểm tra toàn lực dự đoán ngày hôm nay, sau đó tổng hợp lại đầy đủ chi tiết nhất đề xuất hướng xử lý an toàn nâng cao cải thiện dự đoán, push lên githubs nha em»* |
| **09/08** | *«gan chỉ là điểm hội tụ… đề xuất không có trong gan thì gan vô giá trị»* — nền của P4, hôm nay ghi ngày đo tiến đầu tiên |
| **doctrine cũ** | học thuyết **anti-trap** — mã gọi thẳng là *«owner anti-trap owner-doctrine flag»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| ba miền chốt đúng hạn, 26 phép chạy 18:05, journal 0 lỗi | `final_bundles.created_at` · `v10900_consistency_guard` 26 dòng `computed_at_vn=18:05:02` |
| anti-trap **chỉ tính SAU khi đã chọn**, ghi cảnh báo, **không đổi số** | `main.py:10205` `compute_prior_region_spend_for_tail(bach_thu, …)` — nhận `bach_thu` đã chốt làm tham số |
| `max_voters_cap` gỡ 2 model bỏ phiếu `19` ở MT | `main.py:9584-9615` · `model_exclusion_reasons` trong bundle MT |
| `_apply_hot_cold_post_filter` ở tầng **output từng model**, KHÔNG ở tầng ráp bundle | 4 điểm gọi đều trong `run_combo_super()` (`combo_super.py:2029`) và `_make_prediction()` (`main.py:7892/8099/8352`); bundle do `generate_final_bundle()` (`main.py:9405`) ráp |
| `MINED_RULES_MODE='soft'` **runtime-proven**, nhưng boost thật hôm nay **0,01–0,10**, MT **bằng 0** | journal `[RULE_ENGINE_V2] MB_T2 @ 2026-08-10 [soft]` · `BOOST_TABLE` không có khoá `COMBO_ONLY` |
| P4 shadow ghi ngày đo tiến đầu tiên: MT `28→97`, luật gan **TRÚNG** | `gan_hoi_tu_shadow_v11055` date=2026-08-10 |

### `DOC_SAID`

| tài liệu ghi gì | file:mục | lệch? |
|---|---|---|
| *«MINED_RULES đang cộng +0,15 cho mọi luồng»* | `CHANGELOG.md:222` | ✗ **là TRẦN** — thực tế hôm nay 0,01–0,10, MT bằng 0 |
| *«`_apply_hot_cold_post_filter` đang sống trên đường chọn số… dìm số gan cao ×0,3 trước khi vào top-10»* | `REPORT_V11055.md §3.4` (**agent viết sáng nay**) | ✗ **SAI TẦNG** — xem 7.1 |
| `RR §10B`: *«Main pick KHÔNG được là tail ở FULL_SPENT»* | `gpt_analyzer.py:755` | ✗ **prompt dạy, bộ ráp bundle không thi hành** |
| V10752: *«Backtest causal 75d: +9,3pp»* | `main.py:9585-9586` | ✗ **đo tiến 47 ngày không thấy** (DiD −4,1pp, z=−0,24) |
| `VIF = 2,92` | `CLAUDE.md §61 RM-18` | ✗ **đúng cho thước khác**; thước bạch thủ có VIF thực nghiệm **0,889** |

### Ba lớp lệch nhau ⇒ FINDING (đúng §62.2)

1. **`OWNER_SAID` ≠ `CODE_DID`** — học thuyết anti-trap được owner đặt ra, prompt dạy model tuân, nhưng **bộ ráp bundle công bố số vi phạm học thuyết 51 lần** và tự ghi cảnh báo mỗi lần.
2. **`DOC_SAID` ≠ `CODE_DID` (ba lần)** — «+0,15 cho mọi luồng» là trần; V10752 «+9,3pp» không thành hiện thực; `VIF=2,92` áp nhầm thước.
3. **`DOC_SAID` sai do chính agent viết sáng nay** — nhãn tầng của `_apply_hot_cold_post_filter` trong `REPORT_V11055`.

---

## 7. Vướng vấp — NĂM lần agent tự chặn kết luận sai

### 7.1 · Sai tầng trong báo cáo ĐÃ PUSH sáng nay

`REPORT_V11055 §3.4` viết `_apply_hot_cold_post_filter` *«đang sống trên đường chọn số»* và *«số gan cao bị dìm ×0,3 trước khi vào top-10»*.

**TRƯỚC:** hàm nằm trên đường ráp bundle, méo bảng xếp hạng top-10.
**SAU:** 4 điểm gọi đều trong `run_combo_super()` và `_make_prediction()` — tầng **output từng model**. Bundle do `generate_final_bundle()` (`main.py:9405`) ráp, **hàm khác**.
**Hệ quả:** kết luận P4 *«pool đã bị trừng phạt vì có gan»* vẫn còn hiệu lực **gián tiếp** (hàm định hình cái mà từng model xuất ra, rồi mới vào pool), nhưng **mô tả cơ chế đã sai tầng và phải sửa**.

### 7.2 · «Cap V10752 cắt 2 model bỏ phiếu số trúng» — 41% là BẪY

Đếm thô: **41%** số ngày MT có model bị cắt từng bỏ phiếu cho số trúng. Nghe rất nặng.

Nền đúng `1−(1−b)^k` với k≈3,2 số và b≈0,31: **71,0%**. Thực tế **57,6%** ⇒ **KÉM nền** (z=−0,99). **Nhóm bị cắt không hề giỏi hơn.** Ca MT hôm nay chỉ là **giai thoại một ngày**.

### 7.3 · «Pool chứa số trúng 97,8% ⇒ trần cải thiện khổng lồ» — cũng là BẪY

Bốc **ngẫu nhiên 10 số** cũng chứa số trúng **~97,6%**, vì mỗi ngày có ~31/100 đuôi ra. Đó là **số học**, không phải độ phủ tốt.

### 7.4 · Window-shopping và VIF sai thước

Cửa sổ 120 ngày cho lợi thế **−2,2pp** (nghe như hệ tệ hơn ngẫu nhiên). Cửa sổ 164 ngày cho **+0,34pp**. **Dấu đổi theo cửa sổ** ⇒ chọn cửa sổ xấu để kể chuyện là đúng thứ RM-18 cấm. Và `VIF=2,92` áp nhầm thước làm CI phồng lên vô cớ.

### 7.5 · n-cần tính nhầm gấp 3 lần — bắt được lúc chạy script kiểm chứng

Bản nháp báo cáo ghi *«muốn chứng minh +5pp phải chạy 11 tháng»*, tính bằng `VIF=2,92`. Nhưng
chính mục 3.7 vừa chứng minh `VIF` của thước này là **0,889**. Khi viết script tái lập
(`_v11057_do_thuoc_chinh.py`, RM-11) thì con số ra **115 ngày = 3,8 tháng** — **nhẹ hơn 3 lần**.

**Đây là lỗi đổi kết luận:** «11 tháng» đọc thành *vô vọng*, «3,8 tháng» đọc thành *làm được
trong quý này*. Nếu không viết script tái lập thì con số sai đã đi vào sổ.

**Năm lỗi trong một phiên — ba do phản biện đối kháng bắt, hai do agent tự bắt khi buộc mình
viết script tái lập.**

---

## 8. Gỡ về

Phiên này **không đụng production** ⇒ không có gì phải gỡ ở tầng runtime.

```bash
# gỡ toàn bộ V11057 (chỉ là báo cáo + script đo read-only)
git revert <sha V11057>
```

**Gỡ về đang chờ, không liên quan phiên này:** FU-360 nếu canh 24h phát hiện chặn nhầm —
`cp backups/database.py.pre_v11052 web/backend/database.py && systemctl restart lottery`.

---

## 9. Theo dõi tiếp

| mã | việc | ngưỡng hành động | mốc |
|---|---|---|---|
| **FU-360** · `CL1008` | chốt hay rollback | **bất kỳ** chặn NHẦM ⇒ rollback. **Ghi đúng tầng**: hôm nay chỉ MT/MB chạy dưới cổng | **sáng 11/08** |
| **FU-396** · `DO1108` | dựng đo tiến B1 (anti-trap) + B4 (CHỐT GẤP), dùng bảng có sẵn cho B3 | McNemar `\|z\|≥1,96` gộp miền | owner ký |
| **FU-395** · `HT2108` | gói 21/08 — bổ sung C1 (anti-trap vào bộ ráp) và C2 (rà V10752) | owner ký từng mục | **21/08** |
| **FU-394** · `GH1008` | P4 đo tiến — hôm nay ghi ngày đầu (MT `28→97` luật gan trúng) | McNemar gộp 3 miền | tích luỹ |
| **FU-265** · `DO1208` | sàn 5 lượt không áp ở nhánh combo-super | đã có sẵn | **12/08** |
| C18/C19 | tự rơi khỏi cửa sổ 7 ngày | **không tắt, không nới ngưỡng** | **12/08** |
| FU-284 | cửa sổ đang chạy | **9,53** điểm · z ≥ 1,96 · n ≥ 150 | **20/08** — cấm đọc sớm |
| DEHERD_V1 | mới 2/21 ngày | ≥21 ngày · dẫn official · không thua miền nào | **19/08** |

**Đã dùng 1 mã FU mới (`FU-396`).**

---

TanPhatAI cần làm: ① ghi `QD-057` (owner 10/08 tối — lệnh kiểm toàn lực + đề xuất an toàn) và `FU-396 · DO1108`; ② **đính chính `REPORT_V11055 §3.4`** — `_apply_hot_cold_post_filter` ở tầng **output từng model**, không phải tầng ráp bundle (đã ghi TRƯỚC/SAU ở mục 7.1); ③ ghi vào sổ RM-18 rằng **`VIF` phải đo theo TỪNG THƯỚC** — `2,92` đúng cho thước 16-model-một-ngày, thước bạch thủ có VIF thực nghiệm **0,889**; ④ ghi con số **n-cần** (3,8 tháng cho +5pp) vào FU-284 · DEHERD_V1 · FU-394 để không ai đọc sớm; ⑤ theo dõi **FU-360 sáng 11/08** và nhớ **chỉ MT/MB chạy dưới cổng hôm nay** — ghi đúng tầng khi đóng.
