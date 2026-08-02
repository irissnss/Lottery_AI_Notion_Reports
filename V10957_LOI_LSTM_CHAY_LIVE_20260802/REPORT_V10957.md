# V10957 — LSTM live ket so + lech tai suy luan; QD-015 shadow RF

**Ngày:** 02/08/2026 · **Commit riêng:** `(điền sau push)` · **Commit công khai:** `(điền sau push)` · **Trạng thái:** CHI DOC — không sửa code, không deploy

> Báo cáo theo khung A55.3. Owner ký đóng băng QD-014 tới hết 08/08; phiên này chỉ đọc + ghi quyết định.

---

## 1. Tóm tắt

Hai việc trong một phiên. (1) Ghi **QD-015**: owner duyệt trước để sau 08/08 tự chạy luồng bóng miền Trung bạch thủ bằng riêng `random-forest`, kèm chốt tự cắt khớp ≥95% trong 7 ngày đầu — không đổi số công bố, không đặt tiền. (2) Đào LSTM chạy live: trên MT số LSTM **kẹt 96** 17/119 ngày (hai chuỗi 10–14/07 và 19–25/07); live khớp tái suy luận chỉ **23,3%**/30 ngày chủ yếu vì file model bị huấn luyện đè mỗi chủ nhật; phát hiện lỗi kỹ thuật rõ — `combo_super` đọc `ml_probability` trong khi LSTM ghi `lstm_probability` nên mọi số LSTM nhận trọng số giả **0,5**. Bỏ LSTM khỏi phiếu bầu (proxy) **không đổi** số thắng phiếu (0,0pp); LSTM đơn live **−5,58pp** so với đánh bừa (z −2,19). **Chưa sửa gì** — chỉ đề xuất sau 08/08.

## 2. Owner yêu cầu gì (nguyên văn)

> *"Có. Duyệt trước để 08/08 tự chạy, kèm chốt tự cắt nếu tỉ lệ khớp dưới 95% trong 7 ngày đầu."*

> *"Đào ngay để hiểu nguyên nhân (chỉ đọc), nhưng chỉ sửa sau 08/08."*

Phạm vi đóng băng QD-014 vẫn hiệu lực: không đổi 15 model official, không đổi bộ lọc combo-super, không bật/tắt lớp ghi đè.

## 3. Đào bới / phát hiện

### 3.1 Chuỗi kẹt số LSTM (119 ngày × 3 miền)

| Miền | Số xuất hiện nhiều nhất | Chuỗi kẹt ≥3 ngày |
|---|---|---|
| **MT** | **96** × 17 ngày (14,3%) | 96: 10–14/07 (5 ngày); 96: 19–25/07 (7 ngày); thêm 87 (3 ngày), 61 (3 ngày) |
| **MN** | 81 × 21 ngày | Nhiều chuỗi dài: 31 (9 ngày), 81 (7 ngày), 51 (7 ngày), 53 (6 ngày)… |
| **MB** | 65 × 4 | **Không** có chuỗi ≥3 ngày |

Bằng chứng live 19–25/07 (analysis_text predictions): `adaptive_mode=fallback`, `top_n=10`, `confidence_level=VERY_LOW`, `avg_top5_prob≈0,52`, `top1_prob≈0,525–0,531`, `val_loss=0,229469895362854`. Xác suất gần phẳng — 96 thắng sát nút mỗi ngày.

Mốc huấn luyện LSTM tuần: … 12/07, 19/07, 26/07, **02/08**. Chuỗi kẹt **không** khớp restart `lottery.service` (journal không bắt được dòng start/stop hữu ích). File model lúc kẹt đã bị đè: backup còn lại 26/07 và 02/08 **không tái tạo** được chuỗi 96 khi chạy lại trên đúng ngày (old_ket_96=0/7). Nghĩa là: kẹt là thật (có trong DB + analysis_text), nhưng bản trọng số gây kẹt đã mất.

### 3.2 Vì sao live khác tái suy luận

Đường code **giống nhau**: `scheduler._run_free_model` → `predict_with_lstm` (cùng `lstm_predict.py`). Checkpoint có `meta_mean`/`meta_std` và predict có chuẩn hoá — không phải bẫy đưa đặc trưng thô vào scaler.

| Phép đo | Kết quả |
|---|---|
| 30 ngày MT gần nhất, live MDE vs `predict_with_lstm` (file .pt hiện tại 02/08 02:02) | Khớp top-1 **23,3%** (adaptive = force_top_n=5) |
| V10955 trước đó (15 ngày) | 13,3% |
| Trace live gần đây có V6.8 cross-boost | 13/40 bản |
| Adaptive mode trong 40 bản gần | 40/40 = `fallback` (top-10) |

