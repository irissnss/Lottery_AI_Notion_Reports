# CONVERSATION CONTEXT — V11158 · 03/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `CURRENT_ACTOR = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Owner cắt ngang giữa phiên
> bằng hai tin nhắn trực tiếp trong IDE, **có hiệu lực ngay**. Chúng đổi thứ tự việc của phiên
> này, và **owner đúng ở cả hai câu**.

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 03/09 ~13:05 | *«⚠️ 🔬 DeepSeek Reasoner 43% 30d · ⚠️ 🤖 GLM 5.2 45% 30d — 2 model này không ra output sẵn kiểm tra dùm anh luôn em»* | `YÊU_CẦU` | tra ra **hai nguyên nhân khác nhau**, đo bằng lượt gọi thật với đúng prompt production | `ĐÃ_LÀM` |
| 03/09 ~13:20 | *«fix cho chạy ra output luôn chứ em. Chưa tới giờ block mà em.»* | `YÊU_CẦU` | vá **bốn** chỗ, deploy đủ trong `13:25–13:50`, trước block 15:30 | `ĐÃ_LÀM` |
| (phiên trước) | mục `B` — *«Áp materializer repair vào production theo backup/migration gate… Repair/recompute đúng tập 877 dòng… Rerun phải idempotent… Neo FINAL và dữ liệu lịch sử immutable không drift.»* | `YÊU_CẦU` | deploy + recompute 540 cặp, sổ 8.287 mục | `ĐÃ_LÀM` |

### Vì sao owner đúng — bằng số

Owner nhìn thấy `43%` / `45%` kèm ⚠️ và nói *«không ra output»*. Đo ra:

| | lượt rỗng / tổng, 30 ngày | WR tính CẢ lượt rỗng | WR chỉ lượt CÓ ra số |
|---|---|---|---|
| `glm-5.2` | **17/89 (19,1%)** | **43,8%** | **54,2%** |
| `deepseek-reasoner` | 5/88 (5,7%) | 56,8% | 60,2% |

Cả 22 lượt rỗng đều bị chấm `LOSE`. Với `glm-5.2` đó là **10,3 điểm** win-rate bị trừ vì **lỗi
hạ tầng**, không phải vì model đoán kém.

Và câu *«Chưa tới giờ block mà em»* cũng đúng: lúc đó `13:20`, còn **2 giờ 10 phút** trước block
`15:30` — đủ cho cả bốn bản vá cộng kiểm.

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| deploy materializer role-at-time | 🟢 `PID 3279630 → 3289958` · nhập thử **trước** restart |
| đo phạm vi trước khi ghi | 🟢 tái lập đúng **877** dòng owner nêu |
| 🔴 phát hiện `V11155` mới vá **279/1.058** thua ảo | phân rã 4 lớp: `PRE_EXISTENCE` **2.352/760** |
| quét ngược người đọc | 🟢 kết quả **ÂM** — bộ gom đã chặn sẵn `parse_ok=1`, không route `/du-doan` nào |
| vá nốt 3 lỗi cùng khối `_thieu` | 🟢 chạy thử trên **bản sao 804 MB** trước khi áp thật |
| recompute 540 cặp | 🟢 thua ảo `1.058 → 0` · idempotent **0 dòng lệch** · neo 558 nguyên |
| ❌ bước lập sổ treo giữa chừng | 8.287 truy vấn lẻ — dựng lại bằng một lần nạp |
| tra 2 model owner báo | 🟢 `deepseek-reasoner` `reasoning_tokens=40.215` > trần 32.768 |
| ❌ giả thuyết đầu về `glm-5.2` SAI | lượt hỏng có `finish_reason=stop` ⇒ **không phải** cắt token |
| bắt nguyên văn response hỏng | 🟢 thừa **một dấu `{` mở** — và biến thể `{"":{…}}` hỏng **im lặng** |
| ❌ cổng bất biến BÁO ĐỘNG GIẢ | gây **một lần gỡ về thừa** — thủ phạm: `significant_pairs` |
| vá + deploy 4 chỗ | 🟢 test JSON **9/9** · `IMPORT_OK 480 720 840 300` |

