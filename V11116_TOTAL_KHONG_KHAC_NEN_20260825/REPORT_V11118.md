# REPORT V11118 — THI HÀNH `PRJ-INTERACTION-LEDGER-001` VÀO CHÍNH BẢN BÁO CÁO

> **Cùng thư mục với `REPORT_V11116.md`** — `V11118` không phải một phiên đo mới; nó **sửa chính
> bản báo cáo `V11116`** cho đúng luật vừa ký. Mở thư mục riêng sẽ tách bản sửa khỏi thứ nó sửa.

**Ngày:** 2026-08-25, `~18:37` → `~18:50` giờ VN · **Tầng verdict:** `REPORT_PROVEN`
**Không đụng runtime:** không deploy · không restart · không sửa một dòng mã production nào.

---

## 1 · TÓM TẮT

`V11117` dựng **luật** `PRJ-INTERACTION-LEDGER-001`. `V11118` **thi hành luật đó lên bản báo cáo
đang lưu hành** — vì luật viết xong mà báo cáo cũ vẫn chỉ chép prompt lớn thì chính nó là
`PRJ_INTERACTION_REPORT_MISSING`.

Và phiên này bắt được **một chuyện đáng báo hơn cả phần sửa**: **hai phiên chạy song song trên
cùng kho**, xem `§7`.

## 2 · OWNER YÊU CẦU GÌ (NGUYÊN VĂN + GIỜ)

| giờ (VN) | NGUYÊN VĂN | loại |
|---|---|---|
| `~18:37` | *«Đã push báo cáo hết chưa em? · Kiểm tra lại toàn bộ 1 lần nữa xem còn gì không để push báo cáo 1 lần luôn · Các vấn đề anh tương tác trực tiếp đã push thành 1 bảng ghi nhận yêu cầu của owner chưa? Có cần cập nhật quy tắc trong claude.md để chuẩn hóa không vì đôi lúc code đi trước tài liệu do tương tác trực tiếp với em liên tục cho liền mạch ah em. Nên em claude code có thể đi trước tài liệu và việc ghi nhận các yêu cầu xác nhận của anh, chia sẻ của anh là cần thiết kể agent notion không bỡ ngỡ và phản bác nha em. · Việc anh thường xuyên tương tác với claude code để xử lý nhanh nên 1 số vấn đề anh yêu cầu xử lý em cần ghi nhận trong báo cáo có chuyên mục owner yêu cầu · Các vấn đề đào bới, tra soát, theo dõi cần liệt kê đầy đủ.»* | `YÊU_CẦU` |

Nguồn: **`docs/SO_TUONG_TAC_OWNER.md`** (kho riêng, append-only).

## 3 · ĐÀO BỚI / TRA SOÁT — liệt kê đủ

| # | việc | kết quả |
|---|---|---|
| 1 | Quét **cả hai kho**: commit chưa push · tệp chưa commit · báo cáo thiếu mục | kho riêng **0 chưa push**, có **tệp chưa commit**; kho công khai **1 commit chưa push** |
| 2 | Tra `§56` trước khi hỏi — đã có sổ tương tác chưa? | có `docs/SO_YEU_CAU_OWNER_20260824.md` **nhưng KHÔNG phải thứ owner cần**: nó **sinh tự động** từ `FOLLOW_UP_TRACKER` (`_v11107_so_yeu_cau_owner.py`), chỉ là bảng mã `FU`, **không giữ lời owner** |
| 3 | Truy `V11117` đã commit chưa | **đã** (`110b05b` + `7097d16`) — luật đã vào **đủ sáu mặt**, `HEAD` và bản làm việc **khớp 6/6** |
| 4 | Soi 11 mục `M` trong `git status` | **8 mục là chỉ mục cũ** (khác `CRLF`/`mtime`, `git diff` rỗng); chỉ **3 mục** là thay đổi thật |
| 5 | Soi `artifacts/v11056/d2_mn.json` | thay đổi **thật**: `n_ngay` `2338 → 2349`, lợi thế nền `+0,032 → +0,035pp` — làm mới phép đo, **đã commit** |
| 6 | Soi `docs/_I2_DA_CHAY.json` | chỉ đổi **dấu thời gian chạy** |
| 7 | Soi bó `share_exports/` + `share_exports.rar` (**7,7 MB**) | **bó xuất bản, không phải mã nguồn** ⇒ vào `.gitignore`, **không đưa vào Git** |
| 8 | Soi `web/_v10894_ui_check.js` | kiểm mắt thật khối mốc `FINAL` trên `/choi` — **nằm ngoài git từ trước**, nay đưa vào |
| 9 | Đối chiếu `4.9` với `9.2` trong `REPORT_V11116` | **hai bảng cùng nói về việc đào bới** — không xoá bảng nào, **nối chéo** để chúng không trôi khỏi nhau |
| 10 | Chạy cổng sáu mặt · mất mục quản trị · ô status · nâng version | **tất cả ĐẠT** |

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Sửa chính `REPORT_V11116`, không viết báo cáo mới thay thế.** Người đọc đang cầm bản `V11116`;
sửa ở bản khác rồi im lặng về bản cũ **không phải rút lại** (`PRJ-RETRACTION-001`).

