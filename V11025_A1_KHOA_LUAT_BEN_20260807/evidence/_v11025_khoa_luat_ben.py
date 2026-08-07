# -*- coding: utf-8 -*-
"""V11025 (A1) — KHOÁ LUẬT BỀN: giữ được bằng chứng ĐO TIẾN qua mỗi lần đào lại.

═══════════════════════════════════════════════════════════════════════════════
VÌ SAO CÓ TỆP NÀY
═══════════════════════════════════════════════════════════════════════════════

Tra soát V11024 (07/08/2026) đo ra: **bộ đếm đo tiến bị xoá mỗi thứ Hai**.

`weekly_rule_miner.run_weekly_mining()` Step 4 làm hai việc:

    c.execute("DELETE FROM mined_rule_effectiveness WHERE date >= date('now','-112 days')")
    backfill_mined_rules(112)

Ý định ghi trong chú thích là đúng — *"Rebuild recent effectiveness window so new rule_ids keep
livingness/tracking continuity"*. Vấn đề nằm ở **gốc**: `_seed_rules.py:432` chạy
`DELETE FROM mined_rules` rồi INSERT lại, nên **`rule_id` đổi hết mỗi tuần**. Không có cách nào
nối bằng chứng cũ với luật mới ⇒ giải pháp cũ là **xoá sạch rồi chấm lại bằng hindsight**.

**Hậu quả đo được:**
- Mỗi thứ Hai, **1.680 dòng** bằng chứng bị xoá và thay bằng dòng chấm ngược.
- Số lượt ĐO TIẾN **không bao giờ vượt 35/miền** — nó bị bấm về 0 mỗi 7 ngày.
- Toàn bộ 105 luật cộng lại chỉ có **75 lượt** đo tiến, **0/105** đạt ngưỡng n≥20.
- Mọi kế hoạch dạng *"đo thêm N ngày rồi kết luận"* — kể cả FU-284, FU-325 — **vĩnh viễn không
  về đích**. Đây không phải "chưa đủ mẫu", là **bất khả thi về cấu trúc**.

═══════════════════════════════════════════════════════════════════════════════
CÁCH SỬA
═══════════════════════════════════════════════════════════════════════════════

**Không đụng `rule_id`** (nhiều chỗ đang đọc nó). Thay vào đó cấp cho mỗi luật một **KHOÁ BỀN**
không đổi qua các lần đào — chính là bộ sáu cột định danh nghiệp vụ của luật:

    (miền đích, thứ đích, đài nguồn, miền nguồn, lệch ngày, bộ giải)

Đo 07/08: **105 luật active → 105 khoá phân biệt**, tức khoá này **duy nhất**, dùng được.

Ba thứ dựng thêm:

1. **`rule_key_registry`** — sổ CHỈ THÊM, không bao giờ xoá. Ghi lần đầu tiên mỗi khoá xuất hiện.
   Đây là "ngày sinh thật" của một luật, thứ mà `mined_at` không cho biết vì nó bị đặt lại mỗi
   tuần.
2. **`mined_rule_effectiveness.rule_key`** + **`.giai_doan`** — mỗi dòng bằng chứng tự khai nó là
   `DO_TIEN` (ngày chấm ≥ ngày luật ra đời) hay `CHAM_NGUOC` (chấm vào quá khứ trước khi luật tồn
   tại). Suy ra được từ dữ liệu, không phụ thuộc lúc ghi.
3. **Step 4 mới**: thay `DELETE 112 ngày + backfill` bằng **NỐI LẠI + LẤP CHỖ TRỐNG**:
   - nối dòng cũ sang `rule_id` mới **theo khoá bền** (đúng mục tiêu ban đầu của Step 4)
   - **TUYỆT ĐỐI KHÔNG xoá dòng `DO_TIEN`** — đó là bằng chứng duy nhất không mua lại được
   - chỉ chấm lại những (ngày, khoá) **chưa có dòng nào**

**Điều thành thật phải ghi:** các luật đang có **không** biết ngày sinh thật, vì bảng lưu luật cũ
không tồn tại (`archived_previous` chỉ dùng để ghi log). Nên lần đầu chạy, sổ khoá sẽ **gieo
mầm** (`SEED_*`) từ bằng chứng sớm nhất còn lại. Chỉ những khoá xuất hiện **từ lần đào sau trở
đi** mới có ngày sinh `OBSERVED` — tức chắc chắn. Cột `nguon_lan_dau` nói rõ cái nào là cái nào.
"""
from __future__ import annotations

