# V10947 — Luồng nào để chơi? Không luồng nào. Nhưng tìm ra thứ quan trọng hơn

**Ngày:** 01/08/2026 · **Loại:** đo toàn bộ luồng và model · **Trạng thái:** đã ghi hồ sơ

---

## 1. Owner hỏi

> *"Xong rồi đúng không giờ làm gì tiếp theo? luồng nào cần tham khảo để chơi?"* — 01/08 22:12

---

## 2. Đo tất cả bằng cùng một thước

**29 model × 3 miền = 87 tổ hợp**, cửa sổ 180 ngày. Thước đo: với mỗi ngày, thử cả 100 số từ 00
đến 99 trên chính kết quả hôm đó để biết đánh bừa được bao nhiêu.

### Luồng chính thức

| miền | hệ | đánh bừa | chênh |
|---|---|---|---|
| MN | 16,60% | 16,55% | **+0,05pp** |
| MT | 16,71% | 16,50% | **+0,21pp** |
| MB | 21,94% | 23,74% | −1,81pp |

Đúng bằng ngẫu nhiên.

### Từng model đơn lẻ

Không ai vượt ngưỡng ý nghĩa theo hướng tốt. Cao nhất `gemini-2.5-pro` +1,80pp (z 1,49) — chưa
đủ. Hai model kém **có ý nghĩa**: `qwen3-coder` (−3,31pp) và `kimi-k2.5` (−3,32pp).

---

## 3. Nhưng có một chỗ vượt ngưỡng

```
combo-no-token · MT · 21,56% so với bừa 16,49% · +5,07pp · z = 2,81
```

Trên cả mức hoà vốn 18,37%. Và **cả họ no-token ở MT đều dương**:

| model | lợi thế ở MT | z |
|---|---|---|
| `combo-no-token` | +5,07pp | 2,81 |
| `random-forest` | +3,89pp | 2,14 |
| `smart-ml` | +3,65pp | 2,01 |
| `xgboost` | +3,41pp | 1,88 |
| `smart-ensemble` | +3,04pp | 1,68 |
| `combo-super` | +2,94pp | 1,65 |

Cả họ cùng dương thì khó là ngẫu nhiên thuần. Nhưng chúng đều dựng từ cùng bộ model ML, nên đây
là **một** tín hiệu chứ không phải sáu.

**Cảnh báo tự đặt:** đã thử 87 tổ hợp. Ở mức 5% thì trung bình sẽ vớ được ~4 cái đẹp do may.
Sửa theo Bonferroni thì ngưỡng thành z ≈ 3,25 — z = 2,81 **không vượt qua**.

---

## 4. Phép thử quyết định: chia đôi thời gian

Nếu lợi thế là thật thì phải xuất hiện ở **cả hai nửa**.

| phần | kỳ | hệ | bừa | lợi thế | z |
|---|---|---|---|---|---|
| toàn bộ | 174 | 21,56% | 16,49% | +5,07pp | 2,81 |
| **nửa đầu** (08/02 – 06/05) | 87 | **26,07%** | 16,50% | **+9,57pp** | **3,74** |
| **nửa sau** (06/05 – 01/08) | 87 | 17,06% | 16,48% | **+0,58pp** | **0,23** |

Theo tháng còn rõ hơn:

```
02/2026   +18,92pp   z  3,65
03/2026    +4,64pp   z  1,08
04/2026    +6,92pp   z  1,60
05/2026    +8,11pp   z  1,86
06/2026    −1,14pp   z −0,26     ← tắt
07/2026    −1,83pp   z −0,43
```

**Lợi thế là THẬT ở nửa đầu (z 3,74 — rất mạnh), và TẮT HẲN từ tháng 6.**

---

## 5. Đây mới là phát hiện quan trọng nhất

Trước đó bức tranh là *"hệ chưa bao giờ hơn ngẫu nhiên"*. Không chính xác. Đúng hơn:

> Hệ **từng có lợi thế thật** ở MT từ tháng 2 tới tháng 5, rồi **mất từ tháng 6**.

Khác biệt này rất lớn:

- *"Chưa bao giờ được"* nghĩa là bài toán bất khả, chỉ còn nước bỏ.
- *"Từng được rồi mất"* nghĩa là **có cái gì đó đã thay đổi**, và tìm ra nó là một việc **cụ thể,
  có giới hạn** — khác hẳn việc mò mẫm tỉa model.

Nó cũng giải thích một con số khó hiểu trước đó: cửa sổ 30 ngày cho MT chỉ **10,53%**, tệ bất
thường. Không phải hệ dở sẵn — mà là hệ đã mất thứ nó từng có.

---

## 6. Một chỗ script viết sai, đã sửa

Script chia đôi ban đầu chỉ xét `loi_the > 0` nên in ra *"CÓ ở cả hai nửa — đáng tin hơn"*. Sai:
+0,58pp với z 0,23 thực chất là không có gì. Đã sửa để đòi **cả hai nửa có z đủ lớn** mới gọi là
lặp lại được.

---

## 7. Trả lời thẳng câu hỏi

**Không luồng nào đáng tham khảo để chơi bằng tiền thật lúc này.**

Cổng lợi thế (V10945) đóng cả ba miền. Phần duy nhất từng có lợi thế đã tắt hai tháng nay.

---

## 8. Việc tiếp theo

| mã | nội dung | hạn |
|---|---|---|
| **FU-210** | Tháng 6 đã xảy ra chuyện gì làm mất lợi thế ở MT | 08/08 |

Hướng đào: có thay đổi code/cấu hình nào quanh tháng 5–6 chạm vào họ ML hoặc lane MT không · lịch
retrain ML có đổi không · kết quả MT có đổi đặc tính không · hệ có chuyển từ dùng số ML sang số
AI ở MT không.

**Không được làm:** bật lại `combo-no-token` vào total dựa trên con số gộp 180 ngày. Con số đó do
nửa đầu kéo lên; nửa sau không có gì.

FU-210 là **ngoại lệ hợp lệ** của FU-209 (dừng tỉa tót model), vì tiềm năng ≥5pp — đủ lớn để đo
được trong thời gian hợp lý.
