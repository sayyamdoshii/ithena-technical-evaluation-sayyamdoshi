# Project 5: Integration

## What this is
Covers the reasoning side of BI work, when to push logic into SQL vs. Python vs. the BI 
layer, and what "technically correct but misleading" looks like in practice, plus two hands-on 
pieces: a Python script that pulls data on a schedule, and a one-page executive dashboard.

## Files
- `THEORY-QUESTIONS.md`: written answers on misleading dashboard numbers and where to push 
calculation logic
- `pulldata-for-bi.py`: parameterized script that connects to a database, pulls the last N 
days, and saves clean output to CSV. Written for Postgres originally, tested here against a 
local SQLite database since Postgres wasn't actually running
- `generate_data.py`: generates the synthetic subscription data used across this project and 
Project 2. Real subscription data isn't something you can get for an assignment like this 
since it's sensitive business data, so this creates 5,000 fake customers instead, with 
realistic patterns like most customers churning earlier and fewer sticking around long term
- `build_db.py`: loads `subscriptions.csv` into a local SQLite database (`subscriptions.db`), 
standing in for the Postgres/Snowflake database the script is meant to run against
- `subscriptions.csv`: the synthetic data itself, 5,000 rows
- `subscriptions_last_900_days.csv`: real output from running `pulldata-for-bi.py`
- `project-5-results.pdf`: proof of running the script for real, including both a 0-row 
result on the default 30-day window (expected, since the data only goes up to mid-2025) and 
a 4,577-row result once the window was widened, confirming the query logic actually works
- `CFO_Summary.twbx`: one-page executive dashboard built for a non-technical CFO
- `CFO_Summary_screenshot.png`: preview of the dashboard without needing to open Tableau

## What's covered

**Technically correct but misleading (Theory Question 22)**
- Used a real example from this same project: the NRR waterfall's "Churned" number lumped 
together customers who fully cancelled with customers who just downgraded but were still 
active, technically correct, but misleading if read at face value
- What I'd change: ask what decision the stakeholder is trying to make before building the 
metric, not just what's easiest to query

**Where to push calculation logic (Theory Question 23)**
- Rule of thumb: push logic as far upstream as it'll go without needing row-by-row 
conditionals, and only bring it into the BI layer when it depends on how the user is 
currently filtering
- SQL for fixed, reusable definitions. Python for complex conditional logic. DAX/LOD only 
for things that genuinely change based on the viewer's current selection

**Parameterized data pull script (Technical Question 24)**
- Connects via SQLAlchemy (Postgres as the stand-in for Snowflake, per the assignment's 
own allowance)
- "Last N days" is a single variable at the top of the script (`last_n_days`), change that 
one number and the whole query adjusts, no other part of the script needs to be touched. 
Testing a different window just means changing that number, saving, and running the script 
again, it'll automatically save a new CSV named after whatever number was used
- Cleans the output (drops empty rows, standardizes column names) before saving to CSV
- Actually run against a local SQLite database built from this project's own synthetic data, 
not just written and left untested. The only change from the Postgres version is the 
connection string and the date filter syntax, since SQLite doesn't support Postgres's 
`INTERVAL` syntax. Full run details are in `project-5-results.pdf`

**One-page CFO dashboard (Technical Question 25)**
- One big number (current MRR) plus one trend line, nothing else
- Deliberately left out cohort breakdowns, region splits, and churn-type distinctions, 
those are analyst tools, not something a CFO needs to interpret in a 30-second glance
- The dashboard reflects MRR through the most recent complete month in the dataset 
(September 2026: $21,670). Data beyond that point trails toward zero in the underlying 
file, which is a known artifact of how the synthetic dataset was generated, not a real 
revenue signal
