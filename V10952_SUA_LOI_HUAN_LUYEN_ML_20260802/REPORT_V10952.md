# V10952 — Huấn luyện ML hỏng vì ống ghi đã đóng; bảng "OK" không có số chất lượng; MT vẫn còn tín hiệu

**Ngày:** 01–02/08/2026 · **Loại:** đào lỗi hạ tầng huấn luyện + sửa chỗ ghi chất lượng + đo lại AUC
**Trạng thái:** code đã deploy · chạy thật một lượt đã ghi được số · báo cáo công khai hoàn tất phiên bị ngắt

> Phiên kỹ thuật đã xong nhưng bị ngắt giữa chừng (hết hạn dùng model) trước khi kịp viết báo cáo
> và đẩy hai repo. Bản này hoàn tất phần còn lại — **không** sửa thêm code, **không** deploy lại,
> **không** chạy lại phép đo.

---

## 1. Tóm tắt

Có hai lỗi khác nhau. **Lỗi 1** (huấn luyện chết hàng loạt) đã tìm ra nguyên nhân gốc: job chạy
trong tiến trình dịch vụ web, ống ghi màn hình đã bị job trước đóng, mọi `print()` nổ ngay với
`I/O operation on closed file` — cả 12 model chết trong 1 giây. Đúng 7 chủ nhật bị
(17/05 → 12/07). Lỗi này **đã được sửa từ 15/07 (V10800)** bằng tiến trình riêng; hai chủ nhật
sau đó đều thành công. Bảng tỉ lệ hỏng owner nhìn thấy là ảnh quá khứ, không phải lỗi đang chảy.

**Lỗi 2** (vẫn hỏng tới 01/08) mới là cái phiên này sửa: bản vá 15/07 rút câu lệnh ghi bảng còn
4 cột nên `auc`, `old_auc`, `test_loss`, `samples` rỗng hoàn toàn từ 19/07. Đồng thời
`_retrain_all.py` bắt mọi lỗi rồi luôn trả mã thoát 0, nên scheduler ghi cả 12 dòng "OK" dù mọi
model lỗi. Đã dựng chỗ ghi duy nhất `_v10952_training_journal.py` và sửa mã thoát thật.

**Đo lại AUC — kết luận quan trọng nhất:** tín hiệu miền Trung **không chết**. MT
random-forest 0,5517 · xgboost 0,5475 · meta-learning 0,5356 · lstm 0,5467 — cả bốn trên 0,5,
giữ mức ngày 31/05. MB cả bốn đúng bằng ngẫu nhiên (0,4963–0,5017). Kiểm chéo 6 ngày mới cùng
hướng. Phần mất nằm ở **khâu chuyển tín hiệu thành số công bố**, không ở tầng model.

**V10952b (00:02 ngày 02/08):** chạy thật một lượt — bảng ghi 12/12 dòng có AUC. Nhưng 8/9 model
giảm AUC sau huấn luyện lại (MT random-forest 0,5517 → 0,5248). Phép so **chưa công bằng** vì hai
con số nằm trên hai cửa sổ thời gian khác nhau — đó là lý do không bật lại cổng tự gỡ model.

---

## 2. Owner yêu cầu gì (nguyên văn)

Owner 01/08 khuya yêu cầu đào tận gốc tiếp: bảng `training_history` cho thấy tỉ lệ hỏng tăng vọt
từ tháng 5, và mọi bản ghi gần đây đều không có chỉ số chất lượng.

Bối cảnh nối từ V10947 / V10945: hệ từng có lợi thế thật ở MT rồi tắt từ tháng 6; owner đã dừng
đặt tiền thật (QD-013). Câu hỏi tiếp theo là tầng model còn tín hiệu hay đã chết — và vì sao
không ai biết model tốt hay tệ khi bảng chỉ ghi "OK".

