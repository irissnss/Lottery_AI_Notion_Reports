# REPORT V11007 — Gỡ NỐT 10 chỗ sót của V11001 + ký §60 «cấm bỏ nửa chừng»

> **Ngày:** 2026-08-06 · **Mã việc:** FU-284 (đếm lại) · FU-294
> **Deploy:** ĐẠT — PID `936322` → `937241`, 4 bảng khoá **y hệt**
> **Phiên bản prompt:** `SP-4.2 → SP-4.3` · `CTX-16.6 → CTX-16.7` · `PB-18.2 → PB-18.3`

---

## 1. Tóm tắt

Owner bắt đúng **hai lỗi**, lỗi thứ hai nặng hơn hẳn.

**Lỗi 1 — trình bày:** trang phân tích viết ở **thì đề xuất** cho việc **đã làm xong**. Bảng
G1–G5 ghi *"GỠ HẲN / GIỮ / SỬA CHỮA"* như đề nghị; nhìn vào tưởng chưa động gì.

**Lỗi 2 — thi công:** kiểm lại code thì phát hiện **V11001 làm nửa chừng**. Nó gỡ 8 khối dữ
liệu gan/nóng/lạnh rồi báo *"xong"*, nhưng **còn 10 chỗ** vẫn dạy model dùng gan — trong đó có
một chỗ **trỏ vào khối dữ liệu đã bị chính nó gỡ**.

Owner yêu cầu ghi thành quy tắc. Đã ký **§60 (A58)** vào cả sáu mặt quy tắc.

## 2. Owner yêu cầu gì (nguyên văn)

> *"V5 sao anh thấy chưa có trạng thái trước và sau sửa ah, hoàn thành hay chưa ah em, nhìn hình
> gây hiểu nhầm liền sữa rồi thì hoàn thành ở lần ở version nào trong code luôn rõ ràng chứ em,
> anh biết em có tư duy suy nghĩ, phải đảm bảo logic tương quan, tương thích, phù hợp nha em,
> nghĩa là đụng tới chỗ nào các vấn đề nào liên quan là cần phải soi xét mới xử lý chứ đừng để xử
> lý chỗ này làm lỗi chỗ khác điều này cần ghi vào quy tắc làm việc claude.md đó nha cấm cẩu thả
> thiếu suy xét trước sau nha em"*

## 3. Đào bới / phát hiện

### 3.1 V11001 làm nửa chừng — 10 chỗ sót · `VERIFIED_CODE`

| dòng | chỗ sót | vì sao nguy hiểm |
|---|---|---|
| 2962 | `KẾT HỢP … (Top 10 Score, **Gan, Hot/Cold**, Trends)` | ra lệnh dùng nguồn đã bị gỡ |
| **2966** | `Sử dụng dữ liệu Deep Focus (…, **Gan đài**)` | **trỏ vào khối dữ liệu KHÔNG CÒN TỒN TẠI** |
| 2968 | `ưu tiên số … (thống kê + ĐÀI + THỨ **+ Gan**)` | đúng chữ G4 bảo bỏ — sửa được dòng 342, **sót dòng 2968** |
| 394·395 | few-shot `Gan=02(freq=71)` · `02 → 3 nguồn (…+Gan)` | **dạy bằng ví dụ** — với model, ví dụ mạnh hơn mệnh lệnh |
| 402·403 | `Gan=95(freq=76)` · `95 → 1 nguồn (Gan only)` | như trên |
| 2332 | `🔥 Số HOT (xuất hiện nhiều trong WIN)` | **nhãn dữ liệu tự nó là mệnh lệnh** |
| 2337 | `Ưu tiên số HOT (xuất hiện trong WIN gần đây)` | bàn tay nóng đặt lên chính lịch sử thắng của model |
| 2638 | `Kết hợp với: … **hot/cold**, frequency…` | nhắc lại nguồn đã gỡ |
| 4421 | `xếp hạng bằng tần suất/**gan** nội miền` | RULES-FIRST vẫn bảo xếp hạng bằng gan |

**Chỗ 2966 là nặng nhất.** Model được bảo *"Sử dụng dữ liệu Deep Focus (…, Gan đài)"* nhưng khối
`⏳ GAN ĐÀI HÔM NAY` **đã bị V11001 xoá**. Model được lệnh dùng một thứ không tồn tại ⇒ nó **tự
bịa** hoặc **tự suy lại mệnh lệnh cũ**.

**Bỏ nửa chừng tệ hơn không làm** — và **phép đo 14 ngày FU-284 đang đo một thay đổi nửa vời**,
nên kết luận rút ra sẽ vô giá trị.

### 3.2 Suýt báo nhầm vì đếm chuỗi thô · `VERIFIED_TEST`

Vòng quét đầu dùng `grep` đếm chuỗi, thấy `GAN ĐÀI` và `SỐ SẮP ĐẾN CHU KỲ` **vẫn còn** ⇒ suýt
kết luận *"G2 và G5 chưa làm"*. Đọc ngữ cảnh mới thấy chúng chỉ nằm trong **dòng chú thích** ghi
lại chính việc đã gỡ.

