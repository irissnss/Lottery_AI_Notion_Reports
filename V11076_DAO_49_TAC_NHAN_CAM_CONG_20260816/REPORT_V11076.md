# REPORT V11076 — ĐÀO 49 TÁC NHÂN · CẮM CỔNG VÀO CLAUDE CODE · BÙ 12 BẢN TRÔI

**Ngày:** 2026-08-16 · **Mã đọc:** `DA1608` · **Quyết định:** `QD-067`
**Production KHÔNG đổi** — không deploy, không restart · `QD-041` nguyên vẹn

---

## 1. Tóm tắt

Owner yêu cầu tung khối lượng agent lớn đi đào toàn dự án. **49 tác nhân · 40 phát hiện · 31
đứng vững sau phản biện đối kháng · 9 bị bác.**

**Phát hiện nặng nhất — và nó giải thích mọi thứ khác:**

> **Toàn bộ hàng rào cổng của dự án CHƯA BAO GIỜ CHẠY trong các phiên Claude Code.**

Hệ quả đo được: **12 nhãn version trôi 4 ngày** (13/08→16/08) mà `CHANGELOG` · `SSOT` · `STATE` ·
`HISTORY` **đều đứng ở V11065**, kho báo cáo công khai **không có thư mục `V1107*` nào** — trong
đó có **hai thay đổi chạm production thật**.

Đã cắm cổng (RM-15 ba chiều đạt), bù 12 dòng `HISTORY`, bù 12 báo cáo công khai, và đóng `FU-316`
bằng một phép đo cho kết quả **ngược với dự đoán của chính agent**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Làm hết các đề xuất đó đi, rồi tiến hành phân tích đánh giá dự đoán hôm nay… tóm lại nên xem
> chuyển hoá thuần ngữ cảnh cho model để model AI tự phân tích theo năng lực thay vì nhồi nhét
> vào nha em. nhồi cái đúng ko nói, nhồi cái sai, nhồi cái quá sai bầy đàn thôi bó tay luôn đó em»*

> *«anh phải nói rằng em làm việc vẫn chểnh mảng lắm rơi rớt tùm lum, anh phải nhắc đi nhắc lại,
> nhấn mạnh nhiều lần mệt mỏi quá em. Hãy đưa ra khối lượng agent lớn đi làm việc khắp nơi trong
> dự án để đào cho ra cho chỗ thiếu sót»*

> *«làm hết đi giao nhiệm vụ thì làm đi, làm sao phải tổng lực không rơi rớt… cấm đoán bừa, suy diễn»*

---

## 3. Đào bới / phát hiện

### 3.1 · GỐC BỆNH — cổng có mà chưa bao giờ được gọi

| kiểm | kết quả |
|---|---|
| `~/.claude/settings.json` | chỉ có `effortLevel` + `model` — **không có khoá `hooks`** |
| `<kho>/.claude/settings.json` | **không tồn tại** |
| `git config core.hooksPath` | rỗng |
| `.git/hooks/` | **không hook nào** ngoài `.sample` |
| `.cursor/hooks.json` | tên sự kiện **của Cursor** (`sessionStart`, `beforeShellExecution`) — Claude Code **không đọc** |

20 commit gần nhất đều mang trailer `Claude Opus 5` ⇒ do **Claude Code** tạo. Nghĩa là **8 cổng
trong `code_quality_guard` + `truncation_guard` + `governance_guard` chưa cái nào chạy** trong
chính các phiên đã làm trôi 12 bản.

> Trớ trêu: `_v11028_cong_dong_bang.py` đã tự ghi câu *«Một cổng phải nhớ gọi là một cổng không
> tồn tại»* — rồi chính nó thành nạn nhân của câu đó.

### 3.2 · Hậu quả — 12 bản trôi, gồm hai thay đổi chạm production

