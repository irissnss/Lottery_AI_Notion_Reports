# ĐĂNG KÝ TRƯỚC — PHÉP ĐO TIẾN CỨU PURE-CONTEXT (BẢN NHÁP)

> **Mã:** `V11165` · **Cổng:** 11 · **Lập:** 05/09/2026 ICT · **Nhãn:** `PROVISIONAL_AGENT_PROPOSED_DRAFT`
>
> 🔴 **ĐÂY LÀ BẢN NHÁP. CẤM gọi là `OWNER_LOCKED`.** Owner chưa ký một ngưỡng nào trong tệp này.
> Trần verdict của phiên: `CODED_AND_TESTED_NOT_RUNTIME_PROVEN`. Không có dòng nào trong tệp này
> cho phép deploy, restart, promote, retire, hay bật một lane nào.
>
> **Owner lock 23:14 04/09 (QD-073) vẫn nguyên hiệu lực:** `MODEL_ACTION = BLOCKED` ·
> `POOL_VERDICT = HOLD` · `OUTPUT_COUNTERFACTUAL_RANK_PRODUCTION_WRITE = FORBIDDEN` ·
> `MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK`.

---

## 0 · Neo nguồn — mọi con số dưới đây đo trên đâu

| | |
|---|---|
| clone bất biến | `/root/Lottery_AI_Test/artifacts/v11165_immutable.db` · sha256 `c3c2f568…efebb6e2` · mở `mode=ro` |
| mã đang serve | `gpt_analyzer.py` sha256 `758c29c13185763f406ab49e65c44ad2fcf610d7fb9b4c7142fa5c705de144d6` · 416.285 byte · mtime `2026-09-04T00:43:26` |
| runtime | `PID 3370750` · `NRestarts 0` |
| lane đọc | `prompt_3tang_ab_shadow_v11059` · `experiment_name = PROMPT_3TANG_TB_V1` |

**Script tái lập** (`RM-11` — mọi số dưới đây chạy lại được):

```
_k11c_tb_full.py       → artifacts/v11165_k11_c_tb_verdict.json
_k11d_vif_variants.py  → artifacts/v11165_k11_d_vif.json
_k11e_nen_thuoc.py     → artifacts/v11165_k11_e_nen.json
_k11f_nen_chuan.py     → artifacts/v11165_k11_f_nen.json
_k11g_power.py         → artifacts/v11165_k11_g_power.json
_k11h_o_nhiem.py       → artifacts/v11165_k11_h_onhiem.json
_k11i_hash_ctx.py      → artifacts/v11165_k11_i_nguon.json
tổng hợp               → artifacts/v11165_k11_prereg.json (sha256 264c76d0d367b9d2…)
```

---

# PHẦN I — ĐỌC VERDICT PHÉP ĐO T‑B ĐÃ TỒN TẠI

> Phép đo này **đã chạy đủ 25 ngày, đã đủ mẫu theo chính ngưỡng nó đăng ký, và chưa báo cáo nào
> đọc verdict.** Việc đầu tiên của cổng 11 là đọc cho trọn — **cấm làm như nó không tồn tại**.

## I.1 · Tái lập từ đầu — không trích lại báo cáo cũ

| | |
|---|---|
| cửa sổ | `2026-08-11 → 2026-09-04` (25 ngày) |
| n | **346** lượt ghép cặp · **0** lượt chưa chấm · **346/346** `trang_thai = OK` |
| miền | MN 117 · MT 114 · MB 115 |
| model | `gemini-2.5-pro` 74 · `gemini-2.5-flash` 74 · `claude-opus-4-6` 73 · `claude-sonnet-4-6` 73 · `deepseek-reasoner` 52 |

> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18 · RM-21). Phiên này đo **NỀN**
> cho thước bạch thủ, **không** tuyên bố hiệu quả, nên **14 / 30 / 90 / 180 ngày** đều để trống có
> chủ ý. Bộ đủ bốn cửa sổ nằm ở **V11084 + V11086**, và ở đó **dấu ĐỔI**: 30 ngày **+4,07pp** ·
> 90 ngày **−3,18pp** · 180 ngày **+0,91pp** (CI95 [−3,2 ; +5,0]). Trích riêng một cửa sổ để
> tuyên bố hiệu quả là chọn cửa sổ cho khớp kết quả — bản này **không** làm thế.
**Bảng 2×2 (thước: bạch thủ, ghép cặp model × miền × ngày):**

| | T‑B trúng | T‑B trượt | |
|---|---|---|---|
| **CONTROL trúng** | 65 | **51** (`b`) | 116 |
| **CONTROL trượt** | **50** (`c`) | 180 | 230 |
| | 115 | 231 | 346 |

| chỉ số | giá trị |
|---|---|
| cặp bất đồng `b+c` | **101** |
| tỉ lệ bất đồng | **29,19%** |
| WR CONTROL | **33,53%** (116/346) |
| WR T‑B | **33,24%** (115/346) |
| hiệu (T‑B − CONTROL) | **−0,289 pp** |
| McNemar `z` (không hiệu chỉnh liên tục) | **−0,0995** · `p = 0,9207` |
| McNemar `z` (có hiệu chỉnh liên tục) | **0,0** · `p = 1,0000` |

🔴 **Phát hiện về cách trình bày:** báo cáo làn sóng 1 ghi *«McNemar z = −0,10 · p = 1,00»*.
**Hai con số này đến từ HAI PHÉP KHÁC NHAU**: `z = −0,0995` là bản **không** hiệu chỉnh liên tục
(`p` tương ứng là **0,9207**); `p = 1,00` là bản **có** hiệu chỉnh liên tục (`z` tương ứng là
**0,0**). Cả hai đều tái lập được, nhưng ghép chung một dòng là **trộn hai phép**. Kết luận không
đổi (cả hai đều xa 1,96), nhưng mọi báo cáo sau **phải ghi rõ dùng đúng một phép**.

## I.2 · Tách theo miền và theo model — điều con số gộp che mất

| miền | n | `b` | `c` | bất đồng | `z` | `p` | WR CONTROL | WR T‑B |
|---|---|---|---|---|---|---|---|---|
| MN | 117 | 19 | 23 | 42 | +0,617 | 0,537 | 39,32% | 42,74% |
| MT | 114 | 20 | 20 | 40 | 0,000 | 1,000 | 38,60% | 38,60% |
| **MB** | 115 | **12** | **7** | **19** | **−1,147** | 0,251 | 22,61% | **18,26%** |

