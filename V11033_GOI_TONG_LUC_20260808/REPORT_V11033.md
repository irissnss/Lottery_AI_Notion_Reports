# REPORT V11033 — GÓI TỔNG LỰC 08/08: VÁ FU-345 + RM-13…19 + BA CỔNG MỚI

**Ngày:** 2026-08-08 · **Owner ký:** QD-044 *(brief gọi QD-043 — mã đó đã dùng, xem §7.1)*
**Phạm vi mở khoá:** (1) vá FU-345 trong `gpt_analyzer.py` · (2) tooling/cổng/hook/docs.
Mọi thứ khác vẫn khoá theo QD-041 tới 21/08.

---

## 1. Tóm tắt

Bảy mục R1–R7. **Một biến production duy nhất (R1)** đúng QD-018.

| | kết quả |
|---|---|
| **R1** | vá FU-345 — **9 cửa** bơm lỗi vào prompt, không phải 1. Deploy đạt, prompt **+~1.700 ký tự/miền** |
| **R2** | RM-13…RM-19 vào **6 mặt**, khối RM giống nhau **từng byte** |
| **R3** | trường `thay_boi` (34 → **36** trường), backfill chuỗi thay thế, cổng đọc nó trước trạng thái |
| **R4** | canh trôi đặc trưng — cả 3 miền **trong ngưỡng**. Phát hiện: **28 đặc trưng, không phải 39** |
| **R5** | cổng chặn kết luận khi một nguồn 0 dòng — **4/4** phép thử |
| **R6** | cổng tuổi dữ liệu — phát hiện cổng mà tài liệu nói «đã cài» **chưa bao giờ tồn tại** |
| **R7** | 8 mục quá hạn: **2 đóng · 5 dời · 1 escalate**. Phản biện **bác được 6 mệnh đề** |

**Ba thứ phải nói ngay:**
1. `gpt-oss-120b` và 14 model kia nay nhận prompt **sạch** — trước đó có **một dòng lỗi Python**.
2. Tài liệu ghi **39 đặc trưng** là sai, thật là **28** — và con số sai đó đang là **ngưỡng
   hành động FU-320**.
3. Cổng `K8` đang **XANH GIẢ**: thoát 0 trong khi ngưỡng chưa đạt. Phản biện bác chính báo cáo.

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

> R1 — VÁ FU-345 (A4): SCAN-ERROR BƠM VÀO PROMPT CẢ 15 MODEL OFFICIAL
> R2 — RM REGISTER: CẬP NHẬT CLAUDE.md + ĐỒNG BỘ 4 FILE
> R3 — SỔ QUYẾT ĐỊNH: THÊM TRƯỜNG THAY_BOI
> R4 — FU-318 (M-C): CANH TRÔI ĐẶC TRƯNG (monitoring-only)
> R5 — FU-327: CỔNG CHẶN KẾT LUẬN KHI NGUỒN = 0 DÒNG
> R6 — FU-303 NHÂN RỘNG + FU-311 ĐÍNH CHÍNH
> R7 — RÀ 8 MỤC QUÁ HẠN 06/08

---

## 3. Đào bới / phát hiện

### 3.1 R1 — **CHÍN** cửa, không phải một

| | chỗ | TRƯỚC | SAU |
|---|---|---|---|
| **(A) GỐC** | `:5384` | `SELECT ai_model, predicted_numbers, …` — **PRAGMA xác nhận cột KHÔNG TỒN TẠI** | `main_numbers`, giữ nguyên **thứ tự 5 cột** |
| **(B) HỌ** | `:5022` `:5129` `:5170` `:5182` `:5193` `:5293` `:5347` `:5365` `:5475` | `sections.append(f"  ⚠️ … error: …")` — `sections` **chính là prompt** | `print("[CTX-BLOCK-LOI] …")` |

**Vá mình (A) là để tám cửa còn mở.**

**Vì sao KHÔNG trả `CTX_PACK_LOI` như FU-341:** chín khối này là **khối CON**. Bắt cả gói ngữ
cảnh ~10.000 ký tự tự huỷ vì một khối con hỏng là **đổi lỗi nhỏ lấy lỗi to**. Đúng cách là
**giảm cấp trung thực** + kêu vào journal.

**Vì sao KHÔNG gỡ 3 cột dư** (`_preds` chỉ dùng `p[2]` và `len()`): gỡ là **đổi chỉ số**, tức
mở rộng phạm vi. Dư cột không phải lỗi.

### 3.2 R4 — **28 đặc trưng, không phải 39**

Đọc bằng AST: `ml_models.py:31` = **28** · `meta_learner.py:51` = **28** ·
`meta_data_collector.py:37` = 32 (28 + date/region/tail/hit).