```
git log --since=2026-08-13    → 14 commit, 12 nhãn version (V11066…V11075)
ls E:/Lottery_AI_Notion_Reports/V1107*   → No such file or directory
CHANGELOG · SSOT · STATE · HISTORY       → đều đứng ở V11065 (12/08)
git ls-remote origin main (kho công khai) → 9e954be = đúng bằng local ⇒ GitHub cũng đứng 12/08
```

Hai bản chạm production: **`9d6c4fd`** bật **WAL** cho DB sống (restart `lottery`, PID
1438110→1633166) và **`b023eca`** vá **lane giữ khoá DB làm mất 2 kết quả model**.

**TÁI PHẠM đúng ngày đến hạn xử lần trước:** `FU-375 · «TÁM COMMIT 25/07 KHÔNG CÓ BÁO CÁO CÔNG
KHAI» · hạn 16/08`. Lần trước 8 commit, lần này 12. Đã đi tìm đường chối — không có mục nào owner
miễn `§57.2`.

### 3.3 · `FU-316` — hạn MỒ CÔI, và phép đo cho kết quả NGƯỢC

`FU-316` đẻ **07/08** hạn **14/08**. **Một ngày sau**, owner ký `QD-041` mở rộng phạm vi sang đúng
`gpt_analyzer.py`. Hạn 14/08 **thành bất khả thi ngay hôm sau khi đặt**, và **không ai gắn lại
hạn** ⇒ nó rơi khỏi **cả gói 21/08 lẫn hàng đợi**.

**Thứ đang bơm vào prompt** (`gpt_analyzer.py:5958`):

```python
d1_union = hợp toàn bộ đuôi MN+MT+MB ngày D-1     →  trung bình 71,3 đuôi
dòng hiển thị = sorted(d1_union)[:12]              →  LUÔN 12 đuôi NHỎ NHẤT
```
Cắt bỏ **59,3 đuôi/ngày = 83%**, và **30/30 ngày** dòng đó **không chứa đuôi nào > 21**.

**Ngưỡng đăng ký TRƯỚC khi chạy:** `CÓ NEO ⇔ chênh ≥ +2,5pp VÀ |z| ≥ 2`.

| | |
|---|---|
| model official chọn đuôi 00–21 | **20,2%** (553/2.733) |
| **nền thực nghiệm** (đuôi THẬT SỰ về) | **21,0%** (641/3.049) |
| pool ĐẦY ĐỦ `d1_union` | 20,9% |
| **chênh** | **−0,79pp · z = −1,01** |

⇒ **KHÔNG đủ bằng chứng có neo.** Model chọn đuôi thấp **ít hơn** nền.

> **Cả agent lẫn bản đào đều nghiêng về «CÓ NEO» trước khi chạy.** Ngưỡng đăng ký trước là thứ
> duy nhất ngăn agent kết luận theo cảm tính. Không có nó, báo cáo này đã ghi *«tìm ra nguyên
> nhân»* cho một thứ không tồn tại.

### 3.4 · Dự đoán 16/08 — 0/3

| miền | BT | hạng | luật thô | nền |
|---|---|---|---|---|
| MN | `71` | #1 (11 phiếu) | `71` cùng số — cũng trượt | 40% |
| **MT** | `53` | **#2** | **`01` (hạng #1, 9 phiếu) — TRÚNG** | 38% |
| MB | `28` | #1 (11 phiếu) | `28` cùng số — cũng trượt | 23% |

Nền 1,01/3 = 33,7%. **MT lại là ca trọng số làm mất số trúng.**

Chạy lại `FU-400` với dữ liệu mới (**449 miền-ngày**, +12 ô):

> **A (trọng số) 33,4% · B (luật thô) 35,9% · A−B = −2,45pp · z = −1,192 · VIF 1,082**
> A cứu **27** · A hại **38** · hai luật trùng nhau **64,1%** · MB lệch nặng nhất (18,4% vs 23,4%)

Vẫn **chưa đủ bằng chứng** (`|z| < 1,96`), nhưng điểm ước lượng **ổn định qua 3 lần đo liên tiếp**
(−2,75 → −2,45).

