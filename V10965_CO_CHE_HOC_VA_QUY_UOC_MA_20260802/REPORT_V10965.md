# V10965 — Cơ chế học của hệ + đề xuất quy ước mã công việc

**Ngày:** 02/08/2026 · **Commit riêng:** `ad525ed` · **Commit công khai:** `88f1b68` · **Trạng thái:** chỉ tài liệu, không deploy

---

## 1. Tóm tắt

Phiên chỉ đọc code và kiểm VPS, viết hai tài liệu: (1) toàn bộ cơ chế học đang chạy — ML retrain sống, RULES-FIRST đang hại, optimizer chạy nhưng lift âm, nhiều bảng xếp hạng chạy cho có; (2) đề xuất mã công việc dạng `TH0808` với ba phương án, khuyến nghị giữ mã máy kèm nhãn đọc. Không sửa runtime (QD-014).

## 2. Owner yêu cầu gì (nguyên văn)

> *"Rồi các cơ chế như học tập tích luỹ, xếp hạng, retrain của các model LLM và ML thì sao, em đã đào sâu hết cỡ chưa? Viết chi tiết cụ thể tất cả mọi thứ hiện đang code để kiểm soát, tổng hợp thật đầy đủ."*

> *"Số hiệu công việc cần quy chuẩn chứ kiểu như PL6 gì đó khó nhận biết quá. Số hiệu phải viết tắt đầu mục công việc và hạn ngày, ví dụ Kiểm Soát 08/08 thì số hiệu viết tắt phải viết là TH0808 chẳng hạn, thế dễ đọc hơn."*

Kèm chỉ thị phiên: chỉ đọc và viết tài liệu, không sửa code chạy, không deploy; version V10965; đẩy báo cáo công khai; không đụng Notion.

## 3. Đào bới / phát hiện

### Cơ chế học (VPS 02/08)
- Retrain CN 02:02 RETRAINED; guard 06:30 FRESH_SKIP; AUC khớp số owner (MT lstm 0,5554 … MB meta 0,4768).
- Optimizer 03:15 xong; lift MN −4,75 / MT −10,95 / MB −8,47; trọng số đang được STAT dùng.
- mined_rules 105 active `v2026W31`; effectiveness 3173 dòng tới 01/08.
- RULES-FIRST: bằng chứng V10959 — list 12,4% ≈ ngẫu nhiên, model pick 35,8%.
- Optuna: không có thư mục tham số trên VPS.
- Crontab xác nhận: 06:30 retrain_guard, 07:00 weekly_guard, 09:05/09:10/09:15 progress/scoreboard/weakest, 21:25 quality ledger.

### Hệ mã
- FU treo ~72; QD 5; OD 12; CP mở ~18–23; D-01…12 Notion đóng băng; PL-1/2 ad-hoc.
- FU-225 bị dùng kép cùng ngày (UI V10964 vs QD-016) — triệu chứng mã số thuần.

Chi tiết đầy đủ trong hai file kèm thư mục này.

## 4. Hướng xử lý và vì sao chọn

- Việc 1: viết một tài liệu duy nhất thay vì để kiến thức rải CHANGELOG — vì owner cần kiểm soát, không cần thêm code trong cửa sổ đóng băng.
- Việc 2: chỉ đề xuất, không tự đổi — vì đổi mã đứt parser và lịch sử; đưa 3 phương án để owner chọn.
- Loại phương án A (đổi hàng loạt ngay) làm mặc định vì rủi ro cao; khuyến nghị B.

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `docs/CAC_CO_CHE_HOC_CUA_HE.md` | Tạo mới |
| `docs/DE_XUAT_QUY_UOC_MA_CONG_VIEC.md` | Tạo mới |
| `CHANGELOG.md` / `CURRENT_TRUTH_SSOT.md` / `FOLLOW_UP_TRACKER.md` | prepend V10965 + FU-227/228 |
| `docs/AUTOMATION_STATE.json` | governance_seq +1, `_v10965_last_event` |
| Repo công khai thư mục này | Chép 2 tài liệu + REPORT + CONTEXT |

Backup: không cần backup runtime (không sửa code chạy). Deploy: không áp dụng.

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Đọc code 6 nhóm A–F | Đạt — có file:hàm:giờ |
| Crontab VPS learning jobs | Đạt — liệt kê trong tài liệu |
| `training_history` AUC 02/08 | Đạt — 12/12 dòng có AUC |
| Optimizer marker / weekly_guard | Đạt — FRESH cùng ngày |
| mined_rules count | Đạt — 105/105 active |
| Không deploy / không Notion write | Đạt |
| QD-014 tôn trọng | Đạt |

## 7. Vướng vấp

1. PowerShell phá SQL có dấu phẩy trong `round(auc,4)` → phải chuyển sang script paramiko. **Hậu quả nếu bỏ qua:** không lấy được số sống, tài liệu chỉ chép docs cũ.
2. Agent V10964 ghi cùng CHANGELOG/SSOT/FU — phải chờ mtime >60s. **Hậu quả nếu bỏ qua:** ghi đè chéo mất entry vừa thêm.
3. Cột DB lệch tên (`setting_key` không phải `key`; `mined_at` không phải `created_at`) — probe lần đầu lỗi. **Hậu quả nếu bỏ qua:** kết luận sai “không có trọng số học / không có luật”.
4. FU-225 trùng số hai nghĩa — nêu trong đề xuất mã. **Hậu quả nếu bỏ qua:** briefing/parser chỉ thấy một việc.

## 8. Gỡ về

Không áp dụng runtime. Xoá tài liệu:

```
git -C E:/Lottery_AI_Test checkout -- docs/CAC_CO_CHE_HOC_CUA_HE.md docs/DE_XUAT_QUY_UOC_MA_CONG_VIEC.md
# và revert prepend CHANGELOG/SSOT/FU/AUTOMATION_STATE nếu cần
```

Repo công khai: xoá thư mục `V10965_CO_CHE_HOC_VA_QUY_UOC_MA_20260802/`.

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng | Hạn |
|---|---|---|---|
| FU-227 | Owner chọn A/B/C quy ước mã | Có QD ghi sổ trước khi đổi mã | 08/08 |
| FU-228 | Đo A/B hiệu quả cơ chế học sau đóng băng | ≥14 ngày, bạch thủ ≥ nền +3pp (z≥2) mới giữ | 15/08 |
| QD-016/017 | Đã duyệt — chạy sau 08/08 | theo thiết kế sẵn | 08/08 |
