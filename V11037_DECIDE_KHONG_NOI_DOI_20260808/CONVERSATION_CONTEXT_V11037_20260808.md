# CONVERSATION CONTEXT — V11037 · 2026-08-08 khuya

## Owner nói gì (NGUYÊN VĂN)

> Tiếp tục theo đề xuất anh nghĩ em nắm code rõ , ngử canh anh chung cấp em khá nhiều rồi, em
> biết phải làm gì để hệ thống được giám sát và cải tiến tốt nhất

Owner giao toàn quyền theo thứ tự agent đã đề xuất. Agent làm **đúng thứ tự đã trình**, không
tự đổi: **FU-357 trước** (cổng có thể nói dối owner, hạn 19/08), rồi **FU-353**.

## Việc quan trọng nhất: một cổng đang có thể nói dối owner

`_v10879_nghiemthu_lane.decide()`:

```python
if new_only > off_only:
    verdict = "ĐẠT — đủ điều kiện trình owner duyệt thay official"
```

**Hai số đếm thô. Không một phép ý nghĩa nào.**

Đo 08/08: đo tiến đang **3 vs 4**. Chỉ cần **HAI ngày may** nữa là **5 vs 4** ⇒ trang sẽ báo
**«ĐẠT — đủ điều kiện trình owner duyệt thay official»**, trong khi McNemar chính xác cho
5-vs-4 ra **p = 1,0** — tức **không phân biệt được với tung đồng xu**.

`DECISION_DATE = 19/08`, còn **11 ngày**. Nghĩa là hệ có thể trình owner một kết luận sai.

**Nay bắt buộc `p < 0,05`**, ngưỡng ghi bằng số ngay trong hàm (RM-03 — đăng ký ngưỡng TRƯỚC):

| cặp lệch | p | luật CŨ | luật MỚI |
|---|---|---|---|
| 5 vs 4 | **1,0** | **ĐẠT** ⚠ | **CHƯA ĐƯỢC PHÉP KẾT LUẬN** |
| 8 vs 2 | 0,109 | ĐẠT ⚠ | **CHƯA ĐƯỢC PHÉP KẾT LUẬN** |
| 9 vs 1 | 0,021 | ĐẠT | ĐẠT ✓ |

Và khi chưa đủ sức, **chữ nói đúng điều đó** thay vì để owner tự hiểu là đã chứng minh.

## Lỗi thứ hai cùng gốc: bảng công bố cho owner có SỐ ÂM

`_discordant()` lọc theo **SỐ khác nhau** rồi trừ. Nhưng hai bên chọn **hai số khác nhau mà CẢ
HAI CÙNG TRÚNG** là chuyện có thật — **7 ngày** như vậy. Chúng bị cộng vào **cả hai** vế ⇒
`both_lose = −1` trên cửa sổ đo tiến.

Và nặng hơn: `p_value` tính từ `(29, 15)` thay vì cặp lệch thật `(22, 8)`.

**Gốc chung của cả hai lỗi: lẫn «số khác nhau» với «kết quả khác nhau».**
Hai số khác mà cùng trúng là cặp **đồng thuận**, không mang thông tin nào về bên nào hơn.

| | TRƯỚC | SAU |
|---|---|---|
| đo tiến `both_lose` | **−1** | **0** |
| backfill cặp lệch | 29 / 15 | **22 / 8** (`both_win` = 7) |
| backfill `both_lose` | 33 | **40** |

Thêm `assert both_lose >= 0` — bốn nhóm phải phủ kín, không thì dừng ngay.

**Agent suýt chỉ vá `decide()`** — nhưng `_discordant()` mới là chỗ **đang in số âm ra trang cho
owner đọc**. Vá một cái là bỏ nửa chừng (§60).

## FU-353 — tưởng một gốc, thật ra HAI

| mục | gốc | vá |
|---|---|---|
| **FU-317** | tiêu đề `hạn **21/08**` — dấu `**` chen giữa làm mẫu regex **trượt** | lỗi **BỘ ĐỌC** ⇒ cho phép dấu nhấn markdown |
| **FU-325** | tiêu đề `cần 10/08` — **không có chữ «hạn»** | lỗi **DỮ LIỆU** ⇒ sửa chính tiêu đề |

**Nếu chỉ sửa regex thì FU-325 vẫn vô hình. Nếu nới regex đủ rộng để bắt cả FU-325 thì sẽ vơ
nhầm ngày trong câu kể** (*"không phải 08/08"*, *"dựng xong sớm 07/08"*) — hại hơn lợi.

## Điều agent NÓI THẲNG với owner

**1. Cảnh báo đọc số:** backfill `p = 0,01612` **nghe như có ý nghĩa** — nhưng đó là dữ liệu
**chấm ngược**. `decide()` chỉ nhận `forward`, đúng thiết kế. Trích con số backfill làm bằng
chứng *«bản mới hơn official»* chính là **dấu vân tay thiên vị chọn** mà R2 đã đo. Đừng ai dùng
nó, kể cả khi nó nằm ngay trên trang.

**2. CỐ Ý CHƯA LÀM FU-360, và nói rõ vì sao.** `database.py:2986` `UPDATE predictions` **không
lọc `run_source`**. Bẫy chưa nổ (0 khoá trùng/30 ngày) nhưng **sẽ nổ đúng lúc `QD-015/016/017`
chạy 21/08** — vì đó là lúc một model chạy cả hai đường.

Hôm nay đã có **BỐN** thay đổi: V11032 · V11033 · V11036 · V11037. Đây là `database.py` —
**ghi vào bảng khoá `predictions`**. Vá một chỗ ghi DB ở cuối một phiên dài là đúng thứ sổ RM
đã ghi nhiều lần. Hạn **14/08**, còn thừa thời gian làm đầu phiên với đầu óc tỉnh táo.

**Owner giao toàn quyền không có nghĩa là làm hết trong một đêm.** Biết dừng đúng chỗ cũng là
một phần của việc giám sát tốt.

**3. Đây là lần thứ hai trong ngày agent tìm ra một CỔNG nói dối** — sáng nay là cổng đóng băng
QD-041 (mù hoàn toàn vì `git log --since` trả rỗng), giờ là `decide()`. Cả hai đều **báo xanh**
trong khi thứ chúng canh đang hỏng. Đó là lý do **RM-15** (cổng phải chứng minh chặn được) vừa
được ghi vào sổ RM sáng nay — và hai lần trong một ngày cho thấy nó **cần thật**.
