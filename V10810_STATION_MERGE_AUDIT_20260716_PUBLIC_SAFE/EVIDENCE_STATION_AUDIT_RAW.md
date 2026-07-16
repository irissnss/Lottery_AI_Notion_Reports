# V10810 EVIDENCE — RAW PROBE OUTPUT (đài × thứ, mã tắt, MRE backfill, hash)

## E1. Đài theo miền × thứ — TRƯỚC (18/05-30/06) vs SAU (01-15/07)

```
MN T2: ['Cà Mau','TP. HCM','Đồng Tháp']            = SAU (không đổi)
MN T3: ['Bạc Liêu','Bến Tre','Vũng Tàu']           = SAU
MN T4: ['Cần Thơ','Sóc Trăng','Đồng Nai']          = SAU
MN T5: ['An Giang','Bình Thuận','Tây Ninh']        = SAU
MN T6: ['Bình Dương','Trà Vinh','Vĩnh Long']       = SAU
MN T7: ['Bình Phước','Hậu Giang','Long An','TP. HCM'] = SAU
MN CN: ['Kiên Giang','Tiền Giang','Đà Lạt']        = SAU

MT T2: ['Phú Yên','Thừa Thiên Huế']                = SAU
MT T3: TRƯỚC ['Quảng Nam','Đắk Lắk'] → SAU thêm ['DLK','QNA'] (= mã tắt 07/07, đã repair)
MT T4: ['Khánh Hòa','Đà Nẵng']                     = SAU
MT T5: TRƯỚC có ['QB','QT'] (mã tắt 25/06) + tên đầy đủ → SAU sạch
MT T6: TRƯỚC ['Gia Lai','Ninh Thuận'] → SAU thêm ['GL','NT'] (= mã tắt 03/07, đã repair)
MT T7: ['Quảng Ngãi','Đà Nẵng','Đắk Nông']         = SAU
MT CN: ['Khánh Hòa','Kon Tum','Thừa Thiên Huế']    = SAU

MB: T2 Hà Nội / T3 Quảng Ninh / T4 Bắc Ninh / T5 Hà Nội / T6 Hải Phòng / T7 Nam Định / CN Thái Bình = không đổi
```

## E2. Đài xổ >1 lần/tuần (SAU 01/07) — tất cả đã như vậy TRƯỚC đó (từ 2020)

```
MN TP. HCM:        SAU [T2,T7]  | TRƯỚC [T2,T7]   | n lịch sử 644
MT Khánh Hòa:      SAU [T4,CN]  | TRƯỚC [T4,CN]   | n 672
MT Thừa Thiên Huế: SAU [T2,CN]  | TRƯỚC [T2,CN]   | n 375
MT Đà Nẵng:        SAU [T4,T7]  | TRƯỚC [T4,T7]   | n 670
MB Hà Nội:         SAU [T2,T5]  | TRƯỚC [T2,T5]   | n 667
(đài tuần-1-lần: n ~322-337 — gần đúng nửa, nhất quán 2 lần/tuần từ 2020)
```

## E3. 6 dòng mã tắt — chi tiết + verify web ngoài

```
rowid=15051 2026-06-25 MT QB : 9 giải, 18 số, ĐB=318032  | web voh/xsktsoctrang: Quảng Bình ĐB=318032 ✔
rowid=15053 2026-06-25 MT QT : 9 giải, 18 số, ĐB=787705  | web xosoquangtri:    Quảng Trị  ĐB=787705 ✔
rowid=15104 2026-07-03 MT GL : 9 giải, 18 số, ĐB=072277  | web voh/xsmn.mobi:   Gia Lai    ĐB=072277 ✔
rowid=15105 2026-07-03 MT NT : 9 giải, 18 số, ĐB=364600  | web voh/vtcnews:     Ninh Thuận ĐB=364600 ✔
rowid=15131 2026-07-07 MT DLK: 9 giải, 18 số, ĐB=620584  | web xosodaiphat:     Đắk Lắk    ĐB=620584 ✔
rowid=15132 2026-07-07 MT QNA: 9 giải, 18 số, ĐB=353672  | web kqsx.mobi:       Quảng Nam  ĐB=353672 ✔
```

Ngày 15/07 (T4) — kiểm chứng lịch cũ còn hiệu lực + DB khớp web:

```
DB:  Cần Thơ ĐB=867898 G8=05 | Sóc Trăng ĐB=282199 G8=96 | Đồng Nai ĐB=008402 G8=10
Web: Cần Thơ 867898 | Sóc Trăng 282199 | Đồng Nai 008402  (xosohomnay.com.vn)  → khớp 100%
```

