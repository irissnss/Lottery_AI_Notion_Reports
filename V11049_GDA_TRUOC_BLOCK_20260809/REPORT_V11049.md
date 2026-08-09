# REPORT V11049 — GĐ-A (2 GIỜ TRƯỚC BLOCK DEPLOY)

**Ngày:** 2026-08-09 **12:04:47 → 12:21:59** giờ VN (đồng hồ VPS = đồng hồ local, cùng `+07`) · **Tầng verdict:** `RUNTIME_PROVEN`
(bốn lần deploy, đo trên production) cho A1/A2/A3/A4 · `REPORT_PROVEN` cho D1

## 1. Tóm tắt

Owner giao 4 việc theo thứ tự rủi ro. **Việc số 1 — mục P0 nặng nhất — hoá ra dựa trên tiền đề
SAI của chính agent**, và agent phát hiện bằng cách đo lại trước khi động vào.

| việc | kết cục |
|---|---|
| **A1** vá `SESSION_SECRET` | ⛔ **KHÔNG có lỗ hổng** — đã chứng minh. **Không xoay secret.** Vẫn làm cứng (fail-fast + gỡ chuỗi mặc định + chmod 600) |
| **A2** FU-387 `MANUAL_REQUIRED` | ✅ xong + deploy · 9 ca lịch sử nay báo đúng |
| **A3** FU-389 gộp vào 18:05 | ✅ xong + deploy · bộ nay **25 phép** · chờ lượt 18:05 |
| **A4** gỡ 2 bảng chết | ⚠ **1 RETIRED · 1 DỪNG** theo đúng luật owner (còn 4 điểm đọc sống) |
| **D1** ngưỡng FU-284 n=12 | ✅ **9,33 → 9,53**, commit **trước khi nhìn số** (RM-03) |

**Không deploy nào chạm khung cấm.** Khung thật đọc từ `.cursor/hooks/governance_guard.py` là
**05:00–06:30** và **15:30–18:15** — **không phải ~14:00** như prompt owner ghi. Lượt deploy cuối
(`systemctl show lottery -p ActiveEnterTimestamp`) là **12:20:12**, cách mốc 15:30 **3 giờ 10**.

*Mốc thời gian lấy từ máy, không từ trí nhớ:* `/root/lottery.service.pre_v11049` **12:04:47** (vật
thể đầu tiên của GĐ-A) · `main.py.pre_v11049` 12:09:17 · `deploy_api.py.pre_v11049` 12:11:37 ·
`guard.py.pre_v11049` 12:13:51 · restart cuối **12:20:12** · `_v11033_verdict_fu284.py` 12:21:59.

## 2. Owner yêu cầu gì (nguyên văn)

> **A1. 🔴 P0 — VÁ SESSION_SECRET (owner ký 11:57). Việc nặng nhất, làm ĐẦU TIÊN.**
> … production ký cookie phiên bằng chuỗi nằm sẵn trong mã nguồn…
> **d) ĐỔI HÀNH VI MẶC ĐỊNH TRONG CODE:** nếu `SESSION_SECRET` không được khai thì `main.py`
> TỪ CHỐI khởi động (fail-fast) — chuỗi hardcode trong mã nguồn phải biến mất.

> **A4.** … Bước 1: quét mọi điểm ĐỌC hai bảng. **Nếu còn một điểm đọc thật nào → DỪNG, báo,
> không gỡ.**

> **TRẦN SINH MÃ:** tối đa 5 mã FU mới toàn phiên.

## 3. Đào bới / phát hiện



### ⛔ A1 — «P0 SESSION_SECRET» LÀ TIỀN ĐỀ SAI. KHÔNG CÓ LỖ HỔNG.

Owner ký 11:57 giao A1 là *«việc nặng nhất, làm ĐẦU TIÊN»*, dựa trên kết luận V11045 của agent:
*«production đang ký cookie phiên bằng chuỗi nằm sẵn trong mã nguồn»*.

**Đo lại trước khi xoay bất cứ thứ gì — và kết luận đó SAI:**

| bằng chứng | |
|---|---|
| `main.py:106` | `_env_path = load_project_env()` |
| `main.py:177` | `load_project_env(override=True)` |
| `main.py:206` | dòng dùng `SESSION_SECRET` |
| ⇒ | **cả hai lần nạp đều TRƯỚC dòng 206** |
| `env_loader.py:6` | `PROJECT_ENV_PATH = <gốc dự án>/.env` → `load_dotenv(...)` |
| `.env` gốc (quyền **600**) | có `SESSION_SECRET` **86 ký tự**, **không** trùng chuỗi mặc định |

Chạy lại đúng thứ tự trên VPS: `do dai = 86 · la MAC DINH = False` ⇒ **dòng 206 dùng secret
thật**.