**Nguyên nhân chính:** mỗi chủ nhật huấn luyện lại ghi đè `lstm_MT.pt`. Phát lại ngày cũ bằng file mới tất yếu lệch. **Nguyên nhân phụ:** một phần chu kỳ re-predict có `fresh_cross_tails`. Không thấy nhánh mặc định “thiếu dữ liệu” trên các ngày đo (đủ 30 ngày lịch sử).

### 3.3 Lỗi key xác suất (bằng chứng máy)

| | LSTM | RF (đối chứng) |
|---|---|---|
| Key trong `predictions[]` | `lstm_probability` | `ml_probability` |
| `combo_super` đọc | `ml_probability` → `probability` → **0,5** | `ml_probability` (đúng) |
| Thử ngày 22/07 | combo nhận `[0.5,0.5,0.5,0.5,0.5]` | RF nhận xác suất thật |
| Nếu đọc đúng `lstm_probability` | `[0.516, 0.5151, …]` | — |

`lech_do_sai_key = True`. Đây là lỗi kỹ thuật rõ, sửa một dòng — **chưa sửa** theo lệnh owner.

### 3.4 Bỏ LSTM khỏi phiếu bầu thì sao?

Hai lát cắt (nửa sau từ 06/05 = 87 ngày; ~90 ngày). Proxy: mỗi model official bỏ phiếu bằng top-1 / top-5 / top-10 từ `model_daily_eval`, so với/không LSTM.

| Lát | Có LSTM | Bỏ LSTM | Chênh |
|---|---:|---:|---:|
| top-1 · 87 ngày | 15,17% (−1,32pp) | 15,17% (−1,32pp) | **0,0pp** |
| top-5 · 87 ngày | 16,59% (+0,10pp) | 16,59% (+0,10pp) | **0,0pp** |
| top-10 · 87 ngày | 16,59% | 16,59% | **0,0pp** |

Trong 20 bundle MT gần nhất: LSTM **0 lần** nằm trong `voters` của số thắng cuộc. LSTM đơn live: **10,9%** vs bừa 16,48% → **−5,58pp, z −2,19** (đang phá, không phải trung tính). Holdout giấy (AUC 0,55 / V10955 +4,94pp top-1) là phép đo khác — **không dùng để nói live đang tốt**.

Metrics file hiện tại: `lift_vs_random=1,04` (precision@10) — ngay trên giấy cũng chỉ nhỉnh bừa một chút.

Số lát cắt đã thử: 2 cửa sổ thời gian × 3 độ sâu vote (top-1/5/10) + LSTM@K(1,3,5,10) + đối chiếu RF. Ngưỡng ý nghĩa: với ~87 ngày, chênh 0pp không cần z; LSTM đơn z=−2,19 đã rõ chiều âm.

### 3.5 Holdout tốt / live tệ — nói thẳng

Không có bằng chứng rằng “sửa một chỗ là LSTM live sẽ thành +4,94pp”. Bản holdout và bản live đang đo hai thứ khác nhau; live top-1 đang âm nặng; phân phối xác suất gần phẳng (std≈0,01–0,015). Sửa key có thể làm LSTM **có trọng số thật** trong combo — có thể tốt hoặc tệ hơn, phải đo shadow, không đoán.

## 4. Hướng xử lý và vì sao chọn

### Việc 1 — QD-015 (owner đã chọn)

Owner chọn duyệt trước shadow RF-only + chốt tự cắt 95%. Loại phương án kèm XGB vì V10955b: XGB tái suy luận chỉ +0,10pp. Chưa dựng code shadow trong cửa sổ đóng băng (tránh deploy).

### Việc 2 — LSTM (chỉ đề xuất)

| Phương án | Ước lợi | Rủi ro | Chọn? |
|---|---|---|---|
| A. Sửa key `lstm_probability` trong `combo_super` | Khôi phục tín hiệu xác suất đúng; lỗi kỹ thuật rõ | Trọng số LSTM tăng từ giả 0,5 → ~0,52; chưa biết giúp hay hại phiếu | **Đề xuất sau 08/08**, kèm đo shadow |
| B. Loại LSTM khỏi vote official cho đến khi live top-1 không còn âm | Proxy hiện tại 0pp với số công bố; giảm rác trong MDE/score | Mất cơ hội nếu sau này live hồi | Đề xuất đo song song với A |
| C. Sửa kiến trúc/huấn luyện LSTM (focal, temperature, early stop epoch 4–5) | Có thể giảm kẹt / phân phối phẳng | Rộng, dễ đụng đường ra số; QD-014 cấm | Chỉ sau đóng băng + có ngưỡng đo |
| D. Không làm gì | 0 công | LSTM tiếp tục −5,58pp trong MDE; key sai vẫn còn | Không khuyến nghị lâu dài |

