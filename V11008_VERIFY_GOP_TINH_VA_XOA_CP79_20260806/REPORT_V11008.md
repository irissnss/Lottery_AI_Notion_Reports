# REPORT V11008 — Verify 41 đài trước/sau gộp tỉnh · XOÁ HẲN CP-7.9 · đồng bộ trạng thái toàn trang

> **Ngày:** 2026-08-06 · **Mã việc:** FU-293 (đóng) · FU-295 · FU-296
> **Deploy:** ĐẠT — PID `937241` → `939052`, 4 bảng khoá **y hệt**
> **Phiên bản:** `RR-16.4 → RR-16.5` · `PB-18.3 → PB-18.4` · CP-7.9 **xoá hẳn**

---

## 1. Tóm tắt

Owner bắt **ba lỗi cẩu thả**, cả ba đều đúng:

1. **Trạng thái không nhất quán trong cùng một trang** — mục 03 ghi "xong" nhưng mục 08 vẫn đỏ
   "chờ owner chốt"; khối M4 vẫn ghi "việc còn lại là nối vào bộ đào luật" dù V11003 đã nối.
2. **Để việc dễ tới 13/08** — chuyện tên tỉnh gộp xác định dứt khoát ngay bằng dữ liệu đang có.
3. **Không nâng số hiệu** — sửa xong mà trang vẫn ghi V5.

Sửa cả ba. Và khi làm nghiêm phần (2) thì **tìm ra một thay đổi lịch xổ thật** mà bốn phép đo
hôm trước bỏ sót.

## 2. Owner yêu cầu gì (nguyên văn)

> *"trên xong dưới thì vẫn đỏ, không nhất quán gì cả"*

> *"xong chưa mà còn không cập nhật trạng thái. Nếu chờ anh xác nhận thì ghi chờ anh xác nhận
> xong thì ghi xong chỗ nào cũng đỏ hết rồi anh và em phải làm tới làm lui hoài ah"*

> *"như Lâm Đồng tại sao với khối lượng DB lớn như thế trước và sau gộp khác nhau như thế cái nào
> đã hay đổi em không nắm được hay sao mà phải hỏi xem kỹ cả 3 miền và các thứ lại đi verify từng
> thứ 1 cho từng miền 1 để xác định thay đổi cho thật kỹ càng chứ em xử lý chờ gì tới 13/08 hả
> trong khi cái đó xác định rất dễ với sự thông minh như em."*

> *"cái CP7-9 là gì nó có trùng với thông tin gì trong prompt hiện tại cần showlist và lên kế
> hoạch gộp tách loại bỏ để clear CP7-9 luôn, chắc chắn nếu đã nêu như thế thì sẽ có lưu trữ đo
> lường rồi."*

> *"Làm xong chả cập nhật nâng Version gì luôn ah vẫn là V5 là sao chả có thay đổi gì là sao?"*

> *"Ah nếu cẩu thả thế thì em nên xem lại hôm nay em đã làm gì và có sơ xuất gì không đó chứ anh
> thiếu tin tưởng em rồi đó nha"*

## 3. Đào bới / phát hiện

### 3.1 Verify TỪNG đài, TỪNG miền — và tìm ra thay đổi thật · `VERIFIED_TEST`

2.387 ngày dữ liệu, 13 tháng sau mốc gộp 01/07/2025 — thừa đủ để kết luận, không cần hỏi ai.

| | |
|---|---|
| Đài giữ nguyên hoàn toàn (tên · thứ · miền) | **40/41** |
| Đài có thay đổi | **1** — `Thừa Thiên Huế` |
| Đổi gì | **THÊM** ngày xổ **Chủ Nhật** từ **26/10/2025** (giữ nguyên T2) |
| `EXPECTED_STATION_COUNT` | đúng: MT/CN = 3 = Khánh Hòa + Kon Tum + Thừa Thiên Huế |
| Luật bị ảnh hưởng | 2 luật trỏ tới TTH, cả hai còn nguyên tác dụng |

**Bốn phép đo hôm trước bỏ sót chỗ này** vì chỉ nhìn 120 ngày gần nhất — cửa sổ đó nằm hoàn toàn
SAU khi thay đổi đã xảy ra, nên thấy "khớp 21/21" và tưởng không có gì. Phải mở cửa sổ ra
**trước** mốc mới thấy.

