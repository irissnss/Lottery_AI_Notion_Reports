# V10867 — Closeout toàn diện 27/07: official 0/3, selection miss và sửa bằng chứng M2

## Kết luận ngắn

Ngày 27/07 thực sự tệ:

- official BT 0/3, any 0/3;
- K-lane 0/3;
- V3 0/3;
- chỉ Total-V2 MT bắt đúng BT32 và `/choi` MT có 32 ở số phụ.

Không có bằng chứng DB/service/provider/UI corruption. Lỗi chính:

1. MN và MT có tín hiệu đúng ở đơn-model nhưng tầng ranking chọn sai.
2. MB gần như không có supply đúng.
3. MT official chỉ cho 13/15 model vào vote; gpt-5.4 BT32✓ bị cap.
4. Bằng chứng M2 +8.3pp trước đây bị phồng bởi catch-up rows hậu kỳ.

## Nguồn và hạ tầng

Paired sync:
`artifacts/live_sync/20260727_192521/manifest.json`; final post-nightly sync
`artifacts/live_sync/20260727_211636/manifest.json`.

Lần sync đầu 19:24 bị size-guard chặn vì DB tăng trong lúc tải; retry 19:25 thành công,
chứng minh guard bảo vệ đúng.

- self-check 11/11 PASS;
- V10841 contract PASS;
- health 200;
- journal/scheduler ERROR 0;
- DB quick_check OK;
- causal timing 7 ngày: 0 violation;
- trace 73/73 PB-18.1 + rules;
- fallback/degraded = 0;
- MT K10 chốt 16:53, MB K8 chốt 17:52;
- không có DIR1 row sau deadline;
- ba money-board locks có output.

## Ma trận ba miền × bốn luồng

| Miền | Official | K-lane | Total-V2 | Total-V3 | `/choi` |
|---|---|---|---|---|---|
| MN | 42/32 ✗ | 42/02/32 ✗ | 42/32 ✗ | 42/02 ✗ | 42 ✗ |
| MT | 15/25 ✗ | 15/25/98 ✗ | **32/98 — BT32✓** | 37 ✗ | 15/32 — **phụ32✓** |
| MB | 37/16 ✗ | 37/16/32 ✗ | 37/16 ✗ | 37 ✗ | 37/14 ✗ |

MB champion cũ 88/39 có 39 về lô, nhưng BT88 vẫn trượt; K11a không đổi verdict BT.

## Supply đơn-model

| Miền | BT đúng | Any đúng | Sự thật |
|---|---:|---:|---|
| MN | 2/15 | 4/15 | xgboost + random-forest BT14✓; 14 bị rank #5 |
| MT | 6/15 | 7/15 | random-forest BT91✓; 5 AI BT32✓; official chọn cluster ML15 |
| MB | 0/15 | 1/15 | chỉ opus có số phụ92✓; supply thật sự yếu |

Official 0/3 dù tổng cộng MN+MT có 8 model-region BT đúng: selection miss là thật,
không phải cảm giác.

## Vì sao MT bỏ 32

- ML cluster 15: combo-no-token, xgboost, smart-ml, smart-ensemble, cùng random-forest
  secondary → score 0.133.
- AI cluster 32: gemini-pro, gemini-flash, sonnet, gpt-mini → score 0.0616.
- Các AI 32 phần lớn verdict SKIP nên bị downweight.
- gpt-5.4 cũng BT32 nhưng bị `MT_top13_only_V10752_weakest_dropped`.
- Total-V2 đếm coverage main+phụ và neo rules nên chọn 32.

## Pool official input versus scoreable

| Miền | Input | Scoreable 27/07 | 10 ngày incomplete | Excluded BT cứu official-miss |
|---|---:|---:|---:|---:|
| MN | 15 | 15 | 0/10 | 0 |
| MT | 15 | 13 | 10/10 (1 ngày chỉ11) | **5/10** |
| MB | 15 | 14 | 9/10 | 1/10 |

V10752 top13 từng là policy owner duyệt, không phải model/provider thiếu output. Nhưng dưới
PB-18.1 hiện tại nó cần re-verify tại CP-L6 ngày 28/07. Không tự bỏ cap tối 27.

## Hai ngày 0/3 liên tiếp

Official BT hit theo ngày 18→27:

`0, 1, 1, 1, 2, 1, 2, 2, 0, 0`.

Từ 10/05 có bốn chuỗi 2 ngày 0/3 trước đó. Hai ngày 26–27 rất xấu và đáng báo động,
nhưng không đủ để kết luận corruption hoặc rollback prompt khi trial tổng vẫn:

- LLM any 48.6% → 61.4%;
- official bundle BT 20.0% → 33.3%;
- LLM BT 31.4% → 30.0% (gần ngang, MN/MB giảm, MT tăng).

## Lỗi measurement M2 đã sửa

Claim cũ: M2s 12/24 vs M0 10/24 = +8.3pp.

Root:

- sáu row 19–20 được catch-up ngày 22–23;
- gắn `row_source=forward`;
- số M2 hậu kỳ khác số V10822 lane đã persist trước giờ xổ;
- re-materialize bằng snapshot rules mới còn có thể đổi lịch sử thêm.

Truth dùng để quyết writer:

- persisted lane `TOTAL_V2_RULES_V1`;
- M2s 11/27 vs M0 10/27;
- BT lift +3.7pp;
- any lift +18.5pp;
- n=27 < 30;
- gate `WAIT_N_LT_30`, chưa đạt +5pp.

Fix:

- row shadow chỉ giữ nhãn `forward` khi BT trùng persisted lane;
- mismatch → `postdraw_mismatch`, diagnostic-only;
- panel có khối GATE PRE-DRAW riêng;
- V10841 khóa decision basis;
- output-contract hiển thị input→scoreable và model bị loại nhưng BT đúng.

## K-lane

- K15 MT in-trial: champion 5/10, challenger 4/10, net −1 → chưa flip gate.
- K11a MB in-trial: challenger 2/10, champion 1/10 → giữ challenger.
- Hôm nay K15 champ/chall đều BT15 trượt.
- Hôm nay K11 champ88/chall37 đều BT trượt.

## Deploy an toàn

- 4/4 MD5 local=VPS;
- py_compile PASS;
- backfill shadow labels 19–26;
- persist output-contract 27/07 trước natural cron;
- restart service;
- health 200;
- admin endpoints guest 401;
- journal 0;
- official hash-4 pre/post IDENTICAL.
- natural nightly chain 20:15→21:10: MRE15, M2 3/3, rule-cond3/3, MB what-if1,
  monitor zero alert.

Backup:

- VPS `/root/backups_v10867/`;
- local `backups/v10867_pre/`.

Closeout reporter itself was also corrected: it previously summarized the matched-shadow subset
as `n20/+10pp`; it now reads the persisted pre-draw lane and returns `n27/+3.7pp`.

## Quyết định

Không đổi production tối 27:

- M2 chưa đủ n và chưa vượt +5pp thật;
- K15 chưa flip gate;
- K11a đang thắng champion;
- top13 MT là owner-gated policy.

Ngày 28/07 cần quyết bằng dữ liệu corrected:

1. MT cap13 hay exact-scoreable15.
2. M2 sau khi đủ n30.
3. K15/K11a theo đoạn in-trial.
4. Lean roster/CP-R4 sau cùng, một biến số mỗi lần.

Notion short page: `3aa1d385-9bf8-81b8-961f-f512561130b3`.

