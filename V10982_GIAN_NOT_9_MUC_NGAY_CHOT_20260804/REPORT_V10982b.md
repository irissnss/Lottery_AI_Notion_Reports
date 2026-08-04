# V10982b — Owner duyệt chuyển `FU-224` từ 09/08 xuống 06/08 (`QD-022` bổ sung) · siết phép J5

> **Phiên bổ sung của V10982** · 2026-08-04 12:4x (giờ VN)
> Bổ sung cho `REPORT_V10982.md` cùng thư mục. Ngữ cảnh hội thoại dùng chung
> `CONVERSATION_CONTEXT_V10982_20260804.md`.
>
> **Vì sao có báo cáo riêng (viết bổ sung 05/08 trong V10986):** `CHANGELOG.md` có khối
> `## V10982b` nên cổng `_v10921_report_gate.py` đòi báo cáo riêng. Ngày 04/08 chỉ chạy
> `report_gate V10982` (một phiên bản) nên bản quét toàn bộ trượt mà không ai thấy. V10986 vá bằng
> cách viết đúng báo cáo còn thiếu, **không nới cổng**.

---

## 1. Tóm tắt một đoạn

Báo cáo V10982 mục 6 nêu đề nghị: ngày 09/08 gánh **9 mục** trong đó 3 mục nặng của nhóm 14, mà
`FU-224` (*Dọn trang frontend trùng/chết*) chỉ đụng file HTML/JS nên chuyển được. Owner chọn
chuyển xuống **06/08**. Ngày nặng nhất 09/08 giảm **9 → 8**; ngày chốt 10/08 **không đổi, vẫn 3**.
Cùng phiên siết phép **J5** vì phát hiện bảng mốc tải ghi cứng có thể lệch với sổ thật mà không
cổng nào bắt.

## 2. Owner yêu cầu gì — nguyên văn

> **Owner ký 2026-08-04 12:4x** (giờ VN): *"Chuyển xuống 06/08 - 09/08 còn 8 mục"*

Đây là owner **chọn một trong các phương án** agent trình ở mục 6 của báo cáo V10982, không phải
yêu cầu mới.

## 3. Đào bới / phát hiện

| | |
|---|---|
| Hạn | 09/08 → **06/08** |
| Mã đọc | `UI0809` → `UI0806` (MMDD khớp hạn mới) |
| Nhãn | `OWNER_LOCK` — **giữ nguyên** |

Tải từng ngày sau khi chuyển:

| Ngày | 04/08 | 05/08 | 06/08 | 07/08 | 08/08 | 09/08 | 10/08 |
|---|---|---|---|---|---|---|---|
| Tổng | **3** | **6** | **6** | **4** | **5** | **8** | **3** |

**Phát hiện phụ — chỗ xanh giả suýt lọt:** phép J5 vốn chỉ đọc **bảng mốc tải ghi cứng**
(`TAI_PHIEN_KHAC_DO_DUOC` trong `_v10982_lich9.py`). Nếu chỉ đổi hạn `FU-224` trong sổ mà quên bảng
mốc thì mọi con số tải trong `CHANGELOG`, trang lịch và báo cáo đều sai **mà không cổng nào bắt
được** — cổng vẫn xanh vì nó so bảng mốc với chính bảng mốc.

## 4. Hướng xử lý và vì sao chọn

**Vì sao chuyển được `FU-224`:** mục này chỉ đụng file HTML/JS frontend (`viewer.html` chết ·
`v82-monitor` trùng `monitoring` · `user-view` đông · route `/nghiem-thu` mồ côi · API filter 2 số
cuối chết ở FE) — **KHÔNG chạm runtime dự đoán**, không chạm 5 thứ `QD-014` cấm đích danh, nên làm
được trong cửa sổ đóng băng.

Chuyển xuống 06/08 kéo ngày nặng nhất 09/08 từ 9 xuống 8, trong khi 06/08 chỉ lên 6 — bằng trần
thực tế phiên này nhận. **Trần ≤5 vẫn không đạt** (05/08 và 06/08 đều 6) — nói thẳng thay vì ép số
cho đẹp.

**Cái gì GIỮ NGUYÊN:** nhãn `OWNER_LOCK` giữ nguyên. Owner duyệt việc **ĐỔI NGÀY**, chưa duyệt việc
xử từng trang — `next_action` vẫn là *«Owner chọn: giữ / gộp / bỏ. Agent KHÔNG tự xoá trang.»* Ngày
06/08 agent chỉ được trình phương án, **không tự merge/xoá**.

