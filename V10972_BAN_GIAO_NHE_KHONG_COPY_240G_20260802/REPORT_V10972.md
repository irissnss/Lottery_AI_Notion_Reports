# REPORT V10972 — Bàn giao nhẹ, không copy 240G

**Phiên bản:** V10972 · **Ngày (VN):** 02/08/2026 · **Loại:** tài liệu / đo dung lượng — **không deploy production**

Public folder: `V10972_BAN_GIAO_NHE_KHONG_COPY_240G_20260802/`

---

## 1. Tóm tắt

Workspace `E:\Lottery_AI_Test` đo được khoảng **254 GB**, trong đó **~241 GB (95%)** là `artifacts/live_sync/` — **547** snapshot forensic (mỗi bản ~1.0–1.2 GB, chủ yếu `lottery_ai.db` from_vps + before_local). Code git-tracked chỉ **~86.5 MB** (2662 file); `.git` pack private **~95 MiB**. Máy mới chỉ cần clone 2 repo + copy `.env` thủ công ≈ **200–250 MB**; khi audit thì sync 1 lần từ VPS ≈ **+0.6–1 GB**. Không cần copy `backups/` (~9.7 GB) hay `data/` (~1.7 GB).

## 2. Owner yêu cầu gì (nguyên văn)

> repo/folder `Lottery_AI_Test` ~240GB — không thể copy nguyên si sang máy local mới. Cần hướng dẫn thực tế: gì chiếm dung lượng, gì BẮT BUỘC mang, gì bỏ/clone lại, quy trình bàn giao nhẹ.

Yêu cầu kèm: đo top folders · phân loại A–E · quy trình clone 2 repo + secrets thủ công · không copy DB/jsonl/backups/artifacts · audit bằng `_sync_live_forensic_inputs.py` · deliverable V10972 public (REPORT 9 phần + CONTEXT + HUONG_DAN + evidence) · mirror docs · push · gate PASS · REDACT secrets · Notion chỉ đọc · không deploy.

## 3. Đào bới / phát hiện

**Cách đo:** PowerShell `Get-ChildItem -Recurse | Measure-Object Length` trên `E:\Lottery_AI_Test` (giờ VN 02/08/2026); `git count-objects -vH`; `git ls-files` cộng kích thước working tree; soi `artifacts/live_sync` và `data/`.

**Top-level (GB):**

| Tên | GB | Phân loại |
|---|---:|---|
| `artifacts/` | **241.94** | B runtime (presque toàn bộ `live_sync`) |
| `backups/` | **9.67** | C backups |
| `data/` | **1.72** | B runtime |
| `docs/` | 0.46 | D docs (một phần tracked) |
| `Backup Final 23042026 DDXS` | 0.23 | C |
| `.git/` | 0.13 | A git objects |
| `web/` | 0.08 | A source (+ runtime jsonl nhỏ) |
| Còn lại | <0.1 | mixed |

**Chi tiết nặng:**

- `artifacts/live_sync/`: **241.1 GB**, **547** thư mục snapshot; **45** thư mục ≥1 GB; file lớn nhất kiểu `*/from_vps/lottery_ai.db` ~600 MB (không có file đơn ≥1 GB trong live_sync — dung lượng = nhiều bản lặp).
- `backups/`: `vps_backup_20260417_233529.tar.gz` **6.01 GB** · `vps_backup_20260417_232903.tar.gz` **3.01 GB** (2 file duy nhất ≥1 GB toàn workspace trong lần quét dirs nặng).
- `data/lottery_ai.db`: **597.5 MB** + hàng chục `.bak` lịch sử.
- `web/backend/prediction_trace.jsonl`: **19.8 MB**.
- `venv` / `node_modules`: **không có**.

**Git sạch:**

| Metric | Giá trị |
|---|---|
| Tracked files | 2662 |
| Tracked working tree | **86.5 MB** |
| Private `size-pack` | **94.91 MiB** |
| Public reports working tree | **41.7 MB** |
| Public `size-pack` | **~5 MiB** |

Evidence: `evidence/summary.txt`, `evidence/toplevel_sizes.csv`.

## 4. Hướng xử lý và vì sao chọn

