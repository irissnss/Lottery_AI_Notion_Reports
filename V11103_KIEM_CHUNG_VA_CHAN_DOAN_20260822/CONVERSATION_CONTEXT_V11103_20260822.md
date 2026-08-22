# CONVERSATION CONTEXT — V11103 · 22/08/2026 (sáng)

## Owner nói gì (NGUYÊN VĂN)

> *«V11102 đã deploy thước đo model + bộ chấm T-B (PID 2110106→2128063). Verdict còn thiếu
> `RUNTIME_PROVEN` vì lượt production đầu tiên của ngày 22/08 chưa chạy lúc đóng báo cáo. Phiên
> này là phiên KIỂM CHỨNG + CHẨN ĐOÁN — CẤM sửa production.»*

> *«`glm-5.1` … 2/7 lượt tuần này trả RỖNG ở MN (MB/MT gần như không). Đo trước: rỗng vì API lỗi,
> vì bộ lọc nội dung, vì prompt miền Nam, hay vì timeout? Phân tích payload/log của đúng 2 lượt
> rỗng. CẤM hạ `MIN_MAU_DU_TUYEN` cho hết đỏ.»*

> *«`FU-421` — chạy `/du-doan` nhiều lần cùng một ngày trên môi trường thử, xem bộ số cuối có đổi
> không (tiền lệ cách đo của `FU-416`). Chỉ trình — vá là phiên 24/08.»*

---

## Câu hỏi của owner có một tiền đề sai, và việc đo đã sửa nó

Owner viết: *«2/7 lượt tuần này trả RỖNG ở MN (**MB/MT gần như không**)»*.

Tiền đề đó **đến từ báo cáo của chính agent tối hôm trước**, không phải từ owner. Và nó **sai**.
Đo 60 ngày:

```
MN 2/59        MT 1/58        MB 1/60
```

Cả ba miền đều có. Câu *«chỉ ở MN»* dựng trên cửa sổ 30 ngày, nơi MB **tình cờ** bằng 0.

Sai lệch này không vô hại: nó dẫn thẳng tới giả thuyết *«tại prompt miền Nam»*, và owner đã đưa
đúng giả thuyết đó vào danh sách phải kiểm. Nếu không đo lại 60 ngày thì phiên 25/08 đã đi mổ
prompt MN — **một nguyên nhân không tồn tại**.

---

## Hai lượt rỗng, hai chuyện khác hẳn nhau — và cái thứ hai không có trong danh sách owner nêu

| ngày | độ trễ | chuyện gì |
|---|---:|---|
| 15/08 | **134.064 ms** | chờ **134 giây** rồi nhận thân rỗng |
| 18/08 | **9 ms** | **lượt gọi chưa bao giờ ra khỏi máy** |

**15/08 không phải lỗi riêng của `glm-5.1`.** Cùng ngày, cùng miền, `deepseek-reasoner` — **nhà
cung cấp khác hẳn** — hỏng y hệt. Hai model, hai provider, một ngày ⇒ sự kiện diện rộng, không
phải tính nết của model.

**18/08 — 9 mili-giây là con số tự tố cáo.** Không lượt gọi mạng nào tới OpenRouter xong trong 9
mili-giây. Truy ra **cầu dao ngắt mạch** (`gpt_analyzer.py:3560`): khi mở, nó trả về
`{"error": ..., "ok": False}` — **không có khoá `prediction`** — nên `numbers` rỗng.

Và đây là chỗ đáng nói nhất:

> Bảng chẩn đoán ghi **`EMPTY_PROVIDER_OUTPUT`** với câu *«provider response parsed but no
> prediction numbers were found»*.
>
> **Câu đó sai sự thật.** Provider chưa hề trả lời gì.

Nhãn sai kiểu này không chỉ là chuyện chữ nghĩa — nó **chỉ sai đường cho người điều tra**. Agent
này đã đi đúng vào đó: thấy *«response parsed»* thì đi tìm nguyên nhân ở prompt và ở bộ lọc nội
dung, mất một quãng trước khi nhận ra con số 9 ms mới là manh mối thật.

---

## Con số đảo ngược đề xuất

| model | 60 ngày | rỗng | tỉ lệ |
|---|---:|---:|---:|
| `glm-5.1` | 177 | 4 | **2,26%** |
| `deepseek-reasoner` | 180 | 4 | **2,22%** |

`glm-5.1` **ngang bằng** một model đã ở trong danh sách output từ lâu và **chưa ai kêu**.

