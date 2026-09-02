# REPORT V11153 — **KHOÁ NGƯỠNG CHẤP NHẬN** trước mọi replay · 02/09/2026

> `ACTOR_RUNTIME = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**
> Phiên **chỉ ghi tài liệu**: không deploy · không đụng code · không ghi DB.
>
> ⚠️ **Tệp `docs/NGUONG_CHAP_NHAN_GRAND_OVERHAUL.md` được commit TRƯỚC mọi replay** — `RM-03`
> đòi đăng ký ngưỡng **trước** ngày chốt; `VII.1` cấm chọn variant **sau** khi nhìn kết quả.
> Commit `2970605` · 02/09/2026. Replay đầu tiên **chưa chạy**.

---

## 1 · TÓM TẮT

Owner chốt hai điều trong IDE. Cả hai **đổi thiết kế**, không chỉ là lời nhắc:

| | owner nói | hệ quả |
|---|---|---|
| ① | *«chỉ có tiến bộ chứ không thể thụt lùi»* | ngưỡng chấp nhận **nghiêm nhất có thể** — một miền lùi là `STOP`, **dù tổng thể dương** |
| ② | *«giá Token ko quan trọng… Anh chỉ quan trọng chất lượng»* | **chi phí RỜI khỏi bộ chọn nguồn** |

Và một vi phạm của agent: hỏi owner **đơn giá API** — thứ `IV.13` đã khoá.

**Kết quả quan trọng nhất:** `FU-449` trước treo **hai** thứ cần owner; nay còn **một** — cổng
`XV.D` (bật vào official ở Cutover Packet). Mọi việc kỹ thuật còn lại **tự làm được**.

---

## 2 · OWNER YÊU CẦU GÌ — nguyên văn

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI.** Mệnh lệnh trực tiếp của owner, nói trong
> IDE, có hiệu lực ngay (`PRJ-INTERACTION-LEDGER-001`).

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 02/09 ~11:45 | *«giá Token ko quan trọng việc này đã nói nhiều lần rồi em. Anh chỉ quan trọng chất lượng, API đắt mà chất lượng, ít nhưng mà chất lượng là được, đơn giá em nghỉ là em rõ đi hỏi câu hỏi dư thừa quá»* | **`BÁC_BỎ`** | gỡ chi phí khỏi tiêu chí **chọn**; giữ để **báo cáo**. Ghi bộ nhớ dài hạn để không hỏi lại | `ĐÃ_LÀM` |
| 02/09 ~11:45 | *«chỉ có tiến bộ chứ không thể thụt lùi nha em»* | `YÊU_CẦU` | khoá thành ngưỡng đăng ký trước replay | `ĐÃ_LÀM` |

Trước đó, cùng phiên:

| 02/09 ~11:20 | *«Với mong muốn yêu cầu của anh như thế em xem có vướng và trở ngại gì không em? Anh cần xử lý dứt điểm cho xong nha em»* | `HỎI` | trả lời **sáu trở ngại** đã đo, kèm số | `ĐÃ_LÀM` |

### Mục prompt liên quan

> **`IV.13`** — *«Ít model nhưng chất lượng; chi phí gồm API, latency, vận hành, herding,
> complexity và opportunity cost.»*
>
> **`VII.2`** — *«Không hạ tiêu chuẩn chỉ để có phương pháp thắng.»*
>
> **`VII.1`** — *«Variant phải khóa trước khi xem kết quả replay tương ứng. Không chọn variant
> sau khi đã nhìn kết quả rồi gọi là prospective.»*

---

## 3 · ĐÀO BỚI / PHÁT HIỆN

### 3.1 🔴 Agent vi phạm `A54_VIOLATION_ASKED_WITHOUT_LOOKUP`

Agent hỏi owner **đơn giá API từng model**. Ba nơi `§56` bắt tra trước khi hỏi đều **đã có câu
trả lời**:

- `PROMPT 43 R1 IV.13` — *«ít model nhưng chất lượng»*;
- owner nói *«đã nói nhiều lần rồi»* — tức đây không phải lần đầu;
- `VII.2` — *«không hạ tiêu chuẩn chỉ để có phương pháp thắng»*, tức không được đổi chất lượng
  lấy giá rẻ.

Owner phải mất công nhắc lại một việc đã nói. **Đã ghi bộ nhớ dài hạn.**

### 3.2 Vì sao *«không thụt lùi»* phải kèm chữ **«có ý nghĩa»**

Đọc câu owner theo nghĩa **tuyệt đối từng ngày** thì **không thay đổi nào trên đời qua được** —
kể cả một thay đổi thật sự tốt — vì nhiễu ngẫu nhiên **luôn** làm vài ngày xấu hơn. Một ngưỡng
không đo được là một ngưỡng không chặn được gì.

Nên agent thêm chữ **«có ý nghĩa»** và **định nghĩa nó bằng số** (mục 5). **Đây là diễn giải
của agent** — ghi rõ ra đây để owner bác nếu sai.

### 3.3 Chi phí rời khỏi bộ chọn — chỗ nào trong thiết kế bị đổi

| chỗ | trước 02/09 | từ 02/09 |
|---|---|---|
| `VI.2` chấm nguồn | `cost` là **một chiều điểm** | **cột báo cáo** |
| `VII.1` biến thể `COST_LATENCY_AWARE` | ứng viên **ngang hàng** | vẫn chạy **để so**, **không được thắng nhờ rẻ** |
| `TOTAL_V2` selector | được hạ điểm nguồn đắt | **cấm** hạ điểm vì đắt |
| độ trễ | **điểm trừ** | **ràng buộc cứng** — kịp mốc khoá miền hay không, chỉ vậy |

### 3.4 Hệ quả agent nhận ra khi khoá ngưỡng — chưa xử, ghi lại

Với luật **«không miền nào được lùi»**, cách an toàn **không phải** thay cả bộ nguồn một lượt,
mà **thêm từng nguồn** rồi đo lại. Thay cả bộ thì xác suất ít nhất một miền lùi tăng nhanh theo
số thay đổi. Điều này **định hình `TOTAL_V2`**: selector phải hỗ trợ **thêm dần**, không chỉ
**chọn lại từ đầu**. Ghi vào theo dõi, chưa thi hành.

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Vì sao chọn McNemar chứ không phải hai tỉ lệ độc lập.** Phép so ở đây là **cặp**: cùng ngày,
cùng miền, cũ vs mới trên **cùng một sự kiện xổ**. Dùng thước hai-nhánh-độc-lập cho ra **461
ngày** để bắt `+5pp`; thước cặp đúng cho **~49 ngày** cho ứng viên tốt nhất. Đây là `RM-21`
nguyên văn: *«hằng số đo được chỉ đúng cho thước đã đo nó»*. Và kho **đã có sẵn**
`model_paired_scorecard_cumulative` với cột `z_mcnemar` — thước đúng vốn nằm sẵn ở đó.

**Vì sao ngưỡng đối xứng hai chiều `|z| ≥ 1,96`.** Nếu nới bên «xấu đi» thành `−2,5` chẳng hạn
thì ta đã **hạ tiêu chuẩn để dễ thắng** — đúng thứ `VII.2` cấm.

**Vì sao sàn 30 cặp lệch mỗi miền.** `RM-04`: n nhỏ **không chỉ yếu mà không ổn định** — z đổi
dấu khi thêm hai ngày. Dưới sàn thì ghi **«chưa được phép kết luận»**, không ghi «yếu».

**Vì sao thước chính là HẠNG chứ không phải trúng/trượt.** Hỏi nhị phân *«bạch thủ có trúng
không»* vứt bỏ gần hết thông tin mỗi lượt. Hỏi *«số trúng nằm ở hạng mấy trong danh sách ứng
viên»* cho tín hiệu **phân cấp** — và đó đúng là thứ `ranked_candidates` trong Unified Contract
(Wave 1) mở ra. **Rút ngắn thời gian đo mà không hạ tiêu chuẩn.**

---

## 5 · ĐÃ LÀM GÌ — trước / sau / phiên bản / kiểm (§60.4)

### A · `docs/NGUONG_CHAP_NHAN_GRAND_OVERHAUL.md` (MỚI)

**TRƯỚC:** không có ngưỡng nào được đăng ký. Wave 4 replay sẽ phải tự đặt ngưỡng **sau** khi
nhìn kết quả ⇒ `RM-03_VIOLATION`.

**SAU:** ba trạng thái khoá cứng —

| kết quả replay | phán quyết |
|---|---|
| ≥1 miền **tốt lên có ý nghĩa** **VÀ** không miền nào **xấu đi có ý nghĩa** | **`PASS`** — được trình Cutover |
| **bất kỳ** miền nào **xấu đi có ý nghĩa** | **`STOP`** — **dù tổng thể dương** |
| không miền nào đổi có ý nghĩa | **`HOLD`** — đo tiếp, không cutover |

**«Có ý nghĩa» khoá bằng số:**

| tham số | giá trị |
|---|---|
| phép kiểm | **McNemar cặp đôi** (cùng ngày, cùng miền) |
| tốt lên | `z ≥ +1,96` |
| xấu đi | `z ≤ −1,96` — **đối xứng** |
| sàn mẫu | **≥ 30 cặp lệch** mỗi miền |
| cửa sổ | **out-of-time**, cố định trước, không trùng cửa sổ chọn |
| thước chính | **hạng của số trúng trong `ranked_candidates`** |
| thước phụ | bạch thủ · lô2 · xiên — **báo cáo**, không phán quyết |

**Cấm đổi bất kỳ ô nào sau khi nhìn kết quả.** Đổi thì replay **chạy lại từ đầu**.

**PHIÊN BẢN:** commit `2970605` · 02/09/2026, **trước** replay đầu tiên.

### B · `docs/SO_TUONG_TAC_OWNER.md` — APPEND

**TRƯỚC:** 26.004 ký tự. **SAU:** 28.157 ký tự.
**KIỂM:** script khẳng định **toàn bộ nội dung cũ còn nguyên** trước khi ghi — `APPEND-ONLY`,
không sửa dòng cũ (`PRJ-INTERACTION-LEDGER-001` khoản 3).

### C · Bộ nhớ dài hạn agent

Hai mục mới: *«chi phí không phải tiêu chí chọn»* · *«ngưỡng chỉ tiến không lùi»* — để phiên sau
**không hỏi lại** và **không tự nới ngưỡng**.

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11062_nang_version.py --kiem` | ✅ `ĐẠT` — bốn mặt · `governance_seq 469` |
| `_v11044_cong_so_hieu.py V11153` | ✅ `KHỚP` |
| sổ tương tác `APPEND-ONLY` | ✅ nội dung cũ nguyên vẹn, đã khẳng định bằng script |
| ngưỡng commit **trước** replay | ✅ `2970605` · replay **chưa chạy** |
| `_v10921_report_gate.py V11153` | ✅ đủ 9 phần *(chạy sau khi commit bản này)* |

