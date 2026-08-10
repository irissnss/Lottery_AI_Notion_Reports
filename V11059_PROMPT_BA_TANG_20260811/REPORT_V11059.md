# REPORT V11059 — PROMPT BA TẦNG (T-B) CHẠY SHADOW NGAY · ĐO SONG SONG GHÉP CẶP

**Ngày:** 2026-08-11 rạng sáng · **Quyết định owner:** `QD-059` · **Mã đọc:** `PB1108`
**Production:** PID `1345720` → **`1353489`** · health 200 · **hash 4 bảng khoá PRE = POST y hệt**

---

## 1. Tóm tắt

Owner bắt đúng một sai lầm **phương pháp**, không phải sai số:

> *«prompt chuẩn đâu mà đòi AI tốt hơn ML em? **Chưa cân xứng chưa trung thực** luôn đó em»*

Agent đem **cụm AI đang chạy một prompt tự mâu thuẫn** ra so với ML, kết luận *«AI không hơn»*,
rồi dùng chính kết luận đó để **đề xuất cắt roster**. **Đã rút lại đề xuất cắt.**

Và câu *«đo song song»* của owner **giải luôn bài toán thời gian** mà agent đã gọi là «vật lý»:

| | thiết kế cũ | ghép cặp song song |
|---|---|---|
| đơn vị so | miền-ngày | **(model × miền × ngày)** |
| nhiễu còn lại | ngày + model + prompt | **chỉ prompt** |
| ⇒ thời gian | **7,6 tháng** | **~16 ngày** |

**Không phải vật lý — là thiết kế đo dở.**

Đã dựng và **deploy chạy shadow**: prompt ba tầng T-B, lane A/B 5 model × 3 miền = **15 cặp/ngày**,
cron **06:00 / 16:52 / 17:45**, đủ hạ tầng §52, **không đụng prompt official**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Sao không thiết kế prompt 2-3 tầng chuẩn ngữ cảnh để đo song song đi cho tiết kiệm thời gian,
> lúc nào cũng đòi cắt, prompt chuẩn đâu mà đòi AI tốt hơn ML em? Chưa cân xứng chưa trung thực
> luôn đó em»* — 10/08

> *«chạy showdow ngay đi không chờ đợi gì cả, nhưng phải thật kỹ càng tỉ mỉ cẩn trọng cấm cẩu
> thả, tự diễn, tự chế mọi thứ phải có cơ sở và phương pháp đầy đủ nha em»* — 11/08

> *«T-B là đủ rồi em»* — 11/08

---

## 3. Đào bới / phát hiện

### 3.1 · BƯỚC 1 (RM-14) — DUMP PROMPT THẬT từ hàm đang phục vụ

*«Cấm tự chế»* nghĩa là bước đầu tiên bắt buộc phải là **dump production**, không đọc tài liệu.
RM-14 ghi rõ: prompt thật từng đo **46.583** ký tự trong khi báo cáo ghi **15.617**.

| khối | ký tự | hàm nguồn |
|---|---|---|
| `system_prompt` | 7.760 | `build_system_prompt(rules)` |
| `analysis_body` | 16.126 | `create_analysis_prompt(...)` |
| `context_pack` (sau de-herding) | 10.567 | `build_context_pack(...)` + `_deherd_strip_ranking` |
| `REASONING_RULEBOOK` | 15.465 | hằng số |
| **TỔNG CONTROL** | **49.839** | |

`source_regions = "MN_D1,MT_D1,MB_D1"` — **xác nhận chỉ có D-1**, khớp phát hiện `RR §9` (V11056).

**Agent tự bắt một lỗi ngay ở bước này:** bản dump đầu gọi `build_context_pack()` **trực tiếp**,
nhưng đường phục vụ còn **gỡ de-herding SAU đó** (`gpt_analyzer.py:6329`). Nên bản dump đầu
**không phải bản gửi đi thật** — đúng lỗi RM-14 mà agent vừa trích. Đã đo lại đúng.

### 3.2 · BA MÂU THUẪN — bằng chứng nguyên văn, không suy diễn

**M1 · Prompt tự nói ngược nhau về «nhiều nguồn»**

