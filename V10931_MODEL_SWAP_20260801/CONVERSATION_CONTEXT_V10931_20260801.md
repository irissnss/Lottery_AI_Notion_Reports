# Nguyên văn phiên 01/08/2026 — phần V10931 (hoán đổi model + dời hạn)

> Giữ **nguyên văn** lời owner, không diễn giải lại.

---

## 1. Owner bức xúc về shadow (12:56)

> **"Ôi quá lâu quá mệt mỏi ah em, anh quên nhắc và đã bị trôi sông chứ showdow gì mà lâu quá
> trời không lấy được model nào tốt nhét vào total offical quả là lãng phí, 1 chú ý là cắt model
> ảnh hưởng đến combo super mới quan trọng cận thận chỗ này."**

Đo lại: **110 ngày · 3.778 lượt gọi · 28 model · 0 lần promote.** Owner đúng.

---

## 2. Owner sửa hướng của agent (~13:0x)

Agent trình phương án cắt 2 model AI tốn tiền (`gpt-5.4`, `gpt-5-mini`) và hỏi cắt hẳn hay bỏ
cờ bỏ phiếu. Owner không chọn cả hai mà đưa hướng thứ ba:

> **"sao không thay thế 2 model show tốt vào luôn, cơ chế filter model mạnh nhất thì nhét vô mà
> output chứ em"**

**Ý này gọn hơn hẳn cách agent định làm.** Hoán đổi giữ nguyên số lượng pool (7 AI) nên bộ lọc
top-2 của combo-super không mất khả năng chọn, và model mạnh sẽ tự được nhặt.

Owner đồng thời chốt: **promote ngay hôm nay**, và **nhận cả hai model dù `glm-5.1` lỗi 4,65%**
(ngang `gemini-3.5-flash` từng bị cho nghỉ vì hay rớt).

---

## 3. Agent trình rào thời gian — owner cho số (~13:3x)

Agent đo ra hai model mới chậm gấp 40–70 lần hai model bị thay, vượt mốc chặt 300s của chuỗi.
MT chỉ dư **1 phút** trước T-chốt. Owner trả lời:

> **"ok em vậy dời chốt output cuối cùng cho MT là 16h58 và MB là 17h58 em thấy sao?"**

Agent kiểm: `money_board.CUTOFF['MT'] = 17:00` là **trần cứng** chống nhìn trộm. Nên **16:58 là
con số tối đa có thể** — owner chọn đúng sát trần.

---

## 4. Sáu chỗ vấp trong lúc làm

| # | Vấp | Hậu quả nếu bỏ qua |
|---|---|---|
| 1 | Hai model mới vượt mốc chặt **300s**: `glm-5.1` TB 516s (max 796), `gpt-oss-120b` TB 402s (max 886) | **Thay xong thành mất trắng 2 chỗ** — bị cắt giữa chừng, không ra số nào |
| 2 | Cơ chế hạn riêng **đã có sẵn** (V10785, thêm vì `kimi-k2.5` 470s bị cắt 7 lần/7 ngày) nhưng hai model mới **chưa được đăng ký**; và luồng **official** không truyền hạn riêng trong khi luồng **shadow** thì có | Đăng ký hạn riêng thôi vẫn vô dụng với official. Đây là lý do hai model sống được ở shadow mà sẽ chết ở official |
| 3 | `CUTOFF['MT'] = 17:00` là trần cứng | Dời hạn quá 17:00 là vi phạm chống nhìn trộm |
| 4 | Các danh sách model được **suy ra** từ bảng `MODEL_REGISTRY` | Sửa danh sách thay vì bảng gốc là sửa nhầm chỗ, không có tác dụng |
| 5 | Script deploy vỡ ở bước đọc lại vì module in chữ trước JSON | Không ảnh hưởng deploy nhưng suýt tưởng deploy lỗi |
| 6 | `combo_super.py` có sẵn khối cảnh báo *"New models EXCLUDED — default WR=50% có thể thắng top-3 → ảnh hưởng /du-doan"*, và `glm-5.1` đang bị comment lại vì lý do đó | Kiểm ra cổng yêu cầu ≥5 dự đoán, hai model có **306–309**, và ngày 01/08 cả hai có dữ liệu **thật n=7** nên không rơi vào nhánh mặc định 50%. Cổng thoả rất xa |

---

## 5. Chỗ owner cảnh báo — đã giữ nguyên vẹn

Owner dặn hai lần về combo-super. Kết quả sau khi đổi:

```
combo_super.ML_MODELS  =  4 model, KHÔNG ĐỤNG
combo_super.AI_MODELS  =  7 model, hoán đổi 2, giữ nguyên số lượng
```

Pool ML có 4 chọn 3 — cắt 1 là mất hoàn toàn khả năng chọn, nên **không đụng cái nào**.
Pool AI có 7 chọn 2 — hoán đổi giữ nguyên 7 nên biên độ chọn không đổi.

Và ngay lần chọn đầu sau khi đổi, **MN đã tự nhặt `gpt-oss-120b`** vào top-2 — đúng cơ chế
owner mô tả.

---

## 6. Kết quả kiểm sau deploy

```
official 15 (không đổi số lượng)  ·  token 7  ·  shadow 11  ·  combo AI 7  ·  combo ML 4
hạn riêng  glm-5.1 840s · gpt-oss-120b 900s · model khác vẫn 300s
4 hằng số hạn output đều = MT 16:58 / MB 17:58
cron khoá /choi  15:43 · 16:56 · 17:56
bộ tự kiểm nhất quán  16 phép, lệch 0
hash 4 bảng khoá  GIỮ NGUYÊN cả bốn
```
