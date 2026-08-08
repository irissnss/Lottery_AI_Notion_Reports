# REPORT V11041 — PHÂN LOẠI 57 MỤC TREO KHÔNG HẠN, TRÌNH OWNER KÝ GỘP (GĐ-2)

**Ngày:** 2026-08-08, 23:10–23:50 giờ VN *(owner gọi «phiên 09/08»)*
**Phiên bản:** V11041 · **Tầng verdict:** `REPORT_PROVEN` — **chưa thi hành gì**, chờ owner ký

---

## 1. Tóm tắt

Owner ra lệnh phân loại 57 mục treo không hạn thành ba nhóm rồi **trình ký gộp**, và cấm hai
thứ: **đóng hàng loạt mù** · **agent tự đặt hạn** (RM-06).

Kết quả: **A = 43 đề nghị đóng · B = 9 làm được hôm nay · C = 5 luật đứng · D = 0**.

Hai điều owner cần biết trước khi đọc bảng:

**① 57 mục này KHÔNG PHẢI «mất hạn».** Chúng ghi rõ `hạn LX` — *không hạn* theo §58. Câu hỏi
đúng không phải *«hạn của nó đâu?»* mà **«nó còn nghĩa không?»**.

**② Thứ chúng chờ đã chết từ tháng 5.** Đây là bằng chứng quyết định toàn bộ cách xếp nhóm, và
nó đo trên **nguồn production thật**, không đọc lại báo cáo cũ (RM-13).

**Chưa mục nào bị đóng. Chưa hạn nào được đặt.** Bản này là **bản trình ký**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **GĐ-2** — 57 mục không hạn: **PHÂN LOẠI 3 NHÓM rồi trình owner ký gộp — CẤM đóng hàng loạt
> mù, CẤM agent tự đặt hạn (RM-06)**.
>
> Nhóm A (hết hạn → đề nghị đóng) / Nhóm B (còn nghĩa → đề nghị hạn thật, **tránh 15/08 vì ngày
> đó đã có 12 mục**) / Nhóm C (chưa xác định). **Một bảng để owner ký gộp.**

---

## 3. Đào bới / phát hiện

### 3.1 — Chúng từ đâu ra

Toàn bộ 57 mục đến từ **đầu tháng 5/2026**: `V20.3.37.54` … `V98 (2026-05-09 00:50 VN)`.
Treo **ba tháng**. Dải mã thật là **FU-117 … FU-300**, rộng hơn dải `FU-165…FU-209` brief ghi.

33 mục trong đó mang tiêu đề khuôn `DPLX-NNN · Verify lịch sử FU-NNN · hạn LX` — **vỏ sinh máy**
gắn lúc chuẩn hoá mã đọc §58. Nhưng **ruột là việc thật**: mỗi mục có `next_action`,
`last_evidence`, `regression_check` viết tay từ tháng 5.

### 3.2 — Bằng chứng nặng nhất: THỨ CHÚNG CHỜ ĐÃ CHẾT

| đo | nguồn | kết quả |
|---|---|---|
| `weekday_blackspot_shadow` · `loz_stage_trace_shadow` · `model_strength_by_region_weekday_station_daily` | DB sau đồng bộ | dòng mới nhất **2026-05-05** |
| `mt_model_hit_output_drop_shadow` · `model_latency_cost_audit_daily` | DB sau đồng bộ | dòng mới nhất **2026-05-06** |
| `verdict_weight_recalibration_shadow` · `partial_spent_outcome_audit_shadow` | DB sau đồng bộ | **KHÔNG CÓ BẢNG** |
| cron **giờ 23** | **crontab VPS thật** | **0 dòng** — lane V67/V70/V73 (23:35–23:48) đã bị cắt |
| cron **19:08 · 19:12 · 19:14** | **crontab VPS thật** | **không có** — lane V79/V80/V81 đã bị cắt |
| `/du-doan-test` · `/v82-monitor` · `/monitoring` | `main.py` | **cả ba CÒN** |

Hàng chục mục ghi *«accumulate 14 fresh closed days»*, *«run cron 23:48 VN daily»*, *«verify
natural cron tomorrow»*. **Cron đó không còn tồn tại.** Chúng không đang chờ — thứ chúng chờ
**đã ngừng chạy từ tháng 5**, gần như chắc chắn khi `CP-L2` cắt lane research thừa.

