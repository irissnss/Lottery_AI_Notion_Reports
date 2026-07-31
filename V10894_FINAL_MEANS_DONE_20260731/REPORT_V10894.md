# V10894 — Mốc FINAL là "đã xong", không phải "bắt đầu chốt"

**Ngày:** 31/07/2026 · **Commit private:** `ce3347c` · **Hash 4 bảng:** IDENTICAL (2 lần deploy)

---

## Owner yêu cầu

> *"Em phải rõ ràng chứ em. total output Tối đa MN là 15h45 / MT 16h53 / MB 17h53 thật chuẩn chính chính xác để người dùng còn ra quyết định nữa không rõ ràng gì cả biết lúc nào là cuối cùng là final, còn cập nhật tài liệu chống quên lãng kiểm tra đối chiếu nữa em. Đừng có mơ hồ"*
> — 31/07 13:34

---

## 1. Chỗ mơ hồ owner bắt đúng

V10893 (làm 20 phút trước đó) đặt khoá `/choi` **chạy** đúng 15:45 / 16:53 / 17:53. Nghĩa là nó ghi xong lúc **15:45:0x — sau mốc**.

Mốc đang mang nghĩa *"bắt đầu chốt"* chứ không phải *"đã final"*. Người dùng nhìn 15:45 mà số chưa chắc có thì mốc không dùng được để ra quyết định.

---

## 2. Đo trước khi đặt biên — và bộ đo đầu tiên sai

Bộ đo đầu **sai**: nó trừ giờ ghi trong DB cho giờ cron **mới** (lịch mới chưa chạy lần nào, bây giờ mới 13:34), ra 600–1500 giây vô nghĩa.

Đối chiếu đúng — giờ ghi so với giờ cron **cũ** đang hiệu lực lúc đó:

| Job | Cron cũ | Ghi lúc | Mất |
|---|---|---|---|
| `_v10822_total_v2_lane` MN | 15:47 | 15:47:01 | 1s |
| `_v10832_total_v3_cond_lane` MN | 15:49 | 15:49:02 | 2s |
| `_v10872_deherd_selector` MN | 15:51 | 15:51:01 | 1s |
| `_v10822_total_v2_lane` MT | 16:56 | 16:56:02 | 2s |
| khoá `/choi` MN | 16:00 | 16:00:01 | 1s |
| khoá `/choi` MB | 18:00 | 18:00:02 | 2s |
| `_v10781_prompt_v2_lane` MN | 05:10 | 05:10:38 | **38s** |

Chậm nhất 38 giây → **biên 2 phút dư sức**.

---

## 3. Lùi khoá về trước mốc

| Khoá `/choi` | V10893 | V10894 |
|---|---|---|
| MN | 15:45 | **15:43** |
| MT | 16:53 | **16:51** |
| MB | 17:53 | **17:51** |

Đổi 3/3 dòng cron, nạp thành công. Sau đổi, tại đúng **15:45:00 / 16:53:00 / 17:53:00** mọi thứ ĐÃ nằm trong kho.

### Chuỗi đầy đủ

| Bước | MN | MT | MB |
|---|---|---|---|
| Official chốt bundle (đo 9 ngày, muộn nhất) | 04:19 | 16:43 | 17:35 |
| Các lane chạy | 15:36–15:39 | 16:44–16:49 | 17:38–17:44 |
| Lane phải xong | 15:41 | 16:50 | 17:50 |
| Khoá `/choi` chạy | 15:43 | 16:51 | 17:51 |
| **★ FINAL — mọi thứ đã xong** | **15:45:00** | **16:53:00** | **17:53:00** |
| Xổ | ~16:34 | ~17:30 | ~18:31 |

---

## 4. Chốt chặn so theo GIÂY

`_hm()` cắt chuỗi thời gian còn `HH:MM`, nên ghi lúc `15:45:30` bị làm tròn thành `"15:45"` rồi so `"15:45" <= "15:45"` → **cho qua như đúng hạn**. Thay bằng `_hms()` giữ đủ giây.

Kiểm 4 trường hợp biên:

| Ghi lúc | FINAL | Kết quả |
|---|---|---|
| 15:44:59 | 15:45:00 | đúng hạn |
| 15:45:00 | 15:45:00 | đúng hạn |
| 15:45:01 | 15:45:00 | **TRỄ** |
| 15:45:30 | 15:45:00 | **TRỄ** |

Hồi tố 30/07 dưới lịch cũ: **37 mục** ghi sau mốc.

---

## 5. Người dùng phải thấy mốc, không chỉ admin

Owner nói *"để người dùng còn ra quyết định"* — nên mốc lên thẳng trang người chơi:

