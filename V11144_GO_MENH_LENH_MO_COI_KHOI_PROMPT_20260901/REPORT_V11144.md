# REPORT V11144 — GỠ HAI MỆNH LỆNH MỒ CÔI KHỎI PROMPT · cổng của chính dự án đổi từ **CHẶN** sang **ĐẠT**

> **Ngày:** 01/09/2026 · `ACTOR_RUNTIME = CLAUDE_CODE` · **Commit riêng:** `8a7a677`
> **Phiên:** 31/08 – 01/09/2026, owner tương tác liên tục trong IDE.

---

## 1 · Tóm tắt

Cổng `_v11107_cong_prompt_mo_coi.py` **của chính dự án** đang **CHẶN** với mã
`PRJ_PROMPT_DANGLING`, treo từ **23/08**. Bản này xử dứt điểm: gỡ hai câu lệnh trỏ vào hai khối
dữ liệu **đã bị gỡ từ trước**. Cổng chuyển **CHẶN → ĐẠT**, đo trên **prompt đang serve của
production**.

---

## 2 · Owner yêu cầu gì — nguyên văn

> **01/09 ~11:10** — *«làm tiếp đi em, vấn đề nào đã xác định, nằm trong khả năng là xử lý dứt
> điểm đi, push báo cáo tổng hợp tổng lực, gom tổng hợp tồn đọng cấm để nợ phình lớn mất kiểm
> soát…»*

Bảng **11 câu nguyên văn** của owner trong phiên và ba mệnh lệnh `OWNER-01/02/03` nằm ở
`CONVERSATION_CONTEXT` cùng thư mục và `docs/SO_TUONG_TAC_OWNER.md`.

⚠️ **TanPhatAI:** owner trao đổi liên tục trong IDE nên **code thường đi trước tài liệu** — đó là
điều owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`). Tài liệu cũ mâu thuẫn thực tế thì
**thực tế + sổ tương tác thắng**.

---

## 3 · Đào bới / phát hiện

### Đo trên PROMPT ĐANG SERVE, không đọc tài liệu (`RM-14`)

Chạy cổng **trên VPS** — không phải local. Bản chạy local trước đó thổi lên **5** câu mồ côi vì
máy local thiếu dữ liệu, đúng khuôn `RM-13` (nguồn sai thì mọi kết luận sai):

```
cỡ prompt đang serve: MN=34.693 · MT=34.341 · MB=39.674
câu điều kiện-có-mặt: MỒ CÔI=2 · LỆCH MIỀN=1 · CÓ MẶT=5

🔴 MỒ CÔI «BT MODEL RANKING»   REASONING_RULEBOOK:255 — KHÔNG có ở miền nào
🔴 MỒ CÔI «WEEKLY LIVINGNESS»  REASONING_RULEBOOK:256 — KHÔNG có ở miền nào
```

**Đúng 2, không phải 5.** Đây chính là lý do bắt buộc chạy cổng trên nguồn production.

### Hai câu bị gỡ

```
- Khi Context Pack có "BT MODEL RANKING"  → tham khảo model nào mạnh BT nhất, ưu tiên evidence…
- Khi Context Pack có "WEEKLY LIVINGNESS" → chỉ tin tưởng rules ACTIVE/SUPPORT, bỏ qua SHADOW/DROP
```

### Vì sao hai khối đó không còn — **mỗi cái hai neo độc lập**

**`WEEKLY LIVINGNESS`** — `gpt_analyzer.py:4939` ép cứng `_live_rows = []` từ `V11014` (07/08),
kèm lý do đo được: khối trùng **60%** tập số với `MINED RULES` ngay trên và **80%** với
`EVIDENCE TABLE` ngay dưới. Sau đó `if _live_rows:` **không bao giờ vào**.
⇒ neo ① mã ép cứng · neo ② dump production vắng ở **cả ba miền**.

**`BT MODEL RANKING`** — writer **không** bị tắt cứng (`:4681` vẫn có thể append), nhưng
`_deherd_strip_ranking()` (`:4354-4366`) cắt **VÔ ĐIỀU KIỆN** mọi mục `### ` có chuỗi
`BT MODEL RANKING`, từ tiêu đề tới `### ` kế tiếp — khoá ở `_V10768_HERD_SECTION_KEYS:4351`.
⇒ neo ① cắt vô điều kiện theo tiêu đề · neo ② dump production vắng ở **cả ba miền**.

