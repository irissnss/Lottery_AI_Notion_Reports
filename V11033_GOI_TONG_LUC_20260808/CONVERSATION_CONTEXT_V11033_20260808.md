# CONVERSATION CONTEXT — V11033 · 2026-08-08

## Owner giao gì

Prompt TỔNG LỰC 7 mục **R1…R7**, phạm vi mở khoá **chỉ** (1) vá FU-345 trong `gpt_analyzer.py`,
(2) tệp tooling/cổng/hook/docs. Cổng đầu tiên: tuổi dữ liệu > 6 giờ ⇒ **TỪ CHỐI CHẠY**.

## Agent làm gì

Cổng tuổi dữ liệu **5,26 giờ — ĐẠT** (sát ngưỡng). R1 làm trước vì còn **76 phút** trước giờ
chặn deploy 15:00. R2/R3 làm tay; R4–R7 chạy **song song** trong workflow, mỗi mũi có một agent
riêng **cố bác bỏ**.

## Điều quan trọng nhất: R1 không phải MỘT lỗi, mà là CHÍN

Owner giao vá `:5384` + handler `:5475`. Rà theo **RM-07** thì ra **chín** chỗ cùng một khuôn:

```
:5022 Evidence table · :5129 Week-slot · :5170 Direct-hit · :5182 MB 3-tier
:5193 MNMT rule stack · :5293 MB streak · :5347 MB weekday · :5365 MB hard mode
:5475 SP-4.0 scan          ← chỗ đang nổ
```

Mỗi chỗ là **một cửa để lỗi Python chui vào đầu model**, vì `sections` **chính là prompt**.
Vá mình chỗ đang nổ là **để tám cửa còn mở**.

**Không dùng lại cách của FU-341** (trả cờ `CTX_PACK_LOI` giết cả gói): chín khối này là
**khối CON**. Bắt cả gói ~10.000 ký tự tự huỷ vì một khối con hỏng là **đổi lỗi nhỏ lấy lỗi to**.
Đúng cách: **giảm cấp trung thực** — bỏ khối khỏi prompt, kêu thật to vào journal.

**Kết quả đo trên máy chủ:** prompt **dài thêm ~1.700 ký tự/miền** — vì khối `WEEKDAY SCAN` nay
**chạy thật** thay vì in một dòng lỗi. Model trước đây nhận **một dòng báo lỗi Python** thay cho
8 tuần dữ liệu quét.

## Ba con số tài liệu SAI, tìm ra khi làm

| # | chỗ | ghi | thật |
|---|---|---|---|
| 1 | `CHANGELOG.md:1179` + `FOLLOW_UP_TRACKER.md:533` | **39 đặc trưng** | **28** (AST đọc `ml_models.py:31` và `meta_learner.py:51`) |
| 2 | `SSOT:750` + `CHANGELOG:1479` | đã có mẫu cổng `do_lai_tuoi.py` | **CHƯA BAO GIỜ TỒN TẠI** — quét 902 commit, chuỗi ấy vào kho **dưới dạng câu văn** |
| 3 | `V10978` | *"crontab cũng không có dòng nào"* | VPS crontab **dòng 104** chạy hằng ngày, log **62.881 byte** |

Cái số 1 nguy hiểm nhất: **39 đang là ngưỡng hành động FU-320** — để nguyên thì bản A/B đăng ký
sai từ đầu.

## Vấp ở đâu — bảy chỗ, ghi hết

| # | vấp | sửa |
|---|---|---|
| 1 | Neo vá `PROMPT_VERSIONS = {` khớp **2 lần** | đổi neo sang `RUNTIME_PROMPT_VERSIONS = {` |
| 2 | `assert CTX_PACK_LOI == 3` sai, thật là **4** | sửa số |
| 3 | **Làm hỏng bộ đọc sổ** — 3 QD thêm mà thiếu trường `quyet_dinh` ⇒ `KeyError` | bổ sung cả ba |
| 4 | **Trôi 1 → 4**, đều do agent gây | `QD-042` ghim `CTX-18.2` mà R1 nâng lên `CTX-18.3` hợp lệ ⇒ **ghim HÀNH VI, không ghim số** |
| 5 | Biểu thức dùng `len()` | bộ đánh giá **không có builtins** ⇒ `.__len__()`, đúng lối `QD-041` |
| 6 | Cổng nghiệm thu chỉ **ghi chú** rác lỗi | làm cứng: soi **11 nhãn**, rác lỗi nay là **TRƯỢT** |
| 7 | Bộ quét ngược của R4 báo **10 «SQL_GHI»** — **cả 10 sai** (`h.update`, `os.replace`, và **chính dòng regex của nó**) | đổi sang `tokenize` + `ast` |

