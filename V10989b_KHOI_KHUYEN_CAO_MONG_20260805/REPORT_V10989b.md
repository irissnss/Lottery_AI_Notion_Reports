# BÁO CÁO V10989b — Khối khuyến cáo `/du-doan-test` còn hứa hẹn trên 2/8 lượt

**Ngày:** 05/08/2026 · **Giờ:** 11:4x–12:0x (giờ VN) · **Có deploy:** CÓ (ngoài khung cấm)
**Tiếp nối:** [V10989](../V10989_SUA_TRANG_DU_DOAN_TEST_20260805/REPORT_V10989.md) cùng ngày

---

## 1. Tóm tắt

Vòng V10989 sáng nay chữa bốn nhãn sai trên `/du-doan-test` nhưng **chỉ đụng nhánh "đang THEO
DÕI"**. Hậu kiểm ngay sau đó — làm đúng lệnh owner *"tự gọi API đọc nội dung THẬT cả 3 miền"* —
lòi ra **nhánh KHUYẾN CÁO CHÍNH còn nguyên bệnh**: MB đang bảo người đọc **chơi theo lane
`MB_FULL_POOL_D_W06_V1` trên đúng 2 lượt trúng / 8 lượt** (25% vs nền 11%, đuôi nhị thức
**p = 0,217** — không phân biệt được với may rủi), kèm chuỗi **ghi cứng** *"— vượt rõ + bền."*
in ra bất kể cỡ mẫu. Chân khối còn mô tả cổng **`n≥40`** trong khi cổng thật của đường đang đi
là **`REC_WD_MIN_N = 8`**.

Đã sửa ở tầng hiển thị: trang tự chấm đuôi nhị thức, `p > 0,10` thì hạ *"nên chơi LANE"* xuống
**"CHƯA đủ bằng chứng để khuyến cáo"**; thêm `method_last_run_date` để cảnh báo khi lane được
khuyến cáo không có số hôm nay; chân khối ghi đúng **hai** cổng. Số thô vẫn hiện đủ theo §54.
Deploy 11:49:37, **PID 839095 → 842736**, hash 4 bảng khoá **giữ nguyên**, bộ tự kiểm **22 phép**
với `C22` **OK**. Nghiệm thu bằng cách **bốc đúng hàm `renderPlayRecommendation` khỏi tệp đang
phục vụ** rồi đổ payload thật vào đọc chữ — **3/3 miền đạt**. Mở `FU-272` cho owner quyết việc
nâng sàn ở gốc.

---

## 2. Owner yêu cầu gì — nguyên văn

Owner **không nói thêm câu nào** ở vòng này. Đây là hệ quả trực tiếp của một câu owner đã ra
lệnh ở vòng đầu cùng ngày:

> *"Tự gọi API đọc nội dung THẬT cho cả 3 miền sau khi sửa, dán số vào báo cáo. Đừng kết luận
> 'đã đạt' chỉ vì file giống nhau hay header đúng — đó đúng là cái sai hôm qua."*

Và câu owner nói khi gửi ảnh chụp lúc ~10:07:

> *"em tự nhìn đi"*

Cùng nguyên tắc §54 owner đã ký:

> *"output thô phải luôn nhìn thấy được; cổng chỉ khoá tiền; không hứa hẹn con số chưa đủ cỡ
> mẫu — phải ghi rõ cỡ mẫu + z hoặc bỏ nhãn"*

---

## 3. Đào bới / phát hiện — đo bằng gì, số liệu thật, cỡ mẫu

**Cách đo:** ký một cookie phiên admin bằng chính `SESSION_SECRET` của app trên VPS, rồi `curl`
qua HTTP thật vào `/api/du-doan-test/{MN,MT,MB}` và soi nguyên khối `play_recommendation`.
(Bộ đo: `_v10989_mb_probe.py`, `_v10989_mb_lane_song.py`. Khoá đã che trong log.)

### 3.1 Ba miền đang khuyên gì, dựa trên bao nhiêu lượt

| Miền | Trang bảo | `method` | Cơ sở thật | Nền | Đuôi nhị thức một phía |
|---|---|---|---|---|---|
| MN | nên chơi OFFICIAL | `MN_OFFICIAL_BASELINE_CONTROL` | 11/29 | 38% | p = 0,573 |
| MT | nên chơi OFFICIAL | `MT_OFFICIAL_BASELINE_CONTROL` | 9/35 | 26% | p = 0,580 |
| **MB** | **nên chơi LANE** | `MB_FULL_POOL_D_W06_V1` | **2/8** | 11% | **p = 0,217** |