### Một kết quả âm cần ghi

`🟡 LỆCH MIỀN «🎯 RULE TAILS» — chỉ có ở ['MT','MB']`. Cổng **báo, không chặn** — có thể đúng
thiết kế (khối riêng miền). **Chưa xác minh**, ghi lại để phiên sau không tưởng là mới.

---

## 4 · Hướng xử lý và vì sao chọn

### Vì sao đây KHÔNG phải đổi cơ chế

Cả hai là câu **ĐIỀU KIỆN** — *«Khi Context Pack CÓ …»* — mà điều kiện **không bao giờ đúng**.
Gỡ đi là **bỏ nhiễu**, không đổi luật chọn số.

Ngược lại, **giữ chúng mới nguy**: §60.1 — *«gỡ dữ liệu mà để lại câu lệnh trỏ vào nó thì model
được bảo dùng một thứ không tồn tại, và nó sẽ TỰ BỊA RA»*.

### Vì sao xoá hẳn, không comment

Hai dòng nằm **bên trong** chuỗi `REASONING_RULEBOOK`, nên **không thể** comment bằng `#` — dấu
`#` sẽ thành **chữ trong prompt** gửi cho model. Chú thích lịch sử đặt **phía trên dòng định
nghĩa chuỗi**, tức ngoài chuỗi.

### Vì sao GIỮ hai writer

`:4681` và `:4942` là hai điểm ghi khối, **đang ngủ** (hai neo ở mục 3). Gỡ writer là một quyết
định khác — nếu sau này ai bật lại khối thì cần cả writer lẫn câu lệnh. Không gộp vào bản này.

---

## 5 · Đã làm gì — `TRƯỚC / SAU / PHIÊN BẢN / KIỂM` (§60.4)

```
TRƯỚC:  PROMPT_MO_COI = CHẶN · mã PRJ_PROMPT_DANGLING · MỒ CÔI=2
SAU:    PROMPT_MO_COI = ĐẠT  · MỒ CÔI=0 · LỆCH MIỀN=1 (báo, không chặn) · CÓ MẶT=5
PHIÊN BẢN: gpt_analyzer.py 0d2be3247abf → 4fc988bd2c23
        (−2 dòng prompt, +17 dòng chú thích) · backup .bak_v11144
        PID 3150475 → 3156545
KIỂM:   ast.parse hợp lệ · py_compile OK trên VPS · hash VPS khớp candidate
        cổng chạy TRÊN VPS: CHẶN → ĐẠT · 0 traceback · FINAL 09/2026 bất biến
```

**Cỡ prompt không đổi** (`MN 34.693 · MT 34.341 · MB 39.674` trước và sau) — **đúng**, vì con số
đó đo **context pack**, còn hai dòng vừa gỡ nằm trong hằng số `REASONING_RULEBOOK` riêng. Ghi rõ
để không ai đọc thành «vá không ăn».

### Quét ngược CÓ PHÂN LOẠI (§60.3) — không đếm chuỗi thô

