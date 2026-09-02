# CONVERSATION CONTEXT — V11151 · 02/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`. **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Đây là **MỆNH LỆNH TRỰC
> TIẾP CỦA OWNER**, nói trong IDE, **có hiệu lực ngay**. Owner trao đổi liên tục nên **code
> thường đi trước tài liệu** — điều owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`).
> Tài liệu cũ mâu thuẫn thực tế đang chạy thì **thực tế thắng**; tài liệu là thứ phải sửa.

### Prompt chính — `PROMPT 43 R1`, các mục dùng trong bản này

> **`VI.1`** — *«Phải trả lời vì sao 9 runtime-active không vào voters: output eligibility ·
> missing candidate · gate · late · sanitization · configuration · caller/path khác · hay lỗi.
> **Cấm đoán nguyên nhân nếu chưa có trace.**»*
>
> **`III`** — *«Không được mở lại sự cố shadow leak chỉ vì tên model xuất hiện trong `model_bt` ·
> `model_wr` · `model_exclusion_reasons` · `diagnostic_empty_models` · các trường
> diagnostic/trace tương tự.»*
>
> **`IV.14`** — *«Không đo cùng một model hai lần qua hai prompt regime như hai bằng chứng độc
> lập.»*
>
> **`XIX`** — *«Tiếp tục ALL_MODEL_ARENA; không dừng chờ nếu không gặp bốn Owner gates.»*

### Hai câu owner nói giữa phiên — nguyên văn

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 02/09 ~02:00 | *«Tiếp theo là gì cần anh xác nhận chia sẻ thêm vấn đề gì không»* | `HỎI` | trả lời **không cần xác nhận** — chưa chạm bốn cổng (`XV`), tiếp tục Wave 2. Nêu **thứ sẽ cần**: ngưỡng chấp nhận đăng ký **trước Wave 4** (`VII.1` + `RM-03` cấm chọn sau khi nhìn kết quả). Nêu **hai thứ owner chia sẻ được, không chặn**: đơn giá API từng model (cho cột `cost` của `VI.2`), và 3-càng đã có pipeline hợp lệ chưa | `ĐÃ_LÀM` |
| 02/09 ~02:20 | *«Push báo cáo chưa em?»* | `HỎI` | **kiểm thật trước khi trả lời**: `V11150` đã push đủ (công khai `8f78c2b` · riêng `6330ddf`); `V11151` **CHƯA** — có commit code `6a5ca20` nhưng `CHANGELOG`=`0`, `AUTOMATION_HISTORY`=`0`, **không có thư mục báo cáo công khai**. Làm đủ **ngay trong phiên** | `ĐÃ_LÀM` |

**Owner bắt đúng một khoản nợ có thật, không phải hỏi cho có.** `PRJ-INTERACTION-LEDGER-001`
khoản 2: *«code ĐƯỢC đi trước tài liệu, nhưng GHI NHẬN thì KHÔNG được đi sau quá một phiên»*.
`V11151` đã vượt mức đó. Bản này trả nợ.

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| phân loại pool bằng **dấu vết**, không tin registry | `57 → 27 → 18` · **10** active không bỏ phiếu |
| trả lời «vì sao không vào voters», mỗi nguồn kèm **số đo** | **`SHADOW_ONLY` 10/10** — 100% lượt shadow |
| dựng **cổng biên shadow** | **`SHADOW_BOUNDARY_CLEAN` 0/18** |
| ❌ suýt in bảng đọc thành «shadow đang bỏ phiếu» | **chặn lại trước khi công bố** — xem mục 3 |
| 🟡 rút lại «1,8% lá phiếu» của `FU-450` | đủ **bốn phần** `PRJ-RETRACTION-001` |
| trả nợ bốn mặt + báo cáo công khai cho `V11151` | `governance_seq → 467` |

---

## 3 · Vấp trong phiên

**🔴 Suýt mở lại sự cố shadow-leak mà owner cấm mở lại (`III`) — chặn được trước khi công bố.**

Cột *«`run_source` trội»* bản đầu lấy **mode 90 ngày**. Mode đó **vắt qua lần xoay pool 01/08**,
nên in ra ngay dưới tiêu đề «18 VOTER THẬT»:

```
glm-5.1        LLM_BASE   167   shadow_auto_eval
gpt-oss-120b   LLM_BASE   129   shadow_auto_eval
```

Đọc lên là *«shadow đang bỏ phiếu»*. **Sự thật ngược lại:** shadow của cả hai **dừng từ 01/08**;
từ đó tới nay chúng chạy `ai_chain`/`auto_daily` — tức **đã lên official**. Đây là lần thứ **hai
trong hai ngày** một phép đo trình bày sai suýt đẻ ra báo động shadow-leak giả.

Đã tách cột thành `run_source` **HIỆN NAY (14 ngày)** + nhãn `ĐÃ LÊN OFFICIAL` kèm số đo 90 ngày
— **không** bỏ thông tin lịch sử, chỉ **thôi để nó nói sai về hiện tại**.

**🟡 Con số `9` trong prompt là `27 − 18`, và phép trừ đó sai.** Hai tập **không lồng nhau**:
`claude-opus-4-20250514` là voter nhưng **lượt cuối 16/06**, không còn runtime-active. Số đúng là
**10**.

**🟡 `%` của `LIKE '%shadow%'` va vào `%d`** của phép format chuỗi ⇒ `TypeError`. Sửa bằng truyền
tham số thay vì nội suy.

**🟡 Tệp rác `muc`** — output lỗi `git add` với chuỗi tiếng Việt không đóng nháy bị ghi thành tệp.
Đọc xác nhận **100% là dòng `error: pathspec`** rồi mới xoá.

---

## 4 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 **không bị đụng** — phiên chỉ đọc · `PID 3156545` |
| `FINAL` cũ | 🟢 **558 · `a82c508d3569abda…` KHÔNG DRIFT** |
| nợ tài liệu | 🟢 **đã trả** — `V11151` đủ bốn mặt + báo cáo công khai |
| Wave 2 | 🟢 `VI.1` xong · ⚪ `VI.2` Arena namespace · ⚪ `VI.3` vòng đời shadow |
| owner gate | **KHÔNG chạm** — không hỏi xác nhận câu nào |
| sẽ cần owner | **ngưỡng chấp nhận trước Wave 4** · **Cutover Packet** (cổng D) · **`CLASS C` bảo mật** (cổng B) |

---

TanPhatAI cần làm: ghi **`V11151` Wave 2 `VI.1`** — phiên **chỉ đọc**, không deploy. Ghi **owner hỏi «Push báo cáo chưa em?» và bắt đúng một khoản nợ** — `V11151` từng có commit code mà thiếu bốn mặt + báo cáo công khai, **đã trả trong cùng phiên**. Ghi **RÚT LẠI «1,8% lá phiếu»** của `FU-450` mục 1 — `gemini-3.6-flash` **0 lần** trong `voters`; việc đúng là **dừng lượt shadow**, cái được là **tiền API**. Ghi **10 nguồn, không phải 9** — phép trừ `27 − 18` sai vì một voter đã nghỉ hưu. Ghi **`SHADOW_BOUNDARY_CLEAN 0/18`**, biên khớp đến từng ngày — **đừng mở lại sự cố shadow-leak**. Ghi **agent suýt in bảng đọc thành «shadow đang bỏ phiếu» và tự chặn lại** trước khi công bố. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