**MB đang được khuyên đưa tiền theo một lane trên đúng hai lượt trúng.** Với nền 11% và n=8,
chỉ cần **một lượt may** là tỉ lệ nhảy từ 12,5% lên 25% — đủ lật nhãn.

### 3.2 Chuỗi ghi cứng trong nhánh `isLane`

```js
var detail = isLane
  ? ('Lane … đạt ' + p.long_pct + '% (n=' + p.long_n + …) vs official … — vượt rõ + bền.')
```

Chữ **"vượt rõ + bền"** in ra **bất kể cỡ mẫu**, không hề chấm ý nghĩa thống kê. Đây đúng họ
với `62% (hứa hẹn)` mà owner vừa bắt ở vòng đầu — nhưng nằm ở **dòng khuyến cáo chính**, dòng
người đọc tin nhất.

### 3.3 Chân khối mô tả SAI cổng của chính nó

Trang ghi *"cửa sổ dài n≥40"*. Đọc `_v10725_champion_selector.py`:

| Hằng số | Giá trị | Áp cho |
|---|---|---|
| `REC_MIN_LONG_N` | 40 | nền **miền**, cửa sổ 60 ngày |
| `REC_WD_MIN_N` | **8** | đường theo **thứ**, cửa sổ 180 ngày ← **MB đang đi đường này** |
| `REC_MARGIN_PP` | 5 | lane phải vượt official ≥ 5pp |
| `REGIONS_LANE_ALLOWED` | `{"MB"}` | chỉ MB được khuyến cáo LANE (policy owner 15/06) |

MB qua cổng **đúng ở mức sàn 8**. Trang mô tả một cổng nghiêm hơn cổng thật, khiến con số 25%
trông đáng tin hơn thực tế.

### 3.4 Lane được khuyến cáo có còn sống không

| Miền | `method` | Chạy cuối | Tổng dòng |
|---|---|---|---|
| MN | `MN_OFFICIAL_BASELINE_CONTROL` | 05/08 | 212 |
| MT | `MT_OFFICIAL_BASELINE_CONTROL` | 03/08 | 257 |
| MB | `MB_FULL_POOL_D_W06_V1` | **04/08** | 62 |

`MB_FULL_POOL_D_W06_V1` **còn sống** — không phải lane chết như `MN_ADAPTIVE_EXPLOIT_V1`
(ngừng 05/07). Nhưng nó **không có số hôm nay**, mà trang **không có cách nào nói điều đó**:
vòng đầu chỉ thêm `watch_last_run_date` cho lane *theo dõi*, lane *được khuyến cáo* thì không
có trường nào.

### 3.5 Một điều phải nói rõ để không ai hiểu nhầm

Ngày 05/08 `du_doan_test_bundles` vẫn có **8 lane / 15 dòng** ghi mới. Tức **lane test nói
chung CÒN chạy**; chỉ nhóm `{MIỀN}_OUTPUT_V1` của V10692 là tắt. Hai chuyện khác nhau, đừng gộp
làm một.

---

## 4. Hướng xử lý và vì sao chọn — có phương án nào khác, vì sao loại

| Phương án | Nội dung | Chọn? |
|---|---|---|
| **A** | Sửa gốc: nâng `REC_WD_MIN_N` 8→20 trong `_v10725_champion_selector.py` | **LOẠI** — đổi hằng số này là đổi **nội dung bảng** `play_recommendation_shadow`, mà bảng đó còn nơi khác đọc. Đây là quyết định của owner, không phải của agent (§56). Chuyển thành `FU-272` |
| **B** | Giấu khối khuyến cáo khi cỡ mẫu mỏng | **LOẠI** — vi phạm §54: *"output thô phải luôn nhìn thấy được"*. Giấu số là bịt mắt owner |
| **C** | **Giữ nguyên mọi số thô, chỉ hạ LỜI KHẲNG ĐỊNH ở tầng hiển thị**, chấm đuôi nhị thức ngay tại trang | **CHỌN** — đúng §54 (gate chỉ khoá tiền, không khoá dữ liệu), không đụng `QD-014`, không đổi bảng nào, và **cùng cơ chế** đã dùng cho nhãn đài `n=6` ở vòng đầu nên trang nhất quán |