**Chọn:** bàn giao bằng `git clone` 2 repo + secrets thủ công + sync VPS khi cần audit.

**Loại phương án khác:**

| Phương án | Vì sao loại |
|---|---|
| Copy nguyên 254 GB USB/HDD | Chậm, dễ lỗi, mang theo rác forensic vô ích |
| Chỉ mang `data/` + `artifacts/` mới nhất | Vẫn hàng trăm MB–GB; dễ nhầm “local = truth”; VPS mới hơn |
| Zip cả `backups/` | ~10 GB tar cũ 4/2026 không cần cho vận hành ngày thường |

## 5. Đã làm gì

| File / chỗ | Thay đổi |
|---|---|
| `Lottery_AI_Notion_Reports/V10972_.../REPORT_V10972.md` | Báo cáo A55 9 phần |
| `.../CONVERSATION_CONTEXT_V10972_20260802.md` | Nguyên văn + bước agent |
| `.../HUONG_DAN_MAY_MOI_NHE.md` | Hướng dẫn copy-paste owner |
| `.../evidence/*` | Bảng dung lượng |
| `docs/BAN_GIAO_NHE_KHONG_COPY_240G_V10972.md` | Mirror ngắn private |
| `CHANGELOG.md` / `CURRENT_TRUTH_SSOT.md` / `FOLLOW_UP_TRACKER.md` | Prepend V10972 · FU-241 |
| Production / VPS | **Không đụng** |

Backup: không sửa runtime code — không cần `.pre`. Secrets: **không** đưa `.env` vào report.

## 6. Cổng kiểm

| Mục | Kết quả |
|---|---|
| Đo top folders + live_sync count | Đạt — evidence |
| Ước clone sạch (count-objects + tracked MB) | Đạt |
| Public đủ REPORT + CONTEXT + HUONG_DAN + evidence | Đạt |
| REDACT — không in API key / nội dung `.env` | Đạt (chỉ ghi size 773 bytes) |
| Notion ghi | **Không gọi** (A55.1) |
| Deploy production | **Không** |
| `python web/backend/_v10921_report_gate.py V10972` | (chạy sau push — phải PASS) |

## 7. Vướng vấp

1. Lần quét “file ≥1 GB” ban đầu chỉ thấy 2 tar trong `backups/` — dễ hiểu nhầm “không có file lớn”. **Hậu quả nếu bỏ qua:** bỏ sót 241 GB gồm hàng trăm DB ~600 MB. Đã bổ sung đếm thư mục snapshot + đo `live_sync` riêng.
2. `data/` listing lần đầu trống do lỗi script PowerShell lồng `if` trong expression — đo lại được.
3. Public reports repo có nhiều `desktop.ini` garbage trong `.git` (cảnh báo `git count-objects`) — **không** ảnh hưởng bàn giao; clone fresh trên máy mới sạch hơn.

## 8. Gỡ về

Không thay đổi runtime / không deploy → không rollback VPS.

Nếu cần gỡ docs phiên này trên private:

```text
git checkout HEAD~1 -- CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md docs/FOLLOW_UP_TRACKER.md
# hoặc xóa docs/BAN_GIAO_NHE_KHONG_COPY_240G_V10972.md nếu commit riêng
```

Public: xóa folder `V10972_BAN_GIAO_NHE_KHONG_COPY_240G_20260802/` rồi commit/push (chỉ khi owner yêu cầu).

## 9. Theo dõi tiếp

| Mã | Nội dung | Hạn / ngưỡng |
|---|---|---|
| **FU-241 · TK0802-3 · Bàn giao nhẹ không copy 240G · hạn 02/08** | Docs + evidence + gate | Đóng khi gate PASS + owner đã clone máy mới |
| FU-225 · UI0803 | Ưu tiên sau khi máy mới lên | 03/08 |
| (tuỳ chọn) dọn `artifacts/live_sync` máy cũ | Giữ 1–3 snapshot mới nhất; xoá phần còn lại nếu thiếu ổ | Owner quyết — ngưỡng: giữ <5 GB live_sync nếu muốn |

**Ngưỡng hành động:** máy mới sau clone mà folder >5 GB mà chưa chạy sync → dừng, soi đã copy nhầm `artifacts/`/`backups/` chưa.