### 3.2 FU-293 giải xong, không cần owner quyết · `VERIFIED_TEST`

Mỗi **(tỉnh mới, miền, thứ)** trỏ tới **đúng một đài**:

| tên tỉnh mới | + miền/thứ | → đài thật |
|---|---|---|
| `Lâm Đồng` | MN/CN | **Đà Lạt** |
| `Lâm Đồng` | MN/T5 | **Bình Thuận** |
| `Lâm Đồng` | MT/T7 | **Đắk Nông** |
| `Khánh Hòa` | MT/T6 | **Ninh Thuận** |
| `TP. HCM` | MN/T3 | **Vũng Tàu** |
| `Hưng Yên` | MB/CN | **Thái Bình** |

Bảng `PHAN_GIAI_THEO_THU` **42 ô**, kiểm ngược với dữ liệu thật **0 sai**. Ba ô hai đài cùng thứ
(`Cần Thơ`/Sóc Trăng T4 · `Quảng Trị`/Quảng Bình T5 · `Vĩnh Long`/Trà Vinh T6) — cả ba lần tên
tỉnh mới **trùng tên một đài thành viên** nên đài trùng tên thắng. **Không còn ca nào bế tắc.**

Thiếu ngữ cảnh (chỉ có mỗi cái tên) thì **vẫn không đoán** — trả nguyên văn để cảnh gác bắt.

### 3.3 CP-7.9 — 7/8 khối trùng, 1 khối chỏi, 0 phép đo · `VERIFIED_CODE`

| mã | khối | có trong SP-4.3 / RR-16.5 đang chạy? | xử |
|---|---|---|---|
| C1 | Confidence ≥4 nguồn = CAO | **CHỎI** — V11001 đã hạ xuống ≥3 | **bỏ** |
| C2 | Anti-Overclaim | **MẤT 3/3 ý** | **cứu → RR §26** |
| C3 | Convergence contrarian | có — §23 AI-LEVEL ANTI-HERDING | bỏ |
| C4 | Rule-Aware Reasoning | có — khối RULES-FIRST | bỏ |
| C5 | Confidence discipline v7.7 | có — Strength + caveat | bỏ |
| C6 | Ensemble diversity v7.9 | có — §22 ANTI-HERDING ML | bỏ |
| C7 | MB discipline v7.9 | "thận trọng MB" có; **trần 52%/60% MẤT** | **cứu → RR §26** |
| C8 | Width discipline v7.9.1 | có — TOP1-FIRST V8.0 | bỏ |

**Phát hiện nặng hơn:** hai luật cứng **`H7`** (cấm nói quá) và **`H8`** (trần MB 52%/60%) trong
`.Antigravityrules.md` **đều ghi nguồn là `CORE_POLICY`** — lớp **chưa bao giờ tới model**.
Nghĩa là hai luật đó **chưa từng có hiệu lực thật**. Nay trỏ về **RR §26** nên mới ràng buộc.

**Về câu "chắc chắn sẽ có lưu trữ đo lường":** `predictions.policy_version_ref` = **0/0 dòng**.
**Không tồn tại và không thể tồn tại** phép đo hiệu quả nào cho CP-7.9 — nó chưa bao giờ được bơm.

## 4. Hướng xử lý và vì sao chọn

**Xoá CP-7.9 là an toàn tuyệt đối về hành vi** — lớp chưa bao giờ được bơm, xoá = 0 thay đổi
output. Nhưng **cứu C2 + trần MB sang RR §26 thì CÓ đổi prompt**. Chấp nhận vì:

- Khối §26 chỉ ràng buộc **cách nói** và **mức confidence khai ra**, **không đụng cách chọn số**.
- FU-284 đo **tỉ lệ trúng của con số** — khác kênh nhân quả, nên không nhiễu phép đo.
- Để nguyên nghĩa là hai luật cứng của dự án tiếp tục **có tên mà không có hiệu lực**.

**Giải tên tỉnh bằng (miền, thứ) thay vì hỏi owner** — dữ liệu đã đủ; hỏi là lãng phí thời gian
của owner. Thiếu ngữ cảnh thì vẫn không đoán.

## 5. Đã làm gì