MB đi **ngược chiều** (T‑B kém CONTROL 4,35 pp) nhưng **19 cặp bất đồng < sàn 30 cặp/miền của
`V11153`** ⇒ theo đúng ngưỡng đã khoá, **không được đọc MB thành kết luận** (19 cặp ⇒ MDE = **17,6 pp**). Ghi đúng chữ:
*chưa được phép kết luận cho MB* (`RM-04`).

| model | n | WR CONTROL | WR T‑B | `b` | `c` |
|---|---|---|---|---|---|
| `claude-sonnet-4-6` | 73 | 26,03% | **36,99%** | 7 | 15 |
| `deepseek-reasoner` | 52 | 30,77% | 34,62% | 5 | 7 |
| `gemini-2.5-flash` | 74 | 33,78% | 33,78% | 12 | 12 |
| `claude-opus-4-6` | 73 | **36,99%** | 30,14% | 14 | 9 |
| `gemini-2.5-pro` | 74 | **39,19%** | 31,08% | 13 | 7 |

Chiều hiệu ứng **đảo dấu giữa các model** (sonnet +10,96 pp · gemini-pro −8,11 pp). Đây là bằng
chứng bổ sung rằng số gộp đang trung bình hoá những thứ ngược nhau — **cấm đọc số gộp một mình**.

## I.3 · 🔴 NỀN — điều chưa ai đọc, và nó đổi cách hiểu cả phép đo

> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18 · RM-21). Phiên này đo **NỀN**
> cho thước bạch thủ, **không** tuyên bố hiệu quả, nên **14 / 30 / 90 / 180 ngày** đều để trống có
> chủ ý. Bộ đủ bốn cửa sổ nằm ở **V11084 + V11086**, và ở đó **dấu ĐỔI**: 30 ngày **+4,07pp** ·
> 90 ngày **−3,18pp** · 180 ngày **+0,91pp** (CI95 [−3,2 ; +5,0]). Trích riêng một cửa sổ để
> tuyên bố hiệu quả là chọn cửa sổ cho khớp kết quả — bản này **không** làm thế.
`RM-18` bắt buộc **nền đúng cho từng vế**. Thước là **bạch thủ 1 số** ⇒ với `k = 1`, nền là
**`|hợp các đuôi ra trong ngày| / 100`** (hypergeometric với `k=1`; **cấm** dùng `1−(1−b)^k`).

Tự chấm lại từ `lottery_results` khớp **346/346 cho CẢ HAI nhánh** ⇒ cột `trúng` trong bảng đáng
tin.

| miền | số đài/ngày | **nền** | WR CONTROL | `z` vs nền | WR T‑B | `z` vs nền |
|---|---|---|---|---|---|---|
| MN | 3,12 | **43,15%** | 39,32% | −0,84 | 42,74% | −0,09 |
| MT | 2,42 | **34,52%** | 38,60% | +0,92 | 38,60% | +0,92 |
| MB | 1,00 | **23,90%** | 22,61% | −0,33 | 18,26% | −1,42 |
| **gộp** | — | **33,91%** | 33,53% | **−0,15** | 33,24% | **−0,27** |

> **CẢ HAI NHÁNH ĐỀU KHÔNG KHÁC NỀN Ở BẤT KỲ MIỀN NÀO** (`|z| < 1,96` toàn bộ).
> Nghĩa là phép đo T‑B đang so **hai nhánh đều nằm ở mức chọn ngẫu nhiên một đuôi**.

Và con số gộp *«33,24% vs 33,53%»* là **trung bình của ba nền khác nhau: 23,9% · 34,5% · 43,2%**.
Nền MN cao gần **gấp đôi** nền MB chỉ vì MN xổ 3 đài. Đọc con số gộp một mình là `RM-18` vi phạm.
**Mọi báo cáo sau phải kèm nền từng miền.**

**Phân loại:** `PROVEN_DEFECT` (lỗi ở khâu **trình bày/đọc kết quả**, không phải ở mã lane).

## I.4 · 🔴 SÀN NHIỄU — «đổi 70,2% số chọn» nghĩa là gì

Làn sóng 1 ghi: *«prompt ba tầng đổi hẳn số được chọn ở 70,2% số lượt mà tỉ lệ trúng đứng yên»*.
Tái lập: **243/346 = 70,23%** đổi bạch thủ · **312/346 = 90,17%** đổi tập số · Jaccard trung bình
**0,266**.

Câu hỏi chưa ai đặt: **70,2% là TÁC DỤNG của prompt, hay chỉ là LLM tự gieo lại xúc xắc?**

Neo đo được (`artifacts/v11165_h13_lineage.json` · `resample_trung_ket_qua` — combo-super gọi
**LẠI** chính model cha):

| | n | top‑1 **KHÁC** | top‑2 (tập) **KHÁC** |
|---|---|---|---|
| **combo-super · AI** | 910 | **61,32%** | 86,81% |
| combo-super · ML | 859 | 29,34% | 42,03% |
| smart-ensemble · ML | 1.261 | 43,62% | 46,31% |
| smart-ml · ML | 1.238 | 0,24% | 0,24% |

> Gọi **lại** cùng một model AI cho ra **top‑1 khác 61,3%** số lượt.
> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18 · RM-21). Phiên này đo **NỀN**
> cho thước bạch thủ, **không** tuyên bố hiệu quả, nên **14 / 30 / 90 / 180 ngày** đều để trống có
> chủ ý. Bộ đủ bốn cửa sổ nằm ở **V11084 + V11086**, và ở đó **dấu ĐỔI**: 30 ngày **+4,07pp** ·
> 90 ngày **−3,18pp** · 180 ngày **+0,91pp** (CI95 [−3,2 ; +5,0]). Trích riêng một cửa sổ để
> tuyên bố hiệu quả là chọn cửa sổ cho khớp kết quả — bản này **không** làm thế.
> Prompt ba tầng đổi bạch thủ **70,2%**.
> **Hai con số cùng bậc độ lớn.** Phần đổi *có thể quy cho prompt* là **nhỏ so với sàn nhiễu**.

