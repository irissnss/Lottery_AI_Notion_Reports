# V11111 — 2026-08-24 (trưa) — ẢNH CHỤP FINAL BẤT BIẾN · RÚT LẠI `FU-436` (trần `300s` không áp cho `glm-5.1`)

**Ngày làm việc:** 24/08/2026 ·
**Ngày viết báo cáo này:** 26/08/2026 · **Commit riêng:** `daf8cd8` ·
**Trạng thái:** `BÙ TỪ NGUỒN GỐC`

---

> ## ⚠️ ĐÂY LÀ BÁO CÁO **BÙ**, KHÔNG PHẢI BẢN VIẾT LÚC LÀM VIỆC
>
> Bản `V11111` làm ngày **24/08** nhưng **không có** thư mục báo cáo công khai —
> vi phạm `§57.2` đã tồn tại **2 ngày**.
> Cổng A55 cũ **không thấy** vì nó chỉ soi **8 bản gần nhất** (đã vá ở `V11122`, `FU-442`).
>
> **Ba nguồn dựng nên bản này — cả ba đều là bản ghi ĐƯƠNG THỜI:**
>
> | nguồn | quy mô |
> |---|---|
> | khối `## V11111` trong `CHANGELOG.md` — viết **ngay lúc làm việc** | **2,600 ký tự / 52 dòng** |
> | commit git mang nhãn `V11111` | **1** commit |
> | lượt owner trong vết phiên `.jsonl` cùng ngày | **có** |
> | khối phụ (`V11111b`/`c`/…) | — |
>
> 🔴 **PHẦN KHÔNG KHÔI PHỤC ĐƯỢC** — ghi thẳng, không suy:
> · **giờ chính xác** từng thao tác trong phiên · **vướng vấp giữa chừng** không được ghi lại lúc đó
> · **hash 4 bảng khoá trước/sau** (nếu phiên có chạm DB) · **PID trước/sau** (nếu có restart).
> Những chỗ đó dưới đây đều ghi `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.

---

## 1. Tóm tắt

**`P0-A` + `P0-D` của prompt 34.** Toàn bộ phiên **READ-ONLY** trên VPS (`mode=ro` · `journalctl` ·
`import`) — không chạm production.
### 🔴 RÚT LẠI `FU-436` — sai cả hai vế
**Chỗ gốc:** khối `FU-436` trong `docs/FOLLOW_UP_TRACKER.md` ghi **23/08 tối** · `REPORT_V11109` §3.
**Nguyên văn câu sai:**
> *«`glm-5.1` có `p90 = 339 giây`, **CAO HƠN chính cái trần 300 giây**… Bốn sự kiện vắng mặt trong
> 60 ngày là `3× glm-5.1` + `1× deepseek-reasoner` — **đúng hai model chậm nhất**. Không phải
> ngẫu nhiên.»*
**Điều đúng** — `_v10785_late_fill.py:31-41`:
```python
MODEL_HARD_TIMEOUT_OVERRIDES = {
    "glm-5.1": 840, "gpt-oss-120b": 900, "kimi-k2.5": 620, "qwen3.7-max": 480,
}   # mặc định 300
```
`glm-5.1` có trần riêng **840s**, và đường official **đã truyền** trần riêng từ `V10931` (01/08)
(`scheduler.py:4775-4780`) — tức **đã được vá 23 ngày trước khi em «phát hiện» nó**.
Đo timeout thật 60 ngày: chỉ `300s` nổ — 50 lần không gán được model + **2 lần
`deepseek-reasoner`**. **Không một** sự kiện timeout nào của `glm-5.1`. Độ trễ thật sáu lượt gần

## 2. Owner yêu cầu gì (nguyên văn)

> *«em đã push báo cáo githubs chưa em?»*
> — owner, **24/08/2026 08:38** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 33 FINAL BẤT BIẾN · OFFICIAL FALLBACK · SỐ PHỤ · XIÊN 2/3 · 3 CÀNG · ADMIN-ONLY · BỘ ĐỐI CHỨNG VPS Đây là prompt thi hành sau V11110, hợp nhất toàn bộ quyết định Owner ngày 24/08 lúc 09:35, 09:49, 09:59 và 10:09. Không được sử dụng lại phương án viewer, P&L, timeout, sản phẩm output hoặc cách tính thành tích cũ đã bị Owner thay thế. ================================================== 0. VAI TRÒ, MỤ…»*
> — owner, **24/08/2026 10:25** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 34 TIẾP NỐI PROMPT 33 — DỰNG FINAL BẤT BIẾN DÁN PROMPT NÀY VÀO ĐÚNG PHIÊN AGENT IDE ĐANG THỰC HIỆN PROMPT 33. Đây là lệnh TIẾP NỐI và sắp lại mức ưu tiên sau bằng chứng runtime ngày 24/08. KHÔNG mở phiên cạnh tranh, KHÔNG làm lại việc GĐ-0/GĐ-1 đã hoàn thành, KHÔNG dừng bốn Algorithm Card đang chạy. Nơi nào trình tự cũ xung đột, ưu tiên P0 FINAL trong prompt này. ==================================…»*
> — owner, **24/08/2026 12:11** (giờ VN)


*(Trích từ corpus lượt owner đã khử trùng của vết phiên `.jsonl`; giờ đã quy về giờ Việt Nam.)*

## 3. Đào bới / phát hiện

Toàn văn khối `CHANGELOG` đương thời — **nguồn chính** của bản này:

## V11111 — 2026-08-24 (trưa) — ẢNH CHỤP FINAL BẤT BIẾN · RÚT LẠI `FU-436` (trần `300s` không áp cho `glm-5.1`)

**`P0-A` + `P0-D` của prompt 34.** Toàn bộ phiên **READ-ONLY** trên VPS (`mode=ro` · `journalctl` ·
`import`) — không chạm production.

### 🔴 RÚT LẠI `FU-436` — sai cả hai vế

**Chỗ gốc:** khối `FU-436` trong `docs/FOLLOW_UP_TRACKER.md` ghi **23/08 tối** · `REPORT_V11109` §3.

**Nguyên văn câu sai:**

> *«`glm-5.1` có `p90 = 339 giây`, **CAO HƠN chính cái trần 300 giây**… Bốn sự kiện vắng mặt trong
> 60 ngày là `3× glm-5.1` + `1× deepseek-reasoner` — **đúng hai model chậm nhất**. Không phải
> ngẫu nhiên.»*

**Điều đúng** — `_v10785_late_fill.py:31-41`:

```python
MODEL_HARD_TIMEOUT_OVERRIDES = {
    "glm-5.1": 840, "gpt-oss-120b": 900, "kimi-k2.5": 620, "qwen3.7-max": 480,
}   # mặc định 300
```

`glm-5.1` có trần riêng **840s**, và đường official **đã truyền** trần riêng từ `V10931` (01/08)
(`scheduler.py:4775-4780`) — tức **đã được vá 23 ngày trước khi em «phát hiện» nó**.
Đo timeout thật 60 ngày: chỉ `300s` nổ — 50 lần không gán được model + **2 lần
`deepseek-reasoner`**. **Không một** sự kiện timeout nào của `glm-5.1`. Độ trễ thật sáu lượt gần
nhất: `29,1s · 173,6s · 3,6s · 0,1s · 289,6s · 163,8s`.

**Vì sao sai:** đo `p90` rồi so với **hằng số mặc định** mà **không tra bảng override** — `RM-10`.
**Quyết định nào đã dựa vào:** chưa cái nào.

### `P0-D` — `AI_MODEL_HARD_TIMEOUT_SEC = 300` thật sự làm gì

| câu owner hỏi | trả lời | bằng chứng |
|---|---|---|
| huỷ request/future? | **KHÔNG — model vẫn chạy ngầm** | `future.cancel()` chỉ tác dụng khi tác vụ **chưa chạy**; `register_timeout_call:65` ghi thẳng *«future vẫn chạy nền, sẽ poll lại theo watchdog»* |
| late output có persist? | **CÓ, đang chạy thật** | `persist_late_fill_row:98` → `save_prediction:128`; **68 dòng log** 06/07→23/08, ví dụ `deepseek-v4-pro-real` **869s · 1053s · 979s** ghi lane đo `late=1`, **không vào bundle** |
| cutoff riêng từng model? | **CÓ** | bảng override ở trên |

🔴 **Khoảng trống thật:** `scheduler.py:5064` (`combo-super`) **không truyền cutoff riêng** ⇒ luôn
`300s`, trong khi official (`:4779`) và shadow (`:7656`) đều truyền.

⛔ **CẤM đổi `300` → `500`** — đo cho thấy `300` **không phải** con số đang cắt ai. Việc đúng là
**thêm một trục mới** `OUTPUT_ELIGIBILITY_CUTOFF_SEC`, không sửa trục cũ.

### `P0-A` — ảnh chụp FINAL

`_v11111_snapshot_final.py` · thử chặn **9/9** · phân loại cột **ba nhóm**, cột lạ ⇒ **NHÓM A**
(fail-closed). Ảnh #1: `artifacts/final_snapshots/final_2026-08-24_121504_ce71d119.json`,
SHA-256 `ce71d119f10d5280…`, MN `v=1` `BT='45'`.

## 4. Hướng xử lý và vì sao chọn

Lý do chọn nằm trong chính khối `CHANGELOG` ở mục 3 — đó là bản ghi viết **lúc làm việc**,
không phải suy lại. Phần **cân nhắc phương án bị loại** thì 🔴 **KHÔNG KHÔI PHỤC ĐƯỢC**: nó chỉ
tồn tại trong vết phiên và không được ghi vào tài liệu nào lúc đó.

## 5. Đã làm gì

| commit | ngày (giờ VN) | tệp | tổng |
|---|---|---|---|
| `daf8cd8` | 2026-08-24 12:23:20 | .../final_2026-08-24_121504_ce71d119.json, docs/FOLLOW_UP_TRACKER.md, web/backend/_v11111_snapshot_final.py | 3 files changed, 420 insertions(+) |

## 6. Cổng kiểm

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC output cổng của phiên gốc** — cổng in ra `stdout`, không ghi tệp
(đúng khuyết tật `RM-15` mà `V11121` đã vá cho `cong_git_commit.py` bằng sổ điểm danh).

Điều **kiểm được hôm nay**, `26/08/2026`:

| phép | kết quả |
|---|---|
| commit của bản này còn trong `git log` | ✅ **1/1** còn nguyên, đều là tổ tiên của `origin/master` |
| khối `CHANGELOG` còn nguyên | ✅ 2,600 ký tự |
| bản này đã có báo cáo công khai chưa | ✅ **có, từ bản bù này** — trước đó `A55_VIOLATION_REPORT_MISSING` |

## 7. Vướng vấp

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC** vướng vấp trong phiên gốc — không tài liệu nào ghi lại lúc đó.

Vướng vấp **của chính việc bù này**, ghi trung thực: bản bù dựng từ ba nguồn đương thời nhưng
**không thay được** một báo cáo viết lúc làm việc. Cụ thể mất: giờ từng thao tác · các phương án
đã cân nhắc rồi loại · lỗi gặp giữa chừng · trạng thái trước/sau của DB nếu phiên có chạm.

## 8. Gỡ về

Bản bù này **chỉ thêm tài liệu**, không đụng mã và không đụng dữ liệu ⇒ gỡ về =
`git rm -r V11111_P0A_ANH_CHUP_FINAL_VA_RUT_LAI_FU436_20260824/` rồi commit lại. Trạng thái quay về đúng như trước khi bù.

Việc gỡ về của **bản gốc `V11111`** nằm trong chính khối `CHANGELOG` ở mục 3 (nếu bản đó có ghi).

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| `FU-442` | vá cổng A55 — chính lỗ hổng làm bản này vô hình | ✅ **ĐÃ VÁ** ở `V11122`, thử chặn **11/11** |
| — | bù nốt các bản còn thiếu | trên **toàn dải từ mốc thi hành `V10921`** còn **32** bản thiếu báo cáo; 10 bản của đợt này là nhóm ưu tiên |
| — | ngưỡng đóng bằng số | `_v10921_report_gate.py` chạy **không tham số** ⇒ `V11111` không còn trong danh sách `THIẾU BÁO CÁO` |

---

## 10. BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`
> *«em đã push báo cáo githubs chưa em?»*
> — owner, **24/08/2026 08:38** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 33 FINAL BẤT BIẾN · OFFICIAL FALLBACK · SỐ PHỤ · XIÊN 2/3 · 3 CÀNG · ADMIN-ONLY · BỘ ĐỐI CHỨNG VPS Đây là prompt thi hành sau V11110, hợp nhất toàn bộ quyết định Owner ngày 24/08 lúc 09:35, 09:49, 09:59 và 10:09. Không được sử dụng lại phương án viewer, P&L, timeout, sản phẩm output hoặc cách tính thành tích cũ đã bị Owner thay thế. ================================================== 0. VAI TRÒ, MỤ…»*
> — owner, **24/08/2026 10:25** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 34 TIẾP NỐI PROMPT 33 — DỰNG FINAL BẤT BIẾN DÁN PROMPT NÀY VÀO ĐÚNG PHIÊN AGENT IDE ĐANG THỰC HIỆN PROMPT 33. Đây là lệnh TIẾP NỐI và sắp lại mức ưu tiên sau bằng chứng runtime ngày 24/08. KHÔNG mở phiên cạnh tranh, KHÔNG làm lại việc GĐ-0/GĐ-1 đã hoàn thành, KHÔNG dừng bốn Algorithm Card đang chạy. Nơi nào trình tự cũ xung đột, ưu tiên P0 FINAL trong prompt này. ==================================…»*
> — owner, **24/08/2026 12:11** (giờ VN)


