# -*- coding: utf-8 -*-
"""V11013 — XẾP LẠI HẠN cho các mục agent tự mở (FU-286 … FU-313).

Owner 07/08: "cái gì mà đợi tới 24/12 hết năm kiểu này… cân đối thời gian hạn mốc
tương đối ổn hơn đẹp hơn đi"

Hai việc:
  1. FU-286: 24/12 → 27/08. Vì câu hỏi đang chặn quyết định là câu hỏi LỚP
     ("cơ chế mined_rules có lợi thế không") — câu đó GỘP được 105 luật, nhịp 15
     dòng/ngày, đủ 332 cặp để phát hiện chênh 10 điểm vào 27/08. Cổng cũ đòi n≥20
     CHO MỖI LUẬT nên mới ra 140 ngày — đó là câu hỏi TỈA TỪNG LUẬT, chưa cần tới.
  2. Rải 16 mục dồn 13/08 (15 trong đó do agent tự đặt) ra theo mức ưu tiên thật.

CHỈ đổi hạn các mục agent tự mở. KHÔNG đụng mục của phiên khác.
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
P = "docs/FOLLOW_UP_TRACKER.md"

# mã → (hạn mới DD/MM, mã đọc mới, lý do xếp vào ngày đó)
LICH = {
    # ── 08/08 · CHẶN QUYẾT ĐỊNH hoặc NGĂN TÁI PHẠM ──
    "FU-290": ("08/08", "QD0808", "owner ký — bằng chứng đã đủ"),
    "FU-303": ("08/08", "KS0808", "cổng ngăn tái phạm đo trên dữ liệu cũ — để lâu là còn đo sai"),
    "FU-311": ("08/08", "TK0808", "đính chính V10857 — đang là căn cứ giữ RULES-FIRST"),
    "FU-312": ("08/08", "SC0808", "MB lane sớm 20 phút, mỗi ngày trôi là một ngày đo hụt"),
    # ── 10/08 · SỬA THƯỚC ──
    "FU-304": ("10/08", "TK1008", "đính chính DO_TIEN"),
    "FU-294": ("10/08", "KS1008", "cổng quét theo thực thể"),
    "FU-310": ("10/08", "SC1008", "cổng QD-027 dung sai giờ"),
    # ── 12/08 · LÀM RÕ SỐ CŨ ──
    "FU-307": ("12/08", "DO1208", "định nghĩa gốc 57/90"),
    "FU-308": ("12/08", "TK1208", "V10770 SUPERSEDED"),
    # ── 14/08 · CỔNG VÀ DỌN ──
    "FU-288": ("14/08", "KS1408", "nâng 3 diễn tập lên CHẠY THẬT"),
    "FU-289": ("14/08", "DD1408", "56 mục không ghi hạn"),
    "FU-296": ("14/08", "KS1408-1", "cổng luật cứng trỏ lớp chết"),
    # ── 17/08 · HẠ TẦNG ĐO ──
    "FU-292": ("17/08", "KS1708", "cảnh gác tên đài vào cron"),
    "FU-301": ("17/08", "SC1708", "chuẩn hoá múi giờ"),
    "FU-306": ("17/08", "TK1708", "sơ đồ đường đi của một luật"),
    # ── 19/08 · RÀ DIỆN RỘNG ──
    "FU-277": ("19/08", "KS1908", "mở rộng 3 nhánh dữ liệu nhiễm"),
    "FU-309": ("19/08", "DD1908", "hơn 40 bảng cũ"),
    "FU-302": ("19/08", "TK1908", "ký hiệu P&L_mô_phỏng"),
    # ── 21/08 · CHỜ OWNER + CỔNG DÀI HẠN ──
    "FU-295": ("21/08", "QD2108", "owner quyết rule_custom_prompt"),
    "FU-313": ("21/08", "KS2108", "cổng chặn kết luận trước/sau thiếu nền"),
    # ── ĐO DÀI — theo mốc đo thật, không phải đặt bừa ──
    "FU-286": ("27/08", "DO2708", "ĐỔI THIẾT KẾ: hỏi cả LỚP thay vì từng luật · "
                                  "332 cặp đủ phát hiện chênh 10 điểm · nhịp 15 dòng/ngày"),
}

t = io.open(P, encoding="utf-8").read()
n0 = len(t)
doi, khong = [], []

for ma, (han, madoc, ly) in LICH.items():
    # tiêu đề dạng: ### FU-xxx · MÃĐỌC · nhãn · hạn DD/MM
    pat = re.compile(r"^(### " + re.escape(ma) + r" · )([^·\n]+)( · )(.*?)( · hạn [^\n]+)$",
                     re.M)
    m = pat.search(t)
    if not m:
        khong.append(ma)
        continue
    cu_han = m.group(5).replace(" · hạn ", "")
    if cu_han.strip() == han:
        doi.append(f"{ma}: giữ {han}")
        continue
    moi = f"{m.group(1)}{madoc}{m.group(3)}{m.group(4)} · hạn {han}"
    t = t[:m.start()] + moi + t[m.end():]
    doi.append(f"{ma}: {cu_han} → {han}  ({ly})")

io.open(P, "w", encoding="utf-8").write(t)
print(f"{n0:,} → {len(t):,}")
print(f"\nĐÃ ĐỔI {len([x for x in doi if '→' in x])} mục:")
for x in doi:
    print("  ", x)
if khong:
    print(f"\nKHÔNG KHỚP TIÊU ĐỀ ({len(khong)}): {', '.join(khong)}")
