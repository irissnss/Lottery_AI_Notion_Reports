# REPORT V11052 — Q1 THẨM ĐỊNH DẪN XUẤT v93 · Q3 VÁ FU-360 (deploy sáng mai)

> **Cùng thư mục với `REPORT_V11050.md`** theo lệnh owner *«nối báo cáo vào REPORT_V11050, không
> mở folder mới»*. Tệp này là bản đầy đủ 9 phần cho riêng V11052.

**Ngày:** 2026-08-09, 14:20 → 14:40 giờ VN · **Tầng verdict:** `REPORT_PROVEN` (Q1 · read-only) ·
`TEST_PROVEN, CHƯA DEPLOY` (Q3)

## 1. Tóm tắt

**Q1: phát hiện lớn nhất của GĐ-B bị chính phép thẩm định bác bỏ.** Con số *«65,6% dòng đề xuất
trọng số lệch ≥0,05»* là **tạo tác của công thức**, không phải tín hiệu. Em **rút lại** hai câu của
chính em.

**Q3: vá FU-360 xong, thử chặn 5/5 đạt**, nhưng bản vá chạm `save_prediction` ⇒ theo đúng điều kiện
owner đặt, **KHÔNG deploy hôm nay** — sáng mai 10/08 kèm canh 24h.

## 2. Owner yêu cầu gì (nguyên văn)

> **Q1.** *«ĐƯỢC thẩm định dẫn xuất READ-ONLY: kiểm nó có trừ VIF/nền chưa, dẫn xuất từ đâu, cửa
> sổ nào. CẤM dùng kết quả làm căn cứ đổi số trước 21/08. Trước 20/08 phải có: ngưỡng đăng ký
> trước … (đề xuất khung: ≥3pp · z≥1,96 · ≥30 ngày · áp trên lane shadow trước).»*
>
> **Q3.** *«FU-360 phương án ③ — ĐÃ DUYỆT: chặn ở tầng GHI khi `run_source` khác … Hôm nay: PLAN +
> thử trên bản sao DB + viết thử chặn thật … Deploy sớm nhất sau 18:15 hôm nay, CHỈ KHI thử chặn
> thật đạt và không chạm đường ghi đang chạy … nếu chạm đường ghi production → để sáng mai 10/08,
> kèm canh 24h sau deploy.»*

## 3. Đào bới / phát hiện

### Q1 — dẫn xuất thật

```python
# ... For now just store any_hit_pct/100 baseline.
proposed = max(0.4, min(1.5, round(0.5 + 1.0 * (any_pct / 100.0), 3))) if n >= 5 else cur_w
```

`proposed = clip(0.5 + any_hit_pct/100, 0.4, 1.5)`. **Hai hằng số `0.5` và `1.0` không có nguồn
gốc.** Chú thích của chính tác giả tự khai *«For now»* / *«later if available»* — **bản tạm chưa
làm xong, đã chạy 122 ngày**.

Kiểm định danh 30 ngày: **687/957 = 71,8%** khớp đúng công thức; **299** dòng còn lại là
`n_total < 5` ⇒ lệch **bằng 0 theo cấu tạo**.

**Chứng minh là tạo tác:**

| trọng số hiện tại | n | chênh TB | `any_hit_pct` TB |
|---|---|---|---|
| 0,40 | 182 | **+0,642** | 54,2% |
| 1,00 | 206 | **+0,112** | 61,2% |
| 1,50 | 270 | **−0,487** | 51,3% |

Ba nhóm trúng **gần như nhau** mà «chênh» khác hẳn ⇒ chênh do **trọng số đang dùng**, không do
hiệu năng. `any_hit_pct` TB 55,2% nên công thức ép mọi thứ về **~1,05**.

**Bảng KHÔNG có** `baseline` · `vif` · `ci_low/high` · `z` · `p_value` · `n_days`.
**Cửa sổ:** 30 ngày trượt kết thúc đúng `target_date`, **không chạm tương lai** ⇒ không có bẫy nhìn
trước ở chỗ này.

### Q3 — gốc bệnh và đo

`predictions` `UNIQUE(date, target_region, ai_model)` **thiếu `run_source`** ⇒ `INSERT OR REPLACE`
cho lượt sau ghi đè lượt trước **không để lại dấu**. Production: 9 giá trị `run_source`;
`shadow_auto_eval` **4.035 dòng** chung bảng với `auto_daily` **4.271**; 7 ngày = **527 cặp / 527
dòng** (một dòng mỗi cặp **theo cấu tạo** ⇒ va chạm **không thể phát hiện sau sự việc**).