| vị trí | nguyên văn |
|---|---|
| `system_prompt:69` | *«Đếm số nguồn chỉ để BẠN THAM KHẢO độ dày bằng chứng — **KHÔNG có điểm thưởng**.»* |
| `system_prompt:73` | *«số có **3 nguồn**: trúng **26,5%** · nền 33,4% · **z = −2,54** ← THẤP NHẤT»* |
| `system_prompt:77` | *«**đừng cộng điểm cho số chỉ vì nó xuất hiện ở nhiều nguồn**»* |
| **`analysis_body:355`** | *«8. Đưa ra CHỐT HẠ rõ ràng — **ưu tiên số xuất hiện trong NHIỀU nguồn** (thống kê + ĐÀI pattern + THỨ pattern…)»* |

Cùng một lượt gửi: câu trên cấm, câu dưới bắt làm. Câu bắt làm nằm **dòng 355/358** — vị trí cuối,
chỗ mô hình bám mạnh nhất.

**M2 · `§8` xếp `Rules > Diversity` — tức RA LỆNH BẦY ĐÀN**

```
rulebook §8:44   Ưu tiên (cao→thấp): Width > Rules > Diversity > Recency > Caution
rulebook §23:243 MỤC TIÊU: Portfolio đa dạng — ít nhất 2-3/7 AI models nên chọn SỐ KHÁC
```

`§22`/`§23` chống bầy đàn rất kỹ. Nhưng `§8` **có thứ tự ưu tiên rõ ràng** và nó xếp **Rules trên
Diversity**, mà **Rule Tails giống hệt nhau cho cả 16 model**. Model tuân `§8` sẽ bám Rule Tails
và bỏ `§23`.

**Khớp đúng số đã đo:** đồng thuận từng cặp cụm **AI 0,2929** vs **ML 0,1519**, **z = +3,10** —
kết quả **duy nhất** vượt ngưỡng thống kê trong cả chuỗi phiên. **Không phải model tự bầy đàn —
prompt bảo nó làm thế.**

**M3 · De-herding làm nửa chừng**

`_deherd_strip_ranking` chạy **đúng** trên context pack — đo được: gỡ **1.133 ký tự**, cả 4 khoá
(`Model Performance` · `BT MODEL RANKING` · `Width Warning` · `Riêng`) về **0**.

Nhưng nó **không chạm thân phân tích**, nên còn nguyên:

```
analysis_body:304  → AI nên ưu tiên patterns từ models có win_rate cao hơn.
analysis_body:121  WR hiện tại (TRỰC TIẾP): 14% (1/7) (+5 partial)
analysis_body:130  ⚠️ LƯU Ý: Nếu WR thấp (<50%), hãy thay đổi chiến lược!
```

`:304` là **đúng cơ chế** V10768 sinh ra để gỡ. `:121`/`:130` dạy đổi chiến lược theo **WR n=7** —
tức dạy đuổi nhiễu (RM-04: n nhỏ **không ổn định**, z đổi dấu khi thêm 2 ngày).

### 3.3 · HAI CHỖ AGENT TỰ ĐÍNH CHÍNH

- **`§5g` KHÔNG còn là luật cộng điểm.** Đọc nguyên văn `:69-79`: nó **đã được sửa rồi**, ghi
  thẳng *«KHÔNG có điểm thưởng»* kèm cả số đo `z=−2,54`. Agent từng ngụ ý nó còn là vấn đề.
- **Mâu thuẫn «`§4` vs `§11/§18`» từng nêu là NÓI QUÁ.** `§4` nói về đồng thuận **model**;
  `§11/§18` nói về **Rule Tails** — hai đối tượng khác nhau, có thể cùng tồn tại. Mâu thuẫn thật
  nằm ở `§8`, và chỉ tìm ra sau khi đọc hết `§8` (`Conflict Resolution`).

---

## 4. Hướng xử lý và vì sao

### 4.1 · Ba tầng — chỉ XẾP LẠI, không thêm một câu tri thức nào

