# V10924 — CLAUDE.md thành mặt quy tắc thứ tư + soi hậu quả sau khi cắt

**Ngày:** 01/08/2026 · **Trạng thái:** đồng bộ 4 mặt xong · soi hậu quả xong, không gãy chỗ nào

---

## 1. Tóm tắt

Ba việc trong một phiên:

**(a)** Dựng `CLAUDE.md` thành **mặt quy tắc thứ tư**, chứa đủ A53/A54/A55 + chuỗi hoàn tất +
§52 + playbook-first + bảng "bẫy đã học". Đổi bộ đồng bộ từ **ba** thành **bốn** file ở cả 5 nơi
mô tả nó.

**(b)** Kiểm chuyện 3 tab treo: **hai terminal của agent đều rảnh, không có lệnh nào chạy**;
trên VPS không có tiến trình nào của dự án treo. Ba tab kia là phiên agent của Cursor kẹt ở
trạng thái *"Asking questions"* — nằm ngoài tầm agent.

**(c)** **Soi hậu quả SAU khi cắt** — câu owner hỏi thẳng. Kết quả: 6 lane đã nghỉ sinh ra **19
`experiment_name`**, và **không một cái nào** còn bị UI / API / cron / scheduler gọi đích danh.
Journal từ lúc cắt **0 lỗi**. Nhưng phát hiện **một lỗ trong CÁCH soi** của agent — xem phần 7.

---

## 2. Owner yêu cầu gì (nguyên văn)

**01/08 11:31:**

> *"Cập nhật các quy tắc anh vừa trao đổi với em vào claude.md đồng bộ nhất quán với các file
> liên quan, tiếp đi em, chắc chăn là do công cụ của cursos làm lỗi chứ gì nữa hiện tại tự nhiên
> sinh ra 3 tab cùng 1 công việc và đang treo cả chỉ có tab anh đang tương tác với em là hoàn
> thành đó em. Kiểm tra lại đi, chắc chắn đang lỗi treo chỗ nào rồi,*
>
> *Đồng thời em đã cát giảm thay thay thế hết chưa? đã thực sự kiểm soát, có tư duy có logic
> nhất quán chưa hay là thích là cắt bỏ mà không thèm soi tới sự ảnh hưởng tương quan, tương
> thích, liên hệ mật thiết của nhau đó em."*

---

## 3. Đào bới / phát hiện

### 3.1 Chuyện treo — không phải phía hệ thống

| Kiểm | Kết quả |
|---|---|
| Hai terminal của agent | **đều rảnh**, chỉ có dấu nhắc, không lệnh nào chạy |
| Tiến trình VPS chạy > 1 giờ | chỉ `networkd-dispatcher`, `unattended-upgrade`, `BT-Panel`, `BT-Task` — đều là của hệ điều hành và panel máy chủ, bình thường |
| Journal service `lottery` từ 10:25 | **0 dòng lỗi** |

Ba tab kia là **phiên agent của Cursor** kẹt ở *"Asking questions"* — chúng chờ người trả lời
chứ không phải treo do tiến trình. Agent không điều khiển được UI của Cursor. Cách xử: đóng ba
tab đó, hoặc `Developer: Reload Window`.

### 3.2 Soi hậu quả sau khi cắt — bảng dùng chung không chết

5 trong 6 lane nghỉ ghi vào **bảng dùng chung** `du_doan_test_bundles` / `du_doan_test_runs`.
Hai bảng này vẫn được **hơn 10 file khác** ghi nên **không bị chết** (dòng cuối 01/08). Nhìn
thoáng qua thì tưởng an toàn — nhưng nguy hiểm thật nằm chỗ khác.

### 3.3 Chỗ nguy hiểm thật: có ai lọc theo đúng tên experiment không

Nếu một consumer lọc theo đúng `experiment_name` của lane vừa nghỉ, nó sẽ **lặng lẽ mất dữ
liệu** — không báo lỗi, không panel nào đỏ. Đây đúng loại lỗi âm ỉ nhiều tháng.

**19 experiment_name của 6 lane nghỉ, không cái nào còn bị gọi đích danh:**