---

## 4. Hướng xử lý và vì sao

**Cắm cổng trước, dọn sau.** Bù tài liệu mà không cắm cổng thì tuần sau lặp lại y hệt — đó là bài
học của chính `FU-375` (lần trước chỉ bù, không cắm).

**HAI BẪY khi chuyển hook Cursor → Claude Code** (đã đo, không phải lo xa):

1. **Chép nguyên = CỔNG CÂM.** `truncation_guard.py:41` và `code_quality_guard.py:96` đều
   `return 0` **ngay cả khi từ chối**, chỉ báo bằng `{"permission":"deny"}` — khoá **riêng Cursor**.
   Claude Code đọc **mã thoát**, và **`2` mới là CHẶN**.
2. **`matcher` khác nghĩa.** Cursor khớp **regex trên chuỗi lệnh**; Claude Code khớp **TÊN CÔNG
   CỤ**. `"matcher": "git commit"` **không bao giờ nổ** — phải lọc lệnh **bên trong** hook.

---

## 5. Đã làm gì

| # | việc | bằng chứng |
|---|---|---|
| 1 | Đào 49 tác nhân, mỗi phát hiện qua **một phản biện riêng** được lệnh **cố bác bỏ** | 40 → **31 đứng vững**, 9 bị bác |
| 2 | **Cắm cổng** `.claude/settings.json` + `.claude/hooks/cong_git_commit.py` (6 cổng) | RM-15 ba chiều |
| 3 | **RM-15 thử chặn** | `git commit` ⇒ **thoát 2 CHẶN** · lệnh khác ⇒ 0 · cờ bỏ qua ⇒ 0 |
| 4 | Bù **12 dòng `HISTORY`** với `nguon="bu_16_08"` + `ghi_that_ngay` | §63 gate **ĐẠT** |
| 5 | Bù **12 báo cáo công khai** từ commit message, có banner bù | commit `f4c4576` |
| 6 | Dựng `_v11077_do_neo_pool_d1.py`, **đóng `FU-316`** bằng nhánh 2 | gói giữ **14 mục** |
| 7 | Phân tích dự đoán 16/08 + chạy lại `FU-400` | mục 3.4 |

**Đáng chú ý:** ngay lần thử đầu, cổng mới **bắt đúng lỗi đang mắc** — `§63 TRƯỢT, HISTORY im 4
ngày`. Agent **không commit được** cho tới khi bù xong.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `.claude/hooks/cong_git_commit.py` — RM-15 | **✓ ĐẠT ba chiều** |
| `_v11062_nang_version.py --kiem` (§63) | **✓ ĐẠT** sau khi bù (118 mục, seq 408) |
| `_v10921_report_gate.py` V11066…V11075 | **✓ 11/11 có báo cáo** sau khi bù |
| `_v10920_decision_ledger.py` | **✓ 0 trôi** |
| RM-01 cổng tuổi dữ liệu | **✓** trong cả hai bộ đo |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| nguyên văn (trích) |
|---|
| *«em làm việc vẫn chểnh mảng lắm rơi rớt tùm lum, anh phải nhắc đi nhắc lại… mệt mỏi quá em»* |
| *«Hãy đưa ra khối lượng agent lớn đi làm việc khắp nơi trong dự án để đào cho ra cho chỗ thiếu sót»* |
| *«nên xem chuyển hoá thuần ngữ cảnh cho model… nhồi cái đúng ko nói, nhồi cái sai»* |
| *«cấm đoán bừa, suy diễn»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| `.claude/settings.json` **không tồn tại**, `.git/hooks/` trống | kiểm trực tiếp hệ tệp |
| 14 commit / 12 nhãn version trong 4 ngày, tài liệu đứng ở V11065 | `git log --since=2026-08-13` |
| dòng pool D-1 cắt **83%**, 30/30 ngày không đuôi > 21 | `_v11077_do_neo_pool_d1.py` |
| model chọn 00–21 ở **20,2%** vs nền **21,0%** | cùng script |
| trọng số vs luật thô: **−2,45pp** trên 449 miền-ngày | `_v11065_do_trong_so.py` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| `§57.2` *«Không có báo cáo công khai = phiên chưa xong»* | **⚠ VI PHẠM 12 lần** — nay đã bù |
| `_v11028` *«cổng phải nhớ gọi là cổng không tồn tại»* | **khớp** — và chính nó là nạn nhân |
| `FU-316` hạn 14/08 | **⚠ hạn MỒ CÔI** — `QD-041` (08/08) làm nó bất khả thi từ hôm sau |

