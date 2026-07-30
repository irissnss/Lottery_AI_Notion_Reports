# V10882 — Luồng thứ 5 = OFFICIAL NEW (dựng lại đúng hình dạng)

**30/07/2026 · đã deploy, đang chạy thật**

Owner: *"Anh chả hiểu gì cả em làm cái gì thế?... 'Nghiệm Thu 19/08' offical New đó em hiểu chứ... Còn các vấn đề cắt đài, đổi số gì đó anh không hiểu"*

## Sai ở đâu

V10879 dựng phương án **đặt tiền** (1 số/miền, chọn đài, lãi lỗ) — đó là việc của luồng 4 `/choi`. Owner cần **luồng dự đoán** cùng khuôn official. Đã bỏ hết phần tiền khỏi luồng này.

## Luồng 5 giờ là gì

**Giống official mọi thứ:** cùng 15 model · cùng 5 lá `bach_thu/lo2/lo3/xien2/xien3` · cùng luật lắp ráp · cùng công thức lo3 · cùng thước chấm (xiên phải cùng một đài).

**Khác đúng một chỗ:** cách đếm phiếu — de-herd family-√ thay `weighted_voting_wr`.

## Đối chứng 135 miền-ngày (15/06–29/07), gộp 3 miền

| Lá bài | NEW | official | Chênh | Lệch | p |
|---|---|---|---|---|---|
| **Bạch thủ** | **49/135** | 34/135 | **+11,1pp** | 19–4 | **0,0026** |
| **Lô 2** | **20/135** | 11/135 | **+6,7pp** | 12–3 | **0,0352** |
| Lô 3 càng | 6 | 6 | 0 | 3–3 | 1,0 |
| Xiên 2 | 9 | 8 | +0,7pp | 3–2 | 1,0 |
| Xiên 3 | 2 | 2 | 0 | 0–0 | — |

**Giới hạn phải nói rõ:** từng miền đều dương ở bạch thủ (+11,1pp cả ba) nhưng p yếu khi tách nhỏ (MN 0,0625 · MT 0,1797 · MB 0,1797) — 45 ngày mỗi miền quá ít. Bằng chứng chắc ở mức **gộp**, chưa chắc ở mức **từng miền**. Ở mốc chốt có thể chỉ áp miền nào đủ bằng chứng.

Trùng bạch thủ với official 48,9%.

## Ngày đầu 30/07

MN `86` / 86-84 / `086` · MT `20` / 20-54 / `120` / xiên3 20-54-76 · MB `43` / 43-61 / `243` / xiên3 43-61-78

## Chốt

Tối thiểu 7 ngày, sớm nhất **05/08**, chặn cuối 19/08. Thước là **bạch thủ**: đếm ngày hai bên lệch nhau, bên nào thắng nhiều hơn thì hơn.

## An toàn

Hash 4 bảng official pre/post IDENTICAL. V10841 PASS. Không ghi `final_bundles`, không đụng `/choi`, không sửa official. Lên official cần chữ ký owner, đi qua cơ chế cờ có thể tắt.

Báo cáo đầy đủ: `V10882_OFFICIAL_NEW_LANE_20260730/REPORT_V10882.md`
