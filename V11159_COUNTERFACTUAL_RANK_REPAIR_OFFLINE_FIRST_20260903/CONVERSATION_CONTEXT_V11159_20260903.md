# CONVERSATION CONTEXT — V11159 · 03/09–04/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `CURRENT_ACTOR = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Bản này chứa **một RÚT LẠI
> lật ngược điều agent đã khẳng định HAI LẦN trong cùng ngày**. Tài liệu nào còn ghi *«official
> không đổi một ký tự prompt»* cho `V11157`/`V11158` thì **tài liệu phải sửa**.

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 03/09 ~22:05 | *«Tiếp theo là gì em? phân tích đánh giá dự đoán hôm nay, việc xử lý prompt thuần ngữ cảnh và các vấn đề đơn model và total xử lý tới đâu rồi đo được gì rồi? Hôm nay vẫn tệ như mọi ngày»* | `HỎI` + `CHIA_SẺ` | đo 90 ngày × 3 miền vs nền đúng; xác nhận owner **đúng**, và **không phải mới** — `V11116` (25/08) đã ghi | `ĐÃ_LÀM` |
| 03/09 ~22:15 | `PROMPT 43 R1 · CONTINUATION AFTER V11158 · COUNTERFACTUAL RANK REPAIR OFFLINE-FIRST` (19 mục `I`–`XIX`) | `YÊU_CẦU` | thi hành `IV`→`XVI`; `A` và một phần `XIV` còn PARTIAL | `ĐANG_LÀM` |
| 03/09 ~23:5x | *«làm xong chả báo cáo gì là sao em?»* | **`BÁC_BỎ`** | **đúng** — agent báo miệng mà chưa ra bản nào. Ghi bốn mặt + báo cáo công khai ngay | `ĐÃ_LÀM` |
| 04/09 ~00:0x | *«ok vậy đợi soi xong tổng hợp đề xuất báo cáo tổng hợp 1 lần luôn em»* | `ĐỔI_ƯU_TIÊN` | dừng báo lẻ, chờ đợt soi 5 mặt xong rồi gộp một bản | `ĐÃ_LÀM` |

### Owner sửa một đề xuất SAI của agent

Agent đề xuất: *«đổ đầy `output_counterfactual_rank` cho 180 ngày, xếp hạng 27 model **theo kết
quả thật** để biết đáng ra phải chọn model nào»*.

Owner tuyên câu đó phải sửa thành: *«dựng `output_counterfactual_rank` từ **đúng selector/TOTAL
và dữ liệu có trước region lock**; sau đó mới dùng kết quả thật để chấm rank **đã đóng băng**»*.

**Khác biệt không phải chữ nghĩa.** Bản của agent là **oracle hindsight** — dùng kết quả ngày D
để xếp hạng cho chính ngày D. Toàn bộ mục `X` của prompt (khoá chống oracle, hai pha, năm META
test) sinh ra từ chỗ này.

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| pre-flight + clone DB | 🟢 809 MB · `integrity_check=ok` · neo khớp · production READ-ONLY |
| tái lập selector (Gate D) | 🟢 **99/99 = 100,0%** · lệch điểm `0,000000` |
| ❌ vòng 1: so voter với bundle đã cắt top-10 | báo **15 ca lệch giả** |
| ❌ vòng 2: thiếu `round()` của bản gốc | báo tiếp **19 ca lệch giả** |
| khoá chống oracle (Gate E) | 🟢 **6/6 `ANTI_ORACLE_PROVEN`** |
| ❌ META test đầu xoá cả ba ngày mẫu cùng lúc | báo `ORACLE_CONTAMINATED` **giả** 6/8 ô |
| ba comparator + add-one 973 lượt | 🔴 **không cái nào qua cổng Holm** |
| tính sức mạnh phép đo | 🟢 MT **~65 ngày** · MN 907 · MB 1.295 |
| đợt soi 5 mặt song song (30 agent) | 🟢 xong — và **bắt được lỗ rò** |
| 🔴 **RÚT LẠI** «official không đổi prompt» | `gpt-oss-120b` rò prompt thí nghiệm vào official |
| ghi bốn mặt + báo cáo công khai | 🟢 `governance_seq → 475` |

