# REPORT V11017 — ĐO BẦY ĐÀN: phép đo CƠ CHẾ của V11016, biết trong 1 ngày

> **Ngày:** 2026-08-07 · **Đã deploy** · PID `981452 → 981799` · 4 bảng khoá Y HỆT
> **Chuỗi §52 đủ:** bảng shadow · API admin · panel `/monitoring` · cron · tài liệu · báo cáo

---

## 1. Tóm tắt

V11016 gỡ rổ số dọn sẵn để chống bầy đàn. Độ trúng phải đợi **21/08** — nhưng câu *"model có
còn chốt trùng nhau không"* thì **sáng mai biết**. Dựng phép đo đó.

**Nền: 64 lượt miền-ngày, phân tán trung bình 0,474 ± 0,087.** Ngưỡng chốt **trước** khi đo.

Và **bắt được một lỗi nhiễm bẩn ngay sau khi deploy**: mốc phân loại lấy theo **NGÀY** làm ba
lượt chạy **prompt cũ** bị gắn nhãn `SAU_V11016` với 0,56–0,57 — **nhìn như thắng lớn**. Sửa
thành **mốc GIỜ**.

## 2. Owner yêu cầu gì (nguyên văn)

> *"ok tiếp đi em."*

Đồng ý với đề xuất agent trình ngay trước đó: *"em dựng phép đo bầy đàn tối nay và bắt đầu M-A —
cả hai không cần anh duyệt"*.

Việc gốc, owner nêu 07/08:

> *"đừng output theo số gò như thế dẫn đến bầy đàn là đúng rồi, lùa vào 1 bộ số định sẵn trong
> ngày để model quyết định xong thấy bầy đàn."*

Và ràng buộc owner đặt từ 06/08 (`FU-287`):

> *"1 tháng mới biết rồi fix rồi đợi 1 tháng nữa thì quá tệ."*

## 3. Đào bới / phát hiện

### 3.1 Thước và vì sao phải lọc · `VERIFIED_TEST`

`tỉ lệ phân tán = số SỐ CHÍNH khác nhau / số model chốt`, mỗi (ngày, miền).

**Không lọc là ra số sai.** Đếm cả `run_source='shadow_auto_eval'` thì mỗi miền có **27 model**
và phân tán rơi xuống 0,26–0,56. Chỉ đường official thì là **15–16 model**, phân tán 0,31–0,62.
Hai bức tranh khác hẳn nhau — và chỉ bức thứ hai là thứ ra `/du-doan`.

### 3.2 Nền — 64 lượt, 17/07 → 07/08 · `VERIFIED_TEST`

**Trung bình 0,474 ± 0,087.** Ổn định suốt 21 ngày. Vài ca nặng nhất:

| ngày | miền | model | số khác nhau | phân tán | số đông nhất |
|---|---|---|---|---|---|
| 02/08 | MB | 16 | **5** | **0,31** | 73 × 6 model |
| 30/07 | MB | 15 | **5** | **0,33** | 75 × 4 |
| 30/07 | MN | 15 | **5** | **0,33** | 86 × **7 model** |
| 05/08 | MT | 16 | 7 | 0,44 | 93 × **8 model** |

**16 model ra 5 số** — và có hôm **8/16 model chốt đúng một số**. Đó là bầy đàn owner nói, đo
được bằng số.

### 3.3 LỖI NHIỄM BẨN — bắt được ngay sau khi deploy · `VERIFIED_TEST`

Bản đầu lấy mốc theo **NGÀY** (`date(2026,8,7)`). Deploy xong đọc lại thì:

| ngày | miền | nhãn | phân tán |
|---|---|---|---|
| 07/08 | MB | `SAU_V11016` | **0,5714** |
| 07/08 | MN | `SAU_V11016` | **0,5625** |
| 07/08 | MT | `SAU_V11016` | **0,5714** |

