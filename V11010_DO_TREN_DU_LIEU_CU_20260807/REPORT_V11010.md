# REPORT V11010 — 17 BẢN ĐO TRÊN DỮ LIỆU CŨ: soi lại toàn bộ, con số nào đổi

> **Ngày:** 2026-08-07 · **Loại:** audit ngược, READ-ONLY
> **Hash 4 bảng khoá local:** PRE = POST · không mutation · không deploy
> **Nguồn đối chiếu:** truy vấn thẳng VPS (read-only), KHÔNG đồng bộ về local để giữ bất biến hash

---

## 1. Tóm tắt

Owner hỏi: *"thế trước đo PL19a và PL19b thì sao em? có đo trên nền dữ liệu cũ không và các vấn
đề trước đó nữa?"*

**Có.** Lần đồng bộ dữ liệu sống cuối cùng là **05/08 12:11**. Sau đó **không đồng bộ lần nào**.
Toàn bộ **17 bản V10991 → V11009** đo trên dữ liệu cũ từ **9 đến 35 giờ**.

Soi lại từng con số đầu bài trên VPS: **6 kết luận GIỮ NGUYÊN**, **2 kết luận PHẢI SỬA**,
**1 con số cần làm rõ phạm vi đếm**.

Đây là **lỗi quy trình**, không phải lỗi tính toán — CLAUDE.md đã ghi rõ *"Trước mọi việc
accuracy / audit / forensic dùng bản local: chạy `python web/_sync_live_forensic_inputs.py`"* và
*"Trích dẫn `artifacts/live_sync/latest_manifest.json` khi dùng bản local làm bằng chứng"*.
Agent **không làm cả hai**, suốt 17 bản liên tiếp.

## 2. Owner yêu cầu gì (nguyên văn)

> *"thế trước đo PL 19a và PL19b thì sao em? có đo trên nền dữ liệu củ không và các vấn đề trước
> đó nữa có đo trên dữ liệu của không em? em làm việc kiểu gì mà chả tư duy gì cả vây nhỉ? hãy
> xem lại dùm a toàn bộ đi nào. Sua đó cập nhật báo cáo chi tiết đầy đủ len github dùm a nha"*

## 3. Đào bới / phát hiện

### 3.1 Phạm vi nhiễm — đối chiếu mốc đồng bộ với mốc commit · `VERIFIED_TEST`

**Đồng bộ tháng 8** (553 lần từ 20/04, thư mục `artifacts/live_sync/`):

| ngày | giờ |
|---|---|
| 02/08 | 21:14 · 22:45 |
| 04/08 | 21:37 · 21:38 · 21:43 |
| **05/08** | 10:10 · **12:11 ← lần cuối** |
| **06/08** | **KHÔNG LẦN NÀO** |

**Commit sau mốc 05/08 12:11:**

| bản | giờ commit | độ cũ dữ liệu |
|---|---|---|
| V10991 · V10991b | 05/08 21:36 · 21:44 | **~9 giờ** |
| V10992 | 05/08 22:32 | ~10 giờ |
| V10993 → V10999 | 06/08 13:38 → 18:38 | **~25–30 giờ** |
| V11000 → V11002b | 06/08 18:53 → 20:13 | ~31 giờ |
| V11003 → V11009 | 06/08 20:57 → 23:30 | **~33–35 giờ** |

**17 bản.** `prediction_trace.jsonl` cũng đóng băng cùng mốc (mtime `05/08 12:12`), nên phép đo
độ trễ của V11005 cũng dùng bản cũ.

**Lưu ý:** `data/lottery_ai.db` có mtime `06/08 23:29` — nhưng đó là do **chính script V11003
của agent ghi vào local** (thêm cột `giai_doan`, tạo bảng `mined_rule_doi_chung`), **không phải
do đồng bộ**.

### 3.2 Soi lại từng con số trên VPS — cái nào đổi · `VERIFIED_TEST`

