# V11171 — CHUYỂN KHO SANG TỔ CHỨC `BaoBiTanPhat`: GHIM ĐỊA CHỈ THẬT

> **Ngày:** 07/09/2026 · **Tầng verdict:** `CODED_AND_TESTED_NOT_RUNTIME_PROVEN`
> **Production: 0 ghi · 0 deploy · 0 restart · DB không đụng tới.**
> Thay đổi chỉ nằm ở **cấu hình git** và **văn bản quản trị**; hai script sửa đều **không nằm trong
> đường phục vụ** (đã kiểm bằng grep import).

---

## 1 · TÓM TẮT

Owner chuyển bốn kho từ tài khoản cá nhân `irissnss` sang tổ chức **`BaoBiTanPhat`** và hỏi việc đó
có ảnh hưởng gì không.

**Trả lời ngắn: không mất gì, không hỏng gì.** GitHub tự chuyển hướng nên mọi thứ vẫn chạy — kể cả
lượt push `0720dfb` của phiên trước, nó hiện ra đúng trong bảng tin của tổ chức.

**Nhưng hệ đang sống nhờ một cơ chế chuyển hướng có thể gãy.** Bản này ghim mọi nơi về **địa chỉ
thật**, rồi chạy **bảng kiểm 24 phép phủ đủ mọi trường hợp**: local đọc/ghi hai kho · người ngoài
tải được báo cáo công khai · **kho riêng kín đúng** · VPS đọc được qua deploy key · và VPS **không
cần GitHub để chạy**. **24/24 THÔNG.**

Trong lúc làm, **hai bẫy đo lường đã sập** và cả hai đều suýt thành kết luận sai công bố ra kho —
một cái suýt tạo ra "lỗi deploy key" không tồn tại, một cái suýt báo P0 bảo mật giả. Mục 3.4 và
mục 7 ghi lại đầy đủ để phiên sau không lặp.

---

## 2 · OWNER YÊU CẦU GÌ — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| ~00:2x 07/09 | *«Đã push báo cáo đầy đủ chi tiết hết chưa em?»* | `HỎI` | Kiểm hai kho bằng lệnh; **tự phát hiện thiếu 10 phát hiện** của lớp phản biện → bổ sung mục 3.12, đẩy `0720dfb` | `ĐÃ_LÀM` |
| ~00:4x | *«github có nhưng thay đổi anh chuyển cá nhân sáng Organization tổ chức ảo này có ảnh hưởng đến 4 link trong ảnh không ? em có bị ảnh hưởng không code và báo cáo có ảnh hưởng gì không em»* | `HỎI` | Đo `ls-remote` cả hai đường · thử `raw.githubusercontent` · kiểm crontab và service trên VPS · quét địa chỉ ghi cứng toàn kho | `ĐÃ_LÀM` |
| ~00:5x | *«fix dùm anh đi chứ chờ gì nữa?»* | `YÊU_CẦU` | Ghim 3 remote · sửa 12 chỗ trong 6 mặt quy tắc · sửa 2 script · chạy đủ cổng | `ĐÃ_LÀM` |

---

## 3 · ĐÀO BỚI / PHÁT HIỆN

### 3.1 · Không có gì gãy — đo bằng lệnh, không suy đoán

| phép đo | kết quả |
|---|---|
| `ls-remote irissnss/Lottery_AI_Notion_Reports` | `HEAD = 0720dfb` ✓ |
| `ls-remote BaoBiTanPhat/Lottery_AI_Notion_Reports` | `HEAD = 0720dfb` ✓ **cùng kho** |
| `ls-remote irissnss/Lottery_AI_Test` | `HEAD = a4d6636` ✓ |
| `ls-remote BaoBiTanPhat/Lottery_AI_Test` | `HEAD = a4d6636` ✓ **cùng kho** |
| trang web đường cũ | `301` → `BaoBiTanPhat` |
| `raw.githubusercontent` đường cũ | `200` — vẫn phục vụ |
| `raw.githubusercontent` đường mới | `200` |