**Vì sao không đợi hỏi owner rồi mới sửa:** đây là **lỗi hiển thị có bằng chứng rõ ràng**, thuộc
đúng nhóm owner đã ra lệnh *"sửa ngay trong phiên"*. Phần **thuộc vùng quyết định** (nâng sàn ở
gốc) thì **không tự làm**, đã tách ra `FU-272`.

---

## 5. Đã làm gì — bảng file × thay đổi, backup, deploy, hash

### 5.1 Backup trước khi sửa

| Nơi | Đường dẫn |
|---|---|
| Local | `backups/v10989b_pre/main.py.pre` (941.042 B) · `backups/v10989b_pre/du-doan-test.html.pre` (223.399 B) |
| VPS | `/root/Lottery_AI_Test/backups/v10989_pre_20260805_114937/` |

### 5.2 File × thay đổi

| File | Thay đổi |
|---|---|
| `web/backend/main.py` | `_build_play_recommendation` trả thêm **`method_last_run_date`** — lane ĐƯỢC khuyến cáo cũng phải khai ngày chạy cuối |
| `web/frontend/du-doan-test.html` | Nhánh LANE **chấm đuôi nhị thức tại trang** (dùng lại `shBinomTail` + `SH_ALPHA=0,10` đã có từ vòng đầu); `p > 0,10` → đầu khối đổi *"nên chơi LANE"* → **"CHƯA đủ bằng chứng để khuyến cáo"**, viền xanh → **hổ phách** · in **`k/n`** thay vì chỉ `n=` · cảnh báo **"⛔ lane này chạy cuối …, KHÔNG có số hôm nay"** · chân khối ghi ĐÚNG **hai** cổng `n≥8` (thứ) và `n≥40` (miền), kèm câu *"n≥8 là ngưỡng mỏng"* |
| `web/backend/_v10982_lich9.py` | `TAI_PHIEN_KHAC_DO_DUOC[08/08] += "FU-272"` (không cập nhật thì J5 TRƯỢT) |
| `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` · `docs/FOLLOW_UP_TRACKER.md` | Prepend bằng `_doc_prepend.prepend()`, đọc lại xác nhận kích thước **tăng** |

**Bộ đo mới dựng:** `_v10989_hau_kiem.py` (hậu kiểm VPS chỉ đọc) · `_v10989_mb_probe.py` ·
`_v10989_mb_lane_song.py` · `_v10989b_render_check.js` (dựng chữ thật).

### 5.3 Deploy

| Mục | Giá trị |
|---|---|
| Giờ | **11:49:37** giờ VN — ngoài khung cấm (05:00–06:30 · 15:30–18:15) |
| PID | **839095 → 842736** ✓ đã đổi |
| `py_compile` | `COMPILE_OK` |
| Service | `lottery` (KHÔNG phải `lottery-ai`) · `active` |

### 5.4 Hash 4 bảng khoá — trước và sau **giống hệt**

| Bảng | Dòng | SHA256 (32 ký tự đầu) |
|---|---|---|
| `predictions` | 11.754 | `ec59cfd5ee8c9a9a59e0009b2d836e2a` |
| `final_bundles` | 475 | `6848318ee93ad48ede3c978bebd79489` |
| `lottery_results` | 15.213 | `92ccf706553921288f2105f96e2a399b` |
| `model_daily_eval` | 11.577 | `c559a75ad34b78ed89ed7d265dca3e13` |

---

## 6. Cổng kiểm — kiểm gì, kết quả từng mục, đạt hay trượt

