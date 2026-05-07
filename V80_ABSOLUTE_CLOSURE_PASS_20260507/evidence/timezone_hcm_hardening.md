# Timezone HCM Audit

| surface | status | evidence |
| --- | --- | --- |
| scheduler CronTrigger | OK | timezone='Asia/Ho_Chi_Minh' string accepted by APScheduler |
| nested selector jobs V66-V79 | FIXED | use _today_vn_date_str/_tomorrow_vn_date_str, not datetime.now(VN_TZ string) |
| V79 materializer business_date_vn | OK | business_date_vn = target_date, created_at_vn and created_at_utc both stored |
| created_before_result_guard | OK | uses VN closeout cutoffs MN 16:38 / MT 17:38 / MB 18:38 |
| legacy datetime.now/date.today | WATCH | legacy surfaces remain; V79 did not touch official paths |
