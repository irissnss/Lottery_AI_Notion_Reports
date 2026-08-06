# REPORT V11012 — Q16 · Q19 và ĐỀ XUẤT XỬ LÝ TIẾP

> **Ngày:** 2026-08-07 · **Dữ liệu:** đồng bộ `07/08 00:31`, tuổi 0,3 giờ (cổng FU-303 ĐẠT)
> **READ-ONLY** — không mutation, không deploy · script đo commit kèm tại `scripts/`

---

## 1. Tóm tắt

Hoàn tất hai câu cuối của PL19c. Kết quả **đảo một quyết định lớn** và **tìm ra một chỗ hỏng
đang chạy**:

| | |
|---|---|
| **Q16** | Kết luận thắng của RULES-FIRST (V10857, *"official BT hơn GẤP ĐÔI"*) **SỤP ĐỔ** khi đo lại có nền và mở rộng cửa sổ |
| **Q19** | Vá gốc V10884 **giữ được** (0 lệch / 2.112 cặp), nhưng **MB lane chạy sớm 20 phút** nên chỉ thấy 18–21/27 model |

Q16 là bằng chứng mạnh nhất từ trước tới nay cho **FU-291** (gỡ tính ép khỏi prompt).

## 2. Owner yêu cầu gì (nguyên văn)

> *"Làm tiếp đi chứ chờ đợi gì nữa rồi tổng hợp báo cáo lên github đề xuất xử lý tiếp dùm anh
> luôn em"*

## 3. Đào bới / phát hiện

### 3.1 Q16 — "hơn GẤP ĐÔI" là hồi quy về trung bình · `VERIFIED_TEST`

**V10857 (26/07) tuyên bố:** *"Official bundle BT gộp 3 miền: 20,0% (6/30) → 41,7% (10/24) —
hơn GẤP ĐÔI"* và *"LLM any-hit 48,6% → 66,9% (+18,3pp)"*. Đây là căn cứ giữ RULES-FIRST từ 18/07.

**Số học của V10857 tái lập CHÍNH XÁC** — nhưng thiếu hai thứ:

| cửa sổ | n | trúng | tỉ lệ | **NỀN** | **z vs nền** | bốc bừa |
|---|---|---|---|---|---|---|
| TRƯỚC 08–17/07 | 30 | 6 | 20,0% | **34,1%** | **−1,63** | 33,3% |
| SAU 18–25/07 | 24 | 10 | 41,7% | **34,5%** | **+0,74** | 33,3% |

**Cửa sổ "trước" nằm DƯỚI nền 14 điểm** (z=−1,63). Cửa sổ "sau" chỉ trên nền 7 điểm và
**z=+0,74** — không có ý nghĩa. Nghĩa là **"gấp đôi" là bật lên từ một hố xui**, không phải
tiến bộ thật.

**Mở rộng cửa sổ sau tới hôm nay thì hiệu ứng biến mất hoàn toàn:**

| cửa sổ | n | tỉ lệ | nền | **z vs nền** |
|---|---|---|---|---|
| SAU 18/07 → 06/08 | 60 | **33,3%** | 33,8% | **−0,08** |
| SAU 26/07 → 06/08 | 36 | 27,8% | 33,4% | −0,72 |
| TRƯỚC 08/06 → 17/07 | 120 | 26,7% | 33,9% | −1,68 |

**So hai cửa sổ trực tiếp: z = +1,73** — không đạt ngay cả ngưỡng lỏng 1,96, càng không đạt
Bonferroni 3,01.

**Sức mạnh thống kê:** để phát hiện chênh 20 điểm (20%→40%) với sức mạnh 80%, cần
**n ≈ 82 mỗi cửa sổ**. V10857 có **30 và 24**.

⇒ Đây đúng chuỗi *"hứa hẹn rồi rữa"* mà tài liệu dự án đã ghi:
`V10655 → V10672 → V10677 → V10753 → V10789 → V10790` — nay thêm **V10857**.

