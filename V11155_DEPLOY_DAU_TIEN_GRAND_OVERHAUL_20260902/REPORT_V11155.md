# REPORT V11155 — 🟢 **DEPLOY ĐẦU TIÊN CỦA GRAND OVERHAUL** · 02/09/2026

> `ACTOR_RUNTIME = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**
> **`DEPLOYED · RUNTIME_PROVEN`** cho instrument và lane shadow.
> **Official chưa đổi một ký tự.** `MODEL_ACTION_BLOCKED` · `POOL_VERDICT = HOLD`.

---

## 1 · TÓM TẮT

Đêm nay là **lần deploy đầu tiên** của cuộc cải tổ — và là lúc **đồng hồ đo bắt đầu chạy**.

| mục | kết quả |
|---|---|
| `B` sửa hai mâu thuẫn `V11154` | ✅ tại đúng chỗ công bố (`d8e1162`) |
| `C` sửa dụng cụ đo | ✅ `1.600↔1.636` reconcile · phân rã 4 lớp · META **19/19** |
| `D` counterfactual + selector | ✅ **phá được chứng minh vòng tròn** — `97,8%` |
| `E` hợp đồng thống kê | ✅ bản 2 · biên non-inferiority · Holm · **sự thật 17,4 năm** |
| `F` deploy | ✅ **`DEPLOY_OK · RUNTIME_PROVEN`** · backup **768 MB** |
| `D5` chuỗi override | ✅ **bốn** override, nay chỉ còn **một** đang chạy |

---

## 2 · OWNER YÊU CẦU GÌ — nguyên văn

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI.** Mệnh lệnh trực tiếp trong IDE, hiệu lực
> ngay (`PRJ-INTERACTION-LEDGER-001`).

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 02/09 ~20:20 | `PROMPT 43 R1 · CONTINUATION AFTER V11154` — 12 mục `A`–`L` | `YÊU_CẦU` | thi hành `B` → `C` → `E` → `D` → `F` | `ĐÃ_LÀM` |
| 02/09 ~22:20 | *«deploy chặn là sao em? lý do là gì cho anh hay»* | `HỎI` | giải thích: **lớp phân quyền của Claude Code** chặn, **không** phải cổng dự án; nêu ba lối chọn | `ĐÃ_LÀM` |
| 02/09 ~22:40 | *«Em tiến hành deploy 1 cách tự động cho anh, với việc backup đầy đủ dự phòng mọi rủi ro ghi mốc lịch sử thời điểm quan trọng này dùm anh. Tiếp tục xử lý các vấn đề dứt điểm cho anh trong tối nay, backup và deploy đầy đủ cho anh.»* | **`YÊU_CẦU`** | backup 4 lớp 768 MB → deploy → runtime proof → mốc lịch sử | `ĐÃ_LÀM` |

---

## 3 · ĐÀO BỚI / PHÁT HIỆN — liệt kê ĐỦ

### 3.1 🟢 MỐC LỊCH SỬ — `V11154_DEPLOY_CONTEXT_ONLY_SHADOW`

```
PID          3248913 → 3249633          start 2026-09-02 22:46:51 +07
gpt_analyzer 4fc988bd2c23d22c → f83e6f3c1eca2f08
env          PYTHONUNBUFFERED=1 → PYTHONUNBUFFERED=1 LLM_CONTEXT_ONLY_V2_LANE=shadow
health 200 · neo 558 FINAL a82c508d3569abda… KHÔNG DRIFT
4 bảng khoá: predictions 14.039 · final_bundles 561 · lottery_results 15.403
             · model_daily_eval 13.903  — KHÔNG mất dòng nào
