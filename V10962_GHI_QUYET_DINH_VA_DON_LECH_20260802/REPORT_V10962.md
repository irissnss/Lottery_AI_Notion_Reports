# REPORT V10962 — Ghi quyết định QD-016/QD-017 + dọn lệch mốc giờ + bù báo cáo A55 (02/08/2026)

**Ngày:** 02/08/2026 · **Commit riêng:** *(điền sau push)* · **Commit công khai:** *(điền sau push)* · **Trạng thái:** chỉ tài liệu — không sửa runtime, không deploy

---

## 1. Tóm tắt

Ghi **QD-016** (shadow bỏ lệnh bắt buộc RULES-FIRST sau 08/08) và **QD-017** (A/B hai prompt cùng model ≥14 ngày). Sửa lệch tài liệu: FINAL MT/MB **16:58/17:58** (không còn 16:53/17:53) trên năm mặt quy tắc + MOC_FINAL + playbook + mệnh đề `kiem_code` OD-20260731-A. Bù báo cáo V10952b/V10953/V10955b; sửa tiêu đề V10954. Xoá **29** file `.cmd` rác ở gốc. Notion ghi chú: chỉ còn kho lịch sử tới 01/08 16:43.

## 2. Owner yêu cầu gì (nguyên văn)

> *"Duyệt trước: sau 08/08 bỏ lệnh 'bắt buộc chọn từ danh sách' trên luồng bóng để đo — vẫn đưa danh sách như gợi ý, chỉ bỏ chữ bắt buộc."*

> *"Có, duyệt trước để 08/08 tự chạy. Chọn vài model đại diện, chạy ≥ 14 ngày, đo bằng bạch thủ."*

Kèm brief V10962: sửa lệch 16:53→16:58; bù A55; dọn `.cmd`; ghi Notion chỉ là lịch sử; liệt kê D-01…D-12 đề xuất (không tự thêm); đẩy hai repo; không đụng Notion ghi; không sửa code chạy / không deploy.

## 3. Đào bới / phát hiện

**Căn cứ QD-016 (V10959):** prompt↔prompt BT overlap 24–27% (ngẫu nhiên ~1%); ML↔prompt 1,6%. RULES-FIRST list ~11 số: số thật trong list 12,4%; model pick trong list 35,8%.

**Lệch mốc giờ:** code/VPS `FREEZE_MARKS` = 15:45/16:58/17:58 từ V10931; sổ + CLAUDE/MOC_FINAL/cursorrules còn 16:53/17:53 → `_v10920_decision_ledger.py` báo OD-20260731-A **TRÔI 4/4** (nguy cơ agent sửa ngược code).

**A55:** thiếu V10952b, V10953, V10955b; V10954 tiêu đề không dấu → cổng không nhận "tóm tắt"/"đã làm gì".

**Notion:** đứng đông 01/08 16:43; vẫn nói V10936 chưa deploy / gpt-5.4 shadow — sai so với SSOT/VPS.

## 4. Hướng xử lý và vì sao chọn

1. Ghi QD + FU OWNER_LOCK hạn 08/08 — **chưa dựng code** (tránh deploy trong QD-014).
2. Sửa mệnh đề kiểm + tài liệu quy tắc hiện hành về 16:58/17:58; giữ nguyên văn 31/07 và ghi chú V10931 trong lịch sử.
3. Bù/sửa báo cáo công khai thay vì bỏ qua cổng A55.
4. Xoá `.cmd` gốc + `/*.cmd` trong `.gitignore`; không đụng `scripts/*.cmd` thật.
5. Liệt kê D-01…D-12 đề xuất — **không tự thêm** vào sổ máy.

Loại: sửa code FREEZE về 16:53 — **cấm** (production đúng 16:58).

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `docs/OWNER_DECISION_LEDGER.json` | QD-016, QD-017; sửa `kiem_code` OD-20260731-A → 16:58 |
| `CLAUDE.md` / `AGENTS.md` / `.cursorrules` / `.AGENT.md` / `.Antigravityrules.md` | FINAL 16:58/17:58; Notion = kho lịch sử |
| `docs/MOC_FINAL_TOTAL_OUTPUT.md` · `CO_CHE_…` · playbook §1 | Khớp mốc hiện hành |
| `_v10925_rule_sync_check.py` | Dấu hiệu §55 → 16:58/17:58 |
| Public V10952b / V10953 / V10955b / V10954 / V10962 | Bù/sửa A55 |
| Gốc repo `*.cmd` | Xoá 29 file; `.gitignore` thêm `/*.cmd` |
| CHANGELOG / SSOT / FOLLOW_UP / AUTOMATION_STATE | Prepend V10962 (cuối phiên) |