⚠️ **Giới hạn phải khai:** đầu vào của lần gọi lại trong combo-super **chưa được chứng minh là
giống từng byte** với lần gọi gốc. Nên **61,3% là XẤP XỈ TRẦN TRÊN của sàn nhiễu, không phải sàn
nhiễu đo trực tiếp.** Đây chính là lý do phép đo mới **bắt buộc có nhánh A/A thật** (mục III.2).

**Phân loại:** `SUSPICIOUS_NEEDS_MORE_EVIDENCE`.

## I.5 · 🔴 SỨC MẠNH — con số 96 là con số 50% sức mạnh

`V11059` đăng ký 11/08 (nguyên văn trong `_v11059_lane_ab_3tang.py`):

```
điều kiện: >= 96 cặp bất đồng  VÀ  |z| >= 1,96
Cơ sở của con số 96: … Nếu prompt mới thắng 60% số cặp bất đồng thì cần
(1,96/(2·0,6−1))² = 96 cặp lệch.
```

Tái lập: `(1,96/0,2)² = 96,04` ✅ **con số 96 tái lập đúng**.

🔴 **Nhưng công thức đó KHÔNG có số hạng `z_β`.** Nó chỉ bảo đảm: *nếu `ψ` quan sát **đúng bằng**
0,60 thì `|z|` **vừa chạm** 1,96*. Đó là thiết kế **~50% sức mạnh**, không phải 80%.

| | giá trị |
|---|---|
| `m` cần cho `ψ = 0,60`, **power 80%** | **194** cặp bất đồng |
| `m` cần cho `ψ = 0,60`, power 90% | 259 cặp bất đồng |
| sức mạnh **thực tế** tại `m = 101` nếu `ψ = 0,60` | **52,0%** |
| sức mạnh thực tế tại `m = 101` nếu `ψ = 0,55` | 17,0% |
| **MDE** tại `m = 101`, power 80% | `ψ = 0,638` ⇔ **chênh lệch tuyệt đối ≈ 8,04 pp** |

> **Lane T‑B chỉ có 80% sức mạnh với hiệu ứng ≥ ~8 điểm phần trăm.**
> Hiệu ứng quan sát là **−0,29 pp**.

## I.6 · Phán quyết theo ĐÚNG ngưỡng đã đăng ký trước

| ngưỡng `V11059` (khoá 11/08, trước khi có số) | đo được | đạt? |
|---|---|---|
| `T1` ≥ 96 cặp bất đồng | **101** | ✅ |
| `T2` `\|z\|` ≥ 1,96 | **0,0995** | ❌ |
| `T3` ≥ 14 ngày | **25** | ✅ |

> **PHÁN QUYẾT:** `T1` đạt · `T3` đạt · `T2` **không** đạt ⇒ theo đúng ngưỡng đã khoá trước:
> **KHÔNG có bằng chứng T‑B khác CONTROL.**
>
> Vì `T1` **đã đạt**, đây **không** phải trường hợp `RM-04` *«chưa được phép kết luận»* —
> đây là một **kết luận NULL hợp lệ**, nhưng **chỉ trong phạm vi sức mạnh đã đạt** (mục I.5).

**Nhãn:** `NO_ANOMALY_FOUND` — trong phạm vi MDE ≈ 8 pp.

> **Hoà giải một con số dễ đọc nhầm:** bản tóm tắt làn sóng 1 ghi *«101/96 cặp bất đồng»*.
> **`96` KHÔNG phải một phép đo** — nó là **ngưỡng `T1` đăng ký trước** ở `V11059`. Đọc đúng
> là ***«đo được 101, ngưỡng cần 96»***. Ghi kiểu `101/96` khiến người đọc sau tưởng đó là hai
> lần đo khác nhau.

## I.7 · 🔴 Phép đo này KHÔNG nói lên điều gì

| không nói | vì sao |
|---|---|
| *«pure context không có tác dụng»* | **T‑B không phải pure context.** T‑B chỉ **xếp lại ba tầng** + sửa ba mâu thuẫn. Prompt T‑B trung bình **45.104** ký tự vs CONTROL **51.823** — chỉ ngắn hơn **13,0%**, và vẫn giữ rõ số đã chọn sẵn |
| *«prompt không ảnh hưởng gì»* | MDE ≈ 8 pp. Mọi hiệu ứng nhỏ hơn đều **không phát hiện được** |
| *«tái cấu trúc có tác dụng»* / *«gỡ mâu thuẫn có tác dụng»* — riêng lẻ | owner chốt bỏ nhánh `T-A`; `V11059` đã khai trước là **không tách được** |
| bất cứ điều gì về **MB** | 19 cặp bất đồng < sàn 30 |
| bất cứ điều gì về **sàn nhiễu** | thiết kế **không có** nhánh A/A |
| bất cứ điều gì về **FINAL công bố** | thước là bạch thủ **từng model**, giữa nó và bạch thủ FINAL còn tầng override |

## I.8 · 🔴 Nhánh T‑B **chưa sạch** — sáu ổ ô nhiễm còn ở CẢ HAI nhánh

Đo trên **mã đang serve** (`sha256_16 = 758c29c13185763f`), không đọc tài liệu (`RM-14`):

| vị trí | nguyên văn (rút gọn) | trạng thái |
|---|---|---|
| `gpt_analyzer.py:3191` | *«Đưa ra CHỐT HẠ rõ ràng — **ưu tiên số xuất hiện trong NHIỀU nguồn** (thống kê + ĐÀI pattern + THỨ pattern)»* | **CÒN** — nằm trong `_yc +=` **không điều kiện**, `_ctx_only` **KHÔNG gác** |
| `gpt_analyzer.py:3189` | *«**KNOWLEDGE BASE**: Sử dụng dữ liệu Deep Focus (top tails, ĐB/G8 hay ra) để **ưu tiên** số có pattern mạnh»* | **CÒN** — `_ctx_only` không gác |
| `gpt_analyzer.py:3185` | *«THAM KHẢO hiệu suất gần đây và số đã trúng…»* | **chỉ dòng này** được gác bởi `if not _ctx_only` (điều kiện ở `:3184`) |
| `REASONING_RULEBOOK:565` | *«Ưu tiên (cao→thấp): Width > **Rules > Diversity** > Recency > Caution»* | **CÒN** — xếp `Rules` trên `Diversity` = ra lệnh bầy đàn |
| `gpt_analyzer.py:5593-5594` | *«💡 **ML MẠNH HƠN AI CHO MB**: {ml_wr}% vs {ai_wr}%» → «Tham khảo ML output nếu có»* | **CÒN** |
| `gpt_analyzer.py:2472-2473` (khối Phase 15) | *«📊 **LỊCH SỬ DỰ ĐOÁN CỦA BẠN** (model=…, 7 ngày)» · «WR hiện tại (TRỰC TIẾP): …% (…/…)»* | **CÒN** |