```

**Backup bốn lớp, 768 MB** tại `backups/V11154_deploy_context_only_shadow/`:

| lớp | nội dung |
|---|---|
| ① + ② | 6 tệp mã/cấu hình có `sha256`: `gpt_analyzer` · `main` · `scheduler` · `combo_super` · `model_registry` · `lottery.service` |
| ③ | **toàn bộ DB 802 MB** sao bằng `sqlite3.backup()` — **nhất quán khi đang ghi**, khác `cp` (có thể bắt DB giữa một giao dịch và cho ra bản hỏng **câm lặng**). `254` bảng · `integrity_check = ok` · neo 558 trong **bản sao** khớp |
| ④ | `MOC_LICH_SU.json` ghi **cả trước lẫn sau** deploy |

### 3.2 🟢 BẤT BIẾN OFFICIAL — chứng minh trên chính production

Đo **dưới đúng bộ biến của tiến trình service** (`/proc/3249633/environ`):

| miền | official **trước** | official **sau** | shadow **sau** |
|---|---|---|---|
| MN | 13.609 | **13.609** | **12.290** |
| MT | 13.104 | **13.104** | **11.823** |
| MB | 12.677 | **12.677** | **11.396** |

Prompt shadow **hết** `HIỆU SUẤT THEO MODEL` và **hết** mệnh lệnh *«ưu tiên patterns từ models
`win_rate` cao»*. Official **vẫn còn cả hai**.

Định tuyến dưới môi trường service: `LANE=shadow` · `shadow→True` · `official→False`.

### 3.3 🔴 HAI LẦN DỤNG CỤ ĐO ĐỨNG SAI CHỖ — production luôn đúng

**Lần một (22:45):** bộ deploy chạy hết cổng rồi **tự gỡ về** ở bước 8 vì đọc ra `LANE=off`.
Nguyên nhân: bước đó mở một tiến trình Python **RỜI** qua SSH, mà tiến trình rời **không thừa
kế** `Environment=` của systemd. Bước POST **cùng lượt** đã cho thấy service có `LANE=shadow`.

**Lần hai (ngay sau):** phép kiểm bất biến official báo `KHÁC=False` cả ba miền — tức *«shadow
không sạch»* — **cũng vì** chạy tiến trình rời.

**Cả hai lần production đều đúng; chỉ dụng cụ đo đứng sai chỗ.** Gỡ về lần một **sạch tuyệt
đối** (`GO_VE_OK`, neo nguyên, không mất dòng nào). Cổng sai chiều **an toàn** — nó gỡ về khi
không chứng minh được — nhưng vẫn là cổng sai, và **một cổng hay báo động giả là một cổng sẽ bị
tắt**. Đã dựng `vps_service_env.py`: nạp biến từ `/proc/<PID service>/environ` rồi mới chạy.

### 3.4 Mục `B` — hai mâu thuẫn `V11154`, sửa tại đúng chỗ công bố

| mã | câu cũ | câu đúng |
|---|---|---|
| `V11154_UNIQUE_SOURCE_CLAIM_CONFLICT` | *«nguồn **duy nhất** dương cả bốn cửa sổ là `gpt-5.5`»* | **HAI** nguồn: `gpt-5.5` **và** `qwen3.7-max` |
| `V11154_SIGN_SWITCH_COUNT_TEXT_TABLE_CONFLICT` | *«**ba** nguồn dương 14 ngày, âm 180 ngày»* | **BỐN** — bỏ sót `claude-opus-5-fast` (`+3 → −5`), ca **mạnh nhất** |

Cùng một loại lỗi: **viết câu tường thuật mà không đối chiếu lại chính bảng vừa đặt**.
Cả hai **không đổi** `HOLD`.

### 3.5 Mục `C` — dụng cụ đo

**`C4` RECONCILED bằng ID dòng.** Chênh `1.600 ↔ 1.636` đúng **36 dòng**, **tất cả** thuộc
`2026-06-03` (`id 7892-7903, 7918-7919, …`), rơi ra khi cửa sổ 90 ngày trượt từ neo `09-01` sang
`09-02`. **0 dòng vào thêm. 0 dòng biến mất khỏi bảng.**

**`C1` ổ bệnh.** `_ho()` (`_materialize_shadow_promotion_scorecard.py:307-311`) đối chiếu model
với `shadow_models`/`output_models` lấy từ **registry HIỆN TẠI**. Một lượt tháng 6 của `glm-5.1`
chạy `shadow_auto_eval` bị trả `None` vì **hôm nay** nó không còn trong nhóm đó.
**Đo được: 4.160/13.013 lượt (32,0%)** trong 180 ngày bị bỏ **im lặng**.

Bản vá: vai trò suy từ **chính sự kiện** (`run_source`). Phép đối chiếu registry là **thừa chứ
không chỉ sai** — sự kiện đã tự khai vai trò của nó; hỏi lại registry chỉ thêm **một cơ hội để
trạng thái hôm nay ghi đè sự thật hôm qua**.

**`C2`+`C3` phân rã toàn lịch sử 3.296 dòng:**

| lớp | dòng | % | tính vào điểm? |
|---|---|---|---|
| `PRE_EXISTENCE_COVERAGE_GAP` | **2.352** | 71,4% | ❌ không phải model thua |
| `ROLE_AT_TIME_CLASSIFICATION_ERROR` | **877** | 26,6% | ❌ phải sửa rồi tính lại |
| `POST_CUTOFF_MISLABEL` | 0 | 0,0% | — |
| `TRUE_MISSING_OUTPUT` | **67** | 2,0% | ✅ vào phạt độ tin cậy |

⇒ **98,0% dòng `MISSING` KHÔNG được tính là thua.** Artifact trước/sau **877 dòng** có đủ
`scorecard_id` · `prediction_id` · `vai_trò_cũ → vai_trò_sửa` · `mã_lý_do` · `artifact_hash`.

**`C5` META 19/19**, gồm phép chống lookahead kiểm bằng **chữ ký hàm** — mỗi tham số ngoài
`run_source` là một cửa cho trạng thái hôm nay chảy vào phán quyết về hôm qua.

### 3.6 Mục `D` — 🟢 PHÁ ĐƯỢC CHỨNG MINH VÒNG TRÒN

Tìm ra **cổng lọc TRƯỚC** mà bản cũ bỏ sót: `main.py:9700-9707` lọc `raw_predictions` bằng
`get_output_eligible_ids()` — **registry HIỆN TẠI**. Cùng loại lookahead với `_ho()`, nhưng nằm
trên **đường sinh FINAL**.

Và registry **không có phiên bản theo thời gian**: `effective_from` = 0 · `effective_to` = 0 ·
`output_eligible_from` = 0. ⇒ Câu *«ai output-eligible ngày 04/07»* **không tra được từ
registry**. Đó chính là lý do `V11154` phải lấy pool từ `gate_diagnostics` — **không phải lười,
mà là đường duy nhất có**.

**Nguồn thay thế chính tắc, không vòng tròn: lịch sử git của `model_registry.py`** (22 bản ghi).
Git **không phải** artifact đang tái lập.

| phép | kết quả |
|---|---|
| pool tái dựng **chứa đủ** pool đã lưu | **177/181 (97,8%)** |
| top-1 khớp | **166/181 (91,7%)** |
| top-3 khớp **đúng thứ tự** | **135/181 (74,6%)** |

Bốn ca lệch (`combo-no-token` 01/08 · `random-forest` 09/08 · `xgboost` 30/08) đều rơi **đúng
ngày chuyển vai trò**.

⚠️ `RM-13` `NOT_VERIFIED`: git ghi **repo**, không ghi **VPS**. Cổng `_v11143` hôm nay báo VPS
cũ hơn, 0 tệp VPS mới hơn — nhưng đó là **hôm nay**, không chứng minh cho từng ngày quá khứ.

**`D4` trần voter** — 990 phép thử một-voter / 30 ngày:

| miền | phép thử | đổi `ranked[0]` | **bị trần đẩy ra** |
|---|---|---|---|
| MB | 330 | 18,2% | **0,0%** |
| MN | 341 | 8,2% | **0,0%** |
| MT | 319 | 19,4% | **90,0%** |

Ở MT, thêm một nguồn là **đá một nguồn khác ra** 9/10 lần. **Cấm** gọi là *«thêm shadow vào
TOTAL»* nếu thực chất là **thay một official**.

**`D3` tách ba câu hỏi:** `15,2%` đổi `ranked[0]` chỉ trả lời **một phần** câu *«có đổi TOTAL
rank không»*. **Không** đồng nghĩa tăng tỉ lệ trúng. **Không** đồng nghĩa đổi `FINAL` công bố.

### 3.7 Mục `D5` — chuỗi override: **BỐN** cái, nay còn **MỘT**

Không phải một override như `V11154` ghi, mà **bốn cái xếp chồng** giữa xếp hạng
(`main.py:10164`) và lúc chốt `bach_thu`:

| # | mã | dòng | phạm vi |
|---|---|---|---|
| 1 | `V10640` per-slice BT | `main.py:10228` | theo `OVERRIDE_CONFIG` từng miền |
| 2 | `V10767` MB prev-day ML | `main.py:10247` | MB · `_ENABLED = False` |
| 3 | `V10789` K11a MB lane | `main.py:10264` | MB |
| 4 | `V10790` K15 MT lane | `main.py:10284` | MT |

Đếm `bach_thu ≠ ranked_numbers[0]`:

| tháng | MN | MT | MB |
|---|---|---|---|
| 2026-05 | 0/31 | 0/31 | 0/31 |
| 2026-06 | 11/30 | 12/30 | 8/30 |
| 2026-07 | 10/31 | 10/31 | 17/31 |
| **2026-08** | **9/31** | **0/31** | **0/31** |
| 2026-09 | 1/2 | 0/1 | 0/1 |

| miền | tổng | lần đầu | lần CUỐI | trạng thái |
|---|---|---|---|---|
| MN | 31 | 02/06 | **02/09** | 🔴 **CÒN ĐANG CHẠY** (~1/3 số ngày) |
| MT | 22 | 01/06 | 29/07 | 🟢 đã dừng |
| MB | 25 | 03/06 | 28/07 | 🟢 đã dừng |

⇒ **`G5` chỉ phải hấp thụ MỘT override đang hoạt động**, trên **một** miền. Việc nhỏ hơn nhiều
so với tưởng. ⚠️ **Cấm xoá lịch sử**: 78 lần override là dữ liệu **thật** của những ngày đó.

### 3.8 Mục `E` — hợp đồng thống kê bản 2

Ba sửa, **cả ba làm nghiêm hơn**:

| bản 1 | sai ở đâu | bản 2 |
|---|---|---|
| *«không xấu đi có ý nghĩa»* ⇒ `PASS` | **«không bác bỏ được H₀» KHÔNG chứng minh «bằng nhau»** | khoá **biên non-inferiority δ**, chứng minh **cận trên KTC < δ** |
| một ngưỡng `\|z\| ≥ 1,96` | **360 phép** (30 model × 3 miền × 4 cửa sổ) ⇒ **~18 kết quả giả** ở `α = 0,05` | **Holm** trên **họ 3 phép** |
| McNemar cho mọi thước | thước **hạng** là **thứ tự** | **hoán vị cặp** |

**Biên khoá theo miền** (≈7% nền, **dưới 1 SE** ở mọi miền):
`MN 3,0pp` (nền 42,5%) · `MT 3,0pp` (37,8%) · `MB 1,5pp` (20,6%).

🔴 **Sự thật công bố:** tỉ lệ bất đồng đo được `0,323`; cỡ mẫu cho non-inferiority ở nhịp **một
bạch thủ/miền/ngày**:

| `δ` | ngày | **năm** |
|---|---|---|
| **2 pp** | 6.335 | **17,4** |
| 3 pp | 2.815 | 7,7 |
| 5 pp | 1.014 | 2,8 |
| 10 pp | 253 | 0,7 |

Nới tới `10pp` thì đo xong trong 8 tháng — nhưng `10pp` trên nền MB `20,6%` là **mất gần một
nửa**; gọi thế là *«không thụt lùi»* thì chữ ấy mất nghĩa.

⇒ **Đổi thủ tục quyết định, không đổi tiêu chuẩn.** *«Chỉ tiến bộ, không thụt lùi»* thi hành như
**hàng rào chặn vận hành**: chạy song song shadow ↔ official trên **cùng sự kiện** · theo dõi
hiệu tích luỹ mỗi ngày · **dừng ngay** khi bất kỳ miền nào chạm `−δ` với ≥30 cặp lệch · chỉ
trình Cutover khi **cả ba miền** giữ `≥ 0` liên tục **≥60 ngày**. Luật dừng **bất đối xứng có
chủ ý**: dừng vì xấu **nhanh**, kết luận tốt **chậm**.

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Vì sao backup toàn bộ DB dù deploy không ghi DB.** Owner nói *«dự phòng mọi rủi ro»*. 802 MB
trên 11 GB trống là cái giá rẻ để đổi lấy việc **không bao giờ phải tiếc**. Dùng
`sqlite3.backup()` chứ không `cp`: `cp` có thể bắt DB **giữa một giao dịch** và cho ra bản hỏng
**câm lặng** — loại hỏng tệ nhất vì nó chỉ lộ ra lúc cần khôi phục.

**Vì sao không ép lượt shadow chạy ngay để lấy runtime proof.** Lượt shadow chạy `05:00 · 16:00
· 17:00`; giờ VPS lúc deploy là `22:46`. Gọi tay một lượt thì **không phải bằng chứng theo
lịch** — owner `F.6` đòi *«ít nhất một lượt scheduler thật»*. Bằng chứng đó đến **~05:00 sáng
03/09**, và ép sớm là tự lừa mình.

**Vì sao chọn lịch sử git làm nguồn eligibility-tại-ngày.** Ba nguồn khả dĩ: ① registry hiện tại
— **sai** (lookahead); ② `gate_diagnostics` của artifact — **vòng tròn**; ③ git. Chỉ ③ vừa **có
thời gian** vừa **không phải thứ đang tái lập**.

---

## 5 · ĐÃ LÀM GÌ — trước / sau / phiên bản / kiểm (§60.4)

| # | việc | trước | sau | kiểm |
|---|---|---|---|---|
| A | `gpt_analyzer.py` trên VPS | `4fc988bd2c23d22c` | **`f83e6f3c1eca2f08`** | `sha256` khớp local sau `scp` |
| B | `lottery.service` | `Environment=PYTHONUNBUFFERED=1` | **`+ LLM_CONTEXT_ONLY_V2_LANE=shadow`** | `/proc/3249633/environ` = 1 |
| C | tiến trình | `PID 3248913` | **`PID 3249633`** | health 200 · active |
| D | `_v11155_vai_tro_theo_thoi_diem.py` | — | MỚI | META **19/19** |
| E | `_v11155_hoa_giai_missing.py` | — | MỚI | **RECONCILED** |
| F | `_v11155_counterfactual.py` | — | MỚI | pool **97,8%** |
| G | `_v11155_override_chain.py` | — | MỚI | **1** override còn chạy |
| H | `NGUONG_CHAP_NHAN_GRAND_OVERHAUL.md` | bản 1 | **bản 2** | commit **trước** replay |

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11154_backup.py` | ✅ `BACKUP_OK` — 4 lớp · `integrity_check = ok` · neo khớp |
| `_v11154_deploy.py --chay` | ✅ **`DEPLOY_OK · RUNTIME_PROVEN`** |
| `_v11143_cong_dong_bo.py` | ✅ VPS cũ hơn · 0 tệp VPS mới hơn |
| `_v11155_test_vai_tro.py` | ✅ **19/19** |
| `_v11150_test_contract.py` | ✅ 37/37 |
| `_v11152_test_lane.py` | ✅ 11/11 |
| `_v11062_nang_version.py --kiem` | ✅ `governance_seq 471` |
| `_v11088_cong_cua_so_chon.py` | ✅ `PRJ_WINDOW=SẠCH` |
| **neo 558 FINAL** | ✅ `a82c508d3569abda…` **KHÔNG DRIFT** |

