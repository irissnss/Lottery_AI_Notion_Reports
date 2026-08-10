# CONVERSATION CONTEXT — V11055 · 10/08/2026

## Owner nói gì (NGUYÊN VĂN)

> *«FU360, Và P4 luôn nha em cái này hiếm gặp ==> tiến hành»*

Sáu chữ, hai việc. *«cái này hiếm gặp»* — owner nói về **P4**, vì trong toàn bộ danh sách đề xuất
thì P4 là mục **0 đồng, làm được ngay, không phải chờ cửa sổ đo nào**.

Điều kiện đã ký từ hôm trước cho FU-360 (Q3, 09/08 13:58):

> *«Deploy trước 15:30 · thử chặn thật ngay sau deploy (khác run_source bị CHẶN, cùng run_source
> QUA) · canh 24h · sáng 11/08 mới đóng. Rollback ngay nếu thử chặn không đạt.»*

Thiết kế P4 do owner mô tả (09/08) — chính hai câu này định đoạt toàn bộ phép đo:

> *«gan chỉ là điểm hội tụ không nằm trong gan thì cũng đâu có ảnh hưởng, còn trước đây thì cứ đề
> +điểm nên bực ah em… đề xuất không có trong gan thì gan vô giá trị giống như anh đang tắt gan
> thôi.»*

> *«gan điều kiện soi với giải 8 và giải đặc biệt nha em, MB thì gan đang soi với giải đặc biệt…
> chú ý các giải đặt biệt là các giải ÍT BỘ SỐ chứ không phải là giải đặc biệt trong đài.»*

---

## Chuyện đáng kể nhất phiên này: bài thử của agent nói dối hai lần, ngược chiều nhau

**09:55** — chụp trạng thái: PID `1207732`, hash 4 bảng khoá, backup, đẩy `database.py`, restart.
PID `1207732` → `1284725`, health 200. Chạy thử chặn.

**09:58 — `2/5 TRƯỢT`.** Trong khi hôm qua chính bài thử đó ra `5/5`.

Owner đã ký sẵn: *«rollback ngay nếu thử chặn không đạt»*. **10:01 gỡ về** — không phân tích
trước, không cãi. PID `1285083`, health 200, `grep -c "CHAN CHEO LANE"` = 0.

Mổ ra thì lỗi ở **bài thử**, không ở bản vá:

Bài thử ghim cứng `date="2026-08-09"` và miền **MN**. Mốc freeze MN là **15:45**.

| chạy lúc | so với mốc 09/08 15:45 | freeze | kết quả |
|---|---|---|---|
| 09/08 ~14:00 (lúc ký 5/5) | **chưa tới** | ngủ | **5/5** — nhưng chưa chứng minh được gì |
| 10/08 09:58 | **qua 18 tiếng** | thức | **2/5** — vu oan bản vá đúng |

Và phép 3 — phép **quan trọng nhất** — bản vá đã **chặn ĐÚNG**: dòng `[CHAN CHEO LANE]` in ra
rành rành, số cũ giữ nguyên. Nhưng assert viết `rs == "rerun_post_mt"`, tức **giả định phép 2 đã
ghi đè thành công**. Phép 2 bị freeze chặn ⇒ phép 3 trượt theo.

**Ba dòng "trượt" đều in `[FREEZE_LATE_*]`. Không dòng nào in `[CHAN CHEO LANE]`.** Đọc nhãn thì
thấy ngay; đọc con số `2/5` thì suýt kết luận ngược.

Sửa ba thứ: ngày thử là **ngày tương lai +30** (freeze không bao giờ xen vào) · mỗi phép **tự đọc
trạng thái TRƯỚC của chính nó** · **hứng `stdout`** để bắt đích danh cơ chế nào ra tay.

Và thêm thứ đáng lẽ phải có từ đầu: **ĐỐI CHỨNG**. Chạy cùng bài thử trên bản **chưa vá** — phải
**LỌT**. Kết quả: bản đã vá chặn 2 phép chéo lane, bản chưa vá lọt đúng 2 phép đó. **Giờ cổng mới
phân biệt được hai bản.**

---

## Cổng P4 bắt được chính nó mù — nhờ chạy phép thử chặn

Viết xong `_v11055_kiem_p4.py`, chạy `--thu-chan` (giả lập vi phạm rồi khôi phục). Nó lộ ra **hai
lỗ trong chính nó**:

**Lỗ 1 — K3 báo "endpoint có câu ghi".** Mẫu tìm `UPDATE` khớp trúng **`d.update({`** — dict
method của Python. Đúng `A58_VIOLATION_RAW_COUNT`: đếm chuỗi mà không đọc ngữ cảnh.