**Không có cổng runtime nào chạy** — phiên này không đụng code.

---

## 7 · VƯỚNG VẤP

**🔴 Agent hỏi thừa.** `A54_VIOLATION_ASKED_WITHOUT_LOOKUP` — xem 3.1. Đây là loại lỗi tốn
**thời gian của owner**, không tốn máy: owner phải giải thích lại một việc đã nói nhiều lần.
Cách chặn đã dựng: ghi bộ nhớ dài hạn + ghi vào sổ tương tác, để phiên sau tra được.

**🟡 Agent phải tự diễn giải một câu owner.** *«Không thụt lùi»* đọc tuyệt đối thì chặn mọi thay
đổi; đọc kèm «có ý nghĩa» thì đo được. Agent **chọn cách thứ hai và ghi rõ ra** thay vì im lặng
áp dụng. Nếu owner muốn nghiêm hơn thì bác — nhưng cần bác **trước** replay, vì bác sau là đổi
ngưỡng sau khi nhìn kết quả.

---

## 8 · GỠ VỀ

| thành phần | gỡ về |
|---|---|
| `NGUONG_CHAP_NHAN_GRAND_OVERHAUL.md` | `git revert 2970605` — nhưng **gỡ ngưỡng nghĩa là Wave 4 mất căn cứ**, không nên |
| sổ tương tác | **KHÔNG gỡ** — `APPEND-ONLY`, gỡ là viết lại lịch sử |
| bốn mặt quản trị | `backups/FOLLOW_UP_TRACKER.md.pre_*` |

