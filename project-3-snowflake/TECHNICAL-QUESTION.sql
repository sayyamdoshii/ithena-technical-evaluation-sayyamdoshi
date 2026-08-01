/*
QUESTION 16: Write a query against SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY that surfaces the
top 10 most expensive query patterns over the last 30 days, group semantically similar
queries (e.g., strip literals), not individual query IDs. State your credit-estimation
formula/assumption.
*/
----------------------------------------------------------------------------------------------------------
-- Assumed table: SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
-- Relevant columns used:
-- query_text -> the actual SQL text that was run
-- warehouse_size -> size of the compute engine used (Small, Medium, Large, etc.)
-- execution_time -> how long the query took to run, in milliseconds
-- start_time -> when the query started running
-- execution_status -> whether it succeeded, failed, or was cancelled
/*
Assumption: grouped queries by the first 50 characters of query_text, since most
--queries share the same structure at the start even when specific values differ.
--Credit estimation: Small = 2 credits/hour, Medium = 4 credits/hour, Large = 8 credits/hour,
--calculated as (execution_time in seconds / 3600) * credits_per_hour.
*/

SELECT
LEFT(query_text, 50) AS query_pattern,
COUNT(*) AS times_run,
SUM((execution_time / 1000.0 / 3600.0) *
 CASE warehouse_size
 WHEN 'Small' THEN 2
 WHEN 'Medium' THEN 4
 WHEN 'Large' THEN 8
 ELSE 1
 END ) AS estimated_credits
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE start_time >= DATEADD('day', -30, CURRENT_TIMESTAMP())
AND execution_status = 'SUCCESS'
GROUP BY LEFT(query_text, 50)
ORDER BY estimated_credits DESC
LIMIT 10;
