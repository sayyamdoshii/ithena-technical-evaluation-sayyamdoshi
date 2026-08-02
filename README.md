# ithena-technical-evaluation-sayyamdoshi
Commits were made incrementally as each piece was finished, not dumped in all at once 
at the end.

---

## Project 1: SQL & Python

**What it covers:** near-duplicate detection at scale, NULL handling pitfalls in 
aggregations, anti-join patterns, a multi-table order reconciliation query, gateway 
retry deduplication, and a pandas function that reproduces that reconciliation logic 
and classifies flagged rows.

**Tools used:** SQL (written at a beginner-to-intermediate level, deliberately avoiding 
CTEs/WITH clauses where a plain subquery could do the same job, since that's closer to 
where I actually am with SQL right now rather than trying to look more advanced than I 
am), Python with pandas.

**Notable decisions:**
- For the reconciliation query, I joined across four tables (orders, order_items, 
payments, refunds) with a ±1 tolerance built in to account for rounding, rather than 
requiring an exact match, since exact-cent matching is rarely realistic with real 
payment data.
- For `flag_leakage_orders`, I used column-wise vectorized operations instead of 
looping through rows with `.iterrows()`, since `.iterrows()` is much slower on larger 
datasets and column-wise math is the more idiomatic pandas approach once you're past 
pure beginner level.
- Theory questions (near-duplicate detection reasoning, the COALESCE pitfall, anti-join 
comparison) are answered in plain written prose, not code, since they were asking for 
reasoning, not implementation.

---

## Project 2: Tableau

**What it covers:** a cohort retention matrix, an NRR waterfall reconciled to the 
dollar, and a hard churn vs. soft churn monthly trend dashboard.

**Tools used:** Tableau Public (free tier, built on macOS), Python to generate the 
synthetic underlying data (`generate_data.py`, `generate_mrr_history.py`, 
`nrr_waterfall.py`), producing `subscriptions.csv`, `mrr_history.csv`, and 
`nrr_waterfall.csv`.

**Notable decisions:**
- The cohort retention matrix initially returned 100% retention everywhere using a 
standard LOD (level of detail) expression, which was wrong. The fix was switching to a 
`WINDOW_SUM` table calculation instead, computed specifically across the Month 
dimension, which correctly tracks how many customers from each cohort are still active 
in each subsequent month rather than just counting the cohort size repeatedly.
- The NRR waterfall breaks February 2024 into New, Expansion, Contraction, and Churned, 
and I manually reconciled it against starting and ending MRR to confirm the math: 
17,140 (starting) + 15,770 (new) + 740 (expansion) − 640 (contraction) − 1,350 
(churned) = 31,660 (ending), which checks out exactly.
- For churn, the original data only had a `downgrade_flag` (yes/no) with no date 
attached, which meant it couldn't be trended by month. I went back and added a 
`downgrade_date` field to the data generator so soft churn (downgraded but still 
active) could be tracked separately from hard churn (subscription actually ended), 
then built both as monthly trend lines on the same dashboard, color-coded (red for 
hard churn, green for soft churn) so the distinction is visible at a glance.

---

## Project 3: Snowflake

I'd never used Snowflake before this assignment. Everywhere in this folder that I got 
stuck, I stopped and actually studied the relevant documentation before writing 
anything, rather than guessing and hoping it looked right. A few things took real 
revision before I was comfortable with them, especially understanding what 
`WAREHOUSE_METERING_HISTORY` actually logs at the row level, and getting the credit 
estimation logic to make sense against what the table can and can't tell you directly.

**What it covers:** the difference between scaling a warehouse up vs. out, what to 
check first when a large join is timing out, the three-layer caching model (result 
cache, warehouse cache, remote storage), and two SQL queries against Snowflake's 
system views: finding the most expensive query patterns, and detecting warehouses with 
auto-suspend thrashing.

**Tools used:** SQL written against Snowflake's documented `ACCOUNT_USAGE` schema.