import sqlite3
from datetime import datetime

# Sáu cột định danh nghiệp vụ. Đổi bộ này là đổi định nghĩa "cùng một luật" — phải đổi có ý thức.
COT_KHOA = ("target_region", "target_weekday", "source_station_slot|source_station",
            "source_region", "source_offset", "prize_keys")

DDL_REGISTRY = """
CREATE TABLE IF NOT EXISTS rule_key_registry (
    rule_key       TEXT PRIMARY KEY,
    lan_dau_thay   TEXT NOT NULL,     -- ngày đầu tiên khoá này được thấy
    nguon_lan_dau  TEXT NOT NULL,     -- OBSERVED | SEED_TU_MRE | SEED_TU_MINED_AT
    lan_cuoi_thay  TEXT NOT NULL,
    so_lan_dao     INTEGER NOT NULL DEFAULT 1,
    mo_ta          TEXT,
    created_at     TEXT NOT NULL,
    updated_at     TEXT NOT NULL
);
"""


def khoa_luat(target_region, target_weekday, source_station_slot, source_station,
              source_region, source_offset, prize_keys) -> str:
    """Khoá bền của một luật. Cùng khoá = cùng một luật, dù `rule_id` có đổi bao nhiêu lần."""
    dai = (source_station_slot or source_station or "").strip()
    return "|".join([
        str(target_region or "").strip(),
        str(target_weekday if target_weekday is not None else ""),
        dai,
        str(source_region or "").strip(),
        str(source_offset or "").strip(),
        str(prize_keys or "").strip(),
    ])


def _co_cot(con: sqlite3.Connection, bang: str, cot: str) -> bool:
    return any(r[1] == cot for r in con.execute(f"PRAGMA table_info({bang})"))


def nang_cap_luoc_do(con: sqlite3.Connection) -> dict:
    """Thêm cột/bảng còn thiếu. Chạy được nhiều lần, không hỏng gì."""
    ra = {"them_cot": [], "them_bang": []}
    con.execute(DDL_REGISTRY)
    ra["them_bang"].append("rule_key_registry")
    for cot, kieu in (("rule_key", "TEXT"), ("giai_doan", "TEXT")):
        if not _co_cot(con, "mined_rule_effectiveness", cot):
            con.execute(f"ALTER TABLE mined_rule_effectiveness ADD COLUMN {cot} {kieu}")
            ra["them_cot"].append(cot)
    con.execute("CREATE INDEX IF NOT EXISTS idx_mre_rule_key "
                "ON mined_rule_effectiveness(rule_key, date)")
    return ra


def _khoa_tu_dong_mre(r) -> str:
    return khoa_luat(r["target_region"], r["weekday"], r["source_station_slot"],
                     r["source_station"], r["source_region"], r["source_offset"],
                     r["prize_keys"])


def dien_khoa_cho_mre(con: sqlite3.Connection) -> int:
    """Điền `rule_key` cho mọi dòng MRE còn trống. Suy ra từ chính các cột đã có."""
    con.row_factory = sqlite3.Row
    n = 0
    for r in con.execute("SELECT id, target_region, weekday, source_station_slot, "
                         "source_station, source_region, source_offset, prize_keys "
                         "FROM mined_rule_effectiveness WHERE rule_key IS NULL").fetchall():
        con.execute("UPDATE mined_rule_effectiveness SET rule_key=? WHERE id=?",
                    (_khoa_tu_dong_mre(r), r["id"]))
        n += 1
    return n


