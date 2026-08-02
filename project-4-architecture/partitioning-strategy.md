QUESTION 20: On the diagram or in accompanying notes, specify your partitioning/clustering strategy 
and justify it against two concrete query patterns analysts will run (e.g., "DAU by day," 
"sessions by device").

ANSWER: 
Partitioning/clustering strategy: the transformed table in Snowflake is clustered by 
event_date, with device_type as a secondary clustering key. Cloud storage files are also 
organized into date/hour folders before they even reach Snowflake, so pruning happens at 
both the storage layer and the warehouse layer.

Query pattern 1: "DAU by day"
This query filters and groups by a single date, so clustering on event_date means Snowflake 
can skip straight to the micro-partitions containing that day's data instead of scanning the 
full table. Without this, a query for one day out of a growing multi-month dataset would get 
slower every day as more historical data piles up, even though the actual amount of relevant 
data being queried stays the same.

Query pattern 2: "Sessions by device"
This query groups by device_type across a date range, so clustering on device_type as a 
secondary key means Snowflake can prune down to just the relevant device rows within the 
already-narrowed date partitions, rather than scanning every device type and filtering 
afterward. Combining both clustering keys means this two-dimensional query pattern, date 
range plus device breakdown, still only touches the specific slice of data it needs.

----------------------------------------------------------------------------------------------------------------------------------------
QUESTION 21: Light cloud touch-point (reasoning only, no build required): if raw files land in S3 
before reaching Snowflake, name the one service you'd use to move data from S3 into 
Snowflake efficiently, and in 2-3 sentences explain why, over the alternatives (e.g., 
Snowpipe vs. a scheduled COPY vs. a custom script).

ANSWER:

I'd use Snowpipe. Snowpipe uses event notifications from S3 to detect new files the 
moment they land, then loads them automatically within minutes, so data is available to 
query almost immediately after arrival, without anyone needing to trigger anything.

A scheduled COPY command, by comparison, runs on a fixed timer (say, every 15 minutes), 
so it either wastes compute checking for files that haven't arrived yet, or introduces 
unnecessary lag if a file lands right after a scheduled run just finished, meaning it 
could sit unloaded for nearly the full interval before the next check.

A custom script would mean building and maintaining your own logic to watch S3 for new 
files, trigger a load, handle retries if a load fails partway through, and monitor for 
errors, all of which Snowpipe already provides out of the box as a managed service. That's 
extra engineering time spent recreating something Snowflake already built, tested, and 
maintains, with more surface area for something to quietly break.

----------------------------------------------------------------------------------------------------------------------------------------