| tầng | ký tự | nội dung | nguồn |
|---|---|---|---|
| **T1 · DỮ LIỆU** | 25.604 | chỉ sự kiện, **không mệnh lệnh** | thân `:1-342` + context pack |
| **T2 · LUẬT** | 11.226 | phương pháp suy luận | rulebook `§1–§21` |
| **T3 · RÀNG BUỘC** | 6.280 | bắt phân tích, cấm suy diễn | rulebook `§22–§26` + YÊU CẦU |

**`§22`/`§23` được dời lên T3 có chủ ý.** Để chúng lẫn trong T2 cùng `§8` thì ngoại lệ chống bầy
đàn vừa thêm sẽ **bị chính `§8` gốc nuốt lại**.

### 4.2 · MỘT LỖI THIẾT KẾ THÍ NGHIỆM AGENT TỰ BẮT

Bản đầu gửi `system=""` + `user=tất cả`, trong khi CONTROL gửi `system=system_prompt` +
`user=thân`. Thế là hai nhánh khác nhau **cả VAI TRÒ THÔNG ĐIỆP**, không chỉ nội dung — và **mất
tính một-biến**. Mô hình xử lý `system` khác `user`, nên chênh lệch đo được sẽ lẫn tác dụng của
việc **dời khối**, không phải của prompt ba tầng.

**Đã sửa:** `system_prompt` **giữ nguyên vai trò `system` ở CẢ HAI nhánh**.

| | system | user |
|---|---|---|
| CONTROL | 7.760 | 42.079 |
| T-B | **7.760 (y hệt)** | 43.114 |

⇒ chênh **+1.035 ký tự (+2,5%)** ở **đúng một chỗ**: nội dung user.

### 4.3 · Vì sao ghép cặp nhanh hơn 14 lần

Hai nhánh chạy **cùng model, cùng ngày, cùng dữ liệu nguồn** ⇒ hiệu ứng **NGÀY** và hiệu ứng
**MODEL tự triệt tiêu**, chỉ còn nhiễu của chính prompt. Đó là toàn bộ lý do — không phải máy khoẻ hơn.

### 4.4 · NGƯỠNG ĐĂNG KÝ TRƯỚC — chốt 11/08, cấm đổi sau khi thấy số

```
thước    : bạch thủ T-B vs CONTROL, ghép cặp theo (model, miền, ngày)
phép     : McNemar trên cặp BẤT ĐỒNG
điều kiện: >= 96 cặp bất đồng  VÀ  |z| >= 1,96
VIF      : đo lại cho CHÍNH thước này (RM-21)
đọc sớm  : CẤM
```

Cơ sở của **96**: dữ liệu thật `PROMPT_V2_AB_V1` (79 cặp, 05/07→01/08) cho **40,5% cặp bất đồng**;
nếu prompt mới thắng 60% cặp lệch thì cần `(1,96/(2·0,6−1))² = 96`.

### 4.5 · GIỚI HẠN — khai trước, không giấu

Owner chốt **bỏ nhánh T-A** (tái cấu trúc thuần). Nghĩa là:

> **Nếu T-B thắng, KHÔNG tách được phần nào do TÁI CẤU TRÚC ba tầng, phần nào do GỠ BA MÂU
> THUẪN.** Đánh đổi có chủ ý để rẻ và nhanh.

---

## 5. Đã làm gì (deploy)

| # | việc | bằng chứng |
|---|---|---|
| 1 | `_v11059_prompt_3tang.py` — ghép ba tầng từ **chính bốn khối production** | ba phép gỡ có **dấu nhận diện riêng**, **ném lỗi** nếu không tìm thấy chuỗi đích |
| 2 | `_v11059_lane_ab_3tang.py` — lane A/B 5 model × 3 miền | định tuyến **5/5 đủ khoá**, dry-run **15/15 DRY_OK** |
| 3 | Cron **06:00 MN · 16:52 MT · 17:45 MB** | crontab 136 → **139** dòng, **0** dấu `\&` hỏng |
| 4 | API `/api/admin/prompt-3tang-ab` + panel `/monitoring` | `require_admin` + `no-store`, đăng ký **cả** `loadAllSections` **lẫn** `setInterval` |
| 5 | Cổng chung `BO_DO` nay soi **BA** phép đo | thử chặn RM-15 **soi từng phép riêng** |

