# CONVERSATION CONTEXT — V11105 · 23/08/2026 (rạng sáng)

## Owner nói gì (NGUYÊN VĂN)

> *«① Duyệt truy tiếp CẢ HAI: con số 9 ms chưa giải thích + khâu rút số (33.685 token không cho ra
> số nào). ② FU-419 lối (a): dòng «D-1 cross-region tail pool» chuyển thành GHI SỐ ĐẾM, bỏ danh
> sách. Ghi nhận điều kiện đi kèm: CẤM hứa nó làm tăng độ trúng (FU-316 đã đo: 20,2% vs nền 21,0%,
> z=−1,01 — không neo).»*

> *«Nếu payload không còn lưu: ghi thẳng «không kiểm được» (không đoán) + đề xuất THIẾT KẾ lưu raw
> response cho các lượt rỗng từ nay — chờ owner duyệt, cấm tự vá.»*

> *«Phiên prompt lần 28 đã xong việc nhưng báo cáo CHƯA lên kho GitHub công khai.»*

---

## Owner bắt đúng một việc còn thiếu

Câu *«push báo cáo chưa em?»* rồi *«báo cáo CHƯA lên kho GitHub công khai»* — **đúng**. Lúc đó:

- kho riêng còn **1 commit chưa push** (`7625fd5`, bản vá `FU-419`);
- kho công khai **không có thư mục `V11105`** nào.

**Vì sao mắc kẹt:** cổng `§63` chặn commit vì `V11105` chưa có dòng `HISTORY`, mà tôi cố ý chưa nâng
version — đang chờ kết quả hai phép truy để viết `CHANGELOG` đủ nội dung. Rồi phiên trước kết thúc
giữa chừng.

**Bài học đúng, không phải bài học an ủi:** thứ tự làm sai. Đáng lẽ **nâng version sớm** rồi bổ sung
nội dung sau, chứ không phải giữ commit lại chờ nội dung — vì giữ lại thì một lần đứt phiên là
**mất trắng phần công bố**, đúng như đã xảy ra.

---

## Hai phép truy — cả hai ra đích, và cả hai nặng hơn dự kiến

### Con số 9 ms: không phải một dòng lạ, mà là một lớp lỗi

Tưởng là truy một dòng dữ liệu bất thường. Hoá ra:

```
05:16:04   bể song song rolling nạp glm-5.1
05:17:26   lượt gọi XONG                       (trace: 79,36 giây)
05:17:43   vòng lặp tuần tự MỚI TỚI LƯỢT       ⇒ future.result() trả tức thì ⇒ 9 ms
```

`:4557` sửa `start_time` theo bể nhưng **quên `_model_call_start`**. Và câu quyết định:

> Cùng lượt chạy đó, **5 model khác** cũng bị ghi **0,0–0,4 giây** trong khi thật là **12,7–86,0
> giây**.

Nghĩa là đây không phải *«một lần ghi sai»* mà là *«trường này sai bất cứ khi nào bể song song
chạy trước»*. Và `FU-283` — việc canh model chậm — **đang đọc đúng trường đó**. Sai theo hướng
**nhỏ đi** thì cảnh báo *«model chậm»* **không bao giờ nổ**. Đó mới là hậu quả thật, không phải
chuyện một con số xấu trong bảng.

### Payload: câu trả lời là «không còn», nhưng chỗ vứt nó mới đáng nói

Đã kiểm **253 bảng** DB production, `prediction_trace.jsonl` **5.774 dòng / 57 khoá**, `journalctl`
**959 dòng ngày 18/08**. Không đâu có.

Rồi tìm ra chỗ vứt:

```python
scheduler.py:4256   "result_keys": sorted(result_payload.keys())   ← CHỈ TÊN KHOÁ
```

Và trong danh sách tên khoá **có `_native_reasoning_json`**.

> Tức **3.000 ký tự suy luận thật của model đang nằm trong bộ nhớ ngay lúc đó**, đã được cắt sẵn
> (`gpt_analyzer.py:6748`), và mã **ghi tên khoá xong rồi vứt nội dung đi**.

Đường **thành công** (`:4470`) **có** ghi `reasoning_json`. Đường **rỗng** thì **không**.

**Đường rỗng vứt đúng thứ duy nhất giải thích được vì sao nó rỗng.** Mỗi lượt rỗng là một lần mất
bằng chứng vĩnh viễn — và tỉ lệ rỗng là **2,26%**, tức khoảng **2 lần mỗi 90 lượt**. Câu hỏi owner
hỏi hôm nay sẽ **lặp lại y hệt** vào lần rỗng tới, nếu không sửa.

---

## Một vấp nhỏ nhưng suýt vào báo cáo

Bản dump prompt đầu tiên dùng ngày **24/08** và cho ra **dòng D-1 RỖNG**. Nếu chép thẳng vào báo
cáo thì đã có một dòng *«sau khi vá, D-1 rỗng»* — vô nghĩa và gây hoang mang.

Lý do: D-1 của 24/08 là **23/08**, chưa xổ. Đổi sang ngày **23/08** (D-1 = 22/08, có kết quả) thì
ra số thật: **77 đuôi**.

Bắt được vì **đọc con số trước khi chép nó**, không phải vì có cổng nào chặn.

---

## Điều KHÔNG làm, và vì sao

**Không deploy `FU-419`.** Owner khoá *«sau 18:31»*; giờ đóng phiên là **04:5x**.

Và tôi **không để điều kiện giờ nằm trong đầu** — nó nằm trong mã: `_v11105_deploy_fu419.py` đọc
giờ **từ VPS** rồi từ chối nếu chưa tới 18:31. Đã thử lúc 04:02, **từ chối đúng**. Bước 2 của nó
còn bắt **cả ba miền phải có kết quả hôm nay**, vì thiếu một miền là deploy làm **lai** ngày đó —
đúng điều owner lo khi viết *«24/08 là ngày sạch đầu tiên»*.

**Không vá `FU-425` và `FU-426`.** Owner duyệt **truy**, chưa duyệt **vá**. Thiết kế đã soạn đủ cả
được/mất, chờ chữ ký.

**Không đụng dòng chị em** `tails[:12]` dù nó **cùng họ lỗi** với `FU-419` — owner khoá *«một dòng,
không đụng gì khác»*. Ghi lại để không ai tưởng đã xong.

---

## Điều kiện owner kèm theo, ghi ba nơi để không ai quên

> *«CẤM hứa nó làm tăng độ trúng»*

`FU-316` đã đo, có đăng ký ngưỡng **trước**: **20,2%** vs nền **21,0%**, `z = −1,01` ⇒ **không neo**.

Câu này ghi trong **chú thích mã**, trong **`CHANGELOG`**, và trong **báo cáo** — ba nơi, vì đây
đúng loại câu dễ bị một báo cáo sau viện ra làm nguyên nhân của một thay đổi độ trúng nào đó.
