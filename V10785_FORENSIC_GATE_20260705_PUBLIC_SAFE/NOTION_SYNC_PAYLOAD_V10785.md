# V10785 — Forensic + Coverage Fix + Sandbox 25 lane + Gate GO/NO-GO 06/07 (05/07/2026)

**KẾT QUẢ CHÍNH**
- Gate Stage-1 đêm 05/07: **9/9 PASS → GO** cho live 06/07. Stage-2 = cron 07:30 tự chạy.
- Forensic 3 phiên (V10782–84): 5/6 claim đúng; 1 đính chính trung thực (P2.1 lock UI — sớm 1 ngày); phát hiện T-10 MN 15:45 không fire (deploy 16:03 sau mốc — tự lành 06/07).
- Root cause lỗ phủ sóng lớn nhất: kimi-k2.5 timeout 300s < p95 470s → **per-model cutoff 620s/480s + late-fill lane đo (late=1)** — deploy 20:33, sandbox 11/11 PASS trước.
- **Watchdog 15' + startup-recovery**: bịt lớp lỗi "restart giết trigger"; live sạch từ 20:33.
- Sandbox 25 lane cho 06/07: **24/25 OK** (production 0 rows đụng); qwen3-max-thinking root cause = JSON nằm trong `message.reasoning` → salvage fix deploy 21:24.
- 4 bảng official: 0 write sau freeze, 0 late row, tăng trưởng natural 100% khai báo được. /du-doan LOCKED nguyên phiên.
- Check 23:50: PASS toàn bộ (bundles bất biến, watchdog sạch, cron armed). Lock tuần 06/07 active từ 00:00 (bằng chứng 00:03).
- Vá sau 00:00: VPS money-board thiếu field quyết định ký (bản cũ 13:59) → sandbox → deploy 00:10 → /choi lockLine hiện `V10782-P2.3 (owner ký 05/07)` đủ 3 miền. Hash 4 bảng bất biến qua restart.

**QUYẾT ĐỊNH CHỜ KÝ (K1–K7)** — bảng đầy đủ trong GitHub report:
- K1: loại 3 rows qwen3.7-max/glm-5.2 chạy sớm 05/07 khỏi so găng (đề xuất LOẠI, giữ rows trong DB).
- K7: giữ per-model timeout + late-fill, review số liệu 12/07. (K2–K6: như V10784.)

**GITHUB (chi tiết đầy đủ)**
- `V10785_FORENSIC_GATE_20260705_PUBLIC_SAFE/BAO_CAO_TONG_V10785.md` (+ PARTIAL1, PARTIAL2)
- Commits public: 785e544 · 8b76646 · e33af02 · 0dcd27d. Private: d31b683 · 7b05eaf.
