# V10936 — Sửa bộ lọc combo-super: bỏ điểm ảo 50%, mở pool

**Ngày:** 01/08/2026 · **Trạng thái:** code xong, thử trên dữ liệu sống, **CHƯA DEPLOY**
**Chạm đầu ra:** CÓ (MT và MB đổi người trong top-2)

---

## 1. Owner chỉ ra chỗ em hiểu sai

> *"Cơ chế Combo super anh nói rõ rồi mà, các model được filter auto lấy top nhét vô mà em, còn
> không top thì vẫn chạy bình thường để đo lường và xếp hạng thường xuyên chứ em?"* — 01/08 15:53

Owner đúng. Em coi pool combo-super như một danh sách phải sửa tay nên né không dám đụng, trong
khi thực tế:

```python
def get_dynamic_ai_filter(region: str, top_n: int = 2, days: int = 7) -> list:
    all_ai = [m['id'] for m in AI_MODELS]
    wr_data = get_model_win_rates(target_region=region, days=days)
    ai_wr = [(m, wr_data[m]['win_rate'] if m in wr_data else 50.0) for m in all_ai]
    ai_wr.sort(key=lambda x: x[1], reverse=True)
    selected = [m for m, _ in ai_wr[:top_n]]
```

Pool chỉ là **danh sách ứng viên**. Bộ lọc tự chấm win rate 7 ngày rồi lấy top-2. Model không
được chọn vẫn chạy dự đoán riêng của nó ở chuỗi chính nên vẫn được đo và xếp hạng đều.

---

## 2. Nhưng có một lỗi thật khiến không dám mở pool

Nhìn kỹ dòng thứ ba: **model chưa có số liệu bị gán mặc định 50%.**

Đo trên dữ liệu sống ngày 01/08:

| miền | model thật cao điểm nhất | hệ quả của điểm ảo 50% |
|---|---|---|
| MN | 50,0% | hoà |
| MT | 57,1% | an toàn |
| **MB** | **35,7%** | **mọi model chưa chạy đều tự động đứng #1** |

Thử thả `gemini-3.6-flash` (mới chạy đúng 1 lần, **0 lượt** trong cửa sổ 7 ngày) vào pool:

```
MB:  ['gemini-3.6-flash', 'claude-sonnet-4-6']     ← cướp suất #1 bằng điểm ảo
```

Nó đá `claude-opus-4-6` ra ngoài. **Model chưa từng làm gì thắng mọi model đã làm việc.**

Đây đúng là điều cổng V17.13 P0.5 đã cảnh báo từ lâu, và là lý do thật khiến pool bị khoá tay —
không phải vì ai đó cẩn thận quá.

---

## 3. Cách sửa owner chọn

1. **Chưa đủ 5 lượt thật** trong cửa sổ 7 ngày thì **không được dự tuyển**. Vẫn chạy vẫn đo ở
   chuỗi chính, chỉ không được vào đua chọn top.
2. **Điểm chấm trộn hai cửa sổ:** `(2 × WR 7 ngày + 1 × WR 30 ngày) / 3`. Đây đúng là công thức
   hệ đã có sẵn ở `_get_dynamic_win_rates`, chỉ là bộ lọc chưa dùng tới. Cửa sổ 7 ngày chỉ có
   6–7 lượt, quá ít để tin.

Sửa ở **cả ba chỗ**: `get_dynamic_ai_filter`, `get_dynamic_ml_filter`, và
`compute_adaptive_top_n` — hàm cuối cũng dùng mặc định 50%, mà điểm ảo còn làm méo cả độ chênh
lệch nên đổi luôn cả `top_n`.

**Chốt chặn an toàn:** lọc xong còn ít hơn 2 ứng viên thì bù từ nhóm chưa đủ mẫu (xếp cuối) —
không bao giờ để tổ hợp rỗng.

---

## 4. Thử trên dữ liệu sống TRƯỚC khi deploy

