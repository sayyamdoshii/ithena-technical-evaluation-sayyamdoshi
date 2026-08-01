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
QUESTION 14: What is the difference between Snowflake's result cache, local disk (warehouse) cache, and the
remote storage layer — and how does understanding this change how you'd explain a “why did
this query run fast the second time” question to a non-technical stakeholder?

ANSWER:
These are three different layers, and each one explains a different reason a query might run fast the second time. The result cache is the fastest, if you run the exact same query again with no changes to the underlying data, Snowflake just hands back the answer it already computed, no compute needed at all. The warehouse (local disk) cache is the next layer down, it holds recently used data files on the actual compute nodes, so if you run a similar but not identical query, the warehouse doesn't need to pull that data back from storage. The remote storage layer is the actual home for all your data, and it's the slowest of the three since it involves an actual retrieval over the network. If I were explaining "why did this run fast the second time" to a non-technical stakeholder, I'd probably use an analogy like: the first time you asked a question, someone had to go to the archive room and pull the file. The second time, that file was still sitting on their desk, so they just handed it back to you instantly.

---------------------------------------------------------------------------------------------------------------------------------------

