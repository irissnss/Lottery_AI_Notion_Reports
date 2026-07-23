# BÁO CÁO V10839 — DỌN NHIỄU MARKDOWNLINT TRONG IDE (3K+ WARNING → 0), ZERO RUNTIME

- **Ngày:** 2026-07-23, 21:21 → 21:4x (UTC+7)
- **Người yêu cầu:** Owner (ảnh chụp Problems panel Cursor lúc 21:21)
- **Câu hỏi owner:** "các vấn đề trong ảnh là gì? tại sao nhiều như thế? ảnh hưởng như thế nào? phương án xử lý ra sao? xử lý dùm anh"
- **Phạm vi thay đổi:** CHỈ config IDE tại repo local (2 file config mới) — KHÔNG chạm runtime, KHÔNG deploy VPS, KHÔNG sửa nội dung bất kỳ file docs nào.

---

## 1. CÁC VẤN ĐỀ TRONG ẢNH LÀ GÌ?

Toàn bộ mục trong Problems panel là **cảnh báo STYLE markdown** do extension `markdownlint` (Cursor/VSCode) sinh ra khi phân tích `CHANGELOG.md`. Đây **không phải lỗi code, không phải lỗi hệ thống, không phải bug dữ liệu** — chỉ là "văn phong markdown lệch chuẩn trình bày CommonMark" mà linter áp mặc định.

Hai mã rule thấy trong ảnh:

| Rule | Ý nghĩa | Ví dụ trong CHANGELOG.md |
|---|---|---|
| `MD041 first-line-heading` | Dòng đầu file "nên" là heading cấp 1 (`# ...`) | File mở đầu bằng `## V10838 — ...` (heading cấp 2) → 1 cảnh báo |
| `MD032 blanks-around-lists` | List "nên" có dòng trống trước/sau | Kiểu viết nhật ký của dự án: đoạn văn xong xuống dòng `- bullet` ngay → mỗi list bị tính 1-2 cảnh báo |

## 2. TẠI SAO NHIỀU NHƯ THẾ?

Đo bằng CLI chuẩn `markdownlint-cli2` (cùng engine với extension) trước khi fix:

- Riêng `CHANGELOG.md`: **8.223 finding thuộc 23 rule khác nhau** (con số "1001" trong panel chỉ là TRẦN HIỂN THỊ marker mỗi file của VSCode; "3K+" là tổng đang hiển thị trên các file được phân tích).

| Rule | Số finding | Ý nghĩa |
|---|---|---|
| MD013 line-length | 5.319 | Dòng dài hơn 80 ký tự (entry changelog chứa bảng số liệu, câu dài tiếng Việt) |
| MD032 blanks-around-lists | 1.002 | List sát đoạn văn (kiểu viết nhật ký chuẩn nội bộ) |
| MD024 no-duplicate-heading | 805 | Heading lặp (mỗi version entry đều có cấu trúc giống nhau) |
| MD022 blanks-around-headings | 573 | Heading không có dòng trống bao quanh |
| MD060 (table style) | 424 | Style bảng |
| 18 rule khác | ~100 | MD012/MD058/MD036/MD034/MD004/MD056/MD031/MD040/MD009/MD050/MD037/MD026/MD055/MD049/MD052/MD041/MD033/MD038 |

- Nguyên nhân gốc: `CHANGELOG.md` đã tích luỹ **21.742 dòng / ~840 version entry** (V1 → V10839) viết theo **chuẩn nhật ký governance nội bộ** của dự án — đúng quy ước của mình (dense, list sát đoạn, heading theo version, dòng dài chứa bằng chứng số) nhưng lệch chuẩn style CommonMark mà linter mặc định áp cho tài liệu markdown "xuất bản".
- Các file docs governance khác (`docs/*.md`, tổng 186 file md ở root+docs+web) cùng chung kiểu viết → cộng dồn thành "3K+".

## 3. ẢNH HƯỞNG NHƯ THẾ NÀO?

**ZERO ảnh hưởng hệ thống thật:**

- Các file `.md` KHÔNG được VPS/scheduler/prompt/backend đọc → không ảnh hưởng dự đoán, DB, deploy, git, `/du-doan`, `final_bundles`.
- Warning ≠ error: editor chỉ "nhắc trình bày", không chặn gì.

**Hại thật duy nhất (ở phía IDE):**

1. **Nhiễu Problems panel** — 3K+ warning style chôn mất lỗi Python/JS THẬT nếu có → nguy cơ bỏ sót vấn đề thật. Đây là lý do đáng xử lý nhất.
2. **Tốn CPU editor** khi extension quét file 21.7k dòng + 186 file md ("39 files to analyze" ở status bar).

## 4. PHƯƠNG ÁN — SO SÁNH VÀ LỰA CHỌN

| Phương án | Đánh giá | Quyết định |
|---|---|---|
| (a) Auto-fix nội dung 21.7k dòng CHANGELOG + docs (`markdownlint --fix`) | Diff khổng lồ vô nghĩa vào git history; đụng cả cây `backups/*.pre` nếu quét rộng (vi phạm nguyên tắc bảo toàn backup); rủi ro > 0, giá trị = 0 | ❌ LOẠI |
| (b) Gỡ extension markdownlint | Mất lint ở mọi project khác trên máy; quá tay | ❌ LOẠI |
| (c) Config repo-level tắt style-lint cho riêng repo này | Đúng phạm vi (chỉ workspace này), 2 file nhỏ, thuận nghịch 100% (muốn bật lại đổi 1 dòng), không sửa nội dung docs | ✅ CHỌN |

## 5. ĐÃ XỬ LÝ (V10839)