**Notable decisions:**
- I don't currently have a live Snowflake account, so these queries were written and 
reasoned through against Snowflake's documented table structures and column names, not 
tested against real data. I'm flagging that directly rather than implying otherwise, 
happy to sign up for the free trial and run them live, or walk through the logic in a 
follow-up conversation if that's useful.
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

This project ended up being the most valuable part of the assignment for me. Coming in 
with zero Snowflake experience and having to genuinely understand warehouse compute 
model, caching layers, and system usage tables from scratch is exactly the kind of gap 
I wanted this evaluation to surface.

---

## Project 4: Architecture

**What it covers:** the biggest cost/performance levers for a high-volume clickstream 
pipeline, an end-to-end architecture diagram, a partitioning/clustering strategy 
justified against two real query patterns, and a short comparison of Snowpipe vs. 
alternatives for moving data from cloud storage into Snowflake.

**Tools used:** draw.io (diagrams.net) for the architecture diagram, built and exported 
as a PNG.

**Notable decisions:**
- I identified file format, partitioning, and load frequency as the three biggest 
levers for the clickstream scenario: converting raw JSON to a columnar format cuts 
both storage cost and scan time, partitioning by date/hour means a query for "today" 
doesn't have to scan the full history, and hourly loads meet the freshness requirement 
without paying for more frequent loads than necessary.
- The diagram walks through five stages (source → cloud storage → Snowpipe → Snowflake 
transformed layer → BI tool), with each box labeled with the actual tool/service used, 
not a generic placeholder.
- For partitioning, I clustered on `event_date` with `device_type` as a secondary key, 
and justified it against two concrete query patterns ("DAU by day" and "sessions by 
device") rather than just asserting a strategy in the abstract.
- For the Snowpipe question, I kept the answer intentionally short, per the 
assignment's own note that this question was meant to test reasoning, not a full cloud 
build-out.

---

## Project 5: Integration

**What it covers:** a real example of a dashboard number that was technically correct 
but practically misleading, a rule of thumb for when to push calculations into SQL vs. 
Python vs. the BI layer, a parameterized Python script that pulls data on a "last N 
days" basis, and a one-page executive dashboard built for a non-technical CFO.

**Tools used:** Python with pandas and SQLAlchemy, Tableau Public.

**Notable decisions:**
- For the misleading-number question, I used a real example from this same project 
rather than a hypothetical: the NRR waterfall's original "Churned" number lumped fully 
cancelled customers together with customers who'd just downgraded but were still 
active, which was technically correct but would have overstated churn to anyone reading 
it at face value. I described both what caused it and what I'd change (asking what 
decision a stakeholder is trying to make before building the metric, not just what's 
easiest to query).
- The Python script connects via SQLAlchemy using Postgres as a stand-in for Snowflake 
(explicitly allowed by the question), with the "last N days" set as a single 
configurable variable at the top of the script rather than hardcoded into the query, so 
changing the lookback window doesn't require touching the SQL itself.
- For the CFO dashboard, I deliberately kept it to one big number (current MRR) and one 
trend line, and explicitly excluded cohort breakdowns, region splits, and churn-type 
distinctions, those are useful for an analyst investigating a number, but not for a CFO 
who needs a headline and a direction in under 30 seconds. The dashboard reflects MRR 
through the most recent complete month in the underlying dataset; I noted in the 
project's own README that the data trails off toward the very end of the file, which is 
an artifact of how the synthetic dataset was generated, not a real business signal.

---

## What this project brought me
Going in, Snowflake was a learning curve for me, and a few Tableau techniques 
(table calculations, LOD expressions, reference lines) took more trial and error than I 
expected. I didn't try to fake my way past the parts I didn't know. Where something 
didn't work the first time, like the retention matrix returning 100% everywhere, or the 
churn data having no date to trend against, I stopped, figured out why, and rebuilt it 
properly rather than settling for something that looked close enough. That process, 
getting stuck, studying the actual documentation, and coming back with something 
correct, is the part of this assignment I'm most glad I went through.
