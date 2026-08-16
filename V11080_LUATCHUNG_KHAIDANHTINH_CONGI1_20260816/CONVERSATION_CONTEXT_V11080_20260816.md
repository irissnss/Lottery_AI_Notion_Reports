# CONVERSATION_CONTEXT V11080 — 16/08/2026 đêm

## Owner nói gì (NGUYÊN VĂN, từ prompt tổng lực lần 15)

> *"PROMPT TỔNG LỰC LẦN 15 — NÂNG CẤP TOÀN DIỆN LUẬT CHUNG + LUẬT RIÊNG (16/08/2026 đêm — THAY
> THẾ hoàn toàn prompt lần 14, lần 14 = VOID)"*

**Năm quyết định owner khoá, KHÔNG hỏi lại:**

> **QĐ-A (21:57):** *"sổ sai lầm RM GIỮ NGUYÊN cả bối cảnh — nhóm an toàn, TUYỆT ĐỐI không
> tách/cắt gọn khỏi file nạp gốc."*

> **QĐ-B (21:57):** *"tách namespace «§» — HỆ QUẢN TRỊ đổi tiền tố (đề xuất «Đ-» hoặc «L-»); hệ
> prompt MODEL giữ nguyên (đang production). Quét + đổi toàn bộ tham chiếu trong các bản luật và
> script đọc luật; CẤM đụng chuỗi «§» trong code bơm prompt model."*

> **QĐ-C (21:57):** *"GOV-RULEFILE-IDENTITY-001 — dòng ĐẦU mọi file luật gốc khai: tên dự án ·
> vai trò bản này · kiến trúc (có nguồn: CLAUDE.md là nguồn của AGENTS.md/GEMINI.md) · cách sửa.
> Bản sinh nhận qua bộ sinh, CẤM sửa tay bản sinh."*

> **QĐ-D (22:01):** *"kế thừa luật chung — file luật dự án = dòng khai danh tính + một dòng kế
> thừa trỏ LUAT_CHUNG.md (kèm Doc Version) + phần RIÊNG. CẤM chép lặp luật chung. Ngoại lệ: nhóm
> an toàn inline."*

> **QĐ-E (22:35):** *"mọi dự án ĐỌC ĐƯỢC Notion qua MCP (chỉ đọc — Notion là tài liệu). SSOT luật
> chung nằm trên Notion; LUAT_CHUNG.md trong repo là bản sao tiện đọc — hai nơi phải khớp Doc
> Version, lệch thì SSOT Notion thắng. CẤM sửa tay bản sao trong repo."*

**Owner yêu cầu in 6 dòng xác nhận đọc hiểu trước khi làm.** Đã in đủ 6 dòng.

---

## Agent làm gì

1. **GĐ-0 đo trước (read-only)** — 5 bảng đo. Chạy `_v10920_session_start.py`,
   `_v11027_kiem_cheo_6_mat.py`, quét `§` có phân loại, kiểm kê hook từng công cụ.
2. **GĐ-1** — viết `LUAT_CHUNG.md` từ SSOT Notion; thêm 2 dòng khai vào 5 mặt sửa tay; sửa bộ
   sinh để 2 mặt sinh nhận 2 dòng đó **và** mang theo bảng quy hoạch sáu mặt.
3. **GĐ-2/I1** — dựng `_v11080_i1_cong_tu_kiem.py`, thử chặn hai chiều, vá
   `code_quality_guard`.
4. **Nâng version** qua `_v11062_nang_version.ghi()`, số hiệu lấy từ `_v11044_cong_so_hieu.py`.

---

## Vấp ở đâu — ghi thật

### 1. Sáu file INPUT_EVIDENCE của prompt KHÔNG có trong repo

Prompt liệt kê 6 file phải đọc trước. Tìm cả repo + `~/Downloads` + `~/Desktop`: **không có file
nào trong 5 file đầu**. Chỉ `CLAUDE.md` (mục 6) là có thật.

**Xử lý:** theo QĐ-E, SSOT luật chung nằm trên Notion ⇒ đọc thẳng SSOT qua MCP (chỉ đọc), tìm ra
trang *🧭 Hướng Dẫn TanPhatAI V4.0* (`HDAI-V4.0.35`) chứa đúng §13.7/13.8/13.9. `LUAT_CHUNG.md`
dựng từ nguồn đó.
**Còn thiếu:** `NC-20260816-I v2` (năm cổng I1–I5), `DC-20260816` (B1–B5/C1–C4),
`03_RIENG_DU_AN_LOTTERY.md`, `LUAT_TONG_HOP_LOTTERY_20260816.md`. Các mục I1–I5 dựng theo **mô tả
trong prompt owner**, không theo bản gốc — đã ghi rõ ở mục 7 báo cáo.

### 2. Mẹo commit trong CLAUDE.md không dùng được ở môi trường này

`CLAUDE.md` dạy *"bọc `git commit -m` trong file `.cmd`, chạy `cmd /c <batch>`"* — viết cho
**PowerShell**. Ghi `.cmd` bằng heredoc của **Bash** cho ra kết thúc dòng **LF**; `cmd` không
thực thi được, treo hết 2 phút rồi rơi (lần đầu tưởng cổng hook chậm).
**Cách chạy được:** `git commit -F <file thông điệp>` thẳng trong Bash.

### 3. Suýt báo nhầm `code_quality_guard` thành "phát hiện lỗi chất lượng code"

Giữa phiên guard trả `permission: deny` với nhãn *"chấm ngày D bằng tensor ngày D"*. **Không kết
luận vội** — đo lại `_v11050_kiem_bien_anchor` riêng: **nguội 97,4s · ấm 9,6s**, `rc=0`, cổng
báo `BIEN_ANCHOR_V11050=DAT`. Tức `deny` kia là **hết giờ 150s lúc chạy nguội**, không phải phát
hiện thật. Chạy lại guard: **90.358 ms**, `permission=allow`.
*(Đúng tinh thần RM-13: nguồn sai thì mọi kết luận sai.)*

### 4. Quét `§` thô cho kết quả sai lệch — phải phân loại lại

Lần quét đầu báo *"32 số hiệu dùng ở CẢ HAI hệ"* vì đếm mọi `§` trong `web/backend/**/*.py` —
gộp cả **script quản trị** (trích luật quản trị, vô hại) lẫn **file dựng prompt**. Đúng lỗi
**RM-09 / `A58_VIOLATION_RAW_COUNT`**. Quét lại có phân loại
(`TRONG_PROMPT` / `GHI_VAO_PROMPT` / `CODE` / `CHU_THICH`): con số thật là **hệ prompt model dùng
§1–§26**, va với hệ quản trị **18 số hiệu**.

---

## Điều KHÔNG làm và vì sao

- **GĐ-3 (đổi tiền tố namespace) — KHÔNG làm.** Đổi tiền tố mà sót một matcher dò chuỗi `§` sẽ
  làm cổng `A5x`/`A6x` **mù im lặng** — đúng cảnh RM-15 (`git log --since` trả rỗng nên cổng luôn
  báo xanh từ lúc dựng). §60: *"bỏ nửa chừng còn tệ hơn không làm"*.
- **I2 · I3 · I4 · I5 · GĐ-4 · GĐ-5 — KHÔNG làm.** Khối lượng vượt một phiên. Ghi thẳng là thiếu
  (§63), không ghi khống.
- **Không đụng** đường dự đoán/chọn số/prompt model (QD-041 tới 21/08) · không đụng DB · không
  ghi Notion · không deploy.
