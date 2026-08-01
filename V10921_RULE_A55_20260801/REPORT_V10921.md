# V10921 — Quy tắc A55: báo cáo lên GitHub công khai, Notion chỉ đọc

**Ngày:** 01/08/2026 · **Trạng thái:** đã ghi vào cả ba mặt quy tắc, cổng kiểm đã chạy

---

## 1. Tóm tắt

Owner thống nhất mô hình làm việc: **sau mọi việc code / fix / audit phải đẩy báo cáo lên GitHub
công khai**, và **Notion MCP chỉ dùng để tra cứu, cấm ghi**.

Đã ghi thành quy tắc **A55** vào cả ba mặt quy tắc (mỗi file +4.139 ký tự), nêu **đích danh 7
mục bị thay thế** thay vì sửa rải rác 40 chỗ nhắc Notion. Dựng **khung báo cáo 9 phần** bắt buộc
và **cổng kiểm `_v10921_report_gate.py`** để máy tự bắt phiên nào thiếu báo cáo.

Cổng kiểm chạy lần đầu **bắt ngay chính báo cáo agent viết sáng nay** — thiếu 3 đến 6 phần. Đã
chuẩn hoá lại cả ba báo cáo hôm nay.

---

## 2. Owner yêu cầu gì (nguyên văn)

**01/08 11:04:**

> *"thống nhất quy tắc Mô hình code, fix, audit của dự án anh là sau khi thực hiện code, fix,
> audit cần đẩy báo cáo report lên github report public dùm anh, cập nhận, ghi nhận quá trình,
> yêu cầu thật cụ thể chi tiết để kiểm soát tốt nhất nha em, Notion MCP dùng để tham khảo tài
> liệu khi cần không được cập nhật vào Notion nha em."*

Hai vế rõ ràng: **(a)** báo cáo công khai là bắt buộc sau mọi việc, phải cụ thể chi tiết;
**(b)** Notion chuyển từ nơi-ghi thành nơi-tra-cứu.

---

## 3. Đào bới / phát hiện

### 3.1 Quy tắc cũ đang bắt buộc ghi vào Notion ở nhiều chỗ

| Mặt quy tắc | Số chỗ nhắc Notion | Mục bắt buộc ghi |
|---|---|---|
| `.cursorrules` | 21 dòng | bước 9–10 chuỗi hoàn tất · §52 mục 8 · §52F toàn bộ · §52G |
| `.AGENT.md` | 12 dòng | bước 9–10–11 · §9C · bảng 11 bước |
| `.Antigravityrules.md` | **40 chỗ** | §52F, §52G, FU-170 |

Sửa rải rác 40 chỗ là dễ sót và mất lịch sử. Nên viết một quy tắc mới **nêu đích danh mục bị
thay thế**, giữ nguyên văn bản cũ để đối chiếu.

### 3.2 Cổng kiểm chạy lần đầu — bắt ngay báo cáo của chính agent

```
V10920   ✗ thiếu 4/9 phần   (tóm tắt · hướng xử lý · cổng kiểm · gỡ về)
V10919   ✗ thiếu CONVERSATION_CONTEXT · thiếu 6/9 phần
V10917   ✗ thiếu CONVERSATION_CONTEXT · thiếu 3/9 phần
V10906   ✗ KHÔNG CÓ BÁO CÁO
V10905   ✗ KHÔNG CÓ BÁO CÁO
V10901   ✗ KHÔNG CÓ BÁO CÁO
V10896   ✗ KHÔNG CÓ BÁO CÁO
V10895   ✗ thiếu CONVERSATION_CONTEXT · thiếu 5/9 phần
```

Bốn phiên bản ngày 31/07 **không có báo cáo công khai nào**. Đây là tồn đọng có thật, ghi nhận
chứ không lấp liếm.

### 3.3 Còn 11 file sửa dở chưa commit trong repo công khai

Thuộc V10866–V10869 (27–28/07), không phải của phiên này. Ghi vào tồn đọng.

---

## 4. Hướng xử lý và vì sao chọn

| Phương án | Vì sao chọn / loại |
|---|---|
| **Viết quy tắc mới nêu đích danh mục bị thay thế** | **ĐÃ CHỌN.** Không sót, giữ được lịch sử, đọc là biết cái gì hết hiệu lực từ ngày nào |
| Sửa từng chỗ trong 40 chỗ nhắc Notion | Loại: dễ sót, mất lịch sử, khó rà lại |
| Xoá hẳn §52F/§52G | Loại: mất bối cảnh vì sao từng có quy tắc đó |
| **Khung báo cáo 9 phần cố định** | **ĐÃ CHỌN.** Owner yêu cầu *"thật cụ thể chi tiết để kiểm soát tốt nhất"* — khung cố định làm báo cáo đồng nhất và quét được bằng máy |
| Để agent tự quyết cấu trúc báo cáo | Loại: chính vì thế mà báo cáo hôm nay thiếu 3–6 phần mỗi bản |
| Cổng kiểm dò theo **tiêu đề** | **ĐÃ CHỌN.** Dò toàn văn thì nhắc thoáng qua cũng đậu — quá lỏng |
| Xoá 3 trang Notion đã tạo sáng nay | Loại: owner không yêu cầu xoá, chỉ yêu cầu **không cập nhật nữa**. Giữ làm lịch sử |
| Sửa lại toàn bộ báo cáo cũ cho đủ 9 phần | Loại: quy tắc áp dụng **từ nay**. Chỉ chuẩn hoá báo cáo của phiên hôm nay, phần cũ ghi vào tồn đọng |

