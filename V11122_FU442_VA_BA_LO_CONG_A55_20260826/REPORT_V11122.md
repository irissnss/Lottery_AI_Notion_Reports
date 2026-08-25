# V11122 — `FU-442`: VÁ BA LỖ CỦA CỔNG A55 + VÁ HAI LỖI CỦA CHÍNH KHOÁ PHIÊN `V11121`

**Ngày:** 26/08/2026 · **Commit riêng:** `2ee0f9a` · **Commit công khai:** *(bản này)* ·
**Trạng thái:** `READ-ONLY` với production

---

## 1. Tóm tắt

Prompt 37 `GĐ-0` + `GĐ-1`. Hai việc:

1. **Preflight bắt hai lỗi trong module `V11121` vừa dựng đêm trước.** Tiến trình Claude Code khởi
   động lại (`PID 17016` → `18000`) nhưng `CLAUDE_CODE_SESSION_ID` **giữ nguyên** ⇒ nhánh «cùng
   phiên» chạy **trước** phép kiểm PID chết, lease làm mới nhịp tim mà **vẫn ghi PID đã chết** làm
   chủ. Lỗi hai: đếm ngược tính từ `lay_luc` trong khi phép hết hạn dùng `cham_luc` ⇒ in
   *«còn −11 777s»* trên một lease vừa được làm mới. **Đã vá cả hai**, thử lại **8/8 ĐẠT**.
2. **`FU-442` — vá ba lỗ của cổng A55**, thử chặn **11/11 ĐẠT**, và **tự sửa hai chỗ** trong lúc vá
   để cổng không thành vô dụng.

## 2. Owner yêu cầu gì (nguyên văn)

> *« **IX. P4 — GOVERNANCE** — 1. Xác minh/vá A55: worklist = `git log ∪ CHANGELOG ∪ report
> directories`. 2. Chạy cả chế độ chỉ định version và toàn dải. 3. Xác nhận hoặc bác `R5` bằng
> output thật. … 5. Sửa `CLAUDE.md §0` đang dạy chế độ mù. 7. Xác định rõ cổng có được nối vào hook
> hay không. 8. Nếu chưa nối: giải thích; mở decision riêng; **không để `grep=0` im lặng**. »*
> — prompt 37, `26/08/2026`

## 3. Đào bới / phát hiện

### 3.1 · Ba lỗ, xác nhận bằng output thật

Cùng một phiên, cùng một phút, cùng trạng thái kho:

```
_v10921_report_gate.py V11119   → soi 1 bản · "MỌI PHIÊN BẢN ĐỀU CÓ BÁO CÁO" · thoát 0
_v10921_report_gate.py          → soi 8 bản · V11117 V11115 V11112 THIẾU  · thoát 1
```

| # | lỗ | neo mã | thiệt hại đo được |
|---|---|---|---|
| ① | băng-rôn **toàn cục** in khi worklist chỉ có **một** phần tử | `:229` `dsach = chi_dinh or phien_ban_gan_day()` · `:355-356` | `CLAUDE.md §0` **đang dạy đúng chế độ mù** |
| ② | cửa sổ cắt cứng `[:8]` | `:84` `n=8` · `:144` `[:n]` | trong **40** bản gần nhất có **11** thiếu, cổng báo **3**; 8 bản vô hình |
| ③ | sắp theo **SỐ HIỆU**, không theo **thời gian commit** | `:141-144` `key=_so` | `V11037c` commit **hôm đó** nhưng số `11037` ⇒ rơi ngoài cửa sổ **ngay trong ngày tạo** |

### 3.2 · Lỗ ② **tự diễn lại ngay trong ngày** — bằng chứng mạnh nhất

`20:0x` cổng bắt `V11117 · V11115 · V11112`. `21:0x`, sau khi `V11120`/`V11121` chen vào top-8,
chạy lại thì **`V11112` biến mất khỏi danh sách** — dù **chưa ai bù báo cáo cho nó**.
Một bản lỡ một lần rồi trôi quá 8 bản là **vô hình vĩnh viễn**.

### 3.3 · 🔴 HAI CHỖ PHẢI TỰ SỬA TRONG LÚC VÁ — nếu không thì cổng thành vô dụng

Lần chạy toàn dải **đầu tiên** cho **`424/575` trượt**. Con số đó **vô dụng**:

| chỗ sai | vì sao | cách sửa |
|---|---|---|
| ép luật **ngược** lên bản có trước khi luật tồn tại | `A55` owner ký `01/08/2026 11:04`, dựng ở **`V10921`** (`V10921_RULE_A55_20260801/REPORT_V10921.md` — chính là tên tệp cổng). Bắt bản tháng 4–7 phải có `REPORT_*.md` là **cổng đỏ vì lý do sai** | khoá `MOC_THI_HANH_A55 = 10921` |
| coi **hậu tố chữ** là bản riêng | `V11120b` là commit phụ của **cùng** một bản; nhưng `V10964b` lại là bản riêng **thật** | hậu tố chỉ tính là bản riêng khi có **mục CHANGELOG riêng** hoặc **báo cáo riêng** |

Đây đúng bài học chính tệp cổng đã ghi cho `§62`: *«cổng đỏ vì lý do sai thì người ta sẽ học cách
bỏ qua nó, và cổng coi như chết»*.

**Sau khi sửa hai chỗ đó:** `51/200` trượt · **`32` bản thiếu báo cáo thật**.

> **Đính chính phạm vi:** «10 bản thiếu» của `V11119`/prompt 36 đúng cho **dải hẹp
> `V11070–V11199`**. Trên **toàn dải từ mốc thi hành**, con số là **32**. Hai con số **không mâu
> thuẫn** — khác phạm vi.

### 3.4 · 🔴 Cổng A55 **không được nối vào bất kỳ hook nào**

`grep _v10921` ra **0 dòng** ở cả bốn nơi: `.claude/settings.json` · `.claude/hooks/cong_git_commit.py`
· `.cursor/hooks.json` · `.cursor/hooks/*.py`.

## 4. Hướng xử lý và vì sao chọn

| lối | vì sao chọn / loại |
|---|---|
| giữ `[:8]`, chỉ sửa băng-rôn | ❌ **không đủ** — lỗ ② là lỗ làm bản trôi thành vô hình |
| bỏ `[:8]`, soi tất cả từ đầu lịch sử | ❌ **cổng đỏ vì lý do sai** — 424/575 trượt, con số vô dụng |
| **bỏ `[:8]` + khoá mốc thi hành `V10921` + luật hậu tố** ✅ | con số **có nghĩa**: 32 bản thiếu thật, đều nằm sau ngày luật ra đời |

**Vì sao KHÔNG tự nối cổng vào hook:** nối cứng sẽ **chặn mọi commit** cho tới khi bù đủ 32 (nay 23)
báo cáo. Đó là **quyết định vận hành**, không phải kỹ thuật ⇒ mở `FU-444` thay vì tự làm.

## 5. Đã làm gì

| tệp | thay đổi |
|---|---|
| `web/backend/_v10921_report_gate.py` | `+chi_muc_bao_cao()` (quét kho **một lần**, khoá theo **cả** tên thư mục **và** tên tệp) · `+_thoi_gian_commit()` · `+pham_vi_day_du()` · `+_diem_danh_a55()` · băng-rôn theo phạm vi · **fail-closed** ở tầng ngoài |
| `web/backend/_v11120_session_lease.py` | vá 2 lỗi: làm mới `pid`/`pid_start` khi cùng phiên · đếm ngược từ `cham_luc` |
| `web/backend/_v11122_thu_chan_a55.py` | **mới** — 7 phép + hai chiều |
| `CLAUDE.md §0` + `AGENTS.md` + `GEMINI.md` | thôi dạy chế độ mù; dạy **chạy cả hai theo thứ tự** |

**KHÔNG deploy · KHÔNG restart · KHÔNG ghi DB.**

## 6. Cổng kiểm

| phép | kết quả |
|---|---|
| `_v11122_thu_chan_a55.py` | ✅ **11/11 ĐẠT**, mã thoát 0 |
| — `T1` bản thiếu **ngoài** top-8 cũ | bắt được **30 bản** |
| — `T2` **số cũ, commit mới** | `V11037C` nay **đứng đầu** worklist |
| — `T3` kiểm một version | **không** in verdict toàn kho; có cảnh báo + số bản chưa kiểm |
| — `T4` phạm vi sạch | thoát **0** |
| — `T5` cổng **nổ** | thoát **2**, in `FAIL-CLOSED`; `--soft` vẫn ép về 0 |
| — `T6` sổ điểm danh | có dòng `CONG_A55` |
| — `T7` **hai chiều** | bẩn ⇒ chặn · sạch ⇒ cho qua |
| `_v11120_thu_chan_lease.py` sau khi vá | ✅ **8/8 ĐẠT** |
| `_v10925_rule_sync_check.py` | ✅ **SÁU MẶT ĐỒNG BỘ** |
| `_v11062_nang_version.py --kiem` | ✅ **ĐẠT** |
| `py_compile` | ✅ OK |