**Lỗ 2 — K4 báo xanh GIẢ.** Cửa sổ "lấy 4000 ký tự sau `setInterval` cho chắc" **tràn qua** khối
`setInterval` (thật ra chỉ dài ~1.200 ký tự) và nuốt luôn **định nghĩa hàm** `async function
loadGanHoiTu()` nằm phía dưới. Cổng nhầm **định nghĩa** thành **đăng ký làm mới** ⇒ **luôn báo
xanh**, kể cả khi đã gỡ hẳn đăng ký.

Không chạy `--thu-chan` thì lỗ 2 sẽ sống mãi và cổng sẽ xanh vĩnh viễn. Đây đúng là thứ RM-15
sinh ra để bắt — *«cổng không qua thử coi như KHÔNG TỒN TẠI»*.

---

## Điều owner mô tả mà agent không tự nghĩ ra, và nó dẫn tới phát hiện nặng nhất

Owner nói gan là **bộ XÁC NHẬN**, không phải **bộ SINH**. Đo đúng thiết kế đó thì lộ ra:

**`combo_super._apply_hot_cold_post_filter` đang sống trên đường chọn số** — 4 điểm gọi, y hệt
trên VPS, **không có công tắc tắt**:

```
HOT ×1,5 · WARM ×1,2 · COOL ×0,7 · COLD ×0,6 (gan≤8) hoặc ×0,3 (gan>8)   → rồi SẮP XẾP LẠI
```

Số **gan cao** đang bị **dìm tới ×0,3** trước khi vào top-10 — **ngược hẳn** thiết kế owner mô tả.

Và nó lật ngược cách đọc chính con số vừa đo: phép đo P4 soi pool top-10, nhưng pool đó **đã bị
trừng phạt vì có gan**. Đo giá trị của gan trên một pool đã phạt gan là **luẩn quẩn**. Con số
`−0,94pp` phải đọc kèm câu này, không được đọc trần.

Đây cũng là **§60 «bỏ nửa chừng» theo chiều ngược**: V11001 gỡ gan/nóng/lạnh khỏi **prompt**,
nhưng **cơ chế nhân điểm trong mã vẫn nguyên**.

**Không sửa** — `QD-041` khoá đường chọn số tới 21/08. Ghi vào sổ chờ owner.

---

## Về con số P4 — nói thẳng nó nghĩa là gì

Gộp 3 miền phân tầng: **−0,94pp · CI95 [−5,5 … +3,6] · MDE 4,62pp**.

`z < 1,96` **một mình** không phân biệt được hai tình huống khác hẳn nhau: (a) đo quá yếu nên
không biết gì, (b) đo đủ mạnh và **loại trừ được** hiệu ứng đáng kể. Chỉ **khoảng tin cậy** mới
tách được. Ở đây CI đã **loại trừ mức +5pp** ⇒ đây là **câu trả lời thật**, không phải «thiếu dữ
liệu».

Đo **từng miền** thì vô vọng: `n` cần cho +5pp là **1.513–2.199 ngày/nhóm** = **4–6 năm**. Đây
cũng là lời giải thích cho **sáu lần «hứa rồi rữa»** ghi trong CLAUDE.md — các phép đo đó chưa
bao giờ đủ sức mạnh để thấy thứ chúng đi tìm.

---

## Vấp lặt vặt đã ghi lại để lần sau không mất thì giờ

- Tệp backup tên `database.py.pre_v11052` — **đuôi không phải `.py`** ⇒ `spec_from_file_location`
  trả `None` ⇒ đối chứng chết. Phải chép sang tệp `.py` tạm rồi mới nạp.
- Ghi cron qua chuỗi SSH làm `\&\&` lọt vào crontab **nguyên văn**. Phải khôi phục từ backup rồi
  ghi lại **qua tệp**.
- `str.replace` với `\n` khớp **0 lần** trên `main.py` — kho dùng **CRLF**. Bẫy này sập **lần thứ
  sáu** trong hai ngày.
- `kiem_code` trong sổ quyết định: `chay_lenh` là **list argv**, không phải một chuỗi có dấu
  cách; và dấu hiệu `file_chua` phải **đúng nguyên văn có dấu tiếng Việt**.

---

## Trạng thái cuối phiên

PID `1286954` · health 200 · `/du-doan` 200 · admin 401 · 0 dòng lỗi ·
**hash 4 bảng khoá PRE = POST y hệt suốt cả phiên** (12.159 · 490 · 15.247 · 11.982) ·
0 quyết định trôi · cron 134 → 135 dòng · bảng shadow 489 dòng.

**Còn treo có hạn:** FU-360 đóng **sáng 11/08** sau 24h canh.
