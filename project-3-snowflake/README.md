# Project 3: Snowflake

## What this is
A set of Snowflake questions covering warehouse scaling, query performance troubleshooting, caching layers, and cost/usage analysis using Snowflake's system tables. Some are written explanations, some are SQL queries against ACCOUNT_USAGE views.

## Files
- `TECHNICAL-QUESTIONS.sql`: the two SQL queries, each with the original question and my assumptions written as a comment block above it
- `THEORY-QUESTIONS.md`: written answers on scaling, query troubleshooting, and caching

## What's covered

**Scaling up vs. scaling out**
- Explained the difference between making a single warehouse bigger vs. running multiple warehouses in parallel
- Gave one real scenario for each: scaling up for a single heavy nightly job, scaling out for lots of people querying at once

**Troubleshooting a slow 2-billion-row join**
- Listed the top 3 things I'd check first: Query Profile in Snowsight, whether the warehouse is spilling to disk, and whether the query is queuing behind others in QUERY_HISTORY
- Named the specific view/tool for each one

**Result cache vs. warehouse cache vs. remote storage**
- Walked through the three caching layers and what each one actually is
- Used a "someone already pulled the file from the archive room" analogy for explaining this to a non-technical stakeholder

**Top 10 most expensive query patterns (SQL)**
- Query against QUERY_HISTORY that groups similar queries together instead of treating every run as unique
- Stated a credit-estimation formula, since this table doesn't give you credits directly, only execution time and warehouse size

**Auto-suspend thrashing detection (SQL)**
- Query against WAREHOUSE_METERING_HISTORY to catch warehouses that keep starting and stopping in short bursts
- Defined my own threshold for what counts as "thrashing" (3+ short intervals within an hour) and explained why

## A note on execution
I don't have a Snowflake account set up yet, so these queries were written against the assumed table structure and column names given in the instructions, not tested against live data. I'm being upfront about that rather than pretending otherwise. If needed, I'm happy to sign up for the free trial and actually run these, or walk through the logic of each query out loud.
