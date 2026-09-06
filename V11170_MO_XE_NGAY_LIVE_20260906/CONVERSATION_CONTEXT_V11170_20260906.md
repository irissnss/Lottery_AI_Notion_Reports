# CONVERSATION CONTEXT — V11170 · 06/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `CURRENT_ACTOR = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| ~22:0x | *«Tiếp tục phân tích đánh giá kết quả live hôm nay, đơn model, total, prompt v.v... tất cả mọi thứ không soát vấn đề nào nha em»* | `YÊU_CẦU` | Chụp trạng thái thật; cấp V11170 qua cổng chuẩn; 12 cổng đo + 12 cổng phản biện; tự đo 5 phép độc lập | `ĐÃ_LÀM` |

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| quy mô | **24 agent** (12 Sonnet đo + 12 Opus phản biện) · **4,64 triệu token** · 1.072 lượt công cụ · 71 phút · **0 lỗi** |
| lớp phản biện | bác bỏ / hiệu chỉnh **4 cổng ở mức nặng** |
| rút lại | 🔴 **`RL-025`** — ba mệnh đề của V11169 |
| production | **0 ghi · 0 deploy · 0 restart** · DB READ-ONLY |

---

## 3 · Điều đáng nói nhất — lớp phản biện cứu báo cáo khỏi một câu sai

Nếu chỉ chạy **một lớp**, bản này đã viết: *«cơ chế lật bạch thủ đang thắng +13,5 điểm ngoài cửa sổ
chọn, không rữa ngoài mẫu»* — nghe như một cải tiến hiếm hoi đã được chứng minh.

Lớp phản biện hỏi một câu mà **không cổng đo nào hỏi**: *hơn NGẪU NHIÊN hay chưa?*

Nền đúng của MN là **43,1%**, không phải 34,0%. Với nền đó: `ranked[0]` đạt 27,4% — **thua nền có ý
nghĩa** (z = −2,72). Bản đã công bố 38,4% — **vẫn dưới nền**. Nên «+10,96 điểm» là đi **từ
RẤT-dưới-nền lên VẪN-dưới-nền**, không phải vượt nền.

**Lỗi này lặp ở NĂM cổng.** Nó không phải sơ suất của một agent — nó là một chỗ mù có hệ thống:
ai cũng so với **cái mình vừa thay thế**, không ai so với **ngẫu nhiên**.

---

> **Vạch chú `PRJ-SELECTION-WINDOW-001`:** con số «+13,5 điểm» ở trên là **câu SAI đang được dẫn lại
> để bác bỏ**, không phải tuyên bố của bản này. Bộ **đủ bộ cửa sổ** cho phép lật nằm ở
> `REPORT_V11170.md` mục 3.4 và cho thấy **dấu ĐỔI**: 30 ngày **+22,29pp** · 90 ngày **−3,44pp** ·
> 180 ngày **−4,83pp**; MN riêng 73 ngày: TRONG cửa sổ +8,33pp (p=0,375) · NGOÀI +13,51pp (p=0,125).
> **CẤM trích** riêng cửa sổ 30 ngày. Và mọi vế đều **dưới nền** của chính miền nó
> (MN 43,1% · MT 35,2% · MB 23,8%), nên đây **không phải tuyên bố hiệu quả** mà là phép so hai
> phương án đều thua nền.

## 4 · Điều đáng nói thứ hai — agent chính đặt sai giả thuyết, và bị bắt

Trong đề bài, agent chính viết rằng cơ chế lật bạch thủ MN «có thể liên quan» tới `anti_trap` hoặc
`pp1_convergence_dampener`. **Cả hai đều sai.**

Cổng 3 đọc mã thật: cơ chế là `_v10640_official_perslice_override.get_override_bt()` với
`chooser="specialist"` ở `main.py:10231-10240`. Anti-trap tính **SAU** khi chốt và chú thích code
tự ghi *"Pure read-only. Does NOT change voting"*; `PRIOR_REGION_MAP["MN"]` **luôn rỗng**.

Đây là lý do đề bài ghi giả thuyết dưới dạng **«có thể liên quan»** kèm danh sách ứng viên, chứ
không khẳng định — và lý do mỗi cổng đều được lệnh **đọc mã thật, cấm kết luận theo tên đoán**
(RM-10).

---

## 5 · Điều đáng nói thứ ba — phiên tự bắt mình vi phạm §56