Phiên này (bước hoàn tất báo cáo) nhận nhiệm vụ từ agent cha: chỉ viết báo cáo công khai, kiểm
nhanh, đẩy đúng phạm vi V10952 — không sửa code, không deploy lại, không đo lại.

---

## 3. Đào bới / phát hiện

### 3.1 Lỗi 1 — nguyên nhân gốc đã tìm ra (và đã sửa từ 15/07)

Nguyên văn nhật ký, thứ bảy 16/05 19:00 UTC (= chủ nhật 17/05 02:00 giờ VN):

```
❌ [MT] Meta-Learning retrain failed: I/O operation on closed file.
❌ [MT] LSTM retrain failed: I/O operation on closed file.
❌ [MT] xgboost retrain failed: I/O operation on closed file.
❌ [MT] random-forest retrain failed: I/O operation on closed file.
... y hệt cho MN và MB — cả 12 model chết trong đúng 1 giây
```

Huấn luyện chạy **bên trong** tiến trình dịch vụ web. Một job chạy trước đã đóng ống ghi màn hình
của tiến trình đó, nên mọi lệnh `print()` trong bộ huấn luyện nổ ngay từ dòng đầu — chưa kịp đọc
một mẩu dữ liệu nào.

Đúng 7 chủ nhật bị:

```
17/05 · 24/05 · 31/05 · 14/06 · 21/06 · 28/06 · 12/07
```

Cùng lỗi đó cũng giết bộ tối ưu trọng số lúc 03:00 mỗi chủ nhật đó.

Những chủ nhật chạy được là những chủ nhật dịch vụ vừa được khởi động lại trước đó ít phút — ống
ghi còn mới. Ví dụ 02/05: tắt 18:59:14, khởi động lại 18:59:20, job chạy 19:00:00 và thành công.

**Đã sửa ngày 15/07 (V10800)** — chuyển sang tiến trình riêng. Hai chủ nhật sau (19/07, 26/07)
đều thành công. Bảng thống kê tỉ lệ hỏng là ảnh quá khứ.

### 3.2 Lỗi 2 — "OK" là lời tự khen, không có gì kiểm chứng (vẫn hỏng tới 01/08)

Đếm số dòng có ghi AUC theo ngày huấn luyện:

```
29/03 → 05/07   9/12 dòng có AUC   (9 = 3 miền × 3 model; LSTM chưa từng có AUC)
19/07, 26/07    0/12 dòng có AUC   ← từ đây trở đi rỗng hoàn toàn
```

Đúng mốc V10800. Bản sửa 15/07 chuyển sang tiến trình riêng nhưng câu lệnh ghi bảng bị rút gọn
còn 4 cột `(date, region, model_type, status)`. Bốn cột `auc`, `old_auc`, `test_loss`, `samples`
biến thành rỗng. Cổng so AUC cũ với AUC mới do đó không thể hoạt động.

Nặng hơn: `_retrain_all.py` bắt mọi lỗi rồi in ra và đi tiếp, **chưa bao giờ trả mã thoát khác 0**.
Bộ tự chữa cũng luôn trả 0. Dù cả 9 model lỗi, scheduler vẫn thấy `rc=0` và ghi cả 12 dòng "OK".
Từ 19/07 trở đi mọi dòng "OK" trong bảng đều không chứng minh được gì.

Bộ tự chữa 06:30 — nơi DUY NHẤT huấn luyện LSTM — chưa từng ghi dòng nào vào `training_history`.
Lần tự chữa 13/07 (model đã cũ 8,2 ngày) không để lại dấu vết.

### 3.3 Đo lại AUC — MT vẫn còn tín hiệu

AUC 0,5 = ngẫu nhiên hoàn toàn. Đo trên phần 20% cuối theo thời gian, model chưa khớp tham số
trên phần đó (2.400 mẫu, 27/05 → 25/07), đặt cạnh số cũ ngày 31/05:

