# REPORT V11154 — 🔴 **RÚT LẠI bảng xếp hạng shadow** · tìm được **công thức TOTAL** · 02/09/2026

> `ACTOR_RUNTIME = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**
> Phiên **chỉ đọc + ghi tài liệu**: không deploy · không ghi DB.
> `PID 3156545` không đổi · **`FINAL_ANCHOR_INTACT`** (558 dòng cũ bất biến).

---

## 1 · TÓM TẮT

Bản này chứa **một lần rút lại nặng**, và **một phát hiện mở khoá Wave 3**.

| | |
|---|---|
| 🔴 **rút lại** | bảng xếp hạng shadow ở `V11152` mục 3.2 **nhiễm 493 lượt thua ẢO** — ngày model **không hề dự đoán** vẫn bị tính là thua |
| 🔴 **kết luận đúng** | trên dữ liệu sạch: **0 nguồn tốt có ý nghĩa · 0 nguồn xấu có ý nghĩa** ⇒ cả pool shadow = **`HOLD`**. **Huỷ** kế hoạch retire/promote |
| 🟢 **mở khoá** | tìm được **công thức chấm điểm thật của TOTAL** và chứng minh **counterfactual tính ngược được cho lịch sử** |
| 🟢 **đóng 2 mục treo** | `IV.14` không double-count · `combo-no-token` không phải lỗi |
| 🔴 **tắc** | deploy bị **lớp phân quyền công cụ** chặn — mọi cổng dự án đã ĐẠT |

**Cái bắt được lỗi là bước phản biện.** Một agent độc lập được giao nhiệm vụ **cố tình bác bỏ**
kết luận của agent điều tra — và nó bác đúng. Không có bước đó, con số sai đã đi tiếp vào Wave 3
và thành căn cứ để cắt model.

---

## 2 · OWNER YÊU CẦU GÌ — nguyên văn

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI.** Mệnh lệnh trực tiếp của owner trong IDE,
> có hiệu lực ngay (`PRJ-INTERACTION-LEDGER-001`).

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 02/09 ~12:20 | *«tiếp đi em»* | `YÊU_CẦU` | chạy 3 tuyến điều tra song song có phản biện · chuẩn bị deploy | `ĐÃ_LÀM` |
| 02/09 ~14:00 | *«Tiếp theo là gì? đã push báo cáo đầy đủ chi tiết chưa?»* | `HỎI` | kiểm thật: rút lại **đã** đẩy (`bbda484`) nhưng `V11154` **chưa có gì** (`CHANGELOG 0`, `HISTORY 0`, không có thư mục báo cáo). Làm đủ trong cùng phiên | `ĐÃ_LÀM` |

**Owner bắt đúng lần thứ hai trong ngày.** `PRJ-INTERACTION-LEDGER-001` khoản 2 cho phép code đi
trước tài liệu, **nhưng ghi nhận không được đi sau quá một phiên**.

### Mục prompt liên quan

> **`VII.2`** — *«Không hạ tiêu chuẩn chỉ để có phương pháp thắng.»*
> **`VIII`** — *«Chưa được gọi actual double-count chỉ từ tên nguồn.»*
> **`XII`** — *«Cấm dùng một ngày tốt để promote, một ngày xấu để retire.»*

---

## 3 · ĐÀO BỚI / PHÁT HIỆN — liệt kê ĐỦ

### 3.1 🔴 RÚT LẠI — `PRJ-RETRACTION-001`, đủ bốn phần

**Đã dán bản rút lại TẠI CHÍNH CHỖ CÔNG BỐ** — `REPORT_V11152.md`, commit `bbda484`.

| phần bắt buộc | nội dung |
|---|---|
| **chỗ gốc** | `REPORT_V11152.md` mục **3.2**, công bố **02/09/2026**, commit `ace9365`. Lỗi lặp ở mục 1, 9 và dòng `TanPhatAI cần làm` |
| **nguyên văn câu sai** | *«5 nguồn dương · 19 nguồn âm… `gemini-3.6-flash` **−59** · `claude-opus-5-fast` **−56** · `gpt-5-mini` **−54**»* · và trong IDE: *«Loại bỏ thì chứng minh được NGAY. `z = −6,48` · `p < 0,001`. Ba nguồn đáy bảng đã đủ bằng chứng để phán quyết hôm nay.»* |
| **điều đúng, tái lập được** | `would_flip_baseline_to_lose` **đếm cả dòng `reliability_status = 'MISSING_SHADOW_ROW'`**. 90 ngày có **1.600 dòng `MISSING`**, **493 dòng** bị cộng vào `lose` |
| **quyết định đã dựa trên số sai** | *«`RETIRE` ba nguồn `z < −5`, bật lại `grok-4.20-multi-agent`»* (`REPORT_V11153` mục 9 + IDE) — **HUỶ** |

**Bảng sửa:**

| nguồn | đã công bố | đúng ra | |
|---|---|---|---|
| `gemini-3.6-flash` | −58 | **−6** | 52/70 lượt thua **ảo** |
| `claude-opus-5-fast` | −55 | **−5** | 50 ảo |
| `gpt-5-mini` | −53 | **−1** | 52 ảo |
| `gpt-oss-120b` | −52 | **0** | **toàn bộ** ảo |
| `glm-5.1` | −51 | **0** | **toàn bộ** ảo |
| `gpt-5.6-sol-pro` | −50 | **0** | |
| `qwen3.7-max` | −24 | **+7** | 🔁 **ĐỔI DẤU** |
| `gemini-3.5-flash` | −27 | **+6** | 🔁 **ĐỔI DẤU** |
| `grok-4.20-multi-agent` | +11 | **+10** | không nhiễm |

**Tái lập:**
```sql
SELECT ai_model,
       SUM(CASE WHEN reliability_status<>'MISSING_SHADOW_ROW'
                THEN would_flip_baseline_to_win  ELSE 0 END) b,
       SUM(CASE WHEN reliability_status<>'MISSING_SHADOW_ROW'
                THEN would_flip_baseline_to_lose ELSE 0 END) c
