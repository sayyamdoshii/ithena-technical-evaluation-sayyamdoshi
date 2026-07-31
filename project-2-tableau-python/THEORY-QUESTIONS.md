QUESTION 7: Your manager wants “one number” for churn on the homepage of a dashboard. Explain, in your
own words, why a single monthly churn % is often misleading to leadership, and what you'd show
alongside it instead.

ANSWER: 
A single churn number sounds simple, but it hides a lot. It doesn't show if churn is getting better or worse over time, if it's coming from one type of customer more than others, or if a few big customers leaving is skewing the number just as much as many small ones. It also mixes together customers who chose to leave with customers who left because of something like a failed payment, and those two situations need very different responses.

"For example: Assume we have a members table with membership_type and monthly_fee, and a subscriptions table with a cancellation_date and cancellation_reason. If churn is 5% one month at a gym, that number alone doesn't tell us if it's mostly casual, month to month members leaving, which may not be a big deal, or several premium members with personal training packages leaving, which is a much bigger loss even though the percentage looks the same.".

Along with the single number, I'd also show how churn is trending over time, a breakdown by customer type, and how much of it is voluntary versus involuntary, so leadership sees the real picture instead of just one number.

----------------------------------------------------------------------------------------------------------------------------------------

QUESTION 8: What's the difference between a calculated column and a measure in Power BI (or a calculated
field vs. an LOD expression in Tableau), and why does that distinction matter for a cohort retention
calculation specifically?

ANSWER:

A calculated column in Power BI works on one row at a time, and the answer gets saved permanently in the table. A measure doesn't get saved at all, it gets calculated fresh every time, based on whatever filters are being used in the chart. In Tableau, it's the same idea, a calculated field usually works row by row, while an LOD expression lets you decide exactly what level the calculation happens at, no matter how the chart is filtered.

This matters a lot for cohort retention, because retention isn't something you can figure out from just one row. It depends on comparing a customer's activity across several months, compared to when they first joined.

"For example, assume we have a customers table with signup_month, and an activity table with activity_month. If I used a calculated column to mark someone as "retained," that answer would get locked in based on the row it was created on, and it wouldn't update correctly if someone later filters the dashboard down to just one month or one group of customers. A measure, or an LOD expression in Tableau, can recalculate retention correctly every time, no matter what someone clicks on in the dashboard, which is exactly what a retention report needs to work properly."

---------------------------------------------------------------------------------------------------------------------------------------


