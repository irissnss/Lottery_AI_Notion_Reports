# REPORT V11161 — KHỬ TRÙNG THẾ HỆ 2 + ĐĂNG KÝ TRƯỚC PHÉP ĐO TIẾN CỨU MT

> **Ngày:** 04/09/2026 00:55–01:2x (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> `POOL_VERDICT = HOLD` · `MODEL_ACTION = BLOCKED` · **production 0 ghi, 0 deploy**
> Hai việc cuối trong năm việc owner uỷ quyền ở `V11160`.

---

## 1 · Tóm tắt

| # | việc | kết quả |
|---|---|---|
| ⑤ | thiết kế lại luật khử trùng | 🟢 giữ **98%** shadow (cũ: gần 0) · đổi top-1 **48/99** (cũ 1/99) |
| ② | đăng ký trước phép đo tiến cứu | 🟢 `docs/DANG_KY_TRUOC_MT_SHADOW_V11161.md` · **chỉ MT** · nhãn `PROVISIONAL_AGENT_PROPOSED` |

**Và một kết luận trung thực phải nói rõ:** sau khi sửa luật, `C2` cho **ĐÚNG cùng con số với
`B`**. Tức các nguồn shadow **không dư thừa lẫn nhau** — `B` và `C2` là **một** comparator, không
phải hai.

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại |
|---|---|---|
| 04/09 ~00:2x | *«ok em thực hiện tuần tự lần lượt xử lý dứt điểm các vấn đề em đã đào ra dùm anh»* | `YÊU_CẦU` |

---

## 3 · Đào bới / phát hiện

### 3.1 · Luật khử trùng cũ là một comparator GIẢ

`V11159` dùng luật: *«shadow trùng NHÀ với một official đang có mặt ⇒ bỏ»*. Kết quả: `C` **trùng
khít `A`** ở cả 99 ô (`b=0 c=0` ba miền).

Đọc con số đó thành *«khử trùng không hại»* là **sai** — nó không nói gì về khử trùng, nó nói
luật đã loại **gần hết** shadow nên `C` chỉ là `A` đội tên khác. Đây là giới hạn của **luật agent
chọn**, và `V11159` đã ghi đúng như vậy.

### 3.2 · Ba tầng mới — mỗi tầng một lý do, không gộp

| tầng | loại cái gì | vì sao | nguồn |
|---|---|---|---|
| **① lineage** | nguồn PHÁI SINH (`combo-super`, `smart-ensemble`, `smart-ml`, `combo-no-token`) khi CHA có mặt | double-count **có thật trong thiết kế** | đọc code |
| **② alias** | hai id trỏ về CÙNG model API | không phải hai bằng chứng | `DEEPSEEK_API_ROUTE` + `DIRECT_DEEPSEEK_SHADOW_MODEL_MAP` — **đọc từ mã, không đoán** (`RM-10`) |
| **③ tương quan** | đồng thuận top-1 ≥ **0,70** trên ≥ **10** ngày chung | gần như không thêm thông tin | **đo trên cửa sổ as-of `date < D`** ⇒ **không oracle** |

Nhóm alias đọc ra được (không tự nghĩ):

```
deepseek-v4-flash|True   -> ['deepseek-reasoner', 'deepseek-v4-pro']
deepseek-v4-flash|False  -> ['deepseek-chat',     'deepseek-v4-flash']
```

Ngưỡng ③ đăng ký **TRƯỚC** khi nhìn kết quả (`RM-03`), nhãn `PROVISIONAL_AGENT_PROPOSED`.

### 3.3 · Kết quả — và kết luận ngược với kỳ vọng

| | luật cũ | **luật mới** |
|---|---|---|
| shadow hợp lệ TB / ô | 9,8 | 9,8 |
| còn lại sau khử trùng | ~0 | **9,7 (98%)** |
| đổi top-1 so với `A` | 1/99 (1,0%) | **48/99 (48,5%)** |
| số nguồn bị loại | (gần hết) | **16** — toàn bộ do tầng ③ |
| loại bởi ① lineage · ② alias | — | **0** |

**Chấm bằng kết quả thật (McNemar chính xác, Holm 3 miền):**

| miền | BT_A | BT_C2 | b | c | `p_exact` | `p_Holm` |
|---|---|---|---|---|---|---|
| MN | 9 | 7 | 6 | 8 | 0,7905 | 1,000 |
| MT | 11 | 15 | 4 | 0 | 0,1250 | 0,375 |
| MB | 6 | 5 | 2 | 3 | 1,0000 | 1,000 |

**Y hệt `B`.** ⇒ Khử trùng loại 16 nguồn nhưng **không đổi một kết quả nào**. Kết luận: các nguồn
shadow **không dư thừa lẫn nhau** ở ngưỡng này; `B` và `C2` là **một** comparator.

⚠️ Không được đọc thành *«khử trùng vô dụng»*. Nó nói: **giả thuyết «shadow chỉ lặp lại official»
không đúng** — đó là thông tin, và là thông tin ngược với lo ngại ban đầu.

### 3.4 · Vì sao chỉ đăng ký MT

| miền | b | c | tỉ lệ cứu | **n cần** |
|---|---|---|---|---|
| **MT** | 4 | 0 | 1,00 | **≈ 65 ngày (~2,1 tháng)** |
| MN | 6 | 8 | 0,43 | **907 ngày (~30 tháng)** |
| MB | 2 | 3 | 0,40 | **1.295 ngày (~43 tháng)** |

Đăng ký MN/MB là đăng ký một phép đo **không bao giờ kết luận**. Nói thẳng còn hơn hứa suông.

⚠️ `n cần` suy từ chính tỉ lệ quan sát, mà tỉ lệ đó dựa trên **4 ô bất đồng**. `RM-04`: con số này
**cũng không ổn định** — nó nói **bậc độ lớn**, không phải lời hứa.

---

## 4 · Hướng xử lý và vì sao chọn

**Vì sao ngưỡng đọc TỪ bản đăng ký chứ không viết cứng trong mã.** Để không ai — kể cả agent —
sửa ngưỡng sau khi nhìn kết quả. Không có bản đăng ký ⇒ công cụ **từ chối chạy**.

**Vì sao mốc đọc cố định ngày 30 và 65.** Đọc liên tục rồi dừng khi thấy đẹp là **p-hacking**.
Hai mốc này khoá từ bây giờ; công cụ **in cảnh báo** nếu bị gọi ngoài mốc.

**Vì sao cổng TIẾN chỉ cho phép TRÌNH packet, không tự bật.** `POOL_VERDICT = HOLD` và
`MODEL_ACTION = BLOCKED` vẫn đứng; một phép đo đạt cổng là điều kiện **cần**, không phải **đủ**.

**Vì sao ghi sẵn ba điều kiện HUỶ phép đo.** Nếu MT displacement không ghi được thì không tách
được thay-thế khỏi thêm-nguồn; nếu phát hiện thêm đường rò prompt thì nền không sạch; nếu
`runtime_prompt_contam_hits > 0` ở lượt khai `CONTEXT_ONLY_V2` thì regime tự mâu thuẫn. Viết
trước để không phải cãi sau.

---

## 5 · Đã làm gì — TRƯỚC / SAU / PHIÊN BẢN / KIỂM

| | TRƯỚC | SAU |
|---|---|---|
| luật khử trùng | «trùng nhà ⇒ bỏ» — loại gần hết | ba tầng lineage/alias/tương-quan — giữ **98%** |
| comparator `C` | trùng khít `A` (giả) | comparator thật, đổi top-1 **48/99** |
| bản đăng ký trước | **không có** | `docs/DANG_KY_TRUOC_MT_SHADOW_V11161.md` |
| công cụ đo tiến cứu | **không có** | `_v11161_rank_gen.py` + `_v11161_do_tien_cuu.py` |

**KIỂM công cụ (chạy thật trên VPS):**
- `--pha1` đọc bản đăng ký, xác định cửa sổ từ `2026-09-04`, miền sơ cấp `MT`, mốc đọc `[30, 65]`,
  báo `0 ô` — **đúng**, hôm nay chưa có kết quả; và nói rõ *«chưa chạy được, KHÔNG phải lỗi»*.
- `--pha2` **từ chối chạy** khi chưa có artifact pha 1.
- Artifact khử trùng đóng băng, băm `29bc7c76c46aa986…`; bản chấm kiểm băm **khớp** trước khi nối
  kết quả.

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| production ghi | **0** — mọi phép tính trên clone `v11159_phan_tich.db` |
| deploy | **0** |
| chống oracle | ✓ tương quan đo trên `date < D`; hai pha cấm gộp; băm kiểm trước khi nối kết quả |
| `RM-03` đăng ký trước | ✓ ngưỡng viết TRƯỚC mọi dữ liệu tiến cứu |
| `RM-10` không đoán tên | ✓ nhóm alias đọc từ `DEEPSEEK_API_ROUTE`, không tự nghĩ |
| `RM-04` n nhỏ | ✓ ghi rõ `n cần` bản thân nó không ổn định |

---

## 7 · Vướng vấp

**🟡 Bộ chấm `C2` quên `row_factory`** ⇒ `TypeError: tuple indices must be integers`. Sửa một
dòng. Lỗi công cụ, không ảnh hưởng số liệu.

---

## 8 · Gỡ về

**Không áp dụng** — bản này **không deploy, không ghi production, không đổi code đang chạy**. Hai
tệp mới (`_v11161_rank_gen.py`, `_v11161_do_tien_cuu.py`) là công cụ đọc, chạy tay. Xoá hai tệp
và bản đăng ký là gỡ hết.

---

## 9 · Theo dõi tiếp

| việc | trạng thái | ai chặn |
|---|---|---|
| **owner duyệt ngưỡng đăng ký trước** | **CHỜ OWNER** | đổi nhãn `PROVISIONAL_AGENT_PROPOSED` → `OWNER_LOCKED` |
| chạy `--pha1` hằng ngày từ 04/09 | bắt đầu từ lượt scheduled hôm nay | |
| đọc số lần 1 | **ngày thứ 30** (~04/10/2026) | cấm đọc sớm |
| đọc số lần 2 | **ngày thứ 65** (~08/11/2026) | |
| `23/09/2026` | **READOUT CHECKPOINT** | KHÔNG phải hạn buộc promote |
| materialize `output_counterfactual_rank` | `NOT_STARTED` | cần materialization proposal riêng |

---

## Nguồn ba lớp (§62)

### `OWNER_SAID`
- 04/09 ~00:2x — *«ok em thực hiện tuần tự lần lượt xử lý dứt điểm các vấn đề em đã đào ra dùm anh»*
- (03/09, còn hiệu lực) — *«Chưa đo được lợi thế so với baseline ngẫu nhiên ở mẫu hiện tại; cũng
  chưa đủ bằng chứng kết luận hệ thống thật sự kém hơn baseline.»*

### `CODE_DID`
- khử trùng v2 giữ 9,7/9,8 nguồn mỗi ô · đổi top-1 48/99 · loại 16 nguồn, toàn bộ do tầng ③
- `C2` McNemar y hệt `B`: MN `b=6 c=8` · MT `b=4 c=0` · MB `b=2 c=3`
- artifact băm `29bc7c76c46aa986…`, bản chấm kiểm băm khớp
- `--pha1` báo 0 ô (đúng), `--pha2` từ chối khi chưa có artifact

### `DOC_SAID`
- `docs/DANG_KY_TRUOC_MT_SHADOW_V11161.md` — **văn bản mới**, `DOC_SAID` = `CODE_DID` vì công cụ
  **đọc ngưỡng từ chính nó**, không viết cứng.
- `docs/CURRENT_TRUTH_SSOT.md` §V11159 ghi *«luật khử trùng quá gắt (C = A) — cần thiết kế lại»* —
  nay **đã làm**, và kết quả ngược với lo ngại: shadow không dư thừa lẫn nhau.
- `CLAUDE.md` `RM-03` *«đăng ký ngưỡng TRƯỚC ngày chốt»* — bản đăng ký này là ca thi hành trực tiếp.

---

TanPhatAI cần làm: ghi **`V11161`** — `governance_seq 477`, công khai bản này. Ghi **luật khử trùng cũ tạo ra một comparator GIẢ** (`C ≡ A`), đã thay bằng ba tầng lineage/alias/tương-quan-đo-được; luật mới giữ **98%** shadow và đổi top-1 **48/99** (cũ 1/99). Ghi **kết luận ngược kỳ vọng: `C2` cho ĐÚNG cùng con số với `B`** ⇒ các nguồn shadow **KHÔNG dư thừa lẫn nhau**; `B` và `C2` là **một** comparator. Ghi **bản đăng ký trước `docs/DANG_KY_TRUOC_MT_SHADOW_V11161.md`** — **chỉ MT** vì n-cần MT ~65 ngày trong khi MN 907 và MB 1.295; ba cổng TIẾN/DỪNG/HOÃN khoá trước; mốc đọc **cố định ngày 30 và 65** chống p-hacking; ba điều kiện huỷ. Ghi **nhãn `PROVISIONAL_AGENT_PROPOSED` — CHỜ OWNER duyệt** mới thành `OWNER_LOCKED`. Ghi **cổng TIẾN chỉ cho phép TRÌNH packet, KHÔNG tự bật**. Ghi **production 0 ghi, 0 deploy**. Ghi **`23/09/2026` = READOUT CHECKPOINT**. **Không mở Prompt 44. Không mở FU mới.** `POOL_VERDICT` giữ **`HOLD`**.
