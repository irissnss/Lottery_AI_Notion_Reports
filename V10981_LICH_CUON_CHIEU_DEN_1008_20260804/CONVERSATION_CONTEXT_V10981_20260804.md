# NGỮ CẢNH PHIÊN V10981 — 04/08/2026 (giờ Việt Nam)

> Ghi theo §57.2 (A55.2): **nguyên văn** lời owner + agent làm gì + vấp ở đâu.
> Không diễn giải lại lời owner.

---

## 1. Nguyên văn lời owner trong phiên

### 10:29 — quyết định chính của phiên

> "Giãn ra cuốn chiếu tới hết ngày 10/08 phải hoàn thành, làm lần lượt những vấn đề nào xác
> thực rõ ràng , đơn giản làm trước tới cuối cùng 10/08 phải xong"

Bối cảnh: kiểm toán toàn diện đầu ngày (**V10980**, chạy 09:52–10:20) báo **14 mục theo dõi
cùng đáo hạn 08/08** — đúng ngày hết đóng băng `QD-014` — trong đó **5 mục** mang nhãn chờ
owner (`OWNER_LOCK` / `AWAITING_OWNER_OK`). Agent trình hai lựa chọn **"giãn ra hay giữ
nguyên"**. Owner chọn **giãn ra**.

Mười bốn mục đó: `FU-186` `FU-187` `FU-191` `FU-192` `FU-193` `FU-203` `FU-207` `FU-210`
`FU-212` `FU-215` `FU-216` `FU-217` `FU-226` `FU-231`.

### Bốn ràng buộc đọc thẳng từ câu owner nói

| Ràng buộc | Trích nguyên văn |
|---|---|
| Trải ra theo ngày, không dồn | *"Giãn ra cuốn chiếu"* |
| Hạn chót tuyệt đối | *"tới hết ngày 10/08 phải hoàn thành"* · *"tới cuối cùng 10/08 phải xong"* |
| Tuần tự, không chạy song song | *"làm lần lượt"* |
| Thứ tự ưu tiên | *"những vấn đề nào xác thực rõ ràng , đơn giản làm trước"* |

---

## 2. Lời owner đã ký TRƯỚC phiên này mà phiên này phải tuân — tra ra, không hỏi lại

Theo §56 (tra cứu trước khi hỏi), agent tra `docs/OWNER_DECISION_LEDGER.md` trước khi định
trình câu hỏi nào cho owner. Kết quả tra được — tất cả đều là **nguyên văn owner**:

### QD-014 (02/08) — đóng băng đường ra số tới hết 08/08

> "Có. Hôm qua đổi ba thứ cùng lúc, cần một tuần yên để biết chúng có tác dụng gì không."

Phạm vi cấm: đổi danh sách 15 model official · đổi bộ lọc/hằng số combo-super · bật hoặc tắt
lớp ghi đè. Vẫn được: sửa lỗi kỹ thuật rõ ràng, điều tra chỉ-đọc, viết tài liệu.
**Đây là ràng buộc quyết định toàn bộ hình dạng lịch.**

### QD-015 (02/08) — shadow MT random-forest đơn

> "Có. Duyệt trước để 08/08 tự chạy, kèm chốt tự cắt nếu tỉ lệ khớp dưới 95% trong 7 ngày đầu."

Theo dõi bằng `FU-216`. **Owner đã ký rồi — không được hỏi lại.**

### QD-016 (02/08) — bỏ ép RULES-FIRST trên luồng bóng

> "Duyệt trước: sau 08/08 bỏ lệnh 'bắt buộc chọn từ danh sách' trên luồng bóng để đo — vẫn đưa
> danh sách như gợi ý, chỉ bỏ chữ bắt buộc."

Theo dõi bằng `FU-231`. **Owner đã ký rồi — không được hỏi lại.**

### QD-017 (02/08) — A/B hai prompt trên cùng model

> "Có, duyệt trước để 08/08 tự chạy. Chọn vài model đại diện, chạy ≥ 14 ngày, đo bằng bạch thủ."

Theo dõi bằng `FU-226`. **Owner đã ký rồi — không được hỏi lại.**

### QD-018 (02/08) — sau đóng băng làm đúng ba bước, từng cái một

> "Tắt bộ tối ưu trọng số (đang làm tệ đi) · đo xem 105 luật có giúp gì không · gỡ lệnh bắt
> buộc chọn từ danh sách. Làm từng cái một để biết cái nào ăn thua."

