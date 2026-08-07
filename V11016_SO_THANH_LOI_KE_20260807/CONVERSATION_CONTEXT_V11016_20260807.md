# CONVERSATION CONTEXT — V11016 · 2026-08-07

## Owner nói gì (NGUYÊN VĂN)

> Làm ngay luôn đi em.

Bốn chữ. Trả lời câu agent hỏi cuối phiên trước:

> *"**L-A làm ngay hay chờ 21/08?** Làm ngay ⇒ đúng ý anh nhưng FU-284 thành đo **gộp ba biến**,
> hết tách nhân quả. Chờ 21/08 ⇒ giữ phép đo sạch nhưng đợi thêm 2 tuần. **Em nghiêng về làm
> ngay.** Anh chốt."*

Việc gốc owner giao cùng ngày:

> *"các số học được nhồi nhét cần biến thành ngữ cảnh thực sự để model đọc hiểu tự phân tích, tự
> tư duy tự tra soát trong ngưỡng tự quyết định output số tốt nhất ở số chính và nhẹ hơn là số
> phụ, tất cả tự nhiên có quy luật có điều kiện, đừng output theo số gò như thế dẫn đến bầy đàn
> là đúng rồi, lùa vào 1 bộ số định sẵn trong ngày để model quyết định xong thấy bầy đàn."*

## Agent làm gì

1. **Soi trước khi sửa (§60.2).** Hỏi ba câu: ai còn trỏ tới khối này · bỏ trống số phụ có làm vỡ
   chỗ nào không · có phép nào máy chạy được để chứng minh đã sạch không.
   - Kiểm 5 tệp tiêu thụ số phụ ⇒ tất cả lọc rỗng an toàn, hợp đồng JSON đã có `NO_SECONDARY`.
2. Đổi khối `RULES-FIRST` thành lời kể có đài + ngày + giải + hồ sơ + **cách đọc hồ sơ**.
3. **Đo trước/sau bằng cùng một thước** — và số đi SAI HƯỚNG.
4. Đào ra **ba khối khác** vẫn in đúng bộ số đó. Gỡ cả ba.
5. Deploy — **cổng chặn**, còn chỗ thứ tư. Gỡ nốt rồi deploy lại.

## Vấp ở đâu — hai lần trong một phiên

### Vấp 1: sửa một khối, tưởng xong

Sau khi sửa khối đầu, chuỗi kiểm `ép_chọn=False` **đạt**. Nếu dừng ở đó và báo cáo thì đúng lỗi
§60.1. Chỉ vì chạy phép đo trước/sau mới thấy:

| chỉ số | trước | sau bản sửa 1 khối |
|---|---|---|
| ký tự MB | 10.379 | **11.715** (+1.336) |
| dòng rổ số MB | 9 | **12** (+3) |
| cặp khối trùng ≥60% | 10 | **10** |

**Prompt dài thêm mà rổ số nhiều hơn** — đi ngược mục tiêu.

### Vấp 2: gỡ ba chỗ, sót chỗ mạnh nhất

Cổng deploy trước restart:

```
MB: ro_hop_nhat_da_het=True · ke_su_kien=True · nguong_tu_quyet=True
    · ro_xep_hang_da_het=False ← TRƯỢT · ep_chon_da_het=True
✗ DỪNG — prompt trên VPS không đúng như mong đợi, KHÔNG restart
```

Chỗ sót: `OWNER ANTI-TRAP CHECK` › `FRESH candidates (prefer if doctrine support is also
strong): 69 (boost=0.100 CONV×2 …)` — **vừa xếp hạng vừa khuyên chọn**, tức chỗ **neo mạnh nhất
trong cả bốn**. Cổng cứu đúng một lần.

## Bốn chỗ cùng một bộ số

| # | chỗ | hình thức |
|---|---|---|
| 1 | `RULES-FIRST` | rổ hợp nhất `trỏ tới 10 đuôi: 13 31 32 …` |
| 2 | `EVIDENCE TABLE` › Rule candidates | rổ **ĐÃ XẾP HẠNG** `🔥 35: boost=0.180 CONV×2` ×8 |
| 3 | `EVIDENCE TABLE` › trace | rổ trần `← ✅ Hà Nội G6+G7 → tails=[13,35,69,…]` ×5 |
| 4 | `OWNER ANTI-TRAP CHECK` › FRESH | xếp hạng **+ khuyên chọn** |

Khối #2 trùng **100%** bộ số với `Block 3` và **68%** với khối kể sự kiện.

## Điều agent NÓI THẲNG với owner

**1. Prompt DÀI THÊM.** MB +1.014 · MT +1.395 · MN +1.448 ký tự. Lời kể dài hơn danh sách. Owner
xin **ngữ cảnh** chứ không xin ngắn — nhưng đây là đánh đổi thật, nếu owner muốn ngắn lại thì
phải nói.

**2. Cái giảm là cái đáng giảm.** Cặp khối trình lại cùng một bộ số: MB **10 → 4** · MT **7 → 3**.
Đúng chỗ owner nêu — *"các tầng điều nhồi tương tượng na ná nhau liên tục"*.

**3. Chuỗi kiểm có mặt/vắng mặt KHÔNG ĐỦ.** `ép_chọn=False` đúng mà việc vẫn chưa xong. Câu hỏi
thật không phải *"còn câu ép chọn không"* mà *"model còn được đưa một rổ số dọn sẵn không"*. Phải
đo **hình thù dữ liệu**, không chỉ dò chuỗi. Đây là bài học phải nhớ.

**4. §60.3 — không đếm thô.** Chỉ số "dòng ≥6 số" tăng 9→10, nhưng đọc từng dòng thì chỉ **2
dòng** là đuôi thật để chọn (đã gắn đài + ngày + giải) và **1 dòng** là pool đã tiêu (thông tin
để TRÁNH); 7 dòng còn lại là tỉ lệ phần trăm, ngày tháng, ví dụ minh hoạ bị bộ đếm nhận nhầm.

**5. Còn một chỗ chưa xử.** `D-1 cross-region tail pool: 01, 03, 04, …` — 12 đuôi **không gắn
nguồn**. Là thông tin loại trừ nên có ích, nhưng chưa nói được «của đài nào, ngày nào». Để trong
FU-316, hạn 14/08, làm sau khi V11016 có ≥7 ngày đo — **cấm chồng biến lần thứ tư**.

**6. FU-284 nay đo GỘP BA BIẾN.** Owner đã được trình rõ và vẫn chốt "làm ngay". Ghi lại để sau
này không ai đọc kết quả 21/08 mà tưởng nó tách được nhân quả.