Quyền hiển thị giữ đúng sau khi chuyển: `Lottery_AI_Notion_Reports` vẫn **Public** (đúng §57.2 —
báo cáo phải công khai), `Lottery_AI_Test` vẫn **Private**.

### 3.2 · Production KHÔNG phụ thuộc GitHub — đây là lý do việc chuyển kho vô hại

- **Không cron nào `git pull` / `git fetch`** — quét `/etc/cron.d` và `/var/spool/cron/crontabs`,
  0 kết quả.
- Service chạy thẳng từ tệp trên đĩa:
  `WorkingDirectory=/root/Lottery_AI_Test/web/backend` · `ExecStart=.../venv/bin/python3 main.py`.
- `/root/Lottery_AI_Notion_Reports` **không tồn tại** trên VPS.

⇒ Kho GitHub là **nơi lưu và công bố**, không phải nguồn nạp mã lúc chạy. Chuyển chủ sở hữu không
thể chạm tới tiến trình đang phục vụ.

### 3.3 · Chỗ mong manh: ba nơi sống nhờ chuyển hướng

Local ×2 và VPS ×1 vẫn ghi `irissnss/...`. Hôm nay chạy tốt **vì GitHub chuyển hướng**.

**Vì sao phải ghim lại:** chuyển hướng của GitHub **gãy vĩnh viễn** nếu có ai tạo một kho mới trùng
tên dưới `irissnss`. Khi đó push sẽ **âm thầm đi vào kho SAI** — không báo lỗi, không ai biết. Đây
là kiểu hỏng nguy hiểm nhất vì **nó không kêu**.

### 3.4 · 🟢 Một báo động TẠM THỜI — và vì sao nó suýt thành kết luận sai

Ngay sau khi ghim địa chỉ VPS, phép thử báo hỏng:

```
ssh -T git@github.com   →  "Hi BaoBiTanPhat/Lottery_AI_Test! ...successfully authenticated"
git ls-remote (đường CŨ)  →  ERROR: Repository not found.
git ls-remote (đường MỚI) →  ERROR: Repository not found.
```

Phản xạ dễ nhất là kết luận **"deploy key mất quyền do chuyển tổ chức"**. Bản nháp đầu của báo cáo
này **đã viết đúng như vậy**, kèm mức P3 và một việc giao cho owner đi mở `Settings → Deploy keys`.

**Đo lại sau đó thì nó THÔNG.** Chạy **3 lần liên tiếp**, **cả hai đường đều `rc=0`**, và
`git fetch --dry-run` chạy đủ, thấy được nhánh:

```
From github.com:BaoBiTanPhat/Lottery_AI_Test
 * [new branch]  fu438/admin-only-p0a -> origin/fu438/admin-only-p0a
   c9ba901..a4d6636  master            -> origin/master
```

**Kết luận đúng:** đó là **trạng thái TẠM trong lúc GitHub lan truyền việc đổi chủ sở hữu** — quyền
của deploy key mất vài phút để được lập chỉ mục lại ở vị trí mới. **Không có quyền nào hỏng. Không
có việc gì cho owner.**

**Vì sao ghi lại chuyện này thay vì xoá đi:** nếu bản nháp kia được công bố, kho sẽ có một mục
*«deploy key hỏng, cần owner xử lý»* **vĩnh viễn sai**, và phiên sau đọc được sẽ đi tìm một lỗi
**không tồn tại**. Đúng thứ owner vừa cảnh báo: *«để lâu quên tình huống này rồi phải đi kiếm, cho
rằng lỗi này lỗi kia mất thời gian lắm»*.

**Luật rút ra:** sau một thao tác đổi hạ tầng, **một lần đo hỏng KHÔNG đủ để kết luận**. Phải đo
lại sau vài phút, và phải đo **cả đường cũ lẫn đường mới** — nếu **cả hai hỏng như nhau** thì
nguyên nhân **không nằm ở thao tác vừa làm**.