### `CODE_DID`
| điều mã **thực sự** làm | bằng chứng |
|---|---|
| 1 commit mang nhãn `V11111` | `daf8cd8` — còn nguyên trong `git log`, đều là tổ tiên `origin/master` |
| tệp bị đụng | xem bảng mục 5 |
| bản này **chưa từng** có báo cáo công khai cho tới hôm nay | `_v10921_report_gate.py` liệt `V11111` trong `THIẾU BÁO CÁO` trước khi bù |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `CHANGELOG.md` khối `## V11111` | 2,600 ký tự, viết đương thời | 🟢 **khớp** — commit tồn tại đúng ngày ghi |
| kho báo cáo công khai | **không có** thư mục `V11111_*` | 🔴 **LỆCH** — đã đóng bằng bản bù này |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID`: mã đã chạy và đã commit, `CHANGELOG` đã ghi, nhưng **kho công khai không
có gì** suốt 2 ngày. Đó là `A55_VIOLATION_REPORT_MISSING`, và nó **vô hình** vì cổng chỉ soi 8
bản gần nhất — nay đã vá (`FU-442` · `V11122`).

---

**TanPhatAI cần làm:** ghi nhận đây là **báo cáo BÙ** viết ngày 26/08/2026 cho việc làm ngày
24/08, dựng từ **ba nguồn đương thời** (CHANGELOG 2,600 ký tự ·
1 commit · vết phiên), **không** phải bản viết lúc làm việc — mọi chỗ không khôi phục
được đã ghi thẳng là `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.
