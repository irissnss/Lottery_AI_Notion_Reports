# REPORT V11146 — TRUY RA VÌ SAO **MN MẤT HẲN KHỐI `🎯 RULE TAILS`** · và một phép tự động **BỊ TỪ CHỐI** vì cho kết quả vô nghĩa

> **Ngày:** 01/09/2026 · `ACTOR_RUNTIME = CLAUDE_CODE` · **Commit riêng:** `adafaa7`
> **Theo dõi:** `FU-447` · `FU-448`

---

## 1 · Tóm tắt

Hai việc, một dương một âm — **cả hai đều báo**:

**🔴 Dương:** cảnh báo `LỆCH MIỀN` mà cổng `_v11107` để lại ở `V11144` (*«có thể ĐÚNG thiết kế»*)
truy ra **KHÔNG phải thiết kế**. MN **không bao giờ** nhận khối `🎯 RULE TAILS` mà MT/MB nhận —
tức ba miền đang chạy trên **hai bộ hướng dẫn khác nhau**, và **không ai cố ý tạo ra chênh lệch
đó**. Khai `FU-448`.

**⚪ Âm:** thử tự động hoá `FU-447` (16 báo cáo tiêu đề ngoài khung) và **TỪ CHỐI kết quả** vì bộ
gán tự động cho ra ánh xạ vô nghĩa. Ghi lại phép thử thay vì im lặng bỏ.

---

## 2 · Owner yêu cầu gì — nguyên văn

> **01/09 ~12:00** — *«Các vấn đề kiểm soát, xác định có thể xử lý ngay còn gì xử lý tiếp đi,
> chú ý báo cáo đầy đủ nha em»*

Bảng **13 câu nguyên văn** của owner trong phiên và ba mệnh lệnh `OWNER-01/02/03` nằm ở
`CONVERSATION_CONTEXT` cùng thư mục và `docs/SO_TUONG_TAC_OWNER.md`.

⚠️ **TanPhatAI:** owner trao đổi liên tục trong IDE nên **code thường đi trước tài liệu** — điều
owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`). Tài liệu cũ mâu thuẫn thực tế đang
chạy thì **thực tế + sổ tương tác thắng**.

---

## 3 · Đào bới / phát hiện

> ⚠️ **BẢN NÀY KHÔNG TUYÊN BỐ HIỆU QUẢ CỦA LUẬT — `PRJ-SELECTION-WINDOW-001` không áp dụng.**
> Mọi con số dưới đây là **ĐẾM SỐ DÒNG** (bao nhiêu luật có dòng chấm trong 2 ngày, phân theo
> tier), **không** phải tỉ lệ trúng, **không** phải so với nền. Vì không có tuyên bố hiệu quả nào
> nên **không có** phép tách trong/ngoài cửa sổ chọn ở đây. **CẤM trích** các con số này làm bằng
> chứng hiệu quả của luật MN — chúng chỉ nói về **việc chấm có chạy hay không**.

### 3.1 🔴 `FU-448` — cơ chế, đo trên DB VPS

`gpt_analyzer.py:4877-4886` sinh khối `🎯 RULE TAILS (48h)` từ:

```sql
SELECT e.tails_produced, r.score, r.source_region, r.prize_keys
FROM mined_rule_effectiveness e JOIN mined_rules r ON e.rule_id = r.id
WHERE e.target_region = ? AND r.target_weekday = ? AND r.is_active = 1
  AND e.date >= date('now','-2 days')
  AND r.production_tier IN ('READY_STRONG','READY_WITH_CAUTION')