## E4. MRE trước repair — bằng chứng câm lặng lẽ

```
2026-07-03 nguồn-MT: CHỈ 1 row (Bình Định G7+G8) — thiếu Ninh Thuận (5 rule active hôm đó/hôm sau)
2026-07-07 nguồn-MT: CHỈ 1 row (Phú Yên G5+G7) — thiếu Đắk Lắk (2 rule)
2026-06-25 nguồn-MT: 3 row (Đà Nẵng, Khánh Hòa ×2) — thiếu Quảng Bình #2084
So sánh T5 bình thường (04/06, 11/06): có đủ row Quảng Bình G5+GĐB.
Kiểm tra trùng lặp MRE 30d: 0 nhóm trùng; orphan rule_id 7d/19d: 0.
```

## E5. Repair + backfill log (VPS, 16/07 12:26)

```
BACKUP OK: 6 dòng -> bảng v10810_station_repair_backup + /tmp/v10810_repair_backup_rows.json
HASH PRE : predictions 2ffa27cc | final_bundles c6119479 | lottery_results 1a1820b1 | model_daily_eval aaa91dc6
REPAIR OK: 6 dòng UPDATE
HASH POST: predictions 2ffa27cc ✔ | final_bundles c6119479 ✔ | lottery_results a87cc07a (delta chủ đích) | model_daily_eval aaa91dc6 ✔
SHORTCODE REMAINING: 0
MRE BACKFILL 25/06 ev=15 hit=13 | 26/06 ev=15 hit=15 | 03/07 ev=15 hit=12 | 04/07 ev=15 hit=12 | 07/07 ev=15 hit=13 | 08/07 ev=15 hit=14
VERIFY 8/8:
  25/06 Quảng Bình #2084: tails=[32,17] hit=[17] ✔HIT
  03/07 Ninh Thuận #2090: tails=[00,01] miss
  04/07 Ninh Thuận #2021: tails=[00,54] miss (MN)
  04/07 Ninh Thuận #2091: tails=[31,54] hit=[54] ✔HIT (MB)
  04/07 Ninh Thuận #2093: tails=[00,31] miss
  04/07 Ninh Thuận #2094: tails=[31,61] miss
  07/07 Đắk Lắk  #2074: tails=[84,36] miss
  08/07 Đắk Lắk  #2007: tails=[84,72] hit=[84] ✔HIT (MN)
```

## E6. Selfcheck sau deploy (12:26:52) — có check 11 mới

```
1.ml_model_age<=8d        PASS age=3.2d
2.optimizer_marker<=9d    PASS age=6.2d
3.retrain_OK_in_8d        FAIL OK rows 8d=0   <- bệnh CŨ V10800 (subprocess fix đã deploy; model files thật retrain 13/07 06:32 qua guard; hàng OK đầu tiên ghi CN 19/07)
4.rules_fresh             PASS mined=15/07 mn=16/07 mb=16/07 mt=15/07
5.cau_pattern_fresh       PASS | 6.MDE 26 model PASS | 7.T-chốt 3/3 PASS | 8.lane 3/3 PASS | 9.bundle 3/3 PASS | 10.weekly_lock PASS
11.no_shortcode_station_14d PASS rows=0 []   <- CHECK MỚI V10810
```

## E7. Đối chiếu lịch chính thức (nguồn web, truy cập 16/07/2026)

- Tuổi Trẻ (12/11/2025): Bộ TC công văn 16/6 — "tiếp tục duy trì lịch quay số mở thưởng như hiện nay cho đến thời điểm công ty xổ số chính thức hoạt động theo mô hình mới".
- Thanh Niên (10/2025): dự thảo 9 công ty XSMN (TP.HCM 4 kỳ/tuần; VL/CT/LĐ 3 kỳ; ĐT/CM/ĐN/TN/AG 2 kỳ) — dự kiến 1/1/2026, Cần Thơ kiến nghị điều chỉnh + lùi thời điểm.
- xsmn.mobi/xskt.com.vn: XSMT "vẫn giữ nguyên, chờ thông tin mới" — chưa có phương án chính thức.
- Kết quả thực tế 09-15/07/2026 trên các trang kết quả: đúng lịch CŨ mọi ngày (T3 Bến Tre-Vũng Tàu-Bạc Liêu; T4 ĐN-CT-ST; T6 VL-BD-TV; ...).
