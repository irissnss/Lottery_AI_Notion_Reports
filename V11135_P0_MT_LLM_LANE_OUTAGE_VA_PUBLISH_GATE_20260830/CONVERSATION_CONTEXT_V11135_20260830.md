# CONVERSATION CONTEXT — V11135 · 29–30/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — nguyên văn

**29/08 00:47** — lệnh P0:

> *« MT 28/08 có FINAL hợp lệ: row id=786, finalized_at=16:55, trước lock MT 16:58, bach_thu=11,
> model_count=6, is_fallback=0. Cấm tuyệt đối: recompute row 786; đổi số; backfill LLM/Combo sau
> khi biết kết quả; sửa hash/lineage/created_at của FINAL 28/08. »*
>
> *« Không được tiếp tục dùng "tồn tại một dòng ATTEMPT trong log" làm bằng chứng token đã tiêu. »*
>
> *« Anonymous 401 chỉ chứng minh FU-438 auth guard. »*
>
> *« Không gọi FINAL là ML-only nếu chưa chứng minh đủ sáu ID. »*

**29/08 21:42** — lệnh chất lượng:

> *« toàn bộ FINAL/lane dự đoán ngày 29/08 đều sai; một số đơn model có tín hiệu; TOTAL/FINAL lại
> chọn tệ. »*
>
> *« Không dừng ở kết luận INSUFFICIENT_POWER. Không dùng một ngày để promote. »*

**30/08 ~12:40** — owner phê bình thẳng:

> *« MT nay đã sẵn sàng chưa nha em chứ hôm qua thì mất 1 ngày của anh rồi đó nha em… »*
>
> *« kiểm tra hoạt động hôm nay có ổn định không có các đề xuất điều chỉnh cần thực hiện những gì
> xử lý ra sao anh thấy em vẫn quá lòng vòng hời hợt quá em »*

**Lời phê bình này đúng và tôi ghi nhận:** tôi đã đo rất nhiều nhưng **để `V11135` trễ ba bản** —
HEAD công khai đứng ở `ed73afe` (V11134) suốt trong khi đã có hai bản vá chạy thật trên
production. Báo cáo này là việc đóng lại chỗ đó.

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| truy nguyên nhân MT 28/08 | **race 42 giây** · `scheduler.py:5338` vs `:5368` |
| vá scheduler — máy trạng thái | 15/15 thử · PID `2694667→2866664` |
| 🟢 **live proof 29/08** | **MT lấy lại 8/8 LLM**, `model_count 6→13` |
| tìm nguyên nhân THỨ HAI | cổng publish `>= 15` làm trắng bundle hợp lệ |
| vá cổng publish | 13/13 thử · PID `2866664→2897561` · end-to-end ĐẠT |
| niêm phong row 786 | `sha(spj)` PRE==POST qua **hai** lần deploy |
| xuất sáu component | 4 ML base + 2 aggregator · `shadow ∩ = 0` |
| audit 29/08 | sáu verdict · `NO_OVERRIDE` ×3 · scorer 12/12 đúng |
| cửa sổ đóng băng n=273 | M0 **30,77%** thấp nhất trong năm phép so |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### 🔴 V1 · Công bố một verdict quá mạnh rồi phải rút sau 2 giờ

`V11133` viết `SHADOW_CHANGED_FINAL = FALSE`. Con số 0/871 **đúng**, nhưng nó chỉ nói về **một**
kênh còn tôi viết như thể nói về **mọi** kênh. Kênh thứ hai: `gemini-3.5-flash` vào chấm điểm
Combo qua `ai_confirm` 3 lần, mỗi lần rơi đúng số được chọn.

**Bài học cụ thể:** trước khi viết `X = FALSE`, phải **đếm có bao nhiêu đường X có thể xảy ra**,
và nói rõ **đã soi đường nào**.

### 🔴 V2 · Suýt công bố kết luận SAI về hạ tầng

