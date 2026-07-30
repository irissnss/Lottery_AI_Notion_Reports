@echo off
cd /d E:\Lottery_AI_Notion_Reports
git add V10843_EOD_FULL_AUDIT_20260724
git commit -m "V10843: EOD 24/07 full audit - MN sweep 4/4, MT cluster-miss 60/54, AE-MB no source edge, live-verify cache PASS, contract-check stdout fix"
git log --oneline -1
