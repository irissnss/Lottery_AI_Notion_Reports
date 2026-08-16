# REPORT V11080 — LUẬT CHUNG vào repo · KHAI DANH TÍNH sáu mặt · CỔNG I1 TỰ-KIỂM-CỔNG

**LIỀN MẠCH 1/2** — Phiên trước (V11079) chặn bộ đo V11057 tự khai READ-ONLY nhưng ghi đè chính
chứng cứ của nó; V11076 trước đó tìm ra gốc bệnh 12 bản trôi là **`.claude/settings.json` chưa hề
tồn tại** ⇒ không hook nào chạy dưới Claude Code.
**LIỀN MẠCH 2/2** — Phiên này (V11080) owner khoá QĐ-A…QĐ-E đêm 16/08: đặt **`LUAT_CHUNG.md`** vào
gốc repo, khai **danh tính + kế thừa** ở mọi file luật gốc, và dựng **cổng I1 tự-kiểm-cổng** —
đúng cổng lẽ ra đã bắt được lỗi V11076.

---

## 1. Tóm tắt

Làm xong **GĐ-0 · GĐ-1 · GĐ-2/I1**, mỗi phần có phép kiểm máy chạy được.
**CHƯA LÀM:** I2 · I3 · I4 · I5 · GĐ-3 · GĐ-4 · GĐ-5 — ghi thẳng là thiếu (§63), không ghi khống.

Ba kết quả đáng kể:

1. **Vá lỗ hổng `DC-20260816/A2`** — bộ sinh cắt `CLAUDE.md` từ `## 0.`, **bỏ nguyên** BẢNG QUY
   HOẠCH SÁU MẶT khỏi `AGENTS.md`/`GEMINI.md`. Hai công cụ tự nạp hai mặt đó **chưa bao giờ đọc
   được** luật *"sáu mặt KHÔNG phải sáu bản sao"*.
2. **Cổng I1 bắt lỗi thật ngay lượt đầu** — `code_quality_guard` chạy ~123s trong khi chính
   `.cursor/hooks.json` khai `timeout: 120` + `failClosed: true` cho nó.
3. **Đo được 18 số hiệu `§` va nhau** giữa hệ quản trị (§0–§63) và sổ luật bơm vào prompt model
   (§1–§26). QĐ-B chưa thi hành.

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

Trích từ SSOT Notion *Hướng Dẫn TanPhatAI V4.0* (`HDAI-V4.0.35`), mục 13.8/13.9:

> **QĐ-B/QĐ-C (16/08 21:57)** — *"các dự án có file luật trùng tên (AGENTS.md, CLAUDE.md…) nhưng
> kiến trúc có thể ngược nhau hoàn toàn — dự án này 'nhiều replica byte-identical ngang hàng',
> dự án khác 'nhiều mặt cố ý khác nhau, có bản nguồn sinh ra bản khác'. Cùng một tên file, hai
> luật ngược nhau — quen dự án này rồi mở dự án kia là sai ngay."*

> **QĐ-D (16/08 22:01)** — *"file luật của dự án chỉ gồm: dòng khai danh tính + một dòng trỏ tới
> bộ luật chung + phần RIÊNG của dự án đó. Cấm chép lại nội dung luật chung vào từng dự án — lặp
> đi lặp lại sẽ sinh lệch phiên bản và thiếu sót vì không nhớ hết. Ngoại lệ duy nhất: nhóm an
> toàn vẫn nằm INLINE tại file nạp gốc."*

> **QĐ-E (16/08 22:35)** — *"mọi dự án đều đọc được Notion qua MCP — Notion là tài liệu (chỉ đọc;
> ghi phải được cấp). SSOT luật chung nằm trên Notion; mỗi repo giữ bản sao tiện đọc
> `LUAT_CHUNG.md` ở gốc (kèm Doc Version)… hai nơi phải khớp Doc Version, lệch thì SSOT Notion
> thắng… cấm sửa tay bản sao trong repo."*

