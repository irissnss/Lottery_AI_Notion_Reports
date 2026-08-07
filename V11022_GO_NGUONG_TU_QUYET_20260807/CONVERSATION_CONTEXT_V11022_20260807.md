# CONVERSATION CONTEXT — V11022 · 2026-08-07 tối

## Owner nói gì (NGUYÊN VĂN)

> HẾT CHU KỲ LIVE RỒI EM KIỂM TRA TỔNG LỰC TOÀN DIỆN, ĐỐI CHIẾU CÁC VẤN ĐỀ ĐÃ XỬ LÝ HÔM NAY CÓ
> KẾT QUẢ NÀO ỔN KHÔNG, CÓ GÌ CẦN ĐIỀU CHỈNH, CÁC VẤN ĐỀ TỒN ĐỘNG V.V... TẤT CẢ MỌI THỨ KHÔNG
> BỎ SÓT VẤN ĐỀ GÌ NHA EM.

Agent báo cáo lần một. Owner đọc xong, chỉ ra **ba chỗ agent làm chưa tới**:

> ĐÚNG CHẠY TIẾP 4 ĐI ĐÃ, Sao em nói prompt mới là 60 còn MB hôm hợp anh chưa hiểu? Anh vẫn thấy
> tính hiệu về có tín hiệu tốt tin hiệu xấu em phải soi chi tiết từng model Ai chứ em, **phụ 2
> có tín hiệu trúng kìa**, 🔬 DeepSeek Reasoner 40% 30d ở MT **lỗi nữa chứ**, Em phải xem kỹ chứ

Sau khi agent trình bằng chứng:

> ok tiếp đi em, sau đó tiền hành cập nhật báo cáo đầy đủ nâng V13 cho arifract dùm a

## Ba chỗ owner chỉ — cả ba đều đúng

### 1. «phụ 2 có tín hiệu trúng kìa» — ĐÚNG, và đây là chỗ nặng nhất

Agent so «1 số vs 2 số» mà **chỉ tính số chính** ⇒ báo *"12% vs 22%"*. Con số đó **che mất** sự
thật. Tính cả cửa số phụ:

| miền | prompt | chính trúng | **phụ trúng** |
|---|---|---|---|
| MB | MỚI | 3 | **2** |
| MN | CŨ | 8 | **8** |

Ở MN số phụ trúng **đúng bằng** số chính. Ở MB hai model **chỉ trúng nhờ số phụ**:
`lstm ['69','42']` · `xgboost ['25','94']`.

Trúng ít nhất một số: MB nhóm bỏ phụ **0/4** · nhóm giữ phụ **5/12**.

### 2. «DeepSeek Reasoner … lỗi nữa chứ» — ĐÚNG

`07/08 MT` ra **`[]`** (verdict SKIP) — **ngày đầu tiên trong 30 ngày**. Trước đó **88/93 lượt
đều ra 2 số**. Và deepseek 30 ngày: MB 48% · MT 58% · MN 68% — không hề tệ.

### 3. «prompt mới là 60 còn MB hỗn hợp» — bảng của agent viết khó đọc

Sự thật: **MB = prompt MỚI hoàn toàn** (chốt 17:30–17:35, sau deploy 13:35), bạch thủ **60**.
**MT** mới là **hỗn hợp** (05:00 cũ + 16:39–16:45 mới). **MN = prompt CŨ hoàn toàn** (05:00).

## Agent làm gì

1. Chạy việc 4 — dọn **217 tệp** ghi không đóng tay ⇒ toàn kho **0 chỗ**.
2. Soi lại **từng model, từng miền, cả số chính LẪN số phụ** — thứ lẽ ra phải làm từ đầu.
3. Trình bằng chứng, đề xuất **gỡ L-B giữ L-A**, owner chốt.
4. Gỡ L-B, deploy, `CTX-18.1` `PB-20.1`.

## Vấp ở đâu

### Lỗi gốc: đo cái mình nghĩ là quan trọng, không đo cái đang thật sự xảy ra

Agent thiết kế L-B để model «ra ít mà chắc», rồi đo bằng **tỉ lệ trúng của số chính** — đúng cái
chiều mà L-B tác động. Cửa bị đóng (số phụ) thì **không đo**. Owner nhìn ra ngay.

### Ba lỗi cẩu thả nữa trong cùng buổi tối

| # | lỗi | ai bắt |
|---|---|---|
| 1 | `git add web/backend/` quét cả **`node_modules` 19 MB** vào kho | agent, sau khi commit |
| 2 | Cổng vừa dựng **tự đếm nhầm chú thích của chính nó** ⇒ báo 231 chỗ sau khi đã dọn sạch | agent, khi kiểm lại |
| 3 | Lệnh `sed` sửa cron **không ăn mà vẫn báo chạy xong** | agent, khi đọc lại đầu ra |

### Và một chỗ cổng cứu

Script deploy V11022 chép từ V11016 nên **vẫn đòi `nguong_tu_quyet=True`** ⇒ dừng trước restart.
Phải sửa phép kiểm cho khớp việc mới. Đây là lần thứ ba trong ngày cổng deploy chặn đúng.

## Điều agent NÓI THẲNG với owner

**1. Lý do gỡ L-B KHÔNG phải thống kê.** Nó trái quy tắc owner đã chốt — *luôn ra số, không bao
giờ bỏ số*. Số liệu 0/4 vs 5/12 chỉ là xác nhận thêm. Nếu chờ đủ mẫu thống kê thì đã để một quy
tắc bị vi phạm chạy tiếp nhiều ngày.

**2. Kết quả trúng hôm nay không đẹp cho phía prompt mới:** MN (prompt **cũ**) trúng bạch thủ,
MB và MT (prompt mới) trượt cả hai. n=1 ngày nên không kết luận được, nhưng agent báo nguyên văn
thay vì chỉ khoe con số phân tán 0,69.

**3. Phép đo bầy đàn chưa dùng được.** Ngày 07/08 chỉ **MB** chạy prompt mới trọn vẹn. Cần
**3 ngày × 3 miền sạch** ⇒ FU-325 dời **08/08 → 10/08**. **Đừng đổi prompt gì tới 10/08**,
nếu không lại chồng biến lần thứ tư.

**4. Còn một lỗ hổng chưa bịt:** deepseek ra rỗng ở MT mà **không cổng nào báo** — bundle vẫn
dựng, vẫn `ACTIVE`, chỉ thiếu một phiếu, im lặng. Mở **FU-328** hạn 08/08.

**5. MB là miền yếu chung của cả nhóm ML**, không phải lỗi một model: random-forest **23%** ·
combo-no-token **26%** · smart-ml 29% · lstm 32% · combo-super 32% (30 ngày). MN thì model nào
cũng khá 55–81%.
