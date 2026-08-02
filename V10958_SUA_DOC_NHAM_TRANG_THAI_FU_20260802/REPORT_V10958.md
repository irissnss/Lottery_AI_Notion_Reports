# V10958 — Sửa đọc nhầm trạng thái FU (hết báo động giả FU-194)

**Ngày:** 02/08/2026 · **Commit riêng:** `f2aaa711510e38057624fcec0bf79e7a407ccfd4` · **Commit công khai:** *(điền sau push public)* · **Trạng thái:** ĐẠT — bộ đầu phiên không còn báo FU-194 quá hạn

---

## 1. Tóm tắt

`docs/FOLLOW_UP_TRACKER.md` ghi chồng từ trên xuống (`prepend()`), nên cùng một mã FU có thể xuất hiện nhiều lần. Bộ kiểm đầu phiên `_v10920_session_start.py` trước đây duyệt mọi khối đang treo mà không bỏ trùng theo mã — nên vẫn báo `FU-194` quá hạn `WAIT_LIVE` trong khi bản mới nhất đã `CLOSED_PASS` từ 17:45 ngày 01/08. Đã thêm module chung `_v10958_fu_reader.py` (chỉ lấy bản gần đầu file nhất), sửa bộ đầu phiên và bảng master. Sau sửa: **0 mục FU quá hạn giả**; trong file hiện có **2 mã bị trùng** (FU-194, FU-199), trong đó **1 mã** (FU-194) từng bị đọc nhầm thành treo; **2 mã** lệch trạng thái first/last nếu ai lấy bản dưới cùng.

## 2. Owner yêu cầu gì (nguyên văn)

> Sửa một lỗi công cụ đang gây báo động giả lặp lại. … Nên một mã FU có thể xuất hiện **nhiều lần** trong file: bản mới nhất nằm gần đầu, các bản cũ vẫn nằm nguyên phía dưới làm lịch sử. Hậu quả: ai đọc file mà không cẩn thận sẽ vớ trúng bản cũ và báo nhầm trạng thái. **Đã xảy ra thật hai lần trong một ngày.** Cả hai lần đều báo `FU-194` đang quá hạn chờ live tối 01/08, trong khi thực tế nó đã đóng `CLOSED_PASS` lúc 17:45 ngày 01/08.

Yêu cầu kèm: hàm dùng chung; sửa chỗ đọc sai; chạy lại session start; ghi hồ sơ V10958; đẩy hai repo; không đụng Notion; không đụng QD-014 đường ra số.

## 3. Đào bới / phát hiện

**Chạy thật trước sửa** (`python web/backend/_v10920_session_start.py`, 02/08):

- Mục theo dõi còn treo: 42 · trong đó **QUÁ HẠN 1** = `FU-194 … WAIT_LIVE hạn 2026-08-01`
- Cảnh báo đầu phiên: *"1 mục theo dõi quá hạn"*

**Đối chiếu vị trí trong file** (trước khi prepend ghi chú V10958; độ dài file ~962.788 ký tự):

| Mã | pos (ký tự) | status |
|---|---|---|
| FU-194 (mới) | 11.775 | `CLOSED_PASS` |
| FU-194 (cũ) | 21.203 | `WAIT_LIVE` |
| FU-199 (mới) | 12.242 | `CLOSED_PASS` |
| FU-199 (cũ) | 17.236 | `READY_NOT_DEPLOYED` |

**Thống kê trùng** (`_v10958_fu_reader.duplicate_stats`):

| Chỉ số | Số |
|---|---|
| Tổng tiêu đề `### FU-…` | 100 |
| Mã duy nhất | 98 |
| Mã bị trùng lặp | **2** |
| Bản cũ thừa | **2** |
| First ≠ last status | **2** |
| Đọc bản cũ → báo treo giả | **1** (FU-194) |

**Chỗ đọc:**

| Chỗ | Cách đọc trước | Có vớ bản cũ? |
|---|---|---|
| `_v10920_session_start.py` | `split("###")` rồi mọi khối có `` `WAIT_LIVE` ``… trong 220 khối đầu, **không dedupe theo mã** | **Có** — đây là nguồn báo động giả đầu phiên |
| `.cursor/hooks/session_start_briefing.py` | Chỉ gọi `_v10920_session_start.py` | Gián tiếp — sửa session_start là đủ |
| `_v10921_report_gate.py` | Không parse trạng thái FU | Không áp dụng |
| `_v87_master_board.py` | Đã `seen` first-wins sẵn | Đúng logic; chuyển sang gọi reader chung để không lệch sau này |

Bằng chứng: `evidence/duplicate_stats_and_treo.txt`, `evidence/session_start_after.txt`.

