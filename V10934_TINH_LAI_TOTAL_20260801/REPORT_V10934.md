# V10934 — Tính lại total sau khi cứu `gemini-3.5-flash`

**Ngày:** 01/08/2026 · **Trạng thái:** code xong, tự kiểm đạt, **CỐ Ý CHƯA DEPLOY**
**Chạm luồng chính thức:** CÓ (đổi 1 trong 15 suất) — nên mới phải cẩn thận về thời điểm

---

## 1. Owner yêu cầu gì

> *"Vậy cứu được rồi thì phải làm lại rồi em? chạy test thử vài đoạn ngắn, kiểm chứng hoạt động,
> sau đó lên kế hoạch total, filter combo super v.v... lại theo ah em. Còn gemini 3.6 vẫn giữ
> nha em."* — 01/08 14:33

---

## 2. Bắn thử thật — 72 lệnh

| model | đậu | thời gian |
|---|---|---|
| `gemini-3.5-flash` | **36/36** | 4,3 – 6,2 giây |
| `gemini-3.6-flash` | **36/36** | 4,5 – 9,9 giây |

Dùng lại đúng cách đo đã hiệu nghiệm hôm 31/07: bắn dồn 12 lệnh song song, 3 vòng.

**Giới hạn phải nói rõ:** không ép được lỗi 503 nào, vì lúc bắn là 14h40 và Google đang rộng
chỗ. Lịch sử cho thấy 3/4 lần rớt rơi vào khung sáng sớm khi cả dàn model bắn cùng lúc. Nên lối
thoát 503 hiện mới chỉ chứng minh được bằng lỗi giả (V10933b) — muốn thấy nó nổ thật phải đợi
giờ cao điểm. Theo dõi ở FU-197.

---

## 3. Xếp hạng lại — và một sự thật khó chịu

Cửa sổ 06/07–31/07, 2.057 lượt. So mỗi model với **mặt bằng cùng ngày cùng miền**, vì ngày nào
cả làng cùng trúng thì trúng không có gì giỏi.

### Chỉ 1 trong 27 model chắc chắn hơn mặt bằng

`smart-ensemble` (+11,47pp, mép dưới khoảng tin cậy +1,33pp). Tất cả các model còn lại đều có
khoảng tin cậy vắt qua số 0 — nghĩa là **chưa phân biệt được với may rủi**.

Điều này phải nói trước mọi đề xuất: các quyết định dưới đây là đặt cược có cân nhắc, không phải
chân lý.

### Bảng đầu

| hạng | model | hơn mặt bằng | mép dưới | đang ở đâu |
|---|---|---|---|---|
| 1 | `smart-ensemble` | +11,47pp | **+1,33pp** | official |
| 2 | `gemini-2.5-flash` | +8,91pp | −0,62pp | official |
| 3 | `gpt-oss-120b` | +8,91pp | −1,18pp | official (lên 01/08) |
| **4** | **`gemini-3.5-flash`** | **+6,73pp** | −1,79pp | shadow |
| 5 | `glm-5.1` | +5,78pp | −2,53pp | official (lên 01/08) |

`gemini-3.5-flash` đứng **trên** `glm-5.1` — model vừa được duyệt lên official hôm qua. Cùng một
thước đo, không nới tay cho nó.

---

## 4. Tìm ra một chùm thừa

Trong 15 suất official có **3 suất thuộc họ nhà XGBoost + RandomForest, và cả ba đều dưới mặt
bằng**:

| model | thực chất là gì | hơn mặt bằng |
|---|---|---|
| `xgboost` | model gốc | −2,63pp |
| `random-forest` | model gốc | −5,19pp |
| `smart-ml` | **chính là hai model trên gộp lại** | −7,76pp |

Họ này bỏ phiếu **ba lần** cho cùng một lối nghĩ, cả ba lần đều kém.

Đối chiếu cho thấy gộp không phải lúc nào cũng dở: họ LSTM+Meta cũng chiếm ba suất, nhưng cỗ gộp
của nó (`smart-ensemble`) lại là quán quân +11,47pp. Cùng kiểu gộp mà một bên ra vàng một bên ra
than.

---

## 5. Chỗ owner cảnh báo hai lần — nay có bằng chứng

> *"đối với combo-super thì cần nghiên cứu kỹ đó nha vì nó là tổ hợp nhiều model AI và no token
> trong đó, em cắt model no token + model AI trong total thì nó cũng bị ảnh hưởng đó nha."*

Kiểm tận nơi: **`combo_super.py` hoàn toàn không đọc `OUTPUT_ELIGIBLE_MODELS`.** Nó chỉ mượn đúng
một hàm lấy tên hiển thị từ registry. Hai danh sách độc lập nhau.