## 4. Hướng xử lý và vì sao chọn

**Q1: công bố đính chính thay vì im lặng.** Con số đã nằm trong báo cáo công khai; sửa lén là tệ
hơn sai.

**Q3: chặn theo LANE, không theo chuỗi `run_source`.** Làm đúng câu chữ sẽ **hỏng production ngay** —
đường chính thức đi qua `auto_daily` → `rerun_post_mn`/`rerun_post_mt` → `rerun_after_verify`
(6/9 nhãn thuộc đường chính thức). Cái cần chặn là **bắc cầu giữa hai lane**.

**Q3: không deploy hôm nay** — điều kiện owner tự đặt đã loại trừ, vì bản vá chạm đường ghi
production.

## 5. Đã làm gì

| việc | kết quả |
|---|---|
| dossier B'1 | `docs/B1_THAM_DINH_DAN_XUAT_V93_20260809.md` — dẫn xuất · định danh · chứng minh tạo tác · 4 thứ thiếu · cửa sổ · đính chính · khung ngưỡng §8 |
| vá `database.py` | `_lane_cua_run_source()` + chặn chéo lane **trước** mọi cơ chế cũ trong `save_prediction()` |
| thử chặn | `_v11052_thu_chan_cheo_lane.py` — **5/5**, `CHAN_CHEO_LANE_V11052=DAT` |
| **KHÔNG deploy** | `database.py` nằm trong git, **chưa lên VPS** — drift 25 → **26** (trần 30), có chủ ý và đã ghi |

## 6. Cổng kiểm

```
V  : cao nhất V11051 · trống tiếp V11052      ✓ dùng V11052
FU : cao nhất FU-393 · trống tiếp FU-394      (không sinh mã mới)
```
**Trần sinh mã: 3/5** — không tăng ở V11052.

**Thử chặn thật (RM-15), chạy trên BẢN SAO:** DB tạm dựng từ **387/387 câu lược đồ thật** đọc từ
`sqlite_master` production, **không chép một dòng dữ liệu**, gọi **chính `save_prediction` thật**.

| # | tình huống | mong đợi | kết quả |
|---|---|---|---|
| 1 | ghi mới OFFICIAL | QUA | ✅ |
| 2 | ghi đè **cùng lane** | QUA | ✅ luồng chính thức không gãy |
| 3 | OFFICIAL→TEST | CHẶN | ✅ số cũ giữ nguyên |
| 4 | TEST→OFFICIAL | CHẶN | ✅ |
| 5 | `run_source` rỗng | QUA | ✅ |

`THI_HANH_57_V11043=DAT` · `KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI` · `CONG_K1_V11050=DAT` 8/8.

## 7. Vướng vấp

**7.1 — Cách trình bày B4 nghiêng hơn mức bằng chứng cho phép.** Em có ba câu cảnh báo nên **không
con số nào bị dùng làm căn cứ**, nhưng tiêu đề *«phát hiện lớn nhất»* đã đi trước phần thẩm định.
Ghi lại theo **RM-17**.

**7.2 — Thử chặn lần đầu chết vì chỉ chép lược đồ `predictions`** ⇒ `get_setting()` thiếu
`app_settings`. Đoán tiếp xem hàm còn chạm bảng nào là đúng thứ **RM-10** cấm ⇒ chép **cả lược đồ**.

**7.3 — Câu chữ Q3 nếu làm đúng từng chữ sẽ gãy production.** Đã tinh chỉnh và **khai rõ chỗ tinh
chỉnh** thay vì im lặng làm khác.

## 8. Gỡ về

Q1 **không đụng runtime** — không có gì để gỡ.
Q3 chưa deploy; nếu mai deploy rồi cần gỡ:
```bash
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test && \
  cp backups/database.py.pre_v11052 web/backend/database.py && systemctl restart lottery'
git revert <commit V11052>
```

## 9. Theo dõi tiếp

| mã | việc | khi nào |
|---|---|---|
| `FU-360` | **deploy sáng 10/08** + so PID + health + **canh 24h** đếm dòng `[CHAN CHEO LANE]` | mai |
| `QD-047` / v93 | viết lại `proposed_weight_30d` + thêm 4 cột (`baseline_pct` · `vif` · `z` · `n_days`) | **gói 21/08** |
| ngưỡng đăng ký trước | khung ở dossier §8 — **owner ký trước 20/08** | trước 20/08 |
| ngưỡng FU-284 | ✅ **ĐÃ CHỐT 9,53** (owner ký 18:37 09/08) — 12,00 đã huỷ | *xong* |

*Đẩy cùng commit (A55 · §57.2).*
