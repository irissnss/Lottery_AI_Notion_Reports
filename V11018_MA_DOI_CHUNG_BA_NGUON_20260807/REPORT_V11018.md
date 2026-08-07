# REPORT V11018 — M-A: ĐỐI CHỨNG BA NGUỒN ML × LUẬT × BỘ LỌC (FU-317)

> **Ngày:** 2026-08-07 · **Đã deploy** · PID `981799 → 982337` · 4 bảng khoá Y HỆT
> **Chuỗi §52 đủ:** bảng shadow · API admin · panel `/monitoring` · cron · tài liệu · báo cáo

---

## 1. Tóm tắt

Owner hỏi ML có đối chứng với rules và bộ lọc không. Đo V11015: **7/7 tệp ML tham chiếu
`mined_rule` = 0** — **không có**. Nay dựng tầng đó ở dạng shadow.

**Kết quả đầu tiên trả lời NGƯỢC với trực giác:** đuôi được **ba nguồn** cùng chỉ trúng
**33,33%**, thấp hơn đuôi chỉ **một nguồn** (**43,60%**). `z = −1,01`.

Đây là **lần thứ hai** cơ chế *"càng nhiều nguồn cùng chỉ càng đáng tin"* đi ngược — §5g từng
đo `z = −2,54`.

## 2. Owner yêu cầu gì (nguyên văn)

> *"khẩn trương đi em, sắp tới giờ block rồi rm"*

Trước đó owner đã duyệt hướng đi (*"ok tiếp đi em"*) cho đề xuất: *"em dựng phép đo bầy đàn và
bắt đầu M-A — cả hai không cần anh duyệt"*.

Việc gốc, owner nêu 07/08:

> *"Với ML ngoài xác xuất thống kê thuần, anh quan tâm đến **đối chứng với rules, bộ lọc** để so
> sánh đối chiếu để output **số chính và nhẹ hơn là số phụ**."*

## 3. Đào bới / phát hiện

### 3.1 Kết quả — trả lời thẳng câu owner hỏi · `VERIFIED_TEST`

**Hỏi:** đuôi được cả ba nguồn cùng chỉ có trúng cao hơn đuôi chỉ một nguồn không?

| số nguồn cùng chỉ | n | trúng | tỉ lệ |
|---|---|---|---|
| **1 nguồn** | 2.658 | 1.159 | **43,60%** |
| **2 nguồn** | 516 | 245 | **47,48%** |
| **3 nguồn** | **24** | 8 | **33,33%** |

**z (3 vs 1) = −1,01** · ngưỡng cần **|z| ≥ 1,96**

⇒ **KHÔNG CÓ LỢI THẾ.** Chưa vượt ngưỡng nên chưa kết luận được là *tệ hơn thật*, nhưng **chắc
chắn không có căn cứ nào để tách «số chính» / «số phụ» theo số nguồn**.

### 3.2 Cỡ mẫu nhóm 3 nguồn chỉ có 24 — và điều đó tự nó là câu trả lời

24 lượt là mỏng, nói thẳng. Nhưng nó mỏng **vì ba nguồn hiếm khi cùng chỉ một đuôi**: trong
3.231 dòng chỉ có 24 lần cả ba cùng trỏ. Nghĩa là cơ chế *"đồng thuận ba nguồn"* **hầu như không
kích hoạt** — kể cả nếu nó tốt, nó cũng gần như không dùng được.

### 3.3 Lần THỨ HAI cơ chế «nhiều nguồn» đi ngược

| lần | cơ chế | kết quả |
|---|---|---|
| V11012 | §5g — cộng điểm theo số nguồn trong prompt | ô 3 nguồn **z = −2,54**, ô **tệ nhất** · đã gỡ ở V11014 |
| **V11018** | đối chứng ML × luật × bộ lọc | 3 nguồn **33,3%** vs 1 nguồn **43,6%** · **z = −1,01** |

Hai phép đo độc lập, hai bộ nguồn khác nhau, **cùng một hướng**.

### 3.4 Ba nguồn lấy từ đâu · `VERIFIED_CODE`

| nguồn | lấy từ | phủ sóng |
|---|---|---|
| `ML` | `predictions` với `phase_type` ∈ XGBOOST · LSTM · META · RF · SMART_ML · SMART_ENSEMBLE | 279 dòng |
| `LUAT` | `mined_rules` active của bucket (miền, thứ), tính **as-of** — không nhìn tương lai | 490 dòng |
| `LOC` | `filter_2_so_cuoi.get_filter_data_with_cascade()` | 3.026 dòng |

## 4. Hướng xử lý và vì sao chọn

**Đo shadow trước, không đụng official.** Owner hỏi *"có đối chứng không"* — câu trả lời đúng
không phải là *"em gắn đối chứng vào rồi"* mà là *"em đo xem đối chứng có ích không đã"*.

