QUESTION 1: You're given a table with 500M rows and asked to find duplicates on a 
near-match basis (not an exact key match, e.g., same customer, same 
amount, within 2 minutes of each other). Why is a standard GROUP BY / 
DISTINCT insufficient here, and what approach would you actually use?

ANSWER: 
A normal GROUP BY or DISTINCT only works when rows are exactly the same. But in this case, the duplicates are not exactly the same, the timestamps are a little different and the amounts might not match perfectly either. So there's no way to just group by a few columns and catch these, because either you'll miss real duplicates that don't match exactly, or you'll accidentally group together rows that are actually different.
To handle this with 500 million rows, I would not try to compare every row to every other row, because that would take way too long. Instead, I would first split the data into smaller groups, for example grouping by customer_id, so I'm only comparing rows for the same customer instead of the whole table. Then within each customer's group, I would sort the rows by time and just check each row against the one right next to it. If the time gap is within 2 minutes and the amount is close, I would flag them as a duplicate. This way I'm only doing a small number of comparisons instead of checking everything against everything, which keeps it fast even with 500 million rows.

--------------------------------------------------------------------------------------------------------------------------------------

QUESTION 2: A colleague says “we should always use COALESCE to handle NULLs in aggregations.” Explain
one scenario where blindly doing this would silently produce a wrong business number — not just
a technically wrong query. 

ANSWER: 
COALESCE is helpful when you need a query to run smoothly, but blindly replacing every NULL with a default value like 0 can quietly change what the number actually means.
For example, say we're calculating the average discount customers received. If a discount value is NULL, that usually means no discount was applied or recorded, not that it was exactly 0%. If someone blindly turns every NULL into a 0, those missing values now count as real 0% discounts and get pulled into the average. This drags the average down and makes it look like customers are getting smaller discounts than they actually are.
The query still runs without any errors, so nothing looks broken on the surface. But the number it produces is now misleading. Someone might look at that average and make a pricing or marketing decision based on a trend that isn't actually real, all because NULL and 0 got treated as if they meant the same thing, when they don't.

---------------------------------------------------------------------------------------------------------------------------------------

QUESTION 3: What's the practical difference between a LEFT JOIN + WHERE IS NULL anti-join pattern vs. NOT
IN vs. NOT EXISTS for finding orders with no matching payment — specifically around NULL
handling and performance? Which would you default to, and why?

ANSWER: 