| # | con số | local (đã công bố) | **VPS (thật)** | phán xử |
|---|---|---|---|---|
| 1 | model hơn nền sau Bonferroni | **0/34** | **0/34** | ✅ **GIỮ** |
| 2 | bầy đàn MN | 21,6 model → 9,2 số | 21,7 → 9,2 (2,36×) | ✅ **GIỮ** |
| 3 | số đài đang sống | 41 | **41** · 0 đài lạ mới từ 05/08 | ✅ **GIỮ** |
| 4 | bundle làm bù | 90 | **90** | ✅ **GIỮ** |
| 5 | bảng chi phí rỗng | 0/4033 | **0/4033** (cả cost lẫn latency) | ✅ **GIỮ** |
| 6 | hội tụ "3 nguồn" | n=294, z=−2,51 | n=**302**, z=**−2,54** | ✅ **GIỮ, vững hơn** |
| 7 | **`DO_TIEN`** | **15 dòng / 1 ngày / 15 luật** | **45 dòng / 3 ngày / 45 luật** | ❌ **SAI — gấp 3** |
| 8 | **bảng A/B đứt 05–06/08** | *"ĐỨT"*, 21/28 ngày | **KHÔNG ĐỨT**, 23/28, liên tục | ❌ **SAI HẲN** |
| 9 | shadow `output_eligible=0` | 512 | 8.890 (toàn thời gian) | ⚠️ **khác phạm vi đếm** — cần làm rõ |

Riêng #9: truy vấn VPS của báo cáo này đếm **toàn thời gian**; con số 512 của V10994 nhiều khả
năng đếm **theo cửa sổ**. **Chưa kết luận là sai** — phải đối chiếu đúng cùng phạm vi.

### 3.3 Hai kết luận phải sửa · `VERIFIED_TEST`

**(a) FU-297 dựng trên tiền đề SAI.** Bảng `v10801_ml_mark_ab_daily` **chưa bao giờ đứt** — job
ghi đều **19:05 mỗi ngày**, VPS có đủ 05/08 và 06/08 (520 dòng, max 06/08).

| | PL19b nói | **SỰ THẬT** |
|---|---|---|
| bảng A/B | *"ĐỨT 05–06/08"* | **không đứt** |
| ngày forward từ 15/07 | 21/28 | **23/28**, liên tục |
| mốc chốt samday MT | *"dời 12/08 → 17/08"* | **12/08 KHẢ THI** — đủ 28 ngày vào **~11/08** |

**(b) `DO_TIEN` gấp 3 con số đã báo.** 45 dòng / 3 ngày / 45 luật, không phải 15/1/15.

**Nhưng kết luận FU-286 KHÔNG đổi:** ước tính "~140 ngày" dựa trên **nhịp 1 lượt/tuần/luật**
(mỗi luật chỉ chấm vào đúng THỨ của nó), không dựa trên số dòng hiện có. Vẫn **0 luật có ≥5
lượt tiến**. Hạn 24/12 **giữ nguyên**.

### 3.4 Kiểm chứng độc lập B1·B2·B3·B4 — 11/11 KHỚP · `VERIFIED_TEST`

Viết truy vấn mới, thuật toán khác PL19b (SQL thuần thay Python dict · `substr` SQLite thay
`datetime` Python · một câu `GROUP BY` thay nhiều câu). **11/11 khớp** ⇒ PL19b **tính đúng trên
dữ liệu nó có**; sai lệch duy nhất đến từ **độ cũ của dữ liệu**, không từ thuật toán.

**Độ bền hiệu ứng hội tụ** — có ở cả hai nửa, cùng chiều:

| | 1–2 nguồn | **3 nguồn** | ≥4 nguồn |
|---|---|---|---|
| nửa đầu 08/05–21/06 | +0,48 | **−1,57** | −0,64 |
| nửa sau 22/06–nay | −1,30 | **−1,98** | −0,80 |
| gộp | −0,55 | **−2,51** | −1,02 |