🔴 **Điều nặng nhất ở bảng này:** `:3191` chính là **mâu thuẫn M1** mà `V11059` khai là *đã gỡ*
trong nhánh T‑B. Trong **production** nó **vẫn còn** — và **`CONTEXT_ONLY_V2` cũng không gỡ nó**.
Khối `_ctx_only` chỉ gỡ **đúng một** mệnh lệnh trong khối này (dòng `:3185`), trong khi hai mệnh
lệnh **ưu tiên số** ngay bên dưới đứng nguyên.

Bốn mục cuối vi phạm trực tiếp **mục tiêu owner số 5** (cấm dùng tên model · win rate · trọng số
để đẩy LLM bắt chước nhau) và **số 8** (điều kiện là **bằng chứng**, không phải **khuyến nghị số**).

**Phân loại:** `PROVEN_DEFECT`.

---

# PHẦN II — HOÀ GIẢI NGƯỠNG CŨ

> `V11165` cấm **tái sử dụng mù** ngưỡng của `V11059` / `V11153` / `V11161`.
> Bảng này nói: **ngưỡng nào của bản nào · đo trên thước nào · còn dùng không · vì sao.**

| bản | ngày | ngưỡng | đo trên **thước** nào | còn dùng? | vì sao |
|---|---|---|---|---|---|
| `QD-017` | 02/08 | `T1` ≥ 96 cặp bất đồng · `T2` \|z\| ≥ 1,96 · `T3` ≥ 14 ngày | bạch thủ ghép cặp (model × miền × ngày) | `T2` `T3` **CÒN** · `T1` **PHẢI SỬA** | `T1 = 96` sinh từ công thức thiếu `z_β` ⇒ ~50% sức mạnh |
| `QD-059` / `V11059` | 11/08 | y hệt trên + VIF đo lại (cụm = ngày) + **CẤM đọc sớm** | bạch thủ `numbers[0]`, ghép cặp | phần **VIF** và **cấm đọc sớm** **CÒN** · `n = 96` **PHẢI SỬA** | như trên; thêm: VIF phải ghi rõ đo cho **thước nào** (mục II.2) |
| `TOTAL_V2` tiền đăng ký | 25/08 | `T1…T8`: thêm **Holm** · `T6` nhất quán cửa sổ · `T7` **không miền nào lùi có ý nghĩa** · `T8` `M0` tái lập ≥ 99% | bạch thủ / xiên2 / xiên3 / 3 càng của **TOTAL** | `T4…T8` **CÒN và NÊN DÙNG LẠI** · `T1` kế thừa lỗi `QD-017` | `T7` trùng luật owner *«chỉ tiến, không lùi»*; `T8` là **cổng tiền đề** đúng |
| `V11153` | 02/09 | `PASS`/**`STOP`**/`HOLD` · **một miền lùi = STOP dù tổng thể dương** · \|z\| ≥ 1,96 đối xứng · **sàn 30 cặp lệch MỖI MIỀN** · out‑of‑time | McNemar cặp đôi trên nguồn shadow | **CÒN toàn bộ** | là luật owner trực tiếp |
| `V11161` | 04/09 | MT là miền sơ cấp · **McNemar CHÍNH XÁC** hai phía · đọc ở ngày **30** và **65** · ba cổng TIẾN/DỪNG/HOÃN | bạch thủ của **`TOTAL ranked[0]`** | **CÒN** nhưng là `PROVISIONAL_AGENT_PROPOSED` (chưa owner ký) · **VIF/nền của nó KHÔNG mang sang được** | `RM-21` — nó đo **thước khác** (`TOTAL ranked[0]`, không phải bạch thủ từng model) |

🔴 **Một mâu thuẫn phải xử tường minh:** `T1` = **96 cặp gộp** (QD‑017) và `V11153` = **30 cặp
mỗi miền**. Hai sàn này **không phải một**. Bản này tách rõ (mục IV.3): sàn **toàn cục** dùng để
**kết luận**, sàn **mỗi miền** chỉ dùng để **được phép đọc** một miền — **không** để kết luận nó.

## II.2 · 🔴 VIF phải đo lại cho TỪNG THƯỚC, không phải từng lane

`RM-21` nói *«hằng số đo được chỉ đúng cho thước đã đo nó»*. Đo lại **trên chính lane T‑B**, cùng
một tập 346 lượt, chỉ đổi **thước** và **cách chia cụm**:

| thước | cụm | ICC | **VIF** |
|---|---|---|---|
| **hiệu ghép cặp** (`trúng_TB − trúng_CONTROL`) | ngày | −0,0083 | **0,894** |
| hiệu ghép cặp | ngày × miền | −0,0162 | 0,941 |
| hiệu ghép cặp | ngày × model | +0,0179 | 1,032 |
| **một nhánh** (`trúng_TB`) | ngày | +0,0336 | **1,431** |
| **một nhánh** (`trúng_CONTROL`) | ngày | +0,0602 | **1,772** |

> **Cùng lane, cùng cụm (ngày):** thước **ghép cặp** cho VIF **0,894** (< 1 — vì hiệu ứng NGÀY tự
> triệt tiêu trong phép trừ), còn thước **một nhánh** cho VIF **1,43–1,77** (> 1).
> **Dùng một con số cho cả hai là `RM-21_VIOLATION`.**

**Về con số `0,867` của làn sóng 1:** **không tái lập được** dưới bất kỳ định nghĩa nào trong 7
định nghĩa cụm đã thử. Giá trị gần nhất là **0,894** (cụm = ngày, thước ghép cặp). Kết luận
**không đổi** (VIF ≈ 0,9, **không** phải 2,92), nhưng theo `RM-11` con số công bố phải **kèm định
nghĩa cụm** mới dùng được. **Từ nay dùng `0,894` và ghi rõ: *thước ghép cặp, cụm = ngày, lane
T‑B, n = 346*.**

**Cấm tái sử dụng mù:**

