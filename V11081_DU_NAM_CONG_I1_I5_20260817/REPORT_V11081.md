# REPORT V11081 — ĐỦ NĂM CỔNG I1–I5 + VÁ CHỖ MÙ LÀM V11077/V11079 VÔ HÌNH

**LIỀN MẠCH 1/2** — V11080 (đêm 16/08) đặt `LUAT_CHUNG.md` vào gốc repo, khai danh tính sáu mặt,
dựng cổng `I1`, và ghi rõ `I2·I3·I4·I5` cùng `GĐ-3·GĐ-4·GĐ-5` **chưa làm** vì thiếu năm file
`INPUT_EVIDENCE`.
**LIỀN MẠCH 2/2** — Owner gửi **gói bàn giao** `GOI_BAN_GIAO_REPO_20260816` (10 file) đúng các
file còn thiếu, kèm câu hỏi *"V11077 · V11078 · V11079 có tồn tại không, và vì sao không có báo
cáo công khai?"*. Phiên này thi hành `NC-20260816-I v2` theo **bản gốc**, đóng đủ năm cổng, và
trả lời câu hỏi đó bằng bằng chứng.

---

## 1. Tóm tắt

Đóng đủ **năm cổng I1–I5**, mỗi cổng có **thử chặn hai chiều ĐẠT** (RM-15). Thay
`LUAT_CHUNG.md` bằng **bản phát hành chính thức**. Vá **chỗ mù** khiến hai bản đã push trở nên
vô hình với cổng báo cáo.

**Trả lời câu hỏi owner:** V11077 và V11079 **có thật, đã xong, đã push**. V11078 **không tồn
tại**. Giả thiết *"session khác đang giữ số, chạy từ 21h chưa xong"* **không khớp bằng chứng**.

**CHƯA LÀM:** `GĐ-3` · `GĐ-4` · `GĐ-5` · vá `_v11062` K1 · báo cáo cho V11077/V11079.

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

> *"Chạy tiếp prompt đi em, file đính kèm trong link em xem nhé
> `E:\Lottery_AI_Test\GOI_BAN_GIAO_REPO_20260816`"*

> *"Đồng thời trả giải đáp nghi vấn «V11077 · V11078 · V11079 có tồn tại không, và vì sao không
> có báo cáo công khai?» ==> anh nghĩ đang có 1 seccsion khác đang làm việc chắc là chiếm số này
> đó em, secsion đó đã truy quết từ 21h tới giờ vẫn chưa xong ah em. nên chưa có commit báo cáo
> ah em. em có thể tìm hiểu thêm nhé."*

---

## 3. Đào bới / phát hiện

### 3.1 — V11077 · V11078 · V11079: đo bốn nơi

| | commit | CHANGELOG | SSOT | HISTORY | báo cáo công khai |
|---|---|---|---|---|---|
| **V11077** | ✅ `a33b86a` **đã push** | ❌ 0 | ❌ 0 | ❌ 0 dòng | ❌ không có |
| **V11078** | ❌ **0** | ❌ 0 | ❌ 0 | ❌ 0 | ❌ không có |
| **V11079** | ✅ `4a7ee6d` **đã push** | ❌ 0 | ❌ 0 | ❌ 0 dòng | ❌ không có |

**V11078 không tồn tại ở bất kỳ đâu** — số bị nhảy qua.

**V11077 và V11079 đã XONG và ĐÃ PUSH.** Hai commit đó là **tổ tiên của `HEAD` hiện tại**. Một
session còn chạy dở **không thể** có commit đã nằm trong lịch sử `master` và đã lên remote. Thứ
còn thiếu **không phải code** mà là **CHANGELOG + SSOT + HISTORY + báo cáo** ⇒ đúng mã
`A61_VIOLATION_PARTIAL_BUMP` mà §63 đã đặt tên sẵn.

### 3.2 — Vì sao KHÔNG cổng nào kêu (phần đáng lo hơn câu trả lời)

`_v10921_report_gate.phien_ban_gan_day()` lấy danh sách version bằng:

```python
"""Doc CHANGELOG lay cac phien ban moi nhat theo thu tu xuat hien."""
for m in re.finditer(r"^##\s+(V\d{4,6}[A-Za-z]?)", txt, re.M):
```