def gieo_mam_registry(con: sqlite3.Connection) -> dict:
    """Gieo mầm sổ khoá từ bằng chứng còn lại.

    Bảng lưu luật cũ KHÔNG tồn tại, nên với khoá đã có sẵn ta chỉ biết được cận trên của ngày
    sinh: ngày chấm sớm nhất trong MRE, hoặc `mined_at` — lấy cái SỚM HƠN. Ghi rõ là SEED.
    """
    con.row_factory = sqlite3.Row
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hom_nay = datetime.now().strftime("%Y-%m-%d")
    ra = {"moi": 0, "da_co": 0, "seed_tu_mre": 0, "seed_tu_mined_at": 0}

    som_nhat = {}
    for r in con.execute("SELECT rule_key, MIN(date) d FROM mined_rule_effectiveness "
                         "WHERE rule_key IS NOT NULL GROUP BY rule_key"):
        som_nhat[r["rule_key"]] = r["d"]

    for r in con.execute("SELECT target_region, target_weekday, source_station_slot, "
                         "source_station, source_region, source_offset, prize_keys, mined_at "
                         "FROM mined_rules WHERE is_active=1").fetchall():
        k = khoa_luat(r["target_region"], r["target_weekday"], r["source_station_slot"],
                      r["source_station"], r["source_region"], r["source_offset"],
                      r["prize_keys"])
        cu = con.execute("SELECT rule_key FROM rule_key_registry WHERE rule_key=?", (k,)).fetchone()
        if cu:
            con.execute("UPDATE rule_key_registry SET lan_cuoi_thay=?, so_lan_dao=so_lan_dao+1, "
                        "updated_at=? WHERE rule_key=?", (hom_nay, now, k))
            ra["da_co"] += 1
            continue
        mined = str(r["mined_at"] or "")[:10] or hom_nay
        tu_mre = som_nhat.get(k)
        if tu_mre and tu_mre < mined:
            dau, nguon = tu_mre, "SEED_TU_MRE"
            ra["seed_tu_mre"] += 1
        else:
            dau, nguon = mined, "SEED_TU_MINED_AT"
            ra["seed_tu_mined_at"] += 1
        con.execute("INSERT INTO rule_key_registry (rule_key, lan_dau_thay, nguon_lan_dau, "
                    "lan_cuoi_thay, so_lan_dao, mo_ta, created_at, updated_at) "
                    "VALUES (?,?,?,?,1,?,?,?)",
                    (k, dau, nguon, hom_nay,
                     "gieo mầm V11025 — bảng lưu luật cũ không tồn tại nên đây là CẬN TRÊN "
                     "của ngày sinh, không phải ngày sinh chắc chắn", now, now))
        ra["moi"] += 1
    return ra


def ghi_nhan_lan_dao(con: sqlite3.Connection) -> dict:
    """Gọi ở MỖI lần đào. Khoá mới ⇒ OBSERVED (ngày sinh CHẮC CHẮN). Khoá cũ ⇒ bump."""
    con.row_factory = sqlite3.Row
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hom_nay = datetime.now().strftime("%Y-%m-%d")
    ra = {"khoa_moi_observed": 0, "khoa_cu": 0}
    for r in con.execute("SELECT target_region, target_weekday, source_station_slot, "
                         "source_station, source_region, source_offset, prize_keys "
                         "FROM mined_rules WHERE is_active=1").fetchall():
        k = khoa_luat(r["target_region"], r["target_weekday"], r["source_station_slot"],
                      r["source_station"], r["source_region"], r["source_offset"],
                      r["prize_keys"])
        if con.execute("SELECT 1 FROM rule_key_registry WHERE rule_key=?", (k,)).fetchone():
            con.execute("UPDATE rule_key_registry SET lan_cuoi_thay=?, so_lan_dao=so_lan_dao+1, "
                        "updated_at=? WHERE rule_key=?", (hom_nay, now, k))
            ra["khoa_cu"] += 1
        else:
            con.execute("INSERT INTO rule_key_registry (rule_key, lan_dau_thay, nguon_lan_dau, "
                        "lan_cuoi_thay, so_lan_dao, mo_ta, created_at, updated_at) "
                        "VALUES (?,?, 'OBSERVED', ?, 1, ?, ?, ?)",
                        (k, hom_nay, hom_nay,
                         "thấy lần đầu ở đúng lần đào này — ngày sinh CHẮC CHẮN", now, now))
            ra["khoa_moi_observed"] += 1
    return ra