| miền | random-forest | xgboost | meta-learning | lstm |
|---|---|---|---|---|
| **MT** | **0,5517** (31/05: 0,549) | **0,5475** (31/05: 0,552) | **0,5356** | **0,5467** |
| MN | 0,5188 (31/05: 0,506) | 0,5121 (31/05: 0,498) | 0,5092 | 0,5055 |
| MB | 0,4963 (31/05: 0,490) | 0,5002 (31/05: 0,504) | 0,5017 | 0,5002 |

Kiểm chéo trên 6 ngày hoàn toàn mới (27/07 → 01/08, sau mốc huấn luyện 26/07, 240 mẫu):

- MT: random-forest **0,5742** · meta-learning 0,5645 · xgboost 0,5472 — cùng hướng
- MB cùng cửa sổ: 0,482–0,496 — dưới ngẫu nhiên

**Kết luận:** tín hiệu ở MT **không chết**. AUC giữ ~0,54–0,55 y như 31/05, hai tháng sau khi lợi
thế tiền thật đã tắt. Cả bốn họ đều nhỉnh ở MT và cả bốn đều đúng bằng ngẫu nhiên ở MB. Phần mất
nằm ở khâu chuyển tín hiệu thành số công bố, không ở tầng model.

### 3.4 V10952b — chạy thật 00:02 ngày 02/08

Bảng `training_history` ngày 2026-08-02 — **12/12 dòng, 12 dòng có AUC, 9 dòng có AUC cũ**:

| miền | model | AUC mới | AUC cũ | lệch | test_loss | n mẫu | nguồn |
|---|---|---|---|---|---|---|---|
| MT | lstm | 0,5537 | — | — | 0,2283 | 100 | guard |
| MT | meta-learning | 0,5327 | 0,5356 | −0,0029 | — | 2400 | _retrain_all |
| MT | random-forest | 0,5248 | 0,5517 | −0,0269 | — | 2400 | _retrain_all |
| MT | xgboost | 0,5278 | 0,5475 | −0,0197 | — | 2400 | _retrain_all |
| MN | lstm | 0,5095 | — | — | 0,1974 | 100 | guard |
| MN | meta-learning | 0,5115 | 0,5092 | +0,0023 | — | 2400 | _retrain_all |
| MN | random-forest | 0,5041 | 0,5188 | −0,0147 | — | 2400 | _retrain_all |
| MN | xgboost | 0,5019 | 0,5121 | −0,0102 | — | 2400 | _retrain_all |
| MB | lstm | 0,4991 | — | — | 0,2653 | 100 | guard |
| MB | meta-learning | 0,4769 | 0,5017 | −0,0248 | — | 2400 | _retrain_all |
| MB | random-forest | 0,4883 | 0,4963 | −0,0080 | — | 2400 | _retrain_all |
| MB | xgboost | 0,4917 | 0,5002 | −0,0085 | — | 2400 | _retrain_all |

8/9 model giảm AUC. Chỉ MN meta-learning tăng (+0,0023). Hai model vượt ngưỡng cảnh báo −0,02:
MT random-forest và MB meta-learning.

**Nhưng phép so chưa công bằng:** `old_auc` đo cửa sổ 27/05→25/07; `auc` mới đo cửa sổ dịch về
sau ~1 tuần (mỗi lần huấn luyện thu 300 ngày tính từ hôm đó nên 20% cuối trượt theo). "Tụt 0,027"
có thể là model kém đi, cũng có thể chỉ là tuần mới khó đoán hơn. Chưa phân biệt được bằng dữ
liệu hiện có.

Sau lượt chạy: MT cả bốn vẫn trên 0,5 (lstm 0,5537 · meta 0,5327 · xgb 0,5278 · rf 0,5248).
MB cả bốn dưới hoặc bằng 0,5. Kết luận về MT không đổi.

### 3.5 Tự thú: đo sai một lần

