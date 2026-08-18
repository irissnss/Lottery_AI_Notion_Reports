# CONVERSATION CONTEXT — V11087 · 18/08/2026 tối muộn

## Owner nói gì (NGUYÊN VĂN)

> *«Em xem các yêu cầu này có còn phù hợp không, nếu còn thì xử lý, không thì viết rõ lý do gửi
> báo cáo đầy đủ và đề xuất tiếp theo cho anh nhé.»*

Kèm ba quyết định ký **19:18 ngày 18/08**:

> ① *«`V11080b`: TRUY PHIÊN GỐC VIẾT BÙ… Truy không ra → DỪNG, báo owner; cổng K1 cứ đỏ ĐÚNG
> trong lúc chờ. CẤM soạn hộ từ commit message hay nguồn khác.»*
> ② *«Hook SessionStart: TỪ CHỐI… Không ai được cài hook này; đề xuất lại thì phải qua owner.»*
> ③ *«48 bản vá cũ: HOÃN sau 21/08… Sau 21/08 rà lại có đối chiếu, không áp mù.»*

---

## Câu mở đầu của owner cứu cả phiên

*«Em xem các yêu cầu này có còn phù hợp không»* — nếu owner không thêm câu đó, phiên này đã đi
làm quyết định ① và **không tìm ra gì**, rồi báo *«truy không ra, dừng»*. Cổng sẽ đỏ giả thêm
nhiều ngày nữa.

Câu ấy buộc **kiểm tiền đề trước khi thi hành**. Và tiền đề của ① **sụp**.

---

## ① — truy ra được, và kết quả ngược hẳn

**Truy phiên gốc: RA.** Transcript `d63e64c6`, cửa sổ **16/08 22:45 → 17/08 00:45** giờ VN —
khớp chính xác 10 commit của phiên kia. 540 dòng, nhắc `V11080b` **14 lần**.

Và chính bản ghi đó nói thẳng điều mà phiên này đã bỏ lỡ suốt hai ngày:

> *«`V11080b` chỉ là **nhãn commit phụ** cùng một bản — trong khi `V10964b` là **bản riêng
> THẬT** (có mục CHANGELOG riêng).»*

Phiên gốc **không quên viết bù**. Phiên gốc **đã xác định** không có gì để bù, **và đã cài luật
đó vào cổng của họ** (`_v10921:128-138`).

**Bốn bằng chứng, tất cả độc lập với transcript:**

```
grep -cE "^## V11080b" CHANGELOG.md   ->  0      (không có mục riêng)
grep -cE "^## V10964b" CHANGELOG.md   ->  1      (có — phép phân biệt là THẬT)
V11080 trong HISTORY                  ->  1 dòng (đã có)
_v10921_report_gate.py:128-138        ->  luật lọc hậu tố ĐÃ CÓ SẴN
```

Kết luận đứng vững **kể cả khi bỏ transcript đi** — điều này quan trọng, vì nó là lý do việc đọc
transcript ở đây **không phải** «soạn hộ từ nguồn khác».

---

## Và lỗi là của phiên này, không phải của ai khác

`V11082` vá K1 bằng cách hợp `CHANGELOG ∪ git log`. Chú thích **do chính nó viết**:

> *«`_v10921_report_gate` đã vá lỗ y hệt… đây là áp **cùng cách**, không sáng chế cách thứ hai.»*

Nó chép **hợp nguồn**. Nó **không chép** luật lọc hậu tố — thứ nằm **ngay bên cạnh**, trong cùng
hàm, ở `_v10921:128-138`.

Viết ra chữ *«áp cùng cách»* rồi chép nửa cách. Đúng `§60` (bỏ nửa chừng) và `RM-07` (vá một lỗi
không phải vá cả họ lỗi). Và hậu quả kéo **bốn báo cáo công khai** cùng nói sai một câu.

---

## Hai vấp trong lúc vá — cả hai bắt được vì NHÌN SỐ, không vì tin chữ

### Vấp 1 — vá nhầm hàm

Neo `ra: dict[str, str] = {}` khớp `muc_changelog()` **trước** `muc_git_log()`. Bản vá ghi đè
thân hàm sai, làm `muc_changelog` tham chiếu biến `r` không tồn tại.

