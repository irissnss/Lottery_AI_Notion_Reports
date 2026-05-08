# V98 Decision Calendar

## Today / tomorrow (auto, no owner action)

| Date VN | Time | Item | Type |
|---|---|---|---|
| 2026-05-09 | 16:30-18:30 | 3-region cascade với SP-4.1 prompt — first natural fire V97 | AUTO |
| 2026-05-09 | 19:14 | V81 provider pilot cron | AUTO |
| 2026-05-09 | 19:16 | V93.1 P0 shadow audits cron | AUTO |
| 2026-05-09 | 19:18 | V94.1 safe batch cron | AUTO |
| 2026-05-09 | 19:20 | V95 data integrity cron | AUTO |
| 2026-05-09 | 19:22 | V96 master tracker daily snapshot | AUTO |
| 2026-05-09 | 23:35 | V66.1 lag1 signal cron | AUTO |
| 2026-05-09 | 23:40 | V67 adaptive exploit cron | AUTO |
| 2026-05-09 | 23:45 | V70 consensus cron | AUTO **+ FU-172 verify** |
| 2026-05-09 | 23:48 | V73 hybrid cron | AUTO **+ FU-172 verify** |
| 2026-05-09 | 23:50 | V76 drift cron | AUTO **+ FU-172 verify** |
| 2026-05-09 | 23:55 | C16 budget cron | AUTO **+ FU-172 verify** |

## 7d / 14d / 30d / 60d gates (owner)

| Date VN | Items | Severity |
|---|---|---|
| 2026-05-12 | 4 P0 methods reach 14d sample | P0 |
| **2026-05-14** | V79/V80/V81 7d rolling + MB cold-streak escalation | P0 |
| **2026-05-21** | 14d full + MN dossier + V94.1+V95 14d evidence + **FU-165, FU-173, FU-174, FU-175** | P0/P1 |
| 2026-06-06 | 30d sweep | P1 |
| **2026-06-08** | FU-162, FU-164, FU-166, FU-167 30d evidence proposals | P0/P1 |
| 2026-07-06 | 60d full review + MB SPECIALIST_ROSTER | P1 |

## 5-day rolling window (V98 hardened)

For each P0 method (V67, V70, V73, V93.1, V94.1, V95):
- Day-by-day natural fire status
- Sample size growing
- Wilson CI tightening
- 14d gate triggers when n ≥ 14 days

## V98 wrapper schedule

- **2026-05-09 09:00 VN**: First public V98 link visible to Notion AI
- **2026-05-10 09:00 VN**: Re-verify V98 metadata stability
- **2026-05-14**: V98 first 7d health check
- **2026-05-21**: V98 first 14d evidence dossier
