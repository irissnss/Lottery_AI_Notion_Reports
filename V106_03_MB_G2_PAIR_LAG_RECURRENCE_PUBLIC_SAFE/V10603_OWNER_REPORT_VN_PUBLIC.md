# V106.03 Bao Cao Public-Safe: MB Giai Nhi Ca 2 Bo D-1/D-2/D-3 -> MN D

Generated at VN: 2026-05-21T22:07:00+07:00  
Live sync manifest: `artifacts/live_sync/20260521_220205/manifest.json`  
Scope: public-safe analytical report only. No official output mutation. No lane-test promotion. No provider/manual AI call.

## 1. Cau hoi cua owner

Owner hoi: neu khong chi soi bo so dau tien cua Giai nhi MB, ma soi chung ca hai bo so Giai nhi MB thi:

- `MB D-1` sang `MN D` the nao?
- `MB D-2` sang `MN D` the nao?
- `MB D-3` sang `MN D` the nao?
- Ket luan va de xuat dua vao model/no-token la gi?

Quy tac do trong bao cao nay:

- Nguon moi ngay la `Giai nhi` MB gom 2 bo so.
- Lay 2 so cuoi cua ca 2 bo so.
- Soi cac tail nay sang ket qua MN ngay D.
- Tach rieng 3 lag: D-1, D-2, D-3.
- Khong dung tat ca giai MB, khong dung Giai dac biet MB, khong dung cac giai khac.

Vi du dung voi case owner chup:

- `MB 18/05/2026 Giai nhi = 54197, 29265`.
- Tails nguon = `97, 65`.
- `MN 20/05/2026`: `65` ve Can Tho, `97` ve Soc Trang va Dong Nai.
- Dong Nai DB la `325697`, tuc tail `97` cham DB.

## 2. Cach doc chi so

Vi dung ca 2 bo Giai nhi, moi ngay nguon co toi da 2 tail. Do do chi so "ngay co it nhat mot tail ve MN" tu nhien cao hon so voi dung mot tail duy nhat. Bao cao dung 4 chi so:

1. `Any MN prize`: trong ngay D, it nhat 1 trong 2 tail nguon xuat hien o bat ky giai nao cua MN.
2. `Any lift`: chenh lech so voi baseline xac suat ngau nhien khi co 2 tail nguon va tap tail MN thuc te trong ngay.
3. `Candidate-rate`: tinh theo tung tail nguon, vi du 29 hit / 60 candidate trong 30 ngay.
4. `Any DB day`: trong ngay D, it nhat 1 tail nguon cham DB cua mot dai MN.

Ket luan khong duoc chi nhin `Any MN prize`, vi chi so nay de phong khi tang so luong tail nguon tu 1 len 2.

## 3. Ket qua tong hop theo window

### 30 ngay gan nhat

| Lag | Any MN prize | Any lift | Candidate-rate | Candidate lift | Any DB day | DB lift |
|---|---:|---:|---:|---:|---:|---:|
| D-1 | 66.7% (20/30) | -0.3 pp | 43.3% (26/60) | +0.8 pp | 10.0% | +3.8 pp |
| D-2 | 73.3% (22/30) | +6.3 pp | 48.3% (29/60) | +5.8 pp | 13.3% | +7.1 pp |
| D-3 | 80.0% (24/30) | +13.0 pp | 50.0% (30/60) | +7.5 pp | 6.7% | +0.5 pp |

Doc nhanh: 30 ngay gan nhat D-3 rat manh theo "ngay co ve", nhung D-2 can bang hon vi vua co candidate lift, vua co DB-day lift tot nhat.

### 60 ngay gan nhat

| Lag | Any MN prize | Any lift | Candidate-rate | Candidate lift | Any DB day | DB lift |
|---|---:|---:|---:|---:|---:|---:|
| D-1 | 70.0% (42/60) | +2.7 pp | 45.4% (54/119) | +2.2 pp | 8.3% | +2.2 pp |
| D-2 | 65.0% (39/60) | -2.3 pp | 46.2% (55/119) | +3.1 pp | 10.0% | +3.9 pp |
| D-3 | 73.3% (44/60) | +6.1 pp | 45.4% (54/119) | +2.3 pp | 3.3% | -2.8 pp |

Doc nhanh: D-3 van tot ve any-prize nhung yeu DB; D-2 giu duoc candidate lift va DB-day lift.

### 90 ngay gan nhat

| Lag | Any MN prize | Any lift | Candidate-rate | Candidate lift | Any DB day | DB lift |
|---|---:|---:|---:|---:|---:|---:|
| D-1 | 72.2% (65/90) | +4.7 pp | 46.4% (83/179) | +3.1 pp | 5.6% | -0.6 pp |
| D-2 | 67.4% (60/89) | +0.0 pp | 47.5% (84/177) | +4.3 pp | 7.9% | +1.7 pp |
| D-3 | 73.9% (65/88) | +6.5 pp | 44.6% (78/175) | +1.5 pp | 2.3% | -3.9 pp |

Doc nhanh: 90 ngay xac nhan D-2 co candidate-rate tot nhat va DB-day van duong; D-3 noi ve any-day nhung khong chuyen tot sang DB.

### 180 ngay gan nhat