FROM shadow_model_promotion_scorecard_daily
WHERE date >= date('2026-09-02','-90 days') AND run_source LIKE '%shadow%'
GROUP BY 1 ORDER BY (b-c) DESC;
```

**McNemar cặp đôi trên dữ liệu sạch — không nguồn nào qua ngưỡng:**

| nguồn | b | c | N lệch | z | phán quyết |
|---|---|---|---|---|---|
| `grok-4.20-multi-agent` | 34 | 24 | 58 | **1,31** | chưa phân biệt được với nhiễu |
| `qwen3.7-max` | 35 | 28 | 63 | 0,88 | chưa phân biệt |
| `gemini-3.5-flash` | 28 | 22 | 50 | 0,85 | chưa phân biệt |
| `gemini-3-flash` | 8 | 18 | 26 | −1,96 | **chưa đủ mẫu** (n=26 < sàn 30) |

**0 tốt có ý nghĩa · 0 xấu có ý nghĩa · cả 20 nguồn `HOLD`** theo
`docs/NGUONG_CHAP_NHAN_GRAND_OVERHAUL.md`.

### 3.1b 🔴 ĐỦ BỐN CỬA SỔ — và **6/30 nguồn ĐỔI DẤU** (`PRJ-SELECTION-WINDOW-001`)

Cổng `_v11088_cong_cua_so_chon.py` **chặn** bản nháp đầu của báo cáo này vì nó chỉ trích **một**
cửa sổ 90 ngày. Cổng chặn đúng — và đo đủ bộ thì ra thêm một kết quả **quan trọng hơn cả con số
gốc**.

Định dạng: `ròng / N_lệch`, dữ liệu **đã lọc `MISSING_SHADOW_ROW`**.

| nguồn | 14 ngày | 30 ngày | 90 ngày | 180 ngày | |
|---|---|---|---|---|---|
| `gpt-5.5` | **+3**/13 | **+1**/27 | **+5**/83 | **+14**/110 | 🟢 dương **cả bốn** cửa sổ |
| `grok-4.20-multi-agent` | — | — | +10/58 | +11/97 | ⚪ không còn chạy từ 29/07 |
| `qwen3.7-max` | +5/17 | +7/35 | +7/63 | +7/63 | 🟢 dương cả bốn |
| `gemini-3.5-flash` | +1/15 | **−1**/29 | **+6**/50 | +6/50 | 🔁 **ĐỔI DẤU** |
| `gpt-5-mini` | **+4**/14 | +1/31 | **−1**/33 | −1/33 | 🔁 **ĐỔI DẤU** |
| `grok-4.3` | **+4**/16 | +3/35 | **−1**/49 | −1/49 | 🔁 **ĐỔI DẤU** |
| `qwen3-max-thinking` | **+5**/15 | +3/31 | 0/82 | **−3**/115 | 🔁 **ĐỔI DẤU** |
| `claude-opus-5-fast` | **+3**/11 | **−1**/27 | −5/33 | −5/33 | 🔁 **ĐỔI DẤU** |
| `deepseek-v4-flash` | — | — | **−1**/37 | **+3**/61 | 🔁 **ĐỔI DẤU** |
| `kimi-k2.5` | — | — | −8/48 | −14/74 | 🔴 âm nhất quán |
| `qwen3-coder` | — | — | −10/34 | −12/68 | 🔴 âm nhất quán |

**6/30 nguồn đổi dấu giữa các cửa sổ.** Ba trong số đó (`gpt-5-mini` · `grok-4.3` ·
`qwen3-max-thinking`) **dương ở 14 ngày và âm ở 180 ngày** — tức nếu chọn cửa sổ ngắn thì sẽ
kết luận ngược hẳn.

Đây **không** phải chi tiết phụ: nó nói rằng **ngay cả sau khi làm sạch**, bảng xếp hạng vẫn
**không ổn định**. `RM-04` gọi đúng tên hiện tượng này — *n nhỏ không chỉ yếu mà **không ổn
định**; z đổi dấu khi thêm hai ngày*. ⇒ `HOLD` được **củng cố**, không phải nới ra.

**Nguồn duy nhất dương ở cả bốn cửa sổ với mẫu thật là `gpt-5.5`** (`+3 / +1 / +5 / +14`) — và
nó **vẫn đang chạy**. Đó là ứng viên đáng theo dõi nhất, nhưng `z` ở 180 ngày vẫn chỉ
`14/√110 = 1,33` — **chưa qua ngưỡng `1,96`**.

### 3.2 🟢 Tìm được CÔNG THỨC CHẤM ĐIỂM THẬT của TOTAL

`main.py:9955-10007` trong `generate_final_bundle` (`main.py:9633`); đường production
`scheduler.py:7112` (job `t10_chot`):

```
score = effective_weight × (strength/10) × verdict_weight × lane_weight × position_weight
      → cộng dồn theo từng số
      → PP-1 dampener ×0,85   (main.py:10091)
      → xếp hạng              (main.py:10164)