Cảnh báo nổ cho `glm-5.1` **vì nó vừa vào danh sách hôm 21/08** — lần đầu tiên có một cái cổng soi
tới nó. Rút nó ra lúc này là **xử một model vì nó mới, không vì nó kém**, trong khi model cùng tỉ
lệ vẫn ngồi yên.

⇒ Đề xuất: **GIỮ**. Và làm hai việc khác thay vì cắt — vá nhãn sai, và **đếm số ngày bundle thiếu
người** (hôm nay **không ai đang đếm**).

---

## Hai lần agent suýt công bố kết luận sai trong phiên này

### ① Suýt tuyên bố trọng số win-rate «không làm gì cả»

Đọc `main.py:7839` thấy `model_rates = {}`, rồi thấy `:7857` dùng `.get('win_rate', 50)` — kết
luận: mọi model luôn có trọng số 50, tức phép cân theo tỉ lệ thắng **vô nghĩa**.

Đó sẽ là một cáo buộc rất nặng. Và **sai**: `:7839` chỉ là **khởi tạo**; `:7843` nạp thật từ
`combo_super._get_dynamic_win_rates`. Bắt được vì đi `grep` **toàn bộ** chỗ dùng `model_rates`
thay vì đọc một đoạn.

**Bài học đúng nguyên văn `RM-10`:** đọc một khúc rồi suy ra hành vi là cách nhanh nhất để nói sai.

### ② Suýt tuyên bố ba đường không chạy production

Journal **không có một dòng** *«Dynamic WR loaded»* nào từ 16/08 ⇒ phản xạ đầu là *«ba đường này
không chạy»*. **Sai** — `print()` trong worker của scheduler bị bọc chống stdout đóng, nên vắng log
**không** chứng minh vắng chạy (`RM-20`).

Bằng chứng đúng là **dấu vết dữ liệu**: `predictions` có dòng của `smart-ensemble`, `smart-ml`,
`combo-no-token` tới tận **22/08**.

---

## Phép đo FU-421 cho kết quả «không có gì» — và đó là kết quả tốt

Ba phép, 111 cặp ngày-miền:

- **A. thử đối chứng** — một `set` thật cho **3 thứ tự khác nhau** qua 3 seed ⇒ dụng cụ đo **có
  tác dụng**. Không có bước này thì kết quả «mọi seed giống nhau» ở phép B có thể chỉ là **dụng cụ
  hỏng**.
- **B.** thứ tự đổi theo seed: **0/111**.
- **C.** hoà với tỉ lệ thắng thật: **0/111**.

⇒ **KHÔNG CHỨNG.** Ba chỗ đó **không đổi số công bố**.

**Nhưng phép đo lộ ra thứ khác, và nó mới là thứ đáng mang đi vá:**

```python
except Exception:  model_rates = {}     # :7850 — KHÔNG KÊU MỘT TIẾNG NÀO
```

Nếu cả hai phép lấy tỉ lệ thắng hỏng, mọi model về trọng số 50 — và khi đó **96% số ngày** con số
hạng nhất của Smart Ensemble được quyết bởi **thứ tự viết trong danh sách nguồn**
(`meta-learning` luôn thắng `lstm`), chứ không bởi một luật nào.

> Thứ đang phá hoà hôm nay **không phải một luật**, mà là một **chênh lệch số học tình cờ** giữa
> các tỉ lệ thắng. Nó đúng — nhưng **không ai viết ra rằng nó phải đúng**, và không ai được báo
> khi nó thôi đúng.

Và bản thân `except: model_rates = {}` đúng là họ lỗi mà `V11101` vừa dựng cổng để chặn: **che
tiếng kêu rồi đọc số 0 thành sạch**.

---

## Điều KHÔNG kết luận được, ghi thẳng

**Không nâng `V11102` lên `RUNTIME_PROVEN`.** Ba điều kiện thì hai xanh, một **chưa tới lúc kiểm**:
job đo chạy **khi kết quả xổ về** (MN ~16:35), không phải lúc 05:00. Lúc đo là **09:31**, kết quả
chưa miền nào về, và log xác nhận job **chưa chạy lần nào hôm nay**.

`RM-12` cấm tự nâng tầng. Nâng lúc này là đổi một dòng đẹp trong sổ lấy một câu chưa có bằng chứng.

**Không có log gốc của lượt rỗng 15/08** — journal chỉ còn từ 16/08. Nguyên nhân dựng lại từ
`runtime_reliability_model_daily` và từ mã, **không đoán thêm**.
