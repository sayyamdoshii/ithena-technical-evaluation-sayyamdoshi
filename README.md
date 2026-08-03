---
## Project 1: SQL & Python
Near-duplicate detection, NULL handling pitfalls, anti-join patterns, a multi-table 
order reconciliation query, gateway retry deduplication, and a pandas function that 
reproduces that reconciliation logic and classifies flagged rows. Built a small 
synthetic database matching the assignment's schema and actually ran all three 
technical questions against it, real results included in project-1-results.docx.

**How to run:** open `TECHNICAL-QUESTIONS.sql` in any SQL editor to review the queries. 
For the Python function, run `python3 TECHNICAL-PYTHON-QUES.py` after installing 
pandas (`pip install pandas`). `project-1-results.docx` shows the actual output of each 
query and function run against real sample data, that's the fastest way to see the 
results without setting anything up yourself.

## Project 2: Tableau
A cohort retention matrix, an NRR waterfall reconciled to the dollar, and a hard churn 
vs. soft churn monthly trend dashboard.

**How to run:** open the `.twbx` files in Tableau Public (free) or Tableau Desktop. 
`subscriptions.csv`, `mrr_history.csv`, and `nrr_waterfall.csv` are included as the 
underlying data, no need to regenerate anything. If you do want to regenerate 
`subscriptions.csv`, run `python3 generate_data.py`, you should see:
`Done! subscriptions.csv created with 5000 rows`

## Project 3: Snowflake
Covers warehouse scaling, query troubleshooting, the three-layer caching model, 
and two SQL queries against Snowflake's system views. Both queries were run against a 
live Snowflake trial account, one returned real results, the other returned 0 rows 
(expected on a brand-new account with no usage history). Full details and results are 
in project-3-results.pdf.

**How to run:** paste the contents of `TECHNICAL-QUESTION.sql` or 
`TECHNICAL-QUESTION-2.sql` into a Snowflake worksheet (Snowsight) and run. 
`project-3-results.pdf` shows exactly what both queries returned when I ran them, 
that's the quickest way to see the results without needing your own Snowflake account.

## Project 4: Architecture
The biggest cost/performance levers for a high-volume clickstream pipeline, an 
end-to-end architecture diagram, a partitioning strategy justified against two real 
query patterns, and a short comparison of Snowpipe vs. alternatives.

**How to run:** nothing to execute, open `architecture-diagram.png` to view the 
diagram, and `PARTITIONING-NOTES.md` / `THEORY-QUESTIONS.md` for the written reasoning.

## Project 5: Integration

A real example of a technically correct but misleading dashboard number, a rule of thumb for where to push calculation logic, a parameterized Python script, and a one-page executive dashboard for a non-technical CFO.

How to run: `pulldata-for-bi.py` was originally written for Postgres, and is included here tested against a local SQLite database instead, since Postgres wasn't actually running. Install pandas and sqlalchemy (`pip install pandas sqlalchemy`), then run `python3 pulldata-for-bi.py`. It connects to the included `subscriptions.db` file, no setup needed. You should see `Saved 4577 rows to subscriptions_last_900_days.csv` and `(4577, 9)`, followed by a preview of the first 10 rows of real customer data. `project-5-results.pdf` has the full screenshots of this exact run, plus a second run showing the default 30-day window, which returns 0 rows (expected, since the data's dates only go up to mid-2025, not an error). Change the `last_n_days` value at the top of the script to pull a different window yourself. Open `CFO_Summary.twbx` in Tableau Public to view the dashboard.

Note: this was tested against SQLite instead of Postgres, since Postgres wasn't set up locally. The only change needed to point this at a real Postgres or Snowflake database is the connection string in the script, everything else (the query, the parameter, the cleanup, the CSV output) stays exactly the same.

## What these projects brought me
Going in, Snowflake was a learning curve for me, and a few Tableau techniques 
(table calculations, LOD expressions, reference lines) took more trial and error than I 
expected. I didn't try to fake my way past the parts I didn't know. Where something