Truy vấn `scheduler_logs` trả rỗng ⇒ tôi in *«thực sự không có dòng nào»*. Sự thật **75 dòng**,
trong đó 26 dòng `ai_predict` — **chính là mắt xích tôi tìm cả buổi**. Nguyên nhân: cột `status`
không tồn tại, lỗi ra `stderr` mà hàm đọc chỉ lấy `stdout`. Bắt được nhờ **hai con số ngược nhau
trong cùng một phiên**. Nếu tin con số rỗng thì đã **hạ cấp verdict sai**.

### 🟡 V3 · Cổng của chính tôi mắc lỗi `RM-09`

Phép kiểm *«không official reader nào đọc lane shadow»* grep chuỗi thô ⇒ báo động giả vì
`main.py:16954` có `v10622_parallel_lane_shadow_live_board`. Đã neo lại, xác minh cả hai phía.

### 🟡 V4 · Counterfactual của tôi bị chính đối chứng âm bác

Mô hình quy đổi làm đổi top-1 ở **3/23 ca dù không bỏ gì**. Truy ra: manifest lưu **2 số** và
`factors` bỏ sót bonus hậu kỳ (`final_score` > tổng weight ở **85/87** ca).

### 🟡 V5 · Bộ thử bắt lỗ trong chính bản vá của tôi

Ba nhánh làm trắng, bản đầu tôi mới vá **hai**.

### 🟡 V6 · Bốn lỗi kỹ thuật + một sai giả định

Ký tự null thật trong `tr` · `stat -c %%Y` in ra `%Y` · `datetime()` trả `NULL` nuốt cả dòng ·
đặt tên tệp `signal.py` che module `signal` · phép kiểm `NRestarts` sai giả định (nó đếm restart
**tự động sau lỗi**, không đếm `systemctl restart`).

---

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| sửa row 786 | owner cấm tuyệt đối · chứng minh bất biến bằng hash |
| backfill LLM 28/08 | cấm chế prediction sau khi biết kết quả |
| gộp C1–C6 vào hotfix | mất khả năng quy nguyên bản vá scheduler |
| deploy C5 | emitter bỏ sót `SYSTEM_PROMPT` 16,4% · cổng `_v11107` vẫn thoát 1 |
| kết luận «TOTAL tệ» từ 29/08 | n=3, xác suất 0/3 = 22% ngay cả khi TOTAL đúng bằng nền |
| promote `gemini-2.5-pro` | p=0,078, chưa qua Bonferroni · một ngày không được dùng để promote |
| tắt override | 29/08 `NO_OVERRIDE` cả ba miền — override không dính |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| scheduler root fix | 🟢 `RUNTIME_PROVEN` |
| publish gate fix | 🟢 `RUNTIME_PROVEN` |
| FINAL lịch sử | 🟢 **BẤT BIẾN** — hash PRE==POST |
| 30/08 lúc 12:47 | PID `2897561` · health 200 · **0 lỗi/24h** · MN `BT=73 mc=15` · token `RUNNING→SUCCESS` |
| C1–C6 | ⚪ `CODED_NOT_DEPLOYED` — 108 phép thử ĐẠT |
| C5 | 🔴 `BLOCKED_NOT_IN_RELEASE` |
| Decision Packet | ⏳ chờ owner ký **một câu** |

---

TanPhatAI cần làm: ghi **hai bản vá `RUNTIME_PROVEN`** — scheduler token state machine (`a6c8bfff60b6→2961987d8c3a`, PID `2694667→2866664`) và publish gate DEGRADED (`ec2540331be1→42ffe2e6b456`, PID `2866664→2897561`); **live proof 29/08 MT lấy lại 8/8 LLM**. Ghi **FINAL lịch sử bất biến** (`sha(spj)` row 786 PRE==POST). Ghi **đính chính**: *«MT không có output»* → **`MT_LLM_LANE_OUTAGE`**; *«ML-only»* → **4 ML base + 2 aggregator**. Ghi **cửa sổ n=273: M0 30,77% thấp hơn cả bốc ngẫu nhiên 32,60% và model đơn tốt nhất 37,00%**, nhưng **0/13 vượt có ý nghĩa** ⇒ tín hiệu kiến trúc, chưa đủ để cắt TOTAL. **C1–C6 chưa deploy · C5 blocked.** **Decision Packet chờ owner ký một câu** về hai lane shadow 30 ngày.