### Ba lớp lệch nhau ⇒ FINDING

1. **`DOC_SAID` ≠ `CODE_DID` về cổng:** tài liệu mô tả một hàng rào 8 cổng; thực tế **không cổng
   nào chạy** trong môi trường đang được dùng.
2. **`OWNER_SAID` đúng, agent sai:** owner nói *«rơi rớt tùm lum»* — đo được **12 bản trôi**.

---

## 7. Vướng vấp

| # | vấp | quy tắc |
|---|---|---|
| 1 | **12 bản trôi 4 ngày** — tái phạm đúng ngày đến hạn xử `FU-375` | **§57.2** |
| 2 | Agent **nghiêng về «có neo»** trước khi đo; nếu không đăng ký ngưỡng trước đã kết luận sai | **RM-03** |
| 3 | Phiên trước agent nói *«rules chỉ cộng điểm, không sinh số»* — **thiếu**; Context Pack **CÓ** bơm rules vào prompt | **RM-14** |
| 4 | Bản đào đưa lên 40 phát hiện, **9 sai** — trong đó 4 cái sẽ làm owner mất công kiểm hộ | phản biện đối kháng đã chặn |

---

## 8. Gỡ về

```bash
git revert 1582fef      # cắm cổng + bù HISTORY
git revert a33b86a      # FU-316
git -C E:/Lottery_AI_Notion_Reports revert f4c4576   # 12 báo cáo bù
```

Không deploy, không restart, không chạm production.

---

## 9. Theo dõi tiếp

| mã | việc | mốc |
|---|---|---|
| ~~`FU-316`~~ | ~~pool D-1 neo model~~ | **ĐÓNG 16/08** — không neo, không chiếm slot gói |
| **`FU-375`** | tái phạm báo cáo công khai — **nay đã có cổng chặn** | theo dõi 1 tuần |
| **`FU-400`** | trọng số vs luật thô — `−2,45pp`, ổn định qua 3 lần đo | ~90 ngày nữa |
| **`FU-404`** | nhãn `HR12W` nói quá — **trong gói 21/08** | **21/08** |
| **GÓI 21/08** | **14 mục** | **21/08** |
| — | 31 phát hiện đứng vững từ đợt đào — chưa xử hết | chờ owner xếp ưu tiên |

---

TanPhatAI cần làm: ① ghi **gốc bệnh**: `.claude/settings.json` không tồn tại ⇒ **toàn bộ hàng rào
cổng chưa bao giờ chạy** trong phiên Claude Code — nay đã cắm, RM-15 đạt; ② ghi **`FU-375` tái
phạm** (12 bản, lần trước 8) và **đã bù xong** 12 dòng HISTORY + 12 báo cáo công khai, mỗi bản có
**banner bù** phân biệt ngày việc vs ngày viết; ③ ghi **`FU-316` ĐÓNG** — pool D-1 cắt 83% nhưng
**KHÔNG neo** model (−0,79pp, z=−1,01), **cấm suy rộng** thành «mọi nhồi nhét đều vô hại»;
④ ghi **`FU-400` cập nhật**: −2,45pp trên 449 miền-ngày, ổn định qua 3 lần đo, vẫn chưa đủ bằng
chứng; ⑤ **31 phát hiện đứng vững** từ đợt đào chưa xử hết — cần owner xếp ưu tiên.
