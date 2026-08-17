# CONVERSATION CONTEXT — V11082 · 17/08/2026

> **Bản đẩy SỚM, phiên chưa kết thúc.** Owner yêu cầu có bản để đọc trước khi ra lệnh tiếp, nên
> phần đã xong được đẩy ngay thay vì chờ hết phiên. Phần còn lại (`GĐ-1/vá-2` → `GĐ-5`) mang số
> riêng.

---

## Owner nói gì (NGUYÊN VĂN, kèm giờ)

> **12:54** — *«TẠM DỪNG mọi lane khác — phiên này là lane DUY NHẤT; toàn bộ công sức dồn cho hoàn
> thiện luật. (Các lane đo chạy bằng cron trên server không bị ảnh hưởng — CẤM đụng chúng.)»*

> **12:57** — *«V11077/V11079 theo phương án (a) — CHỈ phiên gốc viết bù từ bản ghi của chính nó
> (RM-17). Nếu không còn truy cập bản ghi gốc → DỪNG mục này, báo owner; CẤM tự chuyển sang soạn
> từ commit message hay nguồn khác.»*

> **sau khi GĐ-1/vá-1 xong** — *«không đẩy báo cáo lên ah để anh còn phân tích đánh giá và ra lệnh
> xử lý mới em»*

Câu cuối là lý do tồn tại của bản này. Owner đã nói **cùng một ý** hồi 11/08 —
*«thà em cập nhật tình hình thì anh còn dễ biết, em âm thầm quá»* — và agent lại rơi vào đúng nếp
cũ: làm tiếp, chưa đẩy. **Đây là lần nhắc thứ hai cho cùng một thói quen.**

---

## Việc hôm nay bắt đầu từ một câu hỏi đơn giản: cổng mới có thật sự thấy không?

Hôm 16/08 dựng cổng `git commit`, và nó **chặn thật ngay lần đầu** — agent không commit được cho
tới khi bù đủ 12 dòng `HISTORY`. Nghe như xong chuyện.

Nhưng **34 phút sau khi bù xong**, hai bản `V11077` (`a33b86a`) và `V11079` (`4a7ee6d`) trôi qua —
**cổng vẫn báo xanh**.

Lý do nằm ở một dòng:

```python
_v11062_nang_version.py:159
    tu_moc = sorted([v for v in cl if _doc_v(v) >= MOC_THI_HANH], ...)
                              ↑ cl = CHỈ CHANGELOG
```

`K1` hỏi *«mỗi bản trong CHANGELOG đã có dòng HISTORY chưa?»* — nên một bản **đã commit & push mà
chưa vào CHANGELOG** thì **không có mặt trong danh sách để hỏi**. Nó không lọt qua cổng; nó
**chưa bao giờ bị hỏi**.

Cùng họ với `RM-15`: *«cổng không qua thử coi như KHÔNG TỒN TẠI»*. Ở đây cổng có chạy, có chặn —
nhưng **worklist bị hẹp** nên phần lớn thực tế nằm ngoài tầm nhìn của nó.

---

## Một chỗ agent tự bắt được mình — và tại sao không im lặng cho qua

Bản vá đầu tiên đặt `K1b` **báo đỏ** cho 15 bản *«có ở git mà chưa có tiêu đề riêng trong
CHANGELOG»*. Nghe hợp lý.

Kiểm lại thì **12/15 bản ĐÃ CÓ dòng `HISTORY`** — chúng được ghi **gộp** trong khối `V11076`, là
cách ghi hợp lệ. Nếu để nguyên, cổng sẽ **đỏ vĩnh viễn ngay từ ngày dựng** ⇒ người đọc quen mắt ⇒
**mất sạch giá trị cảnh báo**.

Chính owner đã nêu nguyên tắc này trong prompt hôm nay, cho `CHECKSUMS`: *«đỏ 100% thì tệ hơn là
không có»*. ⇒ **Hạ `K1b` xuống GHI CHÚ.** Giá trị thật của việc hợp `git log` là **mở rộng
worklist của `K1`**, không phải đẻ thêm một phép đỏ.

