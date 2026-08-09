# REPORT V11048 — ĐÍNH CHÍNH BỐN CHỖ AGENT LÀM SAI + ĐẤU NỐI 97 MỤC TREO BỊ CẤT

**Ngày:** 2026-08-09 14:00–15:00 · **Tầng verdict:** `RUNTIME_PROVEN` (đã deploy) cho phần sửa
chú thích · `REPORT_PROVEN` cho phần đấu nối

## 1. Tóm tắt

Rà lại chính việc agent vừa làm, theo **luật ba loại owner ký 09/08**. **Bốn đính chính, đều là
lỗi của agent** — không phải của owner, không phải của hệ.

| # | lỗi | mức |
|---|---|---|
| ① | chú thích **nói quá bằng chứng** nằm trong mã production | đã sửa + **deploy** |
| ② | **97 mục TREO** bị đẩy vào chỗ không ai đọc | đã **đấu nối** cổng |
| ③ | con số deploy API chưa đủ chính xác | đã tách kỹ |
| ④ | một **lập luận thổi phồng** trong V11046 | đã đính chính |

## 2. Owner yêu cầu gì (nguyên văn)

> các mồ côi thực sự thì có thể xóa gỡ bỏ tinh gọn, nhưng các mồ côi do lỗi code chưa đấu nối
> thì phải đấu nổi và tiếp tục kiểm tra còn giá trị phục vụ cho dự án không đã rồi mới có kế
> hoạch clear, nếu còn thì hạn đo, hoặc gộp cung với các phép đo không cần là rõ

Luật đó áp ngược lại chính agent, và bắt được bốn chỗ.

## 3. Đào bới / phát hiện



Rà lại theo **luật ba loại owner ký 09/08**. Ba đính chính, đều là lỗi của agent.

### ① Chú thích SAI nằm trong mã production — đã sửa

V11046 để lại ở `main.py:4262` và `:18404`:

> *«94 ngày vẫn được serve, 0 hit trên **57.011 dòng** nhật ký nginx»*

**Sai cả hai số.** Đo lại: nhật ký nginx chỉ có **15 bản xoay = 26/07 → 09/08 = 15 ngày ·
58.262 dòng**. «0 hit» chứng minh được cho **15 ngày**, **không phải 94**. 79 ngày trước đó
**không có bằng chứng nào** — nhật ký đã xoay mất.

Kết luận gỡ **không đổi** (0 hit trong 15 ngày + 0 inbound link + không route serve vẫn đủ),
nhưng **câu chữ nói quá bằng chứng** thì phải sửa. Lời commit ghi đúng («15 bản xoay»); thứ nằm
lại trong code mới là câu sai — và code là thứ người sau đọc.

### ② 97 mục TREO bị đẩy vào chỗ không ai đọc — loại (B), đã ĐẤU NỐI

V11044 tách 357 khối `### FU-V…` sang `docs/archive/` với lý do agent tự viết:
*«chúng là lịch sử, không phải tồn đọng»*. Rà lại thì lý do đó **chưa được chứng minh**:

| đo được | |
|---|---|
| khối LEGACY trong archive | **357** |
| mang nhãn TREO **bộ đọc công nhận** | **97** |
| trong số đó có mặt lại ở sổ chính | **0** ⇒ **bỏ rơi thật: 97** |
| phân bố | `DEPLOYED_PENDING_LIVE_VERIFY` **64** · `OWNER_LOCK` **18** · `WAIT_LIVE` **9** · `MEASURED_BUT_NOT_FIXED` **5** · `FALSE_NEGATIVE` 1 |

`OWNER_LOCK` và `WAIT_LIVE` đúng là hai nhãn `_v10920_session_start.py:20` khai là **«mục treo
phải báo»**. Và **không bộ đếm nào mở tệp archive** — `_v10958_fu_reader._DEFAULT` trỏ sổ chính.

