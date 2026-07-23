# V10839 — Dọn nhiễu markdownlint IDE: 3K+ warning → 0 (zero runtime)

Owner 21:21 23/07/2026 đưa ảnh Problems panel Cursor: CHANGELOG.md hiện 1001 marker, tổng 3K+ warning. Chẩn đoán + xử lý cùng phiên. Thay đổi CHỈ ở config IDE — ZERO runtime/VPS/DB.

- Bản chất: toàn bộ là cảnh báo STYLE của extension markdownlint (MD041 thiếu H1 đầu file, MD032 list thiếu dòng trống quanh…), KHÔNG phải lỗi code/hệ thống.
- Đo CLI markdownlint-cli2: riêng CHANGELOG.md 8.223 finding / 23 rule — MD013 dòng-dài 5.319 · MD032 1.002 · MD024 heading-trùng 805 · MD022 573 · MD041 1. Panel chỉ hiện 1001 vì đó là trần hiển thị marker mỗi file của VSCode.
- Vì sao nhiều: changelog 21.7k dòng + docs governance viết kiểu nhật ký (~840 version entry; list sát đoạn văn, heading lặp theo version, dòng dài chứa bảng số) — đúng chuẩn nội bộ dự án nhưng lệch chuẩn style CommonMark mà linter áp mặc định.
- Ảnh hưởng thật: ZERO với runtime/dự đoán/DB/deploy (markdown không được VPS đọc). Hại duy nhất: nhiễu Problems panel che lỗi Python/JS thật + tốn CPU editor quét file lớn.
- Fix: thêm .markdownlint.jsonc (default: false — tắt style-lint toàn repo, comment ghi lý do + cách bật lại) + .markdownlintignore (backups/ artifacts/ share_exports/ node_modules/). CHỦ ĐÍCH không auto-fix 21.7k dòng CHANGELOG — diff khổng lồ vô nghĩa, rủi ro lớn hơn 0, giá trị bằng 0.
- Verify: CLI rerun CHANGELOG.md → 0 issues; quét rộng 186 file .md (root+docs+web) → 0 issues; diagnostics editor sạch.
- Governance: backup backups/v10839_pre/CHANGELOG.md.pre · KHÔNG deploy VPS (không chạm runtime, không phiên ghi DB → hash 4 bảng official không đổi) · private + public push · AUTOMATION_STATE seq 299.
- Báo cáo đầy đủ (GitHub-first §52G): https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10839_MARKDOWNLINT_NOISE_CLEANUP_20260723

Notion page: id 3a61d385-9bf8-810b-9827-e4baf9d7d6e0 · https://app.notion.com/p/3a61d3859bf8810b9827e4baf9d7d6e0
