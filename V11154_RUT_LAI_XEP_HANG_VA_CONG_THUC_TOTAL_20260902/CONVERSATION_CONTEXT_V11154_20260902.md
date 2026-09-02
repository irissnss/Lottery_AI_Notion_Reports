# CONVERSATION CONTEXT — V11154 · 02/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`. **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Mệnh lệnh trực tiếp của
> owner trong IDE, **có hiệu lực ngay**. Bản này chứa **một lần agent tự rút lại con số đã công
> bố** — tài liệu nào còn trích con số cũ thì **tài liệu phải sửa**
> (`PRJ-INTERACTION-LEDGER-001`).

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 02/09 ~12:20 | *«tiếp đi em»* | `YÊU_CẦU` | chạy 3 tuyến điều tra song song **có bước phản biện đối kháng**; chuẩn bị deploy đủ 8 bước | `ĐÃ_LÀM` |
| 02/09 ~14:00 | *«Tiếp theo là gì? đã push báo cáo đầy đủ chi tiết chưa?»* | `HỎI` | **kiểm thật trước khi trả lời**: rút lại **đã** đẩy (`bbda484`), nhưng `V11154` **chưa có gì** — `CHANGELOG 0` · `HISTORY 0` · không thư mục báo cáo. Làm đủ trong cùng phiên | `ĐÃ_LÀM` |

**Owner bắt đúng lần thứ hai trong ngày.** Lần trước là `V11151`, lần này là `V11154`. Cùng một
kiểu: agent làm xong việc, đẩy phần cấp bách (bản rút lại), rồi **chưa đóng trọn gói**.
`PRJ-INTERACTION-LEDGER-001` khoản 2 cho phép **code** đi trước tài liệu, nhưng **ghi nhận không
được đi sau quá một phiên**.

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| chạy 3 tuyến điều tra song song, mỗi tuyến có **agent phản biện đối kháng** | 6 agent · 787.690 token · 193 lượt gọi công cụ · **0 lỗi** · **2/3 tuyến bị bác** |
| ❌ **phản biện bác chính bảng xếp hạng agent đã công bố** | agent **tự kiểm lại và xác nhận phản biện ĐÚNG** |
| 🔴 **rút lại tại chỗ công bố** | `bbda484` — đủ bốn phần `PRJ-RETRACTION-001` |
| 🟢 tìm được **công thức chấm điểm thật của TOTAL** | `main.py:9955-10007` · counterfactual **tính ngược được** |
| 🟢 tìm được **gốc `MISSING_SHADOW_ROW`** | ba nguyên nhân, tách hết 100% |
| 🟢 đóng **2 mục `NOT_VERIFIED`** | cả hai **KHÔNG phải lỗi** |
| 🔴 deploy | **bị lớp phân quyền công cụ chặn** — mọi cổng dự án ĐẠT |
| 🟢 bốn mặt + báo cáo công khai | `governance_seq → 470` |

---

## 3 · Vấp trong phiên — bốn lần

**🔴 ① Agent công bố cho owner một bảng xếp hạng SAI, và nó đã thành cơ sở hành động.**

Con số `gemini-3.6-flash −59` / `z = −6,48` / *«loại bỏ chứng minh được NGAY»* đi vào IDE, vào
báo cáo công khai `ace9365`, và thành kế hoạch *«`RETIRE` ba nguồn»* ở `V11153`.

Gốc: cột `would_flip_baseline_to_lose` **đếm cả ngày model KHÔNG HỀ dự đoán** là thua. 493/1.600
dòng `MISSING_SHADOW_ROW` bị cộng vào `lose`.

Sạch rồi thì: `gpt-oss-120b` và `glm-5.1` **toàn bộ** lượt thua là ảo; `qwen3.7-max` và
`gemini-3.5-flash` **đổi dấu** từ âm sang dương; và **không nguồn nào** đạt ngưỡng ý nghĩa —
`|z|` cao nhất chỉ `1,31`.

**Bài học kỹ thuật:** agent tin một cột có sẵn mà **không soi cách nó được tính**. `RM-11` đòi
con số công bố phải **tái lập được** — agent tái lập được *câu truy vấn* nhưng **không tái lập
được *ý nghĩa* của cột**. Đó là một lỗ hổng thật của `RM-11` như đang được thi hành.

