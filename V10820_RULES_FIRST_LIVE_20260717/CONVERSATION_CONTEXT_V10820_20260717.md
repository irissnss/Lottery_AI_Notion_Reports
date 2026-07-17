# CONVERSATION CONTEXT — V10820 (2026-07-17 23:33)

Nguyên văn tin nhắn owner ra lệnh điều chỉnh lớn (sau khi nghe tổng hợp V10816-V10819):

> Ý anh khác hoàn toàn ý em.
> - Cái phương pháp cái prompt đã chạy rất lâu rồi , đơn tín hiệu không ổn định bữa có , bữa không , bữa dày , bữa mỏng lèo tèo mà total có tốt đến mấy mà đơn model lèo tèo thì làm sao output cho đúng nổi .
> - k11a có như thế nào chưa ổn định vì đơn model tín hiệu kém thôi
> ==> tại sao không backup tại thời điểm này và tiến hành điều chỉnh lớn luốn chạy thật luôn trong 7-10 ngày để đo cái cải tiến hành em. Chứ cái hiện tại đã đo lâu quá rồi mà em . Sau 7-10 có live thật luôn kết hợp cái củ trước đó đã được live nhiều ngày chúng ta có cái nhìn tốt hơn đó em. Vấn đề em phải làm sao thật kỷ , thật tỉ mỉ, ghi chú đầy đủ, backup đầy đủ là được. đảm bảo sau xử lý là chạy ổn định đáp ứng tốt cho live ngày mai luôn .

Bối cảnh trước đó cùng phiên (đêm 17/07):
- V10818 (owner 20:59): hỏi prompt gốc, "model luôn lệch ±1", "MB toàn 34-43 đảo pha" → đo: ±1 = ảo giác tần suất, nhưng phụ-biến-thể hại thật ở MB; sandbox PHASE-OFF 27 cặp.
- V10819 (owner 22:38): "rules có giá trị bị đảo pha/±1 làm rơi rớt; 43 ngoài rules được đề xuất phi lý; bốc đại từ rules cũng trúng" → xác nhận lịch sử 200+ ngày: bốc-1-từ-rules thắng model main cả 3 miền; sandbox RULES-FIRST MB@17/07 any 4/5 hội tụ 46✓.
- V10820 (owner 23:33, tin trên): gộp toàn bộ thành MỘT thay đổi prompt production PB-18.1, chạy thật từ live 18/07, đo 7-10 ngày. Em (agent) thực thi trong đêm: backup 2 đầu → patch → smoke as-of → deploy → verify → governance đầy đủ.