Lần đo đầu đưa đặc trưng **thô** vào `meta-learning`, nhưng model đó chuẩn hoá đặc trưng
(`StandardScaler`) trước khi học. Kết quả sai: MT 0,4995 · MN 0,5388 · MB 0,5189 — suýt kết luận
ngược rằng meta-learning ở MT bằng ngẫu nhiên. Sau khi dùng đúng bộ chuẩn hoá, số đo khớp **chính
xác** con số model tự lưu trong file (MT 0,5356). Đó là bằng chứng phép đo đã đúng.

---

## 4. Hướng xử lý và vì sao chọn

| Phương án | Quyết định | Vì sao |
|---|---|---|
| Sửa lỗi 1 (ống ghi đóng) | Không cần — đã sửa V10800 | Đã chạy ổn 19/07 và 26/07 |
| Dựng chỗ ghi bảng duy nhất + mã thoát thật | **Đã chọn** | Lỗi 2 đang chảy; không ghi số thì không biết model tốt hay tệ |
| Bật lại cổng tự gỡ model khi AUC tụt >0,02 | **Không chọn** | Phép so hai cửa sổ khác nhau — cổng cũ có thể gỡ oan / giữ oan. Owner đã chốt FU-209 dừng tỉa tót model |
| Chỉ ghi số và cảnh báo, không đổi model production | **Đã chọn** | An toàn; owner đã dừng đặt tiền thật |
| Đo lại AUC trên cửa sổ cố định | **Đã chọn** (đo một lần) | Trả lời câu hỏi "tín hiệu MT còn không" |
| Sửa phép so AUC cũ↔mới trong phiên này | **Hoãn → FU-213** | Cần giữ bộ kiểm cố định mỗi lần huấn luyện; không vội bật cổng |

---

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `web/backend/_v10952_training_journal.py` | **Mới** — một chỗ ghi bảng duy nhất. `COALESCE(?, cũ)` nên gọi lại không xoá số đã có. Đọc AUC model cũ TRƯỚC khi đè. Ngày theo giờ VN |
| `web/backend/_retrain_all.py` | Ghi đủ `auc` + `old_auc` + `samples` cho meta/xgb/rf. **Mã thoát 1 nếu có model lỗi** |
| `web/backend/_v10646_retrain_guard.py` | Ghi số LSTM (`auc`, `test_loss`). **Mã thoát 1 nếu có model lỗi.** Đọc file kết quả JSON thay vì đoán qua stdout |
| `web/backend/lstm_model.py` | Tính AUC cho LSTM (trước chỉ có val_loss và precision@10) |
| `web/backend/scheduler.py` | Thôi ghi đè 12 dòng 4 cột. Chỉ ghi bù FAILED cho dòng còn thiếu |
| `web/backend/_v10952_*.py` | Script đào lỗi, đo AUC, deploy, xác minh, cập nhật tài liệu |
| `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` · `docs/FOLLOW_UP_TRACKER.md` · `docs/AUTOMATION_STATE.json` | Ghi phát hiện, quyết định, FU-211/212/213 |

**Backup:** `backups/v10952_pre/` (local) — `_retrain_all.py`, `_v10646_retrain_guard.py`,
`lstm_model.py`, `scheduler.py`. Trên VPS: `/root/Lottery_AI_Test/backups/v10952_models_pre/`
(30 file model trước lượt chạy thật 00:02).

**Deploy:** đã deploy trước khi phiên bị ngắt. Service `lottery`. Băm 4 bảng khoá
(`predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`) y nguyên trước/sau lượt
chạy thật. Không đụng `/du-doan`, writer `final_bundles`, bộ chọn số công bố.

**Không làm trong bước hoàn tất báo cáo này:** không sửa code, không deploy lại, không đo lại.

---

## 6. Cổng kiểm