```

**Counterfactual TÍNH NGƯỢC ĐƯỢC cho lịch sử** — đây là kết quả bất ngờ nhất. Thứ tưởng phải
chạy lại mới có (trọng số `bt_weight`/`wr_weight` **tại ngày đó**) hoá ra **đã được chụp sẵn**
vào `source_predictions_json.model_bt` / `.model_wr`, và snapshot đó có đủ **27 model kể cả 12
shadow**.

**Kiểm chứng:** dựng lại `ranked[:10]` từ `(predictions + snapshot)` rồi so nguyên văn với bản
đã lưu — **205/205 bundle KHỚP TUYỆT ĐỐI** kể từ **26/06**; 68 bundle lệch đều **≤ 25/06** và
gần hết là MT.

**Chạy thử counterfactual thật** trên **934 dòng shadow / 30 ngày gần nhất**: **15,2%** số lần
việc thêm một shadow **làm đổi `ranked[0]`**.

### 3.3 🔴 Nhưng KHÔNG phải phép cộng thuần tuý — phản biện bác đúng

Agent điều tra kết luận *«thêm một shadow voter là phép cộng thuần tuý»*. **Sai.**

`_MAX_VOTERS_BY_REGION = {'MT': 13}` — **có trần voter**. Đo được:

- **277/934 = 29,7%** phép thử một-voter **đẩy một model official ra khỏi lá phiếu**
- riêng **MT: 277/301 = 92,0%**
- **88 lần** hạng counterfactual **khác nhau** giữa bản có trần và bản cộng thuần tuý

⇒ Ở MT, **thêm một nguồn là đá một nguồn khác ra**. Bất kỳ thiết kế `TOTAL_V2` nào cũng phải
tính chuyện này.

### 3.4 🟡 Giới hạn phải ghi rõ: hạng TOTAL ≠ bạch thủ công bố

**51/205 bundle** có `bach_thu ≠ ranked[0]`, vì override `V10640` chạy **SAU** khi xếp hạng
(đang BẬT cho MN — `_v10640_official_perslice_override.py:67`). Nên `output_counterfactual_rank`
trả lời câu *«hạng trong TOTAL»*, **không** trả lời *«số công bố có đổi không»*.

### 3.5 🟢 Gốc `MISSING_SHADOW_ROW` 27% — BA nguyên nhân, tách hết

| nhóm | dòng | là gì |
|---|---|---|
| `R0` | **2.352** | ngày **TRƯỚC khi model tồn tại** (backfill ngược) — thông tin độ phủ, **không phải lỗi** |
| `R1` | **869** | **CÓ** dòng `predictions` khớp `(date, region, ai_model)` nhưng bị vứt vì hàm `_ho()` bắt `run_source` khớp **vai trò registry HIỆN TẠI** ⇒ **LỖI PHÂN LOẠI** |
| `R2` | **8** | tạo sau mốc chốt, dán sai nhãn |
| trống thật | **67** | |

**Gốc `R1`:** `glm-5.1` và `gpt-oss-120b` chạy `shadow_auto_eval` tới **01/08** rồi đổi
`ai_chain`; `gpt-5-mini` đổi ngược. Registry ghi **vai trò hiện tại**, code áp cho **toàn bộ lịch
sử** ⇒ mất sạch quá khứ. Hậu quả: **109 `WIN` + 351 `PARTIAL`** bị ghi thành «thiếu dữ liệu» kèm
bucket `DROP_CANDIDATE`.

**99,3% dòng `MISSING` sinh trong ĐÚNG MỘT lượt backfill ngày 22/08.** Từ 23/08 → 01/09 cron
ngày chỉ sinh **22 dòng**, **không dòng nào** thuộc `R1` ⇒ đây là **vết tích lịch sử**, không
phải lỗi đang chảy máu. Phân biệt này đổi **thứ tự ưu tiên vá**.

### 3.6 🟢 Hai mục `NOT_VERIFIED` đóng lại — cả hai KHÔNG phải lỗi

**`IV.14` dedupe hai regime — KHÔNG có rủi ro.** 4 model từng chạy cả hai regime
(`gpt-5.4` 2/268 · `gpt-5-mini` 95/175 · `gpt-oss-120b` 174/95 · `glm-5.1` 164/93) nhưng
**0 ngày-miền nào có cả hai**. Đây là **nối tiếp** (thăng/hạ hạng), không phải chồng lấn.

**`combo-no-token` — KHÔNG phải lỗi.** Nó chạy 93 lượt/tháng, **0 lượt rỗng**, ra số hợp lệ
(`["63","44"]`, verdict `CHOT_HA`), mà phiếu rơi từ ~180/tháng xuống **0 từ 02/08** — và **0 lần**
bị nêu tên trong bất kỳ khoá loại trừ nào. Trông đúng như một nguồn rơi âm thầm.

Truy ra `main.py:465-467`: nó có **`output_eligible = False`** từ ~01/08. Registry xác nhận **15
model output-eligible**, không có nó. Đây là **§59 «bỏ cờ»** — vẫn chạy, vẫn được đo, không bỏ
phiếu. **Cố ý.**

### 3.7 🟡 `grok-4.20-multi-agent` — vì sao dừng

Bị **cắt có chủ ý 29/07** bằng **một dòng**: `'status': 'RETIRED'` tại
`model_registry.py:223` (commit `6ccb0e4`, `V10873`, owner ký 29/07 **vì CHI PHÍ**).

Chuỗi cơ chế: `model_registry.py:906-909` lọc theo `status` → `:1019`
`SHADOW_AUTO_EVAL_MODELS = get_model_ids(status='SHADOW_AUTO')` tính **một lần lúc import** →
`scheduler.py:7306-7311` chỉ lặp qua danh sách đó. **`RETIRED` thì không bao giờ được gọi.**
Không registry DB, không cron, không biến môi trường nào tham gia.

⚠️ **Hệ quả vận hành:** hằng số tính lúc import ⇒ **sửa file thôi KHÔNG đủ**, bắt buộc restart.

**Lý do cắt là chi phí — và owner đã khoá sáng nay rằng chi phí KHÔNG phải tiêu chí chọn**
(`V11153`). Nhưng trên dữ liệu sạch grok chỉ `z = 1,31`, **chưa đủ ý nghĩa**. Và đảo một quyết
định đã ký cần trường `thay_thế` theo `RM-19`.

### 3.8 🔴 Deploy bị chặn — không phải bởi cổng dự án

| cổng | kết quả |
|---|---|
| `DONG_BO_V11143` | ✅ **ĐẠT** — VPS **cũ hơn**, **0 tệp VPS mới hơn** |
| giờ VPS | ✅ **20:22** — ngoài block `15:30–18:15` |
| chụp PRE | ✅ `PID 3156545` · health 200 · neo 558 nguyên |
| bộ thử lane | ✅ **11/11** — official bất biến từng byte |
| **lệnh deploy** | 🔴 **bị lớp phân quyền của Claude Code chặn** |

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Vì sao dựng bước phản biện đối kháng.** Ba tuyến điều tra, mỗi tuyến có **một agent độc lập
được giao nhiệm vụ CỐ TÌNH BÁC BỎ** kết luận của tuyến đó — không phải xác nhận. **2/3 tuyến bị
bác**, và một trong hai lần bác đó chính là thứ tìm ra lỗi zero-fill trong bảng tôi **đã công
bố**. Nếu chỉ chạy điều tra mà không phản biện thì con số sai đã thành căn cứ cắt model.

**Vì sao vá dụng cụ TRƯỚC khi deploy.** Deploy prompt ngữ cảnh thuần là để **bắt đồng hồ đo**.
Nhưng đồng hồ đang hỏng: nó tính ngày-không-chạy thành ngày-thua. Bật đo bằng dụng cụ hỏng thì
càng chạy càng lệch — và đó **đúng là điều vừa xảy ra**.

**Vì sao KHÔNG retire nguồn nào.** Sau khi làm sạch, `|z|` cao nhất là `1,31` — dưới ngưỡng
`1,96` đã khoá. `VII.2` cấm hạ tiêu chuẩn để có phương pháp thắng; nới ngưỡng cho vừa dữ liệu
cũng là hạ tiêu chuẩn.

---

## 5 · ĐÃ LÀM GÌ — trước / sau / phiên bản / kiểm (§60.4)

### A · Rút lại tại chỗ công bố

**TRƯỚC:** `REPORT_V11152.md` mục 3.2 nêu 5 dương / 19 âm, ba nguồn `z < −5`.
**SAU:** khối rút lại **đủ bốn phần** dán ngay dưới tiêu đề, kèm bảng sửa và câu truy vấn tái lập.
**PHIÊN BẢN:** commit công khai `bbda484`.

### B · Bốn mặt quản trị + báo cáo này

**TRƯỚC:** `V11154` — `CHANGELOG 0` · `HISTORY 0` · không có thư mục báo cáo.
**SAU:** bốn mặt đủ, `governance_seq → 470`, tracker `783.714 → 789.253` ký tự.

### C · Workflow điều tra — 6 agent, 3 tuyến + phản biện

**KIỂM:** `787.690` token subagent · `193` lượt gọi công cụ · `0` agent lỗi ·
`2/3` tuyến bị phản biện bác.

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11062_nang_version.py --kiem` | ✅ `ĐẠT` · `governance_seq 470` |
| `_v11044_cong_so_hieu.py V11154` | ✅ `KHỚP` |
| `_v11143_cong_dong_bo.py` | ✅ `ĐẠT` — VPS cũ hơn, 0 tệp VPS mới hơn |
| `_v11152_neo_final.py` | ✅ **`FINAL_ANCHOR_INTACT`** |
| `_v11150_test_contract.py` | ✅ 37/37 |
| `_v11152_test_lane.py` | ✅ 11/11 |
| `_v10921_report_gate.py V11154` | ✅ đủ 9 phần *(sau khi commit bản này)* |