**Nói thẳng:** với số liệu hiện tại, **không** kỳ vọng sửa LSTM sẽ thu lại vài điểm phần trăm công bố trong ngắn hạn (nó gần như không vào voters). Việc đáng làm trước là sửa key + đo, và ưu tiên shadow RF (QD-015) mới là chỗ còn +3pp đo được.

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `docs/OWNER_DECISION_LEDGER.json` (+ `.md` sinh máy) | Thêm **QD-015** |
| `docs/FOLLOW_UP_TRACKER.md` | **FU-216**, **FU-217** |
| `CHANGELOG.md` / `docs/CURRENT_TRUTH_SSOT.md` | Khối V10957 qua `prepend()` |
| `docs/AUTOMATION_STATE.json` | `governance_seq` 374→375, `_v10957_last_event` |
| `web/backend/_v10957_lstm_*.py` | Script chỉ-đọc paramiko |
| `artifacts/v10957_*.json` | Bằng chứng thô |

**Backup / deploy / hash 4 bảng khoá:** không áp dụng vì không sửa runtime, không deploy.

## 6. Cổng kiểm

| Mục | Kết quả |
|---|---|
| Chỉ đọc — không sửa model / không deploy | Đạt |
| QD-015 trong sổ + `kiem_code` khớp 4/4 | Đạt (`_v10920_decision_ledger.py`) |
| FU-216 hạn 08/08, `OWNER_LOCK`, có chốt tự cắt | Đạt |
| Báo cáo đủ 9 phần + evidence/ | Đạt (cổng A55 sau push) |
| Notion ghi | Không đụng (A55.1) |
| OD-20260731-A (mốc FINAL) báo TRÔI 4/4 trên máy local | **Có từ trước** — không xử trong phiên này (ngoài phạm vi; cửa sổ đóng băng) |

## 7. Vướng vấp

1. **File model lúc kẹt 96 đã mất** — không tái tạo được chuỗi bằng backup 26/07/02/08. Hậu quả nếu bỏ qua: tưởng “không từng kẹt” vì phát lại không ra 96; thật ra DB + analysis_text vẫn chứng minh.
2. **Proxy phiếu ≠ combo_super đầy đủ** (trọng số WR, bonus ML, AI…). Hậu quả: chênh 0pp là cận dưới tin cậy cho “có đổi số thắng cuộc không”, không phải mô phỏng 100% score nội bộ.
3. **Holdout đẹp dễ tô hồng** — agent trước đã từng; phiên này cố tình đặt live −5,58pp lên trước.
4. Script đào sâu lần 1 lỗi `TypeError` vì lấy nhầm list ngày — đã sửa và chạy lại.

## 8. Gỡ về

Không áp dụng cho code runtime (không sửa). Gỡ tài liệu nếu cần:

```
git checkout HEAD~1 -- CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md docs/FOLLOW_UP_TRACKER.md docs/OWNER_DECISION_LEDGER.json docs/AUTOMATION_STATE.json
```

Xóa QD-015 / FU-216 khỏi sổ và tracker. Mất khoảng 5 phút.

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng / hạn |
|---|---|---|
| **FU-216** | Dựng + bật shadow RF MT theo QD-015 | Khởi động **08/08**; tự cắt nếu khớp &lt;95%/7 ngày |
| **FU-217** | Sửa key `lstm_probability` + đo ảnh hưởng vote | Sau 08/08; không merge vào official khi chưa có số shadow |
| **FU-215 / QD-014** | Đóng băng đường ra số | Hết **08/08** |
| **QD-013** | Cổng lợi thế vẫn đóng | Shadow không được mở tiền |

---

### Phụ lục — thiết kế shadow QD-015 (chưa code)

1. Mỗi ngày sau chốt MT: lấy `bt_number` của `random-forest` từ đường predict hiện tại → ghi bảng shadow (`output_eligible=0`, `shadow_only=1`).
2. Không ghi đè `final_bundles` / `/du-doan`.
3. Song song: tái suy luận cùng file `.pt` đang load; đếm tỷ lệ khớp theo ngày.
4. Ngày 1–7: nếu khớp &lt;95% → tắt job, mở ticket train/serve (không “cứ để chạy”).
5. Sau ≥60–90 ngày: mới xét z và cổng QD-013 — cửa lợi thế vẫn đóng cho đến khi đủ ngưỡng.
