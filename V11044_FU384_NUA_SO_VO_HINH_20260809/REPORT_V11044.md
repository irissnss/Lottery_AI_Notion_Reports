# REPORT V11044 — FU-384: SỔ THEO DÕI HẾT VÔ HÌNH NỬA TỆP + TÁCH LỊCH SỬ

**Ngày:** 2026-08-09, 09:20 → 10:45 giờ VN
**Phiên bản:** V11044 (+V11044b) · **Tầng verdict:** `REPORT_PROVEN` — sổ sách/tooling, không
đụng runtime

---

## 1. Tóm tắt

Việc nặng nhất còn lại, làm đầu ngày với đầu óc tỉnh (theo dặn của owner). Bộ đọc sổ theo dõi
chỉ khớp `### FU-<số>`; tệp có **780 tiêu đề `###`** ⇒ **384 khối (47,7% dung lượng) chưa bao
giờ được đếm**. Đã sửa bộ đọc thấy đủ, tách lịch sử **1,29 MB → 564 KB (−56%)**, dựng cổng §61
cho lỗi «quên ô status» đã lặp ba lần, và đính chính §60 các con số lịch sử.

**Và suýt mất lịch sử một lần nữa:** file archive rơi vào `.gitignore` — cổng cắt cụt cho qua vì
không phải tiền tố (đúng lỗ hổng 08/08), chỉ bắt được vì kiểm `git ls-files` sau commit.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **GĐ-1 · 10/08 — FU-384: MỘT NỬA SỔ VÔ HÌNH** (việc nặng nhất — làm đầu ngày với đầu óc tỉnh)
> 1. BACKUP sổ + chạy mọi thay đổi trên BẢN SAO trước (bài học FU-324).
> 2. Sửa regex/loader để thấy đủ 768 tiêu đề; nghiệm thu: bộ đọc mới trả TỔNG KHỐI = 768,
> FU-330 xuất hiện lại, FU-185 không còn nuốt thân. KHÔNG xoá 357 khối di sản — gắn nhãn LEGACY.
> 3. Gộp 128 khối trùng: giữ khối mới nhất, GHI TỪ CUỐI NGƯỢC LÊN, đọc lại bằng bộ đọc THẬT.
> 4. Cổng máy §61 cho lỗi "quên ô status": thiếu ⇒ CHẶN. Thử allow/deny thật.
> 5. ĐÍNH CHÍNH §60: liệt kê mọi con số lịch sử từng báo trên nửa tệp và ghi lại con số ĐÚNG.

---

## 3. Đào bới / phát hiện

### 3.1 — Đo trước khi sửa

| | |
|---|---|
| tiêu đề `###` trong tệp | **780** |
| bộ đọc cũ khớp | **384** (`### FU-<số>`) |
| **chưa bao giờ đếm** | **384 khối = 640 KB · 47,7%** |
| thành phần vô hình | **357 khối `### FU-V<version>-…`** (di sản) · 30 khác · **1 FU thật bị sót** |

### 3.2 — Ba lỗi cụ thể

**`FU-330` mất tích:** tiêu đề `### A1 / FU-330 · ĐÃ LÀM …` — tiền tố `A1 / ` làm trượt regex.
Lần thứ tư của họ lỗi V10980 / FU-353 / FU-370.

**`FU-185` nuốt 573 KB:** thân khối chạy tới `### FU-<số>` **kế tiếp**, nên mọi khối không-khớp
nằm giữa bị nuốt vào thân mục đứng trước.

**134 khối FU trùng** (bản cũ của cùng mã) + **357 LEGACY** = phần lớn dung lượng.

---

## 4. Hướng xử lý và vì sao chọn

**Điểm cắt thân = mọi `##`/`###`, không riêng `### FU-<số>`.** Đây là gốc của cả hai lỗi «FU-185
nuốt» và «nửa tệp vô hình».

**Tách lịch sử CHUYỂN — không xoá.** 357 LEGACY + 134 khối cũ sang `docs/archive/`, giữ vết. Bản
mới nhất mỗi mã ở lại sổ chính.

**Vật chất hoá TRƯỚC khi tách.** 27 khối mới đang **kế thừa** hạn/mã đọc từ khối cũ; tách khối cũ
mà chưa vật chất hoá thì mất — **đo được 10 mã đổi khi thử lần đầu**. Hạn ghi ô `**hạn mới**` (bộ
đọc đọc được); **mã đọc ghi vào tiêu đề** (bộ đọc lấy mã đọc từ tiêu đề, không từ ô — đây là chỗ
lần đầu làm sai).

**Ghi một lần, không splice nhiều lần** (bài học băm tiêu đề V11042): dựng tệp mới = gốc TRỪ span
archive, viết một lần.

---

## 5. Đã làm gì (§60.4 TRƯỚC/SAU)

| | TRƯỚC | SAU |
|---|---|---|
| bộ đọc thấy | 384/768 khối | **đủ 780**, phân loại FU/LEGACY/khác |
| `FU-330` | **MẤT TÍCH** | **tái xuất** — `DEPLOYED_PENDING_LIVE_VERIFY`, hạn 07/08 |
| `FU-185` thân | **573 KB** | **1.679 ký tự** |
| sổ chính | **1,29 MB · 14.448 dòng** | **564 KB (−56%)** |
| mã FU (một khối/mã) | — | **259** (258→259, +FU-330) |

