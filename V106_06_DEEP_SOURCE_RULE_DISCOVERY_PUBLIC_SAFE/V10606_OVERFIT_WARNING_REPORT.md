# V106.06 Overfit / Data-Snooping Warning Report

Live snapshot: `artifacts/live_sync/20260523_230610/manifest.json`

## Risk register
| Risk | Detail |
|---|---|
| Multiple-testing | Đã test 153228 rule key. Cần áp dụng gate live verify >=14 ngày trước khi xét đẩy lên test-lane chính. |
| Digit-position transforms | Số lượng P{i}P{j} lớn nên chỉ tin nếu `half_stable >= 1` và đồng thời `db_day_lift_pp >= 3`. |
| Digit-sum family | Có xu hướng tạo ảo tăng vì collision space hẹp; chỉ giữ làm context khi `hit_lift_pp >= 8`. |
| Single-window rules | Bất kỳ rule chỉ đẹp ở 1 window đã bị tier WATCH/REJECT. |
| Sample-size scoped 12-25 days | Bị giữ ở Tier C/WATCH, không được boost. |

## Top rejected rules (sample 30)
| target | rule | window | days | hit_lift | db_lift | reject_reason |
|---|---|---:|---:|---:|---:|---|
| MN | `MB:MB_BOARD:DB#1:HEAD_SUM_UNIT W-3 scope=0` | 180 | 24 | +7.96 | +13.67 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:DB#1:HEAD_SUM_UNIT W-3 scope=Cà Mau|TP. HCM|Đồng Tháp` | 180 | 24 | +7.96 | +13.67 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:G2#2:HEAD_SUM_UNIT D-6 scope=0` | 180 | 24 | +7.96 | +13.67 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:G2#2:HEAD_SUM_UNIT D-6 scope=Cà Mau|TP. HCM|Đồng Tháp` | 180 | 24 | +7.96 | +13.67 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MB | `MB:MB_BOARD:G2#2:SUM_LAST2 D-2 scope=ALL` | 60 | 60 | +7.98 | +5.67 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:G1#1:SUM_UNIT_TAIL W-2 scope=3` | 180 | 25 | +6.16 | +13.0 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:G1#1:SUM_UNIT_TAIL W-2 scope=An Giang|Bình Thuận|Tây Ninh` | 180 | 25 | +6.16 | +13.0 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:G1#1:HEAD_SUM_UNIT W-2 scope=6` | 180 | 25 | +6.0 | +13.08 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:G1#1:HEAD_SUM_UNIT W-2 scope=Kiên Giang|Tiền Giang|Đà Lạt` | 180 | 25 | +6.0 | +13.08 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MB | `MB:MB_BOARD:DB#1:HEAD_SUM_UNIT D-3 scope=5` | 180 | 25 | +7.88 | +7.0 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MB | `MB:MB_BOARD:DB#1:HEAD_SUM_UNIT D-3 scope=Nam Định` | 180 | 25 | +7.88 | +7.0 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:G2#2:TAIL_SUM_UNIT D-4 scope=ALL` | 90 | 89 | +7.34 | +5.84 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:G1#1:HEAD_SUM_UNIT D-5 scope=ALL` | 90 | 88 | +7.86 | +4.81 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:DB#1:SUM_UNIT_HEAD W-2 scope=ALL` | 60 | 60 | +6.58 | +8.52 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MT | `MB:MB_BOARD:DB#1:SUM_UNIT_HEAD D-2 scope=Phú Yên|Thừa Thiên Huế` | 180 | 12 | +3.08 | +14.67 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MT | `MB:MB_BOARD:G2#2:SUM_UNIT_HEAD D-1 scope=Phú Yên|Thừa Thiên Huế` | 180 | 12 | +3.08 | +14.67 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:DB#1:HEAD_SUM_UNIT D-6 scope=ALL` | 90 | 87 | +7.3 | +4.9 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MB | `MB:MB_BOARD:G2#2:SUM_LAST2 D-2 scope=ALL` | 30 | 30 | +6.17 | +9.0 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:DB#1:SUM_LAST2 D-7 scope=2` | 180 | 25 | +6.0 | +9.04 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:DB#1:SUM_LAST2 D-7 scope=Cần Thơ|Sóc Trăng|Đồng Nai` | 180 | 25 | +6.0 | +9.04 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:DB#1:SUM_LAST2 D-7 scope=2` | 180 | 25 | +6.0 | +9.04 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:DB#1:SUM_LAST2 D-7 scope=Cần Thơ|Sóc Trăng|Đồng Nai` | 180 | 25 | +6.0 | +9.04 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:DB#1:SUM_UNIT_HEAD W-2 scope=ALL` | 90 | 86 | +7.81 | +4.99 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MT | `MB:MB_BOARD:G2#2:SUM_UNIT_TAIL D-6 scope=1` | 180 | 25 | +5.56 | +10.0 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MT | `MB:MB_BOARD:G2#2:SUM_UNIT_TAIL D-6 scope=Quảng Nam|Đắk Lắk` | 180 | 25 | +5.56 | +10.0 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MT | `MB:MB_BOARD:DB#1:TAIL_SUM_UNIT D-4 scope=0` | 180 | 23 | +4.65 | +11.04 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:G2#1:SUM_LAST2 D-6 scope=ALL` | 90 | 87 | +6.15 | +4.9 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:DB#1:SUM_UNIT_HEAD W-4 scope=4` | 180 | 26 | +3.69 | +12.38 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MN | `MB:MB_BOARD:DB#1:SUM_UNIT_HEAD W-4 scope=Bình Dương|Trà Vinh|Vĩnh Long` | 180 | 26 | +3.69 | +12.38 | DIGIT_SUM_NOT_STRONG_ENOUGH |
| MB | `MB:MB_BOARD:G1#1:SUM_UNIT_HEAD D-5 scope=0` | 180 | 23 | +6.65 | +7.7 | DIGIT_SUM_NOT_STRONG_ENOUGH |
