QUESTION 13: Explain, in your own words, the difference between scaling a Snowflake warehouse up vs. out,
and give one real scenario for each where you'd choose it

ANSWER:
Scaling up means making a single warehouse bigger, moving from a Small to a Medium to a Large, so each query gets more compute power to work with. Scaling out means adding more clusters of the same size running in parallel, through multi-cluster warehouses. The difference comes down to what kind of problem you're solving. If a single query is slow because it's crunching a huge amount of data or doing heavy joins, scaling up helps since it gives that one query more horsepower. If the problem is that too many people are running queries at the same time and they're all queuing up waiting for a turn, scaling out helps more, since it spreads that concurrent load across multiple clusters instead of making each individual query faster. A good real scenario for scaling up: a single nightly ETL job that reshapes millions of rows and needs to finish faster. A good scenario for scaling out: a BI dashboard that fifty analysts are all querying at 9am, where the bottleneck is queueing, not any one query being slow.

---------------------------------------------------------------------------------------------------------------------------------------

QUESTION 14: A query joining a 2-billion-row fact table to a 50-million-row dimension table is timing out. List
the top 3 things you'd check first, and name the specific Snowflake system view or command for
each.

ANSWER:
First, I'd check the Query Profile in Snowsight, since it shows exactly where time is being spent step by step and will usually point straight at the join or a spill to disk as the bottleneck. Second, I'd check whether the warehouse is spilling to local or remote storage during the join, which shows up in the Query Profile as "bytes spilled," since that means the warehouse size is too small for the amount of data being shuffled around, and a bigger warehouse would likely fix it. Third, I'd check QUERY_HISTORY in ACCOUNT_USAGE to see if this query is competing with other queries on the same warehouse, causing it to queue rather than actually run slow, which would point to a concurrency problem rather than a data volume problem.

---------------------------------------------------------------------------------------------------------------------------------------