| hằng số | phán quyết |
|---|---|
| `VIF = 2,92` | **CẤM** — đo cho thước «16 model cùng đoán một ngày» (`RM-18`) |
| `VIF = 0,889` | **CẤM** mang sang — đo cho một thước bạch thủ ba miền **khác** |
| `VIF = 0,867` | không tái lập được ⇒ thay bằng **0,894** kèm định nghĩa cụm |
| `n = 96` | **CẤM** dùng làm sàn mới — con số 50% sức mạnh |
| ngưỡng `V11161` | **CẤM** mang sang — thước `TOTAL ranked[0]` |

---

# PHẦN III — THIẾT KẾ PHÉP ĐO MỚI

## III.1 · Vì sao cần phép đo mới (và vì sao T‑B không thay được)

| | |
|---|---|
| T‑B chỉ ngắn hơn CONTROL | **13,0%** (45.104 vs 51.823 ký tự) |
| T‑B dùng lại nguyên bốn khối production | `build_system_prompt` · `create_analysis_prompt` · `build_context_pack` · `REASONING_RULEBOOK` (docstring `_v11059_prompt_3tang.py`) |
| sáu ổ ô nhiễm (mục I.8) | có mặt trong **CẢ HAI** nhánh |
| `CONTEXT_ONLY_V2` | chỉ gác **6/171 = 3,51%** điểm bơm chuỗi; `build_context_pack` (141 điểm) gác **0**; lane gỡ 3 khối trong ~30 và **THÊM 4 khối** |

> **CHƯA AI TỪNG ĐO** một prompt thoả đủ chín điều kiện owner. Phép đo này là phép đo **đầu tiên**
> của loại đó.

## III.2 · Bốn nhánh — nhánh A/A là thứ làn sóng 1 còn thiếu

| nhánh | là gì | chi phí |
|---|---|---|
| **CONTROL** | prompt official hiện hành — **tái dùng** lượt gọi official đã có | **$0** |
| 🔴 **CONTROL′** | gọi **LẠI** prompt official, cùng ngày/model/miền, cùng provider settings — **nhánh A/A**, đo **SÀN NHIỄU** | 1 call |
| **CANDIDATE** | pure-context candidate, đạt đủ sáu cổng `K-C` (mục III.4) | 1 call |
| `SHAM` *(tuỳ chọn)* | candidate nhưng **trả lại đúng một** khối `AGGREGATED_NUMBER_SET` — tách «bỏ rõ số» khỏi «xếp lại cấu trúc» | 1 call |

> **`CONTROL′` là bắt buộc, không phải tuỳ chọn.** Không có nó thì mọi con số «đổi X% số chọn»
> đều **không đọc được** — đúng cái bẫy ở mục I.4. Nó cũng cho một phép kiểm tự thân: `CONTROL`
> vs `CONTROL′` **phải** cho `p` không có ý nghĩa; nếu nó **có** ý nghĩa thì thiết bị đo hỏng,
> **huỷ phép đo**.

## III.3 · Giữ cố định — và điều cấm

**Giữ cố định:** cùng model · cùng miền · cùng ngày · cùng cutoff · cùng raw facts · cùng provider
settings (`temperature` · `top_p` · `max_tokens` · `seed` nếu có).

**CẤM:** thay **model** và **prompt** cùng lúc.

**Cổng nhân quả:**
1. chỉ chạy khi miền target **CHƯA XỔ**;
2. `created_at` ghi **có offset**, kiểm **0 dòng tạo SAU khi kết quả về**;
3. **PHA 1** sinh lựa chọn + **băm sha256**, **PHA 2** mới nối kết quả (chống oracle).

**Hợp đồng shadow (không nới một điều nào):** bảng riêng · `shadow_only=1` · `diagnostic_only=1` ·
`output_eligible=0` · `owner_approved=0` · **không đụng** `predictions` · `final_bundles` ·
`lottery_results` · `model_daily_eval` · băm 4 bảng khoá trước/sau.

**Ghi vết bắt buộc mỗi dòng:** sha256 payload **đầy đủ** từng nhánh *(vân tay hiện hành chỉ phủ
**43,59%** — phải dùng bản vá `_v11165_van_tay_payload`)* · số ký tự từng nhánh · `prompt_version`
+ regime + cờ ngữ cảnh · **số đài xổ trong ngày** (để tính nền) · latency · trạng thái parse · số
token nếu đo được.

## III.4 · Định nghĩa CANDIDATE và sáu cổng phải qua TRƯỚC khi đếm ngày

`PURE CONTEXT = raw facts + neutral conditions + reasoning/output contract`

**PHẢI CÓ:** `RAW_NUMBER_FACT` (số trong kết quả lịch sử/sự kiện nguồn thật, kèm **ngày · miền ·
đài · giải · bộ · cutoff**) · `CONDITION` trung tính (phạm vi · đầu vào · phép biến đổi · cutoff ·
**nền** · cỡ mẫu · độ bất định · trạng thái bằng chứng) · hợp đồng lập luận/output.

**PHẢI KHÔNG CÓ:** `AGGREGATED_NUMBER_SET` *(làn sóng 1: **27/35** producer đang bơm loại này)* ·
tên model · win rate · trọng số · `TOTAL` · `FINAL` · mệnh lệnh **ưu tiên một số cụ thể** ·
mệnh lệnh *«tự truy vấn»* khi **không có tool** *(làn sóng 1 [L6]: **0 dòng** tool calling trên
toàn `web/backend`)* · mệnh lệnh/nhãn/ví dụ trỏ vào khối dữ liệu **không còn**.

| cổng | nội dung |
|---|---|
| `K-C1` | **dump prompt từ HÀM ĐANG SERVE** (`RM-14`) — đọc tài liệu **không tính** |
| `K-C2` | **0** lần xuất hiện: `weight=` · `Best MB model` · `AI token models 14d WR` · `ĐỀ XUẤT PYTHON` · `SỐ NÊN TRÁNH` · `TOP 5 GỢI Ý` · `GAN CAO` · `HOT` · `OVERDUE` |
| `K-C3` | **0** mệnh lệnh ưu tiên số cụ thể — danh sách chuỗi **đăng ký TRƯỚC**, phân loại theo `RM-09` (`TRONG_PROMPT` · `GHI_VÀO_PROMPT` **phải xử**; `CHÚ_THÍCH` **giữ**) |
| `K-C4` | mỗi `CONDITION` phải có **schema nguồn truy được**; không truy được ⇒ **bị loại khỏi prompt** (mục tiêu owner **7**) |
| `K-C5` | **0** mệnh lệnh trỏ vào khối đã gỡ (`PRJ_PROMPT_DANGLING`) |
| `K-C6` | **0** cặp câu trong cùng prompt bảo ngược nhau (`PRJ_PROMPT_CONTRADICTS`) |

