# CONVERSATION_CONTEXT V11081 — 17/08/2026

## Owner nói gì (NGUYÊN VĂN)

> *"Chạy tiếp prompt đi em, file đính kèm trong link em xem nhé
> `E:\Lottery_AI_Test\GOI_BAN_GIAO_REPO_20260816`"*

> *"Đồng thời trả giải đáp nghi vấn «V11077 · V11078 · V11079 có tồn tại không, và vì sao không
> có báo cáo công khai?» ==> anh nghĩ đang có 1 seccsion khác đang làm việc chắc là chiếm số này
> đó em, secsion đó đã truy quết từ 21h tới giờ vẫn chưa xong ah em. nên chưa có commit báo cáo
> ah em. em có thể tìm hiểu thêm nhé."*

---

## Agent làm gì

1. Đọc gói bàn giao 10 file — **đúng năm file `INPUT_EVIDENCE`** mà V11080 ghi là không tìm thấy.
2. **Thay `LUAT_CHUNG.md`** bằng bản phát hành chính thức (QĐ-E cấm sửa tay bản sao).
3. **I2** — mở rộng `_v11027_so_muc_quan_tri.py` thêm mốc hiệu lực (`DC-20260816/B1`, `B2`).
4. **I3 + I5** — dựng `_v11080_i3i5_chan_lan_du_an.py`.
5. **I4** — thêm **đúng một** phép vào `_v10921_report_gate.py`.
6. **Vá chỗ mù** `phien_ban_gan_day()`: hợp `CHANGELOG ∪ git log`.
7. Nâng version **V11081** qua `_v11062_nang_version.ghi()`.

---

## Vấp ở đâu — ghi thật, không giấu

### 1. Bài thử I2 TỰ CHO MÌNH ĐIỂM

Bài thử in *"khôi phục nguyên trạng ✓ khớp từng byte"* — **sai**. Nó đọc `.cursorrules` bằng
`io.open(...encoding=...)` rồi ghi lại bằng text mode; text mode bật **universal-newlines**, nên
phép so *"đọc lại == bản gốc"* so **văn bản đã giải mã**, không so **byte**. File thật bị đổi
**CRLF → LF** trên cả **674 dòng**.

**Phát hiện nhờ nguồn thứ hai:** `git status --porcelain .cursorrules` → `" M"` ngay sau khi thử
xong. Nếu chỉ tin bài thử thì đã commit một cổng "đạt" mà nó vừa làm bẩn repo.

Sửa: đọc/ghi **nhị phân**. Kiểm bằng **hai nguồn độc lập** (bài thử **và** `git`).

### 2. I2 so bằng nguyên văn tiêu đề — 6 báo động giả

Lần chạy đầu báo **6 điều mới thiếu mặt**. Sai: cùng một điều luật được viết **khác chữ** ở các
mặt khác nhau, và đó là **cố ý** (`.AGENT.md` là hợp đồng tiếng Anh, đánh số theo bộ riêng):

```
CLAUDE.md   ## §62 (A60) — NGUỒN BA LỚP: OWNER_SAID · CODE_DID · DOC_SAID
.AGENT.md   ## §62 (A60) — THREE-LAYER SOURCING: OWNER_SAID · CODE_DID …
.AGENT.md   ## 11. VERSION BUMP — FOUR SURFACES MOVE TOGETHER (§63 / A61)
```

Đúng lỗi `RM-09` / `A58_VIOLATION_RAW_COUNT`. **Và tệ hơn:** nếu để nguyên, cổng sẽ **đẩy agent
đi chép cho bằng chữ** — tức **đi gom**, đúng việc `DC-20260816/B1` vừa cấm. Một cổng sai có thể
**ép người ta phạm luật mà nó đang bảo vệ**.

Sửa: `_khoa()` rút **số hiệu**, dò cả trong **thân** tiêu đề. **6 → 2 → 0**.

### 3. I3 dương tính giả ở chính bản luật chung

Bắt `LUAT_CHUNG.md:105` `SCOPE: RIÊNG <dự án>` — đó là **chỗ mẫu** trong văn bản **định nghĩa cú
pháp nhãn**. Đếm nó thành vi phạm sẽ bắt agent đi *"sửa"* bản luật chung — thứ **QĐ-E cấm sửa
tay**. Sửa: lọc dạng `<...>`.

### 4. Nhãn commit `V11080b` bị cổng hiểu thành một bản riêng

Sau khi vá `phien_ban_gan_day()`, cổng đọc `git log` và bắt `V11080B` như một version thiếu báo
cáo. Nhưng `V11080b` chỉ là **nhãn commit phụ** cùng một bản — trong khi `V10964b` **là bản riêng
thật** (có mục CHANGELOG riêng). Phân biệt bằng đúng điều đó: hậu tố chữ chỉ tính là bản riêng
**khi có mục CHANGELOG riêng**. Không lọc thì mỗi commit phụ bị đòi một báo cáo ⇒ báo động giả,
và agent sẽ **chế báo cáo rỗng cho đủ**.

---

## Điều KHÔNG làm và vì sao

- **Không tự viết báo cáo cho V11077/V11079.** Em không biết hai bản đó làm gì ngoài dòng commit.
  Soạn báo cáo từ suy đoán là **chế dữ liệu** (`RM-17`) — đúng thứ đã làm hỏng con số *"84/84"*.
- **Không làm GĐ-3** (đổi tiền tố namespace). Sót một matcher dò `§` sẽ làm cổng A5x/A6x **mù im
  lặng** — đúng cảnh `RM-15`. Còn vướng đóng băng `QD-041` tới 21/08.
- **Không ghi "mọi cổng xanh".** `_v10921_report_gate` **còn trượt** vì V11077/V11079 — đó là
  **kết quả đúng** của cổng vừa vá, không phải thứ cần che.
- **Không đụng** đường dự đoán/chọn số/prompt model · DB · Notion (chỉ đọc) · không deploy.
