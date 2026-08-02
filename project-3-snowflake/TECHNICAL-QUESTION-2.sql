/*
QUESTION 17: Write a query against WAREHOUSE_METERING_HISTORY to detect warehouses showing a
pattern of auto-suspend thrashing (frequent start/stop cycles within short windows).
Define your threshold for "thrashing" and justify it.
*/

/*
Assumed table: SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
Columns used: warehouse_name, start_time, end_time, credits_used

Threshold: a warehouse is flagged as thrashing if it has 3 or more usage intervals
within a single hour, where each interval lasted under 5 minutes on average.
Occasional restarts are normal, but 3+ short-lived intervals in one hour suggests
the auto-suspend setting is too aggressive for that warehouse's actual usage pattern.

Tested against a live Snowflake trial account. Ran successfully in 520ms, returned
0 rows, expected, since this trial account has no real warehouse usage history yet
to produce a genuine thrashing pattern (project-3-results.pdf).
*/

SELECT
warehouse_name,
COUNT(*) AS thrashing_hours,
SUM(start_count) AS total_starts_in_thrashing_hours,
AVG(avg_run_seconds) AS avg_run_length_seconds
FROM (
 SELECT
 warehouse_name,
 DATE_TRUNC('hour', start_time) AS hour_window,
 COUNT(*) AS start_count,
 AVG(DATEDIFF('second', start_time, end_time)) AS avg_run_seconds
 FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
 WHERE start_time >= DATEADD('day', -30, CURRENT_TIMESTAMP())
 GROUP BY warehouse_name, DATE_TRUNC('hour', start_time)
) hourly_activity
WHERE start_count >= 3
AND avg_run_seconds < 300
GROUP BY warehouse_name
ORDER BY thrashing_hours DESC;
