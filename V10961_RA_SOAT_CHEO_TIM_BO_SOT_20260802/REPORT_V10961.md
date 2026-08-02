# REPORT V10961 — Rà soát chéo tìm bỏ sót (02/08/2026)

## 1. Tóm tắt

Phiên chỉ-đọc đối chiếu Notion với hồ sơ nội bộ và tự kiểm máy. Notion truy cập được. Tìm thấy khoảng **10 chỗ lệch/bỏ sót thật**; runtime VPS **nhất quán 16/16 lệch 0**. Không sửa code, không deploy (QD-014). Không ghi Notion (A55).

## 2. Owner yêu cầu gì

Nguyên văn: *"Còn gì nữa không em? Còn phát hiện nào không? Đã tra soát hết chưa còn chỗ nào không? Đã đối chiếu với Notion chưa kẻo bỏ sót nữa."*

Ràng buộc: Notion chỉ đọc; phiên chỉ đọc + ghi tài liệu; version V10961; đẩy hai repo đúng phạm vi.

## 3. Đào bới / phát hiện

### 3.1 Notion (đọc qua MCP `user-notion`)

| Nguồn | Phát hiện |
|---|---|
| CURRENT CONTROL (cập nhật 01/08 16:43) | Báo cáo mới nhất **V10936**; V10934/V10936 `CODE_READY / NOT_DEPLOYED` |
| LOCK-IN trên HOME | FINAL MN 15:45 · MT **16:58** · MB **17:58** — khớp code |
| Owner Decision Ledger (Notion D-01…D-12) | D-10 khóa 16:58; D-11 HOLD deploy V10934/36; D-12 không thêm model trong lúc audit |
| Open items OI-01…OI-10 | Nhiều mục P0 vẫn OPEN trên Notion (audit runtime, metric canon, union pre-draw…) |
| HOME Snapshot | Vẫn còn đoạn 05/07: FREEZE 15:55/16:55/17:55 — lỗi thời nặng |

Đối chiếu nội bộ: V10936 **đã deploy** (V10939); V10934 **hủy/thay** bởi V10937 (gọi `gpt-5.4` về thay `combo-no-token`). Notion đứng ở trước các quyết định QD-013/014/015 (đúng quy tắc A55 — không ghi thêm sau 11:04 ngày 01/08).

Quyết định trên Notion chưa có mã OD/QD tương ứng rõ trong `OWNER_DECISION_LEDGER.json`: D-01 (Current Control SSOT), D-02 (GitHub full / Notion summary), D-04/D-05 (roster quality), D-06/D-07 (DEHERD), D-08 (cắt grok-4.20), D-09 (cấm promote bằng backtest union). Nhiều nội dung đã nằm trong CHANGELOG/DECISION_LOG lịch sử nhưng **chưa gắn `kiem_code` trong sổ máy**.

### 3.2 Hồ sơ nội bộ + máy

| Kiểm | Kết quả |
|---|---|
| `_v10920_session_start.py` | 0 checkpoint quá hạn · 0 FU quá hạn (sau V10958) |
| `_v10920_decision_ledger.py` | **OD-20260731-A TRÔI 4/4** (kiểm 16:53; code đã 16:58) · các mục khác khớp |
| `_v10925_rule_sync_check.py` | Sáu mặt đồng bộ dấu hiệu · `.mdc` tự nạp |
| `_v10921_report_gate.py` | Thiếu V10952b · V10953 · V10955b; V10954 tiêu đề không dấu → cổng báo thiếu phần |
| FU CHANGELOG ↔ TRACKER | 0 mã trong CHANGELOG mà thiếu TRACKER |
| VPS `_v10900_consistency_guard.py` | **16 phép · lệch 0** |
| VPS snapshot | FINAL 16:58/17:58 · edge 3pp/z2 · 15 model · combo AI 9 / ML 4 |

### 3.3 Số liệu VPS (evidence/vps_snap_20260802.json)

