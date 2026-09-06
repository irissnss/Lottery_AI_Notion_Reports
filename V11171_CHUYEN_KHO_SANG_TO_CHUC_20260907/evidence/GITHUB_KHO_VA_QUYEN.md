# GITHUB — KHO, QUYỀN, VÀ BẢNG KIỂM THÔNG SUỐT

> **Tài liệu TRA CỨU THƯỜNG TRỰC.** Lập 07/09/2026 (V11171) theo yêu cầu owner:
> *«cần cập nhật, ghi nhận để lần sau không nhầm lẫn, quên lãng… trường hợp nào không thông báo anh
> xử lý luôn để lâu quên tình huống này rồi phải đi kiếm, cho rằng lỗi này lỗi kia mất thời gian
> lắm đó em»*
>
> **Phiên sau gặp bất cứ chuyện gì liên quan GitHub: ĐỌC FILE NÀY TRƯỚC.** Đừng đi chẩn lại từ đầu.

---

## 1 · ĐỊA CHỈ CHÍNH THỨC — dùng cái này, không dùng cái cũ

| kho | địa chỉ CHÍNH THỨC | quyền | dùng để |
|---|---|---|---|
| mã nguồn + tài liệu quản trị | `github.com/BaoBiTanPhat/Lottery_AI_Test` | **Private** | code, docs, sổ quyết định |
| báo cáo công khai (§57.2) | `github.com/BaoBiTanPhat/Lottery_AI_Notion_Reports` | **Public** | báo cáo cho owner + TanPhatAI đọc |

**Ngày chuyển:** 07/09/2026, owner chuyển từ tài khoản cá nhân `irissnss` sang tổ chức
**`BaoBiTanPhat`**. Tổ chức còn hai kho khác (`erptanphat`, `Baocaoerptanphat`) — **thuộc dự án ERP
khác, KHÔNG liên quan Lottery**, đừng đụng.

**Đường cũ `github.com/irissnss/...` VẪN CHẠY** nhờ GitHub tự chuyển hướng, nhưng:

> 🔴 **CẤM ghi đường cũ vào tài liệu mới, mã mới, hay cấu hình mới.**
> Chuyển hướng **gãy vĩnh viễn** nếu có ai tạo một kho trùng tên dưới `irissnss`. Khi đó push sẽ
> **âm thầm đi vào kho SAI — không báo lỗi**. Đây là kiểu hỏng nguy hiểm nhất vì **nó không kêu**.

---

## 2 · AI DÙNG KHOÁ NÀO — hai khoá khác nhau, đúng thiết kế

| nơi | danh tính | kiểm bằng |
|---|---|---|
| **máy local** | tài khoản người `irissnss` | `ssh -T git@github.com` → *"Hi irissnss!"* |
| **VPS** | **deploy key riêng** của `BaoBiTanPhat/Lottery_AI_Test` | `ssh -T git@github.com` → *"Hi BaoBiTanPhat/Lottery_AI_Test!"* |

Deploy key của VPS **chỉ có quyền trên đúng một kho** — đó là thiết kế đúng, không phải lỗi.

---

## 3 · ĐIỀU QUAN TRỌNG NHẤT: PRODUCTION KHÔNG PHỤ THUỘC GITHUB

Đo 07/09/2026:

- **0 cron nào chạy `git pull` / `git fetch`** (quét `crontab -l` của root và `/etc/cron.d`).
- Service chạy thẳng từ tệp trên đĩa:
  `ExecStart=/root/Lottery_AI_Test/venv/bin/python3 main.py`
  `WorkingDirectory=/root/Lottery_AI_Test/web/backend`
- `/root/Lottery_AI_Notion_Reports` **không tồn tại** trên VPS.

⇒ **GitHub là nơi LƯU và CÔNG BỐ, không phải nguồn nạp mã lúc chạy.**
Mọi sự cố GitHub — đổi chủ, đổi tên, mất quyền, sập — **không thể làm dừng dự đoán**.
Deploy lên VPS làm bằng **chép tệp**, không bằng `git pull`.

---

## 4 · BẢNG KIỂM THÔNG SUỐT — chạy khi nghi ngờ