**Nói cho công bằng:** 97 khối này **đã vô hình từ trước** khi chuyển — mẫu cũ chỉ khớp
`### FU-<số>`. Agent **không tạo ra** sự mù. Nhưng V11044 chính là commit **lần đầu nhìn thấy
chúng** (dựng `_LEGACY_TD`) rồi trong **cùng một lượt** đẩy sang chỗ không ai đọc.
**Thấy rồi mà cất đi thì khác với chưa từng thấy.**

**Đã đấu nối:** `_v11048_kiem_legacy_treo.py` đếm và bêu tên, **nối vào hook `git commit`**.
Trần đăng ký **97** — cổng **CHẶN khi tăng**, tức lại có mục treo bị đẩy vào chỗ khuất.
**RM-15:** thêm một khối treo giả ⇒ **thoát 1 CHẶN** («98 > trần 97») · khôi phục byte-khớp ⇒
**thoát 0**. Cổng **KHÔNG tự đóng mục nào** — quyết định là của owner (RM-06).

### ③ Deploy API: con số chính xác hơn V11047

V11047 ghi «43 lượt, `restart: skipped`». Tách kỹ hơn:

| nhánh | lần | mã có nạp? |
|---|---|---|
| `dry_run` | 5 | không ghi gì (đúng thiết kế) |
| `RESTARTING` | **25** | **có** — `deploy_api.py:479` chạy `systemctl restart lottery` |
| `PASS` + `restart: skipped` | **13** | **KHÔNG** |

Trong 13 lần `skip_restart`, **9 lần đẩy tệp `.py` backend** — gồm `main.py` (×3),
`gpt_analyzer.py` (×2), `database.py`, `model_registry.py`, `pnl_settlement.py`.
**Chín lần đó ghi Python xuống đĩa trong khi tiến trình vẫn giữ mã cũ trong bộ nhớ.**

Và 25 lần nhánh `RESTARTING` **kẹt vĩnh viễn ở trạng thái đó** — không lần nào ghi được PASS
cuối, vì tiến trình ghi trạng thái nằm trong cgroup của unit nên bị `systemctl restart` giết
trước khi ghi xong.

⇒ `__trigger_reload__.py` (16/04) chính là **cú vá cho đúng lỗ hổng này**, dựng trên một cơ chế
reload **không tồn tại** — nên lỗ hổng **chưa từng được vá**. `FU-387` cập nhật số.

*(Giới hạn phải nói: journald chỉ giữ một boot từ 09/08 05:23, nên «25 lần đó thật sự restart»
là **suy từ code**, không phải từ log.)*

### ④ Đính chính một lập luận thổi phồng của chính agent

V11046 viết *«15 commit sửa `viewer.html` sau khi nó chết»* để chứng minh lãng phí. Đo từng diff:
**3 commit** quét lại cả tệp, **12 commit** còn lại chỉ 1–47 dòng CSS trong các lượt
«re-inlined 14 pages». **Không commit nào đổi tính năng.** Đó là **bị quét chung**, không phải
có người còn nuôi. Con số 15 đúng nhưng **lập luận rút ra thì thổi**.


---

## 4. Hướng xử lý và vì sao chọn

**Sửa chú thích trước khi sửa gì khác.** Một câu sai nằm trong mã production nguy hơn một câu sai
trong báo cáo: người sau đọc code, không đọc lại commit message.

**Đấu nối chứ không đóng.** Owner ký luật (B) là *«phải đấu nối và tiếp tục kiểm tra còn giá trị
rồi MỚI có kế hoạch clear»*. Nên cổng chỉ **đếm và bêu tên**, tuyệt đối không tự đóng mục nào —
97 mục đó là owner ký, không phải agent quyết (RM-06).