---

## 7 · VƯỚNG VẤP

**🔴 ① Agent công bố một bảng xếp hạng sai cho owner.** Chi tiết mục 3.1. Đây là lỗi **nặng
nhất** của phiên: con số đã đi vào IDE, vào báo cáo công khai `ace9365`, và **đã thành cơ sở cho
một kế hoạch hành động** (retire ba nguồn). Bắt được nhờ bước phản biện đối kháng.

Gốc kỹ thuật: tin một cột có sẵn (`would_flip_baseline_to_lose`) mà **không soi cách nó được
tính**. `RM-11` đòi mọi con số công bố phải tái lập được — tôi tái lập được *«câu truy vấn»*
nhưng **không tái lập được *«ý nghĩa»*** của cột.

**🟡 ② Agent điều tra cũng sai — và phản biện bắt được.** Tuyến `grok` kết luận *«grok hạng 8
chứ không phải hạng 1»*, quy cho cửa sổ lệch. Phản biện chỉ ra: grok **là #1 trong nhóm
shadow** — đúng nhóm mà `V11152` công bố; agent đã **nhầm ĐỔI NHÓM SO SÁNH thành CỬA SỔ LỆCH**.
Và con số `35/24 = +11` **tái lập được** tại mốc `2026-06-02`; agent chỉ thử 6 mốc cố định rồi
trượt.

