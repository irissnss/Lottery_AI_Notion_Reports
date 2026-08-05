# V10990 — Bỏ khối lane đã nghỉ khỏi `/du-doan-test` + nâng cổng khuyến cáo lên n≥40

**Ngày:** 2026-08-05 (giờ Việt Nam) · **Deploy:** 12:52:07 · **Trạng thái:** ĐÃ DEPLOY, ĐÃ NGHIỆM THU

---

## 1. Tóm tắt

Owner chốt hai việc lúc ~12:05 ngày 05/08 sau khi đọc V10989/V10989b. Cả hai đã làm xong và deploy lúc 12:52:07.

**Việc 1 — bỏ khối số của lane đã nghỉ.** Khối "Output Lane Test" trên `/du-doan-test` đọc bảng `{MIỀN}_OUTPUT_V1`, mà nguồn duy nhất ghi bảng đó (`_v10692_mn_mt_multidir_lane.py`) đã bị gỡ cron ngày 01/08. Từ đó trang lùi về số cũ mỗi ngày. Nay khối số đã bỏ, thay bằng một dòng nói thật trạng thái nguồn. Bảng và lane **giữ nguyên** — bật lại cron là khối tự hiện lại.

**Việc 2 — nâng cổng khuyến cáo lên n≥40.** Trước đây đường theo THỨ chỉ cần `REC_WD_MIN_N = 8`, trong khi chân khối lại mô tả là "n≥40" — mô tả nghiêm hơn thực tế. Nay `REC_WD_MIN_N = REC_MIN_LONG_N = 40`, một sàn duy nhất cho cả hai đường.

**Kết quả đo được sau khi nâng cổng — tốt hơn dự đoán.** Owner đã chấp nhận trước rằng khối khuyến cáo sẽ nhàm đi. Thực tế cả ba miền chỉ rời khỏi lát cắt theo-thứ mỏng và rơi xuống nền miền **rộng hơn nhiều**, chứ không mất khuyến cáo:

| Miền | Trước | Sau |
|---|---|---|
| MN | OFFICIAL · theo thứ · **n=29** | OFFICIAL · nền miền · **n=120** |
| MT | OFFICIAL · theo thứ · **n=35** | OFFICIAL · nền miền · **n=169** |
| MB | LANE · theo thứ · **n=8** | LANE · nền miền · **n=62** |

MB vẫn khuyến cáo LANE, nhưng dựa trên **62 lượt thay vì 8**.

**An toàn:** PID 842736 → 846146 (restart chủ động), health 200, 0 traceback, bốn bảng khoá không đổi một dòng, official MN vẫn 15/15 (bạch thủ 25).

---

## 2. Owner yêu cầu gì (nguyên văn)

Owner được hỏi hai câu và chọn:

> **`FU-269`** — *"Bỏ hẳn khối đó khỏi trang — nguồn đã nghỉ thì đừng hiển thị nữa"*

> **`FU-272`** — *"Nâng hẳn lên n≥40 — nghiêm như chú thích cũ vẫn ghi"*

Bối cảnh: trước đó owner gửi ảnh chụp `/du-doan-test` và nói cụt lủn **"em tự nhìn đi"** (V10989), dẫn tới việc phát hiện trang nói sai bốn chỗ và khuyến cáo dựa trên cỡ mẫu quá mỏng.

---

## 3. Đào bới / phát hiện

### 3.1 Vì sao khối "Output Lane Test" chết

`_v10692_mn_mt_multidir_lane.py` là **nguồn duy nhất** ghi `{MIỀN}_OUTPUT_V1`. Cả 4 dòng cron của nó bị gỡ ngày **01/08** (V10919 — owner duyệt cho 6 lane hết hạn đo nghỉ). Nhưng `main.py` vẫn đọc bảng đó để dựng khối. Dòng cuối từng miền:

| Bảng | Dòng cuối |
|---|---|
| `MN_OUTPUT_V1` | 01/08 05:30:01 |
| `MT_OUTPUT_V1` | 31/07 16:45:01 |
| `MB_OUTPUT_V1` | 31/07 17:39:01 |

Chạy `--dry-run` trên VPS: lane **vẫn chạy tốt** (`bt=62 voted=25/25`). Thuần là cron đã tắt.

### 3.2 Cổng khuyến cáo có hai mức, không phải một

`_v10725_champion_selector.py` trước phiên này:

- `REC_MIN_LONG_N = 40` — áp cho **nền miền** (cửa sổ 60 ngày)
- `REC_WD_MIN_N = 8` — áp cho **đường theo THỨ** (cửa sổ 180 ngày)

Chân khối trên trang lại ghi *"n≥40"*. Tức **mô tả nghiêm hơn thực tế**, và đường mà MB đang đi là đường lỏng.

### 3.3 Còn ai đọc `{MIỀN}_OUTPUT_V1`

Đã soi **cả ai đọc BẢNG** chứ không chỉ ai import module — đây đúng là cái bẫy ghi sẵn trong quy tắc và là nguyên nhân gốc của chính sự cố này. Kết quả: ngoài `main.py`, các nơi khác đều là script đo/khảo cổ chạy tay, không có nơi nào khác hiển thị cho owner.

---

## 4. Hướng xử lý và vì sao chọn

**Việc 1 — ba phương án:**

| Phương án | Đánh giá |
|---|---|
| Bật lại cron lane V10692 | **Loại** — owner đã ký cho lane nghỉ ngày 01/08; tự bật lại là lật quyết định |
| Giữ khối, chỉ ghi "nguồn đã nghỉ" | **Loại** — owner chọn bỏ hẳn |
| **Bỏ khối số, giữ một dòng nói thật** | **Chọn** — đúng ý owner, không xoá bảng/lane, bật lại cron là khối tự về |

**Việc 2 — hai phương án:** nâng lên n≥20 (nhẹ) hoặc n≥40 (nghiêm như chú thích cũ). Owner chọn **n≥40**, chấp nhận đổi lại sự nhàm.

Không xoá bảng, không xoá lane, không đụng đường ra số official.

---

## 5. Đã làm gì

| File | Thay đổi | Trước | Sau |
|---|---|---|---|
| `web/frontend/du-doan-test.html` | Bỏ khối số của lane nghỉ; thêm dòng trạng thái thật; lane nghỉ không còn là mặc định | 225.695 B | **218.579 B** |
| `web/backend/_v10725_champion_selector.py` | `REC_WD_MIN_N = REC_MIN_LONG_N` (= 40); cập nhật docstring cho khớp | 18.297 B | **20.613 B** |

**Backup:** `backups/v10990_pre/du-doan-test.html.pre` · `main.py.pre`

**Deploy:** 12:52:07 giờ VN — ngoài khung cấm (05:00–06:30 và 15:30–18:15).

**Sổ quyết định:** `QD-027` ghi nguyên văn hai lựa chọn owner, **khớp 14/14**.

---

## 6. Cổng kiểm

| Cổng | Kết quả |
|---|---|
| `_v10920_decision_ledger.py` | **0 TRÔI** · `QD-027` khớp 14/14 |
| Health `/api/health` | **200** |
| Service `lottery` | `active`, `NRestarts=0` |
| PID trước → sau | **842736 → 846146** (restart chủ động) |
| Traceback hôm nay | **0** |
| `predictions` | 11.754 — **không đổi** |
| `final_bundles` | 475 — **không đổi** |
| `lottery_results` | 15.213 — **không đổi** |
| `model_daily_eval` | 11.577 — **không đổi** |
| Official MN hôm nay | bạch thủ **25**, **15/15** model, 05:19:51 |
| `monitoring.html` | **577.617 B** — không tụt |

**Nghiệm thu — làm đúng cách đã bắt được lỗi ở V10989b:** bóc hàm dựng khối ra khỏi tệp đang phục vụ, đổ dữ liệu thật vào, bỏ thẻ HTML rồi **đọc chữ**, cho cả ba miền, **trước và sau**. Không nghiệm thu bằng "file giống nhau" hay "header đúng" — đó chính là cách sai đã làm `FU-225` phải đóng `CLOSED_FAIL`.

Bằng chứng: `evidence/chu_truoc_{MN,MT,MB}.txt` và `evidence/chu_sau_{MN,MT,MB}.txt`.

Chữ MB đọc được sau khi sửa:

> ⛔ Luồng MB_OUTPUT_V1 (lane V10692) đã NGỪNG chạy — số cuối cùng ngày 31/07/2026. Khối số của luồng này đã bỏ khỏi trang theo quyết định owner 05/08: nguồn đã nghỉ thì không hiển thị số cũ nữa. Bảng dữ liệu và lane vẫn còn nguyên, bật lại cron là khối tự hiện lại.

Chân khối nay ghi đúng thực tế:

> Cổng dữ liệu (owner nâng 05/08): n≥40 cho cả hai đường — theo THỨ (cửa sổ 180 ngày) và nền miền (60 ngày); lane phải vượt official ≥5pp.

**§54 — số thô vẫn hiện nguyên.** Việc bỏ khối này không làm mất phép đo nào: đó là khối hiển thị của một lane đã nghỉ, không phải output official. Các panel đo song song vẫn còn đủ (`panel_truoc` = `panel_sau` cho cả ba miền).

---

## 7. Vướng vấp

### 7.1 Phiên bị cắt hai lần vì hết hạn mức API

Lần một lúc ~12:40, lần hai lúc ~13:13. **Không mất mát gì**, nhưng phải nói rõ trạng thái từng lúc:

- Lúc 12:42 (kiểm độc lập): VPS **hoàn toàn chưa bị động tới** — file trên máy chủ vẫn đúng bản 11:49, `REC_WD_MIN_N` vẫn là 8. Local đã sửa xong hai file, backup đã có, chưa deploy.
- Lúc 13:14 (kiểm lại): deploy **đã chạy lúc 12:52:07** giữa hai lần cắt. Local và VPS khớp nhau.

**Hậu quả nếu bỏ qua:** nếu không kiểm lại lần hai, sẽ tưởng chưa deploy và deploy đè lần nữa — thêm một lần restart vô ích sát giờ MN.

### 7.2 Nâng cổng chưa trọn — chỗ chọn SỐ vẫn chỉ cần n≥4

**Đây là phát hiện quan trọng nhất của phiên, và nó lộ ra đúng nhờ việc đọc chữ thật sau deploy.**

Owner nâng cổng **khuyến cáo** lên n≥40. Nhưng khối *"Phương pháp riêng cho từng số"* — khối **chọn ra con số hiển thị** — không đi qua `_v10725_champion_selector.py` mà nằm ở `_build_per_number_method_output()` trong `main.py`. Cổng của nó:

| Vị trí số | Hàm | Cổng | Cách chọn |
|---|---|---|---|
| **Bạch thủ** (theo thứ) | `_wd_best()` — `main.py:13605` | **`HAVING n>=4`** | `ORDER BY 1.0*wins/n DESC` — **lấy method có hit-rate cao nhất** |
| Bạch thủ (dự phòng) | `_best()` — `main.py:13624` | `total_runs>=10` | hit-rate cao nhất |
| Số phụ 1 / 2 | `_pos_hit()` — `main.py:13705` | `min_n=10`, cửa sổ 45 ngày | per-position hit cao nhất |

Chữ đọc được trên tab MB **sau khi deploy**:

> 🎯 Bạch Thủ: **45** ← MB_SCREEN_WEIGHTED_V1 (62% BT hit/T3, **n=8**)
> Số phụ 1: 45 ← MB_FULL_POOL_D_W06_V1 (44% …, **n=9**)

Tức là: **lời khuyên** nay cần 40 lượt, nhưng **con số được chọn để hiển thị** chỉ cần **4** lượt. Chênh nhau **mười lần**.

Nặng hơn cả con số nhỏ là **cách chọn**: `ORDER BY 1.0*wins/n DESC LIMIT 1` là **lấy giá trị lớn nhất trong toàn bộ method ứng viên**, không hiệu chỉnh so sánh bội. Với hàng chục method và n=4, tìm ra một method đạt 75–100% gần như chắc chắn xảy ra do may rủi. Đây **đúng cùng một cơ chế** đã bị chỉ mặt ở V10989 với lane "đang theo dõi" (nhảy 76% → 66% → 64% → 62% mỗi ngày vì lấy max trên ~13 ứng viên).

Và chú thích mới viết ở dòng 224 của `_v10725_champion_selector.py` tuyên bố:

> `REC_WD_MIN_N = REC_MIN_LONG_N   # = 40; một sàn duy nhất, không còn chỗ nghiêm chỗ lỏng`

Câu đó **đúng trong phạm vi file đó**, nhưng **sai nếu hiểu là toàn trang** — chỗ chọn số nằm ở file khác và vẫn lỏng. Thêm một mẫu "xanh giả" ở tầng chữ nghĩa.

**Không tự sửa** vì nâng ngưỡng này **đổi con số được hiển thị** trên trang, mà owner vừa ra quyết định ngưỡng ở một chỗ khác — mở rộng sang đây phải hỏi. → **`FU-274`**.