### 3.5 · Quét địa chỉ ghi cứng — 14 chỗ trong mã và luật đang sống

| nơi | số chỗ | loại |
|---|---|---|
| `CLAUDE.md` | 1 | **nguồn** của hai mặt sinh |
| `.cursorrules` | 3 | mặt sửa tay |
| `.AGENT.md` | 3 | mặt sửa tay |
| `.Antigravityrules.md` | 5 | mặt sửa tay |
| `AGENTS.md` · `GEMINI.md` | 1 mỗi mặt | **sinh tự động** — cấm sửa tay |
| `web/backend/_v11083_sinh_dieu_huong.py:68` | 1 | `RAW` URL sinh liên kết cho `NEXT_ACTION.md` |
| `web/backend/_v10921_rule_a55.py` | 1 | mẫu văn bản A55 **ghi vào ba mặt quản trị** |

Hai tệp `.py` **đều là script độc lập** — kiểm bằng grep: **không tệp nào `import`** chúng vào đường
phục vụ, chỉ được nhắc trong chuỗi tài liệu của script khác. ⇒ Sửa **không cần deploy, không cần
restart**.

`_v10921_rule_a55.py` đáng chú ý nhất: nó **ghi văn bản A55 vào ba mặt quản trị**. Nếu để nguyên
địa chỉ cũ, lần chạy sau nó sẽ **tự ghi ngược địa chỉ cũ trở lại** — sửa sáu mặt mà bỏ tệp này là
`A58_VIOLATION_HALF_DONE` (§60: gỡ một chỗ mà để chỗ khác trỏ vào nó).

### 3.6 · BẢNG KIỂM THÔNG SUỐT — 24 phép, đủ mọi trường hợp

Owner yêu cầu: *«kiểm tra thông ở github private và public đầy đủ nha tất cả các trường hợp»*.
Đây là bảng đầy đủ, chạy thật, **không ghi gì lên remote** (chỉ `ls-remote` và `--dry-run`).

**A · MÁY LOCAL → KHO RIÊNG (private), qua SSH**

| # | phép | mong đợi | kết quả |
|---|---|---|---|
| A1 | đọc đường MỚI | được | ✅ `a4d6636` |
| A2 | đọc đường CŨ (qua chuyển hướng) | được | ✅ `a4d6636` |
| A3 | **GHI thử** (`push --dry-run`) | được | ✅ |
| A4 | remote đang trỏ tổ chức mới | đúng | ✅ |

**B · MÁY LOCAL → KHO CÔNG KHAI (public), qua SSH**

| # | phép | mong đợi | kết quả |
|---|---|---|---|
| B1 | đọc đường MỚI | được | ✅ `0720dfb` |
| B2 | đọc đường CŨ | được | ✅ `0720dfb` |
| B3 | **GHI thử** (`push --dry-run`) | được | ✅ |
| B4 | remote đang trỏ tổ chức mới | đúng | ✅ |

**C · NGƯỜI NGOÀI đọc báo cáo công khai (hoàn toàn ẩn danh, không qua git)**

| # | phép | mong đợi | kết quả |
|---|---|---|---|
| C1 | API `BaoBiTanPhat/Lottery_AI_Notion_Reports` | 200 | ✅ **200** |
| C2 | API `irissnss/...` (đường cũ) | chuyển hướng | ✅ **301** |
| C3 | tải thật `REPORT_V11170.md` qua `raw`, đường MỚI | 200 | ✅ **200** |
| C4 | tải thật `REPORT_V11170.md` qua `raw`, đường CŨ | 200 | ✅ **200** |
| C5 | trang web đường cũ | 301 → tổ chức | ✅ **301** |

**D · TÍNH RIÊNG TƯ của kho riêng — phải BỊ TỪ CHỐI**

