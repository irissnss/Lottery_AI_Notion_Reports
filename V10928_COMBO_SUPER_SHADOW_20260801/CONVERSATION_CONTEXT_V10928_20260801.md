# Nguyên văn phiên 01/08/2026 — phần V10928 (combo-super + shadow lãng phí)

> Giữ **nguyên văn** lời owner, không diễn giải lại.

---

## Owner nêu hai việc (12:56)

> **"Ôi quá lâu quá mệt mỏi ah em, anh quên nhắc và đã bị trôi sông chứ showdow gì mà lâu quá
> trời không lấy được model nào tốt nhét vào total offical quả là lãng phí, 1 chú ý là cắt model
> ảnh hưởng đến combo super mới quan trọng cận thận chỗ này."**

Hai ý:
1. **Shadow chạy quá lâu mà không promote ai** → lãng phí. Owner tự nhận *"anh quên nhắc và đã
   bị trôi sông"*.
2. **Cắt model ảnh hưởng combo-super** → cẩn thận chỗ này.

Đây là **lần thứ hai** owner nhắc về combo-super. Lần đầu ở phiên trước: *"đối với combo-super
thì cần nghiên cứu kỹ đó nha vì nó là tổ hợp nhiều model Ai và no token trong đó em cắt model no
token + model Ai trong total thì nó cũng bị ảnh hưởng đó nha nên xem cho kỹ vào."*

---

## Kết quả kiểm — owner đúng cả hai

### Shadow

```
từ 2026-04-14 → 2026-08-01   ·   110 ngày   ·   3.778 lượt gọi   ·   28 model
số model đi từ shadow lên official:  0
```

Model chạy lâu nhất đã **104–110 ngày**. Đây không phải thiếu mẫu — đây là **không ai quyết**.

### combo-super — và agent đã báo cáo SAI

Phiên trước agent nói với owner: *"combo-super MN/MT chỉ dùng `meta-learning` + `lstm`"*.

**Sai.** Đó là ảnh chụp một thời điểm, agent trình bày như thể là quy tắc cố định. Sự thật đọc
thẳng từ code và **gọi thẳng hàm** trên VPS:

```python
get_dynamic_ml_filter(region, top_n=3, days=7)   # 3 ML mạnh nhất, từ pool 4
get_dynamic_ai_filter(region, top_n=2, days=7)   # 2 AI mạnh nhất, từ pool 7
```

Chọn lại **mỗi ngày, riêng từng miền**. Hôm nay:

| Miền | ML top-3 | AI top-2 |
|---|---|---|
| MN | random-forest · meta-learning · lstm | claude-sonnet-4-6 · gpt-5-mini |
| MT | lstm · xgboost · random-forest | gemini-2.5-flash · deepseek-reasoner |
| MB | meta-learning · lstm · xgboost | claude-sonnet-4-6 · claude-opus-4-6 |

**Cả 4 ML đều đang được dùng thật.** Nếu owner tin lời agent phiên trước mà duyệt cắt `xgboost`
hoặc `random-forest` vì tưởng chúng không được dùng, thì đã cắt nhầm.

Đây đúng là chỗ owner cảnh báo, và cảnh báo đó đã cứu một lần cắt sai.

---

## Điểm mấu chốt cho mọi quyết định cắt sau này

Pool ML chỉ có **4** mà phải chọn **3** — cắt **1 cái** là mất hoàn toàn khả năng chọn:

| Cắt | Pool còn | Hệ quả |
|---|---|---|
| 0 | 4 | chọn 3 trong 4 — bình thường |
| 1 | 3 | buộc dùng cả 3, không còn chọn |
| 2 | 2 | thiếu nguyên liệu |
| 3 | 1 | hỏng |

Pool AI có 7 chọn 2 — rộng, cắt 2 vẫn còn 5.

**Nguyên tắc an toàn:** bỏ cờ `output_eligible` (model vẫn chạy, chỉ không bỏ phiếu vào bundle)
thì combo-super **không hề bị ảnh hưởng**. Chỉ khi **dừng hẳn** model thì combo-super mới mất
nguyên liệu. Hai việc này khác nhau hoàn toàn, phải nói rõ mỗi lần đề xuất.

---

## Hai chỗ vấp khi kiểm

1. **Regex quét hằng số bắt hụt** vì `AI_MODELS` là danh sách **dict** chứ không phải chuỗi —
   lượt đầu chỉ thấy 3 model thay vì 7. Suýt báo cáo sai lần nữa. Phải **gọi thẳng hàm** mới ra
   đúng.
2. **Nghi mốc 50% mặc định làm chọn mù**: code ghi `chưa có data = 50% default` mà model thật
   chỉ đạt 21–36%, nên model không có dữ liệu sẽ xếp trên. Kiểm từng lựa chọn hôm nay:
   **15/15 đều có n=7 dữ liệu thật** — nghi vấn không thành.

Nhưng lộ ra chuyện khác: **MN hôm nay chọn 3 ML mà cả ba thắng 0/7 trong tuần.** Bộ lọc chọn
"tốt nhất trong đám tệ", không có sàn chất lượng tối thiểu.
