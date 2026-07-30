@echo off
cd /d E:\Lottery_AI_Notion_Reports
git add V10844_MB_WHATIF_MEASURE_20260724
git commit -m "V10844: owner-approved measurement deploy - what-if /choi MB (laneV2/V3 vs AE) + AE per-source panel, shadow only, zero production change"
git log --oneline -1
