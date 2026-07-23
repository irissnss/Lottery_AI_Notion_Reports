# V10838 — Bugbot review: cứng hóa gate V10828 money board (23/07)

**GitHub:** https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10838_BUGBOT_GATE_HARDENING_20260723

## 2 finding của Bugbot (owner đưa ảnh 21:08)
1. **High — ĐÃ FIX:** gate vote trong `_v10759_money_board.py` đếm phiếu từ mọi row non-shadow **không giới hạn 15 model canon** → "phiếu lậu" từ model ngoài canon có thể giữ sống số 0-vote (đúng ca gate phải chặn). Verify dữ liệu: 20–23/07 zero phiếu lậu, kết quả gate không đổi (chưa gây hại); lịch sử có tiền lệ (`claude-opus-4-20250514` non-shadow đến 16/06). Fix: thêm `_V10828_CANON` (đúng bộ 15, khớp AE materializer).
2. **Medium — CHẤP NHẬN THEO THIẾT KẾ:** row lock tồn tại thì frozen thắng gate = bất biến "sáng = tối" cố ý (V10794); gate áp tại thời điểm TẠO lock; row logic-cũ chỉ tồn tại ngày 20/07 (đã qua). Ghi comment vào code, không sửa hồi tố.

## An toàn
Backup 2 đầu · sha khớp · compile · sanity board OK (lock hôm nay giữ nguyên) · restart 21:1x · health 200 / admin 401 · journal sạch · **hash 4 bảng pre=post IDENTICAL** (`fce6bae9`/`60e876fa`/`066d773b`/`bfb0670f`). Hai file herd-chase Bugbot xác nhận sạch.