Bài học: **đếm chuỗi thô là sai** — phải phân loại `TRONG_PROMPT` / `GHI_VÀO_PROMPT` / `CODE` /
`CHU_THICH`. Điều này thành `§60.3`.

## 4. Hướng xử lý và vì sao chọn

**Đây KHÔNG phải biến thứ hai theo QD-018 mà là làm nốt biến thứ nhất.** Nên được phép đi ngay,
nhưng **FU-284 phải đếm lại từ đầu**.

**Nhãn `ĐB hot` / `G8 hot` → `ĐB hay ra` / `G8 hay ra`.** Số liệu **giữ nguyên** (vẫn là top-3
đuôi hay gặp nhất ở giải đó) — nó là dữ liệu tần suất hợp lệ. Chỉ bỏ chữ khung nó thành giả
thuyết số nóng.

**Đổi cả tên biến** `hot`/`hot_str` → `trung_nhieu`/`trung_nhieu_str`: để nguyên thì cổng quét
ngược khớp trúng **tên biến** và báo động giả.

## 5. Đã làm gì

**11 chỗ sửa** trong `gpt_analyzer.py` + **§60 (A58)** vào 6 mặt quy tắc + sửa cổng
`_v11001_kiem_prompt.py` + `_v11007_deploy.py` có cổng quét ngược riêng.

## 6. Cổng kiểm

**Quét ngược trước/sau:**

| | trước V11007 | sau V11007 |
|---|---|---|
| `TRONG_PROMPT` | 8 dòng | **1 dòng** (đúng câu G3 cố ý giữ) |
| `GHI_VAO_PROMPT` | 2 dòng | **0** |

**Deploy — cổng chặn ngay trên VPS trước khi restart:**

| | |
|---|---|
| **Lần đẩy đầu** | **CHẶN** — còn tên biến `hot_str`. Cổng làm đúng việc |
| Lần thứ hai | `TRONG_PROMPT=1 · GHI_VAO=0 · SP-4.3` → cho restart |
| PID | `936322` → `937241` **KHÁC** |
| 4 bảng khoá | `predictions` 11.875 · `final_bundles` 480 · `lottery_results` 15.226 · `model_daily_eval` 11.739 — **y hệt cả bốn** |
| `/api/health` | **200** sau ~10s |

`[cong] V11007_DEPLOY=DAT HASH_DOI=0 PID_KHAC=True TRONG_PROMPT=1 GHI_VAO=0 SP=SP-4.3`
`[cong] PROMPT_SACH=DAT` · sổ quyết định **không mục nào trôi** · sáu mặt quy tắc **đồng bộ**.

## 7. Vướng vấp

**Bắt được thêm một lỗi §60 của chính agent, ngay trong phiên ký §60.** Cổng
`_v11001_kiem_prompt.py` so **CỨNG** chuỗi `'SP-4.2'`. Nâng lên `SP-4.3` làm cổng **TRƯỢT** dù
prompt sạch hơn trước — đúng kiểu *"xử lý chỗ này làm lỗi chỗ khác"*.

Đã đổi sang **so SÀN thay vì so BẰNG**: bằng mốc thì đạt, cao hơn càng đạt, thấp hơn mới trượt.
Nâng bản sau này không làm vỡ cổng nữa.

**Cổng deploy chặn lần đẩy đầu** vì tên biến `hot_str`. Đây là **dương tính giả** — tên biến
không vào prompt. Nhưng thay vì nới cổng, đã **đổi tên biến**: giữ cổng chặt, bỏ chỗ mập mờ.

## 8. Gỡ về

```bash
cp /root/Lottery_AI_Test/backups/v11007_pre_vps/gpt_analyzer.py.pre \
   /root/Lottery_AI_Test/web/backend/gpt_analyzer.py
systemctl restart lottery
```

Bản local: `backups/v11007_pre/gpt_analyzer.py.pre` md5 `d87956d1f45aec1b0f6952e7d41f2464`.

## 9. Theo dõi tiếp

| Mã | Nội dung | Hạn |
|---|---|---|
| **FU-284** | **ĐẾM LẠI** 14 ngày từ V11007. Ngày đo đầu (06/08) chạy trên bản nửa vời ⇒ bỏ. Tụt ≥5 điểm bền ⇒ gỡ về | 20/08 |
| **FU-294** | Dựng cổng quét ngược **tự động** cho mọi thay đổi prompt, nối vào sổ diễn tập DT-06 và cổng deploy. V11001 sót 10 chỗ chính vì không có cổng này | 13/08 |

**Con số cần nhớ:** `TRONG_PROMPT` **8 → 1** · `GHI_VAO_PROMPT` **2 → 0** · và **hai lỗi §60 bắt
được ngay trong phiên ký §60** (cổng so cứng phiên bản, cổng khớp tên biến).
