# -*- coding: utf-8 -*-
"""V11023 (FU-328) — CANH MODEL RA THIẾU SỐ.

**Vì sao có cổng này.** Ngày 07/08, `deepseek-reasoner` ra **rỗng** ở MT. Bundle vẫn dựng, vẫn
`ACTIVE`, `/api/health` vẫn 200, cả 16 phép tự kiểm vẫn xanh — **không một chỗ nào báo**. Chỉ
thiếu một lá phiếu, im lặng. Owner phải tự chỉ ra.

Đó là kiểu hỏng nguy hiểm nhất: **không có gì sai rõ ràng, chỉ có ít hơn bình thường** — mà
không ai biết bình thường là bao nhiêu.

**Nền để so (30 ngày, đường official):** hầu hết model ra **2 số** mọi lượt.
`deepseek-reasoner` 88/93 · `claude-sonnet-4-6` 89/93 · `xgboost` 93/93.

**Ngưỡng báo động — chốt trước:**

| mức | điều kiện |
|---|---|
| `DO` | ≥1 model ra **RỖNG** ở một miền |
| `DO` | ≥3 model ra **1 số** ở một miền |
| `VANG` | 1–2 model ra 1 số |
| `XANH` | mọi model ra đủ 2 số |

CHỈ ĐỌC — không sửa gì, không ghi vào bảng khoá.
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

H = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(H, "..", "..", "data", "lottery_ai.db")
MIEN = ("MN", "MT", "MB")

NGUONG_RONG = 1      # ≥1 model ra rỗng ⇒ ĐỎ
NGUONG_MOT_SO = 3    # ≥3 model ra 1 số ⇒ ĐỎ


def _con():
    return sqlite3.connect(f"file:{os.path.abspath(DB)}?mode=ro", uri=True)


def soi(ngay: str | None = None) -> dict:
    ngay = ngay or datetime.now().strftime("%Y-%m-%d")
    con = _con()
    con.row_factory = sqlite3.Row
    ra = {"ngay": ngay, "mien": {}, "muc": "XANH", "canh_bao": []}
    for m in MIEN:
        rows = list(con.execute(
            "SELECT ai_model, main_numbers FROM predictions "
            "WHERE date=? AND target_region=? "
            "  AND COALESCE(run_source,'') <> 'shadow_auto_eval' "
            "  AND COALESCE(phase_type,'') <> 'shadow_eval'", (ngay, m)))
        if not rows:
            continue
        rong, mot, hai = [], [], 0
        for r in rows:
            try:
                v = json.loads(r["main_numbers"] or "[]")
            except Exception:
                v = []
            if not v:
                rong.append(r["ai_model"])
            elif len(v) == 1:
                mot.append(r["ai_model"])
            else:
                hai += 1
        muc = ("DO" if (len(rong) >= NGUONG_RONG or len(mot) >= NGUONG_MOT_SO)
               else "VANG" if mot else "XANH")
        ra["mien"][m] = {"tong": len(rows), "hai_so": hai,
                         "mot_so": mot, "rong": rong, "muc": muc}
        if muc == "DO":
            ra["muc"] = "DO"
            if rong:
                ra["canh_bao"].append(
                    f"{m}: {len(rong)} model ra RỖNG — {', '.join(rong)}")
            if len(mot) >= NGUONG_MOT_SO:
                ra["canh_bao"].append(
                    f"{m}: {len(mot)} model chỉ ra 1 số — {', '.join(mot)}")
        elif muc == "VANG" and ra["muc"] == "XANH":
            ra["muc"] = "VANG"
            ra["canh_bao"].append(f"{m}: {len(mot)} model ra 1 số — {', '.join(mot)}")
    con.close()
    return ra


def main() -> int:
    kq = soi(sys.argv[1] if len(sys.argv) > 1 and "-" in sys.argv[1] else None)
    bieu = {"XANH": "✓", "VANG": "⚠", "DO": "✗"}
    print("=" * 92)
    print(f"  CANH MODEL RA THIẾU SỐ — ngày {kq['ngay']}   [{bieu[kq['muc']]} {kq['muc']}]")
    print("=" * 92)
    if not kq["mien"]:
        print("  (chưa có dự đoán nào cho ngày này)")
        return 0
    print(f"  {'miền':6} {'model':>6} {'đủ 2 số':>8} {'1 số':>6} {'rỗng':>6}   mức")
    for m, v in kq["mien"].items():
        print(f"  {m:6} {v['tong']:>6} {v['hai_so']:>8} {len(v['mot_so']):>6} "
              f"{len(v['rong']):>6}   {bieu[v['muc']]} {v['muc']}")
    if kq["canh_bao"]:
        print()
        for c in kq["canh_bao"]:
            print(f"  {bieu[kq['muc']]} {c}")
        print()
        print("  Ngưỡng: ≥1 model RỖNG hoặc ≥3 model ra 1 số ⇒ ĐỎ.")
        print("  Ca 07/08: deepseek-reasoner ra rỗng ở MT mà KHÔNG cổng nào báo — sinh ra cổng này.")
    else:
        print("\n  ✓ Mọi model đều ra đủ số.")
    return 1 if kq["muc"] == "DO" else 0


if __name__ == "__main__":
    raise SystemExit(main())