Không nửa nào **một mình** vượt Bonferroni; chỉ bản gộp vượt.

**B4 — Q15 GIỮ NGUYÊN nhưng bằng chứng phải sửa.** `ml_train.py` và `meta_train.py`
**KHÔNG TỒN TẠI** — "không đọc được" nghĩa là agent dùng **danh sách tệp đoán**. Quét lại đường
train THẬT: `lstm_model.py` · `meta_learner.py` · `ml_models.py` · `optuna_tune.py` ·
`run_full_training.py` · `run_backfill_training.py` · `_retrain_all.py` ·
`meta_data_collector.py` — **cả 8 tệp = 0 tham chiếu** `mined_rule`/`rule_engine`/`rule_id`.

Nhưng phát hiện thêm **14 tệp production khác** chạm rules mà PL19b bỏ sót: `database.py` (42) ·
`filter_2_so_cuoi.py` (29) · `combo_super.py` (14) · `mb_rule_ranker.py` (13) ·
`cross_region.py` (7)… ⇒ **sơ đồ đường đi của một luật rộng hơn 3 tầng đã vẽ**.

### 3.5 Ba mục phụ đã xong

- **D1 — `fresh_cross_tails` chỉ tới LSTM là CỐ Ý.** `scheduler.py:1993-1994` ghi rõ:
  *"include_same_day_cross — pass to meta/xgb/rf … fresh_cross_tails — pass to lstm for
  probability boost"*. Hai kênh cho hai kiến trúc. **FU-299 vẫn đứng** vì MB thiếu MN(D) ở
  **cả hai** kênh.
- **E2 — không có lỗi.** `target_weekday=1` = **T3** (chỉ số 0-based). Báo cáo ghi "MN/T3"
  **đúng**; evidence in số thô. Sửa **script in**, không sửa báo cáo.
- **E3 — KHÔNG có config drift.** `git diff --ignore-all-space --numstat -- web/backend/` →
  **0 tệp**. 48 tệp `M` chỉ khác **CRLF/LF**.

## 4. Hướng xử lý và vì sao chọn

**Không đồng bộ trong gói này.** Đồng bộ sẽ làm đổi hash 4 bảng local, phá bất biến READ-ONLY
mà brief đặt ra. Thay vào đó **truy vấn thẳng VPS read-only** — vừa có sự thật, vừa giữ bất biến.

**Không sửa vội các báo cáo cũ.** 6/9 con số giữ nguyên; chỉ 2 con số sai và 1 cần làm rõ phạm
vi. Đính chính đúng 3 chỗ đó, giữ nguyên phần còn lại — sửa hàng loạt sẽ tạo dị bản.

**Đề xuất cổng chặn, không phải nhắc nhở.** Lỗi này lặp 17 lần liên tiếp nghĩa là **nhắc không
đủ** — phải có cổng máy chặn.

## 5. Đã làm gì

**Không sửa gì trong code hay dữ liệu.** Chạy 3 script đo READ-ONLY (`b123.py` · `b4.py` ·
`kiem_lai_vps.py`), trong đó `kiem_lai_vps.py` chạy **trên VPS** qua SSH, chỉ `SELECT`.

Kết quả thô lưu `evidence/`, kèm **lịch sử đồng bộ** và **mốc commit** để đối chiếu độc lập.

## 6. Cổng kiểm

| | |
|---|---|
| `predictions` local | 11.754 dòng `96bf3180…` **PRE = POST** |
| `final_bundles` local | 475 dòng `f8d7eb8f…` **PRE = POST** |
| `lottery_results` local | 15.213 dòng `3c334771…` **PRE = POST** |
| `model_daily_eval` local | 11.577 dòng `75fffeac…` **PRE = POST** |
| Truy vấn VPS | chỉ `SELECT`, mở DB bằng `mode=ro` |
| B1·B2·B3·B4 | **11/11 KHỚP** — không kích hoạt STOP |