Mỗi bước đo 7–14 ngày. Chuỗi này **tự nó đã vượt 10/08 theo chính chữ ký owner** (B1 sớm nhất
09/08, B2 ~05/09, B3 ~19/09) nên KHÔNG tính vào nhóm 14.

### QD-013 (01/08) — dừng đặt tiền thật

> "Dừng đặt tiền thật. Giữ hệ chạy để đo, chỉ tốn token. Đặt lại khi nào chứng minh được lợi thế."

Vẫn đóng. Mọi mục shadow trong lịch **chỉ đo, không đặt tiền**.

### QD-019 (02/08) — quy ước mã công việc phương án B

> "Số hiệu phải viết tắt đầu mục công việc và hạn ngày, ví dụ Kiểm Soát 08/08 thì số hiệu viết
> tắt phải viết là TH0808 chẳng hạn, thế dễ đọc hơn."

Mọi mã đọc mới trong phiên này theo quy ước đó.

---

## 3. Agent đã làm gì, theo thứ tự

| # | Việc | Kết quả |
|---|---|---|
| 1 | Chạy `_v10920_session_start.py` (bắt buộc đầu phiên) | 0 checkpoint quá hạn · 98 mục treo · 1 quá hạn (`FU-225`) · **19 mục mồ côi** |
| 2 | Đọc chi tiết 14 mục bằng bộ đọc chuẩn `_v10958_fu_reader` | Không tự viết parser mới; lấy bản gần đầu file làm sự thật |
| 3 | Đọc `OWNER_DECISION_LEDGER.md` QD-013 → QD-019 | Phát hiện 3/5 mục "chờ owner" thật ra đã ký |
| 4 | Quét **mọi** mục có hạn ≤ 10/08, không chỉ nhóm 14 | 32 mục treo + 4 mồ côi — để lịch không đụng ngày đã kẹt |
| 5 | Quét 167 mã đọc §58 đang dùng | Tránh cấp trùng; phát hiện kho dùng **MMDD** chứ không phải DDMM |
| 6 | Soi `git show` hai commit của phiên V10979 chạy song song | Biết họ vừa thêm `FU-260/261/262`; đưa vào bảng tải ngày |
| 7 | Dựng `_v10981_lich.py` làm nguồn sự thật duy nhất | Sổ + trang + cổng + báo cáo đều sinh từ một chỗ |
| 8 | Dựng cổng `_v10981_kiem_lich.py` (7 phép) và **chạy TRƯỚC khi sửa sổ** | **Trượt K4** — chứng minh cổng bắt được lỗi thật |
| 9 | `prepend()` 14 mục hạn mới vào `FOLLOW_UP_TRACKER.md` | 1.018.092 → 1.034.263 ký tự |
| 10 | Chạy lại cổng | **7/7 ĐẠT** |
| 11 | Cập nhật CP-L6 trong `ACTIVE_ROADMAP_LEAN_HARVEST` | Việc không mồ côi |
| 12 | Sinh `docs/LICH_CUON_CHIEU_DEN_10082026.md` | Trang owner nhìn phát hiểu |
| 13 | Ghi `QD-021` vào sổ quyết định, chạy bộ kiểm | **Khớp 5/5** · toàn sổ 23 quyết định **0 TRÔI** |
| 14 | `prepend()` CHANGELOG + SSOT, bump `governance_seq` 390→391 | Khối V10979/V10980b còn nguyên |
| 15 | Viết báo cáo công khai + bằng chứng, push riêng + công khai | §57.2 |

---

## 4. Vấp ở đâu

### 4.1 PowerShell 5 không nhận `&&`

Hai lệnh đầu tiên hỏng ngay:

```
The token '&&' is not a valid statement separator in this version.
```

Chuyển sang `;`. Nhỏ, nhưng đáng ghi: nếu quen tay dùng `&&` trong script deploy thì vế thứ hai
âm thầm không chạy mà mã thoát vẫn 0.

### 4.2 Đọc `artifacts/` bằng công cụ đọc file bị chặn

`Permission denied` khi đọc `artifacts/_v10981_14muc.txt`. Chuyển sang in thẳng ra màn hình.
Không ảnh hưởng kết quả.

### 4.3 `FU-212` lệch nhãn hạn — lỗi thật, đã sửa

Tiêu đề ghi `hạn LX` (không hạn) nhưng ô `due` trong bảng ghi `2026-08-08`. Bộ đọc lấy ô `due`
nên máy vẫn đếm nó vào nhóm 08/08, còn người đọc tiêu đề tưởng nó không có hạn nên không ai
đụng. **Hậu quả nếu bỏ qua:** đúng loại lỗi làm việc trôi âm thầm — hai bên cùng "đúng" mà lệch
nhau. Đã đồng bộ trong khối V10981.

