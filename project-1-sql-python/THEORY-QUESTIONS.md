QUESTION 1: You're given a table with 500M rows and asked to find duplicates on a 
near-match basis (not an exact key match, e.g., same customer, same 
amount, within 2 minutes of each other). Why is a standard GROUP BY / 
DISTINCT insufficient here, and what approach would you actually use?

ANSWER: 
A normal GROUP BY or DISTINCT only works when rows are exactly the same. But in this case, the duplicates are not exactly the same, the timestamps are a little different and the amounts might not match perfectly either. So there's no way to just group by a few columns and catch these, because either you'll miss real duplicates that don't match exactly, or you'll accidentally group together rows that are actually different.
To handle this with 500 million rows, I would not try to compare every row to every other row, because that would take way too long. Instead, I would first split the data into smaller groups, for example grouping by customer_id, so I'm only comparing rows for the same customer instead of the whole table. Then within each customer's group, I would sort the rows by time and just check each row against the one right next to it. If the time gap is within 2 minutes and the amount is close, I would flag them as a duplicate. This way I'm only doing a small number of comparisons instead of checking everything against everything, which keeps it fast even with 500 million rows.
