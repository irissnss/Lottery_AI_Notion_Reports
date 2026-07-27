# V10863 — Chuẩn hóa UI Lane Test và bỏ điều hướng lặp

## Owner yêu cầu

- Card `/du-doan-test` trên mobile phải ngay ngắn như `/choi`.
- Khi sidebar đã đầy đủ, bỏ các nút điều hướng lặp để giao diện sạch.
- Giữ nguyên chức năng nghiệp vụ và dữ liệu.

## Root cause đã xác nhận

### 1. Loading class không được gỡ

`#app` khởi tạo với class `.loading`. Sau khi fetch xong, code thay `innerHTML` nhưng
không gỡ class. Vì vậy toàn bộ lane-test vẫn chịu:

- `padding: 1.4rem`;
- `text-align: center`;
- màu loading.

Ở 320px, vùng app bị thu từ 309px xuống 247px và text kỹ thuật bị căn giữa sai.

### 2. Comparison giữ hai cột trên mobile

Official và Test vẫn chia đôi ở 320px; mỗi card chỉ còn khoảng 121px. Tên card,
badge, số và chú thích phải ép/gãy trong cột quá hẹp.

### 3. Header chứa navigation trùng

Ba link Dự đoán chính / Quản lý vốn / Dashboard cộng Refresh rộng 339px; viewport
320px chỉ chứa được 304px nên Refresh bị cắt. Nút drawer ☰ còn đè badge Test Lane.

### 4. Card số dùng flex min-width

Bạch Thủ / Số phụ 1 / Số phụ 2 dùng `min-width:90px`; 320px thành bố cục 2 card
hàng đầu + 1 card hàng sau.

### 5. Hai hệ điều hướng cùng tồn tại

`/choi`, lane-test, settings, monitoring và search còn link route cũ dù sidebar đã
có đầy đủ các route đó.

## Fix

- Gỡ `.loading` ngay khi render; chỉ thêm lại trong lúc fetch.
- Bạch Thủ/Số phụ chuyển grid ba cột đều.
- Mobile ≤640px: Official/Test xếp dọc full-width, có nhãn rõ cho từng card.
- Xiên và dòng phương pháp được phép wrap an toàn.
- Header mobile chừa gutter cho ☰; Refresh thành nút icon; region tab rút gọn MN/MT/MB.
- Source/Cách hiểu chuyển thành `<details>` thu gọn như panel `/choi`.
- Ẩn navigation lặp:
  - lane-test: ẩn ba anchor, giữ Refresh;
  - `/choi`: ẩn quick-nav;
  - monitoring: giữ đồng hồ;
  - search: giữ Đăng xuất;
  - settings: giữ logout, user và `/filter` vì route này chưa có trong sidebar.

## Ma trận xác minh lane-test với payload live

Payload MN 27/07 có official, test bundle và 46 history rows.

| Engine | Viewports | Kết quả |
|---|---|---|
| Chromium | 320, 390, 430, 768, 1024, 1366 | 6/6 PASS |
| WebKit | 320, 390, 430, 768, 1024, 1366 | 6/6 PASS |

Tại 320px:

- body overflow = false;
- app padding = 0, text-align = start;
- visible duplicate header links = 0;
- Refresh nằm trong viewport;
- ba number cards = 93/93/93px (WebKit 91/91/91px);
- comparison card = 289px (WebKit 283px);
- help panel đóng mặc định;
- pageerror = 0.

Navigation cleanup: 4 trang × 3 viewport × 2 engine = 24/24 PASS.

## Deploy

- Frontend-only, không restart.
- MD5 local=VPS:
  - lane `75155b03fe6463fdd8f645142a578450`;
  - choi `8f925baefd37756c317a5eca5cb9c357`;
  - settings `5e55302a62ad13e89e37ef68aec00c32`;
  - monitoring `7dfad700ef387b5a802b83612bd28880`;
  - search `f760267c1b1fdbcb9de54b14dc4236a9`.
- Health 200; journal error-level 0.
- Route contract: lane/choi/monitoring guest 401; settings/search shell 200.
- Bốn bảng official giữ SHA256 IDENTICAL.
- Backup VPS `/root/backups_v10863/`; local `backups/v10863_pre/`.

## Safety

Không sửa prompt, scheduler, prediction writer, model selector, API/data contract,
`/du-doan` hoặc `final_bundles`. Contract lane primary exact 20/20 không đổi.

## Trạng thái

`DEPLOYED_PENDING_LIVE_VERIFY`: tự động đã pass; chờ owner hard-refresh và xác nhận
bằng mắt trên thiết bị thật.

Notion short page: `3aa1d385-9bf8-8138-9bd3-e139596701b9`.