Backup ledger: `backups/v10962_pre/OWNER_DECISION_LEDGER.json`.

**Không deploy · không restart · không đụng 4 bảng khoá.**

### Thiết kế QD-017 (chưa code)

| Model | Vai trò | Lý do |
|---|---|---|
| `claude-sonnet-4-6` | mạnh | Official AI mạnh, dễ bị RULES-FIRST kéo |
| `deepseek-reasoner` | trung | Đã từng PROMPT_V2_AB rồi tắt 01/08 |
| `gemini-2.5-flash` | rẻ | Chi phí thấp để đo hướng hiệu ứng |

Chi phí ước: 3×3×14 = **126 lần gọi thêm** ≈ **15–25 USD / 14 ngày**.

## 6. Cổng kiểm

- `_v10920_decision_ledger.py` — **0 TRÔI** sau khi có FU-225/226
- `_v10925_rule_sync_check.py` — sáu mặt đồng bộ
- `_v10921_report_gate.py` V10952b/V10953/V10954/V10955b/V10962 — đạt sau commit+push
- Không deploy → không so hash 4 bảng (không áp dụng)

## 7. Vướng vấp

1. FU-224 đã dùng (frontend) → QD dùng **FU-225/226**; FU-222/223 giữ liên kết.
2. Agent khác có thể đang ghi CHANGELOG/SSOT/FU — chờ mtime ≥60s rồi mới `prepend()`.
3. Cổng A55 chỉ đọc tiêu đề có dấu — V10954 "Tom tat" trượt; đã sửa.
4. Hậu quả nếu bỏ lệch 16:53: agent khác "sửa" production về 16:53 → hỏng hạn MT/MB.

## 8. Gỡ về

- Ledger: `copy backups/v10962_pre/OWNER_DECISION_LEDGER.json docs/`
- Quy tắc: `git checkout -- CLAUDE.md AGENTS.md .cursorrules .AGENT.md .Antigravityrules.md docs/MOC_FINAL_TOTAL_OUTPUT.md`
- Báo cáo công khai: xoá thư mục V10962 + ba thư mục bù; revert tiêu đề V10954
- Thời gian: <5 phút (chỉ tài liệu)

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng / hạn |
|---|---|---|
| **FU-225** (QD-016) | Dựng shadow bỏ bắt buộc RULES-FIRST | Khởi động **2026-08-08**; overlap BT ≤10% / ≥14 ngày |
| **FU-226** (QD-017) | A/B 2 prompt × 3 model | ≥14 ngày; chấm bạch thủ; chi phí theo dõi |
| **FU-219** | Lệch 16:53 | **ĐÓNG** sau V10962 |
| **FU-220** | Báo cáo A55 thiếu | **ĐÓNG** sau V10962 |
| **FU-221** | Notion lỗi thời | OWNER_LOCK — không ghi Notion |
| D-01…D-12 Notion | Đề xuất đưa vào sổ máy | **Chờ owner chọn** — không tự thêm |

### Đề xuất D-01…D-12 (chưa thêm vào sổ)

Theo V10961 / Notion Owner Decision Ledger (đứng đông 01/08 16:43):

| Mã | Nội dung ngắn | Đề xuất |
|---|---|---|
| D-01 | Current Control SSOT trên Notion | Có thể SUPERSEDED bởi SSOT nội bộ + A55 |
| D-02 | GitHub full / Notion summary | Đã thành §57 — có thể gắn OD-20260801-F |
| D-04/D-05 | Roster quality | Rà còn hiệu lực sau V10931/V10937 |
| D-06/D-07 | DEHERD | Rà còn hiệu lực |
| D-08 | Cắt grok-4.20 | Có thể đã thực hiện — cần `kiem_code` |
| D-09 | Cấm promote bằng backtest union | Nên giữ — khớp bài học backtest rữa |
| D-10 | Khóa FINAL 16:58 | Đã khớp OD-20260731-A sau V10962 |
| D-11 | HOLD deploy V10934/36 | **Lỗi thời** — đã deploy/thay; không mang vào sổ như ACTIVE |
| D-12 | Không thêm model lúc audit | Có thể gộp QD-014 cửa sổ đóng băng |
