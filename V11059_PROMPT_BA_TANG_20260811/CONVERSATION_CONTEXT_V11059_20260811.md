# CONVERSATION CONTEXT — V11059 · 11/08/2026 rạng sáng

## Owner nói gì (NGUYÊN VĂN)

> *«Sao không thiết kế prompt 2-3 tầng chuẩn ngữ cảnh để đo song song đi cho tiết kiệm thời gian,
> lúc nào cũng đòi cắt, prompt chuẩn đâu mà đòi AI tốt hơn ML em? Chưa cân xứng chưa trung thực
> luôn đó em»*

> *«chạy showdow ngay đi không chờ đợi gì cả, nhưng phải thật kỹ càng tỉ mỉ cẩn trọng cấm cẩu
> thả, tự diễn, tự chế mọi thứ phải có cơ sở và phương pháp đầy đủ nha em»*

> *«T-B là đủ rồi em»*

---

## Câu phê bình chính xác nhất owner từng đưa

Trước đó agent trình một chuỗi số rất chỉn chu: cụm AI tốn 30.004 token/ngày, cụm ML tốn 0, và
chênh lệch chất lượng **không đo được** ⇒ đề xuất **thu gọn roster AI**.

Owner chặn bằng một câu: **«prompt chuẩn đâu mà đòi AI tốt hơn ML em?»**

Và câu đó đúng. Chính agent, trong ba phiên liền trước, đã ghi vào báo cáo rằng prompt đang chạy:

- tự mâu thuẫn về «nhiều nguồn»
- bơm điểm từ bộ luật mà tài liệu ghi **0/105 qua cổng**
- de-herding làm nửa chừng
- `SP-4.3`/`SP-4.4` không có chữ ký owner

⚠️ [ĐÍNH CHÍNH · ĐÃ RÚT LẠI RL-002: gạch đầu dòng thứ hai ở trên («0/105 qua cổng») là SAI —
thực tế 8/105 luật đạt `READY_STRONG`. Câu đúng phải là «0/105 kiểm NGOÀI MẪU». Không đổi kết
luận của mục này (prompt vẫn nhiều lỗi khác), chỉ đính chính đúng con số. Xem
docs/SO_RUT_LAI.json, bản rút V11073_DINH_CHINH_0_TREN_105_20260815.]

Rồi vẫn đem cụm AI **chạy trên chính prompt đó** ra so với ML và kết luận «AI không hơn». Đó là
phép so **AI-cộng-prompt-hỏng** vs ML — và agent đã dùng nó làm căn cứ để khuyên cắt.

**Đã rút lại đề xuất cắt.** Cắt trước khi biết prompt chuẩn cho ra gì là **cắt mù**, và nếu prompt
chuẩn làm AI bật lên thật thì agent đã khuyên vứt đúng thứ đáng giữ.

---

## Và câu thứ hai của owner phá luôn cái cớ «vật lý»

Agent đã ba lần viết rằng thời gian đo là **vật lý của bài toán**: 3 điểm dữ liệu/ngày, nền 34%,
mọi câu hỏi đáng giá rơi vào 4–30 tháng.

Owner: *«đo song song đi cho tiết kiệm thời gian»*.

Tính lại:

| | thiết kế agent đang dùng | ghép cặp song song |
|---|---|---|
| đơn vị so | miền-ngày | **(model × miền × ngày)** |
| nhiễu còn lại | ngày + model + prompt | **chỉ prompt** |
| n cần | ~696 miền-ngày | ~237 cặp |
| tốc độ | 3/ngày ⇒ **7,6 tháng** | 15/ngày ⇒ **~16 ngày** |

**Không phải vật lý — là thiết kế đo dở.** Ghép cặp triệt tiêu hai nguồn nhiễu lớn nhất (ngày và
model) vì hai nhánh chạy cùng model cùng ngày cùng dữ liệu. Agent đã bỏ qua điều đó suốt.

---

## «Cấm tự chế» — nên bước đầu tiên là dump prompt THẬT

Không đọc tài liệu. Gọi thẳng hàm đang phục vụ trên VPS:

```
system_prompt   7.760   ·  analysis_body  16.126
context_pack   10.567   ·  rulebook       15.465   ⇒ TỔNG 49.839
source_regions = "MN_D1,MT_D1,MB_D1"   ← chỉ D-1
```

**Và agent tự bắt lỗi ngay ở bước này:** bản dump đầu gọi `build_context_pack()` **trực tiếp**,
nhưng đường phục vụ còn **gỡ de-herding sau đó**. Nên bản dump đầu **không phải bản gửi đi thật**
— đúng lỗi `RM-14` mà agent vừa trích trong cùng đoạn văn. Đã đo lại.

---

## Ba mâu thuẫn — và một cái chỉ tìm ra khi chịu đọc hết

**M1** cùng một prompt: `system_prompt:69` ghi *«KHÔNG có điểm thưởng»* kèm số đo `z=−2,54`, còn
`analysis_body:355` ra lệnh *«ưu tiên số xuất hiện trong NHIỀU nguồn»* — và câu ra lệnh nằm
**dòng 355/358**, vị trí cuối.

