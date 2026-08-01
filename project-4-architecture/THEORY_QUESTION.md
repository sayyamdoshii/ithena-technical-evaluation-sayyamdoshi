QUESTION 18: A client's clickstream data (~200GB/day, semi-structured JSON) lands in cloud storage 
hourly and needs to be queryable by analysts within an hour of arrival, at reasonable cost. 
In 150 words, what are the 2-3 biggest cost/performance levers in a pipeline like this 
(think file format, partitioning, load frequency)? No diagram needed for this part, 
reasoning only.

ANSWER:

The biggest lever is file format. Raw JSON is expensive to scan since it's row-based and 
uncompressed, so converting it to a columnar format like Parquet as part of the hourly 
load would cut both storage cost and query time significantly, since analysts querying 
specific columns wouldn't need to scan the entire file.

The second lever is partitioning. Since data lands hourly, partitioning by date and hour 
means a query asking for "today's data" only scans that day's files instead of the entire 
200GB/day history, which keeps both cost and query speed reasonable as the dataset grows 
over time.

The third lever is load frequency itself. Loading hourly, rather than in smaller 
near-real-time micro-batches, keeps warehouse compute costs down, since each load has 
fixed overhead, and hourly is already frequent enough to meet the "queryable within an 
hour" requirement without over-spending on load frequency.

----------------------------------------------------------------------------------------------------------------------------------------