**Chỉ đọc CHANGELOG.** Bản nào bỏ qua CHANGELOG thì cổng **không bao giờ nhìn thấy** ⇒ nó in
`✓ MỌI PHIÊN BẢN ĐỀU CÓ BÁO CÁO ĐẦY ĐỦ VÀ ĐÃ PUSH`.

`_v11062.kiem()` K1 **y hệt**: `cl, hi = muc_changelog(), muc_history()` rồi
`tu_moc = [v for v in cl ...]` — chỉ soi version **có trong CHANGELOG**.

**Đây là MÙ VỀ CẤU TRÚC, không phải sai tham số** — cổng lấy worklist từ **đúng tài liệu mà vi
phạm sẽ bỏ trống**. Cùng một họ với hai lỗi V11080 đã tìm:

| cổng | lấy chuẩn từ đâu | hệ quả |
|---|---|---|
| `_v10925` | **chính quy tắc sinh của nó** | lập luận vòng, luôn báo "SÁU MẶT ĐỒNG BỘ" |
| `_v10921` · `_v11062` K1 | **CHANGELOG** | version bỏ qua CHANGELOG thành vô hình |

Trong khi `_v11044_cong_so_hieu.py` quét **sáu nơi** kể cả `git log` và **thấy cả hai** —
*"425 số · cao nhất V11079"*. Repo **có sẵn** thông tin; hai cổng kia không dùng.

### 3.3 — `LUAT_CHUNG.md` V11080 là bản tự soạn, sai quy trình

Gói bàn giao chứa **bản phát hành chính thức** (20.715 B, `Doc V1.0.1`, do TanPhatAI xuất bản).
Bản V11080 là bản **agent tự soạn** từ SSOT Notion — dù nội dung bám nguồn, vẫn là bản dẫn xuất
viết tay, đúng điều **QĐ-E cấm**: *"cấm sửa tay bản sao trong repo — sửa ở SSOT rồi phát hành
lại"*. Đã thay.

---

## 4. Hướng xử lý và vì sao chọn

- **I2 mở rộng cổng sẵn có, không dựng cổng thứ hai** (`DC-20260816/B2`). Dùng chính
  `_v11027_so_muc_quan_tri.py` — bộ chặn mất mục đã nối vào hook commit.
- **Sổ chụp làm ranh giới mốc hiệu lực** (`DC-20260816/B1`): mục đã có trong sổ = điều **cũ**
  (để yên); mục sổ chưa có = điều **mới** (phải đủ sáu mặt). Không cần bảng ngày riêng.
- **Không tự viết báo cáo cho V11077/V11079.** Em không biết hai bản đó làm gì ngoài dòng
  commit; soạn báo cáo từ suy đoán là **chế dữ liệu** (`RM-17`). Ghi thẳng là thiếu.
- **Không làm GĐ-3.** Đổi tiền tố mà sót một matcher dò `§` sẽ làm cổng A5x/A6x **mù im lặng**;
  §60: *bỏ nửa chừng còn tệ hơn không làm*. Còn vướng đóng băng `QD-041` tới 21/08.

---

## 5. Đã làm gì (TRƯỚC → SAU → PHIÊN BẢN → KIỂM)

| # | việc | TRƯỚC | SAU | kiểm |
|---|---|---|---|---|
| 1 | `LUAT_CHUNG.md` | bản **tự soạn** 258 dòng | **bản chính thức** 20.715 B, Doc V1.0.1, 4 mã `GOV-*` | đọc lại dấu vết, không tin exit code |
| 2 | **I2** | chỉ chặn **mất mục** | thêm **mốc hiệu lực** hai vế (a)(b) | thử chặn **3 phép** ĐẠT |
| 3 | **I2** khoá so sánh | so **nguyên văn tiêu đề** | khoá theo **số hiệu**, dò cả trong thân | báo động giả **6 → 2 → 0** |
| 4 | **I3+I5** | **không có** | `_v11080_i3i5_chan_lan_du_an.py` | thử chặn hai chiều ĐẠT |
| 5 | **I4** | cổng đóng phiên thiếu phép I2 | thêm **đúng một** phép + dấu vết `docs/_I2_DA_CHAY.json` | thử chặn hai chiều ĐẠT |
| 6 | `_v10921` chọn version | **chỉ CHANGELOG** | **CHANGELOG ∪ git log** | nay in đúng `V11079` · `V11077` thiếu báo cáo |
| 7 | nâng version | — | CHANGELOG + SSOT + STATE `seq=410` + HISTORY | `--kiem` **K1–K4 ĐẠT** |