So nền 0,474 thì đây là **thắng lớn**, vượt cả ngưỡng 0,50. Nhưng:

```
predictions ngày 07/08 tạo lúc : 05:00:05 → 05:20:44
gpt_analyzer.py đổi trên VPS   : 13:35:48
```

**Ba lượt đó chạy prompt CŨ.** Sáng mai đọc bảng là báo cáo nhầm *"lời kể có tác dụng"* trên
chính dữ liệu của bản cũ — và đó sẽ là một kết luận sai được đóng dấu bằng một phép đo.

## 4. Hướng xử lý và vì sao chọn

**Mốc phải là MỐC GIỜ**, và phân loại theo `created_at` của **từng bản ghi**, không theo ngày
của cả nhóm.

**Lượt HỖN HỢP phải bị LOẠI, không được gộp.** Một (ngày, miền) có cả bản ghi trước lẫn sau mốc
thì con số của nó là trung bình của **hai prompt khác nhau** — vô nghĩa. Nhãn `HON_HOP`, loại
khỏi cả hai trung bình, và **đếm riêng để nói rõ đã bỏ bao nhiêu**.

**Không đọc được giờ ⇒ xếp về NỀN.** Thà xếp nhầm về nền còn hơn tự khen.

**Ngưỡng chốt TRƯỚC khi có dữ liệu.** Viết thẳng vào mã nguồn và vào panel, để sau này không ai
(kể cả agent) bẻ ngưỡng cho vừa kết quả.

## 5. Đã làm gì

| bề mặt | nội dung |
|---|---|
| **Bảng shadow** | `bay_dan_daily_shadow` — `output_eligible=0 · diagnostic_only=1 · owner_approved=0 · shadow_only=1` · `UNIQUE(date, region)` |
| **Module** | `web/backend/_v11017_bay_dan_shadow.py` — `compute()` ghi · `view()` **CHỈ ĐỌC** (đúng bài học *"đọc bản đã lưu tưởng là tính lại"*) |
| **API admin** | `/api/admin/bay-dan-shadow` — `require_admin` + `Cache-Control: no-store` |
| **Panel** | `/monitoring` › `sectionBayDan`, đăng ký ở **CẢ HAI** chỗ — `loadAllSections()` **và** `setInterval` 60s (§52B) |
| **Cron** | `19:05` mỗi ngày, sau khi MB chốt 17:58 · crontab **81 → 82** dòng |
| **§52.7** | `AUTOMATION_STATE.json` — `governance_seq` **393 → 394** |

### Ngưỡng đã chốt trước khi đo

| kết luận | điều kiện |
|---|---|
| **CÓ TÁC DỤNG** | trung bình **≥ 0,50** *và* hơn nền **≥ 0,05** |
| **KHÔNG TÁC DỤNG** | trung bình **≤ 0,35** ⇒ lời kể không cắt được bầy đàn, phép đo 21/08 vô nghĩa |
| **CHƯA RÕ** | giữa hai ngưỡng |
| **CHƯA ĐỦ** | dưới **9 lượt** (3 ngày × 3 miền) |

### Cũng sửa một lỗi trong chính script deploy

`cp` → **`cp -n`** cho bản sao lưu. Chạy deploy lần hai mà ghi đè là bản *"pre"* thành bản **đã
deploy** — mất luôn đường gỡ về. Lỗi này chỉ lộ ra vì phải deploy hai lần trong cùng phiên.

## 6. Cổng kiểm