---

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `.Antigravityrules.md` | +4.139 ký tự — thêm **A55** |
| `.AGENT.md` | +4.139 ký tự — thêm **A55** |
| `.cursorrules` | +4.139 ký tự — thêm **A55** |
| `web/backend/_v10921_rule_a55.py` | **Mới** — ghi A55 đồng thời vào ba mặt, từ chối ghi nếu kết quả ngắn hơn bản cũ |
| `web/backend/_v10921_report_gate.py` | **Mới** — cổng kiểm báo cáo công khai |
| `_TEMPLATE_REPORT.md` (repo công khai) | **Mới** — bản mẫu khung 9 phần |
| `REPORT_V10917.md` | Thêm phần 2 (nguyên văn owner) · 5b (hướng xử lý) · 9b (gỡ về) |
| `REPORT_V10919_LANE_CLEANUP.md` | Thêm phần 1 (tóm tắt) · 2 (nguyên văn) · 4 (hướng xử lý) · 5 (đã làm) · 7 (vướng vấp) · 9 (gỡ về) |
| `REPORT_V10920.md` | Thêm phần 1 (tóm tắt) · 2 (nguyên văn) · 3c (hướng xử lý) · 6b (cổng kiểm) · 8b (gỡ về) |
| `CONVERSATION_CONTEXT_V10917_20260801.md` | **Mới** — nguyên văn phần V10917/18/19 |
| `docs/OWNER_DECISION_LEDGER.json` | Thêm `OD-20260801-F` |

Nội dung chính của A55:

- **A55.1** Notion chỉ đọc. Cấm 10 hàm ghi, cho phép 6 hàm đọc. Nêu đích danh 7 mục bị thay thế.
- **A55.2** Sau mọi việc code/fix/audit phải có thư mục báo cáo công khai với **hai** file bắt buộc.
- **A55.3** Khung 9 phần.
- **A55.4** Cổng kiểm bằng máy + 3 mã vi phạm.
- **A55.5** Ghi chú lịch sử về 3 trang Notion tạo trước giờ ký.

---

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| A55 có trong cả ba mặt quy tắc | ✓ 10 lần nhắc mỗi file, cùng nội dung |
| A54 vẫn còn nguyên (không đè mất) | ✓ 3 lần nhắc mỗi file |
| Ba file tăng đúng cùng số ký tự | ✓ +4.139 mỗi file |
| Cổng kiểm báo cáo chạy được | ✓ bắt được 8 phiên bản thiếu/không đạt |
| Báo cáo hôm nay sau khi chuẩn hoá | V10917 · V10919 · V10920 · V10921 đủ 9 phần |
| Sổ quyết định sau khi thêm `OD-20260801-F` | 10 quyết định · 0 mục trôi |

---

## 7. Vướng vấp

| # | Vấp | Hậu quả nếu bỏ qua |
|---|---|---|
| 1 | Cổng kiểm bắt ngay **chính báo cáo agent vừa viết sáng nay** thiếu 3–6 phần | Nếu không có cổng, agent tự cho là báo cáo đã "đầy đủ" trong khi thiếu hẳn phần *nguyên văn lời owner* và *gỡ về* — đúng hai thứ owner cần nhất để kiểm soát |
| 2 | Thư mục `V10917_...` **thiếu hẳn** `CONVERSATION_CONTEXT` | Mất nguyên văn lời owner của cả ba phiên bản V10917/18/19 |
| 3 | Cổng kiểm ban đầu dò báo cáo bằng `REPORT_*.md` đầu tiên trong thư mục | Với thư mục chứa nhiều phiên bản (V10917 + V10919) thì chấm nhầm file. Đã sửa: ưu tiên khớp `REPORT_<VERSION>` |
| 4 | Lỗi mã hoá console khi in tiếng Việt từ lệnh `python -c` | Không hỏng gì, nhưng che mất kết quả — phải viết ra file script có `reconfigure(encoding="utf-8")` |
| 5 | 4 phiên bản ngày 31/07 (V10896, V10901, V10905, V10906) **không có báo cáo công khai nào** | Tồn đọng có thật. Ghi nhận vào FU-188 chứ không lấp liếm |
| 6 | 11 file sửa dở chưa commit trong repo công khai (V10866–V10869) | Không phải của phiên này nhưng vẫn là rủi ro mất thay đổi — ghi vào FU-188 |

---

## 8. Gỡ về

Phiên này **chỉ đổi quy tắc và thêm cổng kiểm**, không đụng code chạy, không đụng database,
không deploy.

```
git revert <commit V10921>      # bỏ A55 khỏi ba mặt quy tắc + gỡ cổng kiểm
```

Gỡ lẻ: xoá khối `## A55 —` ở đầu ba file quy tắc (mỗi khối 4.139 ký tự, có đánh dấu rõ) · xoá
`web/backend/_v10921_report_gate.py`. **Mất khoảng 1 phút.**

Gỡ về thì §52F/§52G có hiệu lực trở lại, tức lại phải ghi vào Notion.

---

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng | Hạn |
|---|---|---|---|
| **FU-188** | Bốn phiên bản 31/07 chưa có báo cáo công khai (V10896, V10901, V10905, V10906) + 11 file sửa dở chưa commit | Cổng kiểm `_v10921_report_gate.py` phải về **0 phiên bản không đạt** | sau 08/08 (đang trong cửa sổ đóng băng FU-186) |
| **FU-188b** | Mỗi phiên code/fix/audit từ nay phải chạy cổng kiểm trước khi kết phiên | Không đạt = `A55_VIOLATION_REPORT_MISSING` | liên tục |

Nguyên văn lời owner trong phiên: `CONVERSATION_CONTEXT_V10921_20260801.md` cùng thư mục.