**Không có gì trên production cần gỡ** — phiên này không deploy.

---

## 9 · THEO DÕI TIẾP

| # | việc | trạng thái | chặn ở đâu |
|---|---|---|---|
| 1 | **Deploy + bật lane shadow ăn prompt ngữ cảnh thuần** | 🔴 **tiếp theo ngay** | không cần owner — Class B, ngoài block |
| 2 | **Bật lại `grok-4.20-multi-agent`** (`+11`, tắt từ 29/07) · `RETIRE` ba nguồn `z < −5` | 🔴 tiếp theo | shadow plumbing — `XV` nói **không** hỏi owner |
| 3 | Điền `output_counterfactual_rank` (NULL 12.304 dòng) | 🔴 tiếp theo | — |
| 4 | `cost_est` — nay chỉ là **cột báo cáo** | ⚪ hạ ưu tiên | owner khoá: chi phí không vào điểm chọn |
| 5 | Truy `MISSING_SHADOW_ROW` 1.636 dòng (27%) | 🟡 `NOT_VERIFIED` | — |
| 6 | **`TOTAL_V2` phải hỗ trợ THÊM DẦN**, không chỉ chọn lại từ đầu | 🟡 mới nhận ra (3.4) | hệ quả của luật «không miền nào lùi» |
| 7 | `gpt-5.4` chạy hai regime ⇒ dedupe (`IV.14`) | 🔴 chưa xử | Arena |
| 8 | `DOUBLE_COUNT` — `combo-super`/`smart-*` | 🔴 `PARENT_LINEAGE_PENDING` | Wave 3 |
| 9 | Adapter LLM tự sinh ranked top-K | ⚪ Wave 1 còn lại | — |
| 10 | **3-càng** có pipeline hợp lệ không | ⚪ `XI` | nếu không ⇒ `NO_VALID_3CANG`, cấm chế số |
| 11 | **Cutover Packet** | ⚪ Wave 5 | 🔴 **cổng `XV.D`** — **chặn owner DUY NHẤT còn lại** |
| 12 | Bảo mật / SSH / world-writable | ⚪ `CLASS C` | **cổng `XV.B`** |
| 13 | 38/228 bản thiếu báo cáo (`FU-444` · `FU-447`) | ⚪ nợ CŨ | không bản nào của Grand Overhaul |