| Lag | Any MN prize | Any lift | Candidate-rate | Candidate lift | Any DB day | DB lift |
|---|---:|---:|---:|---:|---:|---:|
| D-1 | 69.3% (122/176) | +1.8 pp | 43.1% (151/350) | -0.1 pp | 5.7% | -0.4 pp |
| D-2 | 68.2% (120/176) | +0.7 pp | 47.4% (166/350) | +4.3 pp | 5.1% | -1.0 pp |
| D-3 | 72.2% (127/176) | +4.7 pp | 43.1% (151/350) | -0.0 pp | 5.7% | -0.4 pp |

Doc nhanh: dai han D-2 van giu candidate-rate cao nhat; D-1/D-3 khong co candidate edge ro tren 180 ngay.

## 4. Station-set dang chu y trong 90 ngay

### Can Tho / Soc Trang / Dong Nai

| Lag | Any MN prize | Any lift | Candidate-rate | Candidate lift | Any DB day |
|---|---:|---:|---:|---:|---:|
| D-1 | 61.5% | -5.3 pp | 30.8% | -11.5 pp | 7.7% |
| D-2 | 76.9% | +12.0 pp | 52.0% | +9.8 pp | 7.7% |
| D-3 | 76.9% | +10.1 pp | 42.3% | +0.1 pp | 0.0% |

Ket luan station-set nay: D-2 la rule sach nhat. D-3 nhin any-day cao nhung candidate lift gan 0 va khong co DB-day trong mau 90 ngay.

### An Giang / Binh Thuan / Tay Ninh

| Lag | Any MN prize | Any lift | Candidate-rate | Candidate lift | Any DB day |
|---|---:|---:|---:|---:|---:|
| D-1 | 84.6% | +17.9 pp | 61.5% | +19.4 pp | 7.7% |
| D-2 | 84.6% | +17.9 pp | 65.4% | +23.2 pp | 23.1% |
| D-3 | 76.9% | +12.1 pp | 60.0% | +17.9 pp | 7.7% |

Ket luan station-set nay: day la cum rat manh, dac biet D-2. Can dua vao rule co dieu kien theo station-set, khong nen dung global mu.

### Kien Giang / Tien Giang / Da Lat

- D-2: Any MN prize `76.9%`, candidate-rate `53.8%`, candidate lift `+12.0 pp`, Any DB day `15.4%`.

### Binh Phuoc / Hau Giang / Long An / TP. HCM

- D-2: Any MN prize `83.3%`, candidate-rate `58.3%`, candidate lift `+6.4 pp`, nhung Any DB day `0.0%`.

## 5. Vi du DB hit gan day

| MN date | Lag | MB source date | MB G2 numbers | Source tails | DB hit |
|---|---|---|---|---|---|
| 2026-05-21 | D-3 | 2026-05-18 | 54197, 29265 | 65, 97 | An Giang DB 65 |
| 2026-05-21 | D-2 | 2026-05-19 | 25623, 79831 | 23, 31 | Binh Thuan DB 31 |
| 2026-05-20 | D-2 | 2026-05-18 | 54197, 29265 | 65, 97 | Dong Nai DB 97 |
| 2026-05-12 | D-1 | 2026-05-11 | 40410, 91383 | 10, 83 | Ben Tre DB 10 |
| 2026-04-30 | D-2 | 2026-04-28 | 40244, 18921 | 21, 44 | Tay Ninh DB 44 |

## 6. Ket luan ky thuat

1. Neu dung ca 2 bo Giai nhi MB, rule co tin hieu that, nhung khong dong deu theo lag.
2. `D-2` la lag nen dua vao model dau tien vi on dinh nhat khi can bang giua candidate-rate, station-set lift, DB-day lift va case owner quan sat.
3. `D-3` co recall tot trong 30/90 ngay, nhung DB chuyen hoa yeu hon. Nen dung D-3 nhu tin hieu mo rong pool, khong boost DB manh.
4. `D-1` chi nen dung khi station-set/weekday co lift rieng. Khong nen dung global D-1 lam rule chinh.
5. Khong nen dua rule nay vao prompt LLM truc tiep. Nen dua vao no-token deterministic feature/ranker.

## 7. De xuat dua vao model no-token

Ten de xuat: `MB_G2_PAIR_LAG_RECURRENCE_V1`.

Feature chinh:

- `mb_g2_pair_d1_tails`
- `mb_g2_pair_d2_tails`
- `mb_g2_pair_d3_tails`
- `weekday`
- `station_set`
- `window_30_candidate_lift_pp`
- `window_60_candidate_lift_pp`
- `window_90_candidate_lift_pp`
- `db_day_lift_pp`

Logic goi y:

- D-2: cho phep boost khi station-set hoac weekday co `candidate_lift >= +3 pp` va sample du.
- D-3: chi dua vao recall/source-pool, khong nang DB weight tru khi station-set co DB lift duong on dinh.
- D-1: chi bat co dieu kien theo station-set; global mac dinh khong boost.

Giai doan trien khai an toan:

1. Shadow table: `mb_g2_pair_lag_recurrence_shadow`.
2. Test-lane scorer: `MB_G2_PAIR_LAG_RECURRENCE_V1`.
3. Khong official promotion cho den khi co 7d/14d live closeout va false-promotion thap.

## 8. Public-safe status

- Official output changed: NO.
- Lane-test promoted: NO.
- Provider/manual AI called: NO.
- Production prompt switched: NO.
- Production ML switched: NO.
- Diagnostic/report only: YES.
- Public-safe scan: PASS by construction; no DB, no jsonl, no sensitive material, no runtime artifact included.
