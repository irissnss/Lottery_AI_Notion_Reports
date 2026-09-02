# CONVERSATION CONTEXT — V11152 · 02/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`. **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Đây là **MỆNH LỆNH TRỰC
> TIẾP CỦA OWNER**, nói trong IDE, **có hiệu lực ngay**. Owner trao đổi liên tục nên **code
> thường đi trước tài liệu** — điều owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`).
> **Bản này chứa một câu owner BÁC BỎ agent** — tài liệu nào nói ngược thì tài liệu phải sửa.

| giờ (VN) | NGUYÊN VĂN | loại |
|---|---|---|
| 02/09 ~10:30 | *«A đọc thấy dừng showdow là sao em? Showdow đang đốt tiền của anh nhưng không mang giá trị không đo được ko sàn lọt ko thử nghiệm để lấy đc các hưu ịch.»* | **`BÁC_BỎ`** |
| 02/09 ~10:30 | *«Điều anh muốn là Prompt thuần ngử cảnh, chạy showdow và showdow cần xếp hạng chung để đưa vào total và total cần đưa ra giải pháp tốt nhất»* | `YÊU_CẦU` |

### Owner bác cái gì, và vì sao nó quan trọng

`V11151` viết: *«việc đúng là **dừng lượt shadow**, và cái được là **tiền API**, không phải chất
lượng dự đoán»*.

Owner bác thẳng. Đọc kỹ câu owner thì thấy ba mệnh đề, **không** phải một:

| owner nói | nghĩa là |
|---|---|
| *«đang đốt tiền … nhưng không mang giá trị»* | vấn đề là **giá trị không được rút ra**, không phải **tiền chi ra** |
| *«không đo được, không sàng lọc, không thử nghiệm»* | thiếu **cơ chế biến kết quả thành phán quyết** |
| *«shadow cần xếp hạng chung để đưa vào total»* | shadow là **nguồn ứng viên**, không phải khoản chi phí để cắt |

**Hai hướng ngược nhau hoàn toàn:** kết luận cũ hướng về **cắt giảm**; kết luận đúng hướng về
**khai thác**. Nếu làm theo bản cũ thì đã gỡ đi chính cái pool ứng viên mà `TOTAL_V2` cần.

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| nhận sai hướng, **đo lại** thay vì bảo vệ kết luận cũ | tìm ra gốc thật, khác hẳn |
| đo shadow thật sự được gì | **1.666 lượt / 8,2 M token · tất cả đều có số, đều đã chấm** |
| soi bảng thăng hạng | 12.304 dòng — nhưng **3 cột quyết định để trống** |
| dựng **bảng xếp hạng chung đầu tiên** | 5 nguồn dương · 19 âm |
| làm **cờ ngữ cảnh thuần theo LANE** | 11/11 · official **bất biến từng byte** |
| ❌ neo `FINAL` báo `DRIFT` | **giả** — là bundle MN hôm nay; đã vá cổng |
| 🟢 cổng commit chặn agent | **đúng** — commit `V11152` thiếu bốn mặt |

### Gốc thật, một dòng

**Tiền không bị đốt vì shadow vô ích — mà vì `output_counterfactual_rank` NULL 12.304/12.304 dòng,
`cost_est` = 0, và 2.659 lời đề cử `PROMOTION_CANDIDATE` không đường nào đọc.**

Verdict **được GHI** mà **không ai ĐỌC** — `RM-20` ở chiều ngược lại.

---

## 3 · Vấp trong phiên — ba lần

**🔴 ① Agent đặt sai vấn đề, owner phải chỉnh.** Đây là vấp **nặng nhất** của phiên, và nó
không phải lỗi kỹ thuật — là lỗi **đọc sai ý định**. Con số `V11151` đo (94/94 lượt shadow,
0 lá phiếu) **đúng**; câu kết luận rút ra từ nó (**«nên dừng»**) **sai**.

Bài học ghi lại: một nguồn **không có ảnh hưởng** thì có hai cách đọc — *«bỏ đi cho đỡ tốn»*
hoặc *«chưa được cho cơ hội ảnh hưởng»*. Agent chọn cách thứ nhất mà **không hỏi dữ liệu xem
cách thứ hai có đúng không**. Dữ liệu, khi đo, nói cách thứ hai.

**🟡 ② Neo `FINAL` báo `DRIFT` giả.** Chạy lại neo sáng 02/09 ⇒ `DRIFT`. Điều tra: **dòng thứ
559** — bundle MN hôm nay, cron sinh `05:21:13`. **558 dòng cũ khớp hash từng byte**, và **0**
dòng cũ có `updated_at` sau mốc chụp.

Lỗi ở **dụng cụ**: bản nháp băm **cả bảng**, nên **mọi ngày mới đều đọc thành drift**. Owner đã
cảnh báo trước ở mục `II`: *«không được diễn giải "hash bất biến" thành dữ liệu tự động bất biến
mãi mãi»*. Nếu báo thẳng cho owner thì đã là **báo động sai lần thứ ba** trong hai ngày.

**🟢 ③ Cổng commit chặn agent — và chặn đúng.** Commit `0d1e0e7` đặt nhãn `V11152` mà chưa ghi
bốn mặt. Cổng `_v11062` chặn: `K1: V11152 không có dòng HISTORY`. Đã ghi đủ rồi commit lại.
**Ghi lại để không ai đi gỡ cổng này** — nó vừa bắt đúng một lỗi thật.

Kèm một chi tiết vận hành: hook `PreToolUse` chặn **cả lệnh ghép**, nên gộp `bump` + `git commit`
trong một dòng thì `bump` **không kịp chạy**. Phải tách hai bước.

---

## 4 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 **không bị đụng** · `PID 3156545` · không restart |
| `FINAL` cũ | 🟢 **`FINAL_ANCHOR_INTACT`** — 558 dòng bất biến, +1 dòng mọc bình thường |
| official prompt | 🟢 **bất biến từng byte** — cờ mặc định `off` |
| lane shadow | 🟢 `CONTEXT_ONLY_PASS` ×3 miền khi đặt chế độ `shadow` |
| việc 1/4 owner nêu | 🟢 **xong** — prompt ngữ cảnh thuần chạy được trên shadow |
| việc 2–4 | ⚪ `counterfactual_rank` · `cost_est` · phán quyết vòng đời |
| owner gate | **KHÔNG chạm** |

---

TanPhatAI cần làm: ghi **`V11152`** — riêng `0d1e0e7` + `902afc8`, công khai bản này. **Không deploy**, official chưa đổi một ký tự. Ghi **owner BÁC BỎ kết luận «dừng shadow» của `V11151`** — đây là **mệnh lệnh trực tiếp**; tài liệu nào còn nói *«cắt shadow cho đỡ tốn»* thì **tài liệu phải sửa**. Ghi **gốc thật**: `output_counterfactual_rank` **NULL 12.304/12.304**, `cost_est` **0**, **2.659 `PROMOTION_CANDIDATE` không ai đọc** — verdict được GHI mà không ai ĐỌC. Ghi **bảng xếp hạng chung đầu tiên** 5 dương / 19 âm, **CHƯA phải phán quyết** (`RM-04`); và **số âm của `glm-5.1`/`gpt-oss-120b` là dòng TRƯỚC khi thăng hạng 01/08**, đừng đọc thành «official đang kéo xuống». Ghi **cờ theo lane 11/11**, phép nặng nhất **official bất biến từng byte**. Ghi **neo `FINAL` báo `DRIFT` GIẢ** — dòng thứ 559 là bundle MN hôm nay. Ghi **cổng commit `_v11062` chặn đúng một lỗi thật của agent — đừng gỡ**. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