### 3.2 Q19 — vá gốc GIỮ ĐƯỢC, nhưng còn lỗi thứ hai · `VERIFIED_TEST`

**Lỗi 3 của V10884 (công bố một đằng, chấm một nẻo) đã hết:**
đối chiếu `du_doan_test_bundles.test_bt` với `du_doan_test_results.test_bt` theo `run_id`,
**2.112 cặp / 30 ngày · LỆCH 0**.

**Nhưng Lỗi 2 (chốt khi kho model chưa đủ) vẫn còn — riêng MB:**

| miền | lane chạy lúc | model lane | official có | dòng cuối official về |
|---|---|---|---|---|
| MN | 05:21 | **27** | 27 | 05:31 |
| MT | 16:44 | **27** | 27 | 16:53 |
| **MB** | **17:38** | **18–21** | **27** | **17:47 – 17:58** |

MB lane bắn lúc **17:38** trong khi model official còn về tới **17:58** ⇒ lane **chỉ thấy
18–21 trong 27 model**, thiếu **6–9 model**. Sáu ngày liên tiếp đều vậy.

**Cổng chặn V10884** *(chỉ chạy khi official đã chốt VÀ kho model đủ)* **không hiệu lực cho MB**.

## 4. Hướng xử lý và vì sao chọn

Đề xuất **bốn việc theo thứ tự**, không làm song song để giữ QD-018 (một biến một lần).

### Đề xuất 1 — FU-290 cắt model *(anh ký 08/08, đã đủ bằng chứng)*

Bằng chứng đứng vững sau khi đo lại trên dữ liệu tươi: **0/34 model hơn nền** sau Bonferroni.
Cắt **không mất gì đo được**, mà giảm **94% thời gian** nếu giữ 5 model nhanh nhất.

**§59 bắt buộc anh nói rõ:** *bỏ cờ `output_eligible`* (model vẫn chạy vẫn đo, chỉ không bỏ
phiếu) **hay** *dừng hẳn* (mất ứng viên khỏi pool combo-super). Sàn: **ML ≥ 4 · AI ≥ 3**.

**Rủi ro:** thấp. **Gỡ về:** bật lại cờ, không cần deploy code.

### Đề xuất 2 — FU-291 + FU-298 gộp làm MỘT biến *(sau 20/08)*

Ba bằng chứng nay chụm vào cùng một chỗ:

| | |
|---|---|
| Q16 | căn cứ giữ RULES-FIRST (V10857) **sụp đổ** — z=+1,73, mẫu bằng 1/3 mức cần |
| M4 | đo tiến **≈ đối chứng** (−0,33 / +0,26) · **0/105** luật qua cổng |
| Q9 | §5g thưởng +1đ cho ô **z=−2,54** — ô tệ nhất |

**Việc:** bỏ câu *"BẮT BUỘC/ƯU TIÊN MẠNH chọn từ DANH SÁCH"*, bỏ cộng điểm theo số nguồn ở §5g;
**giữ nguyên** bảng luật và số nguồn như **dữ liệu để model đọc**.

**Vì sao gộp làm một:** cùng một họ — *"prompt tự cộng điểm cho tín hiệu chưa chứng minh"*. Tách
ra thành hai lần deploy sẽ tốn thêm 14 ngày đo mà không tách được nhân quả.

**Rủi ro:** trung bình — đụng vào cách chọn số. **Gỡ về:**
`backups/` + đo tiến 14 ngày, tụt ≥5 điểm bền ⇒ gỡ.

### Đề xuất 3 — Dời giờ MB lane *(làm được ngay, không đụng số official)*

MB lane 17:38 → **18:00** (sau mốc chốt official 17:58). Chỉ đổi giờ cron của **lane test**,
**không** đụng `/du-doan` official.

**Rủi ro:** rất thấp. **Kiểm:** `model_count` của lane phải bằng số model official, như MN/MT.

