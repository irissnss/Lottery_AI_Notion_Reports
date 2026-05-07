"""V87 — Master Board unified read-only payload.

Single endpoint returning EVERYTHING owner/agent needs to remember:
- 41 AI models with status/provider/region/WR
- 8 prompt layers + 5 PHASE-FIRST GATE cohorts
- Rules (mined_rules count, 12W/16W windows, PB-18 fields, custom_prompt mode)
- Mechanisms (cascade timeline, bundle gate stages, strongest-to-final, V77 post-cascade, anti-herding, cohere)
- Metrics (8 C-XX + 3 PB-XX + 16 flip/risk/health/cost) with live status
- Shadow methods (18 P0 portfolio + 30 V52.5 era + 11 V67/V70/V73/V79/V80/V81 selectors)
- DB tables (129) grouped by family
- Cron jobs (26) with next/last run guess
- Frontend pages (12) with URLs
- API endpoints (132) summary by category
- Decision calendar (V84 11 dates)
- Owner-gate queue (V84 9 items)

Hard contract:
- read-only
- no scoring change
- no candidate selection
- no DB writes
- output is descriptive JSON only
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

VN = dt.timezone(dt.timedelta(hours=7))
DB_PATH = Path(__file__).resolve().parents[2] / "data" / "lottery_ai.db"
ROOT = Path(__file__).resolve().parents[2]


def _conn() -> sqlite3.Connection:
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def _safe_count(c: sqlite3.Connection, name: str) -> int:
    try:
        return int(c.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0])
    except Exception:
        return -1


def _table_exists(c: sqlite3.Connection, name: str) -> bool:
    return bool(c.execute(
        "SELECT 1 FROM sqlite_master WHERE type IN ('table','view') AND name=?", (name,)
    ).fetchone())


def _safe_max_date(c: sqlite3.Connection, name: str, date_col: str) -> str | None:
    try:
        r = c.execute(f"SELECT MAX({date_col}) FROM {name}").fetchone()
        return r[0]
    except Exception:
        return None


def _models_block() -> dict[str, Any]:
    sys.path.insert(0, str(ROOT / "web" / "backend"))
    try:
        from model_registry import MODEL_REGISTRY
    except Exception:
        return {"error": "model_registry import failed", "rows": []}
    rows = []
    for info in sorted(MODEL_REGISTRY, key=lambda x: (x.get("status", ""), x.get("id", ""))):
        rows.append({
            "id": info.get("id"),
            "provider": info.get("provider"),
            "class": info.get("class"),
            "role": info.get("role"),
            "status": info.get("status"),
            "output_eligible": info.get("output_eligible"),
            "regions": info.get("allowed_regions", []),
            "schedule_slots": info.get("schedule_slots", []),
            "wr_note": (info.get("wr_note") or "")[:160],
        })
    counts = Counter(m["status"] for m in rows)
    return {
        "rows": rows,
        "total": len(rows),
        "by_status": dict(counts),
        "by_class": dict(Counter(m["class"] for m in rows)),
        "output_eligible_count": sum(1 for m in rows if m["output_eligible"] is True),
    }


def _prompts_block() -> dict[str, Any]:
    return {
        "production_stack": [
            {"version": "SP-4.0", "name": "SYSTEM_PROMPT", "where": "gpt_analyzer.py L157", "scope": "TOP1-FIRST V8.0", "active": True},
            {"version": "CP-7.9", "name": "CORE_POLICY", "where": "gpt_analyzer.py L256-305", "scope": "Confidence/MB ceiling", "active": False, "note": "ARCHIVE_ONLY, không inject"},
            {"version": "RR-16.4", "name": "REASONING_RULEBOOK", "where": "gpt_analyzer.py L308-520", "scope": "24 rules + §24 BT North Star", "active": True},
            {"version": "CTX-16.4", "name": "CONTEXT_PACK", "where": "build_context_pack()", "scope": "BT model ranking + weekly tiers", "active": True},
            {"version": "PB-18.0", "name": "PHASE-FIRST GATE", "where": "gpt_analyzer.py PB-18", "scope": "8-step phase classification (cohort-gated)", "active": True},
        ],
        "shadow_region_specialist": [
            {"version": "MN_V78_SHADOW", "where": "web/backend/prompts/shadow/MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md", "active_runtime": "SHADOW only (V81 pilot)"},
            {"version": "MT_V78_SHADOW", "where": "web/backend/prompts/shadow/MT_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md", "active_runtime": "SHADOW only (V81 pilot)"},
            {"version": "MB_V78_SHADOW", "where": "web/backend/prompts/shadow/MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md", "active_runtime": "SHADOW only (V81 pilot)"},
        ],
        "phase_first_cohorts": [
            {"id": "PFG-20260417-A", "models": "gemini-2.5-flash + gpt-5.4", "active": "2026-04-17 → 2026-04-26", "contract": False, "status": "RETIRED"},
            {"id": "PFG-20260426-B", "models": "minimax-m2.7 + gpt-oss-120b", "active": "2026-04-26 → 2026-04-27", "contract": True, "status": "RETIRED"},
            {"id": "PFG-20260427-C", "models": "minimax-m2.7 + gpt-oss-120b + gpt-5.5 + deepseek-v4-pro/flash + qwen3.6-plus", "active": "2026-04-27 → 2026-04-28", "contract": True, "status": "RETIRED"},
            {"id": "PFG-20260428-D", "models": "gpt-oss-120b + gpt-5.5 + deepseek-v4-pro/flash + qwen3.6-plus", "active": "2026-04-28 → 2026-05-05", "contract": True, "status": "RETIRED"},
            {"id": "PFG-20260505-E", "models": "gpt-oss-120b + gpt-5.5 + deepseek-v4-pro/flash + qwen3.6-plus + gemini-3.1-pro + gemini-3-flash + gemma-4-31b", "active": "2026-05-05 → present", "contract": True, "status": "ACTIVE"},
        ],
        "v81_pilot_models": [
            {"slot": "FAST_CHEAP", "model": "deepseek-chat", "provider": "deepseek"},
            {"slot": "REASONING", "model": "claude-sonnet-4-6", "provider": "anthropic"},
            {"slot": "NEW_CHEAP", "model": "gemini-3-flash", "provider": "google_shadow_key"},
        ],
    }


def _rules_block(c: sqlite3.Connection) -> dict[str, Any]:
    return {
        "weekly_mining": {
            "table": "mined_rules",
            "rows": _safe_count(c, "mined_rules"),
            "schedule": "Mon 00:30 VN (auto_weekly_mining)",
            "status": "LIVE",
        },
        "mined_effectiveness": {
            "table": "mined_rule_effectiveness",
            "rows": _safe_count(c, "mined_rule_effectiveness"),
            "schedule": "~20:10 VN (auto_mined_rule_eval)",
            "status": "LIVE",
        },
        "verified_bucket_rules": {
            "table": "verified_bucket_rules",
            "rows": _safe_count(c, "verified_bucket_rules"),
            "status": "LIVE",
        },
        "rule_windows": ["12W rolling", "16W rolling"],
        "phase_first_pb18_fields": [
            "primary_rule_group", "secondary_rule_group", "stale_rules",
            "rules_to_downweight", "top_source_prizes_by_region",
            "strongest_source_prizes_used", "strongest_rules_used",
        ],
        "rule_shadow_methods": [
            {"method": "rule_phase_evidence_v1", "table": "shadow_results", "verdict_14d": "DESTRUCTIVE_BIAS_MT"},
            {"method": "rule_injection_contract_shadow_v1", "table": "shadow_results", "verdict_14d": "DESTRUCTIVE_BIAS_MT"},
            {"method": "rule_phase_synthesis_shadow (V80)", "table": "rule_phase_synthesis_shadow", "rows": _safe_count(c, "rule_phase_synthesis_shadow"), "status": "LIVE 4d, no consumer"},
            {"method": "no_token_rule_aware_pack_shadow (V80)", "table": "no_token_rule_aware_pack_shadow", "rows": _safe_count(c, "no_token_rule_aware_pack_shadow"), "status": "LIVE 4d, no consumer"},
        ],
        "custom_prompt_mode": "ARCHIVE_ONLY (containment 500 chars; runtime injection: NO)",
    }


def _mechanisms_block() -> dict[str, Any]:
    return {
        "production_cascade": [
            {"step": "NO_TOKEN ML predict all regions", "time": "04:00 VN", "source": "auto_free_predict"},
            {"step": "MN AI predict", "time": "04:30 VN", "source": "auto_ai_mn"},
            {"step": "MN scrape + verify", "time": "16:30 VN", "source": "auto_mn"},
            {"step": "MT AI predict", "time": "16:45 VN", "source": "auto_ai_mt"},
            {"step": "MT scrape + verify", "time": "17:30 VN", "source": "auto_mt"},
            {"step": "MB AI predict", "time": "17:45 VN", "source": "auto_ai_mb"},
            {"step": "MB watchdog", "time": "17:55 VN", "source": "mb_prediction_watchdog"},
            {"step": "MB scrape + verify", "time": "18:30 VN", "source": "auto_mb"},
        ],
        "bundle_gate_surfaces": [
            "ai_primary_gate_daily", "bundle_readiness_gate_daily", "public_bundle_publish_audit_daily",
            "output_eligible_completion_daily", "reasoning_layer_penetration_daily",
            "ai_reasoning_contract_daily", "source_prize_effectiveness_daily",
            "convergence_cluster_pattern_daily", "weekday_rule_strength_daily",
        ],
        "strongest_to_final": {
            "method": "strongest_to_final_preservation_v1",
            "verdict_14d": "POTENTIAL_LIFT (11/11 hits all regions)",
            "tables": ["strongest_vs_final_conversion_daily", "strongest_candidate_escape_daily", "candidate_drop_stage_daily"],
        },
        "v59_strict_verification": {
            "BT": "Last 2 digits of MTĐB only",
            "LO2": "Last 2 digits any prize",
            "LO3": "Strict 3-digit suffix from actual prize (FIXED V59)",
            "Xien_2_3": "Same-station hit (FIXED V59)",
        },
        "v77_post_cascade_rerun": {
            "trigger": "19:00 VN (v77_post_cascade_rerun)",
            "purpose": "V70/V73 rerun with full pool AFTER all 3 region test runners completed",
        },
        "v77_fast_incident": {
            "trigger": "19:05 VN",
            "alert_classes": ["RED_FAST", "ORANGE_FAST", "YELLOW_FAST", "EXPLOIT_FAIL_FAST", "BUDGET_FAIL_FAST"],
        },
        "anti_herding": [
            "anti_herding_shadow_v1", "verdict_distribution_daily",
            "convergence_cluster_pattern_daily", "V79 AI cap + NO_TOKEN floor",
            "V79 AI ↔ NO_TOKEN cross-verify",
        ],
        "cohere_rerank": {
            "model": "cohere-rerank-4-pro",
            "shadow_method": "cohere_rerank_effectiveness_v1",
            "status": "LIVE 8d shadow, INSUFFICIENT_SAMPLE n=23",
        },
        "provider_keys": {
            "OPENAI_API_KEY": "gpt-5.4 + gpt-5-mini (401 on gpt-5-mini V81)",
            "ANTHROPIC_API_KEY": "claude-opus-4 + claude-sonnet-4-6",
            "DEEPSEEK_API_KEY": "deepseek-reasoner + deepseek-v4-pro/flash + deepseek-chat",
            "GEMINI_API_KEY": "gemini-2.5-flash + gemini-2.5-pro",
            "GEMINI_KEY_SHADOW_NEW": "gemini-3.1-pro + gemini-3-flash + gemma-4-31b (V20.3.37.55 cohort)",
            "OPENROUTER_API_KEY": "gpt-oss-120b + gpt-5.5 + qwen3-coder + qwen3-max-thinking + qwen3.6-plus + kimi-k2.5 + glm-5.1 + grok-4.20",
        },
        "timezone_hcm": {
            "string_for_apscheduler": "VN_TZ = 'Asia/Ho_Chi_Minh' (line 6899)",
            "helpers": "_today_vn_date_str() / _tomorrow_vn_date_str()",
            "vn_now_proper_tzinfo": "vn_timezone.py vn_now()",
            "cron_chain_19xx": [0, 5, 8, 10, 12, 14],
        },
        "hash_guard_4_official": {
            "predictions": "25d1a3db67d6e406",
            "final_bundles": "999d42cbaabea95a",
            "lottery_results": "937407feeb8d8f90",
            "model_daily_eval": "07a53a97d1521933",
        },
    }


def _metrics_block(c: sqlite3.Connection) -> dict[str, Any]:
    return {
        "C_xx_contracts": [
            {"id": "C-01", "purpose": "Strongest-vs-final conversion", "table": "strongest_vs_final_conversion_daily", "rows": _safe_count(c, "strongest_vs_final_conversion_daily"), "status": "LIVE"},
            {"id": "C-02", "purpose": "API source labels", "status": "DEPLOYED V54"},
            {"id": "C-03", "purpose": "Closeout PENDING + would_save tally", "status": "LIVE"},
            {"id": "C-05", "purpose": "Per-model latency / cost", "table": "model_latency_cost_audit_daily", "rows": _safe_count(c, "model_latency_cost_audit_daily"), "status": "RESOLVED V74.1"},
            {"id": "C-06", "purpose": "LOZ stage trace", "table": "loz_stage_trace_shadow", "rows": _safe_count(c, "loz_stage_trace_shadow"), "status": "LIVE V54"},
            {"id": "C-15", "purpose": "Weekday blackspot", "table": "weekday_blackspot_shadow", "rows": _safe_count(c, "weekday_blackspot_shadow"), "status": "LIVE V54"},
            {"id": "C-16", "purpose": "Adaptive Model Budget Selector 20 voters", "table": "du_doan_test_model_budget_daily", "rows": _safe_count(c, "du_doan_test_model_budget_daily"), "status": "LIVE V57+V71+V74"},
            {"id": "C-17", "purpose": "test_lane bundle output_lock_status", "table": "du_doan_test_bundles", "rows": _safe_count(c, "du_doan_test_bundles"), "status": "LIVE V74"},
        ],
        "PB_PP_layers": [
            {"id": "PB-18.0", "purpose": "PHASE-FIRST GATE 8-step", "status": "LIVE for cohort-gated"},
            {"id": "PB-18.1+", "purpose": "Trace fields (current_week_context, phase_alignment, primary/secondary/stale rules)", "status": "LIVE"},
            {"id": "PP-1", "purpose": "Pre-Push live watch (Wave 2)", "status": "LIVE"},
        ],
        "flip_health_cost_metrics": [
            "would_save (would_flip_baseline_to_win)",
            "would_break (would_flip_baseline_to_lose)",
            "false_promotion",
            "strongest_vs_final_conversion",
            "wilson_95_ci",
            "freshness_ready",
            "candidate_drop_stage",
            "herd_pct",
            "reliability_score",
            "stability_score",
            "promotion_bucket",
            "drift_alert_class (V76)",
            "fast_incident_alert_class (V77)",
            "cluster_weighted_score (V79)",
            "regime_shift_warning (V78/V80)",
            "cost_estimate_usd (V76)",
        ],
    }


def _shadow_methods_block(c: sqlite3.Connection) -> dict[str, Any]:
    p0 = []
    if _table_exists(c, "shadow_activation_registry"):
        for r in c.execute("SELECT method_key, method_group, state, min_days, min_samples FROM shadow_activation_registry ORDER BY id"):
            p0.append({
                "method_key": r["method_key"],
                "group": r["method_group"],
                "state": r["state"],
                "min_days": r["min_days"],
                "min_samples": r["min_samples"],
            })
    v525 = []
    if _table_exists(c, "experimental_preview_shadow"):
        for r in c.execute("SELECT DISTINCT experiment_name FROM experimental_preview_shadow ORDER BY experiment_name"):
            v525.append(r["experiment_name"])
    selectors = [
        {"id": "MN/MT/MB_ADAPTIVE_BUDGET_SELECTOR_V1 (V57)", "table": "experimental_preview_shadow + du_doan_test_model_budget_daily", "status": "LIVE 3d"},
        {"id": "MN/MT/MB_ADAPTIVE_EXPLOIT_V1 (V67)", "table": "adaptive_exploit_v67_candidate_trace", "rows": _safe_count(c, "adaptive_exploit_v67_candidate_trace"), "status": "LIVE eager"},
        {"id": "MN/MT/MB_CONSENSUS_V1 (V70)", "table": "consensus_v1_trace", "rows": _safe_count(c, "consensus_v1_trace"), "status": "LIVE 4d post V77 fix"},
        {"id": "MN/MT/MB_HYBRID_V1 (V73)", "table": "hybrid_v1_trace", "rows": _safe_count(c, "hybrid_v1_trace"), "status": "LIVE 15d trace"},
        {"id": "V79 cluster_weighted", "table": "cluster_weighted_consensus_shadow", "rows": _safe_count(c, "cluster_weighted_consensus_shadow"), "status": "LIVE 4d cron 19:08"},
        {"id": "V79 cross_verify", "table": "ai_no_token_cross_verification_shadow", "rows": _safe_count(c, "ai_no_token_cross_verification_shadow"), "status": "LIVE 4d cron 19:08"},
        {"id": "V80 rule_phase_synthesis", "table": "rule_phase_synthesis_shadow", "rows": _safe_count(c, "rule_phase_synthesis_shadow"), "status": "LIVE 4d cron 19:12 NO CONSUMER"},
        {"id": "V80 no_token_rule_pack", "table": "no_token_rule_aware_pack_shadow", "rows": _safe_count(c, "no_token_rule_aware_pack_shadow"), "status": "LIVE 4d cron 19:12 NO CONSUMER"},
        {"id": "V80 mb_regime_shift", "table": "mb_regime_shift_shadow", "rows": _safe_count(c, "mb_regime_shift_shadow"), "status": "LIVE 4d cron 19:12"},
        {"id": "V80 mn_v67_save", "table": "mn_ai_herd_vs_v67_save_daily", "rows": _safe_count(c, "mn_ai_herd_vs_v67_save_daily"), "status": "LIVE 4d cron 19:12"},
        {"id": "V81 provider pilot", "table": "ai_region_specialist_provider_shadow_results", "rows": _safe_count(c, "ai_region_specialist_provider_shadow_results"), "status": "LIVE 2d cron 19:14"},
    ]
    return {
        "p0_portfolio": p0,
        "p0_count": len(p0),
        "v52_5_era": v525,
        "v52_5_count": len(v525),
        "selectors": selectors,
        "selectors_count": len(selectors),
        "total": len(p0) + len(v525) + len(selectors),
    }


def _db_tables_block(c: sqlite3.Connection) -> dict[str, Any]:
    DATE_COLS = ("date", "target_date", "anchor_date", "business_date_vn", "as_of_date", "run_date", "computed_at", "created_at")
    OFFICIAL = {"predictions", "final_bundles", "lottery_results", "model_daily_eval"}
    rows = []
    fams = Counter()
    for r in c.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%' ORDER BY name"):
        name = r["name"]
        cols = [x["name"] for x in c.execute(f"PRAGMA table_info({name})")]
        date_col = next((dc for dc in DATE_COLS if dc in cols), None)
        n = _safe_count(c, name)
        max_date = _safe_max_date(c, name, date_col) if date_col and n > 0 else None
        if name in OFFICIAL:
            fam = "OFFICIAL"
        elif "du_doan_test" in name or "experimental_preview" in name or "model_strength_by_region" in name:
            fam = "TEST_LANE"
        elif any(k in name for k in ("primary_gate", "candidate_escape", "weekday_rule_strength", "bundle_readiness", "publish_audit", "output_eligible_completion", "reasoning_layer", "ai_reasoning_contract", "source_prize", "convergence_cluster", "verdict_distribution", "prompt_section_breakdown", "live_watch")):
            fam = "WAVE_1_2"
        elif any(k in name for k in ("shadow", "trace", "audit", "drift", "monitor", "tensor", "regime", "save_daily", "synthesis", "rule_aware_pack", "cluster_weighted", "specialist_provider")):
            fam = "SHADOW"
        elif "scrap" in name or "scheduler_log" in name:
            fam = "INFRA"
        else:
            fam = "SUPPORT"
        fams[fam] += 1
        rows.append({"name": name, "type": r["type"], "rows": n, "max_date": max_date, "family": fam})
    return {"total": len(rows), "by_family": dict(fams), "rows": rows}


def _cron_block() -> list[dict]:
    return [
        {"time": "04:00 VN", "id": "auto_free_predict", "purpose": "LSTM + Meta + Smart-ML + Smart-Ensemble predict all regions", "lane": "OFFICIAL_NO_TOKEN"},
        {"time": "04:30 VN", "id": "auto_ai_mn", "purpose": "AI predict MN", "lane": "OFFICIAL_AI"},
        {"time": "16:30 VN", "id": "auto_mn", "purpose": "Scrape MN + closeout", "lane": "OFFICIAL_INFRA"},
        {"time": "16:45 VN", "id": "auto_ai_mt", "purpose": "AI predict MT", "lane": "OFFICIAL_AI"},
        {"time": "17:30 VN", "id": "auto_mt", "purpose": "Scrape MT + verify + predict MB", "lane": "OFFICIAL_INFRA"},
        {"time": "17:45 VN", "id": "auto_ai_mb", "purpose": "AI predict MB", "lane": "OFFICIAL_AI"},
        {"time": "17:55 VN", "id": "mb_prediction_watchdog", "purpose": "Re-trigger MB if missing", "lane": "OFFICIAL_INFRA"},
        {"time": "18:30 VN", "id": "auto_mb", "purpose": "Scrape MB + verify all", "lane": "OFFICIAL_INFRA"},
        {"time": "19:00 VN", "id": "v77_post_cascade_rerun", "purpose": "V70/V73 rerun with full pool", "lane": "TEST_LANE_V77"},
        {"time": "19:05 VN", "id": "v77_fast_incident_monitor", "purpose": "Fast incident 5 alert classes", "lane": "MEASUREMENT_V77"},
        {"time": "19:08 VN", "id": "v79_ai_no_token_cross_verify", "purpose": "AI ↔ NO_TOKEN + cluster-weighted", "lane": "SHADOW_V79"},
        {"time": "19:10 VN", "id": "v78_prompt_shadow_audit", "purpose": "Region prompt audit (no provider)", "lane": "SHADOW_V78"},
        {"time": "19:12 VN", "id": "v80_shadow_completion", "purpose": "Rule_phase + no_token_pack + MB regime + MN V67 save", "lane": "SHADOW_V80"},
        {"time": "19:14 VN", "id": "v81_provider_shadow_pilot", "purpose": "Owner-approved 3-model provider pilot", "lane": "SHADOW_V81"},
        {"time": "~20:00 VN", "id": "auto_daily_eval", "purpose": "Daily eval", "lane": "MEASUREMENT"},
        {"time": "~20:10 VN", "id": "auto_mined_rule_eval", "purpose": "Mined rule effectiveness eval", "lane": "RULE_EVAL"},
        {"time": "~20:20 VN", "id": "auto_model_daily_eval", "purpose": "Per-model eval (model_daily_eval)", "lane": "MEASUREMENT"},
        {"time": "23:35 VN", "id": "lag1_adaptive_exploit_signal_materializer", "purpose": "V66.1 lag1 signal", "lane": "MEASUREMENT_V66"},
        {"time": "23:40 VN", "id": "adaptive_exploit_v67_materializer", "purpose": "V67 selector", "lane": "TEST_LANE_V67"},
        {"time": "23:45 VN", "id": "consensus_v1_materializer", "purpose": "V70 selector", "lane": "TEST_LANE_V70"},
        {"time": "23:48 VN", "id": "hybrid_v1_materializer", "purpose": "V73 selector", "lane": "TEST_LANE_V73"},
        {"time": "23:50 VN", "id": "drift_monitor_materializer", "purpose": "V76 drift (alert-only)", "lane": "MEASUREMENT_V76"},
        {"time": "Mon 00:30 VN", "id": "auto_weekly_mining", "purpose": "Weekly rule mining", "lane": "RULE_MINING"},
        {"time": "Sun 02:00 VN", "id": "auto_retrain", "purpose": "ML retrain (LSTM/XGB/RF/Meta)", "lane": "ML_TRAINING"},
        {"time": "every 5min", "id": "du_doan_test_pre_result_trigger", "purpose": "/du-doan-test pre-result readiness", "lane": "TEST_LANE"},
        {"time": "weekly", "id": "auto_weight_optimizer", "purpose": "Weights optimizer", "lane": "MEASUREMENT"},
    ]


def _frontend_block() -> list[dict]:
    return [
        {"file": "index.html", "url": "/", "purpose": "Home"},
        {"file": "login.html", "url": "/login", "purpose": "Login"},
        {"file": "du-doan.html", "url": "/du-doan", "purpose": "Production prediction (15 model output)"},
        {"file": "du-doan-test.html", "url": "/du-doan-test", "purpose": "Admin experimental lane (V52.5+ test methods, V57 budget)"},
        {"file": "monitoring.html", "url": "/monitoring", "purpose": "Admin runtime monitoring center (THIS PAGE; V86 V82 merged + V87 master index)"},
        {"file": "v82-monitor.html", "url": "/v82-monitor", "purpose": "V83 standalone V82 monitor (kept for direct link)"},
        {"file": "accuracy.html", "url": "/accuracy", "purpose": "Accuracy review board"},
        {"file": "review-dashboard.html", "url": "/review-dashboard", "purpose": "Review dashboard"},
        {"file": "search.html", "url": "/search", "purpose": "Search interface"},
        {"file": "settings.html", "url": "/settings", "purpose": "Admin settings"},
        {"file": "user-view.html", "url": "/user-view", "purpose": "Compact user view"},
        {"file": "viewer.html", "url": "/viewer", "purpose": "Generic viewer"},
    ]


def _api_block() -> dict[str, Any]:
    main_py = (ROOT / "web" / "backend" / "main.py").read_text(encoding="utf-8", errors="replace")
    pat = re.compile(r'^@app\.(get|post|put|delete|patch)\("([^"]+)"', re.MULTILINE)
    by_cat: dict[str, list[dict]] = {"ADMIN_API": [], "PUBLIC_API": [], "PAGE": []}
    for m in pat.finditer(main_py):
        method = m.group(1).upper()
        path = m.group(2)
        if path.startswith("/api/admin"):
            cat = "ADMIN_API"
        elif path.startswith("/api/"):
            cat = "PUBLIC_API"
        elif path.startswith("/"):
            cat = "PAGE"
        else:
            continue
        by_cat[cat].append({"method": method, "path": path})
    by_cat["ADMIN_API"].sort(key=lambda x: x["path"])
    by_cat["PUBLIC_API"].sort(key=lambda x: x["path"])
    by_cat["PAGE"].sort(key=lambda x: x["path"])
    total = sum(len(v) for v in by_cat.values())
    return {
        "total": total,
        "admin_api_count": len(by_cat["ADMIN_API"]),
        "public_api_count": len(by_cat["PUBLIC_API"]),
        "page_count": len(by_cat["PAGE"]),
        "by_category": by_cat,
    }


def _decision_calendar_block() -> list[dict]:
    return [
        {"date": "2026-05-08", "trigger": "Cron 19:00-19:14 VN natural", "item": "6 cron job natural proof", "decision": "Auto-verify next morning. P0 fix nếu fail."},
        {"date": "2026-05-08", "trigger": "Closeout 18:30 VN", "item": "Day 1 fresh-live V79 cluster + V81 pilot", "decision": "Append SSOT. NO promote."},
        {"date": "2026-05-09", "trigger": "Day 2 fresh-live", "item": "V79 + V81 cumulative 2d", "decision": "Auto-update SSOT."},
        {"date": "2026-05-10", "trigger": "Day 3 + min_samples=3 gate", "item": "freshness/strongest/no_token_drift/rule_phase/output_policy/counterfactual/cohere reach min sample 3", "decision": "Eligible for evaluation, not promotion."},
        {"date": "2026-05-12", "trigger": "Day 5 + min_days=5 methods", "item": "rule_aware_adaptive_notoken / phase_aware_rerank reach 5d min", "decision": "Eligible, not promote."},
        {"date": "2026-05-14", "trigger": "Day 7 fresh-live", "item": "V79/V80/V81 7d rolling + MB cold check (>=7d cold → P0 forensic)", "decision": "If MB still 0/7 → escalate."},
        {"date": "2026-05-21", "trigger": "Day 14 + min_days=14", "item": "meta_ranker_ltr / context_specialist_policy / online_bayesian reach 14d min + V79/V81 14d + drift V76 active", "decision": "If MN candidates sustain lift + MT no break → trình owner dossier."},
        {"date": "2026-06-06", "trigger": "Day 30 fresh-live", "item": "30d rolling for V79/V81 + top P0", "decision": "Method that beats baseline + Wilson_lo > baseline_hi → eligible promotion proposal."},
        {"date": "2026-07-06", "trigger": "Day 60 fresh-live", "item": "Full 60d rolling for V79/V80/V81", "decision": "Promotion gate full check + owner OK."},
        {"date": "ANY 19:14 VN failure", "trigger": "Cron failure detected", "item": "Auto-FU entry generated", "decision": "Re-run / fix / disable."},
        {"date": "Always", "trigger": "Pre/post hash mismatch official tables", "item": "Hash guard violation", "decision": "STOP + investigate."},
    ]


def _owner_gate_block() -> list[dict]:
    return [
        {"item": "MN_TEST_LANE_VOTER_PROPOSAL dossier", "trigger_date": "2026-05-21", "blocker": "Need 14d fresh-live sustained lift", "owner_action": "Read dossier + OK or REJECT (test-lane voter only)", "official_impact": "NO"},
        {"item": "Provider invoice update _provider_pricing_table.py", "trigger_date": "Anytime", "blocker": "Owner provides real $/1k tokens", "owner_action": "Edit or instruct", "official_impact": "NO"},
        {"item": "MB regime forensic deep dive", "trigger_date": "2026-05-14 if MB OFFICIAL 0/7", "blocker": "Auto-trigger", "owner_action": "OK to proceed", "official_impact": "NO"},
        {"item": "GPT-5-mini key validation", "trigger_date": "Anytime", "blocker": "VPS OPENAI key 401 on gpt-5-mini", "owner_action": "Check OpenAI org access", "official_impact": "NO"},
        {"item": "V83 / V86 / V87 layout feedback", "trigger_date": "Anytime", "blocker": "UX preference", "owner_action": "Comment", "official_impact": "NO"},
        {"item": "Selector promotion (V67/V70/V73/V79/V81 → official)", "trigger_date": "Earliest 60d (2026-07-06) + dossier", "blocker": "60d Wilson + zero MT break", "owner_action": "Owner explicit OK", "official_impact": "YES (LOCKED)"},
        {"item": "Official prompt change", "trigger_date": "Owner-locked", "blocker": "Owner directive", "owner_action": "—", "official_impact": "YES (LOCKED)"},
        {"item": "Production model swap", "trigger_date": "Owner-locked", "blocker": "Owner directive", "owner_action": "—", "official_impact": "YES (LOCKED)"},
        {"item": "Global NO_TOKEN floor change", "trigger_date": "Owner-locked", "blocker": "Region delta differ", "owner_action": "—", "official_impact": "YES (LOCKED)"},
    ]


def build_payload() -> dict[str, Any]:
    """Return the full V87 master board payload. READ-ONLY."""
    c = _conn()
    return {
        "schema_version": "v87_master_board_v1",
        "generated_at_vn": dt.datetime.now(VN).isoformat(timespec="seconds"),
        "today_vn": dt.datetime.now(VN).date().isoformat(),
        "official_unchanged": True,
        "shadow_only_payload": True,
        "owner_actions_in_panel": False,
        "models": _models_block(),
        "prompts": _prompts_block(),
        "rules": _rules_block(c),
        "mechanisms": _mechanisms_block(),
        "metrics": _metrics_block(c),
        "shadow_methods": _shadow_methods_block(c),
        "db_tables": _db_tables_block(c),
        "cron_jobs": _cron_block(),
        "frontend_pages": _frontend_block(),
        "api_endpoints": _api_block(),
        "decision_calendar": _decision_calendar_block(),
        "owner_gate_queue": _owner_gate_block(),
        "owner_controls": {
            "promote_button": False, "rollback_button": False, "edit_button": False, "trigger_run_button": False,
            "note": "V87 Master Index cố ý không có nút điều khiển. Mọi thay đổi đều cần owner OK ở session riêng + dossier.",
        },
    }
