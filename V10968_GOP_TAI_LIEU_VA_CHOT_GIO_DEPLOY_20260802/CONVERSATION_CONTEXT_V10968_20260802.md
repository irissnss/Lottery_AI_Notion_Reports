# CONVERSATION_CONTEXT_V10968_20260802

## Owner (nguyên văn, rút từ yêu cầu phiên)

Hai việc dọn dẹp nhỏ, khắc phục hai sai sót trong phiên hôm nay.

Việc 1: gộp `docs/CO_CHE_HOC_VA_XEP_HANG.md` (bản đầy đủ) và `docs/CAC_CO_CHE_HOC_CUA_HE.md` (bản rút); giữ bản đầy đủ làm chính; chuyển bản rút vào archive kèm dòng ghi đã gộp; sửa liên kết; giải thích nếu đếm 14 vs 18 khác nhau.

Việc 2: thêm chốt máy chặn deploy trong giờ chạy dự đoán vào `governance_guard.py`; khung đề xuất 05:00–06:30 và 15:30–18:15 giờ VN sau khi xem crontab VPS; đường thoát `DEPLOY_KHAN=1` có nhật ký; thử thật 3 trường hợp; báo cáo V10968; đẩy 2 repo; không Notion; không đụng QD-014; không cần deploy VPS.

## Agent làm gì

1. Chạy `_v10920_session_start.py` — 0 checkpoint quá hạn.
2. Đọc đối chiếu hai tài liệu; bổ sung phần thiếu vào bản chính; giải thích tiêu chí đếm; archive bản rút; sửa link.
3. Đối chiếu crontab VPS + playbook; chốt khung cấm như đề xuất owner.
4. Sửa `governance_guard.py` (giờ VN, deny, KHAN log, UTF-8).
5. Chạy 3 phép thử → đạt; ghi artifacts.
6. prepend CHANGELOG/SSOT/FU; bump governance_seq 386; FU-236 CLOSED · FU-237 DP0815.
7. Báo cáo công khai + push 2 repo.

## Vấp ở đâu

- PowerShell backtick làm hỏng dòng đầu archive → ghi lại bằng Python.
- Console cp1252 crash khi in deny tiếng Việt → reconfigure UTF-8 trong hook.
- Phép thử ngoài khung ra `ask` (doc sync) chứ không `allow` vì tree bẩn — ghi rõ trong báo cáo để không hiểu nhầm chốt giờ.
