# Project 3: Snowflake

**What it covers:** the difference between scaling a warehouse up vs. out, what to 
check first when a large join is timing out, the three-layer caching model (result 
cache, warehouse cache, remote storage), and two SQL queries against Snowflake's 
system views: finding the most expensive query patterns, and detecting warehouses with 
auto-suspend thrashing.

**Files:**
- `THEORY-QUESTIONS.md`: written answers on warehouse scaling, query troubleshooting, 
and the three caching layers
- `TECHNICAL-QUESTION.sql`: query finding the top 10 most expensive query patterns 
against QUERY_HISTORY
- `TECHNICAL-QUESTION-2.sql`: query detecting auto-suspend thrashing against 
WAREHOUSE_METERING_HISTORY
- `project-3-results.pdf`: screenshots of both queries executed against a live 
Snowflake trial account, one returning 10 real rows, the other returning 0 rows 
(expected, explained below)

**Tools used:** SQL, tested against a live Snowflake trial account.

**Notable decisions:**
- Both SQL queries were written against Snowflake's documented `ACCOUNT_USAGE` schema, 
then signed up for a Snowflake free trial and actually ran both against real Snowflake 
infrastructure. The expensive-query-patterns query returned 10 real rows of account 
activity. The thrashing-detection query ran successfully with no errors but returned 0 
rows, expected, since a brand-new trial account has no real warehouse usage history yet 
to produce a genuine thrashing pattern.
- For the "most expensive query patterns" question, I grouped similar queries by 
truncating query text to a fixed length rather than using complex regex pattern 
stripping, since a simpler grouping approach is something I can actually explain 
end-to-end, versus a more clever-looking regex solution I'd struggle to defend if asked 
about it directly.
- For the credit estimation, `QUERY_HISTORY` doesn't expose credits directly at the 
query level, only execution time and warehouse size, so I estimated credits using 
Snowflake's published per-hour rates by warehouse size (Small = 2 credits/hour, Medium 
= 4, Large = 8), applied proportionally to execution time. This is a reasonable 
approximation, not the same as Snowflake's actual metered billing.
- For the thrashing detection query, I defined "thrashing" as 3 or more short usage 
intervals (under 5 minutes average) within a single hour, reasoning that occasional 
restarts are normal, but repeated short-lived activity in the same hour signals the 
auto-suspend timer is probably set too aggressively for that warehouse's real usage 
pattern.
