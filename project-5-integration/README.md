# Project 5: Integration

## What this is
Covers the reasoning side of BI work, when to push logic into SQL vs. Python vs. the BI 
layer, and what "technically correct but misleading" looks like in practice, plus two hands-on 
pieces: a Python script that pulls data on a schedule, and a one-page executive dashboard.

## Files
- `THEORY-QUESTIONS.md`: written answers on misleading dashboard numbers and where to push 
calculation logic
- `pull_data_for_bi.py`: parameterized Python script that connects to a database, pulls 
the last N days, and saves clean output to CSV
- `CFO_Summary.twbx`: one-page executive dashboard built for a non-technical CFO
- `CFO_Summary_screenshot.png`: preview of the dashboard without needing to open Tableau
- `subscriptions.csv`: reference data showing the shape of the source table the script 
queries against (the script connects to a live database, it doesn't read this file directly)

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
- "Last N days" is a single variable at the top of the script, change it and the whole 
query adjusts
- Cleans the output (drops empty rows, standardizes column names) before saving to CSV

**One-page CFO dashboard (Technical Question 25)**
- One big number (current MRR) plus one trend line, nothing else
- Deliberately left out cohort breakdowns, region splits, and churn-type distinctions, 
those are analyst tools, not something a CFO needs to interpret in a 30-second glance
- The dashboard reflects MRR through the most recent complete month in the dataset 
(September 2026: $21,670). Data beyond that point trails toward zero in the underlying 
file, which is a known artifact of how the synthetic dataset was generated, not a real 
revenue signal
