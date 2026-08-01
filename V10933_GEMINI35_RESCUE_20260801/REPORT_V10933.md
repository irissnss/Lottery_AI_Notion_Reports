# V10933 — Gọi về `gemini-3.5-flash`: lỗi đã có sẵn cách chữa mà quên dùng

**Ngày:** 01/08/2026 · **Loại:** sửa lỗi định tuyến + khôi phục model shadow
**Chạm luồng chính thức:** KHÔNG (output-eligible vẫn đúng 15)

---

## 1. Owner hỏi gì

> *"gemini-3.5-flash ==> thử lại xem có phương pháp vào vượt qua lỗi này không em?"* — 01/08 14:09

Bối cảnh: hôm trước owner đã tiếc model này —

> *"Chỉ có gemini 3.5 flash là anh đang tiếc nhất chạy ổn nhưng tự nhiên lỗi làm mất một model
> tốt tham gia total."*

---

## 2. Trả lời ngắn

**Có** — và đáng tiếc là cách chữa đã nằm sẵn trong hệ **từ hôm trước**, chỉ là khai thiếu đúng
cái model đang gặp nạn.

Ngày 31/07 (V10888) đã dựng đường thoát: gặp 503 hết chỗ chứa thì nhảy thẳng sang OpenRouter.
Nhưng danh sách chỉ khai bản kế nhiệm:

```python
GOOGLE_OPENROUTER_FALLBACK = {
    'gemini-3.6-flash': 'google/gemini-3.6-flash',   # ← chỉ có bản thay thế
}
```

Chỗ tiêu thụ tra đúng một danh sách đó, nên bản 3.5 rơi thẳng xuống nhánh báo lỗi:

```python
_capacity_err = any(kw in err_str for kw in ['503', 'unavailable', 'overloaded'])
_fallback_slug = GOOGLE_OPENROUTER_FALLBACK.get(model)   # 3.5 → None
if _capacity_err and _fallback_slug:                      # → không vào được
```

Nói cách khác: **dựng đường thoát hiểm cho người thay ca, rồi cho người gặp nạn nghỉ việc.**

---

## 3. Lỗi thật là gì — không phải lỗi chất lượng

Toàn bộ 76 lượt gọi trong 30 ngày:

| loại | số lần | ghi chú |
|---|---|---|
| SUCCESS | 71 | |
| ERROR — `503 UNAVAILABLE` | 4 | hết **chỗ chứa** phía Google, không phải hết quota |
| TIMEOUT 300s | 1 | 15/07 |

Bốn lần rớt: 24/07 MN · 28/07 MN · 30/07 MN · 30/07 MB.

So với bạn cùng nhà Google:

| model | lượt | lỗi | tỉ lệ | TB giây |
|---|---|---|---|---|
| `gemini-3.5-flash` | 76 | 5 | **6,58%** | 64,9 |
| `gemini-3-flash` | 192 | 3 | 1,56% | 61,0 |
| `gemini-3.1-pro` | 192 | 2 | 1,04% | 48,5 |

Model càng mới, Google cấp càng ít chỗ chứa. Đây là **503 sức chứa**, khác hẳn 429 hết quota —
nên không liên quan tới hạng khoá, và vòng thử lại 4 lần / 50 giây sẵn có không cứu được.

---

## 4. Đã gọi thử THẬT trước khi khai

Đúng lệ tự đặt ra ở V10888: *"CHỈ ghi slug đã gọi thử thật và thấy chạy"*.

| phép thử | kết quả |
|---|---|
| `google/gemini-3.5-flash` — 6 lệnh liên tiếp | **6/6 đậu**, 1,8–3,8 giây |
| qua đúng `_call_openrouter` của hệ | ✓ 4,6 giây, JSON hợp lệ: `bach_thu "38"`, `song_thu ["27","72"]` |
| `google/gemini-3.5-flash-preview` | **400 Bad Request** → không dùng hậu tố `-preview` |

### Bẫy suýt mắc

Lần thử đầu đặt hạn 20 token, `content` trả về **rỗng** — nhìn qua tưởng model hỏng. Thật ra
Gemini 3.x có bước suy nghĩ nội bộ, nó ăn hết 17/20 token nên không còn chỗ cho câu trả lời.
Nâng hạn lên 2000 token thì ra JSON đầy đủ kèm lý giải tiếng Việt. Nếu dừng ở phép thử đầu thì
đã kết luận sai là "slug sống nhưng không dùng được".

---

## 5. Vì sao đáng gọi về

`gemini-3.5-flash` là model **mạnh nhất nhà Gemini**:

| model | lượt | trúng bạch thủ | tỉ lệ |
|---|---|---|---|
| **`gemini-3.5-flash`** | 76 | 29 | **38,16%** |
| `gemini-3.1-pro` | 179 | 61 | 34,08% |
| `gemini-3-flash` | 180 | 51 | 28,33% |

Nó bị cho nghỉ vì **độ ổn định**, không phải vì chất lượng — mà độ ổn định thì hệ đã có sẵn cách
chữa từ hôm trước.

---

## 6. Sửa gì