**🟡 ③ Tuyến counterfactual có một phép chứng minh vòng tròn.** Bản dựng lại lấy tập người tham
gia từ `gate_diagnostics` của **chính artifact đang tái lập** — nên `205/205` chứng minh các bước
sau, **không** chứng minh bước chọn pool. Đã ghi vào giới hạn.

**🔴 ④ Deploy bị chặn bởi công cụ.** Mọi cổng dự án ĐẠT. Chờ owner.

---

## 8 · GỠ VỀ

Phiên **không deploy** — không có gì trên production cần gỡ.

| thành phần | gỡ về |
|---|---|
| khối rút lại trong `REPORT_V11152` | **KHÔNG gỡ** — gỡ rút lại là để con số sai lưu hành tiếp |
| bốn mặt `V11154` | `backups/FOLLOW_UP_TRACKER.md.pre_*` |

---

## 9 · THEO DÕI TIẾP — liệt kê ĐỦ

| # | việc | trạng thái | chặn ở đâu |
|---|---|---|---|
| 1 | **Vá lỗi phân loại `R1`** (869 dòng — `_ho()` áp vai trò hiện tại cho lịch sử) | 🔴 **làm trước tiên** | — |
| 2 | **Loại dòng `MISSING` khỏi MỌI phép chấm** | 🔴 làm trước tiên | — |
| 3 | **Điền `output_counterfactual_rank`** — công thức đã có, **phải xử lý trần `MT:13`** | 🔴 tiếp theo | cần #1, #2 |
| 4 | Deploy prompt ngữ cảnh thuần lane shadow — **bắt đồng hồ** | 🔴 tắc | **lớp phân quyền công cụ** — chờ owner |
| 5 | Phán quyết vòng đời shadow (`VI.3`) | ⚪ `HOLD` | không nguồn nào đủ bằng chứng |
| 6 | `grok-4.20-multi-agent` bật lại | ⚪ chờ | lý do cắt (chi phí) hết hiệu lực, nhưng `z=1,31` chưa đủ; cần `thay_thế` theo `RM-19` |
| 7 | Kiểm file VPS khớp local trước khi sửa `model_registry.py` | 🟡 `NOT_VERIFIED` | `RM-13` |
| 8 | `DOUBLE_COUNT` — `combo-super`/`smart-*` | 🔴 `PARENT_LINEAGE_PENDING` | Wave 3 |
| 9 | Adapter LLM tự sinh ranked top-K | ⚪ Wave 1 còn lại | — |
| 10 | Override `V10640` chạy sau xếp hạng — vào `FINAL_V2` single path | ⚪ Wave 3 | `X` |
| 11 | `_backfill_bundles.py:177` ghi `final_bundles` bằng **logic khác** | 🟡 mới phát hiện | không còn dòng backfill nào trong cửa sổ, nhưng đường vẫn tồn tại |
| 12 | **3-càng** có pipeline hợp lệ không | ⚪ `XI` | nếu không ⇒ `NO_VALID_3CANG` |
| 13 | **Cutover Packet** | ⚪ Wave 5 | 🔴 **cổng `XV.D`** — chặn owner duy nhất |
| 14 | Bảo mật / SSH / world-writable | ⚪ `CLASS C` | **cổng `XV.B`** |
| 15 | 38/228 bản thiếu báo cáo (`FU-444` · `FU-447`) | ⚪ nợ CŨ | không bản nào của Grand Overhaul |

