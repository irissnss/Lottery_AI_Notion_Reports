# V10830 — Báo cáo tổng lực toàn diện lần 2 (21/07/2026)

Owner 11:25 21/07 (re-reminder): chu kỳ live thất bại, MB rules có mà model mốc, 26/46-69 ở đâu, LLM gộp là sao, điều kiện đào ra vẫn mơ hồ → kiểm tra tổng lực 3 miền, 4 luồng, từng model, cơ chế tổng hợp + học tập.

Nguồn dữ liệu: DB + trace synced `artifacts/live_sync/20260721_112853` (sha256 khớp VPS). Audit READ-ONLY.

## 1. Chu kỳ /choi (khóa 13/07, chạy 13–19/07 + ngày đầu tuần mới 20/07)

| Miền | BT | any | Ghi chú |
|------|----|-----|---------|
| MN | 2/7 | 2/7 | 19/07 90✓; 20/07 đeo 26✗ |
| MT | 5/8 | 5/8 | luồng khỏe nhất (63✓ 41✓ 87✓…) |
| **MB** | **0/8** | 2/8 | 19/07 [69,93]✗ · 20/07 [46,69]✗ = chase + AE lag-1 pre-fix |

Kết luận: cảm nhận "cực kỳ thất bại" đúng nhất ở **MB**; MT thực tế dương; MN trung tính.

## 2. Bốn luồng, trial 18–20/07 (9 ô region-day)

| Luồng | BT✓ | Ghi chú |
|-------|-----|---------|
| M0 official | 2/9 | 90✓ (19/07 MN), 87✓ (20/07 MT) |
| Lane TOTAL_V2 | 1/9 | 90✓ |
| M2s shadow | 3/9 | 13✓ 46✓ 90✓ |
| A/B arm-B | any 16/45 | so cùng kỳ arm-A xem CP-S3 23/07 |

Ngày 20/07: cả M0 + lane + M2s + /choi cùng đeo **26** — 26 về cả 3 miền ngày 19/07 (herd n=3, verify từ KQ).

## 3. Từng model (non-shadow, 9 slot = 3 ngày × 3 miền)

Tệ nhất Δany vs nền 90d: **gpt-5.4 −25pp · random-forest −25 · combo-no-token −20 · deepseek-reasoner −16 · smart-ml −14**.  
Tốt: **gemini-2.5-flash +24 (any 7/9, main1 4/9) · lstm +12 · xgboost +12**.

Gộp nhóm ("LLM gộp" = tổng any-hit 7 LLM ÷ tổng lượt — chỉ là thước đo guard-rail, không phải cơ chế đẩy số):

| Nhóm | Trial | Nền 90d | Δ |
|------|-------|---------|---|
| LLM ×7 | 52.4% | 55.4% | −3.0pp |
| ML ×8 | 50.0% | 55.5% | −5.5pp |
| LLM tại MB | 33% | 42% | −8pp |
| ML tại MB | 29% | 40% | −10pp |

Chưa chạm ngưỡng rollback (−10pp gộp). Điểm gãy là **MB**, khớp mục 1–2.

## 4. Rules vs model (câu "MB rules có mà model mốc")

| Ngày | Miền | Union VỀ | Winner đáng chú ý |
|------|------|----------|--------------------|
| 18/07 | MN | 9/13 | 13 (4 LLM chọn ✓ M2s bắt) — 7 số khác 0-vote |
| 18/07 | MB | 3/9 | 86 (4 LLM) ✓; 34/46 0-vote |
| 19/07 | MB | 4/14 | **63 có 2 phiếu ML nhưng bị 7 phiếu 46 đè**; 43/68 0-vote |
| 20/07 | MB | **0/10** | ngày chết thật của rules — không ai cứu nổi |

Kết luận: rules vẫn nhả winner gần như mỗi ngày; hỏng ở **tầng chọn** (herd/chase đè, winner ít phiếu) + **ngày chết** cần tầng A cắt bớt.