> **Một cổng `K-C` không đạt ⇒ nhánh đó KHÔNG được gọi là CANDIDATE, và KHÔNG được bắt đầu đếm
> ngày.** Đây chính là chỗ `V11001` đã ngã: gỡ 8 khối, báo xong, hôm sau còn 10 chỗ dạy model dùng
> đúng thứ vừa gỡ — và 14 ngày đo trôi trên một thay đổi làm nửa vời (`§60.1`).

---

# PHẦN IV — ĐĂNG KÝ TRƯỚC: CHỈ SỐ · NGƯỠNG · NGÀY ĐỌC

> Ba nhóm. **Nhóm A và B được đọc sớm** (không liên quan kết quả xổ). **Nhóm C tuyệt đối không.**

## IV.1 · Nhóm A — OPERATIONAL *(đọc sớm: ĐƯỢC)*

| mã | chỉ số | ngưỡng huỷ |
|---|---|---|
| `O1` | output validity — % lượt trả JSON đúng schema | **< 95%** ở bất kỳ nhánh nào ⇒ huỷ nhánh đó |
| `O2` | empty rate | **> 5%** |
| `O3` | parse failure | **> 5%** |
| `O4` | latency (trung vị · p95) | không ngưỡng — **chỉ báo cáo** (`chi phí RỜI khỏi bộ chọn`, `V11153`) |
| `O5` | ký tự prompt · token nếu đo được | không ngưỡng — báo cáo |
| `O6` | **contamination** — số lần xuất hiện chuỗi cấm `K-C2` trên **dump thật** | **> 0** ở `CANDIDATE` ⇒ **HUỶ** và làm lại nền |
| `O7` | prompt coverage — % payload thật được vân tay phủ | **< 99%** ⇒ **KHÔNG được bắt đầu đếm ngày** |

## IV.2 · Nhóm B — REASONING *(đọc sớm: ĐƯỢC)*

| mã | chỉ số |
|---|---|
| `R1` | valid condition refs — % trích dẫn trỏ đúng một `CONDITION` **có thật** trong prompt |
| `R2` | unsupported claims — số mệnh đề số học/thống kê **không** truy được về `CONDITION`/`RAW_FACT` |
| `R3` | contradiction — số lần lập luận **tự mâu thuẫn** trong cùng câu trả lời |
| `R4` | arithmetic — % phép tính trong lập luận **kiểm lại đúng** |
| `R5` | diversity/Jaccard — giữa các nhánh, **và** giữa các model trong cùng nhánh (đo bầy đàn) |

> `R1…R4` chấm bằng **bộ chấm đăng ký TRƯỚC** (rule-based, commit trước ngày bắt đầu). Nếu chấm
> bằng **LLM-judge** thì **phải khai là LLM-judge** và báo **tỉ lệ đồng thuận giữa hai lần chấm**.

## IV.3 · Nhóm C — PREDICTIVE *(đọc sớm: 🔴 CẤM TUYỆT ĐỐI)*

**Sơ cấp:** thước **bạch thủ (số đầu tiên)** — giữ y `V11059` để so sánh được ·
phép **McNemar CHÍNH XÁC (nhị thức), hai phía** — **không** dùng xấp xỉ chuẩn ·
ghép cặp **(model × miền × ngày)**.

**Thứ cấp:**

| mã | thước | nền / phép |
|---|---|---|
| `P2` | lô 2 / bộ `k` số | nền = **`1 − C(100−D, k)/C(100, k)`** (hypergeometric). **CẤM** `1−(1−b)^k` khi rút không hoàn lại |
| `P3` | hạng của ứng viên trúng đầu tiên | **paired permutation test** trên hạng (ordinal) |
| `P4` | top‑3 / top‑5 coverage | **chỉ** nếu hợp đồng output cho phép `k` số; nền phải dùng **đúng set size** |
| `P5` | `lợi_thế(k)` | dùng **independent source count**, **không** đếm voter thô *(làn sóng 1 [L10]: 268/567 bundle mang nhãn cao hơn sự thật)* |

**Nền bắt buộc:** **mỗi miền một nền riêng**, tính từ **số đài xổ thực tế của ngày đó**.
**CẤM gộp ba miền vào một nền** — đó đúng là lỗi ở mục I.3.

**Hiệu chỉnh đa so sánh:** **Holm**, họ phép = *(số nhánh so sánh) × (số thước sơ cấp)*.
Phiên bản hoá: `HOLM_V11165_R1` — **ghi vào artifact trước ngày bắt đầu**. Báo **cả** `p` thô
**và** `p` đã hiệu chỉnh.

**VIF:** công bố **cả ba** con số (ghép cặp · một nhánh · `VIF = 1,0`).
**Số CHÍNH dùng `VIF = 1,0`** — bảo thủ, để không tự thưởng mình.

**🔴 NGÀY ĐỌC CỐ ĐỊNH:** chỉ được đọc vào **ngày thứ 30** và **ngày thứ 65** kể từ ngày bắt đầu.
Đọc ngoài hai mốc đó là **p‑hacking**. Hai mốc này cố định **từ bây giờ**.

## IV.4 · Sức mạnh — bao nhiêu ngày cho hiệu ứng bao nhiêu

Tiền đề đo được: **tỉ lệ cặp bất đồng = 29,19%** (từ 346 lượt T‑B — ước lượng tốt nhất hiện có).
`α = 0,05` hai phía · `power = 80%` · `VIF = 1,0` (bảo thủ):

| hiệu ứng | `ψ` | **cặp bất đồng cần** | **lượt ghép cặp cần** | **ngày** (15 lượt/ngày) |
|---|---|---|---|---|
| +2 pp | 0,534 | 1.670 | 5.720 | **381** |
| +3 pp | 0,551 | 741 | 2.538 | **169** |
| +4 pp | 0,569 | 416 | 1.424 | **95** |
| **+5 pp** | 0,586 | **265** | **908** | **61** |
| +7 pp | 0,620 | 134 | 459 | **31** |
| +10 pp | 0,671 | 64 | 221 | **15** |