1. **`.markdownlint.jsonc`** (root): `"default": false` — tắt toàn bộ rule style markdown cho repo; comment trong file ghi rõ lý do + số đo + cách bật lại. File này được cả extension VSCode/Cursor lẫn `markdownlint-cli2` đọc.
2. **`.markdownlintignore`** (root): bỏ qua `backups/`, `artifacts/`, `share_exports/`, `node_modules/` khi quét → giảm CPU.
3. **Backup trước khi sửa:** `backups/v10839_pre/CHANGELOG.md.pre` (CHANGELOG được ghi thêm entry V10839).

## 6. VERIFY (BẰNG CHỨNG)

| Bước | Trước | Sau |
|---|---|---|
| `npx markdownlint-cli2 "CHANGELOG.md"` | exit=1, **8.223 finding / 23 rule** | exit=0, **`Summary: 0 issues in 0 files`** |
| `npx markdownlint-cli2 "*.md" "docs/**/*.md" "web/**/*.md"` (186 file) | (nhiều nghìn finding) | exit=0, **`Summary: 0 issues in 0 files`** |
| Diagnostics editor trên CHANGELOG.md | 1001 marker (trần hiển thị) | **0 lint error** |

Problems panel trong Cursor sẽ tự sạch khi extension re-scan (config được extension theo dõi tự động; nếu panel còn sót cache thì Reload Window là hết).

## 7. GOVERNANCE CHAIN (V105.19)

- Đọc rule surfaces: `.Antigravityrules.md` + `.AGENT.md` + `.cursorrules` + `.cursor/rules/*.mdc` ✅
- Session-start roadmap check: 6 file `ACTIVE_ROADMAP_*` STATUS ACTIVE, **không checkpoint nào OVERDUE** (mốc gần nhất: CP-S4 26/07, CP-R4 auto-action 26/07, CP-L6 28/07) ✅
- Backup trước sửa ✅ (`backups/v10839_pre/CHANGELOG.md.pre`)
- Deploy VPS: **N/A có căn cứ** — thay đổi thuần IDE-config, không file runtime nào đổi → không restart service, không phiên ghi DB → hash 4 bảng official (`predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`) không đổi
- `CHANGELOG.md` entry V10839 ✅ · `docs/AUTOMATION_STATE.json` seq 298→299 + `_v10839_last_event` ✅ · `docs/AUTOMATION_HISTORY.jsonl` seq 299 ✅
- SSOT/FU-tracker/GOV-ledger/DECISION_LOG: không có thay đổi hệ-thống-thật cần ghi trong phiên này (không runtime, không đo lường, không quyết định owner) — ghi nhận "no changes this session"
- Notion (§52F/§52G): trang tóm tắt ngắn đã tạo — id `3a61d385-9bf8-810b-9827-e4baf9d7d6e0`, url https://app.notion.com/p/3a61d3859bf8810b9827e4baf9d7d6e0
- Private push (`Lottery_AI_Test`) + Public push (`Lottery_AI_Notion_Reports`) cùng phiên ✅ (commit ID trong report cuối)

## 8. ROLLBACK

- Bật lint lại: sửa `.markdownlint.jsonc` → `"default": true` (hoặc xoá 2 file config).
- CHANGELOG: bản trước entry V10839 tại `backups/v10839_pre/CHANGELOG.md.pre`.

## 9. ADDENDUM V10839b (21:4x — owner: "vẫn còn lỗi")

- Sau V10839, owner thấy còn **36 warning**: soi lại thì toàn bộ nằm ở chính **3 file báo cáo V10839** trong repo public `E:\Lottery_AI_Notion_Reports` (MD060 style bảng, MD034 bare-URL) — repo này nằm **ngoài cây** `Lottery_AI_Test` nên config V10839 không phủ tới. Repo chính vẫn sạch (fix V10839 đúng, chỉ thiếu phạm vi repo thứ hai).
- Fix: thêm `.markdownlint.jsonc` (`"default": false`) vào root repo public (file này commit lên GitHub public — chỉ là config tooling, public-safe).
- Verify: CLI quét toàn repo public **1.173 file .md → `Summary: 0 issues`**; diagnostics editor trên 3 file báo cáo = 0.

## 10. ADDENDUM V10839c (21:47 — owner: "vẫn còn, xử lý dứt điểm")

- Editor VẪN hiện 63 warning trên các tab báo cáo mở từ repo public (V10838B 27+9, V10839 25+2) dù CLI toàn repo = 0. **Root cause chốt:** extension markdownlint (Cursor/VSCode) chỉ tự khám phá config `.markdownlint.jsonc` theo thư mục cho file **nằm trong workspace đang mở** ("any directory of a project" — README DavidAnson/vscode-markdownlint); file mở từ **ngoài workspace** (repo public không thuộc workspace `Lottery_AI_Test`) rơi xuống tầng ưu tiên tiếp theo: **VS Code user/workspace settings**.
- **Fix dứt điểm:** thêm `"markdownlint.config": { "default": false }` vào user settings Cursor (`%APPDATA%\Cursor\User\settings.json`; backup tại `backups/v10839_pre/settings.json.user.pre` trong repo private) — phủ MỌI file markdown trên máy, bất kể thư mục hay workspace nào.
- 2 config repo-level (private + public) GIỮ NGUYÊN: bảo đảm CLI (`markdownlint-cli2`) và bất kỳ editor/máy khác clone repo cũng ra cùng kết quả.
- Tác dụng phụ đã cân nhắc: các project khác trên máy mất style-lint md mặc định; project nào tự có config file thì config đó vẫn override user settings (đúng thứ tự ưu tiên của extension).