**STOP CONDITIONS:** official nhiễm hindsight **không** · bundle ghi lại sau FINAL **không** ·
mutation/deploy **không thực hiện** · thiếu dữ liệu **đã ghi rõ**.

## 7. Vướng vấp

**Lỗi quy trình lặp 17 lần liên tiếp.** CLAUDE.md có đúng hai câu về việc này:

> *"Trước mọi việc accuracy / audit / forensic dùng bản local: chạy
> `python web/_sync_live_forensic_inputs.py`."*
> *"Trích dẫn `artifacts/live_sync/latest_manifest.json` khi dùng bản local làm bằng chứng."*

Agent **không làm cả hai**, suốt V10991 → V11009. Không cổng nào chặn, không ai bắt — cho tới
khi owner đối chiếu.

**Vì sao lỗi này sống được lâu:** mọi phép đo vẫn **chạy trơn và ra số đẹp**. Dữ liệu cũ không
gây lỗi, không cảnh báo, chỉ **thiếu vài dòng cuối** — nên không có triệu chứng nào để nghi.
Đây đúng loại lỗi mà **§60 nói phải có phép máy chứng minh, không được tin vào "chạy được là
đúng"**.

**Bài học cụ thể:** phép kiểm `hash 4 bảng PRE=POST` mà agent tự hào suốt hai gói **chỉ chứng
minh không ghi bậy**, **không** chứng minh dữ liệu đúng thời điểm. Hai chuyện khác nhau hoàn toàn.

## 8. Gỡ về

**Không có gì để gỡ** — READ-ONLY, không đụng code, dữ liệu, hay production.

Riêng bản local: V11003 đã ghi vào `data/lottery_ai.db` (cột `giai_doan` + bảng
`mined_rule_doi_chung`). Đồng bộ lại từ VPS sẽ **ghi đè mất** hai thứ đó — cần chạy lại
`_v11003_m4_doi_chung_luat.py --dung` sau khi đồng bộ.

## 9. Theo dõi tiếp

| Mã | Nội dung | Hạn |
|---|---|---|
| **FU-297** | **ĐÓNG — tiền đề SAI.** Bảng A/B chưa bao giờ đứt. **Giữ mốc chốt samday MT 12/08** (đủ 28 ngày ~11/08), KHÔNG dời 17/08 | 07/08 |
| **FU-303** | **CỔNG CHẶN AUDIT KHI DỮ LIỆU CŨ.** Mọi script đo phải đọc `latest_manifest.json`; `sync_completed_at` cũ hơn **6 giờ** ⇒ **từ chối chạy** kèm câu nhắc lệnh đồng bộ. Nhắc suông đã thất bại 17 lần | 08/08 |
| **FU-304** | **ĐÍNH CHÍNH `DO_TIEN`** trong REPORT_V11003 và trang V6: 15/1/15 → **45/3/45**. Kết luận FU-286 (hạn 24/12) **không đổi** vì dựa trên nhịp 1 lượt/tuần/luật | 08/08 |
| **FU-305** | **Làm rõ phạm vi đếm shadow** `output_eligible=0`: V10994 báo 512, VPS toàn thời gian 8.890. Xác định V10994 đếm cửa sổ nào, ghi rõ phạm vi vào báo cáo | 13/08 |
| **FU-306** | **Vẽ lại sơ đồ đường đi của một luật.** PL19b chỉ soi 3 tầng; thật ra **14 tệp production khác** chạm rules. Bổ sung vào FU-300 trước khi trình phương án kiến trúc | 13/08 |
| **FU-286** | **GIỮ hạn 24/12** — con số đầu vào sửa từ 15 lên 45 nhưng nhịp tích luỹ không đổi; vẫn **0 luật có ≥5 lượt tiến** | 24/12 |

**Ba con số cần nhớ:** đồng bộ cuối **05/08 12:11** · **17 bản** đo sau đó · **6 giữ / 2 sai /
1 cần làm rõ**.
