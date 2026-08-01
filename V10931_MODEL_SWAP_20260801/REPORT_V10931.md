# V10931 — Hoán đổi 2 model AI + dời hạn MT 16:58 / MB 17:58

**Ngày:** 01/08/2026 · **Trạng thái:** đã deploy, 16/16 tự kiểm sạch, hash 4 bảng giữ nguyên

---

## 1. Tóm tắt

Sau 110 ngày shadow không promote ai, owner chốt **hoán đổi ngay hôm nay**: hai model AI yếu ra,
hai shadow tốt vào — giữ nguyên số lượng pool để bộ lọc chọn mạnh nhất không mất khả năng chọn.

```
RA    gpt-5.4        −0,99pp so mặt bằng · dương 2/5 kỳ
RA    gpt-5-mini     −1,19pp · dương 2/5 kỳ
VÀO   glm-5.1        +1,58pp · dương 4/5 kỳ · 110 ngày/309 lượt · KEEP_STABLE
VÀO   gpt-oss-120b   +3,14pp · dương 3/5 kỳ · 104 ngày/306 lượt · lỗi 0,98%
```

Kèm **dời hạn output cuối MT `16:53 → 16:58` và MB `17:53 → 17:58`** vì hai model mới chậm gấp
40–70 lần hai model bị thay.

Ngay lần chọn đầu sau khi đổi, **`combo-super` ở MN đã tự nhặt `gpt-oss-120b` vào top-2** — đúng
cơ chế owner mô tả.

---

## 2. Owner yêu cầu gì (nguyên văn)

**01/08 12:56:**

> *"showdow gì mà lâu quá trời không lấy được model nào tốt nhét vào total offical quả là lãng
> phí, 1 chú ý là cắt model ảnh hưởng đến combo super mới quan trọng cận thận chỗ này."*

**01/08 ~13:0x**, khi được hỏi về việc cắt 2 model tốn tiền:

> *"sao không thay thế 2 model show tốt vào luôn, cơ chế filter model mạnh nhất thì nhét vô mà
> output chứ em"*

Và chọn **promote ngay hôm nay**, **nhận cả hai model dù `glm-5.1` lỗi 4,65%**.

**01/08 ~13:3x**, khi được trình rào thời gian:

> *"ok em vậy dời chốt output cuối cùng cho MT là 16h58 và MB là 17h58 em thấy sao?"*

---

## 3. Đào bới / phát hiện

### 3.1 Rào thời gian — suýt làm hỏng nếu không kiểm

Độ trễ thật 14 ngày:

| Model | MN | MT | MB |
|---|---|---|---|
| `glm-5.1` | 571s (max 676) | 545s (max **796**) | 429s (max 733) |
| `gpt-oss-120b` | 256s (max 843) | 618s (max **886**) | 342s (max 585) |
| `gpt-5.4` *(bị thay)* | 11s | 11s | 11s |
| `gpt-5-mini` *(bị thay)* | 11s | 11s | 11s |

**Giới hạn chặt của chuỗi là `AI_MODEL_HARD_TIMEOUT_SEC = 300` giây.** Nhét thẳng vào là hai
model mới **bị cắt gần như mọi lần** — thay xong thành mất trắng 2 chỗ.

### 3.2 Vì sao chúng sống được ở shadow mà sẽ chết ở official

Cơ chế **hạn riêng từng model đã có sẵn** (`_v10785_late_fill.MODEL_HARD_TIMEOUT_OVERRIDES`),
thêm từ V10785 vì `kimi-k2.5` p95 ~470s bị mốc 300s cắt mất 7 lần/7 ngày.

Nhưng:
- Hai model mới **chưa được đăng ký** hạn riêng → nhận mốc chung 300s
- Luồng **shadow** (`scheduler.py` ~7523) **có** truyền hạn riêng và đăng ký late-fill khi
  timeout → watchdog nhặt lại sau
- Luồng **official** (`scheduler.py` ~4652) gọi `_await_model_call_to_hard_timeout(call)`
  **không truyền** hạn riêng → dùng mốc chung, và **không** có late-fill → mất trắng

### 3.3 Trần cứng của hạn MT