---

## 4. Hướng xử lý và vì sao chọn

**Phân loại bằng SCRIPT, không bằng tay.** 57 mục là quá nhiều để gán tay mà không trôi, và
owner phải **chạy lại được** con số agent trình (RM-11). Script
`web/backend/_v11041_phan_loai_57.py` in bằng chứng từng mục, tổng phải cộng ra 57.

**Bốn nhóm, không phải ba.** Owner hình dung A/B/C với C = *«chưa xác định»*. Đào xong thì
`C = 0` nhưng bật ra một loại khác hẳn: **5 mục ghi `due: liên tục`** — chúng là **luật đứng**,
không phải việc có hạn. Trình riêng thành nhóm C và đổi nhóm *«chưa xác định»* thành D. Nhét
luật đứng vào A hay B đều sai: **đặt hạn cho luật đứng là sai loại việc**, còn đóng nó là **bỏ
một cổng đang canh tiền thật**.

**D để rỗng có chủ ý.** Hai mục từng rơi vào D (`FU-122` `FU-129`) đã tra ra bảng chúng đọc
đứng im từ 05/05 ⇒ chuyển sang A. Không đẩy sang owner câu mà agent tự trả lời được.

---

## 5. Đã làm gì

**Dựng `web/backend/_v11041_phan_loai_57.py`** — chỉ phân loại và in bằng chứng.
**KHÔNG** sửa sổ · **KHÔNG** đóng mục · **KHÔNG** đặt hạn.

**Ghi bản trình ký vào `CHANGELOG.md` + `docs/FOLLOW_UP_TRACKER.md`**, ghi rõ *«CHỜ OWNER KÝ»*.

### BẢNG TRÌNH KÝ

| nhóm | số mục | owner ký gì |
|---|---|---|
| **A — đề nghị ĐÓNG** | **43** | *«đóng cả nhóm A»*, hoặc nêu tên mục muốn giữ |
| **B — làm được HÔM NAY** | **9** | cho **hạn thật** từng mục |
| **C — LUẬT ĐỨNG** | **5** | *«không đặt hạn, giữ `liên tục`»* |
| **D — chưa xác định** | **0** | — |

**Nhóm A · 43 mục:** `FU-117` `FU-119`–`FU-130` (trừ `FU-118` `FU-131`) `FU-132`–`FU-148`
`FU-159` `FU-160` `FU-162`–`FU-168` `FU-171` `FU-173` `FU-174` `FU-175`

**Nhóm B · 9 mục** — tất cả cùng một kiểu: owner mở một trang **vẫn còn sống** rồi xác nhận:

| mã | việc |
|---|---|
| `FU-118` `FU-131` | owner mở `/du-doan-test` |
| `FU-149` | owner mở `/v82-monitor` |
| `FU-152` `FU-153` `FU-154` `FU-155` `FU-156` | owner mở `/monitoring`, nghiệm thu tab V86–V90 |
| `FU-300` | kiến trúc `mined_rules` 3 bước — quyết định owner còn treo |

**Agent KHÔNG đề xuất ngày** (RM-06). Chỉ nêu ràng buộc để owner tránh dồn: **15/08 đang có
12 mục · 21/08 có 12 mục** — hai ngày này đã nặng.

**Nhóm C · 5 mục — luật đứng:**

| mã | luật |
|---|---|
| `FU-208` | cổng lợi thế — chỉ đặt tiền thật khi hơn đánh bừa ≥3pp **và** z ≥2 |
| `FU-209` | dừng tỉa model khi khác biệt nhỏ hơn mức đo được |
| `FU-206` | không cắt/đẩy model bằng một thước đo trên cửa sổ ngắn |
| `FU-190` | sáu mặt quy tắc phải nhất quán; `.mdc` phải có `alwaysApply` |
| `FU-188b` | cưỡng chế A55 — không có báo cáo công khai = phiên chưa xong |

---

## 6. Cổng kiểm

```
python web/backend/_v11041_phan_loai_57.py
→ A=43 · B=9 · C=5 · D=0 · tổng=57  ✓ khớp 57
→ Script KHÔNG sửa sổ, KHÔNG đóng mục, KHÔNG đặt hạn. Chờ owner ký (RM-06).
```