**Mặc định là KHÔNG có lợi thế**, viết thẳng vào mã nguồn và panel, cho tới khi `|z| ≥ 1,96` nói
ngược lại. Vì §5g đã một lần đi từ trực giác thẳng vào prompt production mà không đo.

**Ngưỡng chốt trước:** `z ≥ +1,96` ⇒ mới bàn đưa vào cách chọn số · `z ≤ −1,96` ⇒ ghi vào SSOT
là **cấm dựng lại** cơ chế cộng điểm theo số nguồn dưới bất kỳ tên nào.

## 5. Đã làm gì

| bề mặt | nội dung |
|---|---|
| **Bảng shadow** | `ma_doi_chung_shadow` — `output_eligible=0 · diagnostic_only=1 · owner_approved=0 · shadow_only=1` · `UNIQUE(date, region, tail)` |
| **Module** | `web/backend/_v11018_ma_doi_chung.py` — `compute()` ghi · `view()` **CHỈ ĐỌC** |
| **API admin** | `/api/admin/ma-doi-chung` — `require_admin` + `Cache-Control: no-store` |
| **Panel** | `/monitoring` › `sectionMaDoiChung`, đăng ký **CẢ HAI** chỗ (§52B) |
| **Cron** | `19:25` mỗi ngày · crontab **82 → 83** |
| **§52.7** | `governance_seq` **394 → 395** |

## 6. Cổng kiểm

| phép | kết quả |
|---|---|
| md5 ba tệp local = VPS | ✓ cả ba |
| `py_compile` trên VPS (venv) | ✓ OK |
| `compute()` trên VPS | ✓ **3.250 dòng** |
| cờ an toàn | ✓ **đủ 4** |
| PID | `981799 → 982337` ✓ ĐÃ ĐỔI |
| `/api/health` | **200** |
| endpoint admin, chưa đăng nhập | **401** ✓ |
| 4 bảng khoá | ✓ **Y HỆT** — `11916\|25692` · `481\|661` · `15226\|15330` · `11739\|11739` |
| J5 mốc tải | ✓ khớp sổ thật |

## 7. Vướng vấp

**Một nguồn CHẾT mà bảng vẫn ra số.** Bản đầu dò hàm bộ lọc bằng **tên đoán** —
`run_filter` · `filter_2_so_cuoi` · `run` · `compute`. **Không hàm nào tồn tại.** Nguồn `LOC`
ra **0 dòng**, và bảng **vẫn chạy trơn tru**, vẫn ra bảng tỉ lệ, vẫn có kết luận — chỉ là kết
luận của **hai nguồn đội lốt ba**.

Đúng lỗi V11015 đã mắc: đoán tên tệp `ml_train.py` (không tồn tại). Lần đó đoán tên **tệp**, lần
này đoán tên **hàm**. Sửa: đọc tên thật từ mã nguồn — `get_filter_data_with_cascade`. Sau khi
sửa: **743 → 3.250 dòng**.

**Kiểu hỏng này nguy hiểm nhất** vì không có gì báo lỗi — chỉ có một con số nhỏ hơn bình thường
mà không ai biết bình thường là bao nhiêu. Mở **FU-327**: mọi bảng gộp nhiều nguồn phải có cổng
*"nguồn nào đóng góp 0 dòng thì kết luận không được phát ra"*.

## 8. Gỡ về

```bash
for f in _v11018_ma_doi_chung.py main.py monitoring.html; do
  cp /root/Lottery_AI_Test/backups/$f.v11018_pre <đúng đường dẫn>
done && systemctl restart lottery
crontab -l | grep -v _v11018_ma_doi_chung | crontab -
```

Bảng là **shadow thuần** — `DROP TABLE ma_doi_chung_shadow` không ảnh hưởng gì.

## 9. Theo dõi tiếp

| Mã | Nội dung | Trạng thái | Hạn |
|---|---|---|---|
| **FU-317** | M-A đối chứng ba nguồn | **`DEPLOYED_PENDING_LIVE_VERIFY`** (xong sớm 3 ngày) | 10/08 |
| **FU-327** | Cổng bắt **NGUỒN CHẾT** trong các bảng gộp nguồn | `MEASURED_ROOT_CAUSE` | 14/08 |
| **FU-318** | M-C — học lại theo TRÔI | chưa làm | 11/08 |
| **FU-319/320** | M-B · M-D | **chờ owner** | 14/08 |

**Ngưỡng hành động FU-317:** đo tiếp 14 ngày. `z ≥ +1,96` ⇒ mới bàn đưa vào cách chọn số ·
`z ≤ −1,96` ⇒ ghi SSOT **cấm dựng lại** cơ chế cộng điểm theo số nguồn.

**Điều owner cần biết ngay:** câu hỏi *"đối chứng ba nguồn để tách số chính/số phụ"* — số hiện
tại nói **đừng làm**. Không phải vì đo chưa đủ, mà vì hướng đi **giống hệt ca §5g** đã phải gỡ.