**Với J5:** chọn siết thành đối chiếu bảng mốc với **sổ theo dõi THẬT**, trượt nếu lệch — thay vì
thêm phép thứ 9. Vẫn giữ 8 phép.

## 5. Đã làm gì

| File | Việc |
|---|---|
| `web/backend/_v10982_lich9.py` | `TAI_PHIEN_KHAC_DO_DUOC` cập nhật · thêm `QD_BO_SUNG_224` · thêm `tai_phien_khac_that()` + `lech_moc_phien_khac()` |
| `web/backend/_v10982_kiem_lich9.py` | J5 siết: đối chiếu mốc tải với sổ thật |
| `web/backend/_v10982b_ghi_so.py` | **MỚI** — ghi khối chuyển hạn qua `prepend()` |
| `web/backend/_v10982b_ghi_quyet_dinh.py` | **MỚI** — bổ sung `QD-022`, +2 mệnh đề kiểm |
| `web/backend/_v10982b_gov.py` `_v10982b_probe.py` | **MỚI** |
| `web/backend/_v10981_trang_lich.py` | đề nghị → đã duyệt · thêm §8.5 |
| `docs/FOLLOW_UP_TRACKER.md` | khối V10982b (+3.441 ký tự, prepend) |
| `docs/LICH_CUON_CHIEU_DEN_10082026.md` | sinh lại · 32.718 → 34.919 byte |
| `docs/OWNER_DECISION_LEDGER.json` | `QD-022` bổ sung · vẫn 24 quyết định, **không mở QD mới** · mệnh đề kiểm 7 → **9** |

`docs/ACTIVE_ROADMAP_*.md`: **không áp dụng** — đã soát, không roadmap nào tham chiếu `FU-224`.
Backup: `backups/v10982b_pre/` (8 file). **Không deploy, không đụng runtime.**

## 6. Cổng kiểm

| Cổng | Kết quả |
|---|---|
| `_v10982_kiem_lich9.py` | **8/8 ĐẠT** · `GIAN_9_MUC_DAT` |
| `_v10981_kiem_lich.py` (nhóm 14) | **8/8 ĐẠT** |
| `_v10920_decision_ledger.py` | **0 TRÔI** · `QD-022` khớp **9/9** |
| Mồ côi toàn sổ | **18** — không tăng |
| `_v10921_report_gate.py V10982` | exit 0 |
| **Thử ngược J5** | chạy cổng khi mốc đã đổi nhưng sổ chưa đổi → **J5 TRƯỢT**, in đúng tên `FU-224` ở cả hai ngày lệch |

**Xác minh lại 05/08 (V10986):** `_v10982_kiem_lich9.py` vẫn **8/8 ĐẠT**; J5 in tải thật
04/08=3 · 05/08=5 · 06/08=6 · 07/08=5 · 08/08=5 · 09/08=8 · 10/08=3, mốc tải khớp sổ thật 7/7 ngày.
`QD-022` khớp **9/9** trong sổ quyết định.

## 7. Vướng vấp

**Cổng so chính mình với chính mình.** J5 bản cũ đọc bảng mốc ghi cứng rồi so với… bảng mốc ghi
cứng. Luôn xanh. Chỉ lộ ra khi phiên này phải đổi một hạn và tự hỏi *"nếu quên bảng mốc thì cổng có
biết không?"* — câu trả lời là **không**.

**Hậu quả nếu bỏ qua:** mọi con số tải trong lịch, changelog và báo cáo sẽ trôi dần khỏi sổ thật,
trong khi cổng vẫn báo đạt. Đến ngày chốt mới biết lịch sai.

**Đã thử ngược mới dám nói là vá được** — không chỉ sửa rồi tuyên bố xong.

## 8. Gỡ về

Đổi ô `due`/`deadline` của `FU-224` về `2026-08-09`, mã đọc về `UI0809`, trả
`TAI_PHIEN_KHAC_DO_DUOC` về mốc cũ. **~2 phút.** Backup: `backups/v10982b_pre/`.

## 9. Theo dõi tiếp

| Mã | Mã đọc | Việc | Ngưỡng bằng số | Hạn |
|---|---|---|---|---|
| `FU-224` | `UI0806` | Dọn trang frontend trùng/chết | agent **chỉ trình phương án**, owner chọn giữ/gộp/bỏ | 06/08 |

`QD-014` còn hiệu lực hết 08/08. Trần ≤5 mục/ngày **chưa đạt** (06/08=6 · 09/08=8) — ghi nhận thẳng,
theo dõi tiếp trong V10986 phần "còn nợ".
