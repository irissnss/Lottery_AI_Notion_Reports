# CONVERSATION CONTEXT — V11157 · 03/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `CURRENT_ACTOR = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Mệnh lệnh trực tiếp trong
> IDE, **có hiệu lực ngay**. Bản này chứa **một correction của owner LẬT NGƯỢC kết luận agent
> vừa công bố hôm qua** — tài liệu nào còn ghi `NO_VALID_3CANG` thì **tài liệu phải sửa**.

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 03/09 ~09:00 | *«3 càng anh đang xây dựng với số đuôi bạch thủ.»* | **`BÁC_BỎ`** | rút lại `NO_VALID_3CANG`; đọc lại mã và sửa verdict thành `SUBSTANTIALLY_VALID` | `ĐÃ_LÀM` |
| 03/09 ~09:00 | *«Vấn đề anh cần ở đây là đơn model có cần output không?»* | `HỎI` | trả lời: **KHÔNG** — và `UCC` **không cần sửa**, ranked adapter vốn đã đúng hợp đồng | `ĐÃ_LÀM` |
| 03/09 ~09:00 | `PROMPT 43 R1 · CONTINUATION` 10 mục `I`–`X` | `YÊU_CẦU` | thi hành `A` → `C`; `B` mới ở tầng test | `ĐANG_LÀM` |

### Correction này lật cái gì

`V11156` (agent, 03/09 rạng sáng) kết luận:

> *«**`NO_VALID_3CANG`** cho tiêu chí generator… lấy nguyên bạch thủ làm đuôi rồi chỉ chọn một
> chữ số đầu ⇒ **đúng thứ owner cấm ở mục `XI`**»*

Owner nói **ngược lại**: prefix + BT **CHÍNH LÀ** thiết kế. Agent đã đọc mục `XI` theo nghĩa
*«phải có direct three-digit generator»* và suy ra vi phạm — nhưng chính wording đó nay
owner tuyên **`VOID`**.

**Và phép đọc mã của agent cũng sai.** Đọc kỹ `main.py:10587-10640` thì bộ chọn prefix **không
hề tuỳ tiện**: giữ số 0 đầu · **không lookahead** · chọn prefix bằng **đếm (prefix+BT) xuất hiện
như chuỗi con ở bất kỳ vị trí nào trong giải suốt 180 ngày** · tiebreak tất định · và
`V10753.1` **đã backtest 118 ngày**, thắng cửa sổ 90 ngày ở **cả ba miền**.

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| mục `A` — kiểm scheduled runtime proof | **11 lượt shadow thật** `05:22–05:32`, `PID 3249633`, neo 558 khớp |
| ❌ chứng minh prompt shadow sạch | **KHÔNG được** — `journalctl` không bắt `print()`, `prompt_layers` giống hệt |
| 🟢 vá lỗ hổng quan sát | 3 khoá regime vào `prediction_trace`, mỗi lượt **tự khai** |
| ❌ bản vá đầu có `NameError` | **bắt được trước khi deploy** — biến không cùng tầm hàm |
| 🟢 deploy instrument | `PID 3249633 → 3279630` · backup bốn lớp lại đủ |
| 🔴 rút lại `NO_VALID_3CANG` | verdict sửa: `SUBSTANTIALLY_VALID`, thiếu lineage/trace |
| 🟢 mục `C` audit 3-càng đầu-cuối | bảng đầy đủ caller → BT → selector → persist → scorer → UI |

---

## 3 · Vấp trong phiên — bốn lần

**🔴 ① Agent kết luận `NO_VALID_3CANG` trên một tiền đề mà owner vừa tuyên `VOID`.**
Đây là lỗi **đọc sai ý định**, không phải lỗi đo: con số `561/561 = 100%` **đúng**, nhưng nó
chứng minh *«3-càng bám BT»* — mà đó **là thiết kế**, không phải khuyết tật. Agent đã dịch một
quan sát đúng thành một phán quyết sai.

**🔴 ② Và agent đọc mã chưa đủ sâu trước khi phán.** Bản `V11156` mô tả bộ chọn prefix như thể
tuỳ tiện, chỉ ghi nhận *«chọn theo tần suất»* rồi nhấn mạnh fallback `(bt[0]+1)%10`. Đọc kỹ hôm
nay mới thấy: **không lookahead**, **giữ số 0 đầu**, **có backtest 118 ngày**, và **official bám
`bach_thu` sau override** — tức tuân đúng `D.2` từ trước khi có `D.2`.

**🔴 ③ Không quan sát được chính thứ vừa deploy.** Scheduler nổ thật nhưng ba đường kiểm đều
câm: `journalctl` chỉ bắt `logging` (**0 dòng** `[Phase 14A]` cả ngày), `prompt_layers` giống
hệt bốn nhóm, so độ dài prompt **nhiễu** (`−799` vs `~1.281` mong đợi). Theo `RM-15`, không
quan sát được thì **coi như chưa chứng minh** ⇒ ghi `PENDING`, **cấm pass-wash**.

**🟡 ④ Bản vá quan sát suýt làm hỏng dự đoán thật.** Bản đầu viết thẳng `_ctx_only_lane` vào
khối trace, nhưng dòng đó nằm trong `log_prediction_trace` (`:1543`) còn biến định nghĩa trong
`analyze_and_predict` (`:6402`) ⇒ **`NameError` lúc chạy**. Bắt được bằng phép kiểm tầm biến
**trước khi deploy**. Sửa thành hai tham số tuỳ chọn mặc định `False` — gọi cũ vẫn chạy, mặc
định `LEGACY_PROMPT`, fail-safe đúng chiều.

---

## 4 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 `PID 3279630` · health 200 · `LANE=shadow` · neo 558 **không drift** |
| official | 🟢 **chưa đổi một ký tự** |
| `DEPLOYED` | ✅ |
| `SERVICE_ENV_RUNTIME_PROVEN` | ✅ |
| `SCHEDULED_SHADOW_OUTPUT_PROVEN` | 🔴 **PENDING** — chờ lượt 16:00/17:00 hôm nay |
| 3-càng | 🟢 `SUBSTANTIALLY_VALID` · 🟡 thiếu lineage/trace |
| role-at-time | ✅ code+test · ❌ chưa deploy |
| `POOL_VERDICT` | **`HOLD`** |
| Prompt 43 R1 | **`PARTIAL`** |

---

TanPhatAI cần làm: ghi **`V11157`** — riêng `f93f498` + `4087728`, `seq 473`, công khai bản này. Ghi **owner BÁC BỎ kết luận `NO_VALID_3CANG` của `V11156`** — *«3 càng anh đang xây dựng với số đuôi bạch thủ»* ⇒ **prefix + BT LÀ thiết kế**; wording *«direct 3-digit generator»* nay **`VOID`**; ba lựa chọn A/B/C **HUỶ**. Ghi **verdict sửa `SUBSTANTIALLY_VALID`** kèm bằng chứng: không lookahead · giữ số 0 đầu · backtest `V10753.1` 118 ngày · official bám `bach_thu` **sau override** · scorer exact 3 chữ số · rỗng ⇒ `PENDING`. Ghi **trả lời owner: đơn model KHÔNG cần output 3-càng**, `UCC` **không sửa**. Ghi **`SCHEDULED_SHADOW_OUTPUT_PROVEN = PENDING`** — có 11 lượt thật nhưng **không quan sát được**; đã vá bằng 3 khoá regime và deploy. Ghi **agent suýt gây `NameError` trên đường dự đoán thật**, bắt được trước khi deploy. Ghi **`V11128` kết luận theo TÊN** (`RM-10`) — 3-càng nằm dưới tên `lo3`. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
