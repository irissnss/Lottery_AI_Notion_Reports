# CONVERSATION CONTEXT — V11058 · 10/08/2026 đêm

## Owner nói gì (NGUYÊN VĂN)

> *«Các đề xuất an toàn tiến hành ngay được thì tiến hành xử lý đi em, còn gì chưa rõ, chưa xác
> định thì tiếp tục đảm bảo chỉ có cải tiến nâng cao chính xác dự đoán nha em đừng đi lùi nữa»*

Hai vế. Vế đầu là lệnh thi hành. **Vế sau — «đừng đi lùi» — mới là thứ định đoạt cách làm.**

Nó loại bỏ ngay một cám dỗ: sau khi V11057 đo được lợi thế hệ thống chỉ **+0,34pp**, phản xạ tự
nhiên là **gỡ bớt** — tắt luật, cắt model, bỏ cơ chế. Owner chặn đúng chỗ đó. Nên đêm nay
**không việc nào gỡ thứ gì**, tất cả chỉ **thêm phép đo**.

Bằng chứng: **hash 4 bảng khoá PRE = POST y hệt**.

---

## Chuyện chính của phiên: một tín hiệu DƯƠNG, và agent phải tự rút lại

Đây là lần đầu sau nhiều phiên có con số dương.

### Nó xuất hiện thế nào

Đo B4 (nhánh CHỐT GẤP) thì lộ ra `combo_super.py:1901` có **bảng bonus RIÊNG**:

```python
_chot_bonus = {'shadow': 0.0, 'soft': 0.40, 'active': 0.80}.get(_rm, 0.0)
```

`soft` đang chạy ⇒ **+0,40** mỗi đuôi hội tụ — trong khi **mọi tài liệu** (kể cả `CHANGELOG.md:222`)
chỉ nhắc **`+0,15`** của nhánh khác. **Gấp 2,7 lần, và chưa ai ghi nhận nhánh này.**

Journal volatile nên không dùng log để chứng minh nhánh có chạy (RM-20). Nên đo **đầu vào** thay
vì gắn thiết bị đo vào mã (chạm module sinh số ⇒ QD-041 khoá): gọi thẳng
`extract_rule_candidates_v2`, đúng hàm production, đã kiểm 0 câu ghi.

Kết quả: **69/90 miền-ngày = 76,7%** có `convergence_map` không rỗng. Và hôm nay MN hội tụ
`{21, 77, 29, 97}` — combo-super xuất ra đúng **`['97','21']`**.

Đo tiếp tỉ lệ trúng:

| nhóm | trúng | so nền 33,8% | z |
|---|---|---|---|
| **trong** tập hội tụ (+0,40) | 24/53 = **45,3%** | **+11,5pp** | **+1,77** |
| ngoài tập hội tụ | 17/85 = 20,0% | −13,8pp | −2,69 |

Rất thuyết phục. Số được bơm trúng nhiều hơn hẳn số không được bơm.

### Câu hỏi chặn, và câu trả lời

Agent gọi hàm **hôm nay** cho **ngày quá khứ**. Bộ luật có khoá theo thời điểm không?

`get_active_rules` (`rule_engine.py:262-266`) — **toàn bộ** mệnh đề `WHERE`:

```sql
WHERE target_region = ? AND target_weekday = ?
  AND (is_active = 1 OR activation_status = 'active')
  AND production_tier IN (…)
```

**Không một bộ lọc thời điểm nào.** Rồi:

```
MIN/MAX(mined_at) trên cả 105 luật = 2026-08-10T00:30:00 → 00:30:11
```

**Cả 105 luật được đào lúc 00:30 SÁNG NAY.** Nên toàn bộ 30 ngày agent chấm ngược đều **nằm
TRONG cửa sổ đào luật**. Luật được **chọn chính vì** nó khớp đúng những ngày đó.

Chữ ký khớp quá mức nằm ngay trong dữ liệu luật: `hr_4w = 1,0 · hr_8w = 1,0 · hr_12w = 1,0` —
trúng **100% suốt 12 tuần**.

### Và điều làm nó đáng ghi nhất