Nạp bản sửa từ thư mục tạm trên VPS, các module khác vẫn lấy từ thư mục thật. Không đụng dịch vụ
đang chạy.

### Phép thử quan trọng nhất — đã chặn được

```
MB · thả gemini-3.6-flash (0 lượt) vào pool:
    cũ    ['gemini-3.6-flash', 'claude-sonnet-4-6']
    mới   ['claude-sonnet-4-6', 'gemini-2.5-pro']      ✓
```

### Hai chỗ đổi kèm — đều giải thích được

| miền | cũ | mới | vì sao đổi |
|---|---|---|---|
| MN | claude-sonnet, gpt-oss-120b | **giữ nguyên** | — |
| MT | gemini-2.5-flash, deepseek | deepseek, gemini-2.5-flash | hoà **57,1%** ở 7 ngày; cửa sổ 30 ngày phá hoà (41,7% so với 28,3%) |
| MB | claude-sonnet, **claude-opus-4-6** | claude-sonnet, **gemini-2.5-pro** | hoà **28,6%**; 30 ngày 31,7% so với 28,3% |

Cả hai đều là **phá thế hoà bằng số liệu dài hạn**, không phải đổi bừa. Bộ lọc ML chỉ đổi thứ tự
ở MT, không đổi người.

Điểm sau khi trộn hai cửa sổ (bản mới in ra):

```
[DYNAMIC AI] MN top-2: GIỮ [('claude-sonnet-4-6', 51.1, '7 lượt'), ('gpt-oss-120b', 48.3, '7 lượt')]
[DYNAMIC AI] MT top-2: GIỮ [('deepseek-reasoner', 52.0, '7 lượt'), ('gemini-2.5-flash', 47.5, '7 lượt')]
[DYNAMIC AI] MB top-2: GIỮ [('claude-sonnet-4-6', 36.0, '7 lượt'), ('gemini-2.5-pro', 29.6, '7 lượt')]
```

---

## 5. Mở pool: 7 → 9 model

Thả `gemini-3.5-flash` và `gemini-3.6-flash` vào pool AI.

**Đã chứng minh không đổi lựa chọn ở cả ba miền** — bộ lọc tự chấm rồi tự nói "chưa tới lượt".
Đúng cơ chế owner mô tả: cứ thả vào, ai xứng đáng thì được dùng.

Thêm model vào pool **không tốn thêm lệnh gọi API**, vì chỉ top-2 mới được gọi.

---

## 6. Vì sao chưa deploy

Bản sửa này đổi đầu ra thật (MT và MB đổi người trong top-2), nên cùng lý do với V10934: tối nay
là đêm đầu tiên `glm-5.1` (tối đa 796 giây) chạy official với hạn mới 16:58/17:58. Đổi nhiều thứ
cùng một đêm thì hỏng không biết tại ai.

Bấm nút sau khi MB chốt xong 17:58, đi chung chuyến với V10934.

---

## 7. Việc theo dõi

| mã | nội dung | ngưỡng hành động | hạn |
|---|---|---|---|
| **FU-201** | Cổng "đủ 5 lượt" có chặn nhầm model vốn mạnh không | loại oan ≥ 2 lần/tuần → hạ xuống 3 lượt hoặc nới cửa sổ 14 ngày | 08/08 |
| **FU-202** | `win_rate` và `bt_hit` đang lệch nhau — bộ lọc nên chấm theo cái nào | đối chiếu trên cùng cửa sổ, xem cái nào dự báo tốt hơn kết quả bundle | 09/08 |

FU-202 xuất phát từ một chỗ khó hiểu: bảng xếp hạng 26 ngày cho `gemini-3.5-flash` hạng 4
(+6,73pp bạch thủ), nhưng win rate 7 ngày của nó lại gần chót bảng (MN 21,4% · MT 25,0% ·
MB 8,3%). Hai thước đo đang đo hai thứ khác nhau — cần biết cái nào đáng tin hơn.

Hoàn tác: `python web/backend/_v10934_deploy.py --rollback` (~1 phút).