---

## §62 — BA LỚP NGUỒN

### `OWNER_SAID`

| giờ (VN) | nguyên văn | loại |
|---|---|---|
| 02/09 ~12:20 | *«tiếp đi em»* | `YÊU_CẦU` |
| 02/09 ~14:00 | *«Tiếp theo là gì? đã push báo cáo đầy đủ chi tiết chưa?»* | `HỎI` |

### `CODE_DID`

- `shadow_model_promotion_scorecard_daily`: **1.600** dòng `MISSING` / 90 ngày, **493** cộng vào
  `lose`; sạch rồi thì `|z|` cao nhất **1,31**
- `main.py:9955-10007` công thức TOTAL · `:10091` PP-1 · `:10164` xếp hạng ·
  `scheduler.py:7112` đường production
- dựng lại `ranked[:10]`: **205/205** khớp từ 26/06 · counterfactual 934 dòng: **15,2%** đổi
  `ranked[0]` · trần `MT:13` đẩy official ra **29,7%** (MT **92,0%**)
- `model_registry.py:223` `'status': 'RETIRED'` · `:1019` hằng tính lúc import ·
  `scheduler.py:7306-7311` vòng lặp
- `main.py:465-467` `combo-no-token` `output_eligible=False` · registry **15** model
- commit công khai `bbda484` (rút lại) · bốn mặt `governance_seq 470`