**Deploy:** PID `1345720` → **`1353489`** · health 200 · `/du-doan` 200 · API 401 · **0** lỗi ·
**hash 4 bảng khoá PRE = POST y hệt**.

---

## 6. Cổng kiểm — xác minh

| cổng | kết quả |
|---|---|
| `--soi-dinh-tuyen` | **5/5** model đủ khoá (deepseek · gemini×2 · anthropic×2) |
| `--dry-run --date 2026-08-10` | **15/15 DRY_OK**, control khớp đúng dự đoán official hôm đó |
| kiểm chéo ba phép gỡ | 3 câu mệnh lệnh cũ **biến mất**, ngoại lệ mới **có mặt** |
| `_v11055_kiem_p4.py --thu-chan` | **P4 6/6 · B1 6/6 · B2 6/6** + thử chặn **từng phép riêng** |
| hash 4 bảng khoá | **PRE = POST y hệt** |
| sổ quyết định | về **2 phép trôi**, cả hai là **hiệu ứng đổi ngày**, không do phiên này |

**Cổng nhân quả kiểm HAI LẦN.** Giờ trong DB là **UTC** — đọc thẳng lệch 7 tiếng. Quy về giờ VN:
MN official **05:15** → kết quả **16:35** · MT **16:36** → **17:30** · MB **17:31** → **18:30**.
Cửa sổ MT/MB chỉ **~35 phút**, mà 5 model × 120s có thể mất 10 phút ⇒ kiểm lại **ngay trước khi
ghi**; nếu kết quả về giữa chừng thì **bỏ cặp**, không ghi.

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **10/08** | *«prompt chuẩn đâu mà đòi AI tốt hơn ML em? Chưa cân xứng chưa trung thực luôn đó em»* |
| **11/08** | *«chạy showdow ngay đi không chờ đợi gì cả, nhưng phải thật kỹ càng tỉ mỉ cẩn trọng cấm cẩu thả, tự diễn, tự chế»* |
| **11/08** | *«T-B là đủ rồi em»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| prompt official thật **49.839 ký tự**, chỉ nguồn **D-1** | dump từ hàm phục vụ, `source_regions="MN_D1,MT_D1,MB_D1"` |
| `analysis_body:355` **ra lệnh** ưu tiên số nhiều nguồn | ngược `system_prompt:69/73/77` cùng prompt |
| `rulebook §8:44` xếp **`Rules > Diversity`** | `§23:243` đòi 2-3/7 model chọn số khác — bị `§8` đè |
| de-herding gỡ **1.133 ký tự** ở pack, **0** ở thân | `analysis_body:304/121/130` còn nguyên |
| lane mới **không sửa** `gpt_analyzer`/`main` đường official | tự ghép prompt riêng, giống cách `_v10781` đã được duyệt |

### `DOC_SAID`

| tài liệu ghi gì | file:mục | lệch? |
|---|---|---|
| `RM-14`: *«prompt thật ≠ prompt lý thuyết»* | `CLAUDE.md §61` | **khớp** — và agent vẫn suýt đo bản trước-khi-gỡ-de-herding |
| `RM-18`: *«cấm bỏ quên cụm ngày»* | `CLAUDE.md §61` | **khớp** — nền của thiết kế ghép cặp |
| V11054 register: *«§5g đa nguồn ≥3 (z=−2,54)»* nằm ở **nghĩa địa** | `artifacts/v11054/…` | **khớp** — nhưng agent từng ngụ ý nó còn sống trong prompt, **sai** |

### Ba lớp lệch nhau ⇒ FINDING

1. **`OWNER_SAID` ≠ `CODE_DID`** — owner đòi *«bắt model phân tích, cấm suy diễn»*; prompt hiện
   tại **ra lệnh bầy đàn** qua `§8`, và **ra lệnh ưu tiên nhiều nguồn** qua `:355` dù chính nó ghi
   `z=−2,54`.
2. **Trong `CODE_DID` tự lệch nhau** — de-herding gỡ ở một tầng, để nguyên ở tầng kia.
3. **`DOC_SAID` đúng mà agent vẫn suýt sập** — `RM-14` mô tả chính xác bẫy «đo bản không phải bản
   gửi đi», agent vẫn dump nhầm ở lần đầu.

---

## 7. Vướng vấp

