# CONVERSATION CONTEXT — V11107 + V11108 · 23/08/2026 (tối)

## Owner nói gì (NGUYÊN VĂN)

> *«PROMPT TỔNG LỰC LẦN 30 — 24/08: AUDIT CỰC GẮT»*

Sáu chất vấn: ① nghi dữ liệu kết quả **bị ghi đè/trôi** *(«MN không có bạch thủ 10»)* ② đòi
**đo model AI NGAY** ③ **so chéo regime shadow vs official là SAI** ④ lượt AI rỗng phải truy tới
nơi ⑤ **ML fix TỪ GỐC TỚI NGỌN** ⑥ *«đo hoài không ra»* — mọi phép đo phải có **ngày quyết
định** và **verdict**.

---

## Chỗ đầu tiên phải nói lại: **ngày trong lệnh chưa tới**

Prompt đề *«24/08»*. Giờ VN trên VPS lúc bắt đầu phiên: **`2026-08-23 20:46`**.

Nên `GĐ-6` mục đầu — *«kiểm lượt 05:00 ngày 24/08 có đóng dấu prompt mới không, rồi nâng lên
`RUNTIME_PROVEN`»* — **không kiểm được**, và `RM-12` cấm tự nâng tầng. Em ghi thẳng ngay câu đầu
thay vì tìm cách nói khác.

---

## Điều lớn nhất phiên này, và nó đến từ **làn phản biện**, không phải làn đo

Em tung **bảy** tác nhân: **năm** làn đo, và **hai** làn có đúng một việc — **cố bác bỏ năm làn
kia**. Hai làn đó bác **12 kết luận**.

**Và chính chúng tìm ra thứ em truy suốt hai phiên mà chưa ra:** lớp ghi đè số công bố.

```
main.py:10059-10072  →  _v10640_official_perslice_override.get_override_bt()
OVERRIDE_CONFIG      →  MN enabled=True (chooser="specialist") · MT False · MB False
```

Nó **không hề bí ẩn**. `V10917` ngày 01/08 **owner đã ký duyệt**: tắt MT + MB, giữ MN. Có bảng
theo dõi riêng (`_v10918_override_watch`). Có ngày rà (**31/08**). Có ngưỡng viết sẵn trong mã.

**Em đã tìm sai chỗ suốt hai phiên** — soi `bundle_version`, id bị đốt, log `t10_chot`. Cả ba
đều **không thể** thấy lớp này, vì nó đổi số **TRƯỚC** khi ghi vào DB. Log `t10_chot` ghi bản
**đã ghi đè**, nên nó khớp với DB là **đương nhiên** — và em đọc sự khớp đó thành *«không có ghi
đè»*.

---

## Bản vá của chính em bị lật, và đây là phần em phải nói kỹ nhất

Phiên này em vá `FU-427`, viết bài thử chặn, **ĐẠT 9/9**, commit `8ca990d`, **đẩy lên remote**.

Rồi ~30 phút sau, khi tra `QD-045` cho **một việc khác**, em thấy dòng này:

```
docs/CURRENT_TRUTH_SSOT.md:818
  NGƯỠNG ĐĂNG KÝ TRƯỚC: ≥96 cặp bất đồng VÀ |z| ≥ 1,96
```

**«Cặp BẤT ĐỒNG».** Không phải `b+c`.

Bản vá của em đổi con số đặt cạnh sàn `96` từ **bất đồng (122)** sang **`b+c` (46)** — tức lane
từ **đạt sàn** thành **thiếu 50 cặp**. Đó là **tự đổi ngưỡng sau khi thấy số**, đúng câu owner
khoá ở lệnh lần 29: *«CẤM tự ý đổi ngưỡng sau khi thấy số»*.

Ngưỡng ấy ghi ở **ba nơi độc lập**, viết **11/08** — trước mọi kết quả. Và **20/08** chính dự án
đọc đúng như vậy: *«Sàn mẫu ĐẠT (100 ≥ 96) nhưng `|z| = 0,480`»*.

**Điều đáng sợ nhất không phải em vá sai. Là bài thử chặn ĐẠT 9/9 trên chính cái ngưỡng em bịa
ra.**

Bài thử chỉ chứng minh hàm làm **đúng điều nó được viết ra để làm**. Nó **không** kiểm được điều
đó có phải điều **ĐÃ ĐĂNG KÝ** hay không. Chín dấu ✓ xanh trên một ngưỡng sai vẫn là chín dấu
xanh — và em suýt mang chín dấu xanh đó đi báo cáo.

Nay bài thử có **phép [10]**: đối chiếu ba con số ngưỡng **trong mã** với bản đăng ký
`(96 · 1,96 · 14)`. **13/13.**

**Verdict lane không đổi** — cả hai bản đều *«chưa được phép kết luận»*. Nhưng **lý do khác
hẳn**, và nếu số nghiêng chiều khác thì cùng thao tác đó là **dời cột gôn**.

Đã rút lại **đủ bốn phần** (`PRJ-RETRACTION-001`) ngay trong `CHANGELOG` `V11107` — chỗ đã công
bố — chứ không sửa lặng lẽ ở bản mới.

---

## Ba lần trong một phiên, cùng một kiểu: **con số phồng vì chưa nhìn đủ**

| # | em định báo | thật ra | vì sao |
|---|---|---|---|
| 1 | *«10 mệnh lệnh mồ côi»* | **1** | cổng chỉ dump **context pack**, bỏ thân prompt (**4 báo giả**) + nuốt cả giá trị mẫu trong khung JSON đầu ra (`"CHOT_HA"`, `"CAO / TRUNG BÌNH / THẤP"`) |
| 2 | *«27 mục thiếu hạn»* | **19** | đọc *«hạn giữ»* thành thiếu hạn; và `LX`/`STANDING_RULE` **không hạn là đúng thiết kế** |
| 3 | *«327 mục FU»* | **302 mã** | đếm **khối** thay vì gộp theo **số hiệu** — `FU-423` một mình có **ba** khối |