| loại | số | xử |
|---|---|---|
| `TRONG_PROMPT` | **0** | ✅ sạch |
| `GHI_VAO_PROMPT` | 2 | **GIỮ** — hai writer đang ngủ (`:4681` · `:4942`) |
| `CODE` | 8 | giữ — `_v10959c_ab_status` · `_v11107_deploy_ctx187` · `_v10804_prompt_extract` |
| `CHÚ_THÍCH` | 7 | **GIỮ** — là bằng chứng đã làm |

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| `PROMPT_MO_COI` chạy **trên VPS** | ✅ **CHẶN → ĐẠT** · `MỒ CÔI 2 → 0` |
| `DEPLOY_V11144` (5 phép) | ✅ ĐẠT |
| `ast.parse` + `py_compile` trên VPS | ✅ ĐẠT |
| hash VPS khớp candidate | ✅ `4fc988bd2c23` |
| 0 traceback · FINAL 09/2026 bất biến | ✅ ĐẠT |
| `DONG_BO_NHANH` sau commit | ✅ ĐẠT — 5 tệp trọng yếu khớp git |

---

## 7 · Vướng vấp

**Bản chạy cổng ở LOCAL cho 5 câu mồ côi, production chỉ có 2.** Nếu tin bản local thì đã «vá»
ba câu đang hoạt động bình thường. Đây là `RM-13` ở dạng cụ thể: **prompt cũng phải dump từ nguồn
production**, y như DB.

**Cái bẫy `#` trong chuỗi:** suýt comment hai dòng thay vì xoá — dấu `#` sẽ thành chữ gửi cho
model, tức làm prompt **bẩn thêm** thay vì sạch đi.

---

## 8 · Gỡ về

```bash
sudo cp <BACKEND>/gpt_analyzer.py.bak_v11144 <BACKEND>/gpt_analyzer.py
sudo systemctl restart lottery
```

---

## 9 · Theo dõi tiếp

| # | việc | trạng thái |
|---|---|---|
| 1 | `🎯 RULE TAILS` chỉ có ở MT/MB | ⚪ **chưa xác minh** là thiết kế hay lỗi |
| 2 | Hai writer đang ngủ (`:4681` · `:4942`) | ⚪ giữ — quyết định riêng nếu muốn gỡ hẳn |
| 3 | `_v11107` chạy ở local cho kết quả sai | ⚪ nên chặn không cho chạy local, hoặc in cảnh báo |

---

## 10 · Nguồn ba lớp (§62)

### `OWNER_SAID`
*«vấn đề nào đã xác định, nằm trong khả năng là xử lý dứt điểm đi»* (01/09 ~11:10). Đủ 11 câu
nguyên văn ở `CONVERSATION_CONTEXT` cùng thư mục và `docs/SO_TUONG_TAC_OWNER.md`.

### `CODE_DID`
`gpt_analyzer.py` `0d2be3247abf → 4fc988bd2c23` · `PID 3150475 → 3156545` · cổng
`_v11107_cong_prompt_mo_coi.py` chạy **trên VPS** đổi từ `CHẶN` sang `ĐẠT` · commit `8a7a677`.

### `DOC_SAID`
`CHANGELOG.md §V11144` · `docs/CURRENT_TRUTH_SSOT.md §V11144` ·
`docs/AUTOMATION_HISTORY.jsonl` dòng `V11144`.

### Ba lớp lệch nhau
`DOC_SAID` ≠ `CODE_DID` **trước bản này**: `_v11107_cong_prompt_mo_coi.py:11-12` đã **ghi tên**
hai câu mồ côi từ 23/08, nhưng mã vẫn giữ chúng — tài liệu biết, code chưa sửa, suốt **9 ngày**.

---

TanPhatAI cần làm: ghi **cổng `PROMPT_MO_COI` đổi từ CHẶN sang ĐẠT** — hai mệnh lệnh mồ côi `BT MODEL RANKING` và `WEEKLY LIVINGNESS` đã gỡ khỏi `REASONING_RULEBOOK`, đo trên **prompt đang serve của production** (`RM-14`), mỗi câu có **hai neo độc lập**. Ghi **KHÔNG đổi cơ chế/thuật toán** — cả hai là câu điều kiện mà điều kiện không bao giờ đúng. Ghi **cỡ prompt không đổi là đúng** (con số đó đo context pack). Ghi **chạy cổng ở local cho kết quả SAI** (5 thay vì 2) — mọi kết luận về prompt phải dump từ production.
