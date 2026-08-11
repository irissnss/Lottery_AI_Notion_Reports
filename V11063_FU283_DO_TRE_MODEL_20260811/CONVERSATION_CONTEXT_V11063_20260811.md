# CONVERSATION CONTEXT — V11063 (FU-283) · 11/08/2026 khuya

## Owner nói gì (NGUYÊN VĂN)

> *«Các đề xuất của em anh đồng ý em tiến hành 1 cách cẩn thận và tỉ mỉ dùm anh nhé.»*

Rồi sau đó:

> *«em đang làm việc đúng không anh chờ báo cáo hay sao em?»*

Câu thứ hai là một cú bắt quả tang. Lượt trước agent viết *«Em bắt đầu ngay»* rồi **kết thúc lượt
mà không gọi một lệnh nào**. Owner ngồi chờ một thứ không chạy.

Agent trả lời thẳng: **«Không — không có gì đang chạy.»** Rồi bắt đầu thật.

Đây đúng thứ owner đã cảnh báo cùng ngày: *«thà em cập nhật tình hình thì anh còn dễ biết, em âm
thầm quá»*. Nói "sẽ làm" rồi im cũng là một kiểu âm thầm.

---

## Ba lần khung đo sai — và mỗi lần đều "có vẻ đúng"

`FU-283` nghe đơn giản: đổ `latency_seconds` vào bảng, gắn cờ model TB > 180s. Nhưng con số đầu
tiên ra ngay lập tức vô lý.

### Lần 1 — "tổng độ trễ vs biên tới hạn"

```
11/08 MT   tổng 2.564s   biên còn lại 660s   ⇒ TỔNG > BIÊN
14 lượt gần nhất: TỔNG vượt biên 9 lần
```

Nếu đúng thì MT phải vỡ hạn gần như mỗi ngày. **Nó không vỡ lần nào.** Một khung đo cho ra kết
luận mâu thuẫn với thực tế quan sát được thì khung sai, không phải thực tế sai.

### Lần 2 — "vậy chắc chạy song song"

Nghe rất hợp lý: MAX chỉ vượt biên **1/14 lần**. Agent định viết vậy. Rồi đọc mã:

```
scheduler.py:298   ThreadPoolExecutor(max_workers=1, thread_name_prefix="ai-timeout")
```

**`max_workers=1` không phải song song** — đó là **vỏ bọc timeout**, chạy trong luồng riêng để bỏ
được khi quá giờ. Chỗ song song duy nhất trong kho là `scraper.py` — **cào kết quả xổ**, không
phải gọi model.

Nếu dừng ở lần 2, báo cáo đã ghi *«các model chạy song song nên không lo»* — sai hoàn toàn.

### Lần 3 — "tính cả chuỗi từ đầu tới cuối"

```
11/08 MT   chuỗi AI 16:38 → 17:01     nhưng bundle CHỐT 16:47
```

**11/21 model chạy SAU khi đã chốt** — chính là `Shadow Auto-Eval Start` lúc `16:47:41` trong
journal. Chúng chậm mấy cũng không doạ được hạn.

Nếu dừng ở lần 3, báo cáo đã ghi *«chuỗi MT mất 43 phút»* — nghe khủng khiếp và vô nghĩa.

**Khung đúng:** chỉ tính model có `timestamp ≤ giờ chốt bundle`. Khi đó tổng 591–1.102s nhưng
wall-clock chỉ **4–10 phút** ⇒ có song song ~2× ở tầng khác.

---

## Và khi khung đúng thì kết quả lật ngược chính ngưỡng owner đã ký

| model | TB mọi lượt | % trên đường tới hạn | max | còn chạy? |
|---|---|---|---|---|
| `kimi-k2.5` | **231,4s** ⇒ vượt ngưỡng | **0/167 = 0%** | 1.087s | **ngừng từ 29/07** |
| **`glm-5.1`** | 185,5s ⇒ vượt ngưỡng | **32/207 = 15%** · TB-ĐTH **205s** | **1.027s** | **có, hôm nay** |

Ngưỡng `TB > 180s` tính trên **mọi lượt**, gồm cả 11 model chạy sau khi bundle đã chốt. Nên nó:

- **gắn cờ `kimi-k2.5`** — model không bao giờ nằm trên đường tới hạn và **đã ngừng chạy 13 ngày**.
  Cắt nó **không giảm được rủi ro hạn nào**;
- **không phản ánh** hành vi đuôi của `glm-5.1` — TB chỉ sát ngưỡng, nhưng **max 1.027s = 17
  phút**, **vượt toàn bộ ngân sách của MT**.

Đặt cạnh nhau: biên MT **~13 phút kinh niên suốt 12 ngày**, thấp nhất **8 phút**. Ngày 11/08
`glm-5.1` mất **410 giây** — **một mình chiếm gần hết wall-clock 9 phút** của cả chuỗi.

**Agent KHÔNG tự đổi ngưỡng.** `RM-08` và nguyên tắc đăng ký trước đều nói cùng một điều: ngưỡng
đã ký thì thi hành, muốn đổi thì owner đổi. Bảng ghi **đúng** cột owner ký, **và thêm** cột
`pct_tren_duong_toi_han` để owner thấy chỗ chệch mà quyết ở `FU-290`.

---

## Vì sao không cắt model nào trong phiên này

Ba lý do, mỗi lý do đủ để dừng:

1. Cắt model chạm **roster** — `QD-041` khoá tới **21/08**.
2. `FU-283` là mục **ĐO**, mục **CẮT** là `FU-290`. Làm đúng kỹ thuật nhưng sai phạm vi là `RM-05`.
3. Và số vừa đo cho thấy **danh sách cắt theo ngưỡng hiện tại sẽ cắt nhầm**.

---

## Đã dựng gì — đủ §52

Bảng `model_latency_shadow_v11063` (**4.046 ô**, 72 ngày, đủ 4 cờ shadow) · materializer ·
**cron 21:50** (sau P4 21:40 và anti-trap 21:45) · API `/api/admin/do-tre-model`
(`require_admin` + `no-store`) · panel `/monitoring` **đăng ký cả `loadAllSections()` lẫn
`setInterval`** — §52B đòi cả hai.

Đăng ký vào **cổng §52 chung**: giờ có **bốn** bộ đo, cả bốn **ĐẠT 6/6**.

**Deploy:** PID `1353489` → **`1438110`** — đổi thật, không phải tiến trình cũ còn sống (đúng bẫy
`systemctl restart lottery-ai` đã ghi trong CLAUDE.md). Health **200**, admin **401**, và **4 bảng
khoá số dòng y hệt** trước/sau: `12280 / 495 / 15259 / 12144`.

**Tài liệu ghi bằng chính công cụ `§63` dựng vài giờ trước** — `_v11062_nang_version.ghi()`, bốn
mặt một lệnh. Đây là lần đầu nó được dùng cho một phiên khác chính nó, và nó chạy đúng:
`governance_seq → 405`, cổng `§63` vẫn ĐẠT.

---

## Điều agent nói thẳng

Ba khung đo sai trong một phiên, và **cả ba đều cho ra báo cáo nghe rất kêu**:

- *«MT vượt ngân sách gấp 4 lần mỗi ngày»*
- *«các model chạy song song nên không lo»*
- *«chuỗi MT mất 43 phút»*

Thứ cứu được cả ba lần là **cùng một câu hỏi**: *nếu điều này đúng thì MT phải vỡ hạn — sao nó
không vỡ?* Đối chiếu kết luận với **thực tế quan sát được**, không chỉ với dữ liệu mình vừa tính.

---

## Trạng thái cuối phiên

Production **có đổi** (thêm endpoint + panel), đã deploy và verify. `QD-041` nguyên vẹn — phần này
chỉ đọc, không chạm đường chọn số. `FU-283` **XONG trước hạn 2 ngày**.

TanPhatAI cần làm: xem mục cuối `REPORT_V11063.md` — năm việc, quan trọng nhất là ② **`FU-290` sẽ
cắt nhầm** nếu dùng nguyên ngưỡng `TB > 180s`, và ③ agent **không tự đổi ngưỡng** — cột mới
**không phải** ngưỡng mới.