---

## 3 · Vấp trong phiên — NĂM lần, cùng MỘT họ

Cả năm đều là **THƯỚC sai, không phải VẬT ĐO sai**. Ghi đủ vì đây là họ lỗi đã tái phát **năm
lần trong một ngày**, và lần thứ năm là lần **nguy hiểm nhất**.

**🔴 ① Cổng bất biến official KHÔNG THỂ bắt lỗi rò prompt.** Nó dựng prompt bằng
`model="gemini-2.5-pro"` — một model **không** nằm trong `SHADOW_GATE_MODELS`. Nó **về mặt cấu
trúc không thể** phát hiện một lỗi định tuyến **theo model**. Agent đã hai lần công bố *«official
không đổi một ký tự prompt»* dựa trên cổng này.

**🔴 ② So tập voter ĐẦY ĐỦ với bản bundle chỉ lưu `ranked[:10]`** (`main.py:10467`) — báo 15 ca
lệch giả, suýt kết luận «selector sai».

**🔴 ③ Thiếu `round(bt_rate,1)` + `round(bt_weight,3)`** của `database.py:3422-3429` — báo tiếp
19 ca lệch giả. Giữ độ chính xác đầy đủ nghe «đúng hơn» nhưng **không tái lập được** thứ
production thật sự chấm.

**🔴 ④ META test đầu xoá kết quả CẢ BA ngày mẫu cùng lúc** — mà chúng nằm trong cửa sổ 30 ngày
của nhau ⇒ đổi TRỌNG SỐ chứ không phải lộ oracle. Báo `ORACLE_CONTAMINATED` giả.

**🟡 ⑤ Quét mốc cắt dựa trên giả thuyết sai** — mất trọn một vòng chạy.

---

## 4 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 `PID 3299063` · `NRestarts 0` · health 200 · **6/6 bảng không đổi một dòng** |
| neo 558 | 🟢 **NGUYÊN** |
| `output_counterfactual_rank` | 🟢 **vẫn `0/17.040`** — chưa ghi production |
| `PRODUCTION_MUTATION_COUNT` | 🟢 **0** |
| Gate B · D · E · G | ✅ ĐẠT |
| Gate F | 🔴 không comparator nào qua cổng |
| Gate A | 🟡 routing PASS · **semantic clean KHÔNG ĐẠT** |
| Gate C | 🟡 ĐẠT có điều kiện — 111/540 ô thiếu lớp L3 (`RM-13`) |
| 🔴 **rò prompt vào official** | **CHỜ OWNER** — chạm đường official, cần packet riêng |
| `POOL_VERDICT` | **`HOLD`** |
| Prompt 43 R1 | **`PARTIAL`** |
| `23/09/2026` | **READOUT CHECKPOINT** — không phải hạn buộc promote |

---

TanPhatAI cần làm: ghi **`V11159`** — `governance_seq 475`, công khai bản này. Ghi **owner BÁC BỎ** *«làm xong chả báo cáo gì»* — agent báo miệng mà chưa ra bản, đã sửa ngay trong phiên. Ghi **owner ĐỔI ƯU TIÊN** *«đợi soi xong tổng hợp 1 lần luôn»*. Ghi **owner sửa một đề xuất SAI của agent**: bản cũ *«xếp hạng 27 model theo kết quả thật»* là **oracle hindsight**; bốn khoá ngữ nghĩa owner chốt cho `output_counterfactual_rank` phải được tôn trọng. Ghi **RÚT LẠI** *«official không đổi một ký tự prompt»* của `V11157`/`V11158` — **SAI**, `gpt-oss-120b` rò prompt thí nghiệm vào chuỗi `ai_chain` và **là voter của bạch thủ MB=32**; **nhánh đối chứng official KHÔNG sạch từ 03/09**. Ghi **agent vấp NĂM lần cùng một họ «thước sai»**, không giấu lần nào. **Code KHÔNG đi trước tài liệu ở phiên này** — work package offline, 0 dòng production bị ghi, 0 deploy. **Không mở FU mới. Không mở Prompt 44.**
