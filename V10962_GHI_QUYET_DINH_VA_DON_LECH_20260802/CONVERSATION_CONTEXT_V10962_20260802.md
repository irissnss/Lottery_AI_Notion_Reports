# CONVERSATION_CONTEXT V10962 — 2026-08-02

## Owner nguyên văn (phiên này)

1. *"Duyệt trước: sau 08/08 bỏ lệnh 'bắt buộc chọn từ danh sách' trên luồng bóng để đo — vẫn đưa danh sách như gợi ý, chỉ bỏ chữ bắt buộc."* → **QD-016**

2. *"Có, duyệt trước để 08/08 tự chạy. Chọn vài model đại diện, chạy ≥ 14 ngày, đo bằng bạch thủ."* → **QD-017**

3. Brief V10962: sửa lệch tài liệu FINAL 16:53→16:58 (MB 17:58); bù báo cáo A55 V10952b/V10953/V10955b + sửa tiêu đề V10954; dọn `.cmd` gốc; ghi Notion chỉ là lịch sử tới 01/08 16:43; liệt kê D-01…D-12 đề xuất (không tự thêm); đẩy hai repo; không ghi Notion; không sửa code chạy / không deploy (QD-014).

## Agent làm gì

- Chạy `_v10920_session_start.py` (0 checkpoint quá hạn theo script mới).
- Ghi QD-016/QD-017 vào `OWNER_DECISION_LEDGER.json`; sửa `kiem_code` OD-20260731-A → 16:58 + ghi chú V10931.
- Cập nhật CLAUDE / AGENTS (sinh máy) / .cursorrules / .AGENT.md / .Antigravityrules.md / MOC_FINAL / CO_CHE / playbook §1 / rule_sync dấu hiệu.
- Bù 3 báo cáo công khai + sửa V10954; viết REPORT_V10962.
- Xoá 29 file `.cmd` gốc; thêm `/*.cmd` vào `.gitignore`.
- Prepend CHANGELOG/SSOT/FOLLOW_UP; tăng governance_seq; push hai repo.

## Vấp

- FU-224 đã chiếm → dùng FU-225/226.
- Chờ mtime file tài liệu chung trước khi prepend (tránh đụng agent khác).
- Cổng A55 cần tiêu đề có dấu tiếng Việt.