| Mục | Kết quả |
|---|---|
| File code V10952 có mặt | Đạt — `_retrain_all.py`, `_v10646_retrain_guard.py`, `lstm_model.py`, `scheduler.py`, `_v10952_training_journal.py` + 7 script `_v10952_*.py` |
| Backup `backups/v10952_pre` | Đạt — 4 file |
| Cú pháp Python (`py_compile`) | Đạt — 12/12 file |
| Lượt chạy thật 00:02 ngày 02/08 | Đạt — 12/12 dòng có AUC; mã thoát 0 vì 0/12 model lỗi (lần này 0 là đúng thật) |
| LSTM lần đầu có AUC + test_loss | Đạt |
| Băm 4 bảng khoá trước/sau chạy thật | Y nguyên |
| Phép so AUC cũ↔mới công bằng? | **Chưa** — ghi FU-213; không bật cổng tự gỡ |
| FU-211 xác minh job tự động 02:00 | Lượt `--force` 00:02 đã chứng minh chỗ ghi hoạt động; job tự động 02:00 cùng ngày sẽ đè lại — vẫn nên đối chiếu sau 02:00 |

---

## 7. Vướng vấp

1. **Phép so AUC chưa công bằng (FU-213).** Hậu quả nếu bỏ qua: bật lại cổng tự gỡ model dựa trên
   "tụt AUC" sẽ gỡ oan model tốt hoặc giữ model tệ chỉ vì tuần mới khó/dễ hơn. Đã từng có 3 lần
   `ROLLBACK` trong bảng (05/04, 26/04, 10/05) mà không chắc lần nào đúng.

2. **Đo sai meta-learning lần đầu (đặc trưng thô).** Hậu quả nếu bỏ qua và không nói: suýt kết luận
   ngược rằng meta ở MT bằng ngẫu nhiên (0,4995). Bài học: đo model nào cũng phải hỏi model đó có
   chuẩn hoá đầu vào không.

3. **Phiên kỹ thuật bị ngắt trước khi có báo cáo công khai.** Hậu quả nếu bỏ qua bước này: vi phạm
   A55 — code đã deploy mà không có báo cáo = phiên chưa xong; owner mất dấu kiểm soát.

4. **FU-211 vẫn ghi `DEPLOYED_PENDING_LIVE_VERIFY` tới job 02:00.** Lượt 00:02 đã chứng minh chỗ
   ghi, nhưng job tự động mới là xác minh đầy đủ theo đúng lịch. Không tuyên bố "đã xác minh hết"
   khi chưa đối chiếu sau 02:00.

---

## 8. Gỡ về

**Code (local + VPS):**

```
cp backups/v10952_pre/_retrain_all.py web/backend/_retrain_all.py
cp backups/v10952_pre/_v10646_retrain_guard.py web/backend/_v10646_retrain_guard.py
cp backups/v10952_pre/lstm_model.py web/backend/lstm_model.py
cp backups/v10952_pre/scheduler.py web/backend/scheduler.py
# rồi deploy lại 4 file + restart service lottery
```

Gỡ về thì bảng lại ghi thiếu cột chất lượng và mã thoát lại luôn 0 — trở lại trạng thái "OK" giả.

**Model sau lượt chạy thật 00:02 (trên VPS):**

```
cp -a /root/Lottery_AI_Test/backups/v10952_models_pre/. /root/Lottery_AI_Test/data/models/
```

Không gỡ model trong phiên: job chủ nhật 02:00 cùng ngày chạy `--force` sẽ đè lại sau khoảng
2 tiếng dù có gỡ hay không. Owner đã dừng đặt tiền thật nên chất lượng model lúc này không kéo
theo mất tiền. Thời gian gỡ code ~ vài phút; gỡ model ~ dưới 1 phút.

---

## 9. Theo dõi tiếp