### 4.4 §58 viết `DDMM`, kho thực tế dùng `MMDD`

Bằng chứng: `FU-243 · SC0805 · hạn 05/08` · `FU-258 · KS0806-1 · hạn 06/08` ·
`FU-261 · QD0809 · hạn 09/08` · `QD-018 · HT0822 · hạn 22/08`. Hai mục lệch chuẩn
(`FU-252 · KS1008`, `FU-253 · SC1008`) thuộc phiên khác, chỉ ghi nhận chứ không sửa.
**Hậu quả nếu bỏ qua:** theo đúng chữ trong §58 sẽ sinh dị bản thứ ba và mọi mã mới đọc ngược
so với 160+ mã đang có. Đã theo cách kho dùng.

### 4.5 Suýt vi phạm §56 — hỏi owner thứ đã ký

Nhóm 14 có 5 mục nhãn chờ owner. Nếu chỉ nhìn nhãn thì trình owner 5 câu hỏi. Tra sổ mới thấy
`FU-216` / `FU-226` / `FU-231` đã ký từ 02/08 ở `QD-015` / `QD-017` / `QD-016` — chúng chờ
**ngày 08/08**, không chờ chữ ký. **Hậu quả nếu bỏ qua:**
`A54_VIOLATION_ASKED_WITHOUT_LOOKUP`, đúng cái owner đã phải nhắc ngày 01/08. Cuối cùng chỉ
trình **3 câu hỏi thật**.

### 4.6 Ngày 10/08 vẫn nghẽn 11 mục — nói thẳng, không giấu

Nhóm 14 cố ý chỉ đặt 2 mục vào 10/08, nhưng ngày đó đã có sẵn **9 mục** hạn từ V10974–V10980
(`FU-185` `FU-188` `FU-223` `FU-244` `FU-252` `FU-253` `FU-254` `FU-255` `FU-257`).
**Hậu quả nếu bỏ qua:** owner tưởng đã giãn xong mà ngày chót vẫn vỡ. Agent **không tự ý dời
hạn của phiên khác** — ghi rõ trong trang lịch §1 để owner quyết.

### 4.7 Phiên V10979 chạy song song cùng chạm 4 file tài liệu chung

`FOLLOW_UP_TRACKER.md` · `OWNER_DECISION_LEDGER.json` · `CHANGELOG.md` ·
`CURRENT_TRUTH_SSOT.md`. **Hậu quả nếu bỏ qua:** ghi đè mất việc của một trong hai phiên — lỗi
đã xảy ra thật ngày 31/07 (xoá sạch 905 KB SSOT). Cách tránh đã áp dụng:

- chỉ dùng `_doc_prepend.prepend()` (đọc xong mới ghi, từ chối nếu file ngắn đi) và
  `os.replace` qua file tạm;
- **đọc lại file ngay trước mỗi lần ghi**;
- `assert` khối của phiên kia (`FU-260/261/262`, `QD-020`, `V10979`, `V10980b`) còn nguyên
  **sau** khi ghi — nếu mất thì dừng ngay;
- chỉ `git add` đúng file của mình, **không** `git add -A` / `git add .`.

Kết quả kiểm: **tất cả khối của V10979 còn nguyên.**

---

## 5. Ranh giới agent tự đặt cho phiên này

**Không làm** (dù có thể làm được):

- Không deploy, không restart service, không đụng crontab.
- Không sửa 15 model official / bộ lọc combo-super / lớp ghi đè / `/du-doan` /
  writer `final_bundles` / bộ chọn model production — `QD-014` còn hiệu lực tới hết 08/08.
- Không dời hạn của mục thuộc phiên khác, kể cả khi làm vậy sẽ khiến ngày 10/08 nhẹ hơn.
- Không rút ngắn cửa sổ đo 7 ngày / 14 ngày để "kịp hạn 10/08".
- Không hỏi lại owner ba mục đã ký ở `QD-015` / `QD-016` / `QD-017`.

**Nói thẳng thay vì hứa:** 5/14 mục không thể kết luận trước 10/08. Với chúng, "xong" trong
cửa sổ này nghĩa là **chạy được và có ngày đo đầu tiên** — ngày kết luận thật là 15/08 (`FU-216`),
16/08 (`FU-217`, `FU-193`), 23/08 (`FU-231`, `FU-226`).