**Vì sao agent đo sai lần trước:** đọc `/proc/PID/environ` — đó là môi trường **lúc exec**, không
phải `os.environ` runtime mà `load_dotenv` ghi vào. Sai công cụ đo, không sai dữ liệu.

**KHÔNG xoay secret.** Xoay là đá toàn bộ phiên đang sống để đổi lấy con số không.

**Vẫn làm cứng (A1d owner yêu cầu — phần này đúng giá trị):**

| | TRƯỚC | SAU |
|---|---|---|
| thiếu `SESSION_SECRET` | app **vẫn khởi động**, lặng lẽ dùng chuỗi mặc định | **TỪ CHỐI khởi động** (`RuntimeError`), yêu cầu ≥32 ký tự |
| chuỗi mặc định trong mã | có, kể cả trong chú thích | **gỡ hẳn** — `grep` toàn `main.py` = 0 |
| `web/backend/.env` | quyền **666** (ai cũng ghi được), chứa khoá API | **600** |

*(`.env` gốc — cái thật sự được nạp — vốn đã 600. Tệp `web/backend/.env` là **bản sao thừa**,
`env_loader` không nạp; chỉ 3 script test cũ chạm tới.)*

**RM-15:** thiếu biến ⇒ **thoát 1 CHẶN** · 10 ký tự ⇒ **thoát 1 CHẶN** · 86 ký tự ⇒ **thoát 0**.
Deploy: PID 1167898 → 1169259 · health 200 · **0 dòng lỗi** trong log khởi động · secret **không
đổi** (dấu vân tay `3dee0b54e13f`, phiên đang sống không bị đá).

### A2 — FU-387: API deploy nay BÁO THẬT (phương án c)

`deploy_api.py:530` cũ ghi `status: "skipped"`, và dòng `overall` coi `skipped` là **PASS**.
Nay: nếu bỏ restart **mà có tệp `.py` dưới `web/backend/`** ⇒ `status: MANUAL_REQUIRED`, và
`overall` **không còn là PASS**. Tệp tĩnh thì vẫn `skipped` (FileResponse đọc đĩa mỗi lượt).

**Thử trên 4 ca thật:**

| ca | CŨ | MỚI |
|---|---|---|
| đẩy `main.py` *(9 ca lịch sử)* | PASS | **MANUAL_REQUIRED** |
| đẩy `gpt_analyzer.py` + html | PASS | **MANUAL_REQUIRED** |
| chỉ tệp tĩnh *(2 ca vô hại)* | PASS | PASS |
| `.py` ngoài backend | PASS | PASS |

**Không đụng cơ chế runtime** (owner cấm) — chỉ sửa đúng cái sai: **báo cáo không đúng sự thật**.

### A3 — FU-389: `_shadow_phase_audit` GỘP thành phép **C25**, bộ 18:05 nay **25 phép**

Owner dặn *«gộp cùng các phép đo, không cần lạ rõ»* ⇒ **không dựng cron riêng**.

**Ba lần sửa vì ba dương tính giả, ghi lại hết:**

| lượt | kết quả | vì sao sai |
|---|---|---|
| ① đếm tuyệt đối | «156 trường thiếu» | model **tổng hợp** (`combo-super`, `combo-no-token`) không gọi LLM, `reasoning_json` cấu trúc khác — không thể đòi 3 trường |
| ② so theo model | «mất 3 model» | ngày **chưa xong**: 41/81 lượt, mới nhất 05:31; MT 16:58 · MB 17:58 chưa tới |
| ③ so theo cặp (model, miền) | «12 cặp, toàn /MT» | MT có bản ghi sớm nhưng lượt chính thức chưa chạy |
| ④ **gác theo giờ** | trước 18:00 ⇒ **CHƯA ĐỦ NGÀY**, không kết luận | đúng: mốc cuối MB 17:58, bộ chạy 18:05 |

**Chưa tuyên bố đạt** — lượt 18:05 tối nay mới là số liệu hợp lệ đầu tiên.

### A4 — hai bảng chết: một RETIRED, một **DỪNG theo đúng luật owner**

Owner dặn: *«còn một điểm đọc thật nào → DỪNG, báo, không gỡ»*.

| bảng | writer có cron | điểm đọc | xử |
|---|---|---|---|
| `weekday_blackspot_shadow` | **0** | chỉ 1 **nhãn** `_v87_master_board.py:237` ghi cứng `"LIVE V54"` | nhãn → **`RETIRED 2026-05-05`** |
| `mt_model_hit_output_drop_shadow` | **0** | **4 điểm đọc trong `main.py`** (`:11881 :11918 :14923 :14935`), thuộc route SỐNG `/api/du-doan-test/mb` và `/api/du-doan-test/{region}` | **DỪNG — không gỡ** |

