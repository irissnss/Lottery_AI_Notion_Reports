# CONVERSATION CONTEXT — V11092 · 20/08/2026 đêm · đêm trước ngày mở gói

## Owner nói gì (NGUYÊN VĂN)

> **23:45 · 18/08** — *«① bầy đàn: XÁC NHẬN KHÔI PHỤC bảng 4 dòng (CHANGELOG:5128), giữ nguyên
> số. ② DEHERD: KÝ |chênh| ≥16,3pp VÀ |z| ≥1,96 VÀ n ≥63 (kèm ghi nhận phép đo yếu).»*

> **19:58 · 20/08** — *«③ D3: HOÃN (lối C)… ④ FU-290A: agent VIẾT THIẾT KẾ trước… ⑤ FU-284: ĐÓNG,
> ghi «cửa sổ 12 ngày không đủ sức», KHÔNG kéo dài vì sau 21/08 hệ đổi ⇒ số đo sẽ nhiễm.»*

> *«mọi chữ ký dưới đây ĐÃ TỒN TẠI, việc là GHI VÀO KHO»* · *«CẤM đổi bất kỳ con số nào»*

---

## Phiên này không có gì để quyết — và đó là điểm mạnh của nó

Owner đã ký hết. Việc của phiên là **ghi vào kho cho đúng**, và **đọc hai thước theo đúng ngưỡng
đã ký**.

Nghe như việc bàn giấy. Nhưng chính vì không phải quyết gì nên nó lộ ra ba thứ mà những phiên
bận rộn hơn đã bỏ qua.

---

## Thứ nhất — `QD-068` chưa từng tồn tại

Các báo cáo `V11082` → `V11091` đều gắn nhãn `quyet_dinh = "QD-068"`. **Bốn ngày**, sáu bản báo
cáo công khai.

Chạy cổng cấp số đầu phiên: *«cao nhất `QD-067` · **trống tiếp `QD-068`**»*.

Tức là sáu báo cáo đã tag một quyết định **không có trong sổ**. Không ai phát hiện, vì cổng
`_v11044` chỉ làm việc **cấp số** — nó không đối chiếu nhãn trong báo cáo với sổ quyết định.

Nay `QD-068` được lập thật, với **đủ năm chữ ký** và **5 phép `kiem_code`** máy kiểm được. Và
chỗ mù của cổng đã ghi vào theo dõi — nó vẫn còn.

---

## Thứ hai — BẦY ĐÀN **CÓ TÁC DỤNG**, và đây là kết quả dương duy nhất

Bước đầu tiên không phải đọc số, mà là **kiểm `giai_doan`**. Bẫy 07/08 đã sập một lần và nó vẫn
nằm trong dữ liệu:

```
NEN         n=64   phân tán TB 0,4739   17/07 → 07/08
SAU_V11016  n=37   phân tán TB 0,5815   07/08 → 19/08
HON_HOP     n= 1              0,6667    07/08   ← LOẠI khỏi cả hai trung bình
```

Đúng một lượt `HON_HOP`, đúng ngày 07/08 — chính là lượt từng bị gắn nhầm. Cơ chế phân loại theo
**mốc giờ** đang chạy đúng.

Ba điều kiện của bảng 4 dòng: `n=37 ≥ 9` ✓ · `0,5815 ≥ 0,50` ✓ · hơn nền `+0,1076 ≥ 0,05` ✓

**⇒ CÓ TÁC DỤNG.**

### Một xác nhận nhỏ nhưng quan trọng

Nền đo được là **`0,4739`**. Con số ghi trong ngưỡng đăng ký trước là **`0,47`**.

Chúng **khớp**. Nghĩa là ngưỡng và dữ liệu **cùng một nền** — không phải nền được vẽ lại sau khi
đã thấy kết quả. Nếu hai con số này lệch nhau đáng kể thì cả phán quyết sẽ phải xem lại.

### Và một điều phải nói ra dù nó làm kết quả bớt vui

**Ngưỡng bầy đàn KHÔNG có vế `z`.** Khác hẳn `FU-284` (đòi `|z| ≥ 1,96`) và DEHERD (cũng đòi).

