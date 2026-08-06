# REPORT V10998 — Khung chặn một cửa sổ 15:00–18:45 · soi 17 job trước khi dời lịch MN

> **Ngày:** 2026-08-06 · **Quyết định owner:** QD-036 · **Mã việc:** FU-282
> **Báo cáo chung cả mạch:** [`REPORT_V10993_V10996.md`](./REPORT_V10993_V10996.md)

---

## 1. Tóm tắt

Owner muốn dời lịch sinh số MN từ sáng sớm sang chiều để có thời gian code/fix ban ngày.
Đo trước khi gật: **chuỗi MN chạy 18–22 phút, 0/46 ngày vượt 30 phút** — kịp.

Nhưng đề xuất **15:15** của owner sẽ làm hỏng **5 job** xếp ở 15:36–15:43. Owner chốt **15:00**.

**Khung chặn đã đổi. Lịch MN CHƯA dời** — còn 4 job phải xếp lại trước.

## 2. Owner yêu cầu gì (nguyên văn)

> *"Vậy em dời luôn lịch dự đoán cho MN đi để khoản thời gian trước đó anh đủ thời gian để
> code, fix điều chỉnh đi em. Dời lịch dự đoán cho MN sang bắt đầu từ 15h15 - Final tối đa là
> 15h45. Nghĩa là bắt đầu block từ 15h15 đến hết 18h45 khoảng thời gian này phục vụ live để
> kết quả trung thực ôn định nha em. Em thấy thế nào kiểm tra xử lý cập nhật nhất quán toàn bộ
> hệ thống dùm anh push báo cáo nha em"*

> *"ok em vậy theo em 15h đi em, tiến hành các đề xuất em em đi, anh thấy hợp lý đo kỹ càng
> càng tốt"*

## 3. Đào bới / phát hiện

### Chuỗi MN có kịp không — `VERIFIED_TEST`

Đo 46 ngày, từ lượt gọi model đầu tiên tới lúc có bundle:

| | Thời gian |
|---|---|
| Trung vị | **18,2 phút** |
| P90 | 19,5 phút |
| **Chậm nhất** | **21,7 phút** |
| Vượt 30 phút | **0/46 ngày** |

MN dùng dữ liệu D-1 nên **không có ràng buộc kỹ thuật nào** bắt nó chạy lúc 4 giờ sáng.

### 15:15 sẽ làm hỏng 5 job — `VERIFIED_CODE`

| Giờ | Job | Cần gì |
|---|---|---|
| 15:36 | `_v10822_total_v2_lane --region MN` | bundle MN |
| 15:37 | `_v10832_total_v3_cond_lane --region MN` | bundle MN |
| 15:38 | `_v10872_deherd_selector --region MN` | bundle MN |
| 15:39 | `_v10789_selector_shadow --region MN` | bundle MN |
| 15:43 | `_v10834_lock_freeze` | **chính mốc đóng băng** |

MN bắt đầu 15:15 + ngày chậm nhất 21,7 phút = số ra **15:36,7** → job 15:36 nổ **trước khi có
số**. Bắt đầu 15:00 thì số ra 15:18–15:22, **năm job giữ nguyên**, dư 14 phút.

### Soi 17 job buổi sáng — `VERIFIED_CODE`

Đọc **mã thật**, không suy từ tên tệp. Tiêu chí: đọc bảng official **VÀ** lọc MN **VÀ** lọc
ngày hôm nay — thiếu một là không phụ thuộc.

| Kết luận | Số | Ví dụ |
|---|---|---|
| Không đọc bảng official | **8** | `_v10665_mn_ai_limit` · `_v10708_mnmt_rule_ranker` · `_v10646_retrain_guard` |
| Đọc cửa sổ QUÁ KHỨ | **4** | `_v10642_slice_health` (−220 ngày) · `_v10642_model_progress` (−200) · `_v10658_slice_recommendation` (−95) · `_v10800_timetable_selfcheck` |
| **CẦN bundle MN HÔM NAY** | **4** | `05:35 _v10737_output_final_lab_shadow` · `06:05/06:15 _v10879_nghiemthu_lane` · `06:25 _v10725_champion_selector` · `07:30 _v10784_verify_0607` |