| Lane nghỉ | Sinh ra | Còn ai gọi |
|---|---|---|
| V10707 doctrine | `MN_DOCTRINE_AB_V1` · `MT_DOCTRINE_AB_V1` | ✓ không ai |
| V10781 prompt v2 | `PROMPT_V2_AB_V1` | ✓ không ai |
| V10692 multidir | `{MN,MT,MB}_DIR1_BT_V1` · `_DIR2_LO2_V1` · `_DIR3_LO3_V1` (9 cái) | ✓ không ai |
| V10679 full-pool | `{MN,MT,MB}_FULL_POOL_D_W06_V1` | ✓ không ai |
| V10680 top-K | `MN_TOPK22_W04_V2` · `MT_TOPK10_W04_V2` · `MB_TOPK10_W04_V2` | ✓ không ai |
| V10637 lane-v2 | không sinh `experiment_name` nào; chỉ ghi `lane_v2_daily_shadow` | xem 3.4 |

### 3.4 Lỗ trong CÁCH soi của agent — chỗ suýt bỏ sót

`_v10637_lane_v2_daily` ghi bảng `lane_v2_daily_shadow`. Soi lượt đầu (trước khi cắt) chỉ hỏi
*"ai import MODULE này"* → trả lời "không ai" → kết luận an toàn.

Nhưng phải hỏi thêm *"ai đọc BẢNG mà module này ghi"*. Hỏi vậy thì ra:

```
_v10660_no_lookahead_harness.py   CÓ CRON (45 14 * * *)   đọc lane_v2_daily_shadow
```

Kiểm tiếp: nó là bộ **kiểm chứng không-nhìn-trộm** (xác minh mọi dòng shadow/lane được tạo
trước giờ xổ), ghi ra `no_lookahead_audit`, và có `_table_exists()` bảo vệ. Bảng vẫn tồn tại,
chỉ là không có dòng mới → nó audit 0 dòng. **Không gãy.**

Nhưng nếu lane đó là loại có người đọc thật thì đã gãy mà không ai biết.

### 3.5 Ba lượt dò sai của chính agent

| Lượt | Sai gì | Sửa |
|---|---|---|
| 1–2 | Dò cột `experiment` — tên thật là **`experiment_name`** | Đọc `PRAGMA table_info` trước |
| 3 | So "cùng khung giờ" bằng `time(started_at)` — cột đó lưu **UTC**, lệch 7 tiếng nên danh sách "vắng" dính đầy MT/MB chỉ vì chưa tới giờ chạy | Bỏ so theo giờ, hỏi thẳng theo tên lane |
| 3 | Quên rằng cron gỡ lúc **10:31** còn lane chạy lượt sáng **05:30–06:10** → dữ liệu hôm nay **vẫn còn** chúng | Hiệu lực thật bắt đầu **từ ngày mai** |

---

## 4. Hướng xử lý và vì sao chọn

| Phương án | Vì sao chọn / loại |
|---|---|
| **`CLAUDE.md` là bản đầy đủ, tự đứng được** | **ĐÃ CHỌN.** Owner muốn "đồng bộ nhất quán" — một file chỉ trỏ sang file khác thì đọc một mình không dùng được |
| `CLAUDE.md` chỉ là con trỏ tới ba file kia | Loại: không tự đứng được, và dễ lệch khi ba file kia đổi |
| Chép nguyên `.cursorrules` sang | Loại: `.cursorrules` còn nhiều mục đã bị A55 thay thế; chép nguyên là mang theo cả phần chết |
| **Sửa mọi chỗ mô tả bộ đồng bộ** | **ĐÃ CHỌN.** 5 nơi ở 4 file. Không sửa thì phiên sau đọc "ba file" rồi bỏ quên `CLAUDE.md` |
| Soi hậu quả bằng cách chờ xem có lỗi không | Loại: lỗi kiểu này **không báo lỗi**, chỉ lặng lẽ mất dữ liệu |
| **Soi theo tên experiment + hai tầng phụ thuộc** | **ĐÃ CHỌN.** Bắt được đúng loại lỗi âm thầm |

---

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `CLAUDE.md` | **Mới** — mặt quy tắc thứ tư, đầy đủ A53/A54/A55, chuỗi hoàn tất 12 bước, §52, playbook-first, bảng 8 bẫy đã học |
| `.cursorrules` | +105 ký tự — "Three-way" → "Four-way", thêm bullet `CLAUDE.md`, sửa 5 câu |
| `.AGENT.md` | +208 ký tự — ghi rõ bộ đồng bộ bốn file |
| `.Antigravityrules.md` | +227 ký tự — sửa 5 chỗ gồm mục **51I SYNC CONTRACT** |
| `.cursor/rules/governance-traceability-automation.mdc` | +36 ký tự — quy tắc thi hành của Cursor |
| `docs/OWNER_DECISION_LEDGER.json` | Thêm `OD-20260801-G`, 6 mệnh đề kiểm được |
| `_v10922_impact_audit.py` | **Mới** — soi hậu quả 8 mặt sau khi cắt |
| `_v10923_experiment_impact.py` + 3 lượt dò | **Mới** — soi ai còn cần output của lane đã nghỉ |
| `_v10924_sync_four.py` + `_b.py` | **Mới** — đổi bộ đồng bộ ba → bốn, từ chối ghi nếu file ngắn đi |