Nó là **ngưỡng thực dụng**: *«phân tán có cao hơn nền không»*. Không phải phép kiểm ý nghĩa thống
kê. `CÓ TÁC DỤNG` ở đây nghĩa là **vượt ngưỡng đã chốt trước**, **không** nghĩa là *«đã chứng minh
bằng thống kê»*.

Ghi ra vì đây là kết quả dương duy nhất trong bốn ô — và chính vì hiếm nên nó dễ bị đọc quá lên.

---

## Thứ ba — DEHERD trượt cả ba vế

```
n = 60          < 63      (thiếu 3 — một ngày trống trong cửa sổ 21 ngày)
|chênh| = 6,67pp < 16,3
|z| = 1,155      < 1,96
```

DEHERD `20/60 = 33,3%` · official `24/60 = 40,0%` · McNemar `b=8` `c=4` hoà `48`.

Hướng là DEHERD **kém hơn**. Nhưng `6,67pp` nằm **sâu trong vùng nhiễu** của một phép đo chỉ thấy
được `≥16,3pp`.

**Nghĩa là cửa sổ ngắn, không phải DEHERD vô dụng** — và owner đã ký **kèm ghi nhận này** từ
18/08, tức biết trước khả năng cao sẽ ra như vậy.

---

## Một chỗ cổng chặn đúng, và cách xử đúng là **không đi vòng**

Commit `GĐ-2/3` bị `_v11062` chặn: *«`V11092` KHÔNG có dòng `HISTORY`»*.

Phản xạ quen thuộc — và đã dùng nhiều lần trong các phiên trước — là đặt `BO_QUA_CONG_COMMIT=1`
kèm lý do.

Nhưng lần này cổng **nói đúng**: bốn mặt chưa đi cùng nhau, và đó chính là thứ `§63` sinh ra để
chặn. Nâng bốn mặt **trước**, cổng **ĐẠT thật**, commit qua bình thường.

**Lần đầu trong nhiều phiên không phải dùng cờ bỏ qua.** Đáng ghi, vì cờ bỏ qua dùng nhiều lần
sẽ thành thói quen, và thói quen đó làm cổng mất nghĩa.

---

## Gói 21/08 — chốt lại lần cuối

Từ **14 mục** ban đầu:

```
#13 GĐ2 dịch ngữ cảnh   ⛔ RA — FU-284 không cho phép (đọc 20/08)
#3  D3 gỡ RR §11+§18    ⛔ RA — hoãn lối C, 5 chỗ dangling → FU-411
#8  FU-290A             ⚠ đổi tính chất: từ "thi hành" thành "VIẾT THIẾT KẾ"
12 mục còn lại          giữ nguyên, thứ tự ba làn y nguyên
```

⇒ **12 mục thực thi + 1 việc thiết kế.**

Và bảng kiểm lên **10 bước**, với ba bước mới đều là thứ dễ quên nhất:
- **b2** chạy lại bộ chấm T-B **sau đồng bộ** (đồng bộ ghi đè DB ⇒ đọc thẳng thấy 0 cặp)
- **b8** `FU-290A` viết thiết kế + owner duyệt **trước** khi thi hành
- **b9** `FU-360`/`FU-389` — **miễn trừ K8 hết hạn 21/08**

---

## Trạng thái cuối phiên

Production **không đổi**. `QD-041` nguyên vẹn tới 21/08. Cổng đầy đủ xanh, và `_v11062` xanh
**thật** chứ không nhờ cờ bỏ qua.

**Bốn ô verdict đã đủ:** A `KHÔNG ĐẠT` · B `CHƯA KẾT LUẬN` · **C `CÓ TÁC DỤNG`** · D
`CHƯA KẾT LUẬN`.

Ba trên bốn ô ra *«chưa kết luận»* hoặc *«không đạt»* — và cả ba đều vì **cùng một lý do**: cửa
sổ đo quá ngắn so với hiệu ứng cần thấy. Đó không phải bốn thất bại riêng lẻ; đó là **một vấn đề
thiết kế phép đo**, lặp lại bốn lần.

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11092.md` — quan trọng nhất là ① **gói 21/08 chốt 12
mục + 1 thiết kế**, ② **bảng kiểm 10 bước** (đặc biệt b2 và b9), ③ **chỗ mù mới của `_v11044`**.