**`RM-18` đã mô tả đúng cái bẫy này rồi**, bằng số của chính kho: *«luật hơn nền
+7,5/+13,8/+20,7 điểm **trong** cửa sổ chọn nhưng **đúng bằng 0** ngoài cửa sổ»* (V11030).

Agent **đọc quy tắc đó nhiều lần trong ngày**, trích nó vào ba báo cáo — rồi vẫn tạo lại đúng
hiện vật đó và suýt báo như phát hiện mới.

Bốn lỗi tự bắt trong phiên trước đều là tín hiệu **âm hoặc trung tính**. Cái này là tín hiệu
**dương** — tức loại **mời người ta hành động**. Đó chính là hình dạng của sáu lần «hứa rồi rữa».

**Đã rút lại `+11,5pp`.** Muốn biết nhánh CHỐT GẤP có giá trị thật hay không thì chỉ có một
cách: thêm `mined_at <= target_date` vào truy vấn rồi đo ngoài cửa sổ — mà việc đó chạm đường
sinh số ⇒ **PLAN 21/08**.

---

## Chọn thước «xấu hơn» nhưng KHẢ THI

Dựng B1 (đo tiến anti-trap) phải chọn giữa hai thước. Agent tính **n-cần cho cả hai trước khi
chọn**:

| thước | n cần | tốc độ | ⇒ bao lâu |
|---|---|---|---|
| McNemar phép thay số — *đúng câu hỏi hơn* | 72 cặp lệch | 0,079/ngày | **30 tháng** |
| So tỉ lệ `FULL_SPENT` vs `FRESH` | 90 quan sát (có 51) | 0,31/ngày | **4,1 tháng** |

Chọn cái thứ hai. **Đặt hạn cho một thước cần 30 tháng là đúng thứ `RM-06` cấm** — nó tạo cảm
giác đang đo trong khi thực chất không bao giờ đóng được.

Thước McNemar vẫn ghi lại, nhưng **không đặt hạn**, và API trả về kèm dòng ghi rõ *«KHÔNG đặt
hạn — cần ~30 tháng»* để không ai đọc nhầm.

---

## Không đẻ cổng thứ hai

Sổ V11054 liệt kê **sáu chỗ trùng lặp**: thang trạng thái luật **4 bản**, cửa sổ tuần **3 cách**,
`_family()` **2 bản**. Đẻ thêm một cổng §52 nữa là làm dày đúng đống đó.

Nên mở rộng cổng có sẵn thành **sổ đăng ký `BO_DO`** — một cổng soi tất cả phép đo shadow. Thêm
phép mới về sau chỉ cần thêm một mục.

Lần chạy đầu **cổng chết** vì B1 không có cột `gan_bach_thu` mà K6 đi tìm. Sửa bằng cách cho
mỗi phép đo khai `cot_nhin_trom`, và khi `None` thì **in ra lý do không áp** thay vì bỏ qua im
lặng — *bỏ qua im lặng là cách cổng chết dần*.

---

## Vấp lặt vặt

- Thay chuỗi nhiều dòng vào tệp CRLF khớp **0 lần** — bẫy CRLF, **lần thứ tám**. Nay mọi lần
  sửa nhiều dòng đều dùng công cụ Edit thay vì `str.replace`.
- Dòng cron phải ghi qua **tệp**, không qua chuỗi SSH — bẫy `\&\&` đã sập ở V11055, lần này
  kiểm lại `grep -cF "\&"` = **0**.

---

## Trạng thái cuối phiên

PID `1286954` → **`1345720`** · health 200 · `/du-doan` 200 · admin 401 · 0 traceback ·
**hash 4 bảng khoá PRE = POST y hệt** · cron 135 → 136 dòng · cổng §52 **P4 6/6 · B1 6/6 · thử
chặn ĐẠT cho từng phép** trên chính VPS.

Canh 24h FU-360: **0 dòng, 0 chặn nhầm**.

TanPhatAI cần làm: xem mục cuối `REPORT_V11058.md` — năm việc, quan trọng nhất là ② ghi vào sổ
nhánh CHỐT GẤP `+0,40` mà mọi tài liệu đang thiếu, và ③ ghi nhận `+11,5pp` **đã bị rút lại** để
không ai trích lại con số đó.