> **Nói thẳng:** với 15 lượt/ngày, phép đo 80% sức mạnh cho **5 pp** cần **~61 ngày**; cho **3 pp**
> cần **~169 ngày**. Muốn kết luận trong **một tháng** thì hiệu ứng phải **≥ ~7 pp**.
> Đó là **thực tế toán học**, không phải một lựa chọn.

⚠️ `CANDIDATE` khác `T-B` nhiều hơn ⇒ tỉ lệ bất đồng **có thể cao hơn** ⇒ `n` cần **sẽ giảm**.
Phải **đo lại và báo cáo** sau 14 ngày đầu — nhưng **CẤM sửa ngưỡng**.

## IV.5 · Sàn đề xuất — thay cho `T1 = 96`

| sàn | giá trị | vai trò |
|---|---|---|
| `S1` cặp bất đồng **toàn cục** | **265** | ngưỡng để **KẾT LUẬN** (delta 5 pp · power 80% · `VIF = 1,0`) — thay `T1 = 96` |
| `S2` cặp bất đồng **mỗi miền** | **30** (giữ `V11153`) | ngưỡng để **ĐƯỢC PHÉP ĐỌC** một miền — **không** phải để kết luận nó (30 cặp ⇒ MDE = **14,4 pp**) |
| `S3` số ngày tối thiểu | **30** | |
| `S4` ngày đọc | **30** và **65** | |

---

# PHẦN V — CỔNG QUYẾT ĐỊNH · ĐIỀU KIỆN HUỶ · GIỚI HẠN

## V.1 · Ba cổng — khoá trước, cấm sửa sau khi thấy số

**Nguyên tắc owner: CHỈ TIẾN, KHÔNG LÙI — một miền lùi có ý nghĩa = `STOP` dù tổng thể dương.**

| cổng | điều kiện | hành động |
|---|---|---|
| **TIẾN** | cặp bất đồng toàn cục **≥ 265** **VÀ** \|z\| ≥ 1,96 theo chiều `CANDIDATE` thắng **VÀ** không miền nào có `(b−c) < 0` với \|z\| ≥ 1,96 **VÀ** dấu `(b−c)` **không đổi chiều** giữa mốc 30 và mốc 65 | trình **Cutover Packet** cho owner — **TUYỆT ĐỐI KHÔNG tự bật** |
| **DỪNG** | bất kỳ miền nào có `CANDIDATE` **thua** có ý nghĩa (\|z\| ≥ 1,96 chiều phá, cặp bất đồng miền ≥ 30) | **STOP ngay**, tắt lane, báo owner **trong phiên** |
| **HOÃN** | không cổng nào đạt | **HOLD** — chạy tiếp đến mốc đọc kế |
| **CHƯA ĐỦ MẪU** | cặp bất đồng < 265 tại mốc 65 | ghi đúng chữ ***«chưa được phép kết luận»*** (`RM-04`) — **CẤM** ghi *«không khác biệt»* |

> Mọi cổng chỉ dẫn tới **một packet trình owner**. **Không cổng nào tự động bật/tắt production.**

## V.2 · Điều kiện huỷ phép đo

1. `O6` contamination **> 0** ở `CANDIDATE` ⇒ huỷ, làm lại nền
2. `O7` prompt coverage **< 99%** ⇒ **không được bắt đầu**
3. phát hiện thêm **một đường rò prompt** (như `gpt_analyzer.py:6738` — rõ shadow ctx vào official) ⇒ huỷ, làm lại nền
4. **đổi mã sinh prompt** của bất kỳ nhánh nào giữa chừng ⇒ huỷ, bắt đầu lại từ 0
5. `CONTROL` **không khớp official 100%** ⇒ huỷ (nhánh đối chứng không còn là official)
6. **> 0** dòng tạo **SAU** khi kết quả về ⇒ huỷ cửa sổ đó
7. `CONTROL` vs `CONTROL′` cho `p` **có ý nghĩa** ⇒ thiết bị đo hỏng ⇒ huỷ
8. `runtime_prompt_contam_hits > 0` ở lượt khai `CANDIDATE` ⇒ huỷ (regime tự mâu thuẫn)

## V.3 · Phép đo này KHÔNG trả lời gì

- **Không** trả lời *«model nào tốt nhất»* — đó là leaderboard, một câu hỏi khác.
> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18 · RM-21). Phiên này đo **NỀN**
> cho thước bạch thủ, **không** tuyên bố hiệu quả, nên **14 / 30 / 90 / 180 ngày** đều để trống có
> chủ ý. Bộ đủ bốn cửa sổ nằm ở **V11084 + V11086**, và ở đó **dấu ĐỔI**: 30 ngày **+4,07pp** ·
> 90 ngày **−3,18pp** · 180 ngày **+0,91pp** (CI95 [−3,2 ; +5,0]). Trích riêng một cửa sổ để
> tuyên bố hiệu quả là chọn cửa sổ cho khớp kết quả — bản này **không** làm thế.
- **Không** trả lời *«FINAL công bố có đổi không»* — giữa bạch thủ từng model và bạch thủ FINAL còn tầng override.
- **Không** cho phép promote/retire model nào — `POOL_VERDICT` giữ **`HOLD`** (owner lock 23:14 04/09).
- **Không** dùng lịch sử làm căn cứ tiến cứu — lịch sử là `DIAGNOSTIC ONLY`.
- **Không** chứng minh *«pure context tốt hơn»* nếu kết quả null — chỉ chứng minh *«không phát hiện hiệu ứng ≥ MDE»* (mục tiêu owner **9**: cấm hứa hit rate từ thiết kế prompt).

## V.4 · Ngày 04/09 và ngày bắt đầu

Ngày **04/09** chỉ là **observational/pilot**. **KHÔNG** dùng làm confirmatory start,
**KHÔNG** dùng để sửa threshold. Replay lịch sử chỉ dùng cho **unit test / screening** — không
promotion, không cutover, không chọn biến dựa vào kết quả rồi gọi là prospective.

> **Ngày bắt đầu tiến cứu = ngày đầu tiên SAU khi cả sáu cổng `K-C1…K-C6` đạt VÀ `O7 ≥ 99%`.**
> Ngày đó phải được **ghi vào artifact TRƯỚC khi chạy lượt đầu**.