| file | sửa |
|---|---|
| `web/backend/gpt_analyzer.py` | khai `'gemini-3.5-flash': 'google/gemini-3.5-flash'` vào `GOOGLE_OPENROUTER_FALLBACK` |
| `web/backend/model_registry.py` | `RETIRED` → `SHADOW_AUTO`, bỏ `retired_date` |
| `web/backend/model_registry.py` | sửa hai con số tự kiểm **đã cũ từ trước phiên này** (ghi 10/30, thực tế 11/29) |

Cơ chế dựng danh sách shadow là `get_model_ids(status='SHADOW_AUTO')` — lật trạng thái là nó tự
chạy lại, không phải sửa chỗ nào khác.

### Đếm lại pool

| | trước | sau |
|---|---|---|
| output-eligible | 15 | **15** — luồng chính thức KHÔNG đụng |
| shadow auto-eval | 11 | 12 |
| UI-visible | 29 | 30 |

---

## 7. Xác minh sau deploy

```
md5 hai file                 khớp
PID dịch vụ                  558029 → 561685   (đổi thật, không phải báo OK suông)
/api/health                  200
tiến trình đang chạy đọc:
    duong_thoat              ['gemini-3.5-flash', 'gemini-3.6-flash']
    shadow                   12
    official                 15
    3.5 chạy hôm nay         True
băm 4 bảng trước/sau         Y NGUYÊN
```

Băm 4 bảng: `predictions d455c7c8d8e34332` · `final_bundles cb08373a3b17e00c` ·
`lottery_results 5e6e383f1e6f55ff` · `model_daily_eval 0e3d2ebb8444905c` — giống hệt trước/sau.

---

## 7b. Chạy thử TRỌN ĐƯỜNG bằng lỗi 503 giả — có nhóm đối chứng

Mục 4 mới chứng minh được hai nửa **rời nhau**: điều kiện kích hoạt tra ra đúng slug, và lệnh
gọi OpenRouter trả về số. Chỗ **nối** giữa hai nửa thì chưa. Không thể ngồi đợi Google rớt 503
thật để xem, nên dựng lỗi giả: chặn lời gọi Google trong **một tiến trình thử riêng**, ném đúng
chuỗi lỗi 503 mà Google hay trả, rồi xem hàm có tự chuyển hướng không. Không sửa file, không
đụng dịch vụ đang chạy.

Chạy hai model để có đối chứng:

| model | có khai đường thoát? | kết quả khi gặp 503 |
|---|---|---|
| `gemini-3.5-flash` | **có** | ✓ **cứu được** — 4,6s, ra số `bach_thu "38"`, đóng dấu `served_by = openrouter:google/gemini-3.5-flash` |
| `gemini-3.1-pro` | không (đối chứng) | ✗ chờ lại 50 giây rồi vẫn trả lỗi — đúng hành vi cũ |

Hệ in ra đúng chuỗi mong đợi:

```
[API] ↪ Gemini gemini-3.5-flash: 503 hết chỗ chứa — chuyển sang OpenRouter google/gemini-3.5-flash ngay
[API] OpenRouter response: 360 chars, tokens: 644, finish: stop
[API] ✅ OpenRouter cứu được gemini-3.5-flash
```

Nhóm đối chứng là phần quan trọng nhất của phép thử này: nó chứng minh kết quả tốt đến **từ việc
khai vào danh sách**, chứ không phải do môi trường thử dễ dãi.

---

## 8. Chạy song song, chưa vội chọn

Giữ **cả hai** `3.5-flash` và `3.6-flash` chạy shadow để so găng. Lý do: 31/07 thay 3.5 bằng 3.6
dựa trên **độ ổn định** chứ không dựa trên chất lượng — lúc đó 3.6 mới có 1 lượt, chưa đủ căn cứ
để thay một model 76 lượt. Cả hai đều hạng flash rẻ, và đều là shadow nên không chạm output.

**Ngày 01/08 là ngày lẻ:** bật lúc 14h nên 3.5 chỉ kịp MT+MB, thiếu MN. Khi so găng phải bỏ ngày
này, hoặc ghép theo cặp `ngày + miền` chứ đừng gộp thô.

---

## 9. Việc cần theo dõi

| mã | nội dung | ngưỡng hành động | hạn |
|---|---|---|---|
| **FU-197** | Đường thoát có thật sự dập được 5,3% lỗi không | hỏng < 1,5% → xét lên official · vẫn > 4% → gỡ hẳn | 15/08 |
| **FU-198** | Giữ 3.5 hay 3.6 hay cả hai | chênh < 2pp → giữ bản rẻ · >= 2pp → giữ bản mạnh | 01/09 |

Cách kiểm FU-197: journal phải có dòng
`[API] ↪ Gemini gemini-3.5-flash: 503 hết chỗ chứa — chuyển sang OpenRouter` **và** lượt đó vẫn
ra số.

Hoàn tác: lật `status` về `RETIRED` trong `model_registry.py`, khoảng 1 phút, không cần đụng gì
khác.

---

## 10. Bài học ghi vào sổ

**Khi dựng đường thoát cho một lỗi, phải khai chính model đang gặp lỗi đó — không chỉ khai model
thay thế.** Hôm 31/07 vừa dựng cơ chế vừa quyết định thay model trong cùng một phiên, nên cơ chế
mới chỉ phục vụ quyết định mới mà bỏ sót nguyên nhân ban đầu. Kết quả: mất một ngày của model
mạnh nhất hệ vì một lỗi đã có thuốc.