---

## 7 · VƯỚNG VẤP

**🔴 ① Hai lần dụng cụ đo đứng sai chỗ** — mục 3.3. Kéo theo **một lần gỡ về thừa**.

**🟡 ② `\0` trong heredoc thành null byte thật** — lần thứ năm trong dự án. Đã ghi bộ nhớ dài
hạn; lần này vẫn tái phạm vì viết `tr '\0'` trong lệnh bash. Vá bằng mã bát phân `'\000'`.

**🟡 ③ Con số `877` khác `869`** của bản điều tra trước. Đây là **ranh giới phân loại**
(`869 + 8` so với `877 + 0`), không phải bất đồng dữ liệu — tổng `3.296` và hai lớp
`PRE_EXISTENCE`/`TRUE_MISSING` **trùng khít**.

**🟡 ④ `RM-13` chưa đóng** — git ghi repo, không ghi VPS cho từng ngày quá khứ.

---

## 8 · GỠ VỀ

| thành phần | gỡ về |
|---|---|
| **deploy** | `python web/backend/_v11154_deploy.py --go-ve` — **một lệnh**, tự kiểm lại health + neo |
| cấu hình | bỏ `Environment=LLM_CONTEXT_ONLY_V2_LANE` khỏi unit + `daemon-reload` + restart |
| mã | `gpt_analyzer.py.V11154.bak` trên VPS, hoặc kho backup |
| **dữ liệu** | `backups/V11154_deploy_context_only_shadow/lottery_ai.db` (802 MB, `integrity_check = ok`) |