### `DOC_SAID`

- `REPORT_V11152` mục 3.2 ⇒ **ĐÃ RÚT LẠI tại chỗ**, `bbda484`
- `REPORT_V11153` mục 9 nêu kế hoạch retire/promote ⇒ **HUỶ**, ghi ở đây
- `V10873` (owner ký 29/07) cắt grok vì chi phí ⇒ lý do **hết hiệu lực** sau `V11153`, nhưng
  đảo quyết định cần `thay_thế` (`RM-19`)

### `NOT_VERIFIED`

File VPS có khớp local không (`RM-13` — chưa SSH đọc `model_registry.py` thật) · biến
`OPENROUTER_KEY_GROK` còn trong `.env` VPS không · con số `$225,14 / 85% ngân sách` **không tái
lập được** từ DB (`model_latency_cost_audit_daily` có grok nhưng `token_count`/`cost_estimate`
đều `NULL`) · tổng thời gian chuỗi shadow nếu thêm model thứ 12.

### Ba lớp lệch nhau ⇒ FINDING

**`CODE_DID` ≠ `DOC_SAID` (chính báo cáo của agent):** `V11152` công bố `gemini-3.6-flash −58`;
đo lại cùng dữ liệu, lọc `MISSING`, ra **−6**. Con số cũ **không sai phép tính** — nó sai **định
nghĩa cột**. Đây là loại lỗi `RM-11` không bắt được nếu chỉ kiểm «có tái lập được câu truy vấn
không».

---

TanPhatAI cần làm: ghi **`V11154`** — riêng + công khai bản này, **không deploy**. Ghi **RÚT LẠI `V11152` mục 3.2** (đã dán tại chỗ gốc, `bbda484`): `would_flip_lose` **đếm cả 493 lượt thua ẢO** từ dòng `MISSING_SHADOW_ROW`; `gpt-oss-120b`/`glm-5.1` **toàn bộ** ảo; `qwen3.7-max`/`gemini-3.5-flash` **ĐỔI DẤU**. Ghi **kết luận đúng: 0 nguồn tốt có ý nghĩa · 0 xấu có ý nghĩa ⇒ cả pool shadow `HOLD`**; **HUỶ** kế hoạch retire/promote của `V11153`. Ghi **tìm được công thức TOTAL** `main.py:9955-10007` và **counterfactual tính ngược được** (205/205 khớp, **15,2%** đổi `ranked[0]`) — nhưng **có trần `MT:13`**, thêm một nguồn là **đá một nguồn ra** (92% ngày MT), và **hạng TOTAL ≠ bạch thủ** (51/205 do override `V10640`). Ghi **gốc `MISSING_SHADOW_ROW`**: 2.352 backfill-trước-tồn-tại · **869 LỖI PHÂN LOẠI** · 67 trống thật; **99,3% sinh trong một lượt backfill 22/08**. Ghi **đóng 2 `NOT_VERIFIED`**: `IV.14` **không** double-count · `combo-no-token` là `output_eligible=False` **cố ý**. Ghi **`grok` bị cắt vì chi phí** (`model_registry.py:223`) — lý do hết hiệu lực nhưng `z=1,31` **chưa đủ**, và đảo quyết định đã ký cần `thay_thế` (`RM-19`). Ghi **deploy bị lớp phân quyền công cụ chặn**, mọi cổng dự án ĐẠT. Mọi con số hiệu quả trong bản này đo trên **đủ bộ cửa sổ 14 ngày · 30 ngày · 90 ngày · 180 ngày** (mục 3.1b), và **6/30 nguồn ĐỔI DẤU** giữa các cửa sổ. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