def phan_loai_giai_doan(con: sqlite3.Connection) -> dict:
    """Gán `giai_doan` cho mọi dòng MRE.

    ═══ VÌ SAO KHÔNG DÙNG `lan_dau_thay` LÀM MỐC ═══

    Bản đầu của hàm này gán `DO_TIEN` khi `date >= lan_dau_thay`. Thử khô cho ra
    **DO_TIEN 2.437 · CHAM_NGUOC 0** — nghe như thắng lớn, nhưng đó là **thắng lợi giả**:
    với khoá gieo mầm, `lan_dau_thay` được lấy bằng CHÍNH ngày chấm sớm nhất trong MRE, nên
    mọi dòng đương nhiên `>=` nó. Phép đo tự khen chính mình.

    Sự thật: với khoá gieo mầm, ta **không chứng minh được** luật đã tồn tại trước ngày đó hay
    được chọn ra bằng chính dữ liệu ngày đó. Bảng lưu luật cũ không tồn tại. Không biết thì phải
    nói là không biết.

    ═══ BA NHÃN ═══

    `DO_TIEN`              ngày chấm >= `moc_chac_chan` — luật CHẮC CHẮN đã tồn tại trước ngày đó
    `KHONG_XAC_MINH_DUOC`  khoá có trong sổ nhưng ngày chấm nằm TRƯỚC mốc chắc chắn ⇒ không có
                           cách nào biết nó là đo tiến hay chấm ngược. **Không được đếm là đo tiến.**
    `KHONG_RO_LUAT`        khoá không còn trong sổ (luật đã biến mất khỏi bộ hiện hành)

    `moc_chac_chan` = ngày mà ta BẮT ĐẦU biết chắc:
      · khoá `OBSERVED`  ⇒ chính `lan_dau_thay` (thấy lần đầu ở một lần đào có thật)
      · khoá `SEED_*`    ⇒ ngày gieo mầm (`created_at`) — từ hôm đó trở đi mới đếm được

    ⇒ Ngay sau khi vá, số ĐO TIẾN sẽ gần **0**. Đó là con số ĐÚNG. Nó bắt đầu tăng từ ngày mai
    và **không bị xoá nữa** — đó mới là thứ phép vá này mua được.
    """
    con.row_factory = sqlite3.Row
    moc = {}
    for r in con.execute("SELECT rule_key, lan_dau_thay, nguon_lan_dau, created_at "
                         "FROM rule_key_registry"):
        moc[r["rule_key"]] = (r["lan_dau_thay"] if r["nguon_lan_dau"] == "OBSERVED"
                              else str(r["created_at"])[:10])
    ra = {"DO_TIEN": 0, "KHONG_XAC_MINH_DUOC": 0, "KHONG_RO_LUAT": 0}
    for r in con.execute("SELECT id, rule_key, date FROM mined_rule_effectiveness").fetchall():
        m = moc.get(r["rule_key"])
        if not m:
            g = "KHONG_RO_LUAT"
        elif r["date"] >= m:
            g = "DO_TIEN"
        else:
            g = "KHONG_XAC_MINH_DUOC"
        con.execute("UPDATE mined_rule_effectiveness SET giai_doan=? WHERE id=?", (g, r["id"]))
        ra[g] += 1
    return ra


def noi_lai_rule_id(con: sqlite3.Connection) -> dict:
    """Nối dòng bằng chứng cũ sang `rule_id` MỚI theo khoá bền.

    Đây chính là mục tiêu mà Step 4 cũ muốn đạt — nhưng đạt bằng cách XOÁ rồi chấm lại.
    Nối lại giữ nguyên bằng chứng, kể cả bằng chứng đo tiến.
    """
    con.row_factory = sqlite3.Row
    ban_do = {}
    for r in con.execute("SELECT id, target_region, target_weekday, source_station_slot, "
                         "source_station, source_region, source_offset, prize_keys "
                         "FROM mined_rules WHERE is_active=1").fetchall():
        ban_do[khoa_luat(r["target_region"], r["target_weekday"], r["source_station_slot"],
                         r["source_station"], r["source_region"], r["source_offset"],
                         r["prize_keys"])] = r["id"]
    n = 0
    for k, rid in ban_do.items():
        cur = con.execute("UPDATE mined_rule_effectiveness SET rule_id=? "
                          "WHERE rule_key=? AND rule_id<>?", (rid, k, rid))
        n += cur.rowcount or 0
    return {"dong_noi_lai": n, "khoa_hien_hanh": len(ban_do)}


def thong_ke(con: sqlite3.Connection) -> dict:
    con.row_factory = sqlite3.Row
    r = con.execute("SELECT giai_doan, COUNT(*) n, COUNT(DISTINCT rule_key) k "
                    "FROM mined_rule_effectiveness GROUP BY giai_doan").fetchall()
    ra = {x["giai_doan"] or "(trống)": {"dong": x["n"], "khoa": x["k"]} for x in r}
    du = con.execute("SELECT COUNT(*) FROM (SELECT rule_key FROM mined_rule_effectiveness "
                     "WHERE giai_doan='DO_TIEN' GROUP BY rule_key HAVING COUNT(*)>=20)").fetchone()[0]
    ra["_khoa_du_mau_do_tien_n20"] = du
    ra["_so_khoa_trong_so"] = con.execute("SELECT COUNT(*) FROM rule_key_registry").fetchone()[0]
    return ra