```

Không dòng nào thoả ⇒ `if _tail_rows:` không vào ⇒ **khối không được bơm vào prompt**.

**Đo được — tái lập bằng một câu:**

| miền | `LIMITED_WEIGHT` | `READY_WITH_CAUTION` | `READY_STRONG` | **đủ tư cách** |
|---|---|---|---|---|
| MB | 5 | 4 | 1 | **5** |
| MT | 5 | 2 | 3 | **5** |
| **MN** | **10** | **0** | **0** | **0** |

### 3.2 Và MN **KHÔNG thiếu luật tốt** — đây mới là chỗ bất ngờ

> ⚠️ **KHÔNG TUYÊN BỐ HIỆU QUẢ — `PRJ-SELECTION-WINDOW-001` không áp dụng.** Các con số là
> **ĐẾM SỐ DÒNG / SỐ LUẬT**, **không** phải tỉ lệ trúng, **không** so với nền. **CẤM trích** làm
> bằng chứng hiệu quả. Không có phép tách trong/ngoài cửa sổ chọn vì không có tuyên bố nào.

`mined_rules` đang `is_active`:

| miền | `READY_STRONG` | `READY_WITH_CAUTION` | `LIMITED_WEIGHT` |
|---|---|---|---|
| MN | **6** | 4 | 25 |
| MT | 5 | 14 | 16 |
| MB | 3 | 14 | 18 |

MN có **nhiều `READY_STRONG` nhất**. Vấn đề **không phải** *«MN không có luật tốt»*, mà là
**luật tốt của MN không được chấm hiệu quả** — mọi dòng `mined_rule_effectiveness` gần đây của
MN đều thuộc `LIMITED_WEIGHT`.

### 3.3 Hệ quả

Mệnh lệnh `REASONING_RULEBOOK:113` — *«Khi nhận được "🎯 RULE TAILS": …»* — **không bao giờ kích
hoạt cho MN**, trong khi MT/MB dùng bình thường.

Nối được với cảnh báo mãn tính đã ghi 31/08: `RULE_QUALITY_ALERT '0 READY_STRONG rules'` cho MN
— **cùng một gốc**.

### 3.4 ⚪ Kết quả ÂM — `FU-447` không tự động hoá được

Bộ gán tự động «phần khung → mục thật» (đếm từ khoá trong thân mục) cho ra:

```
V11135  THIẾU gỡ về        → ## 14 · DECISION PACKET — MỘT CÂU OWNER CẦN KÝ
V11128  THIẾU đào bới      → ## 8 · BA LỚP NGUỒN (§62)
V11132  THIẾU đã làm gì    → ## 9 · MUTATION LOG
```

**Vô nghĩa.** Ghi theo đó thì người đọc sau sẽ đi tìm *«gỡ về»* ở mục Decision Packet và không
thấy gì — **gán sai còn tệ hơn để thiếu**.

---

## 4 · Hướng xử lý và vì sao

### `FU-448` — ba hướng, agent KHÔNG tự chọn

1. **Sửa bộ chấm** để luật `READY_*` của MN cũng được ghi `mined_rule_effectiveness` ⇒ MN nhận
   khối như MT/MB. **Đổi prompt của MN** ⇒ cần owner ký.
2. **Chấp nhận lệch miền có chủ ý** — ghi thành thiết kế và **gỡ** cảnh báo `LỆCH MIỀN` khỏi cổng
   để nó không kêu mãi.
3. **Đo trước, quyết sau** — dựng lane shadow đo MN có/không khối này, như `D-30` đang làm.

Cả ba đều đổi **prompt production** hoặc **một luật quản trị** ⇒ ngoài thẩm quyền agent.

### `FU-447` — dừng lại, không làm ẩu

Giữ nguyên trạng thái treo. Phải **đọc từng bản** rồi viết ánh xạ thật, hoặc ghi
*«không áp dụng vì …»* đúng như §57.3 đòi. Không có đường tắt.

---

## 5 · Đã làm gì — `TRƯỚC / SAU / PHIÊN BẢN / KIỂM` (§60.4)

```
TRƯỚC:  cảnh báo LỆCH MIỀN của _v11107 để ngỏ, ghi «có thể ĐÚNG thiết kế» — chưa ai truy
        FU-447 chưa thử cách nào
SAU:    FU-448 khai mới, có cơ chế + số đo + ba hướng
        FU-447 đã thử tự động hoá và TỪ CHỐI, ghi rõ vì sao
