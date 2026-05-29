-- PHASE 1 CANONICAL VIEWS (production form). Apply to DB to expose
-- canonical column names without renaming base tables. Read-only overlay.
-- Generated 2026-05-29 22:16 VN. Aliases are clearly-synonymous only.

DROP VIEW IF EXISTS v_predictions;
CREATE VIEW IF NOT EXISTS v_predictions AS
  SELECT "id", "date", "target_region" AS region, "source_regions", "ai_model", "main_numbers", "analysis_text", "phase_type", "cluster", "pivot", "strength", "verdict", "verdict_reason", "status", "hit_numbers", "hit_level", "hit_details", "created_at", "verified_at", "pick_count", "hit_count", "reasoning_json", "pre_result_numbers", "pre_result_strength", "pre_result_status", "pre_result_hit_count", "repredict_verdict", "run_source", "convergence_flag", "prediction_before", "verified_station_count", "policy_version_ref", "week_slot", "context_integrity", "run_id"
  FROM predictions;

DROP VIEW IF EXISTS v_final_bundles;
CREATE VIEW IF NOT EXISTS v_final_bundles AS
  SELECT "id", "date", "region", "bach_thu", "lo2", "lo3", "xien2", "xien3", "policy_version_ref", "source_predictions_json", "generation_method", "consensus_level", "model_count", "top_score", "is_fallback", "status", "notes", "created_at", "updated_at", "bach_thu_status", "lo2_status", "lo3_status", "xien2_status", "xien3_status", "verified_at", "bundle_version"
  FROM final_bundles;

DROP VIEW IF EXISTS v_model_daily_eval;
CREATE VIEW IF NOT EXISTS v_model_daily_eval AS
  SELECT "id", "date", "region", "ai_model", "main_numbers", "pick_count", "status", "hit_numbers", "hit_count", "bt_number" AS bach_thu, "bt_hit", "run_source", "context_integrity", "strength", "created_at"
  FROM model_daily_eval;

DROP VIEW IF EXISTS v_mined_rules;
CREATE VIEW IF NOT EXISTS v_mined_rules AS
  SELECT "id", "target_region" AS region, "target_weekday" AS weekday, "source_station", "source_region", "source_offset", "prize_keys", "lift_365", "lift_180", "delta_lift", "n_365", "hit_rate_365", "avg_src_tails", "streak", "gap", "stability", "score", "sample_quality", "production_tier", "prediction_use", "risk_note", "split_policy", "mined_at", "is_active", "rule_version", "source_run_id", "bucket_mode", "sub_bucket_key", "activation_status", "owner_approved_at", "hr_4w", "hr_8w", "hr_12w", "hr_16w", "composite_score", "window_verdict", "source_weekday", "source_station_slot", "cumulative_rank_score"
  FROM mined_rules;

DROP VIEW IF EXISTS v_lottery_results;
CREATE VIEW IF NOT EXISTS v_lottery_results AS
  SELECT "id", "date", "region", "station", "prizes_json", "tail_db", "tail_g8", "created_at"
  FROM lottery_results;
