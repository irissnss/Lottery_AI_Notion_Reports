# CONVERSATION CONTEXT — V11150 · 02/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`. **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Đây là **MỆNH LỆNH TRỰC
> TIẾP CỦA OWNER**, nói trong IDE, **có hiệu lực ngay**. Owner trao đổi liên tục nên **code
> thường đi trước tài liệu** — điều owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`).
> Tài liệu cũ mâu thuẫn thực tế đang chạy thì **thực tế + sổ `docs/SO_TUONG_TAC_OWNER.md`
> thắng**; tài liệu là thứ phải sửa.

**02/09** — `PROMPT 43 R1 · CONTINUATION AFTER V11149 · GRAND OVERHAUL PHASE 0 DONE →
EXECUTE WAVES 1–5`, 19 mục `I`–`XIX`.

### Các câu quyết định, nguyên văn

> **`I`** — *«Bắt đầu thực thi liên tục: WAVE 1 FOUNDATION → WAVE 2 ALL-MODEL ARENA → WAVE 3
> TOTAL_V2 + COMBO_V2 + FINAL_V2 → WAVE 4 OUT-OF-TIME REPLAY + OPERATIONAL CANARY → WAVE 5 MỘT
> GRAND OVERHAUL CUTOVER PACKET.»*
>
> *«Dừng chuỗi đo nhỏ giọt và báo cáo chủ yếu về D-30. Measurement chỉ là cổng
> acceptance/elimination sau khi đã xây hệ thống, không được dùng làm lý do trì hoãn việc cải
> tiến.»*
>
> *«Không cắt bỏ TOTAL. Phải xây lại TOTAL thành bộ chọn nguồn và xếp hạng candidate mạnh hơn.»*
>
> **`V.1`** — *«Fail-closed với schema hỏng nhưng không được biến N≥1 thành NO_OUTPUT.»*
>
> **`V.2`** — *«Không chấp nhận emitter tiếp tục bỏ 7.935 ký tự SYSTEM_PROMPT.»*
>
> **`V.3`** — *«Reverse scan các pattern ML/TOTAL/FINAL/model ranking. Kết quả phải bằng 0
> trước khi gọi CONTEXT_ONLY_PASS.»*
>
> **`V.5`** — *«Nếu mới code/test nhưng chưa runtime: CODED_AND_TESTED_NOT_RUNTIME_PROVEN.
> Không nói "đã deploy" nếu PID chưa nạp đúng imported path/hash và chưa có behavior proof.»*
>
> **`VII.2`** — *«Trọng số phải đủ dốc để nguồn tốt thực sự có tiếng nói cao hơn, nhưng không
> được collapse vào một model từ một cửa sổ ngắn. Không hạ tiêu chuẩn chỉ để có phương pháp
> thắng.»*
>
> **`VIII`** — *«Chưa được gọi actual double-count chỉ từ tên nguồn.»*
>
> **`XV`** — *«Chỉ hỏi Owner khi: A destructive schema/data · B SSH/key/credential/access
> mutation · C không có rollback · D bật TOTAL_V2/COMBO_V2/FINAL_V2 vào official production.
> Nếu chưa chạm bốn gate trên: tiếp tục làm, không dừng chờ.»*
>
> **`XIX`** — *«Không làm lại Phase 0. Không đo lại D-30. Không mở FU mới. Không mở Prompt 44.
> Không trả về một kế hoạch khác. Không hỏi Owner xác nhận. EXECUTE NOW.»*

### `III` — bốn retraction owner bắt buộc, agent đã tuân

| bị bác | thay bằng |
|---|---|
| «27 model cùng bỏ phiếu» | 27 `RUNTIME_ACTIVE`, **18 actual voters** |
| «high/low ratio 3,87×» | **MN 1,63× · MB 2,08× · MT 5,70×** |
| «16 shadow rò trực tiếp vào TOTAL» | **DƯƠNG TÍNH GIẢ** từ raw string scan |
| — | nhãn `NO_OBSERVED_DIRECT_SHADOW_VOTER_LEAK_IN_270_BUNDLES` |

**Bản này không nhắc lại bất kỳ kết luận nào trong bốn cái trên.**

---

## 2 · Agent làm gì

| bước (`XIX`) | việc | kết quả |
|---|---|---|
| 1 | xác nhận baseline chỉ-đọc | 558 · `a82c508d3569abda…` · PID 3156545 · 200 |
| 2 | `UNIFIED_CANDIDATE_CONTRACT` | `UCC-1.0.0` · bảng mới additive · rollback có phép thử |
| 3 | validator + tương thích + thử | **37/37 ĐẠT** |
| 4 | vá full emitter | 8 mảnh · MN 49.329 · MT 47.164 · MB 48.473 |
| 5 | chuyển prompt sang `LLM_CONTEXT_ONLY_V2` | cờ, mặc định TẮT |
| 6 | cổng contamination + META | **META 17/17** · `PASS` × 3 miền khi bật cờ |
| 7 | `ML_PURE_MATH_V2` | **`ML_PURE_MATH_PASS`** |
| 8 | audit leakage / artifact / nạp runtime | 4/4 model có chặn ngày · artifact VPS 2 ngày |
| 9 | thử end-to-end Wave 1 | **`E2E_PASS`** trên dữ liệu production |
| 10 | rehash 558 FINAL | **KHÔNG DRIFT** |
| 11 | deploy | **KHÔNG deploy** — xem mục 4 |
| 12 | runtime proof | `FILES_PRESENT_NOT_RUNTIME_PROVEN` (chỉ local) |
| 13 | phát hành `V11150` | bản này |

---

## 3 · Vấp trong phiên — năm lần, ghi đủ

**🔴 ① Bộ thử bắt mâu thuẫn trong CHÍNH thiết kế hợp đồng.** `source_snapshot_at` vừa bắt buộc
có giá trị vừa được xử như «thiếu thì cảnh báo» ⇒ **mọi artifact cũ `INVALID`**, đường replay
chết từ dòng đầu. Nếu không có bộ thử thì lỗi này chỉ lộ ra ở Wave 4 khi replay không chạy nổi.

**🔴 ② Cổng contamination báo 6 chỗ — 4 là DƯƠNG TÍNH GIẢ.** Đọc nguyên văn mới thấy *«CONV×3
herding scenarios có win rate THẤP HƠN average»* là câu **chống** herding, và *«Anti-trap chỉ
là lớp an toàn sau khi…»* là mô tả **thứ tự làm việc**. **Gỡ cả sáu thì đã làm hỏng đúng thứ
cần giữ.** Đây là lần thứ **năm** trong hai ngày một phép khớp chuỗi suýt đẻ ra kết luận sai
(`RM-09`).

**🔴 ③ Bộ audit ML báo `lstm` «chưa chứng minh chặn ngày» — SAI.** Nó chặn ở `:160` bằng
**Python**; bộ dò chỉ tìm cú pháp SQL. Cùng lỗi cho `ml_predict` — chặn nằm **một tầng dưới**
ở `statistical_analyzer.py:71`.

**🔴 ④ Bộ audit báo artifact ML 144,6 NGÀY — SAI VỀ PRODUCTION.** Đó là bản **local**. VPS train
lại **30/08**, tức **2 ngày**. Nếu công bố thì đã báo owner sự cố *«ML 5 tháng không train»*
**không có thật** (`RM-13`).

**🟡 ⑤ `\n` trong heredoc thành xuống dòng thật — lần thứ tư.** Và cổng chỉ-đọc của chính agent
chặn nhầm `h.update(...)` **lần thứ ba**. Cả hai đã vá tận gốc, cổng thử được hai chiều.

---

## 4 · Vì sao KHÔNG deploy

Owner `XIV` cho phép deploy `CLASS B` ngoài block `15:30–18:15`, và lúc làm là **~00:30**, tức
ngoài block. Vẫn **không deploy**, vì hai lý do:

1. Owner `XIV`: *«Không restart hoặc đổi official path chỉ để chứng minh đã làm.»* Cờ mặc định
   **TẮT**, nên deploy `gpt_analyzer.py` rồi restart production lúc 00:30 sẽ **không đổi một
   hành vi nào** — chỉ thêm rủi ro.
2. Owner `XV.D`: bật `LLM_CONTEXT_ONLY_V2` vào official **cần owner ký**. Thứ đáng deploy là
   thứ có tác dụng, và thứ đó thuộc **Cutover Packet**.

⇒ Trạng thái ghi đúng tầng: **`CODED_AND_TESTED_NOT_RUNTIME_PROVEN`**, tệp mới là
`FILES_PRESENT_NOT_RUNTIME_PROVEN` (chỉ có ở local).

---

## 5 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 **không bị đụng** — PID `3156545` · health `200` |
| `FINAL` cũ | 🟢 **558 · `a82c508d3569abda…` KHÔNG DRIFT** |
| Wave 1 | 🟢 **A · B · C · D · E xong** — còn adapter «LLM tự sinh ranked top-K» |
| Wave 2 | ⚪ `ALL_MODEL_ARENA` — tiếp ngay, không chờ |
| owner gate | **KHÔNG chạm** — không hỏi câu nào |
| Prompt 43 | **`PARTIAL`** |

---

TanPhatAI cần làm: ghi **`V11150` = Grand Overhaul WAVE 1**, riêng `e9a0ca9` + `6330ddf`, trạng thái **`CODED_AND_TESTED_NOT_RUNTIME_PROVEN`** — **code đi trước tài liệu là được phép**, nhưng **chưa deploy** và **official chưa đổi một ký tự** (cờ mặc định TẮT). Ghi **`FU-450` mục 2 ĐÓNG**, kèm **sửa quy kết**: emitter cũ bỏ **`REASONING_RULEBOOK` 15.256 ký tự**, không phải `SYSTEM_PROMPT`. Ghi **ổ contamination Phase 14A** và hai mã vi phạm `A58_VIOLATION_HALF_DONE` + `PRJ_PROMPT_CONTRADICTS`. Ghi **`ML_PURE_MATH_PASS`** — tầng ML vốn đã sạch, đừng đi «sửa» nó. Ghi **bốn lần agent tự báo sai rồi tự sửa** để lần sau không ai trích lại con số đã bị bác. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
