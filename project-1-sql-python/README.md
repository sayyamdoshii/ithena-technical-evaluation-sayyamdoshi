# Project 1: SQL & Python

## What this is
A set of SQL and Python exercises covering common data quality and reconciliation problems, near-duplicate detection, null handling, anti-joins, multi-table reconciliation, and dedup logic, plus written theory answers on the reasoning behind these approaches.

**Files:**
- `TECHNICAL-QUESTIONS.sql`: the SQL queries, each with the original question and my assumptions written as a comment block above it
- `TECHNICAL-PYTHON-QUES.py`: the flag_leakage_orders function
- `THEORY-QUESTIONS.md`: written answers on near-duplicate detection, the COALESCE pitfall, and anti-join patterns
- `project-1-results.pdf`: screenshots showing the schema being created, sample data inserted, and all three technical questions (the reconciliation query, the dedup logic, and the flag_leakage_orders function) actually executed against that data, with real output, not just written queries

## What's covered

**Theory Question 1: Near-duplicate detection at scale**
- Given a 500M row table, asked why a standard GROUP BY / DISTINCT doesn't work for near-match duplicates (same customer, same amount, within 2 minutes), and what to use instead
- Answered in 100-150 words, walked through why exact-match tools fail here and what approach actually catches near-duplicates

**Theory Question 2: The COALESCE pitfall**
- A colleague suggests always using COALESCE to handle NULLs in aggregations
- Explained a scenario where doing this blindly produces a wrong business number, not just a technically wrong query

**Theory Question 3: Anti-join patterns**
- Compared LEFT JOIN + WHERE IS NULL vs NOT IN vs NOT EXISTS for finding orders with no matching payment
- Focused on the practical differences around NULL handling and performance, and which one I'd default to and why

**Technical Question 4: Order reconciliation**
- One query across orders, order_items, payments, and refunds that flags orders where the net order value doesn't reconcile with payments minus refunds
- Built in a ±₹1 tolerance to account for rounding

**Technical Question 5: Gateway retry deduplication**
- The payments table has duplicate rows from a gateway retry bug, same order, same amount, timestamps within 60 seconds of each other
- Wrote actual de-duplication logic (not just DISTINCT) that needs to run before Technical Question 4

**Technical Question 6: flag_leakage_orders (Python)**
- Pandas function `flag_leakage_orders(orders_df, items_df, payments_df, refunds_df, tolerance=1.0)`
- Reproduces the reconciliation logic from Question 4 and classifies each flagged row as underpayment, overpayment, refund_mismatch, or duplicate_payment_suspected
- Used a plain for-loop instead of `.iterrows()`, did the math column-wise instead for better performance