Script: `web/backend/../scratchpad` (V11171) hoặc chạy tay các lệnh dưới.
**Không lệnh nào ghi lên remote** — chỉ `ls-remote`, `--dry-run`, `curl`.

### A · Local → kho RIÊNG (SSH)
```bash
git ls-remote git@github.com:BaoBiTanPhat/Lottery_AI_Test.git HEAD     # phải ra HEAD
git -C E:\Lottery_AI_Test push --dry-run origin HEAD                    # phải OK
git -C E:\Lottery_AI_Test remote get-url origin                         # phải chứa BaoBiTanPhat
```

### B · Local → kho CÔNG KHAI (SSH)
```bash
git ls-remote git@github.com:BaoBiTanPhat/Lottery_AI_Notion_Reports.git HEAD
git -C E:\Lottery_AI_Notion_Reports push --dry-run origin HEAD
git -C E:\Lottery_AI_Notion_Reports remote get-url origin
```

### C · Người NGOÀI đọc được báo cáo công khai không
```bash
curl -s -o /dev/null -w '%{http_code}\n' https://api.github.com/repos/BaoBiTanPhat/Lottery_AI_Notion_Reports   # 200
curl -s -o /dev/null -w '%{http_code}\n' https://raw.githubusercontent.com/BaoBiTanPhat/Lottery_AI_Notion_Reports/main/README.md  # 200
```

### D · Kho RIÊNG có còn KÍN không  ← **phép an toàn, phải chạy sau mọi thay đổi quyền**
```bash
curl -s -o /dev/null -w '%{http_code}\n' https://api.github.com/repos/BaoBiTanPhat/Lottery_AI_Test
# BẮT BUỘC ra 404. Nếu ra 200 => KHO RIÊNG BỊ LỘ => P0, báo owner NGAY.
```

### E · VPS → kho RIÊNG (deploy key)
```bash
python _chay.py <script>   # trong script:
#   git ls-remote git@github.com:BaoBiTanPhat/Lottery_AI_Test.git HEAD
#   git -C /root/Lottery_AI_Test fetch --dry-run origin
```

### F · VPS có cần GitHub không (phải luôn là KHÔNG)
```bash
crontab -l | grep -c 'git pull\|git fetch'          # phải 0
grep -rl 'git pull\|git fetch' /etc/cron.d | wc -l  # phải 0
systemctl show -p ExecStart --value lottery         # phải là đường tệp trên đĩa
```

**Kết quả đo 07/09/2026: 24/24 THÔNG.**

---

## 5 · 🔴 HAI BẪY ĐÃ SẬP — ĐỌC KỸ, ĐỪNG LẶP

### Bẫy 1 — `credential.helper` làm phép thử "ẩn danh" KHÔNG hề ẩn danh

Git trên Windows có `credential.helper = manager`. Khi thử
`git ls-remote https://github.com/<chủ>/<kho-riêng>.git`, nó **âm thầm cấp thông tin đăng nhập đã
lưu** ⇒ lệnh **THÀNH CÔNG** ⇒ trông y hệt **"kho riêng bị lộ"**.

**Ngày 07/09 việc này suýt làm agent báo một P0 bảo mật KHÔNG CÓ THẬT.**

**Thử ẩn danh cho ĐÚNG:**
```bash
curl -s -o /dev/null -w '%{http_code}' https://api.github.com/repos/<chủ>/<kho>   # cách tin cậy nhất
git -c credential.helper= ls-remote https://github.com/<chủ>/<kho>.git HEAD       # hoặc cách này
```

### Bẫy 2 — sau khi đổi hạ tầng, MỘT lần đo hỏng KHÔNG đủ để kết luận

Ngay sau khi chuyển kho sang tổ chức, `git ls-remote` từ VPS báo `Repository not found` ở **cả hai**
đường, trong khi `ssh -T` vẫn xác thực thành công. Agent đã viết vào bản nháp: *«deploy key mất
quyền, cần owner xử lý»*.

**Đo lại vài phút sau: THÔNG 3/3 lần, `fetch --dry-run` chạy đủ.** Đó chỉ là **trạng thái tạm trong
lúc GitHub lan truyền việc đổi chủ sở hữu**.