**Không xoá bảng nào khi hai lượt sửa gặp nhau.** Hai bảng kiểm kê đều đúng, phục vụ hai góc nhìn.
Xoá một bảng để «gọn» là mất thông tin; để cả hai mà không trỏ nhau là chắc chắn trôi. Chọn
**nối chéo + câu «sửa thì sửa cả hai»**.

**Bó xuất bản không vào Git.** 7,7 MB nhị phân trong kho mã là gánh vĩnh viễn.

## 5 · ĐÃ LÀM GÌ

| # | việc | kết quả |
|---|---|---|
| 1 | `REPORT_V11116` mục **2** → `2.1` prompt chính · `2.2` **bảng 3 yêu cầu trực tiếp** có **nguyên văn + giờ** · `2.3` chỗ hổng thật | 🟢 |
| 2 | Thêm **`4.9`** — kiểm kê **17 việc** đào bới theo dòng chảy phiên, nêu đích danh **3 việc ra kết quả ÂM / không kết luận được** | 🟢 |
| 3 | Mục **9** — kèm cột **«ai chặn / chặn ở đâu»** | 🟢 |
| 4 | Dòng `TanPhatAI cần làm:` — **nói thẳng** phiên này code đi trước tài liệu, **và đó không phải vi phạm**, kèm **trỏ** `docs/SO_TUONG_TAC_OWNER.md` | 🟢 |
| 5 | **Nối chéo `4.9` ↔ `9.2`** | 🟢 |
| 6 | Sổ tương tác — **thêm một dòng KẾT**, **không sửa dòng cũ** | 🟢 |
| 7 | `.gitignore` chặn `share_exports/` + `*.rar` · đưa `web/_v10894_ui_check.js` vào git | 🟢 |
| 8 | **Bốn mặt version** `V11118` (`CHANGELOG` · `SSOT` · `STATE` · `HISTORY`), `seq 447 → 448` | 🟢 |

## 6 · CỔNG KIỂM

```
NANG_VERSION_V11062=ĐẠT      bốn mặt đi cùng nhau (K1..K4)
SÁU MẶT ĐỒNG BỘ              mọi .mdc tự nạp · không còn file chết
_v11027_so_muc_quan_tri      không mục nào biến mất · không điều mới nào thiếu mặt
O_STATUS_V11044=ĐẠT          314 khối FU đều có ô status
bảng đo I2                   đã chạy 2026-08-25 18:43:33 · DAT
cổng cấp số hiệu (FU-369)    V cao nhất V11117 ⇒ dùng V11118 · không sinh mã FU/QD mới
```

## 7 · VƯỚNG VẤP — **HAI PHIÊN CHẠY SONG SONG TRÊN CÙNG KHO**

Đây là phần quan trọng nhất của báo cáo này.

Agent **stage 9 tệp** rồi `git commit`. Commit ra **chỉ 6 tệp**. Ba tệp thiếu —
`CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` · `docs/SO_TUONG_TAC_OWNER.md` — **không mất**: một
**phiên khác đang chạy đồng thời** đã commit đúng ba tệp đó, mang **nhãn của phiên đó**:

```
6487e6d  V11037c: ghi phien 08/08 vao SO_TUONG_TAC_OWNER + liet ke du dao boi/theo doi
         CHANGELOG.md 80+ · docs/CURRENT_TRUTH_SSOT.md 24+ · docs/SO_TUONG_TAC_OWNER.md 1+
76c391b  V11118: ... (6 tệp còn lại)
```

Tương tự ở kho công khai: `eab8c24` **V11037d** đã viết lại mục `9` thành `9.1…9.6` **trong khi**
agent đang sửa mục `2` và `4` của **cùng tệp**.

**Hậu quả thật (nhẹ, nhưng phải nói):**
① khối `CHANGELOG` mang tiêu đề `V11118` lại **nằm trong commit tên `V11037c`** — ai truy theo
nhãn commit sẽ **tìm nhầm chỗ**;
② `REPORT_V11116` có **hai bảng kiểm kê** vì hai lượt sửa không biết nhau — đã nối chéo, không xoá.

