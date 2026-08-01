# V10937 + V10938 — Soi lại bằng hai thước đo: lùi một quyết định, sửa một quyết định vội

**Ngày:** 01/08/2026 · **Trạng thái:** code xong, tự kiểm 7/7, **CHƯA DEPLOY**

---

## 1. Owner hỏi

> *"Ui thế gemini-3.5-flash có thực sự tốt không vậy trời? sao làm anh hoang mang quá rồi các
> model em cắt có rõ ràng không đó em?"* — 01/08 16:34

Owner hoang mang là đúng. Em đưa ra hai con số trái ngược mà chưa giải thích. Soi lại thì em sai
hai chỗ.

---

## 2. Hai thước đo KHÔNG mâu thuẫn — cửa sổ mới là thứ gây lệch

Trên **cùng cửa sổ 26 ngày** (mặt bằng: bạch thủ 30,77% · win rate 31,64%):

| | bạch thủ | win rate |
|---|---|---|
| `gemini-3.5-flash` | **38,16%** trên mặt bằng | 31,58% ngang mặt bằng |

Nó **không hề gần chót** như con số 7 ngày làm tưởng. Chênh lệch trước đó là do **cửa sổ**, không
phải do thước đo.

---

## 3. Nhưng nó đang tụt thật — và em đã bỏ sót

```
gemini-3.5-flash    W27 38,1%  →  W28 47,6%  →  W29 38,1%  →  W30 23,1%
gpt-oss-120b        W26 13,3%  →  W27 38,1%  →  W28 38,1%  →  W29 38,1%  →  W30 46,7%
```

Bốn tuần liên tiếp đi xuống. Trung bình 26 ngày che mất xu hướng — con số 38,16% là thật nhưng
phần lớn đến từ nửa đầu.

**Em gọi nó là "mạnh nhất hệ" là nói quá.** Đúng ra phải nói: từng mạnh, hiện đang tụt, và 76
lượt chưa đủ để chắc.

**Owner quyết:** hoãn đưa vào total, ở lại shadow ít nhất 1 tuần. Kéo theo `smart-ml` ở lại
total vì không còn ai cần suất.

---

## 4. Soi lại 5 model đã cắt — 4 đúng, 1 vội

| model | bạch thủ | win rate | kết luận |
|---|---|---|---|
| `gemma-4-31b` | 20,0% ↓ | 20,0% ↓ | cắt đúng |
| `smart-ml` | 23,08% ↓ | 29,49% ↓ | cắt đúng (nhưng hoãn cắt, xem mục 3) |
| `gpt-5-mini` | 25,64% ↓ | 29,49% ↓ | cắt đúng |
| `kimi-k2.5` | 28,57% ↓ | 31,43% ↓ | cắt đúng |
| **`gpt-5.4`** | 25,64% ↓ | **32,69% TRÊN mặt bằng** | **cắt vội** |

`gpt-5.4` còn đang đi lên: W26 13,3% → W29 33,3% → W30 26,7%.

V10931 sáng nay chấm bằng **một thước đo duy nhất** nên cắt nhầm.

**Owner quyết:** gọi `gpt-5.4` về official.

---

## 5. Vì sao `combo-no-token` nhường suất

| | bạch thủ | win rate |
|---|---|---|
| `combo-no-token` | 25,64% | 25,64% |
| mặt bằng | 30,77% | 31,64% |

Kém **cả hai** thước đo, và **thừa nhất trong 15 suất**: ghi chú của nó nói rõ *"ALL 4 ML models
+ Cross-Region"* — nó gộp cả bốn model ML mà cả bốn đã tự bỏ phiếu riêng trong total. Bỏ nó là
bớt lớp đếm trùng dày nhất, không mất nguồn tin mới nào.

Giữ `status='ACTIVE'` để nó vẫn chạy vẫn đo, chỉ tắt quyền góp phiếu.

---

## 6. V10938 — phát hiện lớn nhất phiên này

`win_rate` tính cả **PARTIAL** (trúng vài số trong dàn) là nửa điểm. Nên một model có thể "trúng
lai rai" mà **con số chốt vẫn trượt**:

| model | bạch thủ | win rate | lệch |
|---|---|---|---|
| `meta-learning` | 23,08% | 33,97% | −10,9 |
| `claude-opus-4-6` | 29,49% | 38,46% | −9,0 |
| `deepseek-reasoner` | 29,49% | 36,54% | −7,1 |

**Owner đánh bạch thủ.** Trong khi bộ lọc combo-super chọn theo `win_rate` — tức đang chọn model
giỏi "trúng lai rai" chứ không phải model giỏi "chốt đúng con số".

### Đo trước khi đổi — đổi lựa chọn ở cả ba miền

| miền | win rate chọn | bạch thủ chọn |
|---|---|---|
| MN | claude-sonnet, gpt-oss-120b | **gpt-oss-120b (74,9), gemini-2.5-flash (47,5)** |
| MT | gemini-2.5-flash, deepseek | **glm-5.1 (59,4), claude-sonnet (53,6)** |
| MB | claude-sonnet, claude-opus | **gemini-2.5-pro (30,2), deepseek (30,2)** |