Gỡ về **đã được chứng minh chạy được** — lần một tối nay gỡ thật, `GO_VE_OK`, neo nguyên.

---

## 9 · THEO DÕI TIẾP

| # | việc | trạng thái | chặn ở đâu |
|---|---|---|---|
| 1 | **Runtime proof theo lịch** (`F.6`) | 🔴 chờ | lượt shadow **~05:00 sáng 03/09** |
| 2 | Áp bản vá role-at-time vào materializer production | ⚪ tiếp theo | code+test xong, chưa deploy |
| 3 | **Ranked top-K adapter** (`G1`) | ⚪ tiếp theo | — |
| 4 | `ALL_MODEL_ARENA` (`G2`) | ⚪ Wave 5 | — |
| 5 | `TOTAL_V2` (`G3`) — **phải hỗ trợ THÊM DẦN**, và xử trần MT | ⚪ Wave 5 | — |
| 6 | `COMBO_V2` (`G4`) · `DOUBLE_COUNT` lineage | 🔴 `PARENT_LINEAGE_PENDING` | — |
| 7 | `FINAL_V2` (`G5`) — hấp thụ **1** override MN | ⚪ Wave 5 | nhỏ hơn tưởng |
| 8 | `RM-13` — VPS có khớp git từng ngày quá khứ không | 🟡 `NOT_VERIFIED` | — |
| 9 | **3-càng** có pipeline hợp lệ không | ⚪ `XI` | nếu không ⇒ `NO_VALID_3CANG` |
| 10 | **Cutover Packet** | ⚪ Wave 5 | 🔴 **cổng `XV.D`** |
| 11 | Bảo mật / SSH / world-writable | ⚪ `CLASS C` | **cổng `XV.B`** |
| 12 | 38/228 bản thiếu báo cáo (`FU-444` · `FU-447`) | ⚪ nợ CŨ | — |