## 5. Nguồn gốc 26 / 63 / 46-69 (re-verify từ DB)

- **26 (20/07)**: rule #2102/#2103 (MN), #2137–2140 (MT), #2171/2172/2174/2175 (MB) — tất cả đọc **MB/Thái Bình G7-family D−1 (G7=26)**; tier LIMITED_WEIGHT / READY_WITH_CAUTION, **không có READY_STRONG nào**. Không ai "nhét tay" — RULES-FIRST ép model nhìn danh sách, tầng vote dồn theo.
- **63 (19/07 MB)**: rule #2202 (MT/Khánh Hòa GĐB+G7) — phát đúng, về thật.
- **46/69**: 46 nằm trong union rules 19/07; **69 KHÔNG thuộc rules** (chase của bundle). Cặp này vào /choi 20/07 qua **AE lag-1 0-vote** — đã fix V10828 (vote-gate). AE trace cho 21/07 (shadow test-lane) vẫn liệt 26 rank-2 → watch lock MB 17:5x tối nay: không được khóa số 0-vote.

## 6. Học tập / tích lũy / xếp hạng

Retrain CN 19/07 ✓ (training_history id 193–204) · miner W30 105 rules active ✓ · MRE 3008 rows, max 20/07 ✓ · re-rank MN/MT/MB snapshot 21/07 ✓ · model_daily_eval 27 model/ngày ✓ · self-check sáng 21/07 **11/11 PASS** · journal 0 lỗi. → Không có bộ phận học tập nào chết.

## 7. Điều kiện ĐÃ đào ra (V10829 — trả lời "vẫn mơ hồ")

Backtest 180 ngày, bền 2 nửa, placebo rank 1/20:

| Điều kiện | Nghĩa tiếng thường | Precision | vs RAW 38.18% |
|-----------|--------------------|-----------|----------------|
| H-A1a | chỉ giữ đuôi từ rule hạng READY_STRONG | 50.1% | +11.9pp |
| H-A4b | READY_STRONG ∧ nguồn có GĐB/G1 (loại G7 đơn độc kiểu 26) | 49.6% | +11.4pp |
| H-A4a | rule khỏe ∧ số KHÔNG vừa về ≥3 miền hôm qua | 42.1% (n=290) | +3.9pp |
| **B: H-A4a∧H-B2a** | thêm: không phải số đuổi D−1 | **BT 46.9%** | vs M0 31.6% (+15.2pp) |
| H-B1a | chỉ đẩy khi có model vote hôm nay | BT 42.5% | +10.4pp vs M0 |

Minh họa 18–20/07 (in-sample — trung thực ghi rõ): B-best BT✓ **5/9 ô** vs official 2/9; 20/07 điều kiện **cắt 26 cả 3 miền**; 19/07 MB chọn **63✓** thay 69✗. Forward thật từ 21/07; đọc ngưỡng 04–11/08; chỉ khi vượt +5pp mới trình wire.

Panel `/monitoring` 📐 nay có khối **"📖 Nghĩa tiếng thường"** để đọc không cần nhớ mã.

## 8. An toàn phiên này

ZERO đổi production (đúng lệnh "không nói tới đâu fix tới đó"). Chỉ 1 file UI chú giải; sha khớp; health 200; admin 401; **hash 4 bảng pre=post IDENTICAL** `556073f8`/`44bf969e`/`7ce7a13f`/`07b4fbc5`. Backup `backups/v10830_pre/` + `/root/backups_v10830/`.

## 9. Watch còn lại hôm nay

15:47 lane MN → 16:56 lane MT → **17:5x lock MB (verify AE vote-gate sống)** → 20:15 MRE → 21:00 V10829 forward row đầu. GĐB watch: xuôi cand 39 · đảo cand 93 (GĐB MB 20/07 = 39128).
