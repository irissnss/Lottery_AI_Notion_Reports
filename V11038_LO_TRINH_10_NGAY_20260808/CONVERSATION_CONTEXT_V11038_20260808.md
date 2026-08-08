# CONVERSATION CONTEXT — V11038 · 2026-08-08 khuya

## Owner giao gì

Lộ trình 10 ngày 08/08 → 18/08, năm giai đoạn GĐ-0 → GĐ-4, ký `OWNER SIGNATURE: QD-046`.
Cứu cánh **không phải tỉ lệ trúng** mà là bốn chỉ số hệ thống K1–K4.

## Việc đầu tiên agent làm: BÁO VA CHẠM NGAY TRONG BRIEF

Brief ký **`QD-046`**. Nhưng **`QD-046` đã dùng lúc 20:10 cùng ngày** cho mở khoá `NO_ANSWER`
(FU-355). Ghi đè là **mất một quyết định của owner**.

| lần | brief cấp | thực tế |
|---|---|---|
| 07/08 | `QD-028` | đã dùng |
| 08/08 sáng | `QD-043` | đã dùng ⇒ ghi `QD-044` |
| **08/08 khuya** | **`QD-046`** | **đã dùng ⇒ ghi `QD-047`** |

Brief còn nói *"QD-043/QD-044 đã dùng — cấm tái sử dụng mã"* nhưng **bỏ sót `QD-045` và
`QD-046`**, cả hai cũng đã dùng tối 08/08.

**Ba lần trong hai ngày.** Và `FU-369` — cổng cấp số hiệu quét ba nơi — **đã có mã nhưng chưa
được dựng**. Đây là bằng chứng rõ nhất rằng nhắc suông đã thất bại.

## Việc thứ hai: agent phạm ĐÚNG lỗi vừa vá, cách nhau vài giờ

Sáng nay agent vá `FU-353` — hai mục mất hạn, vô hình với máy.
Tối nay agent tạo `FU-357` và `FU-360` **không có hạn trong tiêu đề**.

Đo lại toàn sổ: **64 mục treo** không có hạn, không phải 2.

**Cơ chế thật:** `FOLLOW_UP_TRACKER.md` ghi mới ở **ĐẦU** tệp ⇒ *"lần nhắc mới nhất"* = lần đầu
gặp. `load_fu_latest()` lấy lần đó rồi **vứt hết lần cũ**. Nên **nhắc lại một mã FU trong khối
phiên bản sau mà không chép lại hạn = XOÁ HẠN**, không một tiếng động.

Nạn nhân gồm **chính các mục agent tạo hôm nay**: `FU-341` · `FU-344` · `FU-345` · `FU-355` —
đều đã ghi hạn rõ ở khối gốc rồi bị chính agent nhắc lại làm mất.

**Luật đúng đã cài:** lần nhắc sau không lặp hạn là **cập nhật nội dung**, không phải **xoá
hạn**. Kế thừa từ lần nhắc cũ hơn; **hạn mới luôn thắng**; mã đọc §58 kế thừa theo cùng luật.

| | TRƯỚC | SAU |
|---|---|---|
| mục treo thiếu hạn | **64** | **57** |
| kế thừa lại được | 0 | **16** |
| briefing «đến hạn hôm nay» | 9 | **12** |

**57 mục còn lại chưa từng có hạn ở bất kỳ lần nhắc nào** — agent **KHÔNG tự đặt** (RM-06:
cấm đặt hạn cho có). Đó là việc phải hỏi owner.

## Việc thứ ba: kiểm phiên song song

Có phiên khác chạy 20:16 và 20:28, và **cả hai phiên cùng dùng số V11037**. Agent kiểm md5
toàn bộ trước khi làm gì tiếp:

`_v10879_nghiemthu_lane.py` · `combo_super.py` · `gpt_analyzer.py` — **local = VPS cả ba**.
`NGUONG_P = 0.05` và `assert both_lose >= 0` **còn nguyên**. **Không mất gì.**

## GĐ-0 V1 — và một chỗ agent đọc theo Ý ĐỊNH, không theo chữ

Brief viết *"số lượt `context_pack_chars = 64` phải BẰNG 0"*.

Đo thật ngày 08/08: **là 12, không phải 0**. Nhưng **cả 12 đều ở 05:17–05:41**, tức **TRƯỚC**
deploy V11032 (10:27:34). Sau deploy: **0 lượt**, 16h min 10.584, 17h min 15.474.

Điều kiện thật cần kiểm là **0 lượt SAU deploy** — và điều đó **ĐẠT**. Đọc chữ theo nghĩa đen
sẽ dừng cả lộ trình một cách vô lý. Agent ghi rõ cách đọc này thay vì im lặng chọn một bên.

## Điều agent NÓI THẲNG với owner

**1. Agent không im lặng làm theo brief khi brief sai.** Cấp một mã đã dùng thì ghi mã mới và
nêu rõ, để owner sửa nếu muốn. Im lặng ghi đè là mất quyết định.

**2. Vá cơ chế không tự sửa được thói quen.** Sáng vá FU-353, tối lại phạm đúng lỗi đó. Đó là lý
do phải có **cổng**, không phải chỉ có bản vá — đúng tinh thần RM-15 vừa ghi vào sổ sáng nay.

**3. Đây là lần thứ BA trong một ngày agent tìm ra thứ tự nó báo xanh trong khi đang hỏng:**
cổng đóng băng QD-041 (mù vì `git log --since` trả rỗng) · `decide()` của `/nghiem-thu` ·
và nay là bộ đọc sổ theo dõi (im lặng xoá hạn). Ba cái đều **không kêu một tiếng**.

**4. Việc nên làm TRƯỚC TIÊN trong GĐ-1 không phải mục số 1 mà là mục số 3** — dựng `FU-369`
(cổng số hiệu). Vì mọi mục sau đều cấp mã mới, và hôm nay đã va chạm ba lần.