> **QĐ-A (16/08 21:57)** — *"nhóm an toàn thì TUYỆT ĐỐI không tách khỏi file nạp gốc."*
> ⇒ sổ sai lầm **RM giữ nguyên cả bối cảnh**, không cắt gọn.

---

## 3. Đào bới / phát hiện

### 3.1 — Bảng đo GĐ-0(a): kiểm kê bản luật gốc

| mặt | ký tự | dòng | sửa gần nhất |
|---|---:|---:|---|
| `.Antigravityrules.md` | 134.515 B | 2.182 | 11/08 21:46 |
| `.antigravityrules` | 3.164 B | 47 | 15/08 09:00 |
| `.AGENT.md` | 56.584 B | 926 | 11/08 21:46 |
| `.cursorrules` | 45.579 B | 670 | 11/08 21:46 |
| `CLAUDE.md` | 43.654 B | 710 | 11/08 21:46 |
| `AGENTS.md` · `GEMINI.md` | 40.089 / 40.059 B | 671 / 671 | 11/08 21:46 (SINH) |

### 3.2 — Bảng đo GĐ-0(b): cổng tự-kiểm-cổng · **BA ĐƯỜNG NẠP KHÁC HẲN NHAU**

| công cụ | cấu hình **thực sự đọc** | cơ chế | bằng chứng |
|---|---|---|---|
| **Cursor** | `.cursor/hooks.json` | `HOOK_MAY` — 5 hook | cả 5 script **chạy được** trong ngân sách khai |
| **Claude Code** | `.claude/settings.json` | `HOOK_MAY` — 1 hook (`PreToolUse`/Bash → `cong_git_commit.py`) | chạy được, ngân sách 200s |
| **Antigravity** | `.antigravityrules` | **`CHI_VAN_BAN`** | **KHÔNG CÓ CƠ CHẾ HOOK** |

> **Phát hiện phải nói thẳng:** Antigravity **không có cổng máy nào cả**. Mọi câu *"cổng xanh"*
> cho đường này từ trước tới nay **vô nghĩa** — không có cổng để mà xanh. Đây không phải sai sót
> đo đạc, mà là **khai sai hiện trạng**.
>
> **Sổ điểm danh hook** `docs/_HOOK_DIEM_DANH.log` — mục cuối **15/08 09:13**, chỉ ghi hook
> `sessionStart` của **Cursor**. Claude Code **không có** hook `sessionStart` (đúng FU-349).

### 3.3 — Bảng đo GĐ-0(c): phân phối luật, **mang ngày hôm nay**

Dùng `_v11027_kiem_cheo_6_mat.py` (**không** dựng bộ đo thứ hai — cấm chồng tầng):

| | TRƯỚC phiên | SAU phiên |
|---|---:|---:|
| mục có **đủ sáu mặt** | **9 / 100** | **10 / 100** |
| mục **chỉ có ở một mặt** | 79 | 79 *(đúng thiết kế — giữ nguyên)* |
| **LỖI THẬT** — mặt sinh lệch nguồn | **2** (`AGENTS.md`, `GEMINI.md`) | **0** |

### 3.4 — Bảng đo GĐ-0(d): trùng ký hiệu `§` giữa hai hệ

Đã **phân loại**, không đếm chuỗi thô (RM-09 · §60.3):

| hệ | dải số hiệu | nơi định nghĩa |
|---|---|---|
| **QUẢN TRỊ** | §0–§63 (51 số) | 7 file luật gốc |
| **PROMPT MODEL** (sổ luật bơm vào model) | **§1–§26** | `_v11059_prompt_3tang.py:82-83` — *"rulebook `§1–§21`"* (T2 · phương pháp) + *"rulebook `§22–§26`"* (T3 · ràng buộc) |