**M2** là cái đáng kể nhất, và agent **suýt bỏ lỡ**. Ban đầu agent định gọi «`§4` mâu thuẫn với
`§11/§18`» — nhưng đọc kỹ thì `§4` nói về đồng thuận **model**, `§11/§18` nói về **Rule Tails**:
hai đối tượng khác nhau, **không mâu thuẫn**. Đó là **nói quá**.

Chỉ khi chịu đọc hết `§8 Conflict Resolution` mới thấy:

```
§8:44  Ưu tiên (cao→thấp): Width > Rules > Diversity > Recency > Caution
```

Có **thứ tự ưu tiên rõ ràng**, và nó xếp **`Rules > Diversity`**. Mà Rule Tails **giống hệt cho cả
16 model**. Nên `§23:243` (*«ít nhất 2-3/7 AI models nên chọn SỐ KHÁC»*) **bị chính `§8` đè**.

**Prompt không để model tự bầy đàn — prompt RA LỆNH bầy đàn, một cách nhất quán và có thứ tự.**
Khớp đúng con số đo được: đồng thuận cặp AI **0,2929** vs ML **0,1519**, **z = +3,10** — kết quả
duy nhất vượt ngưỡng thống kê trong cả chuỗi phiên.

**M3** de-herding chạy **đúng** trên context pack (gỡ 1.133 ký tự, 4/4 khoá về 0) nhưng **không
chạm thân**, để nguyên `analysis_body:304` *«AI nên ưu tiên patterns từ models có win_rate cao
hơn»* — **đúng cơ chế** V10768 sinh ra để gỡ.

---

## Agent tự đính chính hai chỗ

- **`§5g` KHÔNG còn là luật cộng điểm** — nó đã được sửa, và **có cả số đo `z=−2,54` ghi ngay
  trong prompt**. Agent từng ngụ ý ngược lại trong các phiên trước.
- **«`§4` vs `§11/§18`» là nói quá** — như trên.

---

## Lỗi thiết kế thí nghiệm agent tự bắt

Bản đầu gửi `system=""` + `user=tất cả`, trong khi CONTROL gửi `system=system_prompt`. Thế là hai
nhánh khác nhau **cả vai trò thông điệp**, không chỉ nội dung — **mất tính một-biến**. Mô hình xử
lý `system` khác `user`, nên chênh lệch đo được sẽ lẫn tác dụng của việc **dời khối**.

Đã sửa: `system_prompt` giữ nguyên vai trò ở **cả hai nhánh**, chênh còn **+1.035 ký tự (+2,5%)**
ở đúng nội dung user.

Và một chỗ nữa: agent **thi hành lệch tài liệu thiết kế của chính mình** — tài liệu ghi T3 gồm
`§22–§26`, mã lại nhét cả rulebook vào T2, làm T3 chỉ còn 1.462 ký tự. Sửa rồi: T3 = 6.280, và
`§22/§23` **nằm ở tầng thắng xung đột** — nếu không thì ngoại lệ chống bầy đàn vừa thêm sẽ bị
chính `§8` gốc nuốt lại.

---

## Một lỗi dây chuyền agent tự gây rồi tự sửa

Đưa phép đo **vừa đăng ký, bảng còn rỗng** vào cổng chung ⇒ cổng thoát 1 ⇒ **BA quyết định KHÔNG
LIÊN QUAN** (`QD-055` · `QD-058` · `QD-059`) cùng báo TRÔI.

Sửa tận gốc: `K1` nay phân biệt **«CHƯA CHẠY»** với **«HỎNG»**, ân hạn **2 ngày tự động hết** —
quá đó mà bảng vẫn rỗng thì là **cron chết thật** và phải đỏ. Không bỏ qua im lặng, cũng không
kéo cả sổ xuống vì một phép đo chưa tới lượt.

---

## Một chi tiết suýt làm hỏng cổng nhân quả

Giờ trong DB là **UTC**. Đọc thẳng thì MN có vẻ chạy official lúc 22:15 và ra kết quả lúc 09:35 —
vô lý. Quy về giờ VN mới đúng: MN official **05:15** → kết quả **16:35** · MT **16:36** →
**17:30** · MB **17:31** → **18:30**.

Nghĩa là cửa sổ MT/MB chỉ **~35 phút**, mà 5 model × 120s có thể mất 10 phút. Nên thêm **cổng nhân
quả kiểm lần hai** ngay trước khi ghi: nếu kết quả về giữa chừng thì **bỏ cặp**, không ghi.

---

## Trạng thái cuối phiên

PID `1345720` → **`1353489`** · health 200 · API 401 · 0 lỗi · **hash 4 bảng khoá PRE = POST y
hệt** · cron 136 → 139 dòng · cổng §52 soi **ba** phép đo, thử chặn RM-15 **từng phép riêng**.

Prompt **official không hề bị đụng** — `QD-041` nguyên vẹn.

Lượt thật đầu tiên: **06:00 hôm nay**. Đọc được kết quả khoảng **27/08**.

TanPhatAI cần làm: xem mục cuối `REPORT_V11059.md` — năm việc, quan trọng nhất là ④ ghi vào sổ
**ba mâu thuẫn prompt** vì chúng **còn nguyên trong prompt official**, chỉ được gỡ ở nhánh shadow.