Nghĩa là **cắt một model khỏi total KHÔNG làm combo-super mất nguồn** — nó vẫn hỏi đủ 7 model AI
và 4 model ML của riêng nó. Ngoài ra chỉ có `_test_dynamic_filter.py` đọc pool combo-super, mà đó
là file thử chứ không phải code chạy thật.

---

## 6. Owner duyệt

| | |
|---|---|
| VÀO total | `gemini-3.5-flash` |
| RA total | `smart-ml` → **vẫn chạy vẫn đo**, chỉ mất quyền góp phiếu |
| combo-super | **KHÔNG đụng** lần này |
| `gemini-3.6-flash` | giữ chạy shadow (owner dặn) |

Lý do chưa đụng combo-super: đổi hai thứ cùng lúc thì không biết cái nào gây ra kết quả. Đã xác
minh combo-super độc lập với total nên hoãn được an toàn. Giai đoạn 2 theo dõi ở FU-200.

---

## 7. Một chỗ suýt hỏng

Ban đầu định hạ `smart-ml` xuống `SHADOW_AUTO` cho gọn. Kiểm lại thì thấy:

```python
if slot in ('completion_triggered_shadow', 'shadow_eval_post_verify'):
    models = _filter_models(status='SHADOW_AUTO', slot=slot, region=region)
else:
    models = _filter_models(status='ACTIVE', slot=slot, region=region)
```

`smart-ml` chạy ở khung `04:00_all_regions` — không phải khung shadow. Hạ nó xuống `SHADOW_AUTO`
thì bộ lọc `status='ACTIVE'` sẽ **loại nó hẳn, nó ngừng chạy luôn**, mất sạch số liệu đối chứng —
trái hẳn ý owner "vẫn chạy vẫn đo".

Cách đúng: giữ `status='ACTIVE'`, chỉ tắt `output_eligible`. Nó chạy tại chỗ không tốn token nên
giữ chạy không tốn thêm đồng nào.

---

## 8. Tự kiểm

```
official                                    15   ✓ đúng 15
smart-ml VẪN CHẠY khung 04:00 (để còn đo)   ✓
smart-ml ĐÃ RỜI total                       ✓
gemini-3.5-flash VÀO chuỗi official MT/MB   ✓
gemini-3.5-flash ĐÃ VÀO total               ✓

shadow      12 → 11
UI-visible  30 (không đổi)
chuỗi AI official  8 → 9 model
```

---

## 9. Vì sao CHƯA DEPLOY

Tối nay là **đêm đầu tiên** `glm-5.1` (tối đa 796 giây) và `gpt-oss-120b` (tối đa 886 giây) chạy
official với hạn mới. Đo lịch sử 24–31/07:

| miền | bundle lập lúc | hạn | dư ít nhất |
|---|---|---|---|
| MT | 16:37 – 16:46 | 16:58 | **12 phút** |
| MB | 17:33 – 17:35 | 17:58 | **23 phút** |

Ngưỡng tự đặt trước khi xem số là "dư ≥ 6 phút thì làm ngay" — cả hai đều qua. **Nhưng** số này
đo **trước khi** hai model chậm vào chuỗi, nên 12 phút kia có thể co lại mà chưa ai biết bao
nhiêu.

Thêm model thứ 9 vào đúng đêm đó thì nếu trễ hạn sẽ không biết tại ai. Owner chọn đợi.

**Kế hoạch bấm nút:** sau khi MB chốt xong 17:58 tối nay (~18:10). Lúc đó đêm nay đã đọc sạch, mà
sáng mai MN tự chạy pool mới.

Script deploy **tự từ chối chạy nếu MB chưa chốt** — đã thử, nó từ chối đúng:

```
MB hôm nay: CHUA_CHOT
✗ MB chưa chốt bundle — DỪNG. Đợi qua 17:58 rồi chạy lại.
```

---

## 10. Việc theo dõi

| mã | nội dung | ngưỡng hành động | hạn |
|---|---|---|---|
| **FU-199** | Bấm nút V10934 sau khi MB chốt | — | tối 01/08 |
| **FU-200** | Đo kết quả rồi mới tính combo-super | bundle tốt lên ≥ 2pp → xét thêm vào pool combo-super · xấu đi → trả `smart-ml` về total | 09/08 |
| **FU-197** | Lối thoát 503 có dập được lỗi thật không | hỏng < 1,5% → giữ · > 4% → gỡ | 15/08 |
| **FU-198** | Giữ `3.5` hay `3.6` hay cả hai | chênh < 2pp → giữ bản rẻ · ≥ 2pp → giữ bản mạnh | 01/09 |

Hoàn tác: `python web/backend/_v10934_deploy.py --rollback` (~1 phút).