**Tách:** `len(chính) + len(archive) == len(gốc)` bảo toàn từng byte · `load_fu_latest()`
trước/sau **259 mã, 0 mất, 0 đổi** · **0 tiêu đề băm** · chạy `--thu` trên bản sao trước.

**§60 đính chính con số lịch sử:** «749 mục» = **259 FU thật + 357 LEGACY** (749 cũ đếm cả di sản
lẫn khối trùng như mục riêng, **sai từ gốc**) · «135 treo» → **138**.

**Cổng §61** `_v11044_cong_o_status.py`: khối FU thiếu ô status ⇒ CHẶN, nối hook `git commit`.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11044_archive_so.py --ap-dung` | `ARCHIVE_V11044=DAT` — byte bảo toàn, 259 mã 0 mất 0 đổi |
| `_v11044_cong_o_status.py` | `O_STATUS_V11044=DAT` — 259 khối đều có ô status |
| `_v11042_gian_lich.py` | `GIAN_LICH_V11042=DAT` |
| `_v11040_kiem_cat_cut.py` | `CAT_CUT_V11040=DAT` |
| `_v11034_kiem_cheo_quyet_dinh.py` | `KIEM_CHEO_QD=SACH` |
| `_v11028_cong_dong_bang.py` | `DONG_BANG_QD041=CON_NGUYEN` |
| `_v10920_decision_ledger.py` | **trôi = 0** |

**RM-15 cổng ô status:** khối FU-999 giả không ô status ⇒ **thoát 1 CHẶN**; sạch ⇒ **thoát 0**;
khôi phục byte-khớp. Hook `git commit` khi sạch ⇒ `{"permission": "allow"}`.

**Quét số hiệu BỐN NƠI:** `V11044` `FU-386` `QD-055` `DD0909-2` **TRỐNG**; `KS1008` `SC0908-4`
`SC1008-2` **đã dùng — bỏ**.

**4 bảng khoá:** không chạm. **QD-041 còn nguyên.**

---

## 7. Vướng vấp

**7.1 — Suýt mất lịch sử một lần nữa (nặng nhất).** File `docs/archive/FOLLOW_UP_TRACKER_LICH_SU.md`
rơi vào `.gitignore:128` (`archive/`). Commit V11044 **xoá 8.736 dòng** khỏi FOLLOW_UP nhưng bản
lưu chúng **không vào git** — `git add` bỏ qua file untracked bị ignore. Cổng cắt cụt **cho qua**
vì tệp ngắn đi không phải tiền tố (đúng lỗ hổng 08/08). **Chỉ bắt được vì kiểm `git ls-files` sau
commit.** Force-add ở V11044b: `git add -f`, **7.521 dòng vào git**. Nếu không kiểm, ai clone sẽ
mất toàn bộ lịch sử.

**7.2 — Vật chất hoá mã đọc lần đầu làm sai.** Thêm ô `| **ma_doc** | … |` — nhưng bộ đọc lấy mã
đọc từ **tiêu đề**, không từ ô. Thử archive thấy **10 mã đổi** ⇒ khôi phục, làm lại: chèn mã đọc
vào tiêu đề.

**7.3 — `_doc_prepend` kêu đúng lúc.** Khi ghi khối V11044 vào FOLLOW_UP (đã ngắn 56% sau
archive), `_doc_prepend` cảnh báo *«bản trên đĩa thiếu 7.496 dòng (56,2%)»*. Đây là **cảnh báo
đúng** — nhưng lần này là archive có chủ ý, đã nghiệm thu bảo toàn byte. Ghi tiếp là đúng. Nếu
không có archive mà thấy cảnh báo này thì phải dừng.

---

## 8. Gỡ về

```bash
cp backups/v11044_pre/FOLLOW_UP_TRACKER.md docs/FOLLOW_UP_TRACKER.md
cp backups/v11044_pre/_v10958_fu_reader.py web/backend/
git rm docs/archive/FOLLOW_UP_TRACKER_LICH_SU.md
git revert cfa336c 6c4d150
```

---

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| `FU-385` | tab «Cursor Rules» hỏng hai tầng | **tiếp theo** |
| `FU-369` | cổng cấp số hiệu quét 4 nơi | GĐ-4, ưu tiên |
| `FU-350` `FU-377` `FU-360` `FU-375` | hàng đợi GĐ-4 | chưa làm |
| **tối nay 18:05 / 19:35** | 24 phép C23/C24 → FU-373 · lane `la_do_lui=0` → FU-366 | chờ cron nổ |
| nhóm B · v81=0 · `viewer.js` | ba câu | 🖊️ **chờ owner** |

---

## LOCK-IN / OPEN / NEXT ACTION

**LOCK-IN:** bộ đọc thấy đủ 780 tiêu đề · FU-330 tái xuất · FU-185 hết nuốt · sổ chính −56% ·
lịch sử vào git (7.521 dòng) · cổng §61 ô status chặn được · trôi = 0 · QD-041 còn nguyên.

**OPEN — chờ owner:** nghiệm thu nhóm B · `v81_provider_pilot_recent` rỗng · dây chuyền `viewer.js`.

**NEXT ACTION:** `FU-385` → `FU-369` → `FU-350` → `FU-377` → `FU-360` → `FU-375`. Tối nay đọc log
18:05 + 19:35 để đóng `FU-373` và `FU-366`.

---

*Báo cáo này đẩy **cùng phiên** với commit (A55 · §57.2).*