Cả ba đều bị chính em bắt trước khi báo. Nhưng cả ba đều là **cùng một thói quen**: chạy một
phép đếm, thấy con số kêu, tin nó.

---

## Điều em KHÔNG làm, dù đã có số

**Không công bố bảng xếp hạng 15 model.** Làn đo trình ra bảng đầy đủ, có `b/c/n/điểm/z`, có
`n_cần`, có *«ngày sớm nhất THĂNG»*. Hai làn phản biện bác **ba chỗ**, mỗi chỗ đủ làm hỏng
kết luận:

| chỗ | bản đo | phản biện |
|---|---|---|
| hệ số cụm | `DEFF = 1,045` | dòng **gộp 15 model** phải dùng cụm **NGÀY** ⇒ `6,88`/`7,09`. **`z: 1,72 → 0,65`** |
| `n` cần | `z = 1,96` | tự mâu thuẫn ngưỡng chính nó đăng ký (Bonferroni `z=2,938`) + sức mạnh 80% ⇒ phồng **3,72×**. *«THĂNG 11/12/2026»* → **2027–2028** |
| cửa sổ | một số gộp | tách theo-phiếu-bầu vs bị-ghi-đè: `+0,0055 (p=0,866)` vs `+0,1879 (p=0,00076)` |

Và cơ chế đằng sau đáng nhớ: **0/384** ô ngày-miền có đồng thời `b>0` và `c>0` — **15 model
trong một ngày-miền LUÔN CÙNG DẤU**.

Nếu em công bố bảng đó, owner sẽ có một bảng xếp hạng trông rất chuyên nghiệp với `z` phồng
**2,6 lần** và lịch THĂNG sai **hơn một năm**.

---

## Một điều luật của chính dự án ghi công thức sai

`RM-18` (trong `CLAUDE.md`, cả sáu mặt) viết nền cho bộ `k` đuôi là `1 − (1−b)^k`.

Đó là công thức **CÓ HOÀN LẠI**. `k` số dự đoán là **phân biệt** ⇒ nền đúng là
`1 − C(100−D,k)/C(100,k)`.

Lệch nhỏ (0,18–0,25 điểm ở `k=2`) nhưng **SAI CHIỀU**: luật **ước lượng THẤP** nền ⇒ **luôn làm
model trông tốt hơn thực tế**. Không làn nào bắt được **vì chính điều luật ghi sai** — mọi làn
đều trích nó ra để tự bảo vệ.

---

## Trả lời nghi ngờ của owner cho đúng

Owner nghi *«dữ liệu kết quả bị ghi đè/trôi»*, nêu đích danh *«MN không có bạch thủ 10»*.

**Ở tầng DB, nghi ngờ bị bác bỏ, và em kiểm bằng đuôi ra thật:**
MN 22/08 `bach_thu='10'`, **WIN**, `OFFICIAL` — đuôi `10` có thật (**Hậu Giang, giải tám**). Là
bundle **duy nhất** có `bach_thu='10'` trong 30 ngày. `lottery_results` **0 id bị đốt**. Tự kiểm
**9/9** ca khớp.

**Nhưng có một lời giải thích thứ ba, và nó đo được:**

> **Số công bố cho MN khác số các model bầu ra ở 8/23 ngày = 34,8% kể từ 01/08.**

Nếu owner đang so *«số model chọn»* với *«số hiện trên `/du-doan`»* thì **hai số đó lệch nhau
thật, một phần ba số ngày** — đúng thiết kế, do lớp `V10640`.

Và **ca gần nhất chính là hôm nay**: 23/08 MN, phiếu bầu `46` **TRÚNG**, số công bố `73`
**TRƯỢT**.

Làn đo ban đầu đóng hướng này bằng một suy đoán — *«chắc owner nhớ nhầm ngày, hoặc lỗi UI»*.
Làn phản biện bác đúng chỗ đó: **có lớp ghi đè, có mã, có cờ, có bảng theo dõi, và đang bật** —
không cần giả định owner nhớ nhầm.

---

## Điều em KHÔNG hứa

Gỡ hai mệnh lệnh mồ côi **không phải** để tăng độ trúng. Lý do gỡ là prompt **tự mâu thuẫn**.

ML miền MB `AUC < 0,50` **không có nghĩa là tắt nó ngay**. Ngưỡng đã đăng ký: **ba lần học liên
tiếp** (30/08 · 06/09 · 13/09), và khi đó là **BỎ CỜ**, không phải **DỪNG HẲN** — model vẫn chạy,
vẫn được đo, pool ML giữ nguyên 4.

Lớp ghi đè MN `cứu 4 / phá 1` **không có nghĩa là nó đang thắng**. `n=5`, `p=0,375`. Và chính chú
thích trong mã đã ghi từ đầu: *«giữ vì là phương án đo được tốt nhất, **không phải vì đã chứng
minh**»*.

---

## Điều còn treo — ưu tiên cao nhất cho phiên sau

**Bề mặt HIỂN THỊ.** Toàn bộ phiên này đo ở tầng **DB**. Chưa ai gọi `/du-doan` cho MN 22/08 để
xem **UI render số nào**. Đó là khoảng trống cuối cùng giữa dữ liệu và điều owner nhớ.

**P&L (tiền).** Mọi con số phiên này là **TRÚNG/TRẬT**. `V10917` quyết bằng **TIỀN**, và ngưỡng
rà `31/08` cũng viết bằng **TIỀN**. Hai thước **không thay thế nhau**.