**`/choi`** — khối 3 ô MN/MT/MB:
- Giờ FINAL cỡ lớn (`clamp(1.1rem, 4.4vw, 1.5rem)`, `tabular-nums`)
- Đếm ngược sống: `"còn 1h59 — số còn có thể cập nhật"` → khi qua mốc đổi thành `"✓ đã final — số không đổi nữa"` và ô chuyển viền xanh
- Quy về giờ VN (`getTimezoneOffset() + 420`) nên máy người dùng lệch múi vẫn đúng
- Tự cập nhật mỗi 30 giây
- Câu giải nghĩa: *"Trước mốc, số vẫn có thể được cập nhật khi model về thêm. Từ mốc trở đi số đứng yên cho tới khi xổ."*

**`/monitoring`** — panel đổi tiêu đề thành **MỐC FINAL TOTAL OUTPUT**, ba con số hiện ngay đầu panel kèm dòng *"Tại đúng giây này, toàn bộ output của MỌI luồng ĐÃ nằm trong kho"*.

### Kiểm mắt thật

Playwright qua HTTP server — bài học V10882: nạp `file://` làm API chết trước khi kịp chặn, trang rỗng mà vẫn báo "sạch".

| Khung nhìn | Khối hiện | Tràn ngang | Tràn trong | Lỗi JS | Thẻ miền | Đếm ngược |
|---|---|---|---|---|---|---|
| 390×844 | CÓ (347px) | không | không | 0 | 3 | khớp giờ thật |
| 1440×900 | CÓ (1139px) | không | không | 0 | 3 | khớp giờ thật |

---

## 6. Tài liệu chống quên

**`docs/MOC_FINAL_TOTAL_OUTPUT.md`** — một trang, một bảng, một cách hiểu. Nội dung:

1. Ba mốc FINAL + cách đọc đúng
2. Chuỗi đầy đủ dẫn tới FINAL
3. Cái gì bị áp mốc / cái gì miễn **kèm lý do từng cái**
4. Ai canh mốc này
5. **Vì sao phải có trang này** — lịch trôi tháng 7 vì hệ dựng quanh cutoff 17:00/18:00 (muộn hơn hạn thật 5 phút) rồi mỗi luồng mới xếp sau luồng cũ
6. **Thủ tục bắt buộc khi thêm luồng mới** — 4 bước, có bước chạy guard xác nhận 0 trễ ngay hôm đó
7. Lệnh rollback theo từng bước
8. Lịch sử đổi mốc

Playbook §1 và §Chuỗi mốc trỏ về trang này làm gốc.

---

## 7. Xác minh

| Mục | Kết quả |
|---|---|
| Hash `predictions` / `final_bundles` / `lottery_results` / `model_daily_eval` | **IDENTICAL** trước-sau, cả 2 lần deploy |
| `/api/health` | 200 |
| `/du-doan` | 200 |
| `/api/admin/deadline-guard` | 401 (cổng admin đúng) |
| `/choi`, `/monitoring` | 401 vì có cổng admin — curl trần không kết luận được |

`/choi` và `/monitoring` không kiểm bằng curl được, nên xác minh theo chuỗi mắt xích:

1. Route `serve_choi_page` trả `FileResponse(STATIC_DIR / "choi.html")`
2. `STATIC_DIR = Path(__file__).parent.parent / "frontend"` → `/root/Lottery_AI_Test/web/frontend`
3. md5 file VPS **KHỚP** md5 local (`91b0188e3670` · `2ff9c296af3a`)
4. Nội dung file VPS chứa **8/8** dấu hiệu mốc FINAL trong `choi.html`, **6/6** trong `monitoring.html`
5. `systemctl show` xác nhận tiến trình đang chạy có `WorkingDirectory=/root/Lottery_AI_Test/web/backend`, khớp mắt xích 2

---

## 8. Cần theo dõi live hôm nay

| Giờ | Kỳ vọng |
|---|---|
| 15:43 | Khoá `/choi` MN chạy |
| **15:45:00** | MN đã final — mọi output trong kho |
| 16:51 | Khoá `/choi` MT chạy |
| **16:53:00** | MT đã final |
| 17:51 | Khoá `/choi` MB chạy |
| **17:53:00** | MB đã final |
| 18:02 | Guard chấm cả ngày — phải ra **0 trễ** |

Rollback nếu hỏng: `crontab /root/Lottery_AI_Test/.local_backup_v10894_crontab_20260731_133757.txt`

**Follow-up:** `FU-V10894-FINAL-MEANS-DONE` (`DEPLOYED_PENDING_LIVE_VERIFY`)
