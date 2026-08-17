# CONVERSATION CONTEXT — V11077 · việc xảy ra 16/08/2026, viết bù 17/08/2026

> **BÙ.** Việc chạy lúc **16/08 18:56** (`a33b86a`); bản này viết **17/08** trong `V11083`/`GĐ-5`.
> Nguồn: **bản ghi của chính phiên gốc** — phiên viết bản này là phiên đã chạy phép đo. Owner
> khoá **phương án (a)** lúc **12:57 ngày 17/08**: *«CHỈ phiên gốc viết bù từ bản ghi của chính
> nó (RM-17). Nếu không còn truy cập bản ghi gốc → DỪNG mục này, báo owner; CẤM tự chuyển sang
> soạn từ commit message hay nguồn khác.»*

---

## Owner nói gì (NGUYÊN VĂN)

> *«làm hết đi giao nhiệm vụ thì làm đi, làm sao phải tổng lực không rơi rớt, phải tìm cho ra chỗ
> cải tiến nâng cao dự đoán, cấm đoán bừa, suy diễn. Yêu cầu của anh phải được thực hiện nghiêm
> túc»*

---

## Câu chuyện của phép đo này, kể đúng thứ tự

**Bước 1 — bản đào tìm ra một dòng đáng ngờ.** `gpt_analyzer.py:5958` gom pool đuôi chéo miền
D-1 rồi cắt `[:12]` trước khi bơm vào prompt. Đo ra: cắt mất **83%** pool.

**Bước 2 — và một dấu hiệu nữa, nặng hơn.** `sorted()` chạy trên chuỗi hai chữ số, nên `[:12]`
gần như luôn giữ **nhóm thấp nhất**. Quét 30 ngày: **30/30 ngày** trong 12 đuôi còn lại **không
có đuôi nào lớn hơn 21**.

**Bước 3 — cả agent lẫn bản đào đều nghiêng về «có neo».** Câu chuyện quá gọn: cắt 83%, luôn giữ
nhóm thấp, 30/30 ngày. Nghe là tin.

**Bước 4 — và đây là chỗ luật cứu.** Đăng ký ngưỡng **trước khi chạy**, ghi thẳng vào script:

```
CÓ NEO  ⇔  chênh ≥ +2,5pp  VÀ  |z| ≥ 2
```

**Bước 5 — đo xong, kết quả NGƯỢC:**

```
model chọn đuôi 00–21 :  20,2 %
nền                   :  21,0 %
chênh                 :  −0,79 pp     ← ngược dấu
z                     :  −1,01
⇒ KHÔNG NEO
```

Model **không hề** bị kéo về nhóm đuôi thấp. Dòng cắt kia có cắt thật, nhưng **không đổi hành vi
chọn số**.

---

## Vì sao chuyện này đáng kể hơn bản thân kết quả

Nếu **không** đăng ký ngưỡng trước, báo cáo hôm đó đã ghi *«tìm ra nguyên nhân»* — và owner sẽ đi
duyệt một bản vá cho thứ **không tồn tại**, trong vùng `QD-041` đang khoá.

Đây là luật đã cứu đúng một lần, có số để chỉ. Nó cùng họ với `RM-13`
(*«nguồn sai thì mọi kết luận sai»*) và `RM-17` (*«số không tái lập được thì cấm dùng làm căn cứ
quyết định»*).

---

## Giới hạn — phải nói, không được lờ

Đây là **một** ca, đo **một** cơ chế, trên **30 ngày**.

**KHÔNG được** đọc thành *«nhồi thêm dữ liệu vào prompt là vô hại»*. Ngay trong cùng đợt đào,
`FU-404` cho thấy nhãn `HR12W 1.0` **nói quá** giá trị thật (thực chất *«12/12 tuần trúng ≥1 trong
3,5 đuôi»*, lợi thế thật chỉ **~+1,0%**) — tức có nhãn **đang** dạy model sai. Hai kết quả không
mâu thuẫn: cái này nói **một** dòng cắt vô hại, cái kia nói **một** nhãn có hại.

---

## Vấp

**Không có vấp kỹ thuật.** Vấp duy nhất là **vấp nhận thức và nó đã bị chặn**: agent bước vào
phép đo với niềm tin sẵn về kết quả, và luật đăng-ký-ngưỡng-trước là thứ ngăn niềm tin đó thành
kết luận.

---

## Vì sao bản báo cáo này ra trễ một ngày

`_v11062` `K1` lấy danh sách việc **chỉ từ CHANGELOG**. Bản đã commit & push mà chưa vào CHANGELOG
thì **không nằm trong danh sách để hỏi** — nó không lọt qua cổng, nó **chưa bao giờ bị hỏi**.
V11077 trôi đúng **34 phút** sau khi phiên vừa bù xong 12 bản khác, cổng vẫn xanh.

Đã vá ở **V11082** (`d72ebc7`): `K1` nay hợp `CHANGELOG ∪ git log`, thử chặn hai chiều ĐẠT.

TanPhatAI cần làm: ghi `FU-316` **ĐÓNG — nhánh 2, KHÔNG NEO**; ghi bản này là **BÙ** (việc 16/08,
viết 17/08, phương án (a)); và giữ nguyên `FU-404` **đang mở** — kết quả này **không** dùng để
kết luận chung về việc nhồi ngữ cảnh.
