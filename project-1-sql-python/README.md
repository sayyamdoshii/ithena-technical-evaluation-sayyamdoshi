# Project 1: SQL & Python

## What this is
A set of SQL and Python exercises covering common data quality and reconciliation problems, near-duplicate detection, null handling, anti-joins, multi-table reconciliation, and dedup logic, plus some written theory questions on BI concepts.

## Files
- `TECHNICAL-QUESTIONS.sql`: all the SQL queries, each one has the original question written above it as a comment
- `TECHNICAL-PYTHON-QUES.py`: the pandas function for flagging leakage orders
- `THEORY-QUESTIONS.md`: written answers on Power BI/Tableau concepts, calculated columns vs measures, churn dashboards, refresh cadence

## What's covered

**Near-duplicate detection**
- Compared two approaches: LAG window functions vs a NOT EXISTS self-join
- Went with plain JOINs and subqueries over CTEs where possible, kept it beginner-readable

**NULL handling in aggregations**
- Walked through the COALESCE pitfall, where NULLs can quietly throw off a SUM or AVG if you're not careful

**Anti-join patterns**
- Compared LEFT JOIN, NOT IN, and NOT EXISTS for finding records that don't have a match in another table

**Order reconciliation**
- Query across four tables (orders, order_items, payments, refunds) to catch mismatches, with a small tolerance of ±1 built in to account for rounding

**Gateway retry deduplication**
- Query to catch and remove duplicate payment gateway retries

**flag_leakage_orders (Python)**
- Pandas function that flags orders with revenue leakage
- Used a plain for-loop instead of `.iterrows()`, did the math column-wise instead for better performance

**Theory questions**
- Covered calculated columns vs measures, how to design a churn dashboard, and how often dashboards should refresh
- Answered in plain prose, no code unless the question called for it