**Commit:** `V11080b` bản chính thức · `55f6029` I2 · `5e98178` I2b · `a85d8b0` I3+I5 · I4 ·
bump V11081.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11044_cong_so_hieu` | `V11081` trống — cấp đúng, không đoán |
| `_v11080_i1_cong_tu_kiem --thu-chan` | ✓ hai chiều |
| `_v11027_so_muc_quan_tri --thu-chan` | ✓ **ba phép**: sạch→0 · vi phạm (a)→1 · vi phạm (b)→1 · khôi phục **từng byte** |
| `_v11080_i3i5_chan_lan_du_an --thu-chan` | ✓ hai chiều |
| `_v10921_report_gate --thu-chan-i4` | ✓ hai chiều, **báo đúng mục thiếu** |
| `_v11062_nang_version --kiem` | ✓ K1–K4, `seq=410` |
| `_v10921_report_gate` | ✗ **CÒN TRƯỢT** — V11077 · V11079 thiếu báo cáo (**đúng, không che**) |

---

## 7. Vướng vấp — ba lỗi TỰ BẮT, cùng một họ

1. **I2 so bằng nguyên văn tiêu đề** ⇒ báo **6 điều mới thiếu mặt** giả. Cùng một điều được viết
   **khác chữ** ở các mặt là **cố ý** (`.AGENT.md` là hợp đồng tiếng Anh):
   `## §62 — NGUỒN BA LỚP` vs `## §62 — THREE-LAYER SOURCING` vs
   `## 11. VERSION BUMP … (§63 / A61)`. Đúng lỗi `RM-09` / `A58_VIOLATION_RAW_COUNT` — và tệ
   hơn: nó **đẩy agent đi chép cho bằng chữ**, tức **đi gom**, việc `DC-20260816/B1` vừa cấm.
   Sửa: khoá theo **số hiệu**. **6 → 2 → 0**.
2. **Bài thử I2 tự cho mình điểm.** In *"khôi phục nguyên trạng ✓ khớp từng byte"* trong khi đã
   đổi `.cursorrules` **CRLF → LF** trên cả **674 dòng**; `git status` hiện `M` ngay sau đó.
   Nguyên nhân: so **văn bản đã giải mã** (text mode bật universal-newlines), không so **byte**.
   Sửa: đọc/ghi nhị phân. Kiểm bằng **hai nguồn độc lập** — bài thử tự báo **và** `git`.
3. **I3 dương tính giả** ở `LUAT_CHUNG.md:105` — `SCOPE: RIÊNG <dự án>` là **chỗ mẫu** trong
   chính văn bản định nghĩa cú pháp. Đếm nó thành vi phạm sẽ bắt agent đi *"sửa"* bản luật
   chung — thứ QĐ-E cấm sửa tay. Sửa: lọc dạng `<...>`.

> Cả ba **đều là cổng tự cho mình điểm** — cùng họ với chính chỗ mù `_v10921` đang vá. Ghi lại
> để lần sau soi trước: *cổng lấy chuẩn từ đâu?*

---

## 8. Gỡ về

```bash
git revert <bump V11081> <I4> a85d8b0 5e98178 55f6029 <V11080b>
python web/backend/_v11027_so_muc_quan_tri.py --chup   # chụp lại sổ nếu cần
```

Không đụng DB · không đụng đường dự đoán/chọn số/prompt model · **không deploy** ⇒ không có gì
phải gỡ trên VPS.

---

## 9. Theo dõi tiếp

