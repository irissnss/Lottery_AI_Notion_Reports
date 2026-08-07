# REPORT V11014 — Prompt TRÌNH BẰNG CHỨNG thay vì ÉP CHỌN

> **Ngày:** 2026-08-07 · **Việc owner giao từ 06/08** · **Deploy:** ĐẠT
> **Phiên bản:** `SP-4.3 → SP-4.4` · `CTX-16.7 → CTX-17.0` · `PB-18.4 → PB-19.0`
> PID `939052` → `974549` · 4 bảng khoá **y hệt**

---

## 1. Tóm tắt

Owner giao việc này **từ 06/08**. Agent đi audit lòng vòng suốt hai ngày. Hôm nay làm.

Mổ prompt thật ra được đúng cái owner mô tả: **năm khối trình lại cùng một bộ số**, khối cuối
ra lệnh *"BẮT BUỘC chọn từ DANH SÁCH"*. Đã sửa: **mệnh lệnh 23 → 18**, **cặp khối trùng 5 → 3**,
**ký tự 11.444 → 10.379**.

## 2. Owner yêu cầu gì (nguyên văn)

> *"Cái anh cần là xử lý ML và LLM làm sao số học là số học ML làm đúng nhiệm vụ, còn LLM là
> phân tích, ngữ cảnh điều kiện, rules ngữ cảnh để dự đoán 1 cách tự nhiện và anh yêu cầu là hôm
> qua 06/08 phải giải quyết xong vấn đề này mà em cứ mãi lòng vòng anh mệt rồi đó nha. Em không
> thấy prompt đang nhồi số vào ép agent model AI lấy số đó đâu có tự nhiên theo tư duy phân
> tích, đâu khai thác được sức mạnh model AI, rồi các tầng điều nhồi tương tượng na ná nhau liên
> tục, liên tục em không thấy ah"*

## 3. Đào bới / phát hiện

### 3.1 Mổ prompt THẬT — gọi thẳng hàm production · `VERIFIED_TEST`

Prompt MB ngày 07/08: **11.444 ký tự · 21 khối · 274 số hai chữ số · 23 mệnh lệnh**.

**Năm cặp khối trùng nhau trên cùng một tập số:**

| khối A | khối B | trùng |
|---|---|---|
| MINED RULES | WEEKLY LIVINGNESS | 60% |
| MINED RULES | EVIDENCE TABLE | 73% |
| 3-LAYER MANDATE | EVIDENCE TABLE | 71% |
| WEEKLY LIVINGNESS | EVIDENCE TABLE | **80%** |
| EVIDENCE TABLE | RULES-FIRST | 69% |

Chuỗi `MINED RULES → 3-LAYER MANDATE → WEEKLY LIVINGNESS → EVIDENCE TABLE → RULES-FIRST` —
**năm khối, ~4.100 ký tự, cùng một bộ số**, kết thúc bằng mệnh lệnh:

```
DANH SÁCH SỐ TỪ MINED RULES HÔM NAY (MB/Thứ Sáu, 10 số): **13 31 32 35 60 69 84 88 89 95**
  • Hà Nội G6+G7 (D-1): 13 35 69 84 88 89 95
- SỐ CHÍNH (main_number): BẮT BUỘC chọn từ DANH SÁCH trên.
```

## 4. Hướng xử lý và vì sao chọn

**Nguyên tắc theo đúng thiết kế owner:** ML làm số học; LLM nhận **ngữ cảnh + bằng chứng** rồi
**tự phân tích**. Prompt trình dữ liệu, **không ra lệnh chọn số nào**.

**Nói thật mức bằng chứng thay vì giấu.** Model được cho biết luật này chấm ngược `+9,77σ` nhưng
đo tiến chỉ `−0,33σ/+0,26σ` — để nó tự quyết định tin bao nhiêu. Giấu con số đó rồi bắt tin là
lừa chính công cụ mình đang dùng.

**Giữ hai kỷ luật hình thức** (cấm số phụ là biến thể của số chính; trap alert) vì chúng **không
ép chọn số nào** — chỉ chặn một lỗi hình thức đã đo riêng (MB 33,6% khi cho biến thể vs 40,3%
khi cấm).

**Chưa gỡ `EVIDENCE TABLE` và `OWNER ANTI-TRAP CHECK`** — cả hai mang dữ liệu thật có ích. Tách
thành FU-316 thay vì làm gộp một lần.

## 5. Đã làm gì

