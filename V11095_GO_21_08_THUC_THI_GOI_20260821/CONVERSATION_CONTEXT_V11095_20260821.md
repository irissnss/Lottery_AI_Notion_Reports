# CONVERSATION CONTEXT — V11095 · 21/08/2026 · ngày mở gói

## Owner nói gì (NGUYÊN VĂN)

> **sáng 21/08** — *«GO 21/08: THỰC THI GÓI 12 MỤC + 1 THIẾT KẾ … `QD-041` HẾT HẠN · thực thi
> theo `docs/BAN_DO_THUC_THI_2108.md` ĐÃ CHỐT tối 20/08.»*

> *«L1 → L2 → L3 đúng bản đồ · bảng kiểm 10 bước · mỗi mục một commit riêng, revert độc lập.»*

> *«Va chạm `D2` × `FU-397b`: CẤM GỘP — `D2` tắt đúng thứ `FU-397b` đang đo.»*

> *«Miễn trừ K8 HẾT HẠN HÔM NAY … nếu chưa xử thì K8 đỏ lại là CỐ Ý — phải ghi rõ, cấm im.»*

> *«cổng chặn thì VÁ CHO ĐẠT THẬT, cấm cờ bỏ-qua.»*

---

## Ngày này hoá ra không phải ngày thi hành

Kế hoạch là mở 12 mục. Kết quả là **4 mục thi hành, 1 thiết kế, 8 chờ owner** — nhưng đó không
phải chuyện đáng kể của hôm nay.

Đáng kể là: **mỗi mục em đụng vào đều lộ ra một thứ khác dưới nó**, và không thứ nào trong số đó
nằm trong gói.

---

## Mục #12 — «gỡ một chỉ số chết» hoá ra không trung tính

Mục này trong sổ có **đúng một dòng**, ô ghi chú **trống**. Không một lý do nào trong toàn kho.
Nên phải tự đo lấy căn cứ.

`latency_score` chết thật: **0,5 ở cả 7.981 dòng**, đúng một giá trị suốt đời bảng, vì nguồn
`model_latency_cost_audit_daily` **ngừng nhận dòng từ 06/05** và `latency_available=1` đếm được
**0/4.033** — chưa bao giờ có một dòng dùng được.

Đến đây thì gỡ là chuyện hiển nhiên. Nhưng điểm ấy đi qua `final *= 0.55` khi model chưa đo được.
Bỏ hằng số `0,05` thì nhóm **đo được** mất `0,05`, còn nhóm **chưa đo** chỉ mất `0,0275`.

**1.115/109.426 cặp đảo chiều. 100% là cặp (đo được × chưa đo). 930 cặp chạm model đang bỏ phiếu.**

Tức là: **gỡ một chỉ số đã chết vẫn lặng lẽ chỉnh lại một hình phạt khác.** Nếu chỉ gỡ rồi báo
*«đã dọn rác»* thì báo cáo đúng chữ mà sai việc.

Giữ hằng số dưới tên `DI_SAN_LATENCY = 0.05`, hiện nguyên hình kèm lý do. Công thức mới tái lập
điểm cũ **7.981/7.981, lệch 0**. Việc chỉnh hình phạt tách ra `FU-412`, trình owner.

---

## Và trong lúc đo mục đó, bộ phân loại của chính em nói dối

Quét ngược báo *«2 chỗ còn sót»*. Đọc kỹ thì **cả hai là bắt nhầm**: một là chú thích em vừa
thêm, một là `latency_class` — **cột của bảng khác hoàn toàn**.

Nếu tin phép đếm thì đã đi sửa nhầm hai chỗ vốn đúng. Đúng bài `RM-09`, và lần này bộ đếm sai
là **của chính em vừa viết**.

Cùng ngày còn một ca nữa: câu hỏi *«tập model được chọn có đổi không»* ra **1/281** rồi
**0/281**. Chênh do **thứ tự đầu vào phá hoà** trong phép sắp xếp ổn định — artefact của cách đo,
không phải hành vi. Phải đổi sang **đếm cặp đảo chiều** mới ra con số đứng vững.

---

## `FU-404` — sổ chỉ sai đường, và chỉ dump mới biết

Sổ ghi *«`CTX-18.3` CÓ khối `[V2-RULES]`»* và trích chuỗi `HR12W 1.0 (n=20)`.

Dump prompt production ba miền: **chuỗi `HR12W` xuất hiện 0 lần.**

Vì `[V2-RULES]` nằm ở `_v10781_context_pack_v2.py`, mà **chính tệp đó tự khai ở dòng 26**:
*«Chỉ `_v10781_prompt_v2_lane.py` (cron riêng) dùng nó»* — một **lane A/B**. `CTX-18.3` thật ra
ở `gpt_analyzer.py:844`.