PHIÊN BẢN: commit adafaa7 · KHÔNG deploy · KHÔNG restart · production không bị đụng
KIỂM:   mọi số đo chạy `sqlite3 -readonly` trên DB VPS (OWNER-02), không phải bản chụp local
```

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| `NANG_VERSION_V11062` `K1..K4` | ✅ ĐẠT |
| `SO_HIEU_V11044` | ✅ KHỚP — `FU-448` là số trống kế tiếp |
| nguồn đo | ✅ **DB VPS** `mode=ro`, đúng `OWNER-02` |
| production | ✅ **không đụng** — bản này chỉ đo và ghi tài liệu |

---

## 7 · Vướng vấp

**🟡 Suýt tin cảnh báo của cổng mà không truy.** `_v11107` ghi *«có thể ĐÚNG thiết kế — BÁO,
không chặn»*. Nếu dừng ở đó thì đã bỏ qua một chênh lệch **không ai cố ý** giữa ba miền. Cảnh báo
«có thể đúng» **không phải** kết luận «đúng».

**🟡 Bộ gán tự động cho kết quả vô nghĩa** — đã từ chối. Ghi lại để phiên sau **không làm lại
đúng cách sai đó**.

**🟡 Một lệnh `git commit` nối bằng `&&` im lặng không chạy** — tôi tưởng đã commit, thực ra chưa;
phát hiện nhờ `git log` không có bản mới. Đã tách lệnh và commit lại.

---

## 8 · Gỡ về

```bash
git revert adafaa7      # repo-only, production không bị đụng
```

---

## 9 · Theo dõi tiếp

| # | việc | chặn ở đâu |
|---|---|---|
| 1 | **`FU-448`** — MN mất khối `RULE TAILS` | 🔴 **chờ owner chọn 1 trong 3 hướng** |
| 2 | **`FU-448` phần chưa truy** — vì sao luật `READY_*` của MN không được chấm | ⚪ agent làm tiếp được |
| 3 | **`FU-447`** — 16 bản tiêu đề ngoài khung | ⚪ phải đọc từng bản, **không tự động hoá được** |
| 4 | `FU-444` · `FU-446` · `FU-445` · `CAP5` · quyền thư mục | 🔴 chờ owner |
| 5 | `FU-430` mốc 2 `06/09` · mốc 3 `13/09` | ⚪ để chạy tiếp |
| 6 | 26 bảng còn bị đọc / 38 lane nghỉ | ⚪ đã đo, chưa xử |

---

## 10 · Nguồn ba lớp (§62)

### `OWNER_SAID`
*«Các vấn đề kiểm soát, xác định có thể xử lý ngay còn gì xử lý tiếp đi»* (01/09 ~12:00).
Đủ 13 câu nguyên văn ở `CONVERSATION_CONTEXT` cùng thư mục và `docs/SO_TUONG_TAC_OWNER.md`.

### `CODE_DID`

> ⚠️ **BẢN NÀY KHÔNG TUYÊN BỐ HIỆU QUẢ CỦA LUẬT — `PRJ-SELECTION-WINDOW-001` không áp dụng.**
> Mọi con số dưới đây là **ĐẾM SỐ DÒNG** (bao nhiêu luật có dòng chấm trong 2 ngày, phân theo
> tier), **không** phải tỉ lệ trúng, **không** phải so với nền. Vì không có tuyên bố hiệu quả nào
> nên **không có** phép tách trong/ngoài cửa sổ chọn ở đây. **CẤM trích** các con số này làm bằng
> chứng hiệu quả của luật MN — chúng chỉ nói về **việc chấm có chạy hay không**.
`gpt_analyzer.py:4877-4886` (truy vấn sinh khối) · `REASONING_RULEBOOK:113` (mệnh lệnh) ·
truy vấn đo trên `mined_rule_effectiveness ⋈ mined_rules` **trên DB VPS** · commit `adafaa7`.

### `DOC_SAID`
`CHANGELOG.md §V11146` · `docs/CURRENT_TRUTH_SSOT.md §V11146` ·
`docs/FOLLOW_UP_TRACKER.md → FU-448` (mới) và `FU-447` (giữ treo).

### Ba lớp lệch nhau
`DOC_SAID` ≠ `CODE_DID`: cổng `_v11107` **ghi** *«có thể đúng thiết kế»*, nhưng mã + dữ liệu cho
thấy **không phải thiết kế** — là lỗ hổng chấm luật. Cảnh báo «có thể» đã nằm đó từ `V11144`
mà chưa ai truy; nay truy xong.

---

TanPhatAI cần làm: ghi **`FU-448`** — MN **không bao giờ** nhận khối `🎯 RULE TAILS` mà MT/MB nhận, **KHÔNG phải thiết kế**: MN có **6 `READY_STRONG` + 4 `READY_WITH_CAUTION`** đang `is_active` (nhiều nhất trong ba miền) nhưng **0** luật nào được chấm hiệu quả trong 2 ngày. Hệ quả: **ba miền chạy trên hai bộ hướng dẫn khác nhau, không ai cố ý**. Cùng gốc với `RULE_QUALITY_ALERT '0 READY_STRONG rules'` ghi 31/08. **Chưa kết luận MN mất gì** (`RM-04`). Ba hướng xử **đều cần owner ký**. Ghi **`FU-447` KHÔNG tự động hoá được** — bộ gán tự động cho ánh xạ vô nghĩa, đã từ chối, phải đọc từng bản.