**Không mất dữ liệu, không hỏng nội dung.** Nhưng đây đúng thứ luật *«một phiên tại một thời
điểm»* dựng ra để chặn, và lần này **cổng không bắt được** — vì không cổng nào soi *«có phiên khác
đang ghi cùng kho không»*.

**Agent tự khai giới hạn:** agent **không thể** chứng minh phiên kia là ai hay chạy từ lúc nào —
chỉ đọc được dấu vết trong `git log`. Đây là **quan sát**, không phải kết luận về nguyên nhân.

## 8 · GỠ VỀ

```bash
git revert 76c391b          # V11118 (kho riêng)
git revert 5396a06          # nối chéo 4.9 <-> 9.2 (kho công khai)
```
Không có gì trên máy chủ để gỡ — phiên này **không chạm runtime**.

## 9 · THEO DÕI TIẾP

| # | việc | ai chặn / chặn ở đâu |
|---|---|---|
| 1 | **Không có cổng nào phát hiện hai phiên ghi cùng kho** | **cần owner quyết**: dựng cổng (khoá phiên / kiểm `git log` trước commit) hay chấp nhận rủi ro |
| 2 | Khối `CHANGELOG V11118` nằm trong commit nhãn `V11037c` | **để nguyên** — sửa lịch sử git còn tệ hơn; ghi lại ở đây là đủ truy |
| 3 | Bó xuất bản `share_exports/` + `.rar` (7,7 MB) | **owner chọn nơi lưu** ngoài Git |
| 4 | `docs/SO_TUONG_TAC_OWNER.md` phải ghi **trong cùng phiên** từ nay | agent mỗi phiên — hiệu lực từ **25/08** |
| 5 | Mục `OWNER YÊU CẦU` **đầy đủ** trong mọi báo cáo công khai | agent mỗi phiên — hiệu lực từ **25/08** |
| 6 | Mọi mục treo khác của phiên đo `V11116` | xem `REPORT_V11116` mục **9.1…9.6** — **không lặp lại ở đây** |

## 10 · BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`
> `~18:37` — *«…em cần ghi nhận trong báo cáo có chuyên mục owner yêu cầu · Các vấn đề đào bới,
> tra soát, theo dõi cần liệt kê đầy đủ.»* *(nguyên văn đủ ở mục 2)*

### `CODE_DID`
- `git commit 76c391b` — 6 tệp · `git commit 5396a06` (công khai) — 1 tệp · **cả hai đã push**
- `_v11062_nang_version.ghi(version="V11118")` ⇒ `governance_seq 447 → 448`
- `_v10925_rule_sync_check.py` ⇒ *SÁU MẶT ĐỒNG BỘ* · `_v11027_so_muc_quan_tri.py` ⇒ *không mục nào biến mất*
- `git check-ignore -v` ⇒ `.gitignore:175 share_exports/` · `.gitignore:176 *.rar`
- `git log` ⇒ tồn tại `6487e6d` và `eab8c24` **không do phiên này tạo**

### `DOC_SAID`
- `CLAUDE.md` → `PRJ-INTERACTION-LEDGER-001` (owner ký 25/08) · `§57.3` mục 2/3/9
- `docs/SO_TUONG_TAC_OWNER.md` → sổ append-only, có dòng `~18:37` + dòng KẾT

### 🔴 BA LỚP LỆCH NHAU — finding bắt buộc báo
`DOC_SAID` nói *«một phiên tại một thời điểm»*; `CODE_DID` cho thấy **hai phiên cùng ghi**
(`6487e6d` · `eab8c24`). **Lệch thật, không phải phiền toái** — ghi vào mục 9.1 chờ owner quyết.

---

TanPhatAI cần làm: đọc **`docs/SO_TUONG_TAC_OWNER.md`** (kho riêng, append-only) **TRƯỚC** khi phản bác bất kỳ thay đổi nào của phiên 25/08 — phiên này **code đi trước tài liệu**, và owner **cho phép tường minh** (`PRJ-INTERACTION-LEDGER-001`): đo chạy từ `~13:00`, luật và sổ mới dựng `~18:37`; ghi nhận rằng `V11118` **không đo gì mới, không chạm runtime**, chỉ sửa `REPORT_V11116` cho đủ mục `OWNER YÊU CẦU` + kiểm kê đào bới + mục theo dõi; ghi nhận **hai phiên đã chạy song song** nên khối `CHANGELOG V11118` nằm trong commit nhãn `V11037c` — **truy theo nội dung, đừng truy theo nhãn commit**; và **KHÔNG** đọc `V11118` thành một kết luận đo lường nào — mọi con số vẫn là của `REPORT_V11116`.
