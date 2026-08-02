# CONVERSATION_CONTEXT V10972 — 2026-08-02

## Owner (nguyên văn)

> Owner: repo/folder `Lottery_AI_Test` ~240GB — không thể copy nguyên si sang máy local mới. Cần hướng dẫn thực tế: gì chiếm dung lượng, gì BẮT BUỘC mang, gì bỏ/clone lại, quy trình bàn giao nhẹ.
>
> ## Workspace
> `E:/Lottery_AI_Test` (Windows). Public reports có thể ở `E:/Lottery_AI_Notion_Reports`.
>
> ## Việc làm
> ### 1. Đo dung lượng ... Top-level ... >1GB ... phân loại A–E
> ### 2. Quy trình bàn giao NHẸ ... git clone 2 repo ... secrets thủ công ... KHÔNG copy data/backups/artifacts ...
> ### 3. Ước tính kích thước sau khi clone sạch
> ### 4. Deliverable V10972 ... REPORT + CONTEXT + HUONG_DAN + evidence ... mirror docs ... push ... gate PASS
> ### 5. Trả về parent: bảng GB, ước máy mới, 5–7 bước, link, cảnh báo
>
> Hard: Notion chỉ đọc; không deploy production; giờ VN; không in API keys.

## Agent đã làm

1. Chạy `_v10920_session_start.py` — 0 checkpoint quá hạn.
2. Đo top-level: `artifacts` 241.94 GB · `backups` 9.67 · `data` 1.72 · … tổng ≈254 GB.
3. Đào `artifacts/live_sync`: 547 snapshot, 241.1 GB; DB lặp ~600 MB/bản.
4. `git count-objects` private pack ~95 MiB; tracked working tree ~86.5 MB; public ~42 MB.
5. Viết `HUONG_DAN_MAY_MOI_NHE.md`, `REPORT_V10972.md` (9 phần), evidence CSV/summary.
6. Mirror `docs/BAN_GIAO_NHE_KHONG_COPY_240G_V10972.md`; prepend CHANGELOG / SSOT / FOLLOW_UP (FU-241).
7. Push public + private; chạy gate V10972.
8. **Không** đọc/in nội dung `.env` (chỉ ghi size 773 bytes). **Không** Notion write. **Không** deploy.

## Vấp

- Quét “file ≥1GB” dễ bỏ sót live_sync (nhiều file ~600MB) — đã đo theo thư mục snapshot.
- Script đo `data/` lần 1 lỗi cú pháp PowerShell — đo lại.

## Không làm

- Không xoá `artifacts/live_sync` trên máy cũ (chỉ hướng dẫn; owner tự dọn nếu muốn).
- Không copy secrets vào git/report.