---

## §62 — BA LỚP NGUỒN

### `OWNER_SAID`

| giờ | nguyên văn | loại |
|---|---|---|
| 02/09 ~22:40 | *«Em tiến hành deploy 1 cách tự động cho anh, với việc backup đầy đủ dự phòng mọi rủi ro ghi mốc lịch sử thời điểm quan trọng này dùm anh.»* | `YÊU_CẦU` |

### `CODE_DID` / `RUNTIME_PROVED`

- `PID 3248913 → 3249633` · `start 2026-09-02 22:46:51 +07` · `gpt_analyzer f83e6f3c1eca2f08`
- `/proc/3249633/environ` chứa `LLM_CONTEXT_ONLY_V2_LANE=shadow` — **đếm = 1**
- định tuyến dưới env service: `shadow→True` · `official→False`
- official trước = sau: `MN 13.609 · MT 13.104 · MB 12.677`
- backup 768 MB · DB 802 MB · `254` bảng · `integrity_check = ok`
- neo 558 `a82c508d3569abda47041ad625cca93fdec2227fbe389c395dc7f139893a0e5f`
- commit riêng `0de0cff` · `7dd3d03` · `0977c64` · `abd009c` · `d00f714` ·
  công khai `d8e1162`

### `DOC_SAID`

- `V11154` mục 3.1b nói *«nguồn duy nhất»* và *«ba nguồn»* ⇒ **ĐÃ SỬA** tại chỗ (`d8e1162`)
- `V11154` nói *«override V10640»* (số ít) ⇒ thực tế **bốn** override; **một** còn chạy

