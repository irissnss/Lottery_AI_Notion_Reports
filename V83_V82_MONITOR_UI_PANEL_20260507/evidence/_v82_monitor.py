"""V82 admin-only read-only monitor payload builder.

Reads shadow / measurement tables and returns a single JSON dict consumed by
`/v82-monitor` admin page. NEVER writes to any table. NEVER touches official
output paths (`predictions`, `final_bundles`, `lottery_results`,
`model_daily_eval`, `du_doan_*` official scoring).

Hard contract:
- read-only
- no scoring
- no candidate selection
- no ranking modification
- output is descriptive JSON only
- consumers can only display, never trigger anything
"""
from __future__ import annotations

import datetime as dt
import json
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

VN = dt.timezone(dt.timedelta(hours=7))
DB_PATH = Path(__file__).resolve().parents[2] / "data" / "lottery_ai.db"
REGIONS = ("MN", "MT", "MB")
NO_TOKEN_IDS = {
    "random-forest", "xgboost", "lstm", "smart-ml", "smart-ensemble",
    "combo-no-token", "combo-super", "meta-learning",
}
SOURCE_DOC = (
    "V82 monitor — read-only shadow surfaces. Official tables UNCHANGED. "
    "No promotion. No selection. Display only."
)


def _conn() -> sqlite3.Connection:
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def _today_vn() -> str:
    return dt.datetime.now(VN).date().isoformat()


def _table_exists(c: sqlite3.Connection, name: str) -> bool:
    return bool(
        c.execute(
            "SELECT 1 FROM sqlite_master WHERE type IN ('table','view') AND name=?",
            (name,),
        ).fetchone()
    )


def _safe_select(c: sqlite3.Connection, sql: str, params: tuple = ()) -> list[dict]:
    try:
        return [dict(r) for r in c.execute(sql, params)]
    except sqlite3.OperationalError as exc:
        return [{"error": str(exc)[:200]}]


def _tail(v: Any) -> str | None:
    if v is None:
        return None
    s = str(v).strip()
    return s[-2:].zfill(2) if s else None


def _walk(v):
    if isinstance(v, dict):
        for x in v.values():
            yield from _walk(x)
    elif isinstance(v, list):
        for x in v:
            yield from _walk(x)
    elif v is not None:
        yield v


def _loads(s, default):
    if s is None:
        return default
    if isinstance(s, (list, dict)):
        return s
    try:
        return json.loads(s)
    except Exception:
        return default


def _actuals_window(c, region: str, days: int) -> dict[str, set[str]]:
    cutoff = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    out: dict[str, set[str]] = {}
    for row in c.execute(
        "SELECT date, prizes_json FROM lottery_results WHERE region=? AND date>=?",
        (region, cutoff),
    ):
        s = out.setdefault(row["date"], set())
        for raw in _walk(_loads(row["prizes_json"], {})):
            t = _tail(raw)
            if t:
                s.add(t)
    return out


def _herd_window(c, region: str, days: int) -> dict[str, dict]:
    cutoff = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    counters: dict[str, dict[str, Counter]] = defaultdict(
        lambda: {"AI": Counter(), "NO_TOKEN": Counter()}
    )
    for row in c.execute(
        "SELECT date, ai_model, main_numbers FROM predictions WHERE target_region=? AND date>=?",
        (region, cutoff),
    ):
        nums = [_tail(x) for x in _loads(row["main_numbers"], []) if _tail(x)]
        if not nums:
            continue
        bt = nums[0]
        cls = "NO_TOKEN" if row["ai_model"] in NO_TOKEN_IDS else "AI"
        counters[row["date"]][cls][bt] += 1
    out: dict[str, dict] = {}
    for date_str, dd in counters.items():
        ai_top = dd["AI"].most_common(1)
        nt_top = dd["NO_TOKEN"].most_common(1)
        out[date_str] = {
            "ai_tail": ai_top[0][0] if ai_top else None,
            "ai_count": ai_top[0][1] if ai_top else 0,
            "ai_total": sum(dd["AI"].values()),
            "no_token_tail": nt_top[0][0] if nt_top else None,
            "no_token_count": nt_top[0][1] if nt_top else 0,
            "no_token_total": sum(dd["NO_TOKEN"].values()),
        }
    return out


def _official_window(c, region: str, days: int) -> dict[str, dict]:
    cutoff = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    out: dict[str, dict] = {}
    for row in c.execute(
        "SELECT date, bach_thu, bach_thu_status FROM final_bundles WHERE region=? AND date>=? ORDER BY id DESC",
        (region, cutoff),
    ):
        if row["date"] in out:
            continue
        out[row["date"]] = {"bt": _tail(row["bach_thu"]), "status": row["bach_thu_status"]}
    return out