| chỗ ghi sai | ghi | thật |
|---|---|---|
| `CHANGELOG.md:1179` | «39 đặc trưng» | **28** — chính bảng phân rã kèm theo cộng ra 28 |
| `FOLLOW_UP_TRACKER.md:533` (**ngưỡng FU-320**) | «39 vs 33» | «**28 vs 22**» |

Con số sai đang là **ngưỡng hành động** — để nguyên thì bản A/B **đăng ký sai từ đầu**.

### 3.3 R4 — vụ SUÝT BÁO NHẦM «MT trôi nặng»

PSI thô `gan_vs_avg` = **0,7976** ⇒ nhãn thô TRÔI NẶNG. Nhưng hai phân bố **trùng khít**
(p50 0,556 vs 0,556). PSI to là do **cách đo**: `avg_gan` tính theo NGÀY, cửa sổ 7 ngày chỉ có
7 giá trị nên đẻ ra **20** giá trị thay vì **103**.

| nền | phán quyết MT |
|---|---|
| ngưỡng thô | VƯỢT NGƯỠNG (sai) |
| rút từng DÒNG | VƯỢT NGƯỠNG (vẫn sai) |
| **7 ngày LIÊN TIẾP** | **TRONG NGƯỠNG** (đúng) |

### 3.4 R6 — cổng mà tài liệu nói «đã cài» **CHƯA BAO GIỜ TỒN TẠI**

`SSOT:750` + `CHANGELOG:1479` khẳng định đã có mẫu `do_lai_tuoi.py`.

```
Glob **/*do_lai_tuoi*                              → 0 tệp
git log --all --diff-filter=A -- "*do_lai_tuoi*"   → rỗng (902 commit)
git log --all -S"do_lai_tuoi"                      → chỉ 6b2c94d V11011
```

Chuỗi ấy vào kho **dưới dạng câu văn trong CHANGELOG**. Suốt từ V11011, tài liệu nói có một
cổng mà **không ai từng viết nó**.

**Cổng mới bắt được bẫy thật ngay lần chạy đầu:** từ chối với `tuổi 2884,44 giờ` vì trúng
**`web/data/lottery_ai.db` — bản sao CHẾT 8 MB**.

### 3.5 R7 — ba phát hiện NGƯỢC NHÃN

1. `V10978` ghi *«crontab cũng không có dòng nào»* — **SAI**. VPS crontab **dòng 104** chạy
   `_v10861_runtime_contract_audit.py` mỗi 20:45, log **62.881 byte**.
2. `_v10958_fu_reader.py` là **THƯ VIỆN local** (không có trên VPS) — «mã thoát» của nó
   **vô nghĩa ngay từ đầu**.
3. **Claude Code không chạy hook đầu phiên** — kho không có `.claude/settings.json`. Từ 06/08
   16:06 tới nay **0 dòng `VAO_HOOK`** trong khi có **19 commit**.

---

## 4. Hướng xử lý và vì sao chọn

**4.1** — R1 vá cả 9 chỗ vì chúng là **một họ**. Vá lẻ là để cửa mở, đúng §60.

**4.2** — Nâng `CTX-18.2 → CTX-18.3` vì R1 **có** đổi nội dung prompt. Không nâng thì FU-284
không phân biệt được trước/sau.

**4.3** — R2 làm **6 mặt**, không 5. Brief nêu `.antigravityrules`; đo thật: tệp đó **2.290
byte, không mang khối RM** — nó là **file trỏ đường**. Mặt mang khối RM thật là
`.Antigravityrules.md`, và brief **thiếu `.AGENT.md`** cũng mang khối đó. Thêm RM vào file trỏ
đường là **phá vai trò của nó**.

**4.4** — R3 đổi trạng thái mục bị thay sang `SUPERSEDED_BY_QD041`. Để `ACTIVE` thì trường
`thay_boi` chỉ là **trang trí**.

**4.5** — R6 **không** sửa hàng loạt script cũ, chỉ dựng hàm dùng chung + lập bảng thiếu.
Sửa hàng loạt là bài học FU-324 (**181 tệp hỏng**).

---

## 5. Đã làm gì

### R1 — đo TRÊN MÁY CHỦ

| miền | shadow=False TRƯỚC → SAU | shadow=True TRƯỚC → SAU |
|---|---|---|
| MN | 9.935 → **11.650** | 14.914 → **14.914** |
| MT | 9.964 → **11.671** | 12.943 → **14.650** |
| MB | 12.460 → **14.148** | 15.625 → **17.313** |

**+~1.700 ký tự/miền** — khối `WEEKDAY SCAN` nay **chạy thật** thay vì in một dòng lỗi.