## 4. Hướng xử lý và vì sao chọn

1. **Xoá / dồn bản cũ trong FOLLOW_UP** — loại vì owner yêu cầu giữ lịch sử; từng có sự cố xoá sạch file khi ghi sai.
2. **Sửa tại chỗ chỉ session_start** — loại vì chỗ khác (master board) cũng parse FU; dễ lệch lại.
3. **Module đọc chung + gọi từ mọi chỗ parse** — chọn: một quy ước, kiểm được bằng `duplicate_stats`, ví dụ FU-194 trong docstring.

Không deploy `lottery.service`: đây là công cụ đọc hồ sơ chạy tay trên máy local / hook Cursor, không nằm trên đường ra số.

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `web/backend/_v10958_fu_reader.py` | **Mới** — `load_fu_latest`, `treo_items`, `duplicate_stats`, `get_fu` |
| `web/backend/_v10920_session_start.py` | Dùng `treo_items()` thay split thủ công |
| `web/backend/_v87_master_board.py` | `_fu_items_full_block` + `_fu_audit_block` gọi reader |
| `CHANGELOG.md` / `CURRENT_TRUTH_SSOT.md` / `FOLLOW_UP_TRACKER.md` | `prepend()` — ghi chú quy ước đọc + FU-218 CLOSED_PASS |
| `docs/AUTOMATION_STATE.json` | `governance_seq` 375 → **376**, `_v10958_last_event` |
| `docs/AUTOMATION_HISTORY.jsonl` | Thêm 1 dòng sự kiện |

Backup: `backups/v10958_pre/` (`*.pre` từ git HEAD + bản sau sửa).

Deploy: **không** — không khởi động lại `lottery`, không đụng 4 bảng khoá.

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Session start trước sửa | FU-194 QUÁ HẠN WAIT_LIVE — **trượt (đúng bug)** |
| Session start sau sửa | QUÁ HẠN FU = **0** · treo vẫn có FU-216/215/208/209… — **đạt** |
| `get_fu("FU-194")` | `CLOSED_PASS`, `in_treo=False` — **đạt** |
| `get_fu` FU-208/209/215/216 | `OWNER_LOCK`, `in_treo=True` — **đạt** |
| `duplicate_stats` | 2 mã trùng · 1 false-treo nếu đọc bản cũ — **đạt** |
| QD-014 / 15 model / combo-super | Không sửa — **đạt** |
| Notion ghi | Không gọi — **đạt** |

## 7. Vướng vấp

1. **Backup sau khi sửa rồi mới copy** — lần đầu `Copy-Item` lấy đúng bản đã sửa. Đã bổ sung `*.pre` từ `git show HEAD`. Hậu quả nếu bỏ qua: gỡ về không có bản gốc sạch.
2. **PowerShell nuốt `&&` / chuỗi Python nhiều dòng** — phải tách lệnh / ghi file script. Hậu quả nếu cố nhét một dòng: patch dở, không biết đã sửa audit block chưa.
3. **Số treo sau sửa (67) khác số cũ (42)** — reader mới lấy đúng ô `**status**` của bản mới nhất cho mọi mã; bộ cũ bắt chuỗi `` `STATUS` `` trong 220 khối và không dedupe. Không phải regression chức năng báo quá hạn; là đo đúng hơn. Hậu quả nếu chỉ nhìn số tuyệt đối: tưởng “treo tăng” trong khi thực ra hết báo giả FU-194.

## 8. Gỡ về

```bat
copy /Y backups\v10958_pre\_v10920_session_start.py.pre web\backend\_v10920_session_start.py
copy /Y backups\v10958_pre\_v87_master_board.py.pre web\backend\_v87_master_board.py
del web\backend\_v10958_fu_reader.py
```

Docs đã prepend: khôi phục từ git commit trước V10958 (không xóa tay bằng `open(w)`). Thời gian gỡ code: dưới 1 phút. Sau gỡ, session start sẽ lại báo FU-194 quá hạn giả.

## 9. Theo dõi tiếp

| Mã | Ngưỡng / việc | Hạn |
|---|---|---|
| FU-218 | Đã `CLOSED_PASS` — nếu session start lại báo quá hạn một mã đã `CLOSED_*` trong khi bản đầu file là CLOSED → mở lại ngay | Mọi phiên |
| — | Khi thêm chỗ parse FU mới: **bắt buộc** import `_v10958_fu_reader`, cấm `split("###")` tự chế | Standing |
| FU-215 / QD-014 | Đóng băng đường ra số tới hết 08/08 — phiên này không đụng | 2026-08-08 |