| mục | việc | trạng thái |
|---|---|---|
| **FU-375** | tám commit không có báo cáo công khai | **cùng họ** với V11077/V11079 — nay cổng **thấy được** |
| **mới** | **V11077 · V11079 chưa có báo cáo công khai** — cần session đã làm chúng viết, **không tự soạn** (`RM-17`) | treo |
| **mới** | `_v11062` **K1 vẫn mù y hệt** — lấy `tu_moc` từ `muc_changelog()` | treo |
| **mới** | `GĐ-3` · `GĐ-4` · `GĐ-5` chưa làm; GĐ-3 vướng đóng băng `QD-041` | sau 21/08 |
| **QD-021** | `K8: MỒ CÔI ĐẾN HẠN ≤18/08` — trôi thật | treo |
| **mới** | `_v10920_decision_ledger` cho verdict **không ổn định** (3 rồi 2 phép trôi trong hai lần chạy liên tiếp) vì phép con hết giờ **bị đếm thành "trôi"** — phải tách `KHÔNG_KIỂM_ĐƯỢC` khỏi `TRÔI` (`RM-12`) | treo |

⚠️ [ĐÍNH CHÍNH · ĐÃ RÚT LẠI RL-003: câu «verdict `_v10920` không ổn định» ở hàng trên là SAI ở
phần TRIỆU CHỨNG — chạy lại hai lần liên tiếp cho **cùng một kết quả** (diff rỗng), không tái
hiện "3 rồi 2". CƠ CHẾ nêu ở cột giữa (hết giờ bị đếm thành TRÔI, RM-12) vẫn ĐÚNG và vẫn cần vá —
chỉ vế "verdict không ổn định" là sai, không phải toàn bộ dòng. Xem docs/SO_RUT_LAI.json, bản rút
V11083_GD1_GD5_HET_GIO_DIEU_HUONG_BA_LUAT_20260817/REPORT_V11083.md.]

**Chưa sinh mã FU mới** — trần 5 mã/phiên chưa dùng; để phiên thi hành đặt mã cùng lúc với việc.

---

## §62 — NGUỒN BA LỚP

### `OWNER_SAID` (nguyên văn + giờ)

| giờ 17/08 | nguyên văn | phân loại OIL |
|---|---|---|
| ~00:0x | *"Chạy tiếp prompt đi em, file đính kèm trong link em xem nhé"* | `DONG_THUAN` |
| ~00:0x | *"anh nghĩ đang có 1 seccsion khác đang làm việc chắc là chiếm số này đó em… nên chưa có commit báo cáo ah em. em có thể tìm hiểu thêm nhé."* | **`CHUA_RO`** → đã tra, **bằng chứng ngược** (mục 3.1) |

### `CODE_DID` (evidence)

- `LUAT_CHUNG.md` ← gói bàn giao, **20.715 B**, `Doc V1.0.1`, 4 mã `GOV-*`.
- `web/backend/_v11027_so_muc_quan_tri.py` — `_khoa()` + I2(a) + `--thu-chan`.
- `web/backend/_v11080_i3i5_chan_lan_du_an.py` — mới.
- `web/backend/_v10921_report_gate.py` — `phien_ban_gan_day()` hợp hai nguồn · `_i2_da_chay()` ·
  `--thu-chan-i4`.
- `docs/_I2_DA_CHAY.json` — dấu vết I2 chạy trong phiên.
- Đo thật: `git log` V11077 = 1 · V11078 = **0** · V11079 = 1; CHANGELOG/SSOT/HISTORY = **0** cả
  ba. `_v11062 --kiem`: `seq=410`, `last_version=V11081`, K1–K4 ĐẠT.

### `DOC_SAID`

- `GOI_BAN_GIAO_REPO_20260816/06_NANG_CAP_AGENT_IDE.md` — `NC-20260816-I v2`, mục I1–I5 + mục 2
  *"Cổng không qua thử coi như không tồn tại"*.
- `GOI_BAN_GIAO_REPO_20260816/07_DINH_CHINH_VA_DIEU_CHINH.md` — `DC-20260816` A1 · **A2** · B1 ·
  B2 · B3.
