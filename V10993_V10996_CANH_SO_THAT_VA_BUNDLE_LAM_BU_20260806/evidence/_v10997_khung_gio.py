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

KHUNG MỚI — MỘT CỬA SỔ DUY NHẤT (V10998)
========================================
Owner ban đầu đề xuất chặn từ mốc MN 15:45. Đo 60 ngày thấy đề xuất đó thiếu một cửa sổ:
MN bundle sinh **04:16–05:20**, tức số MN làm từ 4 giờ sáng; mốc 15:45 chỉ là lúc ĐÓNG
BĂNG hiển thị.

Owner giải quyết gọn hơn cách agent đề xuất: **dời hẳn lịch sinh số MN sang 15:00**. Khi
đó chỉ còn MỘT cửa sổ cấm, và thời gian làm việc liền một dải:

    CẤM       15:00 → 18:45    MN sinh số → chốt → MT → MB → kết quả về

    CHO PHÉP  18:45 → 15:00    MỘT dải liền, 20,25 giờ/ngày

So với khung cũ (05:00–18:15, chỉ chừa ~11 giờ ban đêm) thì gần gấp đôi thời gian làm việc,
và quan trọng hơn: **liền một dải**, không phải chia hai mảnh vụn.

PHỤ THUỘC: khung này chỉ ĐÚNG khi lịch MN đã dời sang 15:00
===========================================================
Chừng nào MN còn sinh số lúc 04:16–05:20 thì khung 15:00–18:45 **để hở** đúng lúc MN
đang gọi model. Hai việc phải đi cùng nhau, không được làm một nửa.

Trạng thái: khung đã đổi; **lịch MN CHƯA dời** — còn chờ soi xong 17 job buổi sáng đang
ngầm ăn theo việc MN chạy sớm (xem FU-282). Trong lúc chờ, `docs/NGAY_CODE_FIX.json`
là cách duy nhất được deploy trong khung cấm.

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
# V10998 (owner ký 06/08 ~15:5x): dời lịch sinh số MN từ sáng sớm sang 15:00, nên khung
# cấm 03:45–06:00 KHÔNG còn lý do tồn tại — gộp về MỘT cửa sổ duy nhất.
#
#   Owner: "vậy theo em 15h đi em" — sau khi agent chỉ ra 15:15 sẽ làm hỏng 5 job xếp ở
#   15:36–15:43 (chuỗi MN chậm nhất 21,7 phút → số ra 15:36,7, tức SAU khi job 15:36 nổ).
#   Bắt đầu 15:00 thì số ra 15:18–15:22, năm job kia giữ nguyên, dư 14 phút tới mốc chốt.
#
#   Owner: "bắt đầu block từ 15h15 đến hết 18h45 khoảng thời gian này phục vụ live để kết
#   quả trung thực ổn định" — giữ nguyên ý, chỉ dời mốc đầu về 15:00 cho khớp giờ MN chạy.
KHUNG_CAM = [
    (time(15, 0), time(18, 45),
     "MN sinh số 15:00–15:22 → chốt 15:45 → MT 16:58 → MB 17:58 → kết quả về 18:15, "
     "để live chạy cho xong"),
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
                           "  Khung cho phép: 18:45 → 15:00 hôm sau."
                           % (luc.strftime("%H:%M"), tu.strftime("%H:%M"),
                              den.strftime("%H:%M"), vi_sao))
    return True, "%s giờ VN — ngoài mọi khung cấm" % luc.strftime("%H:%M")


def mo_ta() -> str:
    d = ["Khung CẤM deploy (giờ VN):"]
    for tu, den, vs in KHUNG_CAM:
        d.append("  %s–%s  %s" % (tu.strftime("%H:%M"), den.strftime("%H:%M"), vs))
    d.append("Cho phép: 18:45 → 15:00 hôm sau (một dải liền, 20,25 giờ)")
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