---

## 3 · Vấp trong phiên — bốn lần

**🔴 ① Cổng bất biến của chính agent báo động giả, gây một lần gỡ về thừa.** Nó băm nguyên văn
`USER_PAYLOAD` rồi kết luận *«PROMPT OFFICIAL ĐỔI»* ở cả ba miền — trong khi thay đổi duy nhất
là hai hằng số `max_tokens`, thứ **không dính gì** tới dựng prompt. Dấu hiệu đáng ra phải nhận
ra ngay: *«nguyên nhân này không thể gây ra hậu quả kia»*. Đối chứng đúng điều kiện (hai tiến
trình rời, **không deploy gì**) phơi ra thủ phạm: dòng `significant_pairs` xếp các cặp **đồng
hạng** theo `PYTHONHASHSEED`. **Lần thứ ba** cùng họ *«dụng cụ đo đứng sai chỗ»*.

**🔴 ② Giả thuyết đầu về `glm-5.2` sai, và chính phép đo bác bỏ nó.** Agent kết luận cả bốn chữ
ký lỗi *(`char 2` · `char 3` · `Unterminated string` · `Expecting ','`)* đều là **cắt giữa
chừng**, dựa trên latency 510s. Lượt xác nhận sau deploy hỏng với `finish_reason = stop` — model
kết thúc **bình thường** ⇒ ca đó không phải cắt token. Phải đi bắt **nguyên văn** mới thấy tật
thật. Bài học đúng `RM-14`: **không nhìn thấy ký tự thật thì không được đoán cách vá**.

**🟡 ③ Bước lập sổ before/after treo** vì 8.287 truy vấn lẻ trên bảng không index. Phần **ghi DB
đã xong và đúng** — chỉ khâu lập sổ chết. Dựng lại bằng một lần nạp.

**🟡 ④ Hàm trợ giúp của bộ test tự báo HỎNG cho hai ca đúng** — nhánh `except` gán cứng
`ok = False` nên hai ca *«phải NÉM»* không bao giờ đạt được. Lỗi của **thước**, không của vật đo.

---

## 4 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 `PID 3299063` · health 200 · `LANE=shadow` · neo 558 **nguyên qua 8 lần restart** |
| official | 🟢 **không đổi một ký tự prompt** — 6 băm khớp |
| 4 bảng khoá | 🟢 `14080 · 562 · 15403 · 13903` — không đổi |
| bảng chấm | 🟢 `16.959` dòng · **thua ảo 0** · `parse_ok 12.221` |
| role-at-time | ✅ `DEPLOYED` + recompute xong |
| trần token · timeout · vá JSON | ✅ `DEPLOYED` + `RUNTIME_PROVEN` bằng lượt gọi thật |
| `glm-5.2` — trần token có phải nguyên nhân | 🟡 **CHƯA chứng minh** — đo 14 ngày |
| `SCHEDULED_SHADOW_OUTPUT_PROVEN` | 🔴 **PENDING** — chờ 16:00/17:00 |
| `POOL_VERDICT` | **`HOLD`** |
| Prompt 43 R1 | **`PARTIAL`** |

---

TanPhatAI cần làm: ghi **`V11158`** — `governance_seq 474`, công khai bản này. Ghi **hai tin nhắn trực tiếp của owner giữa phiên** (13:05 · 13:20) — chúng **đổi thứ tự việc** và **owner đúng ở cả hai**. Ghi **code đi trước tài liệu** ở bốn bản vá (mã deploy trước, sổ ghi cùng phiên theo `PRJ-INTERACTION-LEDGER-001`), sổ tương tác đã cập nhật tại `docs/SO_TUONG_TAC_OWNER.md` mục *«03/09/2026 — phiên V11158»*. Ghi **agent tự bác bỏ một giả thuyết của chính mình** (`glm-5.2` không phải chỉ do cắt token) và **cổng của chính agent báo động giả gây một lần gỡ về thừa** — cả hai đều là vấp, không giấu. **Không mở FU mới.** **Không mở Prompt 44.**