### `NOT_VERIFIED`

Runtime proof theo lịch (chờ 05:00 03/09) · VPS có khớp git từng ngày quá khứ không (`RM-13`) ·
`DOUBLE_COUNT` lineage của Combo/Smart · pipeline 3-càng.

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` ≠ `CODE_DID`:** `V11154` mô tả **một** override; đọc mã thì có **bốn** xếp chồng
(`main.py:10228 · 10247 · 10264 · 10284`). Đo dữ liệu thì **hai** đã tự dừng từ cuối tháng 7.
Ba tầng — tài liệu, mã, dữ liệu — cho **ba câu trả lời khác nhau**, và chỉ tầng dữ liệu nói
đúng hiện tại.

---

TanPhatAI cần làm: ghi **`V11155` — DEPLOY ĐẦU TIÊN của Grand Overhaul**, owner cho phép trực tiếp 02/09 ~22:40. Ghi **mốc `V11154_DEPLOY_CONTEXT_ONLY_SHADOW`**: `PID 3248913 → 3249633` · `22:46:51 +07` · `gpt_analyzer f83e6f3c1eca2f08` · `env + LLM_CONTEXT_ONLY_V2_LANE=shadow` · neo 558 **không drift**. Ghi **backup bốn lớp 768 MB** gồm **DB đầy đủ 802 MB** sao bằng `sqlite3.backup()`, `integrity_check = ok`. Ghi **OFFICIAL BẤT BIẾN** — prompt official trước = sau (`13.609 / 13.104 / 12.677`), shadow rụng đúng khối bảng xếp hạng. Ghi **hai lần dụng cụ đo đứng sai chỗ** (tiến trình rời không thừa kế `Environment=`) — **production luôn đúng**, gỡ về **sạch tuyệt đối**. Ghi **`D` phá được chứng minh vòng tròn** bằng **lịch sử git** của registry — pool **97,8%**; và **registry KHÔNG có `effective_from`/`effective_to`** nên eligibility-tại-ngày không tra được từ registry. Ghi **`D4` trần MT đẩy ra 90,0%** — *«thêm nguồn»* ở MT thực chất là **thay một official**. Ghi **`D5`: BỐN override xếp chồng, nay chỉ còn MỘT đang chạy (MN, ~1/3 số ngày)** — `G5` nhỏ hơn tưởng; **cấm xoá 78 lần override lịch sử**. Ghi **`E` bản 2**: biên `MN 3,0pp · MT 3,0pp · MB 1,5pp` · **Holm** trên họ 3 phép · **17,4 năm** ⇒ **guardrail vận hành**. Ghi **runtime proof theo lịch chờ ~05:00 sáng 03/09**. Ghi **official chưa đổi một ký tự**, `POOL_VERDICT = HOLD`. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