| # | phép | mong đợi | kết quả |
|---|---|---|---|
| D1 | API ẩn danh `BaoBiTanPhat/Lottery_AI_Test` | **404 (kín)** | ✅ **404** |
| D2 | API ẩn danh `irissnss/Lottery_AI_Test` | **404 (kín)** | ✅ **404** |
| D3 | `raw` kho riêng, ẩn danh | **không tải được** | ✅ **404** |
| D4 | git HTTPS **tắt hẳn** `credential.helper` | **đòi đăng nhập** | ✅ bị từ chối |

**E · VPS → KHO RIÊNG, qua deploy key**

| # | phép | mong đợi | kết quả |
|---|---|---|---|
| E1 | đọc đường MỚI, **3 lần liên tiếp** | được | ✅ 3/3 `rc=0` |
| E2 | đọc đường CŨ, **3 lần liên tiếp** | được | ✅ 3/3 `rc=0` |
| E3 | `fetch --dry-run` từ thư mục làm việc | được | ✅ thấy đủ nhánh |
| E4 | remote đang trỏ tổ chức mới | đúng | ✅ |

**F · VPS có CẦN GitHub để chạy không**

| # | phép | mong đợi | kết quả |
|---|---|---|---|
| F1 | cron của root có `git pull`/`fetch` | **0** | ✅ **0** |
| F2 | `/etc/cron.d` có `git pull`/`fetch` | **0** | ✅ **0** |
| F3 | service chạy từ tệp trên đĩa | đúng | ✅ `/root/Lottery_AI_Test/venv/bin/python3` |
| F4 | `NRestarts` | **0** | ✅ **0** |
| F5 | `/api/health` | 200 | ✅ **200** |

**TỔNG: 24/24 THÔNG.**

**Danh tính khoá:** local là `irissnss` (tài khoản người) · VPS là **deploy key riêng của
`BaoBiTanPhat/Lottery_AI_Test`** — hai khoá khác nhau, đây là thiết kế đúng.

> ⚠️ **Bẫy đã sập một lần khi dựng bảng này — ghi lại để không lặp:** phép thử "HTTPS ẩn danh đọc
> kho riêng" **ban đầu THÀNH CÔNG**, trông như kho riêng bị lộ. Sự thật: Git trên Windows có
> `credential.helper = manager` **âm thầm cấp thông tin đăng nhập đã lưu**, nên phép thử
> **không hề ẩn danh**. Muốn thử ẩn danh thật phải dùng `-c credential.helper=` hoặc `curl` thẳng
> vào API. **Suýt báo một P0 bảo mật không có thật.**

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Ghim về địa chỉ thật thay vì dựa vào chuyển hướng.** Chuyển hướng là tiện ích tạm, không phải hợp
đồng. Ghim thẳng loại bỏ hẳn kiểu hỏng âm thầm ở mục 3.3.

**Sửa sáu mặt đúng quy trình, không chép tay.** `CLAUDE.md` là **nguồn**; `AGENTS.md` và `GEMINI.md`
**sinh tự động** — sửa tay hai mặt đó là vi phạm bảng quy hoạch sáu mặt. Nên: sửa **bốn mặt sửa
tay**, rồi chạy `_v10925_rule_sync_check.py` để sinh lại hai mặt.

**Sửa cả `_v10921_rule_a55.py`** dù nó chỉ là "chuỗi văn bản" — vì nó là **nguồn ghi ngược** vào ba
mặt. Bỏ qua nó thì lần chạy sau sẽ hoàn tác toàn bộ việc hôm nay (§60.1).

**KHÔNG deploy hai tệp `.py` lên VPS, KHÔNG restart.** Chúng là script chạy tay ở local, không nằm
trong tiến trình phục vụ. Đẩy lên VPS sẽ là một thay đổi runtime không cần thiết.

**KHÔNG tự đụng cấu hình tổ chức GitHub.** Việc deploy key (mục 3.4) cần quyền owner và cần biết ý
định của owner về chính sách tổ chức — em báo, không tự quyết.

---

## 5 · ĐÃ LÀM GÌ