### Đề xuất 4 — Kiến trúc mined_rules *(FU-300, 3 bước, sau khi 2 xong)*

Chỉ bắt đầu sau khi Đề xuất 2 đo xong 14 ngày. Bước 3 (đưa rules thành đặc trưng ML) theo **M3
vẫn bị từ chối mặc định** trừ khi kèm phép đo chứng minh khác lớp 28 đặc trưng hiện có.

## 5. Đã làm gì

Viết và chạy 2 script đo mới (`q16.py` · `q19.py`), **có cổng tuổi dữ liệu** ở đầu. Cập nhật
`CHANGELOG` · `SSOT` · `FOLLOW_UP`. **Không đụng code production, không deploy.**

## 6. Cổng kiểm

| | |
|---|---|
| Tuổi dữ liệu | **0,3 giờ** — cổng FU-303 ĐẠT |
| Q16 tái lập số của V10857 | 6/30 và 10/24 — **khớp chính xác** |
| Q19 publish vs chấm | **2.112 cặp · LỆCH 0** |
| 4 bảng khoá | không đụng (chỉ `SELECT`, `mode=ro`) |

## 7. Vướng vấp

**Q16 cho thấy một mẫu lỗi lặp lại có hệ thống:** đo *"trước vs sau"* trên cửa sổ ngắn, **không
có nền**, **không đăng ký trước**, và **cửa sổ sau kết thúc đúng ngày báo cáo**. Kết hợp bốn thứ
đó thì gần như chắc chắn ra kết quả đẹp — vì cửa sổ trước được chọn (dù vô tình) là lúc đang xui.

Đây là **lần thứ bảy** trong chuỗi đã ghi. Sáu lần trước dự án đã kết luận *"đừng bật lại bằng
backtest, chỉ bằng đo tiến"* — nhưng V10857 vẫn dùng backtest cửa sổ ngắn để **giữ** một cơ chế.

**Q19 cho thấy vá một lỗi không có nghĩa là vá cả họ.** V10884 nêu ba lỗi; lỗi 3 vá xong và giữ
được, nhưng lỗi 2 vẫn sống ở MB suốt 6 ngày mà không cổng nào kêu.

## 8. Gỡ về

Không có gì để gỡ — READ-ONLY.

## 9. Theo dõi tiếp

| Mã | Nội dung | Hạn |
|---|---|---|
| **FU-311** | **ĐÍNH CHÍNH V10857.** *"Official BT hơn GẤP ĐÔI"* → *"nằm trong may rủi: z=+1,73 (cần ≥1,96), cửa sổ trước ở DƯỚI nền 14 điểm, mở rộng tới 06/08 thì về đúng nền (z=−0,08)"*. Đưa V10857 vào chuỗi *"hứa hẹn rồi rữa"* | 08/08 |
| **FU-312** | **MB lane chạy sớm 20 phút** — 17:38 vs official chốt 17:58, chỉ thấy 18–21/27 model, 6 ngày liên tiếp. Dời sang **18:00**; kiểm `model_count` lane == official như MN/MT | 08/08 |
| **FU-313** | **Cổng chặn kết luận trước/sau thiếu nền.** Mọi so sánh "trước vs sau" phải kèm: nền theo ngày · z vs nền cho **cả hai** cửa sổ · tính sức mạnh (n cần) · đăng ký trước ngày chốt. Thiếu một ⇒ không được ghi là "thắng" | 13/08 |
| **FU-291 + FU-298** | **GỘP làm một biến.** Q16 bổ sung bằng chứng thứ ba: căn cứ giữ RULES-FIRST đã sụp | sau 20/08 |

**Ba con số cần nhớ:** V10857 "gấp đôi" → **z=+1,73** (cần 1,96) · mở rộng cửa sổ → **z=−0,08**
(đúng nền) · MB lane thiếu **6–9/27 model** suốt 6 ngày.
