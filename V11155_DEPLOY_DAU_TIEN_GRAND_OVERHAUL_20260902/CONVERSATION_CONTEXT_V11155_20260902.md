# CONVERSATION CONTEXT — V11155 · 02/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`. **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Mệnh lệnh trực tiếp trong
> IDE, **có hiệu lực ngay**. Bản này ghi **lần deploy đầu tiên của Grand Overhaul** — owner
> **cho phép tường minh**, agent **không tự ý** đụng production.

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 02/09 ~20:20 | `PROMPT 43 R1 · CONTINUATION AFTER V11154`, 12 mục `A`–`L` | `YÊU_CẦU` | thi hành `B` → `C` → `E` → `D` → `D5` → `F` | `ĐÃ_LÀM` |
| 02/09 ~22:20 | *«deploy chặn là sao em? lý do là gì cho anh hay»* | `HỎI` | giải thích **lớp phân quyền của Claude Code** chặn, **không** phải cổng dự án; nêu chính xác bốn hành vi bị xếp rủi ro cao (`scp` ghi đè production · `sed -i` sửa systemd · `systemctl restart` · `cp` backup); nêu ba lối owner chọn | `ĐÃ_LÀM` |
| 02/09 ~22:40 | *«Em tiến hành deploy 1 cách tự động cho anh, với việc backup đầy đủ dự phòng mọi rủi ro ghi mốc lịch sử thời điểm quan trọng này dùm anh. Tiếp tục xử lý các vấn đề dứt điểm cho anh trong tối nay, backup và deploy đầy đủ cho anh.»* | **`YÊU_CẦU`** | backup 4 lớp **768 MB** → deploy → runtime proof → ghi mốc | `ĐÃ_LÀM` |
| 02/09 ~23:05 | *«tiếp theo là gì e»* | `HỎI` | làm nốt `D5` (chuỗi override) rồi phát hành bản này | `ĐÃ_LÀM` |

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| `B` sửa hai mâu thuẫn `V11154` | ✅ tại đúng chỗ công bố (`d8e1162`) |
| `C` sửa dụng cụ đo | ✅ `1.600↔1.636` reconcile bằng **ID dòng** · phân rã 4 lớp · META **19/19** |
| `E` hợp đồng thống kê | ✅ bản 2 · **17,4 năm** ⇒ guardrail vận hành |
| `D` counterfactual + selector | ✅ **phá vòng tròn** bằng lịch sử git — **97,8%** |
| `D5` chuỗi override | ✅ **bốn** cái, nay còn **một** |
| **`F` DEPLOY** | ✅ **`DEPLOY_OK · RUNTIME_PROVEN`** |
| backup | ✅ **768 MB**, gồm **DB đầy đủ 802 MB** |
| mốc lịch sử | ✅ `MOC_LICH_SU.json` — cả trước lẫn sau |

---

## 3 · Vấp trong phiên — bốn lần

**🔴 ① Hai lần dụng cụ đo đứng SAI CHỖ, kéo theo một lần gỡ về THỪA.**

Bộ deploy chạy lần đầu lúc `22:45`, qua hết bảy cổng, rồi **tự gỡ về** ở bước 8 vì đọc ra
`LANE=off`. Nguyên nhân: bước đó mở một tiến trình Python **RỜI** qua SSH, mà tiến trình rời
**không thừa kế** `Environment=` của systemd. Bước POST **cùng lượt** đã cho thấy service có
`LANE=shadow`.

Sập **đúng bẫy đó lần thứ hai** ngay sau, ở phép kiểm bất biến official: báo `KHÁC=False` cả ba
miền, tức *«shadow không sạch»* — cũng vì chạy tiến trình rời.

**Cả hai lần production đều đúng; chỉ dụng cụ đo đứng sai chỗ.** Gỡ về lần một **sạch tuyệt
đối**: `GO_VE_OK`, neo 558 nguyên, không mất dòng nào. Cổng sai chiều **an toàn** — nó gỡ về khi
không chứng minh được — nhưng **một cổng hay báo động giả là một cổng sẽ bị tắt**. Đã dựng
`vps_service_env.py` nạp biến từ `/proc/<PID service>/environ`.

**🟡 ② `\0` trong lệnh bash thành null byte thật** — lần thứ **năm** trong dự án, dù đã ghi bộ
nhớ dài hạn. Lần này ở `tr '\0'`. Vá bằng mã bát phân `'\000'`.

**🟡 ③ Con số `877` khác `869`** của bản điều tra trước. Đây là **ranh giới phân loại**
(`869 + 8` so với `877 + 0`), không phải bất đồng dữ liệu — tổng `3.296` và hai lớp
`PRE_EXISTENCE 2.352` / `TRUE_MISSING 67` **trùng khít**.

**🟡 ④ `V11154` mô tả «một» override; thực tế BỐN.** Đọc mã thấy bốn cái xếp chồng
(`main.py:10228 · 10247 · 10264 · 10284`); đo dữ liệu thì **hai đã tự dừng** từ cuối tháng 7.
Ba tầng — tài liệu, mã, dữ liệu — cho **ba câu trả lời khác nhau**, và chỉ **tầng dữ liệu** nói
đúng hiện tại.

---

## 4 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 **`DEPLOYED · RUNTIME_PROVEN`** · `PID 3249633` · health 200 |
| official | 🟢 **KHÔNG đổi một ký tự** — `MN 13.609 · MT 13.104 · MB 12.677` trước = sau |
| lane shadow | 🟢 prompt **ngữ cảnh thuần** — hết bảng xếp hạng, hết mệnh lệnh bắt chước |
| `FINAL` cũ | 🟢 neo 558 `a82c508d3569abda…` **KHÔNG DRIFT** |
| backup | 🟢 **768 MB** · DB `integrity_check = ok` · gỡ về **đã chứng minh chạy được** |
| runtime proof theo lịch | 🔴 chờ lượt shadow **~05:00 sáng 03/09** |
| model action | ⚪ **`HOLD`** — chưa đụng model nào |
| chặn owner | 1 cổng `XV.D` (Cutover) + 1 cổng `XV.B` (`CLASS C`) |

---

TanPhatAI cần làm: ghi **`V11155` — DEPLOY ĐẦU TIÊN của Grand Overhaul**, owner **cho phép tường minh** 02/09 ~22:40; agent **không tự ý** đụng production. Ghi **mốc `V11154_DEPLOY_CONTEXT_ONLY_SHADOW`** — `PID 3248913 → 3249633`, `22:46:51 +07`, `gpt_analyzer f83e6f3c1eca2f08`, neo 558 **không drift**. Ghi **backup bốn lớp 768 MB** gồm **DB đầy đủ 802 MB** (`integrity_check = ok`), **gỡ về đã chứng minh chạy được** ngay trong phiên. Ghi **OFFICIAL BẤT BIẾN** — `13.609 / 13.104 / 12.677` trước = sau. Ghi **hai lần dụng cụ đo đứng sai chỗ** — tiến trình rời không thừa kế `Environment=`; **production luôn đúng**; đã dựng `vps_service_env.py`. Ghi **`V11154` mô tả «một» override nhưng thực tế BỐN**, và **hai đã tự dừng cuối tháng 7** — chỉ MN còn chạy (~1/3 số ngày); `G5` **nhỏ hơn tưởng**; **cấm xoá 78 lần override lịch sử**. Ghi **runtime proof theo lịch chờ ~05:00 sáng 03/09** — agent **không ép** lượt chạy vì gọi tay không phải bằng chứng theo lịch. Ghi **`POOL_VERDICT = HOLD`**. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