---

## Đính chính một điều chính agent viết hôm qua

Báo cáo `V11081` mục 9 ghi lỗi 2 là *«verdict `_v10920` KHÔNG ỔN ĐỊNH»*.

Đo lại hôm nay: **cơ chế sai là thật** —

```python
_v10920_decision_ledger.py:194
    except Exception as ex:
        return False, f"KHÔNG CHẠY ĐƯỢC: ..."     ← hết giờ ⇒ trả FALSE ⇒ đếm thành TRÔI
```

`RM-12` cấm đúng chuyện này: `KHÔNG_KIỂM_ĐƯỢC` bị gộp vào `TRÔI`.

**Nhưng triệu chứng KHÔNG tái hiện.** Chạy hai lần liên tiếp, cả hai lần đều ra `3 PHÉP TRÔI`.

Ghi đúng như đo được: **vá vì cơ chế sai, không vá vì triệu chứng** — và **không được ghi «đã tái
hiện»** khi nó không tái hiện. Đây chính là loại lệch mà `§62` bắt phải báo: `DOC_SAID` (báo cáo
hôm qua) **≠** `CODE_DID` (đo hôm nay).

---

## Vấp trong phiên

**Vấp 1 — biến dùng trước khi định nghĩa.** Bản vá đầu đặt `chi_git_va_thieu` **sau** chỗ dùng nó
⇒ `UnboundLocalError`. Bắt được vì **chạy và nhìn output**, không phải vì tin dòng «✓ đã sửa».
Cùng bài học ngày 13/08 và 16/08: **«lệnh chạy xong» không bằng «việc đã xảy ra»**.

**Vấp 2 — commit bị chính cổng mới chặn.** Cổng đang đỏ **vì chính lỗi mà commit đó đi vá**
(3 bản chưa có dòng `HISTORY`). Không bỏ qua thì không commit được bản vá. ⇒ dùng
`BO_QUA_CONG_COMMIT=1` **có ghi lý do vào commit message**, đúng giao kèo của cổng — không phải
lách.

---

## Ba việc DỪNG LẠI CHỜ OWNER — và vì sao không tự quyết

**① Cảnh báo an ninh.** Một subagent trong đợt đào đề xuất **tự cắm hook `SessionStart`** vào
`.claude/settings.json`. Đó là thêm **mã tự chạy mỗi lần mở phiên**. Owner **chưa cho phép**, và
loại thay đổi này không nằm trong nhóm được tự quyết. **KHÔNG ÁP.**

**② Phiên khác đã sửa kho.** Từ `16/08 22:58` đến `17/08 00:40` có **10 commit**, **30 tệp**,
**+2.439 dòng**, trong đó **sửa 3 cổng đang dùng**. **48 bản vá** dựng lúc 19:00 ngày 16/08 nay
**có thể đã cũ**. Áp mù có nguy cơ **đè mất việc của phiên kia** — phải kiểm lại từng bản trên kho
hiện tại, bản nào đoạn `trước` không còn khớp thì **loại**, cấm sửa mò.

**③ `K8`/`QD-021`.** Prompt quy định `GĐ-4` **chỉ TRÌNH**, cấm tự đóng. Hạn `≤18/08` — mai.

---

## Trạng thái cuối phần này

Production **không đổi**: không DB, không deploy, không Notion, không đụng đường dự đoán —
`QD-041` nguyên vẹn.

**Hai cổng đang ĐỎ, và đỏ ĐÚNG:** `_v11062` đỏ vì 3 bản chưa bù (`GĐ-5` sẽ xử), `_v10920` đỏ vì
3 phép trôi thật. **Không ghi «mọi cổng xanh»** — đó là câu nói dối quen thuộc mà `RM-12` sinh ra
để chặn.

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11082.md` — quan trọng nhất là **ba việc chờ owner ký**
và **đính chính lỗi 2** (cơ chế đúng, triệu chứng không tái hiện).