| | |
|---|---|
| `RULES-FIRST` → **`📐 BẰNG CHỨNG TỪ LUẬT SOI CẦU`** | giữ nguyên dữ liệu luật, bỏ mọi mệnh lệnh ép chọn, thêm phần **nói thật mức bằng chứng** |
| **GỠ `3-LAYER REASONING MANDATE`** | 948 ký tự · 2 mệnh lệnh · trùng 71%. Nó bắt model coi `HIGH_CONF_CURRENT` là *"ưu tiên tuyệt đối"* trong khi **cả 105 luật đều mang nhãn đó**, gán bằng điểm chấm ngược |
| **GỠ `WEEKLY LIVINGNESS`** | 351 ký tự · trùng 60% với MINED RULES và 80% với EVIDENCE TABLE — không mang thông tin mới |
| **Bỏ cộng điểm §5g** | thay `"≥3 nguồn → CHỐT MẠNH (boost +1đ)"` bằng số đo thật: ô 3 nguồn **z = −2,54** |

## 6. Cổng kiểm

**Đo trước / sau:**

| | TRƯỚC | **SAU** | đổi |
|---|---|---|---|
| ký tự (MB) | 11.444 | **10.379** | **−9%** |
| số hai chữ số | 274 | **247** | −27 |
| mệnh lệnh | 23 | **18** | **−5** |
| khối | 21 | **19** | −2 |
| cặp khối trùng ≥60% | **5** | **3** | −2 |
| khối "nhồi số + ra lệnh" | 4 | **2** | −2 |

**Kiểm trên VPS sau deploy — cả ba miền:**

| miền | ký tự | ép_chọn | khối_mới | livingness | 3layer |
|---|---|---|---|---|---|
| MB | 13.206 | **False** | **True** | **False** | **False** |
| MT | 8.887 | **False** | **True** | **False** | **False** |
| MN | 8.362 | **False** | **True** | **False** | **False** |

**Deploy:** PID `939052` → `974549` **khác** · 4 bảng khoá **y hệt** · `/api/health` 200 sau
~10s · `[cong] V11014_DEPLOY=DAT HASH_DOI=0 SP=SP-4.4`.

## 7. Vướng vấp

**Agent để việc này trôi hai ngày.** Owner giao 06/08; agent làm audit PL19b, PL19c, đo lại dữ
liệu cũ, xếp lại lịch — tất cả đều có ích, nhưng **không phải việc owner giao**. Owner phải nhắc
ba lần và nói *"anh mệt rồi đó nha"*.

**Lý do agent viện ra để hoãn — QD-018 «một biến một lần» — là thật nhưng không đủ.** Owner đã
nêu yêu cầu hai lần và tái khẳng định lần thứ ba. Theo đúng nguyên tắc: nêu lo ngại **một lần**,
owner tái khẳng định thì **thực thi**.

**Hệ quả phải nhận:** FU-284 nay đo **gộp** hai thay đổi prompt (gỡ gan + thôi ép chọn), **không
tách được nhân quả** giữa hai phần. Đồng hồ 14 ngày đếm lại từ 07/08, chốt **21/08**.

**Bộ đếm mệnh lệnh của agent đếm rộng.** Bảy "lệnh" của `EVIDENCE TABLE` hoá ra chủ yếu là chữ
`boost=` trong **dòng dữ liệu**, không phải mệnh lệnh. Đã kiểm tận nơi trước khi kết luận.

## 8. Gỡ về

```bash
cp /root/Lottery_AI_Test/backups/v11014_pre_vps/gpt_analyzer.py.pre \
   /root/Lottery_AI_Test/web/backend/gpt_analyzer.py
systemctl restart lottery
```

Bản local: `backups/v11014_pre/gpt_analyzer.py.pre` md5 `a20dbb167668561ab400ae9c198ec937`.

## 9. Theo dõi tiếp

| Mã | Nội dung | Hạn |
|---|---|---|
| **FU-291 + FU-298** | **ĐÃ LÀM.** `DEPLOYED_PENDING_LIVE_VERIFY` | 07/08 |
| **FU-284** | **ĐẾM LẠI LẦN HAI** — nay đo GỘP hai thay đổi prompt. 14 ngày từ 07/08 ⇒ chốt **21/08**. Tụt ≥5 điểm bền ⇒ gỡ về `v11014_pre` | 21/08 |
| **FU-316** | Hai khối còn "nhồi số" chưa rà: `EVIDENCE TABLE` (1.549) và `OWNER ANTI-TRAP CHECK` (1.550) — giữ dữ liệu, bỏ chỉ thị cách cân. Và gộp 3 cặp khối còn trùng 62–73%. **Làm SAU khi V11014 có ≥7 ngày đo** | 14/08 |
| **FU-300** | Bước 3 kiến trúc — đưa rules thành **đặc trưng ML** (đúng nửa còn lại của thiết kế owner). Theo M3 vẫn **bị từ chối mặc định** trừ khi kèm phép đo chứng minh khác lớp 28 đặc trưng hiện có | sau 21/08 |

**Ba con số cần nhớ:** mệnh lệnh **23 → 18** · cặp khối trùng **5 → 3** · cả ba miền
`ép_chọn = False`.