| # | vấp | quy tắc |
|---|---|---|
| 1 | Dump `build_context_pack()` **trực tiếp** — không phải bản gửi đi (đường phục vụ còn gỡ de-herding sau) | **RM-14** |
| 2 | Nêu mâu thuẫn «`§4` vs `§11/§18`» — **nói quá**, hai đối tượng khác nhau | — |
| 3 | Ngụ ý `§5g` còn là luật cộng điểm — **nó đã được sửa rồi** | — |
| 4 | Gửi `system=""` khác CONTROL ⇒ **mất tính một-biến** | thiết kế thí nghiệm |
| 5 | Thi hành **lệch tài liệu thiết kế của chính mình** — tài liệu ghi T3 gồm `§22–§26`, mã lại nhét cả rulebook vào T2 | — |
| 6 | Đưa phép đo **vừa đăng ký, bảng còn rỗng** vào cổng chung ⇒ **BA quyết định không liên quan** cùng báo TRÔI | lỗi dây chuyền |

**Vấp 6 đã sửa tận gốc:** `K1` nay phân biệt **«CHƯA CHẠY»** với **«HỎNG»**, ân hạn **2 ngày tự
động hết** — quá đó mà bảng vẫn rỗng thì là **cron chết thật** và phải đỏ. Không bỏ qua im lặng.

---

## 8. Gỡ về

```bash
crontab backups/crontab.pre_v11059.txt
cp backups/main.py.pre_v11059 web/backend/main.py
cp backups/monitoring.html.pre_v11059 web/frontend/monitoring.html
sqlite3 data/lottery_ai.db "DROP TABLE prompt_3tang_ab_shadow_v11059;"
systemctl restart lottery
```

Prompt **official không hề bị đụng** ⇒ gỡ lane là hệ trở về đúng trạng thái trước phiên.

---

## 9. Theo dõi tiếp

| mã | việc | ngưỡng hành động | mốc |
|---|---|---|---|
| **FU-398** · `PB1108` | lane A/B ba tầng | `≥96 cặp bất đồng` **VÀ** `\|z\| ≥ 1,96` · **cấm đọc sớm** | lượt đầu **06:00 ngày 11/08** ⇒ đọc được **~27/08** |
| **FU-360** · `CL1008` | canh 24h kết thúc **10:06 ngày 11/08** | chặn NHẦM ⇒ rollback · **hôm 10/08 chỉ MT/MB chạy dưới cổng** — ghi đúng tầng | **sáng 11/08** |
| **FU-397** · `AT1008` | B1 anti-trap | `n(FULL_SPENT) ≥ 90` · đang **51/90** | ~giữa 12/2026 |
| **FU-397b** · `CG2108` | nhánh CHỐT GẤP `+0,40` — thêm `mined_at <= target_date` | chạm đường sinh số ⇒ **PLAN** | **21/08** |
| **FU-283** | vừa lọt cửa sổ `≤13/08` khi ngày đổi | — | **13/08** |
| FU-284 | cửa sổ đang chạy | **9,53** điểm · z ≥ 1,96 · n ≥ 150 | **20/08** — cấm đọc sớm |

**Đã dùng 1 mã FU mới (`FU-398`).**

---

TanPhatAI cần làm: ① ghi `QD-059` (owner 11/08 — prompt ba tầng chạy shadow ngay) và
`FU-398 · PB1108`; ② ghi **ngưỡng đăng ký trước `≥96 cặp bất đồng`** và **CẤM đọc sớm** trước
~27/08; ③ ghi **GIỚI HẠN**: bỏ nhánh T-A ⇒ nếu T-B thắng **không tách được** tái-cấu-trúc vs
gỡ-mâu-thuẫn — đừng để ai đọc thành một trong hai; ④ ghi vào sổ **ba mâu thuẫn prompt** (`M1`
`analysis_body:355` · `M2` `rulebook §8:44` · `M3` de-herding nửa chừng) vì chúng còn nguyên
trong **prompt official** và chỉ được gỡ ở nhánh shadow; ⑤ theo dõi **FU-360 chốt sau 10:06 hôm
nay** và **FU-283 hạn 13/08** vừa lọt cửa sổ.
