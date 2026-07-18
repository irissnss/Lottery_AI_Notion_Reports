# BÁO CÁO V10823 — VERIFY TRUNG THỰC SỐ 93 + QUÉT 7 BIẾN THỂ TỔNG HỢP + PANEL "TOTAL 10 NGÀY THAY ĐỔI LỚN"

- **Ngày:** 2026-07-18, phiên 22:00 → 22:2x
- **Trigger (verbatim):** "Đã backtest verify kỹ chưa em? Sao số out ra 93 là lose ah là trung thực đó hả? có cách nào làm nổi bật hơn để dễ nhìn hơn không em? Có tìm ra phương pháp nào tối ưu tốt hơn không, đã thử hết các phương pháp các cách chưa? đặt tên cho Chỗ này là total 10 ngày thay đổi lớn đi. chứ nằm lọt giữ khó xem quá."

---

## PHẦN 1 — VERIFY TRUNG THỰC: 93 LOSE LÀ THẬT

Đối chiếu trực tiếp DB live (`_v10823_variant_backtest.py` phần verify):

- MB tails 18/07 = 24 số: `09 12 18 19 21 22 30 32 34 42 46 50 52 53 54 61 68 71 72 84 85 86 90 95` — **KHÔNG có 93** → BT lane ngày-0 TRƯỢT thật. **CÓ 86** → số phụ VỀ lô.
- Cả 3 miền ngày-0: MN 31✗ 38✗ · MT 41✗ 46✓ · MB 93✗ 86✓ — panel chấm khớp 100% DB, không tô hồng, không giấu lỗ.
- **Kỳ vọng đúng để anh đọc số hằng ngày:** M2s backtest BT chỉ 30-48%/miền (MB thấp nhất 32.9%) — nghĩa là PHẦN LỚN ngày vẫn trượt BT. Giá trị của phương pháp nằm ở **chênh +9→+11.5pp so với bundle cũ cộng dồn nhiều ngày**, không phải trúng mỗi ngày.

## PHẦN 2 — "ĐÃ THỬ HẾT CÁC PHƯƠNG PHÁP CHƯA?": QUÉT THÊM 7 BIẾN THỂ

Cùng khung leak-safe V10821 (predictions `run_source≠shadow`, union MRE, 165 ngày 20/12→17/07, n≈470 region-days). V10821 đã đo M0/M1/M2s/M3/M4; lượt này thêm 7 biến thể:

| Biến thể | Ý tưởng | BT-gộp FULL | BT-gộp 60d | Kết luận |
|---|---|---|---|---|
| **M2s (chuẩn)** | coverage + neo rules | **40.0** | **38.9** | đang chạy lane |
| VA main-weight | main 1.0 / phụ 0.6 | 39.5 | 37.8 | KÉM hơn |
| **VC WR-rules** | phiếu × form-30d model + neo rules | 41.0 | 40.6 | nhỉnh +1.0/+1.7pp = TRONG NHIỄU → re-check sau 28/07 |
| VD multi-rule | bonus số được nhiều rule phát | 40.0 | 38.9 | ngang |
| VE dual-gate | in-rules VÀ coverage≥2 | 41.0 | 39.4 | nhỉnh nhẹ, không bền |
| VF main-gate | in-rules VÀ có mặt ở main | 39.5 | 37.8 | KÉM hơn |
| VH hedge | BT in-rules + partner ngoài | 40.0 | 38.9 | any MB SẬP 42.5% vs 50.3% → BỎ |
| W3 bộ-3 | M2s top-3 | 40.0 (BT như M2s) | 38.9 | any 84.7/78.5/65.4 (>bộ-2 73.9/65.2/50.3) nhưng 1.5× vốn — play-style, kèo vốn owner |

**KẾT LUẬN TRUNG THỰC:** không biến thể nào thắng M2s bền cả 2 cửa sổ vượt nhiễu (chênh <2pp với n này chưa đủ tin). **GIỮ M2s nguyên vẹn cho 10 ngày đo** (nguyên tắc 1 biến số/lần — lane đang live). VC đánh dấu **RE-CHECK sau 28/07** bằng dữ liệu forward; nếu vẫn nhỉnh → đề xuất A/B lane riêng.

## PHẦN 3 — PANEL THEO LỆNH OWNER

- Đổi tên: **"🧮 TOTAL 10 NGÀY THAY ĐỔI LỚN — số CHƠI mỗi ngày (LANE trước giờ xổ) + so găng tầng tổng hợp (3 miền)"**.
- **Dời từ giữa trang (sau CHASE-BIAS) lên vị trí #2** ngay sau 🎯 BẢNG NÊN CHƠI; khối cũ xóa (id duy nhất, `node --check` pass); viền vàng 3px + glow nhận diện.
- Khối đầu tiên = **🚏 SỐ CHƠI HÔM NAY**: chip số TO (font 1.05rem) từng số có nhãn BT/phụ, màu trung thực **xanh = VỀ · đỏ = TRƯỢT · xám = chờ KQ**, kèm dòng trạng thái chữ rõ ("BT trượt, phụ VỀ lô"). Lịch sử lane mỗi ngày chip ✓/✗ TỪNG SỐ (backend `_lane_view` thêm field `marks` per-pick) + ghi chú "18/07 là ngày-0 retro".
- Bảng so găng M0/M1/M2s/M4, 7-ngày shadow, preview giữ nguyên bên dưới; footer ghi kết quả quét 7 biến thể.

## PHẦN 4 — DEPLOY + §52

- Backup 2 đầu TRƯỚC sửa: `backups/v10823_pre/` (local) + `/root/backups_v10823/` (VPS).
- SHA khớp 2 file; py_compile + node --check pass; restart `lottery.service` 22:1x (ngoài giờ job học — MRE/re-rank/shadow 20:15-20:50 xong, kế tiếp 00:30 T2) → active; health 200; admin 401; journal sạch; view check `marks` đúng (MB today [0,1] = 93✗ 86✓).
- **Hash 4 bảng official pre/post IDENTICAL** (a6a7fa8e / c6bb036d / b080e2cc / b8de7d94). Đợt này UI-only + 1 field hiển thị — phương pháp lane/shadow KHÔNG đổi.

## ARTIFACTS
- `web/backend/_v10823_variant_backtest.py` (7 biến thể + verify ngày-0) · `web/backend/_v10821_total_v2_shadow.py` (field `marks`) · `web/frontend/monitoring.html` (panel mới vị trí #2) · `_v10823_js_extract.py` · `_v10823_deploy.py`.
- Governance: CHANGELOG V10823 · SSOT V10823 · FU-V10823-TOTAL10-PANEL · AUTOMATION_STATE seq 284 · HISTORY jsonl · PLAYBOOK 28/07 (+VC re-check) · SO_TAY 1.2/1.3.