## 7. Vướng vấp

1. **Lần chạy toàn dải đầu tiên cho một con số vô dụng** (`424/575`). Nếu công bố nó thì mọi người
   sẽ học cách bỏ qua cổng. Phải dừng lại, tìm **mốc thi hành thật** (`V10921`) và **luật hậu tố**,
   rồi chạy lại. *Hậu quả nếu bỏ qua:* giết chính cổng vừa vá.
2. **Bộ quét route của agent bỏ sót bản vá của chính mình** (cửa sổ 14 dòng, docstring mới dài hơn)
   ⇒ báo nhầm *«chưa gắn cổng»*. Quét lại với cửa sổ 34 dòng mới đúng.
3. **Hai lỗi trong module vừa dựng đêm trước** — chỉ lộ ra vì tiến trình khởi động lại giữa hai
   phiên. Nếu không khởi động lại thì không ai thấy.

## 8. Gỡ về

`git revert 2ee0f9a`. Hoặc từng phần: cổng A55 là một tệp; lease là một tệp; `CLAUDE.md §0` là một
khối. **Không có migration DB, không đụng mã production.**

## 9. Theo dõi tiếp

| mã | việc | ngưỡng đóng bằng số |
|---|---|---|
| `FU-442` | ✅ **ĐÓNG** — ba lỗ đã vá, thử **11/11** | đã đạt |
| `FU-444` *(mới)* | nối cổng A55 vào đường commit | sổ điểm danh có `CONG_A55` ở **mỗi** commit |
| — | bù nốt **23** bản còn thiếu báo cáo | `_v10921_report_gate.py` không tham số ⇒ danh sách `THIẾU BÁO CÁO` rỗng |

---

## 10. BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`
> *«Xác nhận hoặc bác `R5` bằng output thật.»* · *«Sửa `CLAUDE.md §0` đang dạy chế độ mù.»* ·
> *«Nếu chưa nối: giải thích; mở decision riêng; **không để `grep=0` im lặng**.»*
> — prompt 37, `26/08/2026`

### `CODE_DID`
| điều mã **thực sự** làm | bằng chứng |
|---|---|
| cùng phút, hai chế độ cho hai kết luận ngược nhau | thoát `0` + băng-rôn toàn cục ↔ thoát `1` + 3 bản thiếu |
| `V11112` **biến mất** khỏi danh sách trong vòng một giờ | chạy `20:0x` có · `21:0x` không, vì `V11120`/`V11121` chen vào top-8 |
| cổng **không nối** hook nào | `grep _v10921` = **0 dòng** ở 4 nơi |
| lease ghi **PID đã chết** làm chủ | `--xem` in *«tiến trình ĐÃ CHẾT»* trên lease của chính phiên |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `CLAUDE.md §0` (trước bản này) | `_v10921_report_gate.py <VERSION>` | 🔴 **dạy đúng chế độ mù** — đã sửa |
| `.cursorrules:376-377` · `.Antigravityrules.md:542-543` · `.AGENT.md:444-445` | dạy **đủ hai chế độ** từ trước | 🟢 **khớp** — thiếu chỉ ở `CLAUDE.md` |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID`: tài liệu vận hành chính (`CLAUDE.md §0`) dạy chế độ mù trong khi ba mặt
sửa tay dạy đúng — nghĩa là **lỗi nằm ở đúng mặt agent đọc đầu tiên mỗi phiên**.

---

**TanPhatAI cần làm:** ghi nhận (a) `FU-442` **ĐÓNG**, cổng A55 nay soi **toàn dải từ mốc thi hành
`V10921`**, sắp theo **thời gian commit**, băng-rôn **nói đúng phạm vi**; (b) con số bản thiếu báo
cáo là **32** trên toàn dải (sau khi bù 10 còn **23**), **không phải 10** — 10 là của dải hẹp
`V11070–V11199`, hai con số không mâu thuẫn; (c) cổng **chưa được nối vào hook nào** ⇒ `FU-444`
chờ owner; (d) `CLAUDE.md §0` đã thôi dạy chế độ mù — **thói quen chạy** mới là thứ phải đổi.
