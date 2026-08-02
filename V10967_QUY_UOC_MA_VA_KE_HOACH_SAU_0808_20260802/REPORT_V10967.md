# REPORT V10967 — Quy ước mã công việc (phương án B) + kế hoạch sau 08/08

Ngày: 2026-08-02 (giờ Việt Nam) · Phiên bản: V10967 · Không deploy VPS

---

## 1. Tóm tắt một đoạn

Áp quy ước mã **phương án B** (giữ mã máy, bắt buộc kèm mã đọc + nhãn + hạn): gắn nhãn cho **81 mục FU treo** (0 thiếu mã đọc), ghi `ma_doc` cho **19 quyết định** trong sổ (thêm QD-018/QD-019), gắn nhãn checkpoint mở trên 4 roadmap ACTIVE, sửa briefing đầu phiên hiện nhãn đọc, tách mã trùng FU-225→FU-231 và FU-222 frontend→FU-222b. Ghi kế hoạch sau 08/08 thành QD-018 (3 bước tuần tự, đo 7–14 ngày/bước) kèm FU-233/234/235; ghi sót V10938 thành FU-232 (chưa sửa code). Không đụng đường ra số.

## 2. Owner yêu cầu gì

> *"Số hiệu phải viết tắt đầu mục công việc và hạn ngày, ví dụ Kiểm Soát 08/08 thì số hiệu viết tắt phải viết là TH0808 chẳng hạn, thế dễ đọc hơn."*

Owner chọn phương án B (giữ mã máy + nhãn đọc).

> *"Tắt bộ tối ưu trọng số (đang làm tệ đi) · đo xem 105 luật có giúp gì không · gỡ lệnh bắt buộc chọn từ danh sách. Làm từng cái một để biết cái nào ăn thua."*

Ghi sót V10938: nửa trọng số số còn WR. Ràng buộc QD-014 đóng băng tới hết 08/08.

## 3. Đào bới / phát hiện

- FU treo trước khi gắn nhãn: parser báo 72; sau khi đọc thêm bullet `Trạng thái`/`Hạn` tiếng Việt + tách trùng: **81 treo**, **0 thiếu mã đọc**.
- **FU-225 dùng hai nghĩa** cùng ngày: (1) UI `/du-doan-test` sau V10964; (2) QD-016 bỏ ép RULES-FIRST. Bản (2) bị che vì reader chỉ giữ occurrence đầu → **tách thành FU-231**.
- **FU-222** cũng hai nghĩa: RULES-FIRST (giữ) vs đề xuất dọn frontend (đã có FU-224) → occurrence frontend đổi **FU-222b CLOSED**.
- Các cặp FU-194/199/219/220: chồng lịch sử đóng/mở cùng việc — bình thường, không tách.
- Căn cứ kế hoạch học: `docs/CAC_CO_CHE_HOC_CUA_HE.md` — tối ưu trọng số âm 3 miền; 105 luật chưa đo; RULES-FIRST pick 35,8% vs actual-in-list 12,4%.

## 4. Hướng xử lý và vì sao chọn

| Phương án | Chọn? | Lý do |
|---|---|---|
| A đổi mã hàng loạt | Không | Gãy parser, đứt báo cáo GitHub |
| **B giữ máy + nhãn đọc** | **Có** | Đúng owner; không gãy công cụ |
| C việc mới chỉ mã đọc | Sau | Có thể nâng sau 08/08 nếu B hữu ích |

Kế hoạch 3 bước tuần tự (không song song) để tách tác dụng; mỗi bước ≥7–14 ngày + ngưỡng tự cắt ≥3pp BT (z≥2).

## 5. Đã làm gì

| File / nhóm | Thay đổi |
|---|---|
| `docs/FOLLOW_UP_TRACKER.md` | Gắn nhãn treo; tách 225/222; prepend FU-232..235; đóng FU-227 |
| `docs/OWNER_DECISION_LEDGER.json` | `ma_doc` mọi QD/OD; QD-018; QD-019; QD-016→FU-231 |
| `docs/DE_XUAT_QUY_UOC_MA_CONG_VIEC.md` | APPROVED_B + bảng viết tắt chốt |
| `docs/ACTIVE_ROADMAP_*.md` (4 file) | Checkpoint mở kèm mã đọc |
| `_v10958_fu_reader.py` | Status/hạn VN; ma_doc; thieu_ma_doc; hien_thi |
| `_v10920_session_start.py` | Briefing hiện nhãn đọc + cảnh báo thiếu mã |
| `_v10920_decision_ledger.py` | sinh_md hiện mã đọc + 3 bước QD-018 |
| CLAUDE / AGENTS / .cursorrules / .AGENT / .Antigravityrules | §58 (A56) |
| CHANGELOG / SSOT / AUTOMATION_STATE | V10967; governance_seq 385 |

Backup: không đụng runtime VPS — không tạo `backups/v10967_pre/` (không deploy).

Hash 4 bảng official: **không áp dụng** (không deploy, không ghi DB sống).

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| `treo_items()` + `thieu_ma_doc()` | 81 treo · 0 thiếu mã đọc |
| `get_fu(FU-225)` | UI0803 · DEPLOYED_PENDING_LIVE_VERIFY |
| `get_fu(FU-231)` | HT0808-1 · OWNER_LOCK (QD-016) |
| `get_fu(FU-222b)` | CLOSED (gộp FU-224) |
| `_v10920_session_start.py` | Hiện dòng dạng `FU-189 · KS0802-1 · … · hạn 02/08` |
| Deploy VPS / hash 4 bảng | Không áp dụng — không deploy |
| `_v10921_report_gate.py V10967` | Chạy sau khi push công khai |

## 7. Vướng vấp

| Vấp | Hậu quả nếu bỏ qua |
|---|---|
| FU-225 kép làm QD-016 biến mất khỏi treo | Owner/agent tưởng chưa có theo dõi bỏ ép RULES-FIRST |
| Parser cũ không đọc `**Trạng thái:**` | ~5 mục mới (229/230/228/225 UI) “mồ côi” khỏi briefing |
| Agent trước gắn nhãn hàng loạt cả heading đã đóng | Không hại chức năng; hơi ồn lịch sử — chấp nhận vì chỉ thêm text |

## 8. Gỡ về

- Quy ước / nhãn: `git checkout` các file docs + reader/session_start về commit trước V10967.
- QD-018/019: đổi `trang_thai` → SUPERSEDED trong ledger (không xoá).
- Không có rollback VPS vì không deploy.

## 9. Theo dõi tiếp

| Mã | Mã đọc | Việc | Hạn / ngưỡng |
|---|---|---|---|
| QD-014 / FU-215 | DB0808 | Đóng băng đường ra số | hết 08/08 |
| QD-018 / FU-233 | HT0822-1 | B1 tắt tối ưu trọng số | ≥7–14d; tự cắt nếu BT xấu ≥3pp |
| QD-018 / FU-234 | DO0905 | B2 đo 105 luật | ≥14d; cắt nếu luật hại ≥3pp |
| QD-018 / FU-235 | HT0919 | B3 gỡ ép list | ≥14d; overlap ≤10% hoặc hoàn |
| FU-232 | SC0815-3 | Hoàn nửa V10938 WR→BT trọng số số | sau 08/08; chưa sửa |
| QD-019 / FU-227 | TK0808 | Quy ước B | CLOSED |

Rà soát QD-018: **09/08/2026** (ngày đầu được phép B1).
