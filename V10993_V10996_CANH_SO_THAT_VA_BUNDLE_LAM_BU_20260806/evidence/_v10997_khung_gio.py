# -*- coding: utf-8 -*-
"""V10997 — KHUNG GIỜ DEPLOY: một nguồn sự thật duy nhất.

Owner ký 06/08/2026 ~15:1x, nguyên văn:

    "Anh xác nhận riêng ngày hôm nay danh riêng cho việc code, fix, chỉnh sửa hay cho
     thực hiện đi em, các ngày khác vẫn như củ ngày nào cũng Block thì anh không thời
     gian để code, fix điều khiển, block theo anh nghĩ thì sau khi ra số final MN 15h45
     là không được xử lý nữa nha em, để hệ thống ổn định chạy cho xong live của ngày
     là được"

VẤN ĐỀ CỦA KHUNG CŨ
===================
FU-207 cũ cấm **05:00–18:15**, tức chỉ còn ban đêm để làm việc. Owner nói thẳng:
*"ngày nào cũng Block thì anh không thời gian để code, fix điều khiển"*. Đúng — khung đó
biến mọi việc sửa chữa thành việc phải làm lúc nửa đêm.

KHUNG MỚI — theo ý owner, CHỈNH THEO SỐ ĐO
==========================================
Owner đề xuất: chặn từ mốc MN 15:45. Đo 60 ngày thì thấy đề xuất đó **thiếu một cửa sổ**:

    MN  bundle sinh 04:16 – 05:20   ← số MN LÀM TỪ 4 GIỜ SÁNG
    MT  bundle sinh 16:37 – 16:50
    MB  bundle sinh 17:32 – 17:44

Mốc 15:45 chỉ là lúc ĐÓNG BĂNG hiển thị, không phải lúc sinh số. Chặn từ 15:45 thì
khoảng 04:00–05:30 — lúc MN thật sự đang gọi model và ghi bundle — vẫn hở.

Nên hai cửa sổ cấm:

    CẤM 1   03:45 → 06:00    MN sinh số (04:16–05:20 + biên hai đầu)
    CẤM 2   15:30 → 18:15    từ trước mốc MN 15:45, qua MT 16:58, tới sau MB 17:58

    CHO PHÉP  06:00 → 15:30   (9,5 giờ ban ngày)
              18:15 → 03:45   (9,75 giờ đêm)

Tổng thời gian làm việc: ~19 giờ/ngày, so với ~11 giờ của khung cũ.

Mốc 15:30 không phải số mới: `_v10990_deploy.py` đã dùng đúng mốc này từ 05/08
(`HAN_CHOT = (15, 30)`, chú thích *"khung cấm 15:30–18:15"*).

RỦI RO CÒN LẠI — nói rõ, không giấu
===================================
Bảng `predictions` có hai cụm gọi model nữa: **09h–10h** (627 lượt/14 ngày) và
**21h–22h** (507 lượt). Hai cụm này nằm TRONG khung cho phép. Restart lúc đó có thể
làm mất vài dòng `predictions` của lane đo, **nhưng không mất bundle official** — MN đã
xong từ sáng sớm, MT/MB chưa tới lượt. Đây là đánh đổi có ý thức để owner có giờ làm việc.

NGÀY CODE/FIX DO OWNER CHỈ ĐỊNH
===============================
Owner có thể tuyên bố một ngày là ngày dành riêng cho code/fix. Ngày đó khung giờ không
áp. Khai báo trong `docs/NGAY_CODE_FIX.json` — **tệp, không phải cờ dòng lệnh**: có ngày,
có lời owner nguyên văn, xem lại được, không giống hành vi lách cổng.
"""
from __future__ import annotations

import io
import json
import os
from datetime import datetime, time
from zoneinfo import ZoneInfo

VN = ZoneInfo("Asia/Ho_Chi_Minh")
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(os.path.dirname(_HERE))
TEP_NGAY = os.path.join(_REPO, "docs", "NGAY_CODE_FIX.json")

# (bắt đầu, kết thúc, vì sao) — giờ VN
KHUNG_CAM = [
    (time(3, 45), time(6, 0), "MN sinh số (đo 60 ngày: bundle ra 04:16–05:20)"),
    (time(15, 30), time(18, 15), "MN chốt 15:45 → MT 16:58 → MB 17:58, để live chạy cho xong"),
]


def ngay_code_fix(ngay: str | None = None) -> dict | None:
    """Owner có tuyên bố ngày này là ngày code/fix không? Trả dict khai báo, hoặc None."""
    ngay = ngay or datetime.now(VN).strftime("%Y-%m-%d")
    try:
        ds = json.loads(io.open(TEP_NGAY, encoding="utf-8").read())
    except Exception:
        return None
    m = (ds.get("ngay") or {}).get(ngay)
    return {"ngay": ngay, **m} if isinstance(m, dict) else None


def duoc_deploy(luc: datetime | None = None) -> tuple[bool, str]:
    """Trả (được hay không, lý do đọc được cho người)."""
    luc = luc or datetime.now(VN)
    kb = ngay_code_fix(luc.strftime("%Y-%m-%d"))
    if kb:
        return True, ("NGÀY CODE/FIX do owner chỉ định (%s) — khung giờ không áp.\n"
                      "  Owner: «%s»" % (kb["ngay"], kb.get("nguyen_van", "")[:200]))
    t = luc.time()
    for tu, den, vi_sao in KHUNG_CAM:
        if tu <= t < den:
            return False, ("%s giờ VN nằm trong khung CẤM %s–%s — %s.\n"
                           "  Khung cho phép: 06:00–15:30 và 18:15–03:45."
                           % (luc.strftime("%H:%M"), tu.strftime("%H:%M"),
                              den.strftime("%H:%M"), vi_sao))
    return True, "%s giờ VN — ngoài mọi khung cấm" % luc.strftime("%H:%M")


def mo_ta() -> str:
    d = ["Khung CẤM deploy (giờ VN):"]
    for tu, den, vs in KHUNG_CAM:
        d.append("  %s–%s  %s" % (tu.strftime("%H:%M"), den.strftime("%H:%M"), vs))
    d.append("Cho phép: 06:00–15:30 · 18:15–03:45")
    return "\n".join(d)


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    print(mo_ta())
    ok, ly = duoc_deploy()
    print("\n%s %s" % ("✓ ĐƯỢC DEPLOY —" if ok else "✗ KHÔNG được deploy —", ly))
    print("[cong] DUOC_DEPLOY=%s" % ("CO" if ok else "KHONG"))
