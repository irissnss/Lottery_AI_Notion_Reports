# V91 — Per-decision tracking spec

Generated 2026-05-08T01:19:20+07:00

## Goal

Mỗi DEC entry trong DECISION_LOG.md cần có metadata mở rộng để track lifecycle:
- finality: FINAL / PROVISIONAL / EXPERIMENTAL / OWNER_LOCKED / SUPERSEDED
- affected_scope: official / test_lane / shadow / docs_only / governance
- evidence_source: report ID + commit hash + runtime proof
- next_review_date: ISO date
- superseded_by: DEC-NNN if applicable
- related_FU: list FU IDs
- related_report: list V?? IDs
- official_impact: YES/NO

## Current state (22 DEC entries from DECISION_LOG.md)

- DEC-001 → DEC-022 đã có cột finality (FINAL / PROVISIONAL / SUPERSEDED).
- Cần thêm cột next_review_date + related_FU + official_impact để query nhanh.

## Implementation (docs-only, safe now)

V91 sẽ append section `## Decision tracking metadata (V91)` vào DECISION_LOG.md với bảng metadata mở rộng cho 22 entries hiện có. KHÔNG đổi rows cũ.

## Auto-update rule (proposed for V92+)

- On new DEC entry creation, agent tự fill metadata fields trong cùng commit.
- On FU closure, scan DEC.related_FU for backreference → auto-update DEC if all related FU resolved.
- Owner-locked DEC không tự change finality.

## Hard locks

- DEC-NNN finality = OWNER_LOCKED never auto-changes.
- official_impact field is SET-ONCE on creation, never modified by agent.