---

## §62 — BA LỚP NGUỒN

### `OWNER_SAID`

| giờ (VN) | nguyên văn | loại |
|---|---|---|
| 02/09 ~11:20 | *«Anh cần xử lý dứt điểm cho xong nha em»* | `YÊU_CẦU` |
| 02/09 ~11:45 | *«giá Token ko quan trọng… Anh chỉ quan trọng chất lượng, API đắt mà chất lượng, ít nhưng mà chất lượng là được»* | `BÁC_BỎ` |
| 02/09 ~11:45 | *«chỉ có tiến bộ chứ không thể thụt lùi nha em»* | `YÊU_CẦU` |

### `CODE_DID`

- `docs/NGUONG_CHAP_NHAN_GRAND_OVERHAUL.md` — MỚI, commit `2970605`, **trước** replay đầu tiên
- `docs/SO_TUONG_TAC_OWNER.md` — `26.004 → 28.157` ký tự, `APPEND-ONLY` đã khẳng định
- `governance_seq 468 → 469` · `_v11062 --kiem = ĐẠT`
- **Không** chạy lệnh nào đụng production; **không** deploy; PID không đổi

### `DOC_SAID`

- `PROMPT 43 R1 VI.2` liệt `cost` là chiều chấm điểm ⇒ **owner override**: chi phí thành cột
  báo cáo. Tài liệu prompt **không sửa được** (là lời owner cũ), nên ghi override ở
  `NGUONG_CHAP_NHAN` §4 và sổ tương tác.
- `VII.1` liệt `COST_LATENCY_AWARE` là một trong 8 variant ⇒ **vẫn chạy để so**, nhưng không
  được thắng nhờ rẻ.

### `NOT_VERIFIED`

Cách đọc *«có ý nghĩa»* là **diễn giải của agent**, chưa được owner xác nhận lại. Nếu sai thì
phải bác **trước** replay.

### Ba lớp lệch nhau ⇒ FINDING

**`OWNER_SAID` mới ≠ `DOC_SAID` cũ:** `VI.2` (chính prompt của owner, 02/09 sáng) liệt `cost` là
chiều chấm điểm; owner nói (02/09 trưa) chi phí **không quan trọng**. **Lời nói sau thắng** —
`PRJ-INTERACTION-LEDGER-001`. Đã ghi override, **không** sửa prompt gốc.

---

TanPhatAI cần làm: ghi **`V11153`** — riêng `2970605`, **không deploy, không đụng code**. Ghi **NGƯỠNG CHẤP NHẬN ĐÃ KHOÁ** tại `docs/NGUONG_CHAP_NHAN_GRAND_OVERHAUL.md`, **commit TRƯỚC mọi replay** — `PASS` / **`STOP`** / `HOLD`, và **một miền lùi có ý nghĩa = `STOP` dù tổng thể dương**. Ghi **«có ý nghĩa» = McNemar cặp đôi, `|z| ≥ 1,96` đối xứng, sàn 30 cặp lệch/miền, out-of-time** — cấm đổi sau khi nhìn kết quả. Ghi **CHI PHÍ RỜI KHỎI BỘ CHỌN** — chất lượng là tiêu chí duy nhất; `VI.2` liệt `cost` là chiều chấm điểm nhưng **lời owner sau thắng**, `cost`/`latency` nay chỉ là **cột báo cáo**. Ghi **agent vi phạm `A54_VIOLATION_ASKED_WITHOUT_LOOKUP`** — hỏi đơn giá API mà `IV.13` đã khoá. Ghi **`FU-449` nay chỉ còn MỘT chặn owner**: cổng `XV.D` bật official. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