Kèm sửa một nhãn sai nữa: `C-06 loz_stage_trace_shadow` cũng ghi `"LIVE V54"` trong khi ngừng ghi
từ 05/05 → đổi thành **«NGỪNG GHI 2026-05-05; DỮ LIỆU CÒN GIÁ TRỊ: ~85% đuôi trúng chưa model nào
sinh ra»**.

**KHÔNG `DROP TABLE`** — dữ liệu giữ tới 21/08 rồi quyết, đúng lệnh owner.

### D1 — NGƯỠNG FU-284 TÍNH LẠI CHO n=12, ĐĂNG KÝ TRƯỚC KHI NHÌN SỐ (RM-03)

Owner chốt **20/08** ⇒ cửa sổ SAU **13 → 12 ngày** ⇒ sức phát hiện giảm ⇒ **ngưỡng phải nâng**.

```
he_so = √((1/14 + 1/12) / (1/14 + 1/13)) = √(0,154762 / 0,148352) = 1,02138
NGUONG_DIEM = 9,33 × 1,02138 = 9,5294  →  9,53
```

`NGUONG_Z = 1.96` · `VIF = 2.92` · `N_TOI_THIEU = 150` **giữ nguyên**.
Dẫn xuất đầy đủ: `docs/NGUONG_FU284_N12_20260809.md`, **commit trước mọi phép đo**.

**Giữ 9,33 trên cửa sổ ngắn hơn là tự nới alpha mà không khai.** Và phải nói trước: 9,53 điểm là
mức rất cao — cải tiến thật cỡ 3–5 điểm sẽ **không** vượt ngưỡng trong 12 ngày, kết quả đúng khi
đó là **«chưa được phép kết luận»**, không phải «không có tác dụng».


---

## 4. Hướng xử lý và vì sao chọn

**A1 — đo trước khi động, và dừng khi tiền đề sập.** Xoay secret là **đá toàn bộ phiên đang
sống**. Làm việc đó dựa trên một kết luận chưa kiểm lại thì cái giá là thật còn lợi ích là con
số không. Nhưng phần **A1d** (fail-fast) vẫn giữ nguyên giá trị kể cả khi không có lỗ hổng: nó
biến một bẫy ngủ thành lỗi ồn.

**A4 — dừng đúng chỗ owner bảo dừng.** Bốn điểm đọc nằm trong hai route đang sống. Luật owner
viết rõ, và agent theo, kể cả khi biết bốn truy vấn đó chắc chắn trả 0 dòng.

**D1 — nâng ngưỡng chứ không giữ.** Cửa sổ ngắn đi mà giữ ngưỡng cũ là **tự nới alpha mà không
khai**. Commit trước khi nhìn số là điều kiện để phép đo còn giá trị.

## 5. Đã làm gì — mọi thay đổi production

| # | thay đổi | PID trước → sau | nghiệm thu |
|---|---|---|---|
| A1 | `main.py` fail-fast + gỡ chuỗi mặc định; `web/backend/.env` 666 → **600** | 1167898 → **1169259** | health 200 · 0 dòng lỗi · secret **không đổi** (`3dee0b54e13f`) · `/monitoring`=401 |
| A2 | `deploy_api.py` `MANUAL_REQUIRED` | 1169259 → **1169604** | health 200 · `/api/_system/deploy/health` ok |
| A3 | `_v10900_consistency_guard.py` thêm **C25** | *(không restart — script cron)* | chạy thật trên VPS: **25 phép** · nhánh «chưa đủ ngày» OK · nhánh 18:05 chạm thật |
| A4 | `_v87_master_board.py` hai nhãn `LIVE V54` → đúng sự thật | 1169604 → **1171150** | health 200 · `/du-doan` 200 · `/monitoring` 401 |

**4 bảng khoá:** không chạm ngoài SELECT. **QD-041 còn nguyên** (`DONG_BANG_QD041=CON_NGUYEN`).

## 6. Cổng kiểm

**Cổng cấp số hiệu FU-369** (chạy TRƯỚC khi cấp mã, theo lệnh owner):

```
V  : 395 số · cao nhất V11048 · trống tiếp: V11049   ✓ dùng V11049
FU : 259 số · cao nhất FU-390 · trống tiếp: FU-391   ✓ dùng FU-391
QD : 42 số  · cao nhất QD-054 · trống tiếp: QD-055   (không dùng)
```

**Trần sinh mã: 1/5** — chỉ `FU-391` mới trong GĐ-A. Còn 4 suất.

| cổng | kết quả |
|---|---|
| `O_STATUS_V11044` | **DAT** (265 khối) |
| `LEGACY_TREO_V11048` | **DAT** (97, trần 97) |
| `_v11015_cong_chan_cat_cut` | **0** |
| `DONG_BANG_QD041` | **CON_NGUYEN** |
| `KIEM_CHEO_QD` | **SACH** |