---

# PHẦN VI — NGUỒN BA LỚP (§62)

## `OWNER_SAID`

| giờ | nguyên văn | nguồn |
|---|---|---|
| 10/08 | *«Sao không thiết kế prompt 2-3 tầng chuẩn ngữ cảnh để đo song song đi cho tiết kiệm thời gian, lúc nào cũng đòi cắt, prompt chuẩn đâu mà đòi AI tốt hơn ML em? Chưa cân xứng chưa trung thực luôn đó em»* | `_v11059_prompt_3tang.py` docstring |
| 11/08 | *«chạy shadow ngay đi không chờ đợi gì cả, nhưng phải thật kỹ càng tỉ mỉ cẩn trọng cấm cẩu thả, tự diễn, tự chế mọi thứ phải có cơ sở và phương pháp đầy đủ»* | `_v11059_lane_ab_3tang.py` docstring |
| 11/08 | *«T-B là đủ rồi em»* | `_v11059_lane_ab_3tang.py` docstring |
| 04/09 23:14 | `MATERIALIZATION_OPTION = B` · `MODEL_ACTION = BLOCKED` · `POOL_VERDICT = HOLD` · `MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK` | `QD-073` |

*(Chín mục tiêu «thuần ngữ cảnh» được dẫn lại trong prompt phiên này; bản này không diễn giải lại
chúng mà ánh xạ thẳng thành cổng `K-C1…K-C6` ở mục III.4.)*

## `CODE_DID`

| việc | bằng chứng |
|---|---|
| lane T‑B đã chạy đủ và đã chấm xong | `prompt_3tang_ab_shadow_v11059` — 346 dòng, 346/346 `OK`, 0 chưa chấm, `11/08 → 04/09` |
| tự chấm lại từ `lottery_results` khớp | **346/346** cả hai nhánh (`_k11f_nen_chuan.py`) |
| `T1` đạt, `T2` không đạt | 101 cặp bất đồng · `z = −0,0995` |
| nền chưa từng được đọc | tính lần đầu ở bản này: MN 43,15% · MT 34,52% · MB 23,90% |
| sáu ổ ô nhiễm còn trong mã đang serve | `gpt_analyzer.py` sha256 `758c29c1…44d6` · `:3189` `:3191` `:5593-5594` · `:2472-2473` · `REASONING_RULEBOOK:565` |
| `_ctx_only` chỉ gác **một** mệnh lệnh trong khối `_yc` | `gpt_analyzer.py:3185` là dòng duy nhất dưới `if not _ctx_only` (`:3184`) |
| VIF phụ thuộc **thước** | ghép cặp **0,894** vs một nhánh **1,431 / 1,772** — cùng lane, cùng cụm |

## `DOC_SAID`

| tài liệu | ghi gì | lệch không |
|---|---|---|
| `_v11059_lane_ab_3tang.py` (ngưỡng khoá 11/08) | `≥ 96` cặp bất đồng · `\|z\| ≥ 1,96` | ✅ tái lập đúng · 🔴 **nhưng 96 là con số 50% sức mạnh** — tài liệu **không** nói điều này |
| `_v11059_prompt_3tang.py` | *«M1 đã gỡ»* trong nhánh T‑B | 🔴 `DOC_SAID ≠ CODE_DID` cho **production**: `:3191` **vẫn còn**, và `CONTEXT_ONLY_V2` **không** gỡ nó |
| `docs/TOTAL_V2_TIEN_DANG_KY_20260825.md` | nền bạch thủ MN/MT phải dùng **hypergeometric**, cấm `1−(1−b)^k` | ✅ bản này tuân thủ (`k=1` ⇒ `D/100`) |
| `docs/CURRENT_TRUTH_SSOT.md §V11153` | *«một miền lùi = STOP»* · sàn **30 cặp/miền** | ✅ giữ nguyên · 🔴 **mâu thuẫn với `T1 = 96` gộp** — bản này tách vai trò hai sàn ở mục IV.5 |
| `docs/DANG_KY_TRUOC_MT_SHADOW_V11161.md` | McNemar **chính xác** · đọc ngày 30/65 | ✅ kế thừa · 🔴 nhưng đo **thước khác** ⇒ VIF/nền **không** mang sang (`RM-21`) |
| báo cáo làn sóng 1 | *«z = −0,10 · p = 1,00»* · *«VIF = 0,867»* · *«KTC95 [−5,49; +4,90]»* | 🔴 trộn hai phép · 🔴 `0,867` không tái lập (dùng **0,894**) · 🔴 KTC tái lập ra **[−5,68; +5,10]** — **kết luận không đổi** |

---

## VII · Chữ ký

| | |
|---|---|
| người đề xuất | agent (Claude Code) |
| trạng thái | **`PROVISIONAL_AGENT_PROPOSED_DRAFT`** |
| owner duyệt | ☐ **chưa** |
| ngày khoá | — |
| trần verdict phiên | `CODED_AND_TESTED_NOT_RUNTIME_PROVEN` |

Khi owner duyệt: đổi nhãn thành `OWNER_LOCKED`, ghi ngày, và **từ đó cấm sửa mọi ngưỡng**.

---

**TanPhatAI cần làm:** cập nhật `docs/FOLLOW_UP_TRACKER.md` với ba việc treo — ① **rút lại** ba
con số của làn sóng 1 theo `PRJ-RETRACTION-001` (*«z=−0,10 · p=1,00»* trộn hai phép · `VIF 0,867`
không tái lập ⇒ **0,894** · `KTC95` đúng là **[−5,68; +5,10]**); ② ghi verdict lane
`prompt_3tang_ab_shadow_v11059` là **`NO_ANOMALY_FOUND` trong phạm vi MDE ≈ 8 pp**, kèm câu cấm
đọc thành *«pure context không có tác dụng»*; ③ theo dõi sáu ổ ô nhiễm ở mục I.8 còn trong
`gpt_analyzer.py` sha256 `758c29c1…44d6` (đặc biệt `:3191` mà `CONTEXT_ONLY_V2` **không** gỡ) —
**chưa vá, chưa deploy, chờ owner**. Phiên này **không** có code đi trước tài liệu: không sửa một
tệp production nào, chỉ đọc clone bất biến và ghi artifact trong `artifacts/`.