**Cái bắt được lỗi là bước PHẢN BIỆN.** Agent phản biện được giao nhiệm vụ **cố tình bác bỏ**,
không phải xác nhận. Nếu chỉ chạy điều tra thì con số sai đã đi tiếp vào Wave 3.

**🟡 ② Agent điều tra cũng sai — và bị phản biện bắt.** Tuyến `grok` kết luận *«grok hạng 8 chứ
không phải hạng 1, do cửa sổ lệch»*. Phản biện chỉ ra grok **là #1 trong nhóm shadow** — đúng
nhóm mà `V11152` công bố; agent đã **nhầm ĐỔI NHÓM SO SÁNH thành CỬA SỔ LỆCH**. Và con số
`35/24 = +11` **tái lập được** tại mốc `2026-06-02`; agent chỉ thử 6 mốc cố định rồi trượt, xong
dựng cảnh báo `RM-17` nhắm vào **con số đúng**.

**🟡 ③ Tuyến counterfactual có một phép chứng minh vòng tròn.** Bản dựng lại lấy tập người tham
gia từ `gate_diagnostics` của **chính artifact đang tái lập**, nên `205/205` chứng minh các bước
sau chứ **không** chứng minh bước chọn pool. Đã ghi vào giới hạn thay vì để nguyên như một bằng
chứng mạnh hơn thực tế.

**🔴 ④ Deploy bị chặn bởi lớp phân quyền của Claude Code** — không phải bởi cổng nào của dự án.
`DONG_BO_V11143=ĐẠT` (VPS **cũ hơn**, 0 tệp VPS mới hơn), giờ VPS 20:22 ngoài block, PRE sạch,
bộ thử lane 11/11. Bộ deploy 8 bước + gỡ về đã sẵn, **chờ owner cho phép**.

---

## 4 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 **không bị đụng** · `PID 3156545` · `FINAL_ANCHOR_INTACT` |
| bảng xếp hạng shadow | 🔴 **ĐÃ RÚT LẠI** — cả pool = **`HOLD`**, không retire, không promote |
| công thức TOTAL | 🟢 **tìm được**, counterfactual **tính ngược được cho lịch sử** |
| dụng cụ đo | 🔴 **hỏng, phải vá trước** — 869 dòng lỗi phân loại + phải loại dòng `MISSING` |
| deploy | 🔴 **tắc ở phân quyền công cụ** |
| chặn owner | 1 cổng `XV.D` (Cutover) + 1 cổng `XV.B` (`CLASS C` bảo mật) |

---

TanPhatAI cần làm: ghi **`V11154`** — riêng + công khai, **không deploy**. Ghi **agent TỰ RÚT LẠI một bảng xếp hạng đã công bố cho owner** (`bbda484`, đủ bốn phần): `would_flip_lose` **đếm 493 lượt thua ẢO**; `gpt-oss-120b`/`glm-5.1` **toàn bộ** ảo; `qwen3.7-max`/`gemini-3.5-flash` **ĐỔI DẤU**; kết luận đúng là **0 nguồn tốt · 0 nguồn xấu có ý nghĩa ⇒ cả pool `HOLD`**, **HUỶ** kế hoạch retire/promote. Ghi **bài học `RM-11`**: tái lập được *câu truy vấn* **không** bằng tái lập được *ý nghĩa của cột*. Ghi **bước PHẢN BIỆN ĐỐI KHÁNG là thứ bắt được lỗi** — nên giữ nó cho mọi kết luận về sau. Ghi **công thức TOTAL** `main.py:9955-10007` + **counterfactual tính ngược được** (205/205), **15,2%** đổi `ranked[0]`, nhưng **trần `MT:13`** làm thêm-một-nguồn = **đá-một-nguồn-ra** (92% ngày MT), và **hạng TOTAL ≠ bạch thủ** (51/205, override `V10640`). Ghi **gốc `MISSING_SHADOW_ROW`** ba nguyên nhân, **869 là lỗi phân loại sửa được**. Ghi **`IV.14` KHÔNG double-count** và **`combo-no-token` KHÔNG phải lỗi**. Ghi **deploy tắc ở lớp phân quyền công cụ**, mọi cổng dự án ĐẠT. Mọi con số hiệu quả trong bản này đo trên **đủ bộ cửa sổ 14 ngày · 30 ngày · 90 ngày · 180 ngày** (mục 3.1b), và **6/30 nguồn ĐỔI DẤU** giữa các cửa sổ. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