**Hậu quả nếu bỏ qua:** owner vừa yêu cầu siết vì không muốn bị dẫn dắt bởi cỡ mẫu mỏng. Nếu chỉ siết chỗ khuyên mà để nguyên chỗ chọn số, thì trang vẫn hiển thị một con số sinh ra từ 4 lượt — chỉ là không còn dán chữ "nên chơi" bên cạnh. Đó là siết hình thức.

### 7.3 Cây làm việc nhiều nhiễu

`git status` đang có hàng chục file `M` do trôi ký tự kết thúc dòng (Google Drive), không phải thay đổi thật. Đã chỉ stage đúng file của phiên. **Hậu quả nếu bỏ qua:** `git add -A` sẽ nuốt cả nhiễu lẫn thay đổi của phiên khác — đúng lỗi đã xảy ra sáng 03/08.

---

## 8. Gỡ về

Khoảng 2 phút, chỉ gỡ tầng hiển thị và một hằng số:

```bash
# 1. Khôi phục hai file từ backup
scp backups/v10990_pre/du-doan-test.html.pre root@14.225.224.89:/root/Lottery_AI_Test/web/frontend/du-doan-test.html
git checkout HEAD -- web/backend/_v10725_champion_selector.py   # về REC_WD_MIN_N = 8
# rồi đẩy file này lên VPS

# 2. Restart đúng tên service
ssh root@14.225.224.89 "systemctl restart lottery && sleep 3 && systemctl show -p MainPID --value lottery"

# 3. Kiểm
curl -s -o /dev/null -w '%{http_code}\n' https://xs.io.vn/api/health   # phải 200
```

**Không cần đụng cơ sở dữ liệu** — phiên này không ghi một dòng nào vào bốn bảng khoá. Bảng `{MIỀN}_OUTPUT_V1` và lane V10692 **chưa hề bị xoá**; muốn khối số hiện lại thì chỉ cần bật lại cron lane, không cần gỡ bản vá này.

---

## 9. Theo dõi tiếp

| Mã máy | Mã đọc | Nội dung | Hạn | Trạng thái |
|---|---|---|---|---|
| `FU-269` | `QD0807` | Bỏ khối lane nghỉ khỏi `/du-doan-test` | 07/08 | **CLOSED_PASS** — nghiệm thu đọc chữ 3/3 miền |
| `FU-272` | `QD0808` | Nâng cổng khuyến cáo `REC_WD_MIN_N` | 08/08 | **CLOSED_PASS** — n=8→40; MN 29→120, MT 35→169, MB 8→62 |
| **`FU-274`** | **`QD0808-1`** | **Chỗ chọn SỐ hiển thị (`_wd_best` `HAVING n>=4`, `_pos_hit` `min_n=10` trong `main.py`) vẫn lỏng gấp mười lần cổng khuyến cáo n≥40 — owner quyết có nâng cho khớp không** | **08/08** | **OWNER_LOCK** |

**Ngưỡng hành động của `FU-274`** — phải đo trước khi chốt, không đổi thẳng:

1. Đo trên 30 ngày: nếu nâng `_wd_best` từ `n>=4` lên `n>=40` thì **bao nhiêu ô (ngày × miền) mất hẳn số hiển thị**, bao nhiêu ô đổi số. Nếu mất quá nửa số ô thì phải cân nhắc mức trung gian thay vì 40.
2. Đo **hit-rate thật** của số do `_wd_best` chọn trên 30–90 ngày, so với `OFFICIAL_BASELINE_CONTROL`. Nếu không hơn official ở mức có ý nghĩa (≥3pp, z≥2) thì cách chọn max-trên-nhiều-ứng-viên này **không đáng giữ ở bất kỳ ngưỡng nào**.
3. Bất kể owner chọn gì, **phải sửa `ORDER BY 1.0*wins/n DESC LIMIT 1`** để không lấy max trần trụi — tối thiểu là in kèm số ứng viên đã duyệt và p-value, như đã làm với khối khuyến cáo ở V10989b.
4. Nếu owner giữ nguyên ngưỡng, **phải sửa chú thích dòng 224** cho hết tuyên bố "một sàn duy nhất", vì phạm vi thật chỉ là một file.

`FU-270` (bộ chấm lane test không có cron, dừng từ 28/07) — cần rà lại: bỏ khối hiển thị rồi thì mục này còn ý nghĩa gì, hạn 07/08.

**Không áp dụng vì:** phiên này không đụng đường ra số official nên không có mục theo dõi nào về `QD-014`; freeze còn nguyên hiệu lực đến hết 08/08.
