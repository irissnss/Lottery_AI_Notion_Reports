# -*- coding: utf-8 -*-
"""V11017 — ĐO BẦY ĐÀN: bao nhiêu model chốt, ra bao nhiêu SỐ CHÍNH khác nhau.

Owner nguyên văn (07/08): *"đừng output theo số gò như thế dẫn đến bầy đàn là đúng rồi, lùa vào
1 bộ số định sẵn trong ngày để model quyết định xong thấy bầy đàn."*

V11016 (07/08) gỡ cả bốn chỗ đưa rổ số dọn sẵn. Câu hỏi: **có cắt được bầy đàn thật không?**

**Vì sao phải có phép đo NÀY, không đợi phép đo 21/08.**
`FU-287` bắt: mọi thay đổi phải kèm một phép đo **CƠ CHẾ** biết trong **1 ngày**, không chỉ phép
đo **KẾT QUẢ** 14–120 ngày. Độ trúng thì phải đợi; nhưng *"model có còn chốt trùng nhau không"*
thì **sáng mai biết**. Nếu cơ chế không đổi thì phép đo kết quả 21/08 đang đo một thứ vô nghĩa.

**Thước:** mỗi (ngày, miền) — `tỉ lệ phân tán = số SỐ CHÍNH khác nhau / số model chốt`.
- gần **1,00** ⇒ mỗi model một số ⇒ không bầy đàn
- gần **0,10** ⇒ cả làng chốt chung vài số ⇒ bầy đàn nặng

**CHỈ đếm đường official.** Loại `run_source='shadow_auto_eval'` và `phase_type='shadow_eval'` —
gộp vào là thổi số model từ 16 lên 27 và làm tỉ lệ méo.

**Nền đo được trước khi V11016 chạy (01–06/08, 18 lượt miền-ngày):**
15–16 model · tỉ lệ **0,31–0,62** · trung bình **≈0,47**.

An toàn §52: `output_eligible=0 · diagnostic_only=1 · owner_approved=0 · shadow_only=1`.
Bảng này KHÔNG đụng `/du-doan`, KHÔNG đụng writer của `final_bundles`, KHÔNG đụng bộ chọn model.
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
from collections import Counter
from datetime import date, datetime, timedelta

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

H = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(H, "..", "..", "data", "lottery_ai.db")

BANG = "bay_dan_daily_shadow"
MIEN = ("MN", "MT", "MB")

# ── Mốc V11016 vào production ────────────────────────────────────────────────────────
#
# PHẢI là MỐC GIỜ, không phải mốc NGÀY. Bản đầu của tệp này lấy mốc `date(2026,8,7)` và
# lập tức nhiễm bẩn: ba lượt ngày 07/08 được tạo lúc **05:00–05:20**, tức TRƯỚC khi
# V11016 lên máy chủ lúc **13:35:48**, mà vẫn bị gắn nhãn `SAU_V11016`. Sáng hôm sau đọc
# bảng sẽ thấy MN 0,56 và tưởng lời kể có tác dụng — trong khi ba lượt đó chạy prompt CŨ.
#
# Đây đúng cái bẫy đã ghi trong CLAUDE.md: *"cẩn thận cột thời gian"*. Lệch 8 tiếng là đủ
# để kết luận ngược.
MOC_V11016 = datetime(2026, 8, 7, 13, 36, 0)   # gpt_analyzer.py đổi 13:35:48, restart ngay sau

# Một (ngày, miền) có cả bản ghi trước lẫn sau mốc thì KHÔNG xếp vào bên nào — nó là
# HON_HOP và bị loại khỏi cả hai trung bình. Gộp vào là trộn hai prompt trong một con số.
GIAI_DOAN = ("NEN", "SAU_V11016", "HON_HOP")

# Sàn: dưới ngần này model thì tỉ lệ không có ý nghĩa (một hôm hỏng cron chỉ 3 model
# chốt thì tỉ lệ 1,00 mà chẳng nói lên gì).
SAN_MODEL = 8

DDL = f"""
CREATE TABLE IF NOT EXISTS {BANG} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    region TEXT NOT NULL,
    giai_doan TEXT NOT NULL,              -- NEN | SAU_V11016
    n_model INTEGER NOT NULL,
    n_so_khac INTEGER NOT NULL,
    ty_le_phan_tan REAL NOT NULL,         -- n_so_khac / n_model
    cum_lon_nhat TEXT,                    -- số được nhiều model chốt nhất
    so_model_cum_lon INTEGER,
    ty_le_cum_lon REAL,                   -- so_model_cum_lon / n_model
    du_mau INTEGER NOT NULL,              -- 1 nếu n_model >= SAN_MODEL
    output_eligible INTEGER NOT NULL DEFAULT 0,
    diagnostic_only INTEGER NOT NULL DEFAULT 1,
    owner_approved INTEGER NOT NULL DEFAULT 0,
    shadow_only INTEGER NOT NULL DEFAULT 1,
    computed_at TEXT NOT NULL,
    UNIQUE(date, region)
);
"""


def _con(ro: bool = False):
    if ro:
        return sqlite3.connect(f"file:{os.path.abspath(DB)}?mode=ro", uri=True)
    return sqlite3.connect(os.path.abspath(DB), timeout=30)


def _so_chinh(main_numbers) -> str | None:
    """main_numbers lưu dạng JSON '[\"52\", \"83\"]'. Số CHÍNH là phần tử đầu."""
    if not main_numbers:
        return None
    try:
        v = json.loads(main_numbers)
        if isinstance(v, list) and v:
            s = str(v[0]).strip()
            return s if s else None
    except Exception:
        pass
    s = str(main_numbers).strip().strip("[]").split(",")[0].strip().strip('"').strip("'")
    return s or None


def _sau_moc(created_at) -> bool | None:
    """Bản ghi này tạo SAU khi V11016 lên máy chủ chưa? None = không đọc được giờ."""
    if not created_at:
        return None
    s = str(created_at).replace("T", " ")[:19]
    try:
        return datetime.strptime(s, "%Y-%m-%d %H:%M:%S") >= MOC_V11016
    except Exception:
        return None


def _gom(con, tu_ngay: str, den_ngay: str) -> dict[tuple[str, str], dict]:
    """Gom theo (ngày, miền) — kèm phân loại giai đoạn theo GIỜ TẠO từng bản ghi."""
    ra: dict[tuple[str, str], dict] = {}
    cur = con.cursor()
    cur.execute(
        "SELECT date, target_region, main_numbers, created_at FROM predictions "
        "WHERE date >= ? AND date <= ? "
        "  AND COALESCE(run_source,'') <> 'shadow_auto_eval' "
        "  AND COALESCE(phase_type,'') <> 'shadow_eval' "
        "  AND main_numbers IS NOT NULL AND main_numbers <> ''",
        (tu_ngay, den_ngay))
    for ngay, mien, mn, tao_luc in cur.fetchall():
        s = _so_chinh(mn)
        if not s or mien not in MIEN:
            continue
        o = ra.setdefault((ngay, mien), {"so": [], "sau": 0, "truoc": 0, "khong_ro": 0})
        o["so"].append(s)
        v = _sau_moc(tao_luc)
        o["sau" if v is True else "truoc" if v is False else "khong_ro"] += 1
    for o in ra.values():
        # Không đọc được giờ thì coi như TRƯỚC — thà xếp nhầm về nền còn hơn tự khen.
        truoc = o["truoc"] + o["khong_ro"]
        o["giai_doan"] = ("SAU_V11016" if o["sau"] and not truoc
                          else "HON_HOP" if o["sau"] and truoc
                          else "NEN")
    return ra


def compute(so_ngay: int = 21, hom_nay: str | None = None) -> dict:
    """Tính lại và ghi bảng shadow. Trả về số dòng ghi."""
    ht = hom_nay or datetime.now().strftime("%Y-%m-%d")
    tu = (datetime.strptime(ht, "%Y-%m-%d").date() - timedelta(days=so_ngay)).isoformat()

    con = _con()
    con.execute(DDL)
    goi = _gom(con, tu, ht)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    n = 0
    for (ngay, mien), o in sorted(goi.items()):
        ds = o["so"]
        cnt = Counter(ds)
        dong = cnt.most_common(1)[0] if cnt else ("", 0)
        gd = o["giai_doan"]
        con.execute(
            f"INSERT INTO {BANG} (date, region, giai_doan, n_model, n_so_khac, "
            f"ty_le_phan_tan, cum_lon_nhat, so_model_cum_lon, ty_le_cum_lon, du_mau, "
            f"computed_at) VALUES (?,?,?,?,?,?,?,?,?,?,?) "
            f"ON CONFLICT(date, region) DO UPDATE SET "
            f"giai_doan=excluded.giai_doan, n_model=excluded.n_model, "
            f"n_so_khac=excluded.n_so_khac, ty_le_phan_tan=excluded.ty_le_phan_tan, "
            f"cum_lon_nhat=excluded.cum_lon_nhat, so_model_cum_lon=excluded.so_model_cum_lon, "
            f"ty_le_cum_lon=excluded.ty_le_cum_lon, du_mau=excluded.du_mau, "
            f"computed_at=excluded.computed_at",
            (ngay, mien, gd, len(ds), len(cnt), round(len(cnt) / len(ds), 4),
             dong[0], dong[1], round(dong[1] / len(ds), 4),
             1 if len(ds) >= SAN_MODEL else 0, now))
        n += 1
    con.commit()
    con.close()
    return {"so_dong": n, "tu_ngay": tu, "den_ngay": ht}


def _tb(xs):
    return sum(xs) / len(xs) if xs else 0.0


def _do_lech(xs):
    if len(xs) < 2:
        return 0.0
    m = _tb(xs)
    return (sum((x - m) ** 2 for x in xs) / (len(xs) - 1)) ** 0.5


def view() -> dict:
    """CHỈ ĐỌC bảng đã ghi — không tính lại. Dùng cho API và cho panel."""
    con = _con(ro=True)
    con.row_factory = sqlite3.Row
    try:
        rows = [dict(r) for r in con.execute(
            f"SELECT * FROM {BANG} ORDER BY date DESC, region")]
    except sqlite3.OperationalError:
        con.close()
        return {"success": False, "error": f"chưa có bảng {BANG} — chạy compute() trước"}
    con.close()

    du = [r for r in rows if r["du_mau"]]
    nen = [r["ty_le_phan_tan"] for r in du if r["giai_doan"] == "NEN"]
    sau = [r["ty_le_phan_tan"] for r in du if r["giai_doan"] == "SAU_V11016"]
    # HON_HOP = lượt có cả bản ghi trước lẫn sau mốc 13:36 ⇒ trộn hai prompt trong một
    # con số ⇒ LOẠI khỏi cả hai trung bình, chỉ đếm để nói rõ đã bỏ bao nhiêu.
    hon_hop = [r["ty_le_phan_tan"] for r in du if r["giai_doan"] == "HON_HOP"]

    # Ngưỡng chốt TRƯỚC khi đo (07/08) để không bẻ số sau khi thấy kết quả.
    tb_nen, tb_sau = _tb(nen), _tb(sau)
    if not sau:
        ket = "CHUA_DU_DU_LIEU"
        giai_thich = "Chưa có ngày nào sau V11016. Đợi lượt chốt đầu tiên."
    elif len(sau) < 9:
        ket = "CHUA_DU_3_NGAY"
        giai_thich = (f"Mới {len(sau)}/9 lượt miền-ngày sau V11016 (cần 3 ngày × 3 miền). "
                      f"Trung bình tạm: {tb_sau:.2f} so với nền {tb_nen:.2f} — "
                      f"CHƯA KẾT LUẬN ĐƯỢC.")
    elif tb_sau >= 0.50 and tb_sau - tb_nen >= 0.05:
        ket = "CO_TAC_DUNG"
        giai_thich = (f"Phân tán {tb_nen:.2f} → {tb_sau:.2f} (+{tb_sau - tb_nen:.2f}). "
                      f"Đạt ngưỡng ≥0,50 và hơn nền ≥0,05 ⇒ lời kể CÓ cắt được bầy đàn.")
    elif tb_sau <= 0.35:
        ket = "KHONG_TAC_DUNG"
        giai_thich = (f"Phân tán {tb_nen:.2f} → {tb_sau:.2f}. Dưới ngưỡng 0,35 ⇒ lời kể "
                      f"KHÔNG cắt được bầy đàn, và phép đo kết quả 21/08 đang đo thứ vô nghĩa.")
    else:
        ket = "CHUA_RO"
        giai_thich = (f"Phân tán {tb_nen:.2f} → {tb_sau:.2f} — nằm giữa hai ngưỡng "
                      f"(0,35 và 0,50). Chưa phân biệt được, đo tiếp.")

    return {
        "success": True,
        "bang": BANG,
        "an_toan": {"output_eligible": 0, "diagnostic_only": 1,
                    "owner_approved": 0, "shadow_only": 1},
        "thuoc": "tỉ lệ phân tán = số SỐ CHÍNH khác nhau / số model chốt (chỉ đường official)",
        "moc_v11016": MOC_V11016.strftime("%Y-%m-%d %H:%M:%S"),
        "hon_hop": {"n": len(hon_hop),
                    "vi_sao_loai": "lượt có cả bản ghi trước lẫn sau mốc 13:36 — trộn hai "
                                   "prompt trong một con số, không xếp vào bên nào"},
        "san_model": SAN_MODEL,
        "nguong": {"co_tac_dung": ">= 0,50 và hơn nền >= 0,05",
                   "khong_tac_dung": "<= 0,35",
                   "can_it_nhat": "3 ngày × 3 miền = 9 lượt"},
        "nen": {"n": len(nen), "trung_binh": round(tb_nen, 4),
                "do_lech": round(_do_lech(nen), 4),
                "thap_nhat": round(min(nen), 4) if nen else None,
                "cao_nhat": round(max(nen), 4) if nen else None},
        "sau_v11016": {"n": len(sau), "trung_binh": round(tb_sau, 4),
                       "do_lech": round(_do_lech(sau), 4),
                       "thap_nhat": round(min(sau), 4) if sau else None,
                       "cao_nhat": round(max(sau), 4) if sau else None},
        "ket_luan": ket,
        "giai_thich": giai_thich,
        "dong": rows[:45],
    }


if __name__ == "__main__":
    r = compute()
    print(f"  đã ghi {r['so_dong']} dòng · {r['tu_ngay']} → {r['den_ngay']}")
    v = view()
    print(f"\n  {'ngày':11} {'miền':5} {'giai đoạn':11} {'model':>6} {'số khác':>8} "
          f"{'phân tán':>9}  đông nhất")
    for x in v["dong"][:24]:
        print(f"  {x['date']:11} {x['region']:5} {x['giai_doan']:11} {x['n_model']:>6} "
              f"{x['n_so_khac']:>8} {x['ty_le_phan_tan']:>9.2f}  "
              f"{x['cum_lon_nhat']}×{x['so_model_cum_lon']}")
    print(f"\n  NỀN        : n={v['nen']['n']:>3} · trung bình {v['nen']['trung_binh']:.3f} "
          f"± {v['nen']['do_lech']:.3f}")
    print(f"  SAU V11016 : n={v['sau_v11016']['n']:>3} · trung bình "
          f"{v['sau_v11016']['trung_binh']:.3f} ± {v['sau_v11016']['do_lech']:.3f}")
    print(f"\n  ⇒ {v['ket_luan']}: {v['giai_thich']}")
