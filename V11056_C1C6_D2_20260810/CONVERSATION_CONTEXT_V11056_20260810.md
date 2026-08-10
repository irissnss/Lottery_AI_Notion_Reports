# CONVERSATION CONTEXT — V11056 · 10/08/2026 chiều

## Owner nói gì (NGUYÊN VĂN, 12:52)

> *«① ĐO khả thi D-2 cho MN (anh mới đề xuất trong tài liệu, CHƯA có chứng minh) · ② làm rõ LUÔN
> toàn bộ mục CHƯA RÕ (C1–C6) rồi chốt một lượt · ③ LUẬT MỚI: NGUỒN BA LỚP.»*

> *«MỌI báo cáo phải có mục riêng ghi nhận các trao đổi trong phiên chat/IDE, phân tách ba lớp
> nguồn… anh trao đổi trực tiếp trong IDE nhanh hơn TanPhatAI theo kịp — báo cáo phải đủ để
> TanPhatAI đọc là biết phải đồng bộ/hỗ trợ gì.»*

> *«"đúng theo tài liệu" ≠ "có giá trị đo được". PHẢI ĐO TRƯỚC.»*

---

## Câu chỉ đạo hay nhất phiên này, và vì sao

*«anh mới đề xuất trong tài liệu, CHƯA có chứng minh»* — owner **tự nghi ngờ đề xuất của chính
mình** và bắt đo trước khi agent sửa mã cho khớp.

Đó là chỗ agent chắc chắn sẽ ngã nếu không bị chặn. Khuôn phản xạ là: *tài liệu owner khoá có vế
`D-2`, mã thiếu vế đó ⇒ mã sai ⇒ sửa mã*. Đo xong thì hoá ra vế `D-2` **đóng góp riêng 1,9% ứng
viên**, và sửa cho khớp tài liệu là **làm hệ loãng đi một cách có căn cứ**.

Và trong lúc đo thì lộ ra ba tầng lệch — đúng thứ luật §62 vừa ký sinh ra để bắt.

---

## Agent tự khai: mã trích sai, và đã nhân nó ra 5 tệp trong cùng buổi sáng

Sổ V11054 (viết hôm qua) ghi công thức của owner là **`V105.19 §7`**. Sai. Công thức thật ở
**`V105.5`** — `docs/CURRENT_TRUTH_SSOT.md:7252`, cột cuối ghi *«Owner formula clarification
2026-05-10 11:22 VN»*. `V105.19` là *Hard Stabilization Night Pass*, **không hề có** công thức
cross-region nào.

Nặng hơn: **sáng nay**, khi viết luật §62, agent lấy chính mã trích sai đó làm **ví dụ minh hoạ**
cho mục *«OWNER_SAID ≠ CODE_DID»* và **nhân nó vào 5 tệp governance** (`CLAUDE.md` ·
`.Antigravityrules.md` · `.AGENT.md` · và hai mặt sinh `AGENTS.md`/`GEMINI.md`).

Nó bị bắt theo một đường vòng đáng chú ý: điều tra viên D-2 báo *«V105.19 §7 KHÔNG TỒN TẠI»*,
phản biện viên phản bác *«có tồn tại, nằm ở ba mặt governance»* — **và ba mặt đó chính là ba tệp
agent vừa sửa vài giờ trước**. Phản biện đang trích lại chữ của chính agent làm bằng chứng cho
sự tồn tại của nó. Vòng lặp tự xác nhận.

Đã sửa hết trong cùng phiên, và ghi **banner đính chính có TRƯỚC/SAU** vào sổ V11054 thay vì sửa
lén.

---

## Mô tả M2 cũng sai bản chất, không chỉ sai mã trích

Sổ V11054 viết *«RR §9 thiếu D-2 ⇒ mã thiếu»*. Thực tế: vế `D-2` **CÓ được thi hành**, ở hai chỗ:

- `_v101_shadow_pilot.materialize_mn_cross_region_rule` — `method_version =
  v101_mn_cross_region_d1_d2_v1`, **3.991 dòng / 133 ngày**, và docstring của nó ghi thẳng
  *«never target_date actuals»* (tức đã phòng bẫy nhìn trộm từ đầu)
- `gpt_analyzer.py:6090` — dựng khối `D-2` cho MN

Nhưng **cả hai đều nằm sau cổng `lane_test_shadow_pack`**, chỉ bật từ `shadow_auto_eval`. Nên
`/du-doan` official chưa bao giờ thấy vế `D-2`.