- `LUAT_CHUNG.md` `Doc V1.0.1` — `GOV-PROJECT-SCOPE-SEPARATION-001` ·
  `GOV-RULEFILE-IDENTITY-001` · `GOV-LAW-STATE-SEPARATION-001` · `GOV-OWNER-REQUEST-LEDGER-001`.
- `CLAUDE.md §61` `RM-09` · `RM-12` · `RM-15` · `RM-17` · `RM-21`.

### ⚠ BA LỚP LỆCH NHAU — FINDING BẮT BUỘC BÁO

1. **`OWNER_SAID` ≠ `CODE_DID`.** Owner nghĩ V11077/V11079 do session khác **đang giữ, chưa
   xong**. Bằng chứng: hai commit **đã push**, là **tổ tiên của HEAD**. Không phải chưa xong —
   mà là **xong rồi nhưng thiếu tài liệu**. Đây là lệch **quan trọng**: nếu tin giả thiết cũ thì
   sẽ **chờ**, trong khi việc thật cần làm là **viết báo cáo bù**.
2. **`DOC_SAID` ≠ `CODE_DID`.** `_v10921` in *"MỌI PHIÊN BẢN ĐỀU CÓ BÁO CÁO ĐẦY ĐỦ"* trong khi
   hai bản đã push không có báo cáo. Đã vá; **`_v11062` K1 chưa vá** ⇒ lệch này **còn tồn tại
   một phần**.
3. **`DOC_SAID` (V11080) ≠ hiện trạng.** Báo cáo V11080 ghi `LUAT_CHUNG.md` là *"bản sao repo
   Doc V1.0.1"* — thật ra khi đó là **bản agent tự soạn**. Nay đã thay bằng bản chính thức; ghi
   ở đây để bản V11080 **không bị đọc nhầm về sau**.

---

## VERDICT

```
CODE_PUSHED      : ĐẠT — 6 commit trên master
REPORT_PUBLISHED : ĐẠT — thư mục này trên Lottery_AI_Notion_Reports
```

**KHÔNG** ghi `DEPLOYED` · **KHÔNG** ghi `RUNTIME_PROVEN` — phiên này không deploy, không đụng
VPS, không đụng DB (`RM-12`).

**KHÔNG** ghi *"mọi cổng xanh"* — `_v10921_report_gate` **còn trượt** vì V11077 · V11079 thiếu
báo cáo. Đó là **kết quả đúng**, không che.

---

TanPhatAI cần làm: ghi vào sổ theo dõi năm việc — (a) **V11077 · V11079 đã push nhưng thiếu CHANGELOG/SSOT/HISTORY/báo cáo**, cần session đã làm chúng viết bù, **không được tự soạn** (`RM-17`); (b) **V11078 không tồn tại**, không phải bản bị mất; (c) `_v11062` **K1 vẫn mù** — lấy worklist từ `muc_changelog()`, cùng lỗi vừa vá ở `_v10921`; (d) `_v10920_decision_ledger` cho **verdict không ổn định** vì đếm *"không kiểm được"* thành *"trôi"*, phải tách theo `RM-12`; (e) `GĐ-3 · GĐ-4 · GĐ-5` chưa làm, GĐ-3 chỉ làm được **sau 21/08** vì vùng đóng băng `QD-041`. Đồng thời cập nhật SSOT Notion §13.8: Lottery_AI_Test đã nhận **bản phát hành chính thức** `LUAT_CHUNG.md` Doc `V1.0.1` (thay bản agent tự soạn ở V11080).

⚠️ [ĐÍNH CHÍNH · ĐÃ RÚT LẠI RL-003: mục (d) ở trên — «verdict không ổn định» — sai ở phần TRIỆU
CHỨNG, chạy lại hai lần liên tiếp cho cùng một kết quả (diff rỗng), không tái hiện. Việc tách
`KHÔNG_KIỂM_ĐƯỢC` khỏi `TRÔI` theo `RM-12` vẫn nên làm vì CƠ CHẾ sai là thật, nhưng lý do vá là
vì cơ chế sai, KHÔNG phải vì verdict đang thật sự trôi. Xem docs/SO_RUT_LAI.json, bản rút
V11083_GD1_GD5_HET_GIO_DIEU_HUONG_BA_LUAT_20260817/REPORT_V11083.md.]