**RM-15 — ba phép thử chặn thật trong GĐ-A:**
- A1 fail-fast: thiếu biến ⇒ **thoát 1** · 10 ký tự ⇒ **thoát 1** · 86 ký tự ⇒ **thoát 0**
- A2 `MANUAL_REQUIRED`: 4 ca thật, 2 chuyển trạng thái, 2 giữ nguyên (đúng phân định)
- A3 C25: nhánh trước-18:00 và nhánh sau-18:00 đều chạy thật trên VPS

## 7. Vướng vấp

**7.1 — Việc P0 nặng nhất dựa trên kết luận sai của chính agent.** Chi tiết §3. Nguyên nhân:
đo bằng `/proc/PID/environ` (môi trường lúc exec) thay vì `os.environ` runtime. Nếu không kiểm
lại, agent đã **xoay secret production, đá toàn bộ phiên đang sống, để sửa một thứ không hỏng** —
và câu sai vẫn nằm trong báo cáo công khai. **Đã chèn đính chính vào REPORT V11045.**

**7.2 — C25 phải sửa BA lần vì ba dương tính giả khác nhau.** Đếm tuyệt đối → model tổng hợp
không gọi LLM. So theo model → ngày chưa xong. So theo cặp → MT chưa tới lượt chính thức. Chỉ khi
**gác theo giờ** mới hết nhiễu. Bài học: một phép đo trên dữ liệu chạy rải trong ngày **phải khai
rõ nó chỉ có nghĩa khi nào**.

**7.3 — Bẫy CRLF lần thứ tư trong hai ngày.** Chèn C25 lần đầu thất bại vì mẫu dùng `
` trên
tệp CRLF. Đây là bẫy CLAUDE.md đã ghi, và agent vẫn dính.

**7.4 — C25 lần đầu ghi vào kết nối đã đóng.** Chạy thử thật trên VPS mới lộ («Cannot operate on
a closed database») — nếu không chạy thử mà tin `PARSE OK` thì cổng đã lên production hỏng.

## 8. Gỡ về

```bash
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test &&   cp backups/main.py.pre_v11049 web/backend/main.py &&   cp backups/deploy_api.py.pre_v11049 web/backend/deploy_api.py &&   cp backups/guard.py.pre_v11049 web/backend/_v10900_consistency_guard.py &&   systemctl restart lottery'
git revert <commit V11049>
```
Unit systemd **không đổi** (backup vẫn ở `/root/lottery.service.pre_v11049`). Secret **không
xoay** nên không có gì phải khôi phục.

## 9. Theo dõi tiếp

| mã | việc | chờ ai |
|---|---|---|
| `FU-391` | `mt_model_hit_output_drop_shadow` còn 4 điểm đọc sống — (a) bật lại writer · (b) gỡ cả 4 điểm rồi RETIRED · (c) để nguyên, sửa nhãn | **owner** |
| `FU-389` | lượt **18:05 tối nay** — số liệu C25 hợp lệ đầu tiên | cron |
| `FU-390` | 97 mục treo trong archive — ba phương án | **owner** |
| `FU-388` | chạy soi `_v10705` (chiều ĐÀI) | **owner** |
| GĐ-B | B1 vá biên `anchor_date` · B2 `loz_stage_trace` 96 ngày · B3 soi `_v10705` · B4 `FU-160/162/164` · B5 K3 drift 37 tệp · B6 `QD-047` kiem_code · B7 `FU-360` thiết kế lại | read-only, sau block |
| GĐ-C | C1 18:05 = 25 phép gồm C23/C24/C25 · C2 19:35 lane `la_do_lui=0` · C3 bầy đàn · C4 trace 0×64 | tối nay |

---

## LOCK-IN / OPEN / NEXT ACTION

**LOCK-IN:** không có lỗ hổng `SESSION_SECRET` (đã chứng minh, không xoay) · chuỗi mặc định **gỡ
hẳn** khỏi mã + fail-fast · `web/backend/.env` 666 → 600 · API deploy **báo thật** · bộ 18:05 nay
**25 phép** · hai nhãn `LIVE V54` sai đã sửa · ngưỡng FU-284 **9,53** commit **trước khi đo** ·
4 lần deploy đều xong trước khung cấm 15:30.

**OPEN:** `FU-391` ba phương án · `FU-390` 97 mục · `FU-388` · cộng sáu mục treo từ V11046.

**NEXT ACTION:** GĐ-B (read-only, không deploy) · **18:05 và 19:35 tối nay** đọc C1/C2 ·
**20/08** đọc FU-284 với ngưỡng 9,53 đã chốt.

*Đẩy cùng commit (A55 · §57.2).*
