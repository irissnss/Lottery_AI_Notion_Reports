# CONVERSATION CONTEXT — V11169 · 06/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `CURRENT_ACTOR = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| ~10:0x | *«còn gì nữa ko tiếp tục đi em»* | `YÊU_CẦU` | Kiểm ngày live 06/09; chạy 5 cổng Sonnet; chạy lại 2 cổng hỏng schema | `ĐÃ_LÀM` |

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| model nhẹ | 7 agent Sonnet · **1,72 triệu token** |
| đóng mục | **7/13** · `OWNER_APPROVAL_PACKET` **33 KB** |
| rút lại | 🔴 **`R24`** — «73/79» không tái lập được, số đúng **64/79** |
| production | **0 ghi · 0 deploy · 0 restart** |

---

## 3 · Điều đáng nói nhất — agent rút lại con số của chính phiên trước

Phiên trước báo *«73/79 = 92,4% mismatch đã giải thích được»*. Phiên này đo **độc lập** ra
**64/79 = 81,0%**. Agent **rút lại ngay** thay vì im lặng dùng số cũ, và ghi rõ **không tìm thấy
quyết định owner nào đã dựa vào «73/79»**.

Đáng nói hơn: agent **tự bắt lỗi phương pháp trước khi báo** — lần chạy đầu patch
`sqlite3.connect` **toàn cục** gây **đệ quy vô hạn**, ra `0/79`. Sửa bằng cách vô hiệu hoá **đúng
ba hàm** `_log`/`_log_shadow` thay vì patch toàn cục.

---

## 4 · Điều đáng nói thứ hai — «cơ chế thứ 5» chỉ là nhầm phạm vi

`_v10640_official_perslice_override.py` được báo cáo trước ghi là **«chỉ MN»**. Thực tế nó điều
khiển **cả MT và MB** từ 31/05 đến 01/08 — **trước cả** V10767/89/90.

Kèm phát hiện phụ nghiêm túc: bảng audit `v10767_mb_prevday_shadow` **chứa dữ liệu backfill sai**
(ghi 5–7 ngày sau ngày chạy thật) ⇒ **không dùng được làm bằng chứng**.

---

## 5 · Điều đáng nói thứ ba — thiên lệch có hệ thống theo hướng làm đẹp

**4 tệp shadow lệch sổ chính 153/270 dòng, và 149/153 = 97,4% lệch theo MỘT hướng duy nhất:**
shadow báo `VALID_LIVE_DAY` trong khi sổ chính ghi `DEGRADED_LIVE_DAY`.

**Không phải nhiễu ngẫu nhiên.** Nếu là nhiễu thì phải lệch cả hai chiều.

---

## 6 · Vấp ở đâu

| # | vấp | gỡ |
|---|---|---|
| 1 | 🔴 **Trích «73/79» mà không tái lập được** | rút lại `R24`, dùng **64/79** |
| 2 | **Patch `sqlite3.connect` toàn cục** → đệ quy vô hạn, ra `0/79` | no-op **đúng ba hàm** thay vì patch toàn cục |
| 3 | **Công thức nền bạch thủ dùng `1/D2`** — sai | sửa `D2/100`, khớp **34,0%** đã công bố |
| 4 | **Một cổng trả rỗng** do `StructuredOutput retry cap` | chạy lại với schema đơn giản hơn, **2/2 thành công** |
| 5 | **Gộp tỉ lệ token theo provider** — sai, phương sai *trong* provider gấp 5 lần | đổi sang đơn vị **model** (RM-21) |

---

## 7 · Cho TanPhatAI đọc tiếp

**Việc rẻ nhất và có lợi nhất:** duyệt **mục A** của `OWNER_APPROVAL_PACKET` — đánh dấu 91 bundle
backfill **gần như miễn phí** vì **90/91 vẫn còn nguyên dấu `notes='Phase 1.5 backfill'`**, chỉ cần
một `SELECT`, không cần `ALTER`/`UPDATE`.

**Bốn con số dễ bị trích sai:**
- «73/79» → **64/79** (đã rút `R24`)
- «cơ chế thứ 5» → **không tồn tại**, là nhầm phạm vi `_v10640`
- `v10767_mb_prevday_shadow` → **chứa backfill sai**, không dùng làm bằng chứng
- `model_latency_shadow_v11063` → **snapshot tĩnh**, không phải dữ liệu sống

**`t10_chot` chỉ có độ phân giải PHÚT** — mọi câu hỏi về biên an toàn tính bằng giây đều không trả
lời được từ nguồn đó, và **`final_bundles.created_at` cũng không dùng được** (`RL-018`).

---

TanPhatAI cần làm: ghi **`V11169`** — `governance_seq 484`, công khai bản này cùng `REPORT_V11169.md` và `OWNER_APPROVAL_PACKET.md`. Ghi **RÚT LẠI `R24`: «73/79» không tái lập được, số đúng 64/79 (81,0%)** — agent rút lại thay vì im lặng dùng số cũ. Ghi **«cơ chế thứ 5» KHÔNG tồn tại, là vụ nhầm phạm vi `_v10640`** (thực tế điều khiển cả ba miền từ 31/05). Ghi **bảng audit `v10767_mb_prevday_shadow` chứa BACKFILL SAI**. Ghi **MN 14 model là RACE CONDITION 3 giây, KHÔNG phải lỗi kế toán MT**. Ghi **4 tệp shadow lệch 153/270 dòng, 97,4% theo MỘT hướng LÀM ĐẸP số liệu** — thiên lệch có hệ thống. Ghi **biên an toàn MN từng = 0 GIÂY trong 26/62 ngày**, đã sửa từ 01/08. Ghi **đếm token đóng 6 mục mà không cài gì**, `token_count` là **`total_tokens`** chứ không phải `prompt_tokens`. Ghi **RNG KHÔNG gieo hạt** ⇒ mọi so sánh trước/sau retrain đang trộn nhiễu. Ghi **91 bundle backfill đánh dấu gần như MIỄN PHÍ** (90/91 còn nguyên dấu). **Code KHÔNG đi trước tài liệu** — 0 ghi production. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.**
