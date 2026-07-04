# V10777 — MN BT 1-SỐ: GIẢM VỐN TĂNG LỜI (theo hướng owner) — 2026-07-05

## PHẦN 1 — YÊU CẦU CỦA OWNER (nguyên văn, 05/07 02:04)

> "MN âm là đúng rồi em nếu chơi song thủ vốn lớn quá mà em. Âm là điều không thể tránh khỏi. Việc BT ở MN mới giảm vốn tăng lời thôi. Nên MN cần xem xét kỹ BT ah em"

## PHẦN 2 — KIỂM CHỨNG KINH TẾ: OWNER ĐÚNG

| Cách chơi MN | Vốn/ngày (50đ, 18k/số/đài) | Hòa vốn |
|---|---|---|
| Song-thủ (2 số) | 3 đài: 5.4M · T7 4 đài: 7.2M | cần ≥1.1 nháy/ngày |
| **BT 1 số** | 3 đài: **2.7M** · T7 4 đài: 3.6M | 3 đài: 55% ngày-trúng · **T7: 73% (gần bất khả)** |

Cùng kỳ 56 ngày (10/5→04/07): aggregate song-thủ MN **−37.5M** nhưng official bạch-thủ (1 số) chỉ **−1.6M** → phần lớn lỗ MN đến từ **cấu trúc vốn song-thủ**, không phải từ số. Đài MN: đúng 3 đài mọi thứ trong tuần, riêng **T7 = 4 đài**.

## PHẦN 3 — BACKTEST BT 1-SỐ 56 NGÀY (mọi nguồn số, 1 nháy = +4.9M)

**Full tuần (7 ngày):**

| Nguồn BT | P&L 56d | hit% | Nửa1/Nửa2 | Bền? |
|---|---|---|---|---|
| top-1 strength | +22.9M | 51.8% | −5.7 / +28.6 | KHÔNG |
| top-1 plurality | +13.1M | 48.2% | −15.5 / +28.6 | KHÔNG |
| gpt-5-mini số1 | +13.1M | 48.2% | −15.5 / +28.6 | KHÔNG |
| combo-super số1 | +13.1M | 50.0% | +13.9 / −0.8 | KHÔNG |
| **gpt-oss-120b số1** | **+8.7M** | 48.1% | **+1.9 / +6.8** | **BỀN (duy nhất)** |
| OFFICIAL bạch-thủ | −1.6M | 44.6% | −5.7 / +4.1 | — |
| deepseek số1 | −8.7M | 43.6% | +16.6 / −25.3 | KHÔNG |
| random-forest/xgboost số1 | −60.4M | 30-34% | — | ML đừng đánh BT MN |

**BỎ T7 (tránh ngày 4 đài hòa vốn 73%):**

| Nguồn BT | P&L bỏ-T7 | Nửa1/Nửa2 | Bền? |
|---|---|---|---|
| **gpt-oss-120b số1** | **+17.9M** | +6.5 / +11.4 | **BỀN** |
| top-1 strength | +17.4M | −1.1 / +18.5 | KHÔNG |
| **OFFICIAL bạch-thủ** | **+7.6M** | +3.8 / +3.8 | **BỀN** |
| top-1 plurality | +7.6M | −10.9 / +18.5 | KHÔNG |
| deepseek số1 | −9.3M | — | KHÔNG |

**Phát hiện quan trọng:**
1. **Bỏ T7 biến official bạch-thủ từ −1.6M thành +7.6M BỀN cả 2 nửa** — chỉ bằng tránh ngày vốn cao.
2. **deepseek nghịch lý:** song-thủ +40.1M (mạnh nhất MN) nhưng BT −8.7M → sức mạnh deepseek nằm ở CẶP số (số 2 gánh), không phải số 1. Không dùng deepseek cho BT.
3. **gpt-oss-120b** là nguồn BT bền duy nhất full-tuần (+8.7M) và mạnh hơn khi bỏ T7 (+17.9M) — nhưng 14 ngày gần đây nguội (−20.0M) → phải đo forward thêm trước khi chọn.
4. Official BT dương T2/T3/T6/CN, âm T4/T7 (bucket-first theo thứ).

## PHẦN 4 — ĐÃ TRIỂN KHAI (đo lường, KHÔNG đổi output/choi)

1. `_v10765_aggregation_signal_shadow.py`: hàm `_mn_bt_summary()` READ-ONLY (không tạo bảng mới — tính causal từ predictions/final_bundles/lottery_results đã lưu) → khối `mn_bt` trong API `/api/admin/aggregation-signal`: 8 nguồn × (45d/14d) × (full/bỏ-T7).
2. `monitoring.html` panel 📶: bảng "🎯 MN — BT 1 SỐ (V10777, vốn ½ song-thủ)" + note; auto-refresh 60s sẵn có.
3. Forward 14 ngày hiện tại: top1-strength +29.0M full (+31.3M bỏ-T7) · official −0.4M full (**+6.8M bỏ-T7**) · gpt-oss −20.0M (nguội).

## PHẦN 5 — ĐỀ XUẤT (CHỜ OWNER — không tự làm)

- /choi MN hiện khóa **song-thủ** tuần 29/06 (method MN_ADAPTIVE_EXPLOIT_V1, 2 số/ngày).
- Phương án V10777: đổi /choi MN sang **BT 1 số + NGHỈ T7** từ tuần khóa tiếp theo (06/07 hoặc 13/07), nguồn số chọn tại checkpoint **14/07** theo forward: official bạch-thủ (ổn định, +7.6M BỀN bỏ-T7) vs gpt-oss-120b (+17.9M BỀN nhưng 14d nguội) vs top1-strength (tổng cao nhưng không bền).
- Anh OK phương án nào thì em áp cho tuần khóa kế tiếp; /du-doan official KHÔNG đổi.

## PHẦN 6 — BẰNG CHỨNG & GOVERNANCE

- Backtest độc lập 2 script (full + bỏ-T7); VPS verify: `mn_bt` 8 nguồn trả đúng (official 45d bỏ-T7 −4.6M; gpt-oss +19.9M — khớp local).
- Hash 4 bảng official pre/post IDENTICAL (predictions 9268 `548c6421`, final_bundles 381 `0f70d14a`, lottery_results 15010 `2076e8f7`, model_daily_eval 9132 `cbd1f568`); smoke ALL PASS; health 200.
- Backup `backups/v10777_pre/`; rollback = restore 2 file. Private commit `114a54d`.
- Docs cùng phiên: CHANGELOG V10777, SSOT V10777, FU-V10777-MN-BT (checkpoint 14/07), AUTOMATION_STATE seq 232.