**Luật:**
1. Sau thao tác đổi hạ tầng, **đo lại sau vài phút** trước khi kết luận hỏng.
2. Luôn đo **cả đường cũ lẫn đường mới**. Nếu **cả hai hỏng như nhau** ⇒ nguyên nhân **không nằm ở
   thao tác vừa làm**.
3. Nếu vẫn hỏng sau khi đo lại: ghi `INDETERMINATE` kèm lý do, **đừng đoán nguyên nhân**.

---

## 6 · KHI OWNER ĐỔI TÊN TỔ CHỨC / CHUYỂN KHO LẦN NỮA — làm đúng 5 bước này

1. **Ghim 3 remote** về địa chỉ mới:
   ```bash
   git -C E:\Lottery_AI_Test           remote set-url origin git@github.com:<MỚI>/Lottery_AI_Test.git
   git -C E:\Lottery_AI_Notion_Reports remote set-url origin git@github.com:<MỚI>/Lottery_AI_Notion_Reports.git
   # VPS:
   git -C /root/Lottery_AI_Test        remote set-url origin git@github.com:<MỚI>/Lottery_AI_Test.git
   ```
   *(Sao lưu `.git/config` trước khi đổi.)*

2. **Sửa BỐN mặt quy tắc SỬA TAY** — `CLAUDE.md` · `.cursorrules` · `.AGENT.md` ·
   `.Antigravityrules.md`. **CẤM sửa tay `AGENTS.md` và `GEMINI.md`** (chúng sinh tự động).

3. **Sinh lại hai mặt tự động:**
   ```bash
   python web/backend/_v10925_rule_sync_check.py
   ```

4. **Sửa HAI script ghi cứng địa chỉ** — bỏ sót là việc sẽ tự hoàn tác:
   - `web/backend/_v11083_sinh_dieu_huong.py` — hằng `RAW`, sinh liên kết cho `NEXT_ACTION.md`
   - `web/backend/_v10921_rule_a55.py` — ⚠️ **quan trọng nhất**: nó **GHI NGƯỢC** văn bản A55 vào
     **ba mặt quản trị**. Bỏ qua tệp này thì lần chạy sau **ghi lại địa chỉ cũ**, xoá sạch việc vừa
     làm (`A58_VIOLATION_HALF_DONE`, §60.1).

   *(Cả hai là script độc lập, **không tệp nào import** chúng vào đường phục vụ ⇒ **không cần
   deploy, không cần restart**.)*

5. **Chạy bảng kiểm mục 4** — phải đủ 24/24, đặc biệt **phép D (kho riêng phải 404)**.
   Rồi chạy `_v10925_rule_sync_check.py` + `_v11027_so_muc_quan_tri.py` + `_v10921_report_gate.py`.

**Quét lại cho chắc — phải ra 0 kết quả:**
```bash
grep -rn "<CHỦ CŨ>" web/backend/*.py .cursor CLAUDE.md AGENTS.md GEMINI.md .cursorrules .AGENT.md .Antigravityrules.md
```

---

## 7 · NHỮNG CHỖ KHÔNG CẦN SỬA — cố ý để nguyên

| nơi | vì sao để nguyên |
|---|---|
| `backups/**` | ảnh chụp lịch sử; sửa là **viết lại lịch sử** |
| `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` (mục cũ) | sổ **APPEND-ONLY**; địa chỉ cũ ở mục cũ là **đúng với thời điểm đó** |
| báo cáo đã công bố trong `Lottery_AI_Notion_Reports/` | đã phát hành; sửa là viết lại lịch sử. Bản mới ghi địa chỉ mới |

---

## 8 · TÓM TẮT MỘT DÒNG CHO PHIÊN VỘI

> Kho ở **`BaoBiTanPhat`** (riêng `Lottery_AI_Test` · công khai `Lottery_AI_Notion_Reports`).
> Đường `irissnss` cũ vẫn chạy nhờ chuyển hướng nhưng **cấm dùng trong tài liệu mới**.
> **Production KHÔNG phụ thuộc GitHub** — sự cố GitHub không làm dừng dự đoán.
> Nghi ngờ thì chạy bảng kiểm mục 4; nhớ **hai bẫy ở mục 5** trước khi kết luận bất cứ điều gì hỏng.
