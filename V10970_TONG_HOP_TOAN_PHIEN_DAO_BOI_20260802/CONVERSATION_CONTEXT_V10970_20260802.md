# CONVERSATION_CONTEXT_V10970 — 2026-08-02

Nguyên văn lời owner (rút từ transcript `eeb49d3c-16d5-440b-9e2e-df1485c7bdf9`) + agent làm gì + vấp.  
Index đầy đủ 199 mục: `evidence/owner_message_index.json`.

---

## 1. Câu kích hoạt V10970 (nguyên văn)

> Quá nhiều vấn đề anh và em đã đề cập đến và đào bới trong suốt trò chuyện này em có thể tổng hợp lại đầy đủ , chiêt hơn nữa được không em? Đẩy thêm 1 báo cáo thật đầy đủ hơn nữa bao gồm tất cả các vấn đề anh đã đề cập, em đã xử lý , em đã tổng hợp, em đã đào bới, em đã ghi nhận chờ tới hạn , tất cả mọi thứ không bỏ sót bất kỳ nội dung nào trong trò chuyện này ? Đồng thời em đánh live hôm nay thành công nhờ đâu? Có thay đổi gì khiến "tốt lên" hay chỉ may?

**Agent làm:** đọc briefing · quét transcript · đọc V10945–V10969 · ledger/FU/CHANGELOG · query VPS 3/3 + model voters · viết REPORT 9 phần + phụ lục A–F · prepend docs · push public · chạy report gate.  
**Không:** sửa production, restart lottery, ghi Notion.

---

## 2. Chủ đề owner lặp lại trong arc (nguyên văn rút)

### 2.1 Tổng hợp / đừng quên / đừng hỏi lại

> Tới giờ anh vẫn chưa rõ các vấn đề em phát hiện ra bao gồm những gì tổng hợp thật chi tiết dùm anh… Nguyên nhân giảm sút là gì tại sao?

> Anh không muốn nhắc tới nhắc lui hoài những vấn đề mà em có thể tra ra, có thể kiểm soát được đâu?

→ Sinh §56 (A54) sổ quyết định + session start; V10954/TONG_HOP; V10970 bao quát.

### 2.2 Báo cáo public / Notion chỉ đọc

> …sau khi thực hiện code, fix, audit cần đẩy báo cáo report lên github report public… Notion MCP dùng để tham khảo tài liệu khi cần không được cập nhật vào Notion nha em.

→ §57 (A55). V10970 chỉ push GitHub reports.

### 2.3 Dừng tiền / edge

(Owner xác nhận sau V10945 — đo lỗ 133tr/90d, hệ không hơn bừa.)  
→ QD-013 + FU-208. Vẫn hiệu lực sau ngày 3/3.

### 2.4 Đóng băng tới 08/08

> Đóng hết. Chúng là di sản… giờ đã có cổng thống kê thay thế.  
(và lệnh đóng băng đường ra số — QD-014 / FU-215)

### 2.5 Tín hiệu MT / prompt / hai prompt cùng model

> …tín hiệu rơi rớt ở đâu… Nếu kết luận là "không cứu được", hãy nói thẳng.

> chỉ hiểu là prompt A + Model A không thể so sánh prompt B với Model B…

→ V10955; QD-016/017/018.

### 2.6 Mã công việc dễ đọc

> Số hiệu phải viết tắt đầu mục công việc và hạn ngày… TH0808…

→ QD-019 / §58 phương án B.

### 2.7 Hết live 02/08

> Hết live rồi đó em kiểm tra tổng lực toàn diện dùm anh? đẩy toàn bộ các báo cáo chi tiết đầy đủ lên github report dùm anh nha em

→ V10969 (3/3 WIN, edge ĐÓNG) rồi V10970 (tổng hợp + may vs thật).

### 2.8 Mốc FINAL / nhất quán giờ VN (đầu arc)

> X1… phải nhất quán và hệ thống phải hiểu giờ việt nam…  
> X2 Vậy biên chốt nhất quán 2 phút hết đi…

> total output Tối đa MN là 15h45 / MT 16h53 / MB 17h53…  
(sau V10931: MT 16:58 / MB 17:58)

### 2.9 Total / combo / cắt model cẩn thận

> cắt model ảnh hưởng đến combo super mới quan trọng cận thận chỗ này.

> gemini-3.5-flash ==> thử lại xem có phương pháp vào vượt qua lỗi này không em?

---

## 3. Agent làm gì theo giai (tóm tắt)

| Giai đoạn | Việc chính | Vấp |
|---|---|---|
| 31/07–01/08 | Múi giờ, FINAL, promote model, cứu gemini, filter combo, deploy V10939 | Deploy chạm T-chốt (V10940); agent hỏi lại việc đã có trong roadmap |
| 01/08 | Edge gate, dừng tiền, tổng hợp | FU/SSOT lệch “CHƯA DEPLOY” |
| 02/08 sáng–chiều | Retrain AUC, MT drop, freeze, RULES-FIRST, UI, mã §58 | Đọc FU bản cuối file; folder báo cáo trùng tên; sync size mismatch |
| 02/08 tối | V10969 hết live; bù V10964b/65b | Push bị chặn secret base64 |
| 02/08 ~21:14 | **V10970** tổng hợp + phân tích may | Local DB thiếu 02/08 → chuyển VPS |

---

## 4. Kết luận agent trả owner về “may hay thật”

Live 02/08 3/3 WIN là **biến thiên ngày**. Cổng 90 ngày vẫn ĐÓNG. Trong 90 ngày chỉ 1 lần 3/3 (hôm nay); kỳ vọng độc lập ~2,2%. Model mới có góp phiếu thắng — anecdote, không phải edge hệ thống. Không mở tiền. Tôn trọng QD-014 tới hết 08/08.

---

## 5. Không ghi Notion

Theo §57: Notion chỉ đọc. Không tạo/sửa trang.
