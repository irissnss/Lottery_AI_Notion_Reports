# V10883 — Trang `/nghiem-thu` + ổ cắm bộ chọn vào official

**30/07/2026 · đã deploy · ổ cắm TẮT cả 3 miền**

Owner: *"UI của nó cũng cần làm cho chuẩn chỉnh để anh theo dõi ah em 3 miền rõ ràng. kế hoạch gộp và officical nên là đấu nối tiện lợi đấu nối xong mình cắt bỏ hoặc khởi động qua luồng khác đo khác cho tiện."*

## Trang riêng `/nghiem-thu`

Luồng thứ 5 có trang riêng như bốn luồng kia. Lấy nguyên theme/shell/drawer của `/choi` qua `_v10883_build_page.py` nên đồng bộ tuyệt đối; `/choi` đổi áo thì chạy lại script là khớp.

Bố cục: phán quyết → **3 thẻ miền số hôm nay** → 3 thẻ miền kỳ gần nhất (bản mới vs official hai cột, nhãn TRÚNG/trượt từng lá) → bảng thành tích gộp + từng miền → lịch sử từng ngày.

Mục "Nghiệm Thu" thêm vào sidebar của **12 trang**.

## Kiểm giao diện — bắt được lỗi mobile thật

Playwright 5 khổ (1440·1280·820·390·360, Chromium+WebKit). **Kết quả cuối 5/5 sạch.**

**Lỗi:** trang rộng 630px trên màn 390px. Nguyên nhân: `.v2-content` là flex cột, `min-width:0` chỉ tác dụng theo trục chính; bảng `min-width:620px` đẩy con nở theo trục ngang. **Sửa đúng:** `max-width: min(1240px, 100%)` trên `.nt-wrap`.

**Bản vá sai đã loại:** `overflow-x:hidden` — chỉ CHE, nội dung vẫn 622px và bị cắt.

**Bộ kiểm từng báo sai:** chạy bằng `file://` làm fetch hỏng, trang trắng vẫn báo "sạch". Đã đổi sang http + điều kiện render rỗng KHÔNG được tính sạch.

## Ổ cắm vào official

Đặt SAU khi official chấm điểm, TRƯỚC khi lắp 5 lá. Bộ chọn cắm vào **chỉ đổi thứ tự xếp hạng**; luật lắp lá, cổng 0,40, công thức lo3, cách chấm giữ nguyên.

- **Mặc định TẮT** — deploy không đổi con số nào
- **Bật/tắt từng miền** — vì bằng chứng mỏng ở mức từng miền
- **Hỏng thì tự rút** — mọi lỗi rơi về xếp hạng official + ghi lý do
- **Không cần deploy** — nút ở `/monitoring`, hiệu lực từ lần chốt kế tiếp
- **Bắt buộc ghi lý do** khi đổi; hai bảng nhật ký cắm/rút và ngày có tác dụng
- `generation_method` = `weighted_voting_wr+connector_<tên>` những ngày có cắm

Bộ chọn có sẵn: `deherd_family_sqrt` (backfill 135 miền-ngày, bạch thủ 49 so 34, p=0,0026).

## Một lỗi quy trình của agent

Bài kiểm lần deploy đầu gọi `generate_final_bundle` — hàm GHI chứ không phải đọc — làm bundle MN 30/07 nhảy version 1→2. **Nội dung không đổi** (`BT=86`, `lo2=["86","31"]`, `lo3=086`, method y nguyên); chưa xổ nên không mất kết quả chấm; v2 là trạng thái bình thường của mọi bundle gần đây. Đã thay bằng chứng minh chỉ-đọc-code. Bài học ghi vào tracker.

## An toàn

Hash 4 bảng official pre/post IDENTICAL. V10841 PASS. Công tắc TẮT cả 3 miền. Mọi trang quản trị trả 401 khi chưa đăng nhập.

**Ổ cắm không tự bật** — mọi lần cắm cần quyết định owner và lý do ghi lại. Đọc phán quyết luồng vào 05/08.

Báo cáo đầy đủ: `V10883_PAGE_AND_CONNECTOR_20260730/REPORT_V10883.md`