---

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Bốn mặt quy tắc nhắc `CLAUDE.md` | `.cursorrules` 5 · `.AGENT.md` 1 · `.Antigravityrules.md` 6 · `.mdc` 2 · `CLAUDE.md` 3 — **đủ cả 5 nơi** |
| Sổ quyết định sau khi thêm `OD-20260801-G` | **11 quyết định · 0 mục trôi** |
| Journal service từ lúc cắt (10:25) | **0 dòng lỗi** |
| Tiến trình treo của dự án | **không có** (chỉ OS + BT-Panel, bình thường) |
| Job SỐNG còn cron | Nghiệm Thu · Total V2 · Total V3 · de-herd · khoá `/choi` — **đủ** |
| Bundle MN hôm nay | bạch thủ `38` · **15 model** · ACTIVE · tạo 05:20 — bình thường |
| Số model trong bundle 7 ngày | MN 15/15/15/14/15/15/15 — **không tụt** sau khi cắt |
| 19 experiment của lane nghỉ | **0 cái** còn bị UI/API/cron/scheduler gọi |
| Ghi file quy tắc | script **từ chối ghi** nếu kết quả ngắn hơn bản cũ — cả 4 file đều dài ra |

---

## 7. Vướng vấp

| # | Vấp | Hậu quả nếu bỏ qua |
|---|---|---|
| 1 | **Soi phụ thuộc chỉ một tầng** — chỉ hỏi "ai import MODULE", không hỏi "ai đọc BẢNG module đó ghi" | Suýt bỏ sót `_v10660_no_lookahead_harness` (có cron, đọc bảng của V10637). Lần này may vì nó có `_table_exists()` bảo vệ; lane khác thì đã gãy âm thầm |
| 2 | Dò sai tên cột: `experiment` thay vì `experiment_name` | Hai lượt kiểm đầu trả về rỗng, tưởng "không có gì để lo" |
| 3 | So "cùng khung giờ" bằng cột lưu **UTC** | Danh sách "vắng" dính đầy MT/MB chỉ vì chúng chưa tới giờ chạy — suýt báo động nhầm hàng loạt |
| 4 | Quên mốc thời gian: cắt cron lúc 10:31, lane chạy 05:30–06:10 | Suýt kết luận "cắt không ăn" vì hôm nay dữ liệu vẫn còn. **Hiệu lực thật từ ngày mai** |
| 5 | `.AGENT.md` và `.Antigravityrules.md` dùng câu chữ khác nên mẫu tìm lượt 1 không khớp | Nếu không kiểm lại số lần nhắc `CLAUDE.md` thì hai file này bị bỏ quên, bộ đồng bộ hỏng ngay từ đầu |

---

## 8. Gỡ về

Phiên này **chỉ đổi tài liệu quy tắc và thêm script soi**, không đụng code chạy, không deploy,
không đụng database.

```
git revert <commit V10924>     # bỏ CLAUDE.md + bộ đồng bộ bốn file
```

Gỡ lẻ: xoá `CLAUDE.md` · hoàn nguyên 5 chỗ mô tả bộ đồng bộ về "ba file" · xoá
`_v10922_*.py`, `_v10923_*.py`, `_v10924_*.py`. **Mất khoảng 1 phút.**

---

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng | Hạn |
|---|---|---|---|
| **FU-189** | Xác minh **ngày mai 02/08**: 19 experiment của 6 lane nghỉ phải **thực sự vắng**, và không job nào báo lỗi vì thiếu chúng | `_v10922_impact_audit.py` → journal 0 lỗi; số model bundle không tụt | 02/08 |
| **FU-189b** | Bổ sung vào quy trình: soi phụ thuộc phải **hai tầng** — ai import module, **và** ai đọc bảng module đó ghi | Đã ghi vào `CLAUDE.md` bảng bẫy + `OD-20260801-G` ghi chú | xong |
| FU-186 | Cửa sổ đóng băng đường ra số | không đổi gì tới 08/08 | 08/08 |
| FU-188 | 4 phiên bản 31/07 chưa có báo cáo công khai | cổng kiểm về 0 | sau 08/08 |

Nguyên văn lời owner: `CONVERSATION_CONTEXT_V10924_20260801.md` cùng thư mục.
