# Project 4: Architecture

## What this is
A system design exercise around a clickstream data pipeline, 200GB/day of semi-structured JSON landing in cloud storage hourly, needing to be queryable within an hour at reasonable cost. Covers the reasoning behind the pipeline design, an actual architecture diagram, partitioning strategy, and one cloud service comparison.

## Files
- `THEORY-QUESTIONS.md`: written answer on the biggest cost/performance levers in a pipeline like this
- `architecture-diagram.png`: end-to-end diagram built in draw.io, raw JSON landing all the way through to the BI tool
- `PARTITIONING-NOTES.md`: partitioning/clustering strategy, justified against two real query patterns, plus the Snowpipe vs. alternatives reasoning

## What's covered

**Biggest cost/performance levers (Theory Question 18)**
- Three things matter most here: file format, partitioning, and load frequency
- Converting raw JSON to a columnar format (like Parquet) as part of the load cuts both storage cost and scan time
- Partitioning by date/hour means a query for "today" only touches today's files, not the whole history
- Hourly loads hit the "queryable within an hour" requirement without paying the overhead of loading more often than needed

**End-to-end architecture diagram (Technical Question 19)**
- Five stages, drawn out and labeled: Clickstream Source → Cloud Storage (S3) → Snowpipe → Snowflake (transformed layer) → BI Tool
- Each box names the actual tool/service used at that stage, not just a generic label
- Arrows between boxes are labeled with what's happening at each handoff (hourly, auto-ingest, transform, query)
- Built by hand in draw.io rather than generated, so I actually understand what each stage is doing and why it's there

**Partitioning/clustering strategy (Technical Question 20)**
- Clustered the Snowflake table by event_date, with device_type as a secondary key
- Justified against two query patterns analysts would actually run: "DAU by day" (benefits from date clustering, since Snowflake can skip straight to that day's data) and "sessions by device" (benefits from the secondary device_type key, so it doesn't have to scan every device type across the date range)

**Snowpipe vs. alternatives (Technical Question 21)**
- Named Snowpipe as the service I'd use to move files from S3 into Snowflake
- Compared it directly against the two named alternatives: a scheduled COPY command (wastes compute checking for files that aren't there yet, or introduces lag if a file lands right after a scheduled run) and a custom script (means rebuilding file detection, retry logic, and error handling that Snowpipe already provides out of the box)
- Kept this one intentionally short, per the assignment's own note that this question is meant to check reasoning, not a full cloud build-out