def _per_region_recent(c, region: str, days: int = 7) -> dict[str, Any]:
    actuals = _actuals_window(c, region, days)
    herd = _herd_window(c, region, days)
    official = _official_window(c, region, days)
    dates = sorted(set(list(actuals.keys()) + list(herd.keys()) + list(official.keys())), reverse=True)[:days]
    rows = []
    for d in dates:
        a = actuals.get(d, set())
        h = herd.get(d, {})
        o = official.get(d, {})
        ai_tail = h.get("ai_tail")
        nt_tail = h.get("no_token_tail")
        off_tail = o.get("bt")
        rows.append({
            "date": d,
            "official_tail": off_tail,
            "official_status": o.get("status"),
            "official_hit": (off_tail in a) if (off_tail and a) else None,
            "ai_herd_tail": ai_tail,
            "ai_herd_count": h.get("ai_count"),
            "ai_herd_total": h.get("ai_total"),
            "ai_herd_pct": (h.get("ai_count") / h.get("ai_total"))
            if h.get("ai_total") else None,
            "ai_herd_hit": (ai_tail in a) if (ai_tail and a) else None,
            "no_token_tail": nt_tail,
            "no_token_count": h.get("no_token_count"),
            "no_token_total": h.get("no_token_total"),
            "no_token_hit": (nt_tail in a) if (nt_tail and a) else None,
            "actuals_count": len(a),
        })
    return {"region": region, "rows": rows}


def _shadow_table_recent(
    c,
    table: str,
    cols: list[str],
    region_col: str = "region",
    date_col: str = "target_date",
    days: int = 7,
    where_extra: str = "",
) -> list[dict]:
    if not _table_exists(c, table):
        return []
    cutoff = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    where = f"{date_col} >= ?"
    params: tuple = (cutoff,)
    if where_extra:
        where += f" AND {where_extra}"
    sql = (
        f"SELECT {', '.join(cols)} FROM {table} WHERE {where} "
        f"ORDER BY {date_col} DESC, {region_col} ASC"
    )
    return _safe_select(c, sql, params)


