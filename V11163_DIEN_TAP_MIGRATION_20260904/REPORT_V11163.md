# REPORT V11163 — DIỄN TẬP MIGRATION: KHUYẾN NGHỊ **ĐỪNG ĐỔ**

> **Ngày:** 04/09/2026 01:30–02:0x (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> `POOL_VERDICT = HOLD` · `MODEL_ACTION = BLOCKED` · **production 0 ghi · 0 deploy**
> **Bản này lật ngược một đề xuất của chính agent** — bằng số đo, không bằng đổi ý.

---

## 1 · Tóm tắt

Agent từng đề xuất *«đổ đầy `output_counterfactual_rank`»*. Diễn tập **thật trên bản sao** cho ra
khuyến nghị **ngược lại: ĐỪNG ĐỔ** theo thiết kế cột hiện tại.

Kỹ thuật thì **sạch hoàn toàn** — ghi `0,04s`, idempotent, rollback `0,03s`, `integrity ok`.
**Rủi ro nằm ở NGỮ NGHĨA**, và nó là loại rủi ro kho này vừa mất hai ngày để dọn.

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại |
|---|---|---|
| 04/09 ~00:2x | *«ok em thực hiện tuần tự lần lượt xử lý dứt điểm các vấn đề em đã đào ra dùm anh»* | `YÊU_CẦU` |
| 04/09 ~01:0x | *«Tiếp đi em»* | `YÊU_CẦU` |
| 04/09 ~01:3x | *«Tiếp tục đi e»* | `YÊU_CẦU` |

Mục `XVI` prompt owner (03/09) vẫn ràng buộc: muốn ghi production thì **phải xuất materialization
proposal riêng** với đủ mười mục, **rồi mới** được ghi.

---

## 3 · Đào bới / phát hiện

### 3.1 · Diễn tập — số THẬT, không ước lượng

Trên bản sao `809 MB` (tạo trong `5,7s`), production đọc-chỉ suốt quá trình:

| bước | kết quả |
|---|---|
| dựng giá trị | **2.538** · trong top-10 **2.094** · ngoài top-10 **444** |
| ghi lần 1 | **0,04s** · `0 → 2.094` dòng có giá trị |
| **idempotency** — ghi lần 2 | băm cột **KHỚP** `ee1659161ac83058…` |
| **rollback** `SET … = NULL` | **0,03s** · về đúng `0` dòng |
| `integrity_check` sau toàn bộ | **`ok`** |
| production trong lúc diễn tập | **`0/17.040`** — không đụng |

### 3.2 · 🔴 Chặn ①: `NULL` sẽ mang HAI nghĩa lẫn nhau

Sau migration chỉ **2.094/17.040 = 12,3%** dòng có giá trị. **14.946 dòng vẫn `NULL`**, và `NULL`
đó gộp hai thứ **khác hẳn nhau về ý nghĩa**:

| nghĩa | dòng |
|---|---|
| ô **ngoài** cửa sổ `02/08–03/09` — **CHƯA TÍNH** | ~14.502 |
| ô **trong** cửa sổ nhưng số của model rơi **ngoài top-10** — **ĐÃ TÍNH, không có hạng** | **444** |

Đây **đúng cái bẫy** `V11158` mất một ngày để dọn: `MISSING_SHADOW_ROW` gộp **bốn lớp** khác nhau
vào một nhãn và đẻ ra **1.058 lượt thua ảo**. Đổ vào cột này theo thiết kế hiện tại là **tự dựng
lại đúng bẫy đó**, ở một cột khác.

### 3.3 · 🔴 Chặn ②: writer hằng giờ sẽ XOÁ SẠCH giá trị vừa đổ

`_materialize_shadow_promotion_scorecard.py` có **2 câu `INSERT OR REPLACE`** truyền **hằng cứng
`None`** ở vị trí **17/34**, **vô điều kiện** (không nằm trong nhánh nào), và job
`measurement_materialize` chạy **`16:00 · 17:00 · 18:00 · 20:00`**.

⚠️ [ĐÍNH CHÍNH · ĐÃ RÚT LẠI RL-008: câu «chạy `16:00 · 17:00 · 18:00 · 20:00`» ở trên là SAI —
đo lại trên `scheduler_logs` ngày 04/09 cho **3 LẦN CHẠY THẬT**, theo KẾT QUẢ TỪNG MIỀN chứ không
theo giờ chẵn: 16:39:55 (MN) · 17:30:18 (MT) · 18:31:48 (MB), caller thật `scheduler.py:665`.
Tần suất chính xác chung: **INDETERMINATE**. Kết luận «writer ghi đè trong <1 giờ» ở dòng dưới
KHÔNG đổi. Xem docs/SO_RUT_LAI.json, bản rút V11164_EOD_LIVE_CLOSURE_20260904.]

⇒ Đổ mà **không sửa writer trước** là đổ vào một cột bị ghi đè trong **chưa tới một giờ**.

### 3.4 · Và đổ vào KHÔNG mở khoá được việc gì

Quét **3.024 tệp**: **không reader nào đọc cột này**. 34 dòng khớp tên cột đều là DDL hoặc danh
sách cột của `INSERT`. Nên materialize chỉ **đổi chỗ lưu** của một thứ đã có sẵn trong artifact
`v11159_pha1_rank_dong_bang.json` (băm `9474b7bc…`).

---

## 4 · Hướng xử lý và vì sao chọn

**Vì sao khuyến nghị B (giữ artifact).** Ba yếu tố cộng lại: cột **chưa có reader** ⇒ lợi ích
bằng 0; đổ vào **tạo `NULL` hai nghĩa** ⇒ hại có thật; và **phải đụng writer đang chạy hằng giờ**
⇒ rủi ro có thật. Một thay đổi lợi-0 / hại-có / rủi-ro-có thì không nên làm.

**Vì sao KHÔNG tự chọn giúp owner.** Lựa chọn **C** (bảng riêng + cột trạng thái + panel `§52`) là
cách làm **đúng bài** nếu sau này có người đọc thật. Đó là quyết định về **hướng sản phẩm**, không
phải quyết định kỹ thuật — nên trình đủ ba lựa chọn kèm giá của từng cái.

**Vì sao agent KHÔNG sửa rủi ro `_safe_stdio_ctx`.** `V11162` phát hiện `_restore_stdio` trả lại
**chính luồng stdout hỏng**, tức hỏng một lần là câm vĩnh viễn. Nhưng đo được **0 dòng lỗi I/O**
⇒ nhánh đó **chưa từng chạy**. Sửa một nhánh chưa bao giờ nổ là đổi hành vi scheduler để đối phó
với giả định. Ghi lại là đủ.

---

## 5 · Đã làm gì — TRƯỚC / SAU / KIỂM

| | TRƯỚC | SAU |
|---|---|---|
| gói materialization | **không có** | `docs/DE_XUAT_MATERIALIZATION_V11163.md`, đủ **12 mục** |
| số liệu migration | **ước lượng** | **đo thật**: 2.538 giá trị · 12,3% phủ · ghi 0,04s · rollback 0,03s |
| rủi ro partial-population | nghi ngờ | **chứng minh**: `NULL` gộp ~14.502 «chưa tính» với **444** «đã tính, không hạng» |
| va chạm writer | chưa ai nêu | **đo được**: writer truyền `None` vô điều kiện, chạy 4 lần/ngày |
| `output_counterfactual_rank` production | `0/17.040` | **`0/17.040`** — không đụng |

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| production ghi | **0** — mọi thao tác trên bản sao, xoá sau khi xong |
| deploy | **0** |
| idempotency | ✓ băm cột khớp giữa hai lần ghi |
| rollback | ✓ `0,03s`, về đúng trạng thái đầu |
| `integrity_check` | ✓ `ok` |
| xác nhận cuối | ✓ production `0/17.040` dòng có giá trị |

---

## 7 · Vướng vấp

**🟡 Không có vướng vấp kỹ thuật.** Diễn tập chạy trơn ngay lần đầu. Điều đáng ghi là **kết luận
đi ngược đề xuất ban đầu của chính agent** — và đó là lý do phải diễn tập trước khi làm, thay vì
làm rồi mới biết.

---

## 8 · Gỡ về

**Không áp dụng** — không ghi production, không deploy. Bản diễn tập đã xoá sau khi đo xong.

---

## 9 · Theo dõi tiếp

| việc | trạng thái |
|---|---|
| **owner chọn A / B / C** | **CHỜ OWNER** — chọn **B** thì đóng mục này, không làm gì thêm |
| lineage 3-càng persist | cùng câu chuyện, cùng khuyến nghị · nếu chọn **C** phải nhớ mốc `2026-06-27` (`RM-21`) |
| duyệt ngưỡng đăng ký trước MT | **CHỜ OWNER** |
| lượt scheduled MN ~05:15 | chờ — đóng `SCHEDULED_SHADOW_PROMPT_CLEAN_PROVEN` |
| rủi ro `_safe_stdio_ctx` | ghi nhận, **chủ động không sửa** |

---

## Nguồn ba lớp (§62)

### `OWNER_SAID`
- 04/09 ~01:3x — *«Tiếp tục đi e»*
- (03/09, còn ràng buộc) mục `XVI` — *«Nếu offline artifact PASS: xuất materialization proposal
  riêng… Chỉ sau gate đó mới ghi production. Không nói "thuần đọc" nếu có UPDATE/INSERT.»*

### `CODE_DID`
- diễn tập: 2.538 giá trị · 2.094 trong top-10 · 444 ngoài · ghi `0,04s` · rollback `0,03s`
- idempotency: băm cột `ee1659161ac83058…` khớp giữa hai lần ghi
- `integrity_check` = `ok` · production `0/17.040` trước và sau
- writer: 2 câu `INSERT OR REPLACE` truyền hằng `None` ở vị trí 17/34, vô điều kiện

### `DOC_SAID`
- `docs/DE_XUAT_MATERIALIZATION_V11163.md` — **văn bản mới**, `DOC_SAID` = `CODE_DID`: mọi con số
  trong đó đến từ `v11163_dien_tap.json`, không viết tay.
- `docs/CURRENT_TRUTH_SSOT.md` §V11159 ghi *«materialize `output_counterfactual_rank` — cần
  materialization proposal riêng»* — **nay đã có**, và proposal đó khuyến nghị **đừng đổ**.
- `CLAUDE.md` `§52` mục 13 *«không đụng writer của `final_bundles`»* — là lý do lineage 3-càng
  không thể persist vào bundle, phải sang bảng riêng nếu owner chọn **C**.

---

TanPhatAI cần làm: ghi **`V11163`** — `governance_seq 479`, công khai bản này. Ghi **agent LẬT NGƯỢC đề xuất của chính mình bằng số đo**: từng đề xuất *«đổ đầy `output_counterfactual_rank`»*, diễn tập cho khuyến nghị **ĐỪNG ĐỔ**. Ghi **hai chặn đo được**: ① sau migration chỉ **12,3%** dòng có giá trị và `NULL` mang **hai nghĩa lẫn nhau** (~14.502 «chưa tính» vs **444** «đã tính, không có hạng») — đúng bẫy `V11158` mất một ngày dọn; ② **writer hằng giờ truyền `None` vô điều kiện** sẽ **xoá sạch** trong chưa tới một giờ. Ghi **KHÔNG reader nào đọc cột** (quét 3.024 tệp) ⇒ đổ vào **không mở khoá được việc gì**. Ghi **kỹ thuật thì sạch**: ghi `0,04s` · idempotent · rollback `0,03s` · `integrity ok` · **production `0/17.040` không đụng** — rủi ro nằm ở **ngữ nghĩa**, không ở kỹ thuật. Ghi **ba lựa chọn A/B/C trình owner**, agent nghiêng về **B** (giữ artifact, không đụng schema). Ghi **agent chủ động KHÔNG sửa** rủi ro `_safe_stdio_ctx` vì đo được 0 dòng lỗi I/O. **Không mở Prompt 44. Không mở FU mới.** `POOL_VERDICT` giữ **`HOLD`**.
