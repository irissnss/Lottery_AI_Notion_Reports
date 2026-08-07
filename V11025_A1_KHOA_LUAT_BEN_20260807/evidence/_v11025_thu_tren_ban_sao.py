# -*- coding: utf-8 -*-
"""V11025 — THỬ KHÔ trên BẢN SAO của DB. Không đụng bản thật một chữ nào.

Mô phỏng đúng thứ tự sẽ chạy thật:
  1. nâng cấp lược đồ · 2. điền khoá cho MRE · 3. gieo mầm sổ khoá ·
  4. phân loại giai đoạn · 5. nối lại rule_id
Rồi MÔ PHỎNG một lần đào lại (đổi hết rule_id như `_seed_rules` vẫn làm) và kiểm:
  - cách CŨ mất bao nhiêu bằng chứng
  - cách MỚI giữ được bao nhiêu
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
GOC = os.path.abspath(os.path.join(H, "..", ".."))
DB = os.path.join(GOC, "data", "lottery_ai.db")

import _v11025_khoa_luat_ben as K  # noqa: E402


def main() -> int:
    tam = tempfile.mkdtemp(prefix="v11025_")
    ban_sao = os.path.join(tam, "thu.db")
    print("=" * 96)
    print("  V11025 — THỬ KHÔ TRÊN BẢN SAO (bản thật KHÔNG bị mở ghi)")
    print("=" * 96)
    shutil.copy2(DB, ban_sao)
    print(f"  chép DB → {ban_sao}  ({os.path.getsize(ban_sao):,} byte)")

    con = sqlite3.connect(ban_sao)
    con.row_factory = sqlite3.Row

    truoc = con.execute("SELECT COUNT(*) FROM mined_rule_effectiveness").fetchone()[0]
    print(f"\n  MRE trước: {truoc:,} dòng")

    print("\n  ── 1. nâng cấp lược đồ " + "─" * 66)
    print("    ", K.nang_cap_luoc_do(con))
    print("  ── 2. điền khoá cho MRE " + "─" * 65)
    print(f"     điền {K.dien_khoa_cho_mre(con):,} dòng")
    print("  ── 3. gieo mầm sổ khoá " + "─" * 66)
    print("    ", K.gieo_mam_registry(con))
    print("  ── 4. phân loại giai đoạn " + "─" * 63)
    print("    ", K.phan_loai_giai_doan(con))
    print("  ── 5. nối lại rule_id " + "─" * 67)
    print("    ", K.noi_lai_rule_id(con))
    con.commit()

    sau = con.execute("SELECT COUNT(*) FROM mined_rule_effectiveness").fetchone()[0]
    print(f"\n  MRE sau: {sau:,} dòng  {'✓ KHÔNG mất dòng nào' if sau == truoc else '✗ MẤT ' + str(truoc - sau)}")
    print("\n  Thống kê:", K.thong_ke(con))

    # ── MÔ PHỎNG MỘT LẦN ĐÀO LẠI ────────────────────────────────────────────────
    print("\n" + "=" * 96)
    print("  MÔ PHỎNG LẦN ĐÀO THỨ HAI TỚI — so cách CŨ với cách MỚI")
    print("=" * 96)

    do_tien_truoc = con.execute(
        "SELECT COUNT(*) FROM mined_rule_effectiveness WHERE giai_doan='DO_TIEN'").fetchone()[0]
    giu_truoc = con.execute(
        "SELECT COUNT(*) FROM mined_rule_effectiveness "
        "WHERE giai_doan IN ('DO_TIEN','KHONG_XAC_MINH_DUOC')").fetchone()[0]
    trong_112 = con.execute(
        "SELECT COUNT(*) FROM mined_rule_effectiveness "
        "WHERE date >= date('now','-112 days')").fetchone()[0]
    do_tien_112 = con.execute(
        "SELECT COUNT(*) FROM mined_rule_effectiveness "
        "WHERE date >= date('now','-112 days') AND giai_doan='DO_TIEN'").fetchone()[0]

    print(f"  CÁCH CŨ  — DELETE date>=now-112d : xoá {trong_112:,} dòng, "
          f"trong đó {do_tien_112:,} dòng ĐO TIẾN mất hẳn")

    # đổi hết rule_id giống _seed_rules (id mới = id cũ + 100000)
    con.execute("UPDATE mined_rules SET id = id + 100000 WHERE is_active=1")
    con.commit()
    lech = con.execute(
        "SELECT COUNT(*) FROM mined_rule_effectiveness e "
        "WHERE NOT EXISTS (SELECT 1 FROM mined_rules r WHERE r.id=e.rule_id)").fetchone()[0]
    print(f"  sau khi đổi hết rule_id: {lech:,} dòng MRE mồ côi (đây là lý do Step 4 cũ phải xoá)")

    noi = K.noi_lai_rule_id(con)
    con.commit()
    lech2 = con.execute(
        "SELECT COUNT(*) FROM mined_rule_effectiveness e "
        "WHERE NOT EXISTS (SELECT 1 FROM mined_rules r WHERE r.id=e.rule_id)").fetchone()[0]
    do_tien_sau = con.execute(
        "SELECT COUNT(*) FROM mined_rule_effectiveness WHERE giai_doan='DO_TIEN'").fetchone()[0]
    sau2 = con.execute("SELECT COUNT(*) FROM mined_rule_effectiveness").fetchone()[0]

    print(f"  CÁCH MỚI — nối lại theo khoá bền : nối {noi['dong_noi_lai']:,} dòng · "
          f"còn mồ côi {lech2:,}")
    print(f"                                     MRE {sau2:,} dòng (giữ nguyên) · "
          f"ĐO TIẾN {do_tien_sau:,} (trước {do_tien_truoc:,})")

    giu_sau = con.execute(
        "SELECT COUNT(*) FROM mined_rule_effectiveness "
        "WHERE giai_doan IN ('DO_TIEN','KHONG_XAC_MINH_DUOC')").fetchone()[0]
    print(f"                                     bằng chứng giữ lại {giu_sau:,} "
          f"(trước {giu_truoc:,})")
    dat = (sau2 == truoc and do_tien_sau == do_tien_truoc and giu_sau == giu_truoc and lech2 < lech)
    print()
    print("  " + ("✓ ĐẠT — không mất dòng nào, bằng chứng đo tiến còn nguyên, hết mồ côi"
                  if dat else "✗ KHÔNG ĐẠT — xem lại"))
    con.close()
    shutil.rmtree(tam, ignore_errors=True)
    print(f"\n  đã xoá bản sao. DB thật mtime giữ nguyên: "
          f"{__import__('datetime').datetime.fromtimestamp(os.stat(DB).st_mtime):%Y-%m-%d %H:%M:%S}")
    return 0 if dat else 1


if __name__ == "__main__":
    raise SystemExit(main())