| phép | kết quả |
|---|---|
| md5 ba tệp local = VPS | ✓ cả ba |
| `py_compile` trên VPS (venv) | ✓ OK |
| `compute()` trên VPS | ✓ ghi **66 dòng** (17/07 → 07/08) |
| `view()` cờ an toàn | ✓ **đủ 4** — `output_eligible=0 · diagnostic_only=1 · owner_approved=0 · shadow_only=1` |
| nền sau khi sửa mốc | **n=64 · 0,474** (trước khi sửa: n=63, và 1 lượt bị gắn nhãn sai) |
| `sau_v11016` sau khi sửa mốc | **n=0** — đúng, vì chưa có lượt nào chạy sau 13:36 |
| PID | `981452 → 981799` ✓ ĐÃ ĐỔI |
| `/api/health` | **200** |
| endpoint admin, chưa đăng nhập | **401** ✓ đúng |
| 4 bảng khoá | ✓ **Y HỆT** — `11916\|25692` · `481\|661` · `15226\|15330` · `11739\|11739` |
| cron | 1 dòng · tổng crontab 82 |
| cổng chặn cắt cụt | ✓ sạch |
| J5 mốc tải | ✓ khớp sổ thật |

## 7. Vướng vấp

**Suýt tạo ra một phép đo tự khen.** Nếu không đọc lại dữ liệu ngay sau deploy thì sáng mai bảng
sẽ hiển thị `SAU_V11016 = 0,57` và agent sẽ báo cáo *"lời kể cắt được bầy đàn"* — trên ba lượt
chạy **prompt cũ**. Đây đúng bẫy CLAUDE.md đã ghi: *"cẩn thận cột thời gian"*, và lệch **8 tiếng**
là đủ để kết luận ngược.

**Đáng lo hơn cái lỗi:** một phép đo dựng ra để chống tự huyễn hoặc lại suýt trở thành công cụ
tự huyễn hoặc. Cái cứu không phải là cẩn thận — mà là **đọc lại dữ liệu thật ngay sau khi
deploy**, thay vì tin vào việc mình vừa viết.

**Hệ quả về lịch:** lượt đo `SAU_V11016` **sạch** đầu tiên là **08/08**, không phải 07/08. Ba
lượt 07/08 nếu tối nay có thêm bản ghi sẽ thành `HON_HOP` và **bị loại** — đúng như thiết kế.

## 8. Gỡ về

```bash
# VPS — ba tệp
for f in _v11017_bay_dan_shadow.py main.py monitoring.html; do
  cp /root/Lottery_AI_Test/backups/$f.v11017_pre <đúng đường dẫn>
done && systemctl restart lottery
# cron
crontab -l | grep -v _v11017_bay_dan_shadow | crontab -
```

Bảng `bay_dan_daily_shadow` là **shadow thuần** — bỏ đi không ảnh hưởng gì; muốn xoá hẳn thì
`DROP TABLE bay_dan_daily_shadow`.

## 9. Theo dõi tiếp

| Mã | Nội dung | Trạng thái | Hạn |
|---|---|---|---|
| **FU-287** | Phép đo CƠ CHẾ cho V11016 | **`DEPLOYED_PENDING_LIVE_VERIFY`** | 07/08 |
| **FU-325** | Đọc lượt đo bầy đàn **SẠCH** đầu tiên | `WAIT_LIVE` | **08/08** |
| **FU-326** | Rà các phép đo khác có dùng **mốc NGÀY** thay vì **mốc GIỜ** không | `MEASURED_ROOT_CAUSE` | 14/08 |
| **FU-284** | Phép đo KẾT QUẢ, gộp ba biến | `WAIT_LIVE` | 21/08 |

**FU-326 quan trọng hơn vẻ ngoài:** bất kỳ phép đo trước/sau nào của một thay đổi **deploy giữa
ngày** đều dính đúng lỗi vừa bắt. Phép đo nào chia trước/sau theo NGÀY trong hoàn cảnh đó thì
**kết luận của nó không dùng được**, phải tính lại.

**Ngưỡng hành động FU-325:** đọc panel sáng 08/08. `≥0,50 và hơn nền ≥0,05` ⇒ giữ ·
`≤0,35` sau 3 ngày ⇒ lời kể **không** cắt được bầy đàn ⇒ gỡ về `v11016_pre` hoặc đổi hướng.