| # | Kiểm gì | Kết quả | Đạt? |
|---|---|---|---|
| 1 | Cú pháp JS nội tuyến | 2 khối, **0 lỗi** | ✓ |
| 2 | `py_compile main.py` | `COMPILE_OK` | ✓ |
| 3 | PID đổi | 839095 → 842736 | ✓ |
| 4 | Hash 4 bảng khoá | **giữ nguyên hết** | ✓ |
| 5 | Smoke | `/api/health`=**200** · admin=**401** | ✓ |
| 6 | `model_count` official MN | **15** — không đụng `QD-014` | ✓ |
| 7 | cron `v10692` | **0 dòng bật** trước và sau — không lén lật quyết định owner | ✓ |
| 8 | Bộ tự kiểm VPS | **22 phép** · `C22_giao_dien_toan_ven` **OK** | ✓ |
| 9 | `monitoring.html` | **577.617 B**, không tụt kích thước | ✓ |
| 10 | `C18`/`C19` lệch | Có — nhưng **lệch từ 04/08** (biên MT hẹp), đã có `FU-259`/`FU-260` **trước** phiên này. Không phải hệ quả V10989 | ✓ (đã trừ đúng) |
| 11 | **Chữ THẬT 3 miền** | **3/3 đạt**, 0 lỗi — xem 6.1 | ✓ |
| 12 | Cổng lịch nhóm 14 | **8/8** `LICH_CUON_CHIEU_DAT` | ✓ |
| 13 | Cổng lịch nhóm 9 | **8/8** `GIAN_9_MUC_DAT` (J5: 08/08 = 8 mục, mốc tải khớp sổ thật 7/7 ngày) | ✓ |
| 14 | Sổ quyết định owner | **0 TRÔI** · 28 quyết định | ✓ |
| 15 | Sáu mặt quy tắc | đồng bộ · 4/4 `.mdc` tự nạp | ✓ |
| 16 | Briefing đầu phiên | 0 checkpoint quá hạn · 0 mục theo dõi quá hạn | ✓ |

### 6.1 Nghiệm thu bằng CHỮ THẬT, không bằng trường JSON

Chữ người đọc thấy do **hàm JS** dựng ra, không phải do trường JSON. Nên
`_v10989b_render_check.js` **bốc đúng hàm `renderPlayRecommendation` khỏi tệp đang phục vụ**,
đổ payload THẬT lấy từ VPS vào, rồi in chữ sau khi bỏ thẻ HTML:

```
── MB ──
⚠ CHƯA đủ bằng chứng để khuyến cáo — lane FULL POOL D W06 V1 mới dẫn trên mẫu mỏng
Lane FULL POOL D W06 V1 đạt 25% (2/8, gần đây 36%) vs official 11% — chênh này CHƯA
phân biệt được với may rủi (p=0.22 > 0.1). Số thô vẫn hiện nguyên, nhưng không đủ cơ
sở để đưa tiền theo. ⛔ lane này chạy cuối 04/08/2026, KHÔNG có số hôm nay
   [chấm] 2/8 vs nền 11% → p=0.217
   ✓ đã hạ về cảnh báo, không khẳng định
```

Bốn phép chặn trong bộ này: **(a)** không được còn chữ *"nên chơi LANE"* khi p > 0,10 ·
**(b)** không được còn chuỗi *"vượt rõ + bền"* · **(c)** lane khuyến cáo trễ mà không cảnh báo
là trượt · **(d)** không được còn chữ *"hứa hẹn"*. Kết quả **exit 0**.

Bằng chứng đầy đủ: `evidence/15_chu_that_khoi_khuyen_cao_SAU_sua.txt`.

---

## 7. Vướng vấp — mọi chỗ vấp, kèm hậu quả nếu bỏ qua

1. **Vòng đầu chữa chưa hết — lỗi của agent.** Tôi chỉ soi nhánh *"đang THEO DÕI"* vì đó là chỗ
   owner chỉ mặt (`62% hứa hẹn`), mà **không soi nhánh khuyến cáo chính** dù nó **cùng một khối,
   cùng một hàm, cùng một bệnh**.
   **Hậu quả nếu bỏ qua:** owner lại là người phát hiện lần thứ hai — đúng cái vòng lặp owner
   vừa mắng sáng nay. Bài học: khi bắt được một nhãn hứa hẹn, phải **soi hết mọi nhánh của cùng
   hàm dựng**, không chỉ nhánh được chỉ mặt.

2. **Bộ hậu kiểm tôi tự viết báo TRƯỢT vì chính nó gõ nhầm đường dẫn admin.** Dùng
   `/api/admin/v10642/slice-health` (không tồn tại) → trả **404** chứ không phải 401. Lỗi ở bộ
   đo, không ở hệ. Đã đổi sang `/api/admin/play-recommendation` → 401 đúng kỳ vọng.
   **Hậu quả nếu bỏ qua:** một cổng luôn đỏ vì lý do sai sẽ bị người sau tắt đi, rồi **mất luôn
   phép canh thật** — đúng kiểu "xanh giả" ngược.