**⇒ 18 số hiệu va nhau.** Va chạm cụ thể đã xác nhận nằm trong chuỗi bơm prompt: `§10A`/`§10B`
(`prompt_registry.py:40,44`), `§24` BT North Star (`gpt_analyzer.py:843`), `§25`, `§26` KHÔNG
NÓI QUÁ (`_v11008_deploy.py:160`), `§22`/`§23` chống bầy đàn (`_v11059_prompt_3tang.py:161-162`).

Các lần `§` xuất hiện trong **script quản trị** (32 số hiệu) là **vô hại** — chúng trích dẫn luật
quản trị, không bơm vào model.

### 3.5 — Bảng đo GĐ-0(e): rà SCOPE — **KHÔNG tự gán nhãn**

**KHÔNG ĐO ĐƯỢC ĐẦY ĐỦ trong phiên này.** Đo được phần khung: **100 mục** quản trị đang tồn tại
trên sáu mặt, **0 mục** có nhãn `SCOPE`. Đề xuất nhãn cho từng mục là việc của **GĐ-3(b)**, chưa
làm. Theo `GOV-PROJECT-SCOPE-SEPARATION-001`: *điều cũ chưa gắn nhãn vẫn còn hiệu lực như cũ*;
nhóm `CHƯA RÕ` **để nguyên**, cấm tự gán.

### 3.6 — Lỗ hổng `DC-20260816/A2` — cơ chế đầy đủ

```
TRƯỚC:  ban_sinh() → re.search(r"^## 0\.", src)   ⇒ cắt từ "## 0." đầu tiên
        ⇒ BỎ NGUYÊN khối "## BẢNG QUY HOẠCH SÁU MẶT QUẢN TRỊ" nằm ngay TRÊN nó
SAU:    re.search(r"^## BẢNG QUY HOẠCH", src) or re.search(r"^## 0\.", src)
```

**Vì sao trôi im lặng suốt:** `_v10925_rule_sync_check.py` đối chiếu bản sinh với **chính quy tắc
sinh của nó** — một **phép lập luận vòng**, nên luôn in *"SÁU MẶT ĐỒNG BỘ"*. Đúng loại lỗi mà
chính docstring của tệp đó cảnh báo: *bộ kiểm báo xanh cho thứ nó chưa kiểm*.

---

## 4. Hướng xử lý và vì sao chọn

- **`LUAT_CHUNG.md` ghi CẢ HAI số hiệu.** Prompt owner ghi `Doc V1.0.1`, SSOT Notion đang ở
  `HDAI-V4.0.35`. Hai con số **đo hai thứ khác nhau**: `V1.0.1` là số của **bản sao phân phối**,
  `HDAI-V4.0.35` là số của **nội dung nguồn**. Ghi cả hai để cổng đối chiếu **không phải đoán**.
- **Không áp `GOV-FIVE-REPLICA-SYNC-001` vào Lottery.** Luật đó (Owner khoá 16/08 15:41 · B4) nói
  *5 file quản trị = 5 replica byte-identical*. Kiến trúc Lottery **ngược lại**: sáu mặt cố ý
  khác nhau, có bản nguồn sinh ra bản khác. Áp vào sẽ **xoá 79 mục một-bản-duy-nhất**. Chính
  `GOV-RULEFILE-IDENTITY-001` nêu **đúng hai kiến trúc này** làm ví dụ. Đã ghi thành **phụ lục
  cảnh báo** trong `LUAT_CHUNG.md`.
- **Sửa bộ sinh thay vì sửa tay bản sinh.** QĐ-C nói rõ bản sinh nhận hai dòng khai **qua bộ
  sinh**; sửa tay `AGENTS.md` là vi phạm chính luật vừa đặt.
- **KHÔNG làm dở GĐ-3.** Đổi tiền tố hệ quản trị mà sót một matcher dò chuỗi `§` sẽ làm cổng
  A5x/A6x **mù im lặng** — đúng cảnh RM-15 (`git log --since` trả rỗng nên cổng luôn báo xanh).
  §60 nói thẳng: **bỏ nửa chừng còn tệ hơn không làm**.