Bạch thủ còn bắt được chênh lệch theo miền mà win rate làm mờ:

```
gpt-oss-120b    trúng 85,7% ở MN   nhưng   0% ở MB
glm-5.1         trúng  0%   ở MN   nhưng  66,7% ở MT
```

Số liệu bạch thủ dày y hệt số liệu win rate (7 ngày gần nhất: 181–187 dòng, 29 model, cả ba
miền) nên không lo thiếu dữ liệu.

**Chốt chặn:** đọc bảng bạch thủ lỗi thì tự lùi về win rate và ghi rõ trong log — không để bộ
lọc chết.

---

## 7. Tự kiểm — đạt 7/7

```
total đúng 15                              ✓
gpt-5.4 ĐÃ VÀO total                       ✓
gpt-5.4 vào chuỗi official                 ✓
combo-no-token ĐÃ RỜI total                ✓
combo-no-token VẪN CHẠY khung 04:00        ✓
gemini-3.5-flash HOÃN, còn ở shadow        ✓
smart-ml ở lại total                       ✓
```

---

## 8. Bài học ghi vào sổ (FU-206)

**Không được cắt hoặc đẩy model lên official bằng một thước đo trên cửa sổ ngắn.**

Hai lỗi trong ngày đều cùng một gốc:

- V10931 cắt `gpt-5.4` bằng một thước đo → phải gọi về sau nửa ngày
- V10934 định đẩy `gemini-3.5-flash` lên bằng trung bình 26 ngày mà không xem xu hướng → phải hoãn

Từ nay bắt buộc có đủ ba thứ: **bạch thủ**, **win rate**, và **bảng theo tuần** để thấy xu hướng.
Kém cả hai thước **và** không có dấu hiệu đi lên mới được cắt.

---

## 9. Việc theo dõi

| mã | nội dung | ngưỡng hành động | hạn |
|---|---|---|---|
| **FU-203** | `gemini-3.5-flash` có hồi không | tuần ≥ 30% → xét lại vào total · < 25% → gỡ khỏi pool | 08/08 |
| **FU-204** | `gpt-5.4` gọi về có đúng không | bạch thủ < 25% VÀ win rate < 30% sau 14 ngày → cắt hẳn | 15/08 |
| **FU-205** | Bộ lọc chấm bạch thủ có tốt hơn không | `combo-super` tốt lên ≥ 3pp → giữ · xấu đi ≥ 3pp → quay về win rate | 15/08 |
| **FU-206** | Quy tắc mới khi xét cắt model | bắt buộc hai thước đo + bảng theo tuần | liên tục |

---

## 10. ĐÃ DEPLOY lúc 17:45 — sau khi nghiệm thu đêm đầu

### Nghiệm thu đêm 01/08 (FU-194) — SẠCH

| miền | chốt | hạn | dư | model | bạch thủ |
|---|---|---|---|---|---|
| MN | 05:20 | 15:45 | 625 phút | 13 | 16 |
| MT | 16:46 | 16:58 | **12 phút** | 13 | 55 |
| MB | 17:39 | 17:58 | **19 phút** | **15** | 90 |

**0 lỗi** cả ngày. `glm-5.1` và `gpt-oss-120b` đều góp mặt trong chuỗi MT và MB, không quá giờ.
Chậm nhất toàn hệ là `gpt-5.5` 643 giây nhưng đó là model shadow, không chạm hạn official.

Đây là đêm đầu tiên hai model chậm chạy official với hạn mới — lo ngại chính đã được gỡ, nên
bấm nút được.

### Kết quả deploy

```
md5 hai file                    khớp
PID dịch vụ                     561685 → 575903   (đổi thật)
/api/health                     200
tự kiểm sau deploy              10/10 ĐẠT
băm 4 bảng trước/sau            Y NGUYÊN
tự kiểm 16 mục trên VPS         lệch 0
```

Bộ lọc sau deploy chọn đúng như đã đo trước khi sửa:

```
MN: ['gpt-oss-120b', 'gemini-2.5-flash']
MT: ['glm-5.1', 'claude-sonnet-4-6']
MB: ['gemini-2.5-pro', 'deepseek-reasoner']
```

Hoàn tác: `python web/backend/_v10934_deploy.py --rollback` (~1 phút).

---

## 11. Tổng kết cả phiên 01/08

| version | nội dung | trạng thái |
|---|---|---|
| V10933 | cứu `gemini-3.5-flash` — khai vào đường thoát 503 | ĐÃ DEPLOY |
| V10933b | chạy thử trọn đường có nhóm đối chứng | ĐÃ DEPLOY |
| V10934 | định đổi total — **bị thay bởi V10937** | HUỶ |
| V10936 | bộ lọc: bỏ điểm ảo 50%, mở pool 7→9 | ĐÃ DEPLOY |
| V10937 | hoãn `gemini-3.5-flash`, gọi `gpt-5.4` về thay `combo-no-token` | ĐÃ DEPLOY |
| V10938 | bộ lọc chấm bạch thủ thay win rate | ĐÃ DEPLOY |