Bản in đầy đủ kèm lý do từng mục: `evidence_phan_loai_57.txt` trong thư mục này.

| cổng | kết quả |
|---|---|
| `_v11015_cong_chan_cat_cut.py` | 0 — không tệp nào ngắn đi bất thường |
| `_v11040_kiem_dac_trung.py` | 0 `DAC_TRUNG_V11040=DAT` |
| `_v11040_kiem_cat_cut.py` | 0 `CAT_CUT_V11040=DAT` |

**Quét số hiệu BỐN NƠI trước khi cấp `V11041`:** `V11041` **TRỐNG — dùng được** (in trong
report V11040 cùng phiên).

---

## 7. Vướng vấp — bộ phân loại tự sai hai lần, ghi lại chứ không giấu

**7.1 — Phép «cron chết theo giờ» sai kiểu RM-10.** Bản đầu xếp mọi mục nhắc `19:08/19:12/19:14`
vào nhóm chết. Nhưng crontab thật cho thấy `19:00/19:05/19:10` **vẫn còn** — chỉ là **script đời
sau đã chiếm chỗ** (`_v10677_postdraw_settle` · `_v10801_ml_mark_ab_shadow` ·
`_v10803_chase_bias_shadow`). Giờ trùng **không** chứng minh lane còn sống, mà lane cũ **vẫn**
chết. Kết luận theo giờ là **kết luận theo tên đoán**. Đã đổi sang xét **ngày mục tự nêu**.

**7.2 — Nhóm B thành thùng rơi mặc định.** Bản đầu cho B = 17 mục, trong đó `FU-136`/`FU-137`
chờ cron 23:45/23:48 **đã chết** và `FU-117` neo vào **04/05**. Nguyên nhân: phép soi **cả thân
bài** thay vì soi **đúng câu `next_action`** — thân bài có nhắc một đường dẫn còn sống ở đâu đó
là lọt. Đã siết: chỉ đọc `next_action`, và câu đó **không được chứa mốc ngày cũ**. B rơi
**17 → 9**.

Cả hai lần đều là **thùng rơi mặc định quá rộng** — nhóm «còn nghĩa» nhận mọi thứ không khớp
luật nào. Đó là chỗ một bộ phân loại nói dối êm nhất: nó không báo lỗi, chỉ **im lặng xếp nhầm
về phía an toàn giả**.

---

## 8. Gỡ về

Không có gì để gỡ về mặt thi hành — **chưa mục nào bị đóng, chưa hạn nào được đặt**.

```bash
git revert <mã commit V11041>        # gỡ bản trình ký khỏi hai sổ
rm web/backend/_v11041_phan_loai_57.py
```

---

## 9. Theo dõi tiếp

**Chặn ngay trước mặt:** `GĐ-3` (dọn sổ FOLLOW_UP) **không thể bắt đầu** cho tới khi owner ký
bảng này — dọn sổ tức là đóng mục, mà đóng mục là việc owner ký, không phải agent làm.

| mã | việc | trạng thái |
|---|---|---|
| **57 mục** | owner ký gộp A/B/C | **chờ owner — đang chặn GĐ-3** |
| **FU-379 · TD1008** | bảng tải `QD-022` đếm thiếu từ lúc ký — hai phương án A/B | **chờ owner** |
| `FU-319` `FU-320` | `OWNER_DECISION_NEEDED`, đã có hạn **14/08** | đang chờ tới hạn |
| `FU-369` | cổng cấp số hiệu — **đã va chạm 5 lần trong 2 ngày** | GĐ-4, chưa làm |
| `FU-350` `FU-360` `FU-375` | hàng đợi GĐ-4 | chưa làm |
| `FU-284` | **cấm kết luận trước 21/08** | đang đo |

**Một câu nói thẳng về nhóm A:** đóng 43 mục **không phải là làm xong 43 việc**. Nếu owner còn
muốn câu trả lời của mục nào trong đó — ví dụ `FU-164` (rò rỉ chéo miền, 30 ngày cho MN→MT
+13,70pp) hoặc `FU-174` (`combo_super` dùng win-rate, trái `BT_NORTH_STAR`) — thì phải **dựng
phép đo mới**, không nghiệm thu được bản cũ. Xin owner nêu tên mục muốn giữ lại.

---

*Báo cáo này đẩy **cùng phiên** với commit (A55 · §57.2).*