---

## 5. Đã làm gì (TRƯỚC → SAU → PHIÊN BẢN → KIỂM, theo §60.4)

| # | việc | TRƯỚC | SAU | kiểm |
|---|---|---|---|---|
| 1 | `LUAT_CHUNG.md` | **không tồn tại** | gốc repo · Doc `V1.0.1` / SSOT `HDAI-V4.0.35` | commit `2eacea7` |
| 2 | khai danh tính + kế thừa | **0/6 mặt** | **6/6 mặt** | commit `82ef27a` |
| 3 | bộ sinh `_v10925` | cắt từ `## 0.` | cắt từ `## BẢNG QUY HOẠCH` | `_v11027`: 9/100 → **10/100**, 2 lỗi thật → **0** |
| 4 | cổng **I1** | **không có** | `_v11080_i1_cong_tu_kiem.py` | thử chặn hai chiều **ĐẠT** |
| 5 | `code_quality_guard` | `subprocess.run` **không timeout**, ~123s cold vs ngân sách 120s `failClosed` | `SOI_TIMEOUT=150s`/cổng con · khai báo 120→**300s** | chạy lại **90.358 ms** · `permission=allow` |
| 6 | nâng version bốn mặt | — | CHANGELOG + SSOT + STATE `seq=409` + HISTORY append | `_v11062 --kiem` **K1–K4 ĐẠT** |