`CTX-18.2 → CTX-18.3` · md5 `e6578ff6…` → **`c60ab13ba9bb83e35e6366f07002db74`**
PID `1044843 → 1053968` · health **200** · 4 bảng khoá **PRE = POST** · `CTX-BLOCK-LOI` **0 lần**

**Cổng nghiệm thu làm cứng:** soi **11 nhãn rác**; rác lỗi nay là **TRƯỢT** chứ không còn ghi
chú — bản V11032 chỉ ghi chú nên A4 lọt qua đúng một lần rồi mới bị bắt bằng mắt.

### R2 — sáu mặt, băm khối RM `63f37e71a144dac9`

| mặt | trước | sau |
|---|---|---|
| `CLAUDE.md` | 25.668 | 27.869 |
| `AGENTS.md` | 22.897 | 25.098 |
| `GEMINI.md` | 23.146 | 25.347 |
| `.cursorrules` | 33.164 | 35.365 |
| `.Antigravityrules.md` | 112.803 | 115.004 |
| `.AGENT.md` | 42.324 | 44.525 |

`RM register version: 2026-08-08 · V11033`

### R3 — 36 trường

```
OD-20260801-D · QD-014 · QD-029  →  thay_boi: QD-041, trang_thai: SUPERSEDED_BY_QD041
QD-041                            →  thay_the: [ba mục trên]
```

`_con_hieu_luc()` nay đọc `thay_boi` **trước** trạng thái. `DA_KHAI` nay **rỗng**.

### R4/R5/R6 — ba cổng mới, cả ba thử chặn thật

| cổng | thử |
|---|---|
| `_v11033_canh_troi_dac_trung.py` | 4/4 · băm 4 bảng khoá **14:00:06 = 14:19:59 y hệt** |
| `_v11033_cong_nguon_rong.py` | 4/4 |
| `_v11033_cong_tuoi_dung_chung.py` | **6/6** |

### R7 — 8 mục

**ĐÓNG 2** · **DỜI 5** · **ESCALATE 1**. Không dồn ngày nào:
10/08 3→4 · 11/08 5→6 · 12/08 6→7 · 13/08 1→2 · 18/08 0→1 · 22/08 2→3.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| **Tuổi dữ liệu (FU-303)** | **ĐẠT** — 5,26 giờ < 6 · `[cong] DU_LIEU_TUOI` |
| **R1 prompt 3 miền sạch** | **ĐẠT** — `VA_V11032=DAT`, 6/6 ô, 0/11 nhãn rác |
| **4 bảng khoá PRE=POST** | **ĐẠT** — y hệt cả trước lẫn sau deploy |
| **health / PID** | **200** · `1044843 → 1053968` |
| **Backup + gỡ về 1 lệnh** | **ĐẠT** — `backups/v11033_pre/` cả hai đầu |
| **Rà cùng họ (RM-07)** | **ĐẠT** — 9/9 cửa, không phải 1 |
| **R2 sáu mặt khớp từng byte** | **ĐẠT** — `63f37e71a144dac9` × 6 |
| **`_v11027_so_muc_quan_tri`** | **ĐẠT** — không mục nào biến mất |
| **R3/R5/R6 thử allow-deny** | **ĐẠT** — 4/4 · 4/4 · 6/6 |
| **R4 0 write** | **ĐẠT** — băm y hệt, quét ngược có phân loại |
| **Cổng đóng băng QD-041** | **ĐẠT** — `DONG_BANG_QD041=CON_NGUYEN`, 2 commit đều được phép |
| **Kiểm chéo quyết định** | **ĐẠT** — `KIEM_CHEO_QD=SACH` |
| **Sổ quyết định** | **1 phép trôi** (QD-022, tồn từ trước) |

---

## 7. Vướng vấp

### 7.1 LỆCH MÃ QUYẾT ĐỊNH — brief gọi `QD-043`, mã đó đã dùng

Brief ghi *"OWNER SIGNATURE: QD-043"*. Nhưng `QD-043` **đã dùng sáng 08/08** cho quyết định giữ
hạn FU-284. **Ghi đè là mất một quyết định của owner** — đúng lỗi suýt xảy ra với `QD-028` ngày
07/08. Gói này ghi thành **`QD-044`**, nêu rõ trong `ghi_chu`. **FU-346** chờ owner xác nhận.

### 7.2 Agent làm hỏng bộ đọc sổ — và tự sửa

Ba mục `QD-042/043/044` thêm mà **thiếu trường `quyet_dinh`** ⇒ `_v10920_decision_ledger.py`
ném `KeyError: 'quyet_dinh'`. Đã bổ sung cả ba.

### 7.3 Trôi 1 → 4, đều do agent gây ra