| mã | nội dung | ngưỡng hành động bằng số | hạn | ai quyết |
|---|---|---|---|---|
| **FU-211** | Xác minh chỗ ghi `auc/old_auc/test_loss/samples` trên lượt job tự động 02/08 02:00 | Phải thấy 12/12 dòng ngày 2026-08-02 · ≥9 dòng có `auc` khác NULL · cột `nguon` rõ `_retrain_all` hoặc `guard` | 02/08/2026 | agent đối chiếu, báo owner nếu trượt |
| **FU-212** | MT còn tín hiệu AUC ~0,55 nhưng không thành số trúng — đào khâu chuyển | Không tăng trọng số họ ML ở MT chỉ vì AUC; cổng lợi thế (QD-013) vẫn đóng. Đào: điểm ML có vào bộ số công bố không; AUC có thành lợi thế Top-K không | 08/08/2026 | owner duyệt hướng đào |
| **FU-213** | Phép so AUC cũ↔mới đang so hai cửa sổ khác nhau | **KHÔNG** bật lại cổng tự gỡ trước khi đo cả hai bản trên CÙNG bộ kiểm. Hướng: giữ bộ kiểm cố định (vd 60 ngày gần nhất tại thời điểm huấn luyện) | 15/08/2026 | owner duyệt trước khi bật cổng |
| **FU-210** (liên quan, từ V10947) | Tháng 6 mất lợi thế tiền thật ở MT | Không bật lại `combo-no-token` vào total dựa trên số gộp 180 ngày | đang mở | owner |

**Không có FU-214** trong phiên này — chỉ mở FU-211, FU-212, FU-213.

---

## Phụ lục V10953 — Xác minh đường chạy tự động 02:00 — ĐẠT

Kiểm lúc **02:18 ngày 02/08/2026** (giờ VN). Không sửa code, không deploy, không đo lại —
chỉ đối chiếu bảng và nhật ký sau khi job chủ nhật 02:00 chạy qua `scheduler.py`.

Lý do phải kiểm riêng: `scheduler.py` cũng bị sửa trong V10952 (thôi ghi đè 12 dòng 4 cột,
chỉ ghi bù FAILED cho dòng còn thiếu). Nhánh tự động chưa từng chạy thật lần nào trước đó.
Lượt 00:02 chỉ là chạy ép bằng tay (`--force`).

### Kết quả

| Mục | Kết quả |
|---|---|
| Số dòng ngày 2026-08-02 | 12/12 |
| Dòng có AUC | 12/12 — **0 dòng rỗng** |
| Trạng thái khác OK | 0 |
| Lỗi `I/O operation on closed file` quanh 02:00 | Không có |

### Điểm tinh tế về `old_auc`

Số dòng **không tăng** (vẫn 12) và `created_at` vẫn là 00:03–00:05. Thoạt nhìn tưởng job
02:00 không chạy. Nhưng bảng dùng ghi đè theo khoá `(date, region, model_type)` — đúng thiết
kế `_v10952_training_journal.py`. Bằng chứng đã chạy nằm ở cột `old_auc`: mỗi lượt ghi đúng
giá trị lượt trước.

```
MT random-forest:  0,5517 (đo 31/05)  →  0,5248 (lượt 00:02)  →  0,5299 (lượt 02:00)
MN meta-learning:  0,5092            →  0,5115              →  0,4892
```

### AUC lượt tự động 02:00 ngày 02/08

| miền | meta-learning | xgboost | random-forest | lstm |
|---|---|---|---|---|
| MT | 0,5394 | 0,5236 | 0,5299 | 0,5554 |
| MN | 0,4892 | 0,4993 | 0,5039 | 0,5137 |
| MB | 0,4768 | 0,4839 | 0,5017 | 0,5106 |

**Cả bốn model ở MT vẫn trên 0,5** sau một lượt huấn luyện hoàn toàn mới. MB ba trên bốn vẫn
dưới 0,5. Đây là lần xác nhận thứ ba, trên dữ liệu mới, cùng một hướng — củng cố kết luận rằng
tín hiệu ở MT còn thật và phần mất nằm ở khâu chuyển tín hiệu thành số công bố, không ở tầng
model.

**FU-211 → `CLOSED_PASS`** (V10953, 02/08 02:18).
