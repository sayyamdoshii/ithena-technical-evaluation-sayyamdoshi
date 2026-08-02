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