Official 15: `claude-opus-4-6`, `claude-sonnet-4-6`, `combo-super`, `deepseek-reasoner`, `gemini-2.5-flash`, `gemini-2.5-pro`, `glm-5.1`, `gpt-5.4`, `gpt-oss-120b`, `lstm`, `meta-learning`, `random-forest`, `smart-ensemble`, `smart-ml`, `xgboost`.

## 4. Hướng xử lý và vì sao chọn

Chỉ **ghi nhận + FU**, không sửa ledger/quy tắc số trong phiên này: (1) QD-014 đóng băng đường ra số; (2) hai agent song song V10959/V10960 cũng ghi cùng file tài liệu — tránh đụng nội dung quyết định; (3) lệch OD-20260731-A là lệch **tài liệu**, không phải code đang chạy sai giờ.

Phương án loại: tự SUPERSEDED OD + sửa CLAUDE ngay — đúng hướng nhưng dễ xung đột commit và nằm sát phạm vi “đóng băng”; để FU-219 hạn 09/08.

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `CHANGELOG.md` | Prepend V10961 qua `_doc_prepend.prepend()` |
| `docs/CURRENT_TRUTH_SSOT.md` | Prepend bảng truth |
| `docs/FOLLOW_UP_TRACKER.md` | FU-219 · FU-220 · FU-221 |
| `docs/AUTOMATION_STATE.json` | `governance_seq` +1 · `_v10961_last_event` |
| `docs/AUTOMATION_HISTORY.jsonl` | 1 dòng sự kiện |
| `web/backend/_v10961_governance.py` | Script ghi tài liệu (không deploy) |
| Public `V10961_RA_SOAT_CHEO_TIM_BO_SOT_20260802/` | REPORT + CONTEXT + evidence |

Backup runtime: không áp dụng (không sửa runtime). Không deploy.

## 6. Cổng kiểm

| Mục | Kết quả |
|---|---|
| Session start | Đạt — 0 quá hạn |
| Decision ledger | 1 mục TRÔI (OD-20260731-A) — đã ghi FU-219 |
| Rule sync | Đạt |
| Consistency VPS | 16/16 đạt |
| Report gate (phiên cũ) | 4 phiên bản thiếu/không đạt — FU-220 |
| Notion ghi | Không gọi — đạt A55 |
| Hash 4 bảng | Không áp dụng (không deploy) |

## 7. Vướng vấp

| # | Vấp | Hậu quả nếu bỏ qua |
|---|---|---|
| 1 | Sổ quyết định còn mốc 16:53 | Mỗi phiên đầu báo TRÔI giả → agent có thể dừng hoặc sửa nhầm code về 16:53 |
| 2 | Notion CURRENT CONTROL đứng V10936 | Owner đọc Notion tưởng V10936 chưa deploy / thiếu QD-013+ |
| 3 | Báo cáo thiếu A55 | Vi phạm cứng nếu coi các phiên đó đã “xong” |
| 4 | File `.cmd` tạm còn ở gốc | Bẩn repo; dễ commit nhầm |
| 5 | Agent song song V10959/V10960 | Có thể đụng CHANGELOG/SSOT/FU — đã đọc lại đầu file trước khi ghi |

## 8. Gỡ về

Chỉ tài liệu: `git revert` commit V10961 ở hai repo; hoặc xóa khối prepend V10961 ở đầu CHANGELOG/SSOT/FU và hạ `governance_seq`. Không có backup runtime vì không đụng VPS. Mất khoảng 2 phút.

## 9. Theo dõi tiếp

| Mã | Việc | Hạn |
|---|---|---|
| FU-219 | SUPERSEDED OD-20260731-A + cập nhật mặt quy tắc 16:58 | 2026-08-09 |
| FU-220 | Bổ sung báo cáo V10952b/V10953/V10955b + sửa tiêu đề V10954 | 2026-08-05 |
| FU-221 | Notion lỗi thời — owner tự cập nhật tay nếu cần; agent không ghi Notion | 2026-08-15 |
| QD-014 / FU-215 | Đóng băng đường ra số tới hết 08/08 | 2026-08-08 |