def build_payload() -> dict[str, Any]:
    """Return the full V82 monitor payload. READ-ONLY."""
    c = _conn()
    today = _today_vn()
    payload: dict[str, Any] = {
        "schema_version": "v82_monitor_v1",
        "source_doctrine": SOURCE_DOC,
        "generated_at_vn": dt.datetime.now(VN).isoformat(timespec="seconds"),
        "today_vn": today,
        "official_unchanged": True,
        "shadow_only": True,
        "owner_actions_in_panel": False,
        "regions": REGIONS,
    }

    # Section 1 — per-region last 7 days OFFICIAL vs AI herd vs NO_TOKEN herd
    payload["region_recent"] = {r: _per_region_recent(c, r, days=7) for r in REGIONS}

    # Section 2 — V79 cluster-weighted last 7 days (rank=1 selected)
    payload["v79_cluster_weighted_recent"] = _shadow_table_recent(
        c,
        "cluster_weighted_consensus_shadow",
        cols=[
            "target_date AS date",
            "region",
            "selected_tail",
            "selected_reason",
            "ai_cluster_weight",
            "no_token_cluster_weight",
            "exploit_weight",
            "consensus_weight",
            "budget_weight",
            "final_cluster_score",
            "independent_cluster_count",
            "herd_risk_flag",
        ],
        where_extra="rank=1",
    )

    # Section 3 — V79 AI vs NO_TOKEN cross-verify (latest 7 days)
    payload["v79_cross_verify_recent"] = _shadow_table_recent(
        c,
        "ai_no_token_cross_verification_shadow",
        cols=[
            "target_date AS date",
            "region",
            "ai_herd_tail",
            "ai_herd_count",
            "ai_cluster_count",
            "no_token_herd_tail",
            "no_token_herd_count",
            "no_token_cluster_count",
            "v67_tail",
            "v70_tail",
            "v73_tail",
            "c16_tail",
            "official_tail",
            "cluster_weighted_tail",
            "independent_cluster_count",
            "ai_vs_no_token_relation",
            "herd_risk_flag",
            "final_shadow_recommendation",
            "confidence",
            "would_save",
            "would_break",
            "false_promotion",
            "actual_status",
        ],
    )

    # Section 4 — V81 provider shadow pilot per-call (latest 7 days)
    payload["v81_provider_pilot_recent"] = _shadow_table_recent(
        c,
        "ai_region_specialist_provider_shadow_results",
        cols=[
            "target_date AS date",
            "region",
            "model_id",
            "lane",
            "parse_status",
            "parsed_bt",
            "parsed_confidence",
            "parsed_herd_warning",
            "parsed_regime_shift_warning",
            "official_bt",
            "v67_tail",
            "v73_tail",
            "cluster_weighted_tail",
            "actual_status",
            "actual_bt_hit",
            "would_save",
            "would_break",
            "false_promotion",
            "latency_seconds",
        ],
    )

    # Section 5 — V80 MB regime shift
    payload["v80_mb_regime_recent"] = _shadow_table_recent(
        c,
        "mb_regime_shift_shadow",
        cols=[
            "target_date AS date",
            "regime_state",
            "regime_severity",
            "all_method_cold_streak",
            "diversification_warning",
            "lag1_signal",
            "lag2_signal",
            "lag3_signal",
            "source_prize_top",
            "method_cluster_summary",
            "owner_action_required",
        ],
        region_col="target_date",  # MB only, no region split
        days=14,
    )

    # Section 6 — V80 MN AI herd vs V67 save monitor
    payload["v80_mn_v67_save_recent"] = _shadow_table_recent(
        c,
        "mn_ai_herd_vs_v67_save_daily",
        cols=[
            "target_date AS date",
            "ai_herd_tail",
            "official_tail",
            "v67_tail",
            "v73_tail",
            "actual_tails_count",
            "ai_herd_hit",
            "official_hit",
            "v67_hit",
            "v73_hit",
            "save_signal",
            "save_signal_count_7d",
        ],
        region_col="target_date",
        days=14,
    )

    # Section 7 — V77 fast incident monitor (alert classes)
    payload["v77_fast_incident_recent"] = _shadow_table_recent(
        c,
        "test_lane_fast_incident_monitor",
        cols=[
            "target_date AS date",
            "region",
            "alert_class",
            "alert_severity",
            "method_name",
            "fail_streak",
            "details",
            "auto_action_taken",
        ],
        days=7,
    )

    # Section 8 — V73 hybrid + V70 consensus + V67 exploit traces (latest 7 days)
    payload["v67_v70_v73_traces_recent"] = {
        "v67_exploit": _shadow_table_recent(
            c, "adaptive_exploit_v67_candidate_trace",
            cols=["target_date AS date", "region", "candidate_tail", "score", "contribution_count", "notes"],
        ),
        "v70_consensus": _shadow_table_recent(
            c, "consensus_v1_trace",
            cols=["target_date AS date", "region", "candidate_tail", "agreement_count", "methods_agreeing_json", "notes"],
        ),
        "v73_hybrid": _shadow_table_recent(
            c, "hybrid_v1_trace",
            cols=[
                "target_date AS date", "region", "candidate_tail", "confidence_tier",
                "consensus_pick", "consensus_agreement", "exploit_pick", "budget_pick", "notes",
            ],
        ),
    }

    # Section 9 — V82 60d summary (cached static data — owner already saw in V82 report)
    payload["v82_60d_summary"] = {
        "note": "Static V82 60d evidence summary. See public V82 report for full table.",
        "MN": [
            {"method": "MN_AI_CHAIN_PRESERVATION_V1", "n": 59, "hit": 0.5254, "save": 5, "break": 1, "verdict": "PROMOTION_CANDIDATE_AFTER_DOSSIER"},
            {"method": "MN_SPECIALIST_ROSTER_V1", "n": 60, "hit": 0.5167, "save": 4, "break": 0, "verdict": "PROMOTION_CANDIDATE_CLEAN"},
            {"method": "NO_TOKEN_HERD", "n": 60, "hit": 0.5167, "save": 14, "break": 10, "verdict": "REGION_SPECIFIC"},
            {"method": "AI_HERD", "n": 60, "hit": 0.4833, "save": 6, "break": 4, "verdict": "PARITY+"},
            {"method": "OFFICIAL", "n": 60, "hit": 0.4500, "save": 0, "break": 0, "verdict": "BASELINE"},
        ],
        "MT": [
            {"method": "OFFICIAL", "n": 60, "hit": 0.5000, "save": 0, "break": 0, "verdict": "BASELINE_STRONG"},
            {"method": "NO_TOKEN_HERD", "n": 60, "hit": 0.5167, "save": 7, "break": 6, "verdict": "PARITY"},
            {"method": "AI_HERD", "n": 60, "hit": 0.4333, "save": 8, "break": 12, "verdict": "DESTRUCTIVE_-6.7pp"},
            {"method": "MT_AI_CHAIN_PRESERVATION_V1", "n": 60, "hit": 0.4167, "save": 7, "break": 12, "verdict": "DO_NOT_PROMOTE"},
            {"method": "MT_PRIOR_REGION_CONTEXT_SAFE_V1", "n": 60, "hit": 0.4167, "save": 4, "break": 9, "verdict": "DO_NOT_PROMOTE"},
        ],
        "MB": [
            {"method": "MB_SPECIALIST_ROSTER_V1", "n": 41, "hit": 0.3659, "save": 5, "break": 0, "verdict": "PROMISING_LIMITED_SAMPLE"},
            {"method": "MB_PRIOR_REGION_CONTEXT_SAFE_V1", "n": 60, "hit": 0.2833, "save": 8, "break": 6, "verdict": "PARITY+"},
            {"method": "AI_HERD", "n": 60, "hit": 0.2667, "save": 12, "break": 11, "verdict": "NOISY"},
            {"method": "OFFICIAL", "n": 60, "hit": 0.2500, "save": 0, "break": 0, "verdict": "BASELINE_WEAK"},
            {"method": "NO_TOKEN_HERD", "n": 60, "hit": 0.2333, "save": 5, "break": 6, "verdict": "PARITY"},
        ],
    }

    # Section 10 — owner controls (intentionally none)
    payload["owner_controls"] = {
        "promote_button": False,
        "rollback_button": False,
        "edit_button": False,
        "trigger_run_button": False,
        "note": "V82 monitor cố ý không có nút điều khiển. Mọi promotion/rollback đều cần owner OK ở session riêng + dossier.",
    }

    return payload
