# Project 5: Integration

## What this is
Covers the reasoning side of BI work, when to push logic into SQL vs. Python vs. the BI 
layer, and what "technically correct but misleading" looks like in practice, plus two hands-on 
pieces: a Python script that pulls data on a schedule, and a one-page executive dashboard.

## Files
- `THEORY-QUESTIONS.md`: written answers on misleading dashboard numbers and where to push 
calculation logic
- `pulldata-for-bi.py`: parameterized script that connects to a database, pulls the last N 
days, and saves clean output to CSV. Connects to SQLite here, see the note below for why
- `subscriptions.db`: SQLite database the script connects to, includes the synthetic 
subscription data used across this project and Project 2
- `subscriptions_last_900_days.csv`: real output from running `pulldata-for-bi.py`
- `pulldata-for-bi-results.pdf`: proof of running the script for real, including both a 
0-row result on the default 30-day window (expected, since the data only goes up to 
mid-2025) and a 4,577-row result once the window was widened, confirming the query logic 
actually works
- `CFO Summary.twb`: one-page executive dashboard built for a non-technical CFO
- `CFO Summary.png`: preview of the dashboard without needing to open Tableau

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
- "Last N days" is a single variable at the top of the script (`last_n_days`), change that 
one number and the whole query adjusts, no other part of the script needs to be touched
- Cleans the output (drops empty rows, standardizes column names) before saving to CSV
- Actually run for real against `subscriptions.db`, not just written and left untested

Note: `pulldata-for-bi.py` connects to SQLite, not Postgres. The question allows Postgres 
as a stand-in for Snowflake, but Postgres wasn't set up locally, so this connects to a 
local SQLite database (`subscriptions.db`) instead, which is included in this folder. The 
only change needed to point this at Postgres or Snowflake instead is the connection 
string, everything else (the query, the parameter, the cleanup, the CSV output) stays 
the same.

Note: commands above use `python3` and `pip3`, which work on Mac and Linux. On Windows, use 
`python` and `pip` instead (no "3" at the end). Everything else in the script and the steps 
stays the same.

**One-page CFO dashboard (Technical Question 25)**
- One big number (current MRR) plus one trend line, nothing else
- Deliberately left out cohort breakdowns, region splits, and churn-type distinctions, 
those are analyst tools, not something a CFO needs to interpret in a 30-second glance
- The dashboard reflects MRR through the most recent complete month in the dataset 
(September 2026: $21,670). Data beyond that point trails toward zero in the underlying 
file, which is a known artifact of how the synthetic dataset was generated, not a real 
revenue signal