Agent chính **và** cổng 10 đều đo học thuyết chống bẫy («số đã ra ở miền trước thì đừng chơi lại»)
mà **không tra trước**. Phản biện tìm ra: dự án **đã có phép đo ĐĂNG KÝ TRƯỚC** cho đúng câu hỏi đó
— bảng `anti_trap_shadow_v11058` / `FU-397`, đăng ký **10/08/2026**, ngưỡng **n ≥ 90 và
|z_MH| ≥ 1,96**, ghi rõ **«chưa đủ n ⇒ cấm đọc sớm»**. Hiện **n = 63/90**.

Nặng hơn: trục anti-trap **từng được cắm thành cơ chế ghi đè thật** và **đã TẮT** sau khi đo tiến
cứu ra **−29,4 triệu / 60 ngày**.

⇒ Con số đọc sớm **không được dùng làm căn cứ**. Ghi vào báo cáo như một ca vi phạm, không giấu.

---

## 6 · Vấp ở đâu

| # | vấp | ai bắt |
|---|---|---|
| 1 | 🔴 **Năm cổng tuyên bố hiệu quả mà không có nền tuyệt đối** (`RM-18`) | lớp phản biện |
| 2 | 🔴 **Đọc sớm thí nghiệm đăng ký trước** (`§56`) | phản biện cổng 10 |
| 3 | 🔴 **Agent chính đặt sai giả thuyết** trong đề bài | cổng 3 |
| 4 | 🟠 Cổng 1 tuyên 3 số «không tái lập được» mà **chưa đi tìm định nghĩa gốc** — cả ba tái lập được | phản biện cổng 1 |
| 5 | 🟠 Cổng 8 đếm **124/253** bảng, bỏ sót 4 tên cột thời gian → đúng là **153/253** | phản biện cổng 8 |
| 6 | 🟠 Cổng 6 so `46.583` với số **có** system prompt — hai đơn vị khác nhau | phản biện cổng 6 |
| 7 | 🟠 Cổng 12 chạy lại truy vấn lúc 22:00 thay vì tại thời điểm tính thật (`RM-16`) | phản biện cổng 12 |
| 8 | 🟡 Một cổng trả bản nháp **rỗng** — phản biện đọc thẳng artifact, không mất việc | phản biện cổng 2 |
| 9 | 🟡 Ba chỗ ghi `NOT PROVEN` thật ra **chỉ cách một truy vấn** | các phản biện |

**Bài học ghi lại:** `NOT PROVEN` chỉ chính đáng khi **đã THỬ và thất bại**. Ghi `NOT PROVEN` vì
lười là một dạng nói dối nhẹ — nó làm người đọc tưởng câu hỏi khó, trong khi nó dễ.

---

## 7 · Cho TanPhatAI đọc tiếp

**Con số dễ bị trích sai nhất của phiên này:** «nền bạch thủ 34,0%». Đó là nền **GỘP BA MIỀN**.
Nền riêng: **MN 43,1% · MT 35,2% · MB 23,8%**. Dùng 34,0% cho một miền cụ thể là
`RM-21_VIOLATION`.

**Con số thứ hai:** «cơ chế lật +13,51pp ngoài cửa sổ chọn». Đúng khi so với `ranked[0]`, nhưng
**cả hai vế đều dưới nền**, và trên ba miền thì lợi ích **đổi dấu** (30 ngày +22,29 · 90 ngày −3,44
· 180 ngày −4,83). Hôm nay là 1 trong n=10 tạo ra con số +22,29 đẹp mắt đó.

**Việc rẻ nhất và có lợi nhất đang chờ owner:** ký **`SC-12`** — bản vá kế toán MT đã có, test
30/30, chờ ký. Nó đang làm **MB bị báo thấp 23,4 điểm** và loại MT khỏi **83,1%** lượt chấm.

---

TanPhatAI cần làm: ghi **`V11170`** — công khai bản này cùng `REPORT_V11170.md`. Ghi **NỀN RIÊNG TỪNG MIỀN: MN 43,1% · MT 35,2% · MB 23,8%**, cấm mượn 34,0% cho một miền. Ghi **NĂM ĐƯỜNG ĐO ĐỘC LẬP đều kết luận hệ KHÔNG hơn ngẫu nhiên, và cũng CHƯA đủ bằng chứng nói kém hơn**. Ghi **lớp phản biện đã cứu báo cáo khỏi câu «cơ chế lật đang thắng»**. Ghi **agent chính TỰ NHẬN đặt sai giả thuyết và TỰ NHẬN đọc sớm thí nghiệm đăng ký trước (§56)**. Ghi **RÚT LẠI `RL-025`** cho ba mệnh đề V11169. **Code KHÔNG đi trước tài liệu** — 0 ghi production. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.**