`_v10759_money_board.CUTOFF = {'MN': 16.0, 'MT': 17.0, 'MB': 18.0}` — mốc chống nhìn trộm.
Hạn output **bắt buộc phải trước** mốc đó. Nên **16:58 là con số tối đa có thể cho MT** —
owner chọn đúng sát trần.

### 3.4 Kiểm cảnh báo có sẵn trong code combo-super

`combo_super.py` có khối cảnh báo:

```
# V17.13 P0.5 OUTPUT SAFETY: New models EXCLUDED from combo pool
# Reason: default WR=50% → can win top-3 selection → AFFECTS /du-doan output
# Gate: Must reach SHADOW_AUTO + ≥5 predictions before pool entry
```

và `glm-5.1` đang bị **comment lại** vì chính lý do đó.

Kiểm: cổng yêu cầu **≥5 dự đoán** — hai model có **306–309**. Và ngày 01/08 cả hai có dữ liệu
**thật n=7** trong cửa sổ WR 7 ngày, **không** rơi vào nhánh mặc định 50%. Cổng thoả rất xa.

---

## 4. Hướng xử lý và vì sao chọn

| Phương án | Vì sao chọn / loại |
|---|---|
| **Hoán đổi giữ nguyên pool 7** | **ĐÃ CHỌN** (ý owner). Bộ lọc top-2 không mất khả năng chọn; model mạnh tự được nhặt |
| Chỉ cắt 2 model yếu, không thêm | Loại: pool AI còn 5, và không giải quyết chuyện shadow 110 ngày không promote |
| Chỉ thêm 2 model mới, giữ 9 | Loại: đổi số lượng official 15→17, làm nhiễu mọi phép so lịch sử |
| **Đăng ký hạn riêng 840s/900s** | **ĐÃ CHỌN.** Dùng lại cơ chế sẵn có |
| Nâng mốc chung 300s → 900s | **Loại.** Mọi model hỏng đều treo lâu gấp 3 lần |
| **Dời hạn MT 16:58 / MB 17:58** | **ĐÃ CHỌN** (số của owner). MT sát trần `CUTOFF=17:00` |
| Dời chuỗi AI sớm hơn thay vì nới hạn | Loại: MT phải chờ MN xổ 16:30, không thể sớm hơn |
| Cắt hẳn model ML để tiết kiệm | Loại: 4 ML **miễn phí**, pool 4 chọn 3 — cắt 1 là mất hoàn toàn khả năng chọn |

---

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `model_registry.py` | `gpt-5.4` + `gpt-5-mini`: `ACTIVE → SHADOW_AUTO`, `output_eligible False`. `glm-5.1` + `gpt-oss-120b`: `SHADOW_AUTO → ACTIVE`, `output_eligible True`. **Sửa ở bảng gốc**, các danh sách tự suy ra |
| `combo_super.py` | `AI_MODELS` hoán đổi, giữ đúng **7**. `ML_MODELS` **không đụng** (vẫn 4) |
| `_v10785_late_fill.py` | Thêm hạn riêng `glm-5.1: 840s`, `gpt-oss-120b: 900s` |
| `scheduler.py` | Luồng official nay **truyền hạn riêng** như luồng shadow vốn đã làm |
| `_v10782_freeze.py` | `FREEZE_MARKS` MT/MB → 16:58/17:58 · `T_CHOT_MARKS` → 16:55/17:55 |
| `_v10759_money_board.py` · `_v10861_*.py` · `_v10692_*.py` | `OUTPUT_DUE` / `DEADLINE` / `OUTPUT_FREEZE_HHMM` → 16:58/17:58 |
| `_v10891_deadline_guard.py` | `FINAL` → 16:58:00/17:58:00 · `LOCK_TARGET` → 16:56/17:56 |
| crontab | Khoá `/choi` MT `16:51→16:56`, MB `17:51→17:56` |

Backup: `backups/v10931_pre/` (9 file, bản VPS trước khi sửa) + crontab trên VPS.
Deploy: PID `549882 → 558029`, health 200, admin 401.

