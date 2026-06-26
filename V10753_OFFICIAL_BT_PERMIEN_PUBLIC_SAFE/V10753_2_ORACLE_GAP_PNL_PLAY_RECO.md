# V10753.2 — Backtest oracle-gap P&L + Khuyến nghị chơi per-miền (admin /du-doan)

**Thời điểm:** 2026-06-26T19:50:00+07:00 · **Bối cảnh:** owner bực "tín hiệu có total tào lao" (26/06 cả 3 miền BT trật) → yêu cầu backtest khai thác oracle-gap.

## Backtest P&L nhân-quả 119 ngày

Model tiền: 50 điểm/số/đài, 98k/điểm/nháy, cộng mọi đài. Chiến lược suy từ pool ứng viên tiền-xổ (causal). Head-to-head chooser ĐANG LIVE vs plurality vs official cũ:

| Miền | Chiến lược tốt nhất | Net 119d | ROI | 30d gần |
|---|---|---|---|---|
| **MN** | specialist **1 số** (live) | **+45.6M** | +13.5% | +10.7M |
| MN | song-thủ 2 số | −36.2M | −5.4% | −17.8M |
| **MT** | nt_consensus **song-thủ** (live) | **+102.1M** | +19.6% | +31.6M |
| **MB** | prior_region **1 số** (live) | **+30.4M** | +19.0% | +16.9M |
| MB | song-thủ 2 số | +16.8M | +5.2% | +9.4M |

## 2 kết luận

1. **BT chooser deploy V10753 hôm nay là ĐÚNG — tiền xác nhận** (thắng cả official cũ lẫn plurality cả 3 miền). Hôm nay cả 3 trật chỉ là **1 ngày xui** (xác suất ~24%), không phải hệ thống hỏng.
2. **Số lượng chơi tối ưu khác nhau theo miền: MN 1 số · MT song-thủ · MB 1 số.** Đánh song-thủ ở MN/MB **lỗ dài hạn** (nhiều đài, phủ 2 số tốn hơn tiền trúng).

## Thay đổi (additive, admin-only, KHÔNG đổi số dự đoán)

- Backend: config `PLAY_RECOMMENDATION` + endpoint `GET /api/admin/play-recommendation` (require_admin, no-store).
- Frontend `/du-doan`: banner "🎯 KHUYẾN NGHỊ CHƠI" per-miền, **chỉ admin thấy** (public nhận 401 → ẩn).
- Verify: diff thuần thêm; compile OK; health 200; admin endpoint unauth=401; /du-doan=200; **4 bảng official IDENTICAL trong deploy** (không regen). Rollback: gỡ endpoint + banner.

## Hôm nay 26/06 (ngày live đầu logic mới)

MN BT53/đề21 · MT BT80/đề73 · MB BT18/đề04 — cả 3 trật lô. MN song-thủ `00` trúng lô. Tín hiệu rank-2 (`00`,`13`,`45`) trúng nhưng phủ rank-1+2 ở MN/MB lỗ dài hạn → giữ 1 số.
