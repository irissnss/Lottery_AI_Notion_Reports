@echo off
cd /d E:\Lottery_AI_Notion_Reports
git add V10845_EOD_CHOI_REALTIME_20260725
git commit -m "V10845: EOD 25/07 full audit + owner-signed /choi always-show numbers with realtime warnings; boundary PASS closes V10841; CP-S4 cron cleanup"
git log --oneline -1