Vấp 1, 2 **dừng trước khi ghi** nhờ `assert` đặt trước `os.replace` — tệp không hỏng lần nào.

## PHẢN BIỆN BÁC ĐƯỢC SÁU MỆNH ĐỀ CỦA CHÍNH CÁC MŨI

Nặng nhất: **B1 — «cổng K8 trượt, exit=1, cổng có răng» là SAI NGƯỢC.**
`_v10981_kiem_lich.py` thoát **0**, in `[ĐẠT] K8` — trong khi ngưỡng mà FU-258 **tự viết** là
*"tổng mồ côi ≤ 2"* mà thực tế **5**. Cổng không kêu vì `MO_COI_TRAN = 15` **chưa hạ**.

**Sự thật xấu hơn báo cáo.** Gọi nó là «cổng có răng» là **ru ngủ**. Ghi đúng tầng (RM-12):
`CỔNG_XANH_NHƯNG_NGƯỠNG_CHƯA_ĐẠT`, không phải «cổng trượt». Mở **FU-348**.

Năm cái còn lại: 10 vs **12** trang FE · `SCOPE_CHANGED` sinh **cùng ngày** vá chứ không phải
sau · lệnh gốc FU-268 **không tái lập được** · bảng tải **cắt cụt bỏ 6 mục** · «một sự kiện»
thật ra **ít nhất hai**.

## Điều agent NÓI THẲNG với owner

**1. LỆCH MÃ.** Brief ghi *"OWNER SIGNATURE: QD-043"* nhưng `QD-043` **đã dùng sáng nay** cho
quyết định giữ hạn FU-284. Ghi đè là **mất một quyết định của owner** — đúng lỗi suýt xảy ra
với `QD-028` ngày 07/08. Agent ghi thành **`QD-044`** và **không tự quyết** — `FU-346` chờ owner
xác nhận.

**2. LỆCH DANH SÁCH FILE.** Brief nêu `.antigravityrules`. Đo thật: tệp đó **2.290 byte, KHÔNG
mang khối RM** — nó là **file trỏ đường**. Mặt mang khối RM thật là `.Antigravityrules.md`, và
brief **thiếu `.AGENT.md`** cũng mang khối đó. Thêm RM vào file trỏ đường là **phá vai trò của
nó**. Agent làm theo **thực tế: 6 mặt**, và ghi rõ chỗ lệch thay vì im lặng làm theo brief.

**3. Cổng tuổi dữ liệu bắt được bẫy thật ngay lần chạy đầu** — nó từ chối với `tuổi 2884,44
giờ` vì đi ngược từ `web/backend/` và trúng **`web/data/lottery_ai.db`, bản sao CHẾT 8 MB**.
Nếu không có cổng, mọi phép đo chạy từ thư mục đó đã đọc nhầm DB suốt.

**4. R4 suýt báo nhầm «MT trôi nặng».** PSI thô 0,7976 nhưng hai phân bố **trùng khít**. Phải
thêm **dải nền cắt theo 7 ngày LIÊN TIẾP** cờ giả mới tắt. Và script **tự khai giới hạn**: với
cửa sổ 7 ngày, ngưỡng ngành 0,10/0,25 **vô dụng cho 2–4 đặc trưng mỗi miền** — muốn nhạy hơn
phải kéo dài cửa sổ, **cấm hạ ngưỡng**.

**5. Claude Code đang chạy bằng niềm tin.** Kho **không có `.claude/settings.json`**; hook chỉ
đăng ký ở `.cursor/hooks.json`. Từ **06/08 16:06** tới nay **0 dòng `VAO_HOOK`** trong khi git
log 07–08/08 có **19 commit**. §0 CLAUDE.md bắt chạy `_v10920_session_start.py` mỗi phiên —
**không có cổng nào bảo đảm điều đó**. Mở `FU-349`.