3. **Bộ deploy đếm chữ `"hứa hẹn"` ra 2 và tự gắn cờ.** Soi lại: cả hai nằm trong **chú thích
   JS** tôi vừa viết để giải thích chỗ sửa, **không phải chữ người đọc thấy**.
   **Hậu quả nếu bỏ qua:** hoặc hoảng vô cớ, hoặc tệ hơn — quen với việc cổng đỏ rồi bỏ qua.
   Đây là bằng chứng thứ hai trong ngày rằng **nghiệm thu bằng đếm chuỗi thô là không đủ**, phải
   dựng chữ thật rồi đọc.

4. **`C18`/`C19` vẫn lệch.** Không phải do phiên này — lệch từ 04/08 vì biên MT hẹp (227s < 300s
   và 467s < 480s), đã có `FU-259`/`FU-260` theo dõi. Bộ hậu kiểm đã được sửa để **trừ đúng hai
   mã này** và vẫn TRƯỢT nếu có phép đỏ nào khác.
   **Hậu quả nếu bỏ qua:** trừ bừa cả cụm sẽ nuốt mất một phép đỏ thật trong tương lai.

5. **Cổng báo cáo bắt ngay `V10989B` chưa có thư mục.** Vì `CHANGELOG` có mục `## V10989b`, cổng
   đòi một thư mục báo cáo riêng — đúng cái đã làm bản quét toàn bộ TRƯỢT 13,5 giờ hôm 04/08
   (V10980b/V10981b/V10982b). **Không né bằng cách đổi tên phiên bản**; đã dựng báo cáo thật này.

---

## 8. Gỡ về

| Việc | Lệnh | Thời gian |
|---|---|---|
| Gỡ 2 tệp runtime (local) | `copy backups\v10989b_pre\main.py.pre web\backend\main.py` · `copy backups\v10989b_pre\du-doan-test.html.pre web\frontend\du-doan-test.html` | ~1 phút |
| Gỡ trên VPS | `cp /root/Lottery_AI_Test/backups/v10989_pre_20260805_114937/{main.py,du-doan-test.html} /root/Lottery_AI_Test/…` rồi `systemctl restart lottery` | ~2 phút |
| Gỡ tài liệu | `git checkout HEAD~1 -- CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md docs/FOLLOW_UP_TRACKER.md web/backend/_v10982_lich9.py` | ~1 phút |

**Rủi ro khi gỡ về: thấp.** Phiên không đụng bảng dữ liệu nào — hash 4 bảng khoá giống hệt
trước/sau. Gỡ về chỉ đưa trang **trở lại chỗ khuyên chơi lane trên 2/8 lượt**.

---

## 9. Theo dõi tiếp — mã FU, ngưỡng hành động bằng số, hạn rà soát

| Mã | Mã đọc | Việc | Hạn | Nhãn | Ngưỡng "xong" đo bằng số |
|---|---|---|---|---|---|
| `FU-272` | `QD0808` | **Owner quyết:** nâng sàn cổng khuyến cáo ở gốc `_v10725` | **08/08** | `AWAITING_OWNER_OK` | `SELECT long_n FROM play_recommendation_shadow WHERE play='LANE'` phải **≥ 20** ở mọi dòng mới |

**Đề xuất kèm cái giá, để owner cân:**

- Nâng `REC_WD_MIN_N` **8 → 20** và đưa điều kiện **`p ≤ 0,10`** vào **thẳng materializer** thay
  vì chỉ chặn ở trang.
- **Cái giá phải nói thẳng:** MB sẽ ra `OFFICIAL` gần như suốt một thời gian dài, khối khuyến
  cáo trông nhàm. **Nhưng thà nhàm còn hơn chỉ tiền theo 2 lượt trúng.**
- **Vì sao chỉ vá ở trang trước:** đổi hằng số là đổi nội dung bảng `play_recommendation_shadow`,
  mà bảng đó còn nơi khác đọc — phải là quyết định của owner.

**Liên quan cùng họ (mở ở vòng đầu, chưa đóng):** `FU-268` (UI0806-1, hạn 06/08 — owner xác minh
lại trang) · `FU-269` (QD0807 — bật lại lane V10692 hay bỏ khối Output) · `FU-270` (SC0807 — bộ
chấm lane test không có cron) · `FU-271` (DO0808 — ngưỡng cỡ mẫu nhãn sức khoẻ đài).

**Hạn rà soát chung:** 08/08/2026 (trùng ngày hết đóng băng `QD-014`).
