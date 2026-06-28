# V10761 — /choi cược phụ INFO-only (xiên/3-càng) + /du-doan-test tinh gọn

**Ngày:** 2026-06-29 · **Scope:** SHADOW read-only UI, ZERO official/ví impact · **FU:** FU-V10761-SIDEBETS-DECLUTTER

## Bối cảnh (owner)
"đụng tới tiền rồi nên cẩn thận theo dõi triệt để"; hỏi: (1) /choi treo "chờ xổ"?; (2) xiên2/xiên3/3-càng có method gắn lên card?; (3) /du-doan-test nhiều card đo lường quá rối, có cần tinh gọn?

## 1. /choi "chờ xổ" = bình thường
0h sáng lane chưa chạy → card hiện "⏳ chờ"; số tự hiện trước giờ xổ từng miền (MN<16:15, MT<17:15, MB<18:30). Không lỗi.

## 2. Xiên/3-càng — đo trước, owner chọn INFO-only (không staking)
Official đã sinh xiên2/xiên3/lo3. Đo ĐÚNG luật CÙNG ĐÀI 90 ngày:
| Cược | MN | MT | MB | Hoà vốn cần | Odds thị trường |
|---|---|---|---|---|---|
| Xiên 2 (cùng đài) | 7.7% | 6.6% | 6.6% | 1 ăn 13-15 | 1 ăn 10-17 (biên mỏng) |
| Xiên 3 (cùng đài) | 3.6% (3 lần) | 0% (0/57) | 1.2% | 28-83 | 1 ăn 40-65 (thất thường) |
| 3 càng (lô3) | 7.7% | 3.3% | 3.3% | 13-30 | 1 ăn 400+ (chưa có khung tính tiền) |

`pnl_settlement.py` chỉ settle LÔ → xiên/3-càng KHÔNG có P&L tracking → **không có edge ổn định**. Owner chọn **INFO-only**: block "🎲 Cược phụ" trên mỗi card /choi (số official hôm nay + tỉ lệ trúng 60d cùng-đài + nhãn đỏ "rủi ro cao, KHÔNG khuyến nghị vốn, chỉ tham khảo").

## 3. /du-doan-test tinh gọn (~28 panel)
Thêm thanh lọc **⭐ Lõi / 🔬 Chẩn đoán / 📁 Tất cả** (mặc định Lõi = output + lịch sử; ẩn 8 panel chẩn đoán V106.xx + metrics). `data-testcat` + `applyTestFilter()`. KHÔNG mất panel nào, không đụng logic render #app.

## An toàn
READ-ONLY (final_bundles + lottery_results), ZERO official/ví. Hash-guard 4 bảng official IDENTICAL pre/post. health200, /choi + /du-doan-test = 401 (admin-gated). Rollback: restore backups/v10761_remote_pre/.