| # | việc | trước | sau |
|---|---|---|---|
| 1 | remote kho riêng (local) | `irissnss/Lottery_AI_Test.git` | `BaoBiTanPhat/Lottery_AI_Test.git` |
| 2 | remote kho công khai (local) | `irissnss/Lottery_AI_Notion_Reports.git` | `BaoBiTanPhat/Lottery_AI_Notion_Reports.git` |
| 3 | remote trên VPS | `irissnss/Lottery_AI_Test.git` | `BaoBiTanPhat/Lottery_AI_Test.git` |
| 4 | `CLAUDE.md` | 1 chỗ địa chỉ cũ | 0 |
| 5 | `.cursorrules` | 3 | 0 |
| 6 | `.AGENT.md` | 3 | 0 |
| 7 | `.Antigravityrules.md` | 5 | 0 |
| 8 | `AGENTS.md` · `GEMINI.md` | 1 mỗi mặt | 0 — **sinh lại**, không sửa tay |
| 9 | `_v11083_sinh_dieu_huong.py:68` | `RAW` trỏ `irissnss` | trỏ `BaoBiTanPhat` |
| 10 | `_v10921_rule_a55.py` | mẫu A55 ghi địa chỉ cũ | ghi địa chỉ mới |

**Sao lưu trước khi sửa:** `backups/v11171_pre_org/` (4 mặt sửa tay) ·
`/root/Lottery_AI_Test/.git/config.pre_org_20260907` (VPS).

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11044_cong_so_hieu.py` | ✅ `SO_HIEU_V11044=KHỚP` — cấp V11171 |
| `_v10925_rule_sync_check.py` | ✅ **SÁU MẶT ĐỒNG BỘ** · mọi `.mdc` tự nạp · không còn file chết |
| `_v11027_so_muc_quan_tri.py` | ✅ **không mục nào biến mất** · thoát 0 |
| `_v11062_nang_version.py --kiem` | ✅ `NANG_VERSION_V11062=ĐẠT` |
| `_v11085_cong_rut_lai.py` | ✅ `PRJ_RETRACTION=SẠCH` |
| `_v11088_cong_cua_so_chon.py` | ✅ `PRJ_WINDOW=SẠCH` |
| quét địa chỉ cũ trong mã sống | ✅ **0 chỗ** còn lại trong `web/backend/*.py` và `.cursor/` |
| cú pháp 2 tệp vừa sửa | ✅ `ast.parse` OK cả hai |
| `ls-remote` local sau khi ghim | ✅ kho riêng `a4d6636` · kho công khai `0720dfb` |
| production | ✅ **không đụng** — 0 ghi, 0 deploy, 0 restart |

---

## 7 · VƯỚNG VẤP

| # | vấp | gỡ |
|---|---|---|
| 1 | Lệnh `git remote set-url` **bị bộ lọc quyền chặn** ở lần thử đầu | Em **dừng, không lách**, báo owner kèm lệnh cụ thể. Owner cho phép (*«fix dùm anh đi chứ chờ gì nữa?»*) rồi mới làm |
| 2 | Ghim xong VPS thì `ls-remote` **báo `Repository not found`** ở cả hai đường | Bản nháp đã viết *«deploy key mất quyền»* kèm việc giao owner. **Đo lại thì THÔNG 3/3 lần** ⇒ chỉ là **trạng thái tạm lúc GitHub lan truyền đổi chủ**. **Sửa trước khi công bố** — nếu để nguyên, kho sẽ có một lỗi vĩnh viễn không tồn tại |
| 3 | Suýt bỏ sót `_v10921_rule_a55.py` vì nghĩ "chỉ là chuỗi văn bản" | Nó **ghi ngược** vào ba mặt quản trị ⇒ bỏ qua sẽ tự hoàn tác việc hôm nay (§60.1) |
| 4 | `grep -r` toàn kho **quá 300 giây** (có `venv`, `backups`, `.git`) | Chuyển sang công cụ tìm kiếm có lọc, quét theo loại tệp |
| 5 | 🔴 Phép thử *«HTTPS ẩn danh đọc kho riêng»* **THÀNH CÔNG** — trông như **kho riêng bị lộ** | `credential.helper = manager` **âm thầm cấp thông tin đăng nhập đã lưu** ⇒ phép thử không hề ẩn danh. Thử lại bằng `curl` thẳng API: **404 đúng như phải thế**. **Suýt báo một P0 bảo mật không có thật** |

---

## 8 · GỠ VỀ

```
# 1 · ba remote
git -C E:\Lottery_AI_Test remote set-url origin git@github.com:irissnss/Lottery_AI_Test.git
git -C E:\Lottery_AI_Notion_Reports remote set-url origin git@github.com:irissnss/Lottery_AI_Notion_Reports.git
# VPS — hoặc khôi phục nguyên bản:
cp /root/Lottery_AI_Test/.git/config.pre_org_20260907 /root/Lottery_AI_Test/.git/config

# 2 · bốn mặt sửa tay
cp backups/v11171_pre_org/CLAUDE.md.pre_org           CLAUDE.md
cp backups/v11171_pre_org/cursorrules.pre_org         .cursorrules
cp backups/v11171_pre_org/AGENT.md.pre_org            .AGENT.md
cp backups/v11171_pre_org/Antigravityrules.md.pre_org .Antigravityrules.md
python web/backend/_v10925_rule_sync_check.py      # sinh lại hai mặt tự động

# 3 · hai script — đổi ngược chuỗi BaoBiTanPhat → irissnss, hoặc git revert commit của bản này
```

**Không có gì cần gỡ ở production** — phiên này không deploy, không restart, không đụng DB.

---

## 9 · THEO DÕI TIẾP

| # | việc | ai làm | mức |
|---|---|---|---|
| 1 | **KHÔNG có việc gì về GitHub cần owner làm.** 24/24 phép kiểm thông, kể cả deploy key của VPS | — | — |
| 2 | Nếu owner đổi tên tổ chức hoặc chuyển kho lần nữa: **chạy lại `docs/GITHUB_KHO_VA_QUYEN.md`** — quy trình + bảng kiểm đã có sẵn, chỉ đổi chuỗi | agent | — |
| 3 | Sau **mọi** thao tác đổi hạ tầng: **đo lại sau vài phút trước khi kết luận hỏng**; và đo **cả đường cũ lẫn mới** | agent | luật mới |
| 4 | Ba việc kỹ thuật của **V11170** vẫn nguyên: ký `SC-12` · sửa `main.py:10491`/`:10511` · `LIMIT 270` ra trước bộ lọc | **owner** | P0–P1 |
| 5 | Năm P0 hạ tầng của **V11166** vẫn nguyên | **owner** | P0 |

---

## §62 — NGUỒN BA LỚP

### `OWNER_SAID`
> *«github có nhưng thay đổi anh chuyển cá nhân sáng Organization tổ chức ảo này có ảnh hưởng đến 4
> link trong ảnh không ? em có bị ảnh hưởng không code và báo cáo có ảnh hưởng gì không em»*
> — ~00:4x 07/09/2026, IDE, kèm hai ảnh chụp bảng tin và danh sách kho của tổ chức.

> *«fix dùm anh đi chứ chờ gì nữa?»* — ~00:5x 07/09/2026.

### `CODE_DID`
- `git ls-remote` — cả hai đường trả **cùng `HEAD`**: `a4d6636` (riêng) · `0720dfb` (công khai).
- `curl` — trang web cũ `301` → tổ chức; `raw.githubusercontent` cũ và mới đều `200`.
- VPS `ssh -T git@github.com` → *"Hi BaoBiTanPhat/Lottery_AI_Test!"* nhưng `ls-remote`
  **`Repository not found`** ở **cả hai** đường.
- VPS `systemctl cat lottery` → `ExecStart=/root/Lottery_AI_Test/venv/bin/python3 main.py`;
  quét crontab → **0 dòng** `git pull`/`git fetch`.
- `_v10925_rule_sync_check.py` → **SÁU MẶT ĐỒNG BỘ**; `_v11027_so_muc_quan_tri.py` → thoát 0.
- `grep irissnss web/backend/*.py .cursor` → **0 kết quả** sau khi sửa.

### `DOC_SAID`
- `CLAUDE.md` §57.2 (trước bản này): *«Repo `https://github.com/irissnss/Lottery_AI_Notion_Reports`»*
  — nay đã đổi sang `BaoBiTanPhat`, và **đồng bộ đủ sáu mặt**.
- `CLAUDE.md` — **BẢNG QUY HOẠCH SÁU MẶT**: `AGENTS.md` và `GEMINI.md` **sinh tự động, cấm sửa tay**
  ⇒ bản này tuân đúng.

**LỆCH GIỮA BA LỚP — phải báo:**
`DOC_SAID` ≠ `CODE_DID` **đã tồn tại trong khoảng từ lúc owner chuyển kho đến lúc bản này chạy**:
sáu mặt quy tắc chỉ agent tới `irissnss/...` trong khi kho thật đã ở `BaoBiTanPhat/...`. Bất kỳ agent
nào đọc luật trong khoảng đó đều nhận địa chỉ **không còn là địa chỉ chính thức** — nó vẫn chạy nhờ
chuyển hướng, nên **lệch này sẽ không bao giờ tự lộ ra**. Bản này đóng khoảng lệch đó.

---

TanPhatAI cần làm: ghi **`V11171`** — `governance_seq 486`, công khai bản này cùng `CONVERSATION_CONTEXT_V11171_20260907.md`. Ghi **BỐN KHO ĐÃ CHUYỂN TỪ `irissnss` SANG TỔ CHỨC `BaoBiTanPhat`** — địa chỉ chính thức từ nay là **`github.com/BaoBiTanPhat/Lottery_AI_Test`** (Private) và **`github.com/BaoBiTanPhat/Lottery_AI_Notion_Reports`** (Public); đường `irissnss/...` chỉ còn sống nhờ chuyển hướng, **cấm ghi vào tài liệu mới**. Ghi **BẢNG KIỂM 24/24 THÔNG** — local đọc/ghi được cả hai kho, người ngoài tải được báo cáo công khai (`raw` 200 cả hai đường), **kho riêng KÍN đúng (404 ẩn danh)**, VPS đọc được qua deploy key, và **VPS KHÔNG cần GitHub để chạy** (0 cron `git pull`, service chạy từ tệp trên đĩa). Ghi **KHÔNG có việc gì về GitHub cần owner làm.** Ghi **đã ghim 3 remote + sửa 12 chỗ trong 6 mặt quy tắc đúng quy trình + 2 script**, và **`_v10921_rule_a55.py` bắt buộc phải sửa cùng** vì nó **ghi ngược** văn bản A55 vào ba mặt — bỏ qua sẽ tự hoàn tác (§60.1). Ghi **HAI BẪY ĐO LƯỜNG đã sập trong phiên này, ghi lại để không lặp**: ① sau thao tác đổi hạ tầng, **một lần đo hỏng KHÔNG đủ kết luận** — `ls-remote` báo `Repository not found` rồi **đo lại thông 3/3**, chỉ là trạng thái tạm lúc GitHub lan truyền; ② `credential.helper = manager` **âm thầm cấp thông tin đăng nhập** khiến phép thử *«ẩn danh»* không hề ẩn danh — **suýt báo một P0 bảo mật không có thật**. Ghi **tài liệu tra cứu thường trực: `docs/GITHUB_KHO_VA_QUYEN.md`** — mọi phiên sau tra ở đó, không đi chẩn lại. **Code KHÔNG đi trước tài liệu** — 0 ghi production, 0 deploy, 0 restart, DB không đụng. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.**