`station_identity.py` thêm `PHAN_GIAI_THEO_THU` 42 ô + `canonical_station_by_context()` ·
`gpt_analyzer.py` xoá `CORE_POLICY`, thêm RR §26 · `prompt_registry.py` và
`_v87_master_board.py` dọn tham chiếu · `.Antigravityrules.md` H7/H8 trỏ về RR §26 ·
`docs/CP_7_9_LUU_TRU.md` lưu nguyên văn · trang phân tích sửa **17 chỗ** trạng thái, nâng
**V5 → V6**.

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `PROMPT_SACH` | **DAT** |
| `DONG_BANG` | **DAT** |
| `TEN_DAI` | **DAT** — 41 đài · 360 bí danh · 0 tên lạ |
| `M4_DOI_CHUNG` | **DAT** |
| Sổ quyết định | **không mục nào trôi** |
| Sáu mặt quy tắc | **đồng bộ** |
| Báo cáo công khai | **đủ, đã push** |

**Deploy:** PID `937241` → `939052` · 4 bảng khoá **y hệt** · `/api/health` 200 sau ~10s.
Cổng deploy kiểm thêm: `CP-7.9 còn trong code = 0` · `RR §26 CÓ` · bảng phân giải **42 ô** ·
`Lâm Đồng` MN/CN→Đà Lạt, MT/T7→Đắk Nông, thiếu ngữ cảnh→giữ nguyên văn.

**Trang:** HTML **0 lỗi cấu trúc** · 19 mục nav · **0 neo hỏng** · quét ngược **0 câu còn nói ở
thì chưa làm**.

## 7. Vướng vấp

**Ba lỗi cẩu thả owner bắt được — nhận đủ:**

| lỗi | vì sao xảy ra |
|---|---|
| Trạng thái lệch giữa các mục cùng trang | Sửa mục 03 mà **không quét ngược toàn trang** — đúng thứ `§60.3` vừa ký **cùng ngày** bắt phải làm |
| Để FU-293 tới 13/08 | Mặc định "cần owner quyết" mà **không thử tự giải trước**. Dữ liệu trả lời được trong vài phút |
| Không nâng số hiệu trang | Nâng nhãn nội bộ (V5.1) nhưng **quên `<title>`** — người đọc chỉ thấy tiêu đề |

**Vá vòng đầu để lại thẻ `<b>` mồ côi** — thay chuỗi `chờ owner chốt</b>` mà không thay thẻ mở.
Bộ kiểm cấu trúc HTML bắt được ngay, đã sửa.

**Bốn phép đo "gộp tỉnh không ảnh hưởng" hôm trước là ĐÚNG NHƯNG KHÔNG ĐỦ** — cửa sổ 120 ngày
nằm hoàn toàn sau khi Thừa Thiên Huế đã thêm ngày CN, nên không thể thấy thay đổi.

## 8. Gỡ về

```bash
cp /root/Lottery_AI_Test/backups/v11008_pre_vps/gpt_analyzer.py.pre      web/backend/
cp /root/Lottery_AI_Test/backups/v11008_pre_vps/prompt_registry.py.pre   web/backend/
cp /root/Lottery_AI_Test/backups/v11008_pre_vps/station_identity.py.pre  web/backend/
systemctl restart lottery
```

Bản local `backups/v11008_pre/`: `gpt_analyzer.py.pre` md5 `c028047bf56a7b00f392562072411cff` ·
`prompt_registry.py.pre` md5 `c151c2b0d5ab7a1d6a03069d6fa767e0` · `_v87_master_board.py.pre`
md5 `276e7001e1e8545201dffdef645627bf`.

## 9. Theo dõi tiếp

| Mã | Nội dung | Hạn |
|---|---|---|
| **FU-293** | **ĐÓNG `CLOSED_PASS`** — giải xong bằng dữ liệu, không cần owner | 06/08 |
| **FU-295** | Owner quyết `rule_custom_prompt` 2.700 ký tự: bật lại · gộp vào RR · hay xoá như CP-7.9 | 13/08 |
| **FU-296** | Cổng chặn luật cứng trỏ vào lớp prompt KHÔNG chạy. H7/H8 trỏ vào lớp chết nhiều tháng mà không cổng nào bắt | 13/08 |

**Con số cần nhớ:** **40/41** đài giữ nguyên · **1** đài đổi (`Thừa Thiên Huế` thêm CN từ
26/10/2025) · bảng phân giải **42 ô, 0 sai** · CP-7.9 **7/8 khối trùng, 0 phép đo**.
