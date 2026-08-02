---

## Project 1: SQL & Python
Near-duplicate detection, NULL handling pitfalls, anti-join patterns, a multi-table 
order reconciliation query, gateway retry deduplication, and a pandas function that 
reproduces that reconciliation logic and classifies flagged rows. Built a small 
synthetic database matching the assignment's schema and actually ran all three 
technical questions against it, real results included in project-1-results.docx.

**How to run:** open `TECHNICAL-QUESTIONS.sql` in any SQL editor to review the queries. 
For the Python function, run `python3 TECHNICAL-PYTHON-QUES.py` after installing 
pandas (`pip install pandas`). See `project-1-results.docx` for proof of live execution 
against sample data.

## Project 2: Tableau
A cohort retention matrix, an NRR waterfall reconciled to the dollar, and a hard churn 
vs. soft churn monthly trend dashboard.

**How to run:** open the `.twbx` files in Tableau Public (free) or Tableau Desktop. 
Underlying data was generated with the included Python scripts 
(`generate_data.py`, `generate_mrr_history.py`, `nrr_waterfall.py`); run with 
`python3 <script_name>.py` to regenerate the CSVs if needed.

## Project 3: Snowflake
I'd never used Snowflake before this assignment, and had to study the documentation as 
I went. Covers warehouse scaling, query troubleshooting, the three-layer caching model, 
and two SQL queries against Snowflake's system views. Both queries were run against a 
live Snowflake trial account, one returned real results, the other returned 0 rows 
(expected on a brand-new account with no usage history). Full details and results are 
in project-3-results.pdf.

**How to run:** paste the contents of `TECHNICAL-QUESTION.sql` or 
`TECHNICAL-QUESTION-2.sql` into a Snowflake worksheet (Snowsight) and run. See 
`project-3-results.pdf` for the results I got.

## Project 4: Architecture
The biggest cost/performance levers for a high-volume clickstream pipeline, an 
end-to-end architecture diagram, a partitioning strategy justified against two real 
query patterns, and a short comparison of Snowpipe vs. alternatives.

**How to run:** nothing to execute, open `architecture-diagram.png` to view the 
diagram, and `PARTITIONING-NOTES.md` / `THEORY-QUESTIONS.md` for the written reasoning.

## Project 5: Integration
A real example of a technically correct but misleading dashboard number, a rule of 
thumb for where to push calculation logic, a parameterized Python script, and a 
one-page executive dashboard for a non-technical CFO.

**How to run:** run `python3 pull_data_for_bi.py` after installing pandas and 
sqlalchemy (`pip install pandas sqlalchemy`), update the connection details at the 
top of the script to point at your own Postgres instance. Open `CFO_Summary.twbx` in 
Tableau Public to view the dashboard.

---

## What these projects brought me
Going in, Snowflake was a learning curve for me, and a few Tableau techniques 
(table calculations, LOD expressions, reference lines) took more trial and error than I 
expected. I didn't try to fake my way past the parts I didn't know. Where something 
didn't work the first time, like the retention matrix returning 100% everywhere, or the 
churn data having no date to trend against, I stopped, figured out why, and rebuilt it 
properly rather than settling for something that looked close enough. For the technical 
questions in Projects 1 and 3, I went further than just writing the queries, I built 
small synthetic databases matching the given schemas and actually ran everything 
against real data, so what's in this repo is proven, not just reasoned through.