## 4. Hướng xử lý và vì sao chọn

**15:00 thay vì 15:15** — mất 15 phút của owner, đổi lại **không phải đụng 5 job** và có 14
phút biên thay vì âm 0,7 phút.

**Khung chặn về MỘT cửa sổ 15:00–18:45.** Cho phép **18:45 → 15:00 hôm sau** = **20,25 giờ
liền một dải** (khung cũ 05:00–18:15 chỉ chừa ~11 giờ, lại chia vụn). Khung hai cửa sổ của
V10997 bỏ — cửa sổ sáng sinh ra để canh MN chạy lúc 4h, nay MN dời thì không còn lý do.

**Chưa dời lịch MN.** Dời trước khi xếp lại 4 job kia là chúng chạy **trước** MN và làm việc
trên **số hôm qua** — sai âm thầm, hệ vẫn chạy, số vẫn ra, không ai biết.

## 5. Đã làm gì

`_v10997_khung_gio.KHUNG_CAM` về một cửa sổ `15:00–18:45`. Ghi thẳng vào mã nguồn cảnh báo:
**khung này chỉ đúng khi lịch MN đã dời**; chừng nào MN còn sinh số 04:16–05:20 thì khung đang
để hở đúng chỗ đó.

Bảng mốc tải `_v10982_lich9.py`: thêm `FU-282` vào 07/08.

## 6. Cổng kiểm

`python web/backend/_v10997_khung_gio.py` → `[cong] DUOC_DEPLOY=CO/KHONG`.

Thử hai chiều trên ngày **không phải** ngày code/fix: 04:30 CHO PHÉP (đúng — MN chưa dời thì
chưa cấm) · 15:22 **CẤM** · 17:40 **CẤM** · 18:50 CHO PHÉP · 02:00 CHO PHÉP.

`J5` (lịch cuốn chiếu) **ĐẠT**. Sổ quyết định **không mục nào trôi**.

## 7. Vướng vấp

**Ba lỗi của chính agent, tự bắt và sửa trong phiên:**

1. **Chèn chú thích sai thụt lề** làm dòng `dt.date(2026, 8, 7)` mất 4 dấu cách. Python **vẫn
   parse được** vì nó nằm trong dict literal — nên phép kiểm cú pháp **không báo gì**. Chỉ lộ
   ra khi phép dò chuỗi của QD-027 trượt.
2. **Script sửa `kiem_code` khớp HAI phép thay vì một**, ghi đè nhầm phép [9] (dò trong
   `FOLLOW_UP_TRACKER.md`) bằng mẫu của tệp `.py`. Đã lấy lại bản gốc **từ git** rồi chỉ giữ
   phần nới cho phép [10].
3. **Mẫu dò của QD-027 khoá cứng cả dấu ngoặc đóng `]`** nên thêm bất kỳ mục nào vào 07/08 cũng
   làm phép trượt oan, dù ý nó chỉ là *"FU-273 có mặt, FU-269/FU-272 đã rời"*. Đã nới về đúng ý,
   **ghi rõ lý do trong `mo_ta`** để sau này không ai tưởng là nới cho dễ.

## 8. Gỡ về

Sửa `KHUNG_CAM` trong `_v10997_khung_gio.py` về `[(5,0)–(18,15)]`. Không cần restart — bộ này
chỉ đọc. Bảng mốc tải: bỏ `"FU-282"` khỏi dòng 07/08.

## 9. Theo dõi tiếp

**FU-282 · SC0708 · hạn 07/08** — đo thời lượng chạy của 4 job phụ thuộc, xếp vào khe sau 15:22
và trước 15:36, hoặc dời sang buổi tối. **Xong mới dời lịch MN sang 15:00.**

**KHÔNG được đụng** 5 job ở `15:36`–`15:43` — chúng nằm đúng giữa *"MN xong"* và *"mốc chốt"*.

**Ngưỡng:** chưa xếp xong 4 job thì **không dời lịch MN**.