Bắt được vì **đọc lại output** của script vá — nó in `thay dai dong 95..100` trong khi
`muc_git_log` nằm ở dòng 157. Đã `git checkout` khôi phục, rồi **xác minh mọi hàm còn đủ, cú
pháp OK, khớp `HEAD`** trước khi làm tiếp.

### Vấp 2 — và đây là vấp đáng sợ hơn nhiều

Heredoc nuốt `\b` thành **ký tự BACKSPACE thật** (`\x08`). Regex thành:

```
^\s*(V\d+)([A-Za-z]?\d*)^H(.*)$
```

Khớp **0 dòng**. Cổng in:

```
git log : 0 nhãn version · chỉ-có-ở-git 0 (trong đó THIẾU HISTORY: 0)
✓ [cổng] NANG_VERSION_V11062=ĐẠT
```

**Cổng xanh vì nó THÔI NHÌN.** Đó là loại hỏng tệ nhất — tệ hơn cổng đỏ, vì cổng đỏ thì có người
đi xem.

Bắt được **không phải** vì thấy chữ `ĐẠT`, mà vì **nhìn con số `0`** ở dòng ngay trên. Trước vá
là 352 nhãn; sau vá còn 0 — không có cách nào con số đó đúng.

Đây là **lần thứ ba trong ba ngày** cùng lớp lỗi heredoc/escape: 16/08 (bash ăn backtick, tệp
rỗng mà lệnh báo thành công) · 18/08 sáng (heredoc vỡ khi viết báo cáo) · 18/08 tối (lần này).
Đã chuyển sang công cụ sửa trực tiếp — hết tầng escape.

---

## Vì sao có phép kiểm «95 nhãn bị gộp»

Bản vá làm cổng **thấy ít hơn** (352 → 254 nhãn). Đó là hướng **dễ giấu lỗi thật nhất**: vá xong
cổng xanh, và không ai biết nó xanh vì hết lỗi hay vì hết nhìn.

Nên phải chứng minh phần bị bớt là phần **đáng bớt**:

```
95 nhãn bị gộp — CẢ 95 đều KHÔNG có mục CHANGELOG riêng
   V10807b · V10809c · V10820e · V10821b · ...
1 nhãn mới xuất hiện: V10807 (bản gốc của V10807b)
```

Không mất bản thật nào.

---

## ② — quyết định còn nguyên giá trị, và đã đúng sẵn

Hook `SessionStart` **chưa bao giờ được cài**. `grep -c SessionStart .claude/settings.json` → **0**.

Nên việc thi hành ở đây không phải gỡ gì, mà là **ghi thành văn** để lần sau không ai cài lại:
`FU-408` `CLOSED_FAIL`, kèm lý do owner nêu và câu *«đề xuất lại phải qua owner»*.

---

## ③ — quyết định đúng, nhưng đối tượng đang tan

Owner hoãn 48 bản vá vì *«áp mù có thể đè mất việc của phiên kia»*. Lý do đó **đúng**.

Nhưng đo ra một chuyện quyết định chưa biết: **48 bản vá không tồn tại thành một bộ rà được**.

```
nằm rải rác trong  : 1.507 tệp, thư mục TẠM AppData/Local/Temp/.../scratchpad
mục lục            : KHÔNG có
số hiệu cao nhất   : #41  (không phải dãy 1-48 liền)
tệp .patch/.diff   : 0
độ bền             : thư mục tạm có thể bị dọn bất cứ lúc nào
```

Nên vế *«sau 21/08 rà lại có đối chiếu»* **có thể không thực hiện được**.

Phiên này **không tự làm mục lục** — đó là việc mới, ngoài ba quyết định, và owner đang khoá phạm
vi tới 21/08. Nên nó thành **đề xuất có hạn dùng**, ghi thẳng vào ô rủi ro của `FU-409`.

---

## Trạng thái cuối phiên

Production **không đổi**. `QD-041` nguyên vẹn.

**Lần đầu kể từ 17/08 không có cổng nào đỏ** — và điều đáng nói là nó xanh **không phải vì bù
thêm gì**, mà vì **cái đỏ vốn là giả**.

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11087.md` — quan trọng nhất là **`RL-007`** (rút lại
câu đã công bố ở bốn báo cáo) và **đề xuất lập mục lục 48 bản vá**, việc này **có hạn dùng**.