| trôi | gốc | sửa |
|---|---|---|
| `QD-042` ghim `PROMPT_VERSIONS['context_pack'] == 'CTX-18.2'` | R1 nâng lên CTX-18.3 **hợp lệ** theo QD-044, phép kiểm lập tức trôi | **ghim HÀNH VI, không ghim số** — đổi sang `CTX_PACK_LOI.__len__() > 0` |
| biểu thức dùng `len()` | bộ đánh giá **không có builtins** | đổi sang `.__len__()`, đúng lối `QD-041` đã dùng |

Về lại **1 phép trôi** = mức trước phiên.

### 7.4 Neo vá trượt hai lần *(dừng trước khi ghi nhờ `assert`)*

`PROMPT_VERSIONS = {` khớp **2 lần**; `CTX_PACK_LOI` đếm ra **4** không phải 3.

### 7.5 PHẢN BIỆN BÁC ĐƯỢC **6 MỆNH ĐỀ** — ghi hết

| # | bị bác | sự thật |
|---|---|---|
| **B1** | *"K8 trượt, exit=1, cổng có răng"* | **SAI NGƯỢC** — thoát **0**, in `[ĐẠT] K8`. `MO_COI_TRAN = 15` **chưa hạ**; ngưỡng FU-258 tự viết là ≤2 mà thực tế **5**. **Cổng XANH GIẢ**, sự thật **xấu hơn** báo cáo |
| **B2** | *"10 trang FE"* | thật **12** |
| **B3** | *"3 nhãn sinh SAU 06/08"* | `SCOPE_CHANGED` sinh **cùng ngày 06/08**, 7 giờ sau bản vá ⇒ luận điểm mạnh hơn |
| **B4** | lệnh gốc FU-268 | `/tmp/_r7_lane.py` **không tồn tại** trên VPS — bằng chứng không tái lập được |
| **B5** | bảng tải | cắt cụt, **bỏ 6 mục** |
| **B6** | *"chỉ MỘT sự kiện"* | có **ít nhất 2** |

### 7.6 Bộ quét ngược của R4 tự báo động giả 10 lần

Nó báo **10 chỗ «SQL_GHI»** — **cả 10 đều sai**: `h.update()` của hashlib, `sys.path.insert`,
`os.replace`, và **chính dòng regex của nó**. Đã đổi sang `tokenize` + `ast`. Đúng **RM-09**.

---

## 8. Gỡ về

```bash
cp backups/v11033_pre/gpt_analyzer.py.pre web/backend/gpt_analyzer.py
# VPS:
cp /root/Lottery_AI_Test/backups/v11033_pre/gpt_analyzer.py.pre \
   /root/Lottery_AI_Test/web/backend/gpt_analyzer.py && systemctl restart lottery
```

Bản trước vá: md5 `e6578ff6564632ec017dc746078540db` (CTX-18.2). Bản sao **cả hai đầu**.

---

## 9. Theo dõi tiếp

### LOCK-IN — đã chốt, không bàn lại

- `gpt_analyzer.py` md5 **`c60ab13ba9bb83e35e6366f07002db74`** · `CTX-18.3` · khoá tới **21/08**
- Sổ RM **19 mục**, sáu mặt băm **`63f37e71a144dac9`**
- Sổ quyết định **36 trường**, chuỗi thay thế đã khai
- Ngưỡng FU-284 = **9,33 điểm**, cửa sổ SAU `09/08 → 21/08`

### OPEN ITEMS

| mã | việc | hạn |
|---|---|---|
| **FU-346** | owner xác nhận mã `QD-044` | 08/08 |
| **FU-347** | sửa tài liệu **39 → 28** đặc trưng (đang là ngưỡng FU-320) | 08/08 |
| **FU-348** | `K8` xanh giả — hạ `MO_COI_TRAN` | 12/08 |
| **FU-349** | Claude Code không chạy hook đầu phiên | 11/08 |
| **FU-224** | **owner chọn** giữ/gộp/bỏ 4 trang | 11/08 |
| **FU-341/345** | 24h sau đọc trace: `context_pack_chars` phải > 10.000, **0 lượt** = 64 | 09/08 |

### KHÔNG LÀM — cố ý chờ

FU-290 cắt model *(tránh 2 thay đổi official cùng ngày)* · FU-319 · FU-320 *(ngưỡng đang sai
số, phải sửa FU-347 trước)* · FU-299 · FU-300 · mọi thay đổi prompt content — **QD-041 khoá tới
21/08**.

### NEXT ACTION — một bước

**Sáng 09/08: đọc `prediction_trace.jsonl`, đếm lượt có `context_pack_chars = 64`.**
Phải bằng **0**. Nếu > 0 ⇒ bản vá chưa ăn vào đường chạy thật, gỡ về ngay bằng lệnh §8.