---

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| `OUTPUT_ELIGIBLE_MODELS` | **15** (không đổi số lượng) · có 2 model mới · không còn 2 model cũ ✓ |
| `TOKEN_MODELS` | **7** ✓ |
| `SHADOW_AUTO_EVAL_MODELS` | **11** · nhận lại 2 model cũ ✓ |
| `combo_super.AI_MODELS` | **7** ✓ |
| `combo_super.ML_MODELS` | **4 nguyên vẹn** — chỗ owner cảnh báo ✓ |
| Hạn riêng | `glm-5.1` 840s · `gpt-oss-120b` 900s · model khác vẫn 300s ✓ |
| 4 hằng số hạn output | `FREEZE` = `OUTPUT_DUE` = `DEADLINE` = `lane FREEZE` = MT 16:58 / MB 17:58 ✓ |
| Cron khoá `/choi` | `15:43` · `16:56` · `17:56` ✓ · tổng 71 dòng không đổi |
| **Bộ tự kiểm nhất quán** | **16 phép · lệch 0** ✓ |
| **Hash 4 bảng khoá** | **GIỮ NGUYÊN cả bốn** ✓ |
| combo-super chọn với pool mới | MN đã tự nhặt **`gpt-oss-120b`** vào top-2 ✓ |

---

## 7. Vướng vấp

| # | Vấp | Hậu quả nếu bỏ qua |
|---|---|---|
| 1 | Hai model mới chậm gấp 40–70 lần, vượt mốc chặt 300s | **Thay xong thành mất trắng 2 chỗ** — model bị cắt, không ra số nào |
| 2 | Luồng official không truyền hạn riêng, luồng shadow thì có | Đăng ký hạn riêng thôi vẫn vô dụng với official |
| 3 | `CUTOFF['MT'] = 17:00` là trần cứng | Dời hạn quá 17:00 là vi phạm chống nhìn trộm |
| 4 | Các danh sách model **suy ra** từ `MODEL_REGISTRY` | Sửa danh sách thay vì bảng gốc là sửa nhầm chỗ, không có tác dụng |
| 5 | Script deploy vỡ ở bước đọc lại vì module in chữ trước JSON | Không ảnh hưởng deploy, nhưng suýt tưởng deploy lỗi. Đã tách bằng mốc `JSON_START` |
| 6 | `glm-5.1` lỗi **4,65%** — ngang `gemini-3.5-flash` từng bị cho nghỉ vì hay rớt | Owner đã được báo và **chấp nhận rủi ro** |

---

## 8. Gỡ về

```
python web/backend/_v10931_deploy.py --rollback
```

Đẩy lại 9 file trong `backups/v10931_pre/`, hoàn nguyên cron khoá `/choi` về 16:51/17:51,
restart. **Mất khoảng 1 phút.**

Gỡ về thì: hạn quay lại MT 16:53 / MB 17:53, `gpt-5.4` + `gpt-5-mini` trở lại official,
`glm-5.1` + `gpt-oss-120b` trở lại shadow. Không cần đụng database — phiên này **không sửa dữ
liệu**, hash 4 bảng giữ nguyên.

Bản crontab cũ cũng còn trên VPS: `/root/.local_backup_v10931b_crontab_*.txt`

---

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng | Hạn |
|---|---|---|---|
| **FU-194** | Canh live tối nay: MT **16:58**, MB **17:58** | Bundle đủ **15 model**; `glm-5.1` và `gpt-oss-120b` có mặt trong `score_breakdown`; journal 0 lỗi timeout | 01/08 tối |
| **FU-195** | `glm-5.1` lỗi 4,65% — owner chấp nhận nhưng phải canh | Nếu lỗi vượt **6%** trong 14 ngày hoặc làm MT lỡ mốc **≥2 ngày**, gỡ nó ra khỏi official | 15/08 |
| **FU-196** | Đo hiệu quả hoán đổi | So 14 ngày sau với 14 ngày trước: tỉ lệ trúng bạch thủ và tiền, theo từng miền | 15/08 |
| FU-189 | 19 experiment của 6 lane nghỉ phải thực sự vắng | journal 0 lỗi | 02/08 |

Nguyên văn lời owner: `CONVERSATION_CONTEXT_V10931_20260801.md` cùng thư mục.
