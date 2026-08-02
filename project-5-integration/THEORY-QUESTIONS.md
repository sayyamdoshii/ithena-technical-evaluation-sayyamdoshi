QUESTION 22: Describe (200 words max) a real or hypothetical case where a dashboard number you 
built was "technically correct but practically misleading" to a stakeholder. What caused 
it, and what would you change in your process to catch this earlier?

ANSWER:

While building an NRR waterfall dashboard, I had a "Churned" category showing customers 
whose subscriptions ended. The number was technically correct, calculated straight from 
the end_date column, but it was practically misleading because it lumped together two 
very different situations: customers who fully cancelled and left, and customers who had 
simply downgraded to a cheaper plan but were still active, generating revenue. A 
stakeholder glancing at "churn" going up might assume the business was bleeding customers, 
when in reality a chunk of that number was still-active, still-paying customers who just 
moved to a lower tier.

The root cause was that I built the number from whatever column was easiest to query, 
end_date, without stepping back to ask whether that column actually represented the 
business concept the stakeholder cared about. What I'd change in my process: before 
building any metric, I'd ask what decision the stakeholder is trying to make with this 
number, and check whether the underlying data actually distinguishes between the 
scenarios that decision depends on. In this case, that meant separating hard churn from 
soft churn as two distinct trends instead of one blended number.

---------------------------------------------------------------------------------------------------------------------------------------

QUESTION 23: When would you choose to push a calculation into SQL/the warehouse vs. doing it in 
Python/pandas vs. doing it as a DAX measure/LOD expression in the BI layer? Give one clear 
rule of thumb.

ANSWER:

My rule of thumb: push it as far upstream as the logic will allow without needing 
row-by-row conditional branching, and only bring it into the BI layer when it needs to 
change based on how the user is currently filtering or slicing the dashboard.

SQL/the warehouse is the right place for anything that's a fixed, reusable definition, 
joins, aggregations, deduplication, filtering out bad rows, things that should be true no 
matter who's looking at the data or how they've filtered it. Doing this in SQL means every 
tool downstream (BI, Python, anyone else) gets the same clean answer.

Python/pandas is the right place when the logic is too complex or conditional for SQL to 
express cleanly, classifying rows into multiple categories based on layered business rules, 
or when I need to loop through data doing something SQL genuinely can't do in one query.

DAX/LOD in the BI layer is the right place only when the calculation genuinely depends on 
the user's current view, like a running total that changes based on which date range 
someone has selected, since that kind of context-dependent logic doesn't make sense to 
bake into the raw data itself.

---------------------------------------------------------------------------------------------------------------------------------------
