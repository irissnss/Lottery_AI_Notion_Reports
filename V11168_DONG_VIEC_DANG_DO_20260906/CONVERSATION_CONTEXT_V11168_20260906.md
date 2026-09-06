# CONVERSATION CONTEXT — V11168 · 06/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `CURRENT_ACTOR = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| ~09:2x | *«Các agent được điều đi trước đó có còn cần thiết không. Do fable hút Token quá nên có vẻ gián đoạn em rà soát điều tiếp theo với các agent model nhẹ hơn để làm tiếp các việc còn dang dở chưa xác định cần tìm hiểu nha e»* | `YÊU_CẦU` | Gom **131 mục dang dở** từ V11165–V11166; chạy 5 cổng (4 Sonnet + 1 Haiku) | `ĐÃ_LÀM` |

**Trả lời trực tiếp:** 16 workflow cũ **đều đã chết**, cái im lâu nhất 11 ngày, **không còn tốn
token**. Không cần chạy lại cái nào.

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| model nhẹ | 5 agent · **1,04 triệu token** · 23 phút · 0 lỗi |
| việc dang dở | **16/28 đóng · 11 treo · 1 không đáng làm** |
| phân loại 131 mục | 22 đã giải quyết · 91 cần bằng chứng · 6 cần owner · 6 cần công cụ · 4 bỏ |
| production | **0 ghi · 0 deploy · 0 restart** |

---

## 3 · Điều đáng nói nhất — phần lớn báo động là hạ nhiệt

Trong 16 mục đóng được, **6 mục khi đo thật thì không phải lỗi**: mâu thuẫn cấu trúc **chưa bao giờ
xảy ra** (0/271 bundle) · «rò rỉ» bị chặn bởi một cờ (`lane_test_shadow_pack`) · «vượt timeout» là
**retry có chủ ý** · trộn regime chỉ **1/31 ngày** · reasoning 96% **chưa từng gây hỏng** ·
«chỉ 2 cổng» thật ra là **10 cổng**.

**Bài học:** một danh sách «việc dang dở» dài không có nghĩa là hệ nhiều lỗi — nó có nghĩa là
**nhiều thứ chưa ai đi đo**. Đo xong thì phần lớn tự tan.

---

## 4 · Điều đáng nói thứ hai — một mục đổi bản chất

**79 bundle** (không phải 78 — RM-11) có `bach_thu` ≠ `ranked_numbers[0]`. **Không phải lỗi tính.**
50/79 là **override hợp lệ owner đã duyệt**. Lỗi thật: **`main_selection_reason` khoá cứng** ở
`main.py:10379` ⇒ **không ai biết cơ chế nào đã quyết định số cuối cùng**.

---

## 5 · Vấp ở đâu

| # | vấp | gỡ |
|---|---|---|
| 1 | **Đếm chuỗi thô ra «184/271»** — `model_wr/model_bt` liệt kê cả 27 model theo dõi, không phải danh sách bỏ phiếu | đọc đúng `ranked_numbers[*].voters` → **0/271**. RM-09/RM-10 |
| 2 | **Đề bài của chính agent ghi «10 lượt»** — số thật **9** | sửa khi trích lại |

---

## 6 · Cho TanPhatAI đọc tiếp

**Bốn con số dễ bị trích sai:** «78 bundle» → **79** · «184/271» → **0/271** ·
«chỉ 2 cổng có sổ điểm danh» → **10 cổng** chứng minh được đã chạy · «10 lượt» → **9**.

**Năm P0 hạ tầng của V11166 vẫn nguyên.**

---

TanPhatAI cần làm: ghi **`V11168`** — công khai bản này cùng `REPORT_V11168.md`. Ghi **16/28 việc dang dở đóng được bằng 5 agent model nhẹ (1,04 triệu token)**, và **phần lớn là BÁO ĐỘNG HẠ NHIỆT** — 6 mục đo thật thì không phải lỗi. Ghi **79 bundle (không phải 78) đổi bản chất: 50/79 là override HỢP LỆ, lỗi thật là `main_selection_reason` khoá cứng ⇒ LỖ HỔNG PROVENANCE**. Ghi **4 tệp shadow tự định nghĩa lại `DEGRADED_LIVE_DAY`**. Ghi **agent tự bắt bẫy đếm-chuỗi-thô của chính nó**. **Code KHÔNG đi trước tài liệu** — 0 ghi production. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.**
