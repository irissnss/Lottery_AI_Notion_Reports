# CONVERSATION CONTEXT — V11163 · 04/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `CURRENT_ACTOR = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 04/09 ~01:3x | *«Tiếp tục đi e»* | `YÊU_CẦU` | diễn tập migration + gói đề xuất A/B/C | `ĐÃ_LÀM` |

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| diễn tập migration trên bản sao | 🟢 ghi 0,04s · idempotent · rollback 0,03s · `integrity ok` |
| đo rủi ro partial-population | 🔴 chỉ **12,3%** phủ · `NULL` mang **hai nghĩa lẫn nhau** |
| tìm va chạm writer | 🔴 writer hằng giờ truyền `None` **vô điều kiện** ⇒ xoá sạch <1 giờ |
| quét reader | 🔴 **không reader nào** đọc cột ⇒ đổ vào không mở khoá việc gì |
| gói đề xuất 12 mục | 🟢 `docs/DE_XUAT_MATERIALIZATION_V11163.md` · ba lựa chọn A/B/C |

---

## 3 · Điều đáng nói nhất — agent lật ngược đề xuất của chính mình

Cuối `V11159` agent đề xuất *«materialize `output_counterfactual_rank` vào production»* và ghi nó
vào mục theo dõi. Diễn tập cho ra khuyến nghị **ngược lại**.

Điều quan trọng: **kỹ thuật hoàn toàn sạch** — ghi `0,04s`, idempotent, rollback `0,03s`,
`integrity ok`. Nếu chỉ nhìn kỹ thuật thì đây là một migration dễ, và agent đã có thể làm rồi báo
*«xong»*. Cái chặn nằm ở **ngữ nghĩa**: cột sẽ có `NULL` mang hai nghĩa, và writer hằng giờ sẽ xoá
sạch. **Không diễn tập thì không thấy.**

Đây là lý do mục `XVI` của owner bắt phải có **rehearsal** trước — và lần này nó cứu đúng một
quyết định sai.

---

## 4 · Một việc agent CHỦ ĐỘNG KHÔNG làm

`V11162` phát hiện `scheduler._restore_stdio` trả lại **chính luồng stdout hỏng** ⇒ hỏng một lần
là câm vĩnh viễn. Nghe như một bug đáng sửa.

Agent **không sửa**: đo được **0 dòng lỗi I/O** trong journal ⇒ nhánh đó **chưa từng chạy**. Sửa
một nhánh chưa bao giờ nổ là đổi hành vi scheduler để đối phó với giả định, và bản thân việc đó
mới là rủi ro. Ghi lại đầy đủ để người sau quyết, không tự quyết thay.

---

## 5 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 **0 ghi · 0 deploy** · `output_counterfactual_rank` vẫn `0/17.040` |
| gói đề xuất | 🟡 **CHỜ OWNER** chọn A / B / C |
| `POOL_VERDICT` | **`HOLD`** |
| Prompt 43 R1 | **`PARTIAL`** |

---

TanPhatAI cần làm: ghi **`V11163`** — `governance_seq 479`, công khai bản này. Ghi **agent lật ngược đề xuất của chính mình bằng diễn tập**, và ghi rõ **kỹ thuật thì sạch — cái chặn nằm ở ngữ nghĩa**, nên nếu chỉ nhìn kỹ thuật thì đã làm sai rồi báo «xong». Ghi **mục `XVI` của owner (bắt buộc rehearsal) lần này cứu đúng một quyết định sai**. Ghi **agent chủ động KHÔNG sửa** rủi ro `_safe_stdio_ctx` và nêu lý do. **Code KHÔNG đi trước tài liệu** — bốn mặt ghi cùng phiên, 0 dòng production bị ghi. **Không mở FU mới. Không mở Prompt 44.**