**Trần đăng ký = con số đo được hôm nay (97), không làm tròn.** Cổng chặn khi **TĂNG**, tức khi
lại có mục treo bị đẩy vào chỗ khuất. Không chặn con số hiện tại — vì chặn thì mọi commit đều đỏ,
và cổng đỏ vĩnh viễn bị bỏ qua y như cổng xanh mù.

## 5. Đã làm gì

| việc | bằng chứng |
|---|---|
| sửa chú thích sai ở `main.py:4262` + `:18404` | đo lại: **15 bản xoay · 26/07→09/08 · 58.262 dòng** |
| **deploy** bản sửa | PID **1157897 → 1167898** · health **200** · `/du-doan` 200 · `/viewer.js` 404 |
| dựng `_v11048_kiem_legacy_treo.py` | 97 khối TREO · 0 có người kế nhiệm |
| nối vào hook `git commit` | hook khi sạch ⇒ `{"permission": "allow"}` |
| ghi `FU-390` | `DEPLOYED_PENDING_LIVE_VERIFY`, hạn `LX`, ba phương án cho owner |

## 6. Cổng kiểm

`LEGACY_TREO_V11048=DAT` (97, trần 97) · `O_STATUS_V11044=DAT` (264 khối) ·
`_v11015_cong_chan_cat_cut` **0** · `main.py` PARSE OK local + `py_compile` VPS.

**RM-15 — chứng minh chặn được:** thêm một khối `### FU-V99999-THU-CONG` mang `OWNER_LOCK` vào
archive ⇒ **thoát 1 CHẶN** («98 > trần 97») · khôi phục **byte-khớp** ⇒ **thoát 0 cho qua**.

## 7. Vướng vấp

Cả bốn mục ở §3 **là vướng vấp** — đều do agent. Đáng nói nhất là ②: agent dựng đúng công cụ để
**lần đầu nhìn thấy** 357 khối LEGACY, rồi trong **cùng một commit** đẩy chúng sang chỗ không ai
đọc, với lý do **tự viết** là «chúng là lịch sử». Lý do đó chưa từng được chứng minh.

Và ④ là bài học riêng: con số **15 commit** thì đúng, nhưng **lập luận rút ra** («có người còn
nuôi nó») thì sai — 12/15 chỉ là bị quét chung trong lượt re-inline CSS. Đúng số vẫn có thể sai
kết luận.

## 8. Gỡ về

```bash
git revert <commit V11048>
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test && cp backups/main.py.pre_v11042 web/backend/main.py && systemctl restart lottery'
```
Cổng mới độc lập — xoá `_v11048_kiem_legacy_treo.py` và dòng trong `code_quality_guard.py:56`.

## 9. Theo dõi tiếp

| mã | việc | chờ ai |
|---|---|---|
| `FU-390` | 97 mục TREO trong archive: **(a)** rà từng cái · **(b)** đóng gộp kèm lý do · **(c)** để nguyên, chỉ giữ cổng canh | **owner** |
| `FU-387` | ba cách xử cơ chế reload | **owner** |
| `FU-388` `FU-389` | `_v10705` · `_shadow_phase_audit` — chạy soi / gộp vào 18:05 | **owner** |
| — | vá biên `anchor_date <= date(?,'-1 day')` | ngay, trước khi bật lại tensor |

---

## LOCK-IN / OPEN / NEXT ACTION

**LOCK-IN:** chú thích sai đã sửa **và deploy** · 97 mục treo bị cất **đã có cổng canh, chặn được**
· con số deploy API đã chính xác (25 restart / 13 skip, trong đó **9 lần đẩy `.py` backend**) ·
lập luận «15 commit» đã đính chính.

**OPEN:** `FU-390` ba phương án · `FU-387` ba cách xử · `FU-388`/`FU-389` · cộng sáu mục còn treo
từ V11046.

**NEXT ACTION:** vá biên chống lookahead · tối nay đọc log 18:05 + 19:35 để đóng `FU-373`/`FU-366`.

*Đẩy cùng commit (A55 · §57.2).*