«Mã thiếu» và «mã có nhưng chỉ chạy ở lane shadow» là hai chẩn đoán khác hẳn nhau, dẫn tới hai
hành động khác hẳn nhau.

---

## Điều may mắn: bảng shadow đó cho phép đo THẲNG thay vì mô phỏng

Vì `v101_mn_cross_region_rule_shadow` tách riêng `d1_occurrences` và `d2_occurrences` cho **từng
ứng viên**, nên trả lời được đúng câu hỏi gốc mà không cần proxy nào:

| nhóm | trúng | tỉ lệ | nền 43,2% |
|---|---|---|---|
| CHỈ D-1 | 163/358 | 45,5% | +2,3pp |
| cả hai | 1559/3558 | 43,8% | +0,6pp |
| **CHỈ D-2** | **34/75** | 45,3% | +2,1pp |

**75/3.991 = 1,9%.** Đó là toàn bộ phần vế `D-2` đóng góp riêng trong 133 ngày.

Điểm phương pháp đáng ghi: `n=75` quá nhỏ để kết luận về **tỉ lệ** (RM-04), nhưng **tỉ trọng**
thì kết luận được, và tỉ trọng mới là thứ quyết định ở đây. RM-04 cấm cái thứ nhất, không cấm
cái thứ hai — trộn hai chuyện đó lại là cách dễ nhất để hoặc kết luận bừa, hoặc tê liệt không
dám kết luận gì.

---

## Tầng phản biện đã cứu hai nhãn sai

Chạy 7 điều tra viên rồi cho mỗi kết quả một **phản biện viên có nhiệm vụ BÁC BỎ**, không phải
đồng ý. Kết quả: **hai nhãn `ĐÃ RÕ` bị lật**.

**C4** — điều tra viên kết luận `VERIFIED` dựa vào *«4/4 phép kiểm ĐẠT»*. Phản biện đọc thẳng
`_v10864_deploy.py`:
- hai trong bốn phép là **tautology**: `'.v50-kv {' in t and 'min-width: 0' in t` là **hai phép
  `in` độc lập trên toàn tệp**, không ràng buộc thứ này nằm trong thứ kia — **không thể thất bại**
- `journal 0` là **hằng số viết cứng** `"journal_errors": 0,` ở dòng 99
- `md5` trong tệp kết quả là bam của **tệp LOCAL**, không phải bam đọc về từ VPS
- ba dòng evidence được trích thuộc **`FU-V10863`**, không phải `FU-V10864`

**C5** — điều tra viên kết luận *«bản đang chạy là SP-4.4 nguyên vẹn»*. Phản biện: đúng ở **tầng
tệp**, nhưng **chuỗi gửi cho model ≠ chuỗi trong tệp** — đường phục vụ thật ráp ở
`gpt_analyzer.py:6317`. Và mọi con số ký tự đều đo trên **lát cắt mã nguồn** chứ không đo chuỗi
prompt (RM-14). Phản biện còn tìm ra **một commit bị bỏ sót** (`bf910d6`, 06/08 22:12).

---

## Vấp lặt vặt

- Heredoc bash lồng nháy đơn trong nội dung tiếng Việt bị nát ⇒ chuyển sang ghi tệp bằng công cụ
  Write rồi mới chạy.
- `str.replace` với `\n` khớp **0 lần** trên `main.py` — kho dùng **CRLF**. Bẫy này sập lần thứ
  bảy trong ba ngày; nay mọi bộ kiểm mới đều đọc `newline=""` rồi bỏ `\r`.
- Kết quả workflow trả về là **dict** chứ không phải list, phải lấy khoá `["result"]` — mất một
  vòng thử.

---

## Trạng thái cuối phiên

Production **không đổi**: PID `1286954` · health 200 · hash 4 bảng khoá nguyên · không deploy,
không restart. `QD-041` nguyên vẹn.

**Còn treo có hạn:** `FU-360` chốt hay rollback **sáng 11/08** · `FU-265` hạn **12/08** ·
`FU-284` chốt **20/08** · mở khoá **21/08**.

TanPhatAI cần làm: xem mục cuối của `REPORT_V11056.md` — bốn việc, gồm ghi `QD-056`, đính chính
mã trích `V105.19 §7` → `V105.5`, ghi verdict `D-2 = KHÔNG_KHẢ_THI` để không đưa vào gói 21/08,
và theo dõi `FU-360` sáng 11/08.