**Commit:** `2eacea7` · `82ef27a` · `19e148e` · `82f3a0d`

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11044_cong_so_hieu.py` | `V11080` — **trống**, cấp đúng quy ước (không đoán số) |
| `_v10925_rule_sync_check.py` | ✓ SÁU MẶT ĐỒNG BỘ · mọi `.mdc` tự nạp · không file chết |
| `_v11027_kiem_cheo_6_mat.py` | ✓ *"Hai mặt sinh tự động KHỚP `CLAUDE.md` từng mục"* |
| `_v11062_nang_version.py --kiem` | ✓ `NANG_VERSION_V11062=ĐẠT` — bốn mặt đi cùng nhau |
| **`_v11080_i1_cong_tu_kiem.py --thu-chan`** | ✓ **hai chiều**: sạch → thoát **0**; giấu `.claude/settings.json` → thoát **1** + in `GATES_UNVERIFIED`; **khôi phục nguyên trạng OK** |

---

## 7. Vướng vấp

- **Cách commit trong CLAUDE.md không dùng được ở đây.** Mẹo *"bọc `git commit -m` trong `.cmd`,
  chạy `cmd /c`"* viết cho PowerShell. Ghi `.cmd` bằng heredoc của Bash cho ra **kết thúc dòng
  LF**, `cmd` không thực thi được — treo hết 2 phút rồi rơi. Cách chạy được: `git commit -F
  <file thông điệp>` thẳng trong Bash.
- **`code_quality_guard` từng trả `deny` giữa phiên** — không phải phát hiện thật mà là
  `_v11050_kiem_bien_anchor` **chạy nguội** vượt 150s. Đo lại: nguội **97,4s**, ấm **9,6s**.
  Đã xác minh trước khi kết luận, không báo nhầm thành lỗi chất lượng code.
- **Sáu file INPUT_EVIDENCE của prompt không có trong repo** (`LUAT_CHUNG.md` ·
  `LUAT_TONG_HOP_LOTTERY_20260816.md` · `NC-20260816-I v2` · `DC-20260816` ·
  `03_RIENG_DU_AN_LOTTERY.md`). Đã lấy nội dung luật từ **SSOT Notion** theo QĐ-E (chỉ đọc).
  **Bốn file kia vẫn chưa đọc được** — các mục I1–I5 và B1–B5/C1–C4 trong báo cáo này dựng theo
  **mô tả trong prompt owner + SSOT Notion**, không phải theo bản gốc.

---

## 8. Gỡ về

```bash
git revert 82f3a0d 19e148e 82ef27a 2eacea7      # theo đúng thứ tự ngược
python web/backend/_v10925_rule_sync_check.py   # sinh lại hai mặt sinh theo CLAUDE.md cũ
python web/backend/_v11027_kiem_cheo_6_mat.py   # phải quay về 9/100 + 2 lỗi thật
```

Không đụng DB, không đụng đường dự đoán/chọn số/prompt model, không deploy ⇒ **không có gì phải
gỡ trên VPS**.

---

## 9. Theo dõi tiếp

| mục | việc | hạn |
|---|---|---|
| **FU-349** | Claude Code không chạy hook đầu phiên — **I1 nay đo được**, nhưng vẫn **chưa có** hook `SessionStart` cho Claude Code | 16/08 (quá hạn) |
| **FU-335** | Ghi rõ VAI TRÒ từng mặt vào chính `CLAUDE.md` — **đã làm** qua dòng khai danh tính | 18/08 |
| **mới** | **I2 · I3 · I4 · I5 · GĐ-3 · GĐ-4 · GĐ-5 CHƯA LÀM** — cần một phiên riêng | — |
| **mới** | **18 số hiệu `§` va nhau** giữa hệ quản trị và sổ luật bơm prompt — QĐ-B chưa thi hành | sau 21/08 (vùng đóng băng QD-041) |

> **Chưa sinh mã FU mới trong phiên này** (trần 5 mã/phiên chưa dùng) — để phiên thi hành GĐ-3
> đặt mã cùng lúc với việc, tránh mã mồ côi.

---

## §62 — NGUỒN BA LỚP

### `OWNER_SAID` (nguyên văn + giờ)

| giờ 16/08 | nguyên văn | phân loại OIL |
|---|---|---|
| 21:57 | *"nhóm an toàn thì TUYỆT ĐỐI không tách khỏi file nạp gốc"* (QĐ-A) | `DONG_THUAN` |
| 21:57 | *"tách namespace §: HỆ QUẢN TRỊ đổi tiền tố; hệ prompt MODEL giữ nguyên (đang production)"* (QĐ-B) | `DONG_THUAN` — **chưa thi hành** |
| 21:57 | *"dòng ĐẦU mọi file luật gốc khai: tên dự án · vai trò bản này · kiến trúc · cách sửa"* (QĐ-C) | `DONG_THUAN` — **đã thi hành** |
| 22:01 | *"CẤM chép lặp luật chung. Ngoại lệ: nhóm an toàn inline."* (QĐ-D) | `DONG_THUAN` — **đã thi hành** |
| 22:35 | *"SSOT luật chung nằm trên Notion; LUAT_CHUNG.md trong repo là bản sao tiện đọc — hai nơi phải khớp Doc Version, lệch thì SSOT Notion thắng"* (QĐ-E) | `DONG_THUAN` — **đã thi hành** |
| — | *"LUAT_CHUNG.md (Doc V1.0.1)"* vs SSOT Notion `HDAI-V4.0.35` | **`CHUA_RO`** — xem lệch lớp bên dưới |

### `CODE_DID` (evidence: tệp:dòng · lệnh · output thật)

- `LUAT_CHUNG.md` — tạo mới, 258 dòng, commit `2eacea7`.
- `web/backend/_v10925_rule_sync_check.py:125-131` — `ban_sinh()` đổi mốc cắt; commit `82ef27a`.
- `web/backend/_v11080_i1_cong_tu_kiem.py` — cổng I1 mới, 259 dòng; commit `19e148e`.
- `.cursor/hooks/code_quality_guard.py` — thêm `SOI_TIMEOUT=150`; `.cursor/hooks.json` `120→300`.
- Đo thật: `_v11050_kiem_bien_anchor` **97.400 ms** (nguội) → **9.632 ms** (ấm);
  `code_quality_guard` **90.358 ms**, `permission=allow`.
- `_v11027_kiem_cheo_6_mat.py`: **9/100 + 2 lỗi thật** → **10/100 + 0 lỗi**.
- `_v11062_nang_version.py --kiem`: `seq=409`, `last_version=V11080`, **K1–K4 ĐẠT**.

### `DOC_SAID`

- `Notion · Hướng Dẫn TanPhatAI V4.0 §13.7/13.8/13.9` (`HDAI-V4.0.35`, cập nhật 16/08 22:40).
- `CLAUDE.md §BẢNG QUY HOẠCH SÁU MẶT` — *"sáu mặt KHÔNG phải sáu bản sao… 79 mục chỉ có ở MỘT mặt
  — và đó là ĐÚNG thiết kế"*.
- `CLAUDE.md §61 RM-15` — *"cổng không qua thử coi như KHÔNG TỒN TẠI"*.

### ⚠ BA LỚP LỆCH NHAU — FINDING BẮT BUỘC BÁO

1. **`DOC_SAID` (Notion B4) ≠ `DOC_SAID` (CLAUDE.md).** Notion khoá *5 file quản trị = 5 replica
   **byte-identical** ngang hàng* (`GOV-FIVE-REPLICA-SYNC-001`); `CLAUDE.md` khoá *sáu mặt **cố ý
   khác nhau**, có bản nguồn sinh ra bản khác*. **Hai luật ngược nhau.**
   **Xử lý:** KHÔNG tự chọn bên — `GOV-RULEFILE-IDENTITY-001` đã giải chính xung đột này bằng
   cách nêu **đúng hai kiến trúc đó** là ví dụ về hai dự án khác nhau ⇒ B4 là luật **RIÊNG của
   dự án khác**, không lan sang Lottery. Đã ghi thành phụ lục cảnh báo trong `LUAT_CHUNG.md`.
2. **`OWNER_SAID` ≠ `DOC_SAID` về Doc Version.** Prompt ghi `Doc V1.0.1`; SSOT Notion ghi
   `HDAI-V4.0.35`. **Chưa tự chọn bên** — ghi **cả hai** vào bảng đầu `LUAT_CHUNG.md`.
   **Cần owner xác nhận** `V1.0.1` là số của bản sao phân phối (như đã hiểu) hay là số khác.
3. **`OWNER_SAID` ≠ `CODE_DID` về QĐ-B.** Owner khoá đổi tiền tố hệ quản trị; **mã chưa thi
   hành** — 18 số hiệu `§` vẫn va nhau. Đã đo và ghi, **chưa sửa** (xem mục 4).

---

## VERDICT

```
CODE_PUSHED      : ĐẠT — 4 commit trên master (2eacea7 · 82ef27a · 19e148e · 82f3a0d)
REPORT_PUBLISHED : ĐẠT — thư mục này trên Lottery_AI_Notion_Reports
```

**KHÔNG** ghi `DEPLOYED` và **KHÔNG** ghi `RUNTIME_PROVEN` — phiên này **không deploy**, không
đụng VPS, không đụng DB (RM-12: cấm tự nâng cấp tầng).

---

TanPhatAI cần làm: cập nhật SSOT Notion *Hướng Dẫn TanPhatAI V4.0* §13.8 ghi nhận Lottery_AI_Test đã phát hành bản sao `LUAT_CHUNG.md` Doc `V1.0.1` từ `HDAI-V4.0.35` (16/08), và ghi rõ `GOV-FIVE-REPLICA-SYNC-001` **KHÔNG áp** cho Lottery_AI_Test; theo dõi ba việc còn treo — (a) owner xác nhận số hiệu `V1.0.1` cho bản sao phân phối, (b) QĐ-B đổi tiền tố hệ quản trị **chưa thi hành, 18 số hiệu § còn va nhau**, chỉ làm được sau 21/08 vì vùng đóng băng QD-041, (c) I2·I3·I4·I5 và GĐ-3·GĐ-4·GĐ-5 **chưa làm**, cần một phiên riêng.