Tin sổ mà không dump thì đã đi sửa một tệp **không ai chạy**, rồi báo cáo *«đã sửa`*.

Và vế *«trạng thái ngoài mẫu»* mà sổ đòi thêm thì **đã có sẵn từ trước** ở `:4805`. Phần thiếu
thật là **lợi thế trên nền**.

### Lỗi thật nặng hơn sổ mô tả

Sổ nói *«nói quá»*. Đo ra thì có lúc **nói ngược**:

```
MN/Hà Nội   G6+G7  → prompt hiển thị HR12W = 1.0 → lợi thế thật −3,88%  KÉM NỀN
MN/Nam Định G1+G7  → prompt hiển thị HR12W = 1.0 → lợi thế thật −1,62%  KÉM NỀN
```

**13/105 luật dưới nền.** Và `1.0` gần **mức sàn** chứ không phải đỉnh: `HR12W` đếm *«tuần đó có
ít nhất MỘT trong 3–4 số trúng»* nên **105/105 luật đều đạt ≥ 40%**.

---

## Một dòng diff không giải thích được, và nó dẫn tới phát hiện lớn nhất phiên

So prompt TRƯỚC/SAU thấy một dòng đổi mà bản vá **không đụng tới**.

Có thể cho qua — nó nhỏ, và bản vá thì rõ ràng đúng. Nhưng một dòng không giải thích được nghĩa
là **em chưa hiểu thứ mình vừa sửa**.

```
hai lần chạy CÙNG MÃ:      MN 6 dòng khác · MT 6 dòng khác · MB 2 dòng khác
đặt PYTHONHASHSEED=0:      MN 0          · MT 0          · MB 0
```

**Prompt production đổi nội dung theo hạt băm chuỗi của từng tiến trình Python.**

Gốc ở `gpt_analyzer.py:5941`: `sorted(candidate_tails.items(), key=lambda x: -x[1])[:10]` —
sắp xếp **không phá hoà bằng khoá**, rồi `[:10]` và `[:6]` **cắt**.

Và đây là chỗ nó thành nghiêm trọng: **MT có 2/3 đuôi hoà điểm đúng ở hai vị trí đầu**, MB có
5/6 đuôi trong nhóm hoà gồm cả top-2. Nên **số nào model nhìn thấy trước tiên là do hạt băm**.

Nghĩa là mọi phép đo prompt A/B của dự án — **kể cả `FU-284` đo ba miền suốt 12 ngày** — đang có
nhiễu này chồng lên tín hiệu, và **chưa ai từng trừ nó ra**.

Vá chỉ **một dòng**. Nhưng hôm nay prompt đã đổi vì `FU-404`, thêm biến thứ hai là đúng vết
`QD-018` — nên để owner quyết.

---

## `FU-394` — mục treo suốt vì một điều không có thật

Mục này treo vì tin `×0,3` đang dìm số gan cao, *«ngược thiết kế owner»*.

`analyze_gan()` trả dict **bốn khoá**; số nằm ở tầng trong `gan_data['gan'][num]['gan_days']`.
Nhưng bộ lọc đọc `gan_data.get(num, 0)` ⇒ **luôn 0** ⇒ `if gan_days <= 8` **luôn đúng** ⇒
**`×0,3` không bao giờ tới**.

Đo xác nhận: nhóm `COLD + gan>8` = **0 số cả ba miền**, trong khi MB thật sự có `75`:15 ngày ·
`98`:15 · `01`:14, và **`01` đúng là `COLD`**.

Quét cả họ lỗi thì chỗ thứ hai nặng hơn: `post_filter.py:120` cùng lỗi, làm **toàn bộ nhánh thay
số `COLD` → `HOT/WARM` chưa từng chạy**. Hàm này gọi từ `main.py:8637` và `scheduler.py` — đường
production sống.

Và chi tiết xảo quyệt nhất: nhật ký in `«COLD nhưng GAN=0d (≤10), giữ lại»`. Dòng log đó **đọc
như bằng chứng cơ chế đang chạy**. Thật ra nó là bằng chứng cơ chế **đang hỏng**.

Vá = **kích hoạt hai cơ chế ngủ đông trên production**, trong đó một cơ chế chính là thứ owner
gọi là ngược. Nên không vá — ba lối, owner chọn.

---

## `FU-290A` — số lật ngược cả phép cắt

| | |
|---|---|
| biên tới mốc chốt | **≈220 phút** |
| lượt chậm nhất từng ghi nhận | **23,8 phút** = 10,8% biên |
| `p95` của model chậm nhất | **1,6% biên** |

Và lượt `p95 > biên`: `glm-5.1` **1/90** — nhưng `deepseek-reasoner` (TB chỉ 142s) cũng **1/90**,
`gpt-oss-120b` (TB chỉ 108s) cũng **1/92**. Con số 1 là **nền**.

⇒ **cắt model để cứu mốc giờ là cứu một thứ chưa từng bị đe doạ.**

Thêm hai điều thước cũ `TB > 180s` không thấy: `gpt-5.4` **nhanh nhất hệ** (15,9s) nhưng ở trên
đường tới hạn **97,8%** lượt, còn `gpt-5.5` chậm (170s) thì **0%** — hai trục khác nhau. Và
ngưỡng ấy sẽ cắt ba model, **hai trong ba không mua được gì**.

---

## K8 — và một lỗi em tự tạo trong chính phiên này

Miễn trừ `QD-066` hết hạn hôm nay. `QD-066` giữ `FU-360` mở vì *«ngày nó gặp va chạm thật là
21/08 khi `QD-015/016/017` chạy»*.

Kiểm: ba quyết định ấy vẫn **`ACTIVE`, hạn 08/08, quá hạn 13 ngày, chưa chạy**. Va chạm **không
xảy ra hôm nay**. Nên neo `FU-360` theo **sự kiện** thay vì theo ngày — giữ bằng một ngày trên
lịch là *«đặt hạn cho có»*.

`FU-389` thì đóng được: nó không còn gì treo về kỹ thuật, ở lại sổ **chỉ vì cái nhãn**.

Rồi chạy K8 lại thì nó **trượt** — vì **ba mục hôm nay mang nhãn `CODE_PUSHED`**, một nhãn tầng
của `RM-12` mà bộ đọc **chưa từng được khai**. Ba mục lập tức thành mồ côi, và cổng trượt **ngay
trong phiên vừa tạo ra chúng** — đúng gốc bệnh V10980.

Khai vào `TREO_STATUSES`, chiều an toàn. Khác hẳn ca `DEPLOYED_LIVE_VERIFIED` mà `QD-066` để dành
cho owner: nhãn đó đẩy 6 mục sang ĐÓNG (chiều rủi ro).

---

## Không deploy — và đó là quyết định, không phải quên

MN **đã chốt bundle lúc 05:20 sáng nay**.

Deploy bây giờ ⇒ MN chạy prompt **cũ**, MT/MB chạy prompt **mới**. Một **ngày lai** — đúng thứ
nhiễu đã giết cửa sổ đo `FU-284`, thứ mà cả ngày hôm nay em đang cố tránh.

Đề nghị deploy **sau 18:15 tối nay**, để **22/08 là ngày sạch đầu tiên** của `CTX-18.4`.

---

## Một câu em nói sai, và đính chính ngay

Giữa phiên em báo mệnh lệnh `SCAN 12W … HR12W >= 40%` nằm ở **đường chính thức**.

Đọc tiếp thì nó nằm trong `if shadow_mode:` (`gpt_analyzer.py:5550`), có chú thích ngay trên đầu:
*«Production path: shadow_mode=False → this block is skipped entirely»*.

Phép đo **105/105 đạt · 0/105 bị hạ** vẫn đúng — nhưng nó nói về **cổng shadow PB-18.0**, không
phải prompt production. Đính chính trước khi con số ấy đi vào bất kỳ kết luận nào.

---

## Điều em nghĩ đáng nói nhất về hôm nay

Sáu chỗ `DOC_SAID ≠ CODE_DID` trong một phiên. Ba chỗ sai vì **số dòng đã trôi**, ba chỗ
**chưa bao giờ đúng**.

Không chỗ nào lộ ra khi đọc tài liệu. **Tất cả chỉ lộ khi chạy mã thật.**

Sổ theo dõi của dự án ghi kết luận **kèm đường dẫn** — đó là điểm mạnh, vì nó cho phép truy lại.
Nhưng đường dẫn ấy **không ai kiểm lại khi mã đổi**, nên càng để lâu, cái kèm theo càng thành
cái dẫn sai. Ba mục hôm nay (`FU-380` `FU-397b` `FU-404`) đều có số dòng sai trong sổ.

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11095.md` — bốn việc owner cần quyết
(**deploy khi nào** · `FU-290A` · `FU-394` · `FU-416`), và hai cảnh báo:
**K8 sẽ đỏ từ 22/08 (CỐ Ý)** và **`QD-015/016/017` quá hạn 13 ngày**.
