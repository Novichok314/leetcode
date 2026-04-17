'''
We have a ClickHouse table raw_events with millions of rows.
 We need to build a daily aggregated table daily_summary.
Write:
The SQL query to populate the daily summary
How to structure an Airflow DAG so that:
It can be re-run for any specific date
It does not create duplicate data

Example Schema
Raw events table
CREATE TABLE raw_events (
   event_time   DateTime,
   user_id      UInt64,
   event_type   String,
   amount       Float64
)
ENGINE = MergeTree
PARTITION BY toYYYYMM(event_time)
ORDER BY (event_time, user_id);
Target daily summary table
CREATE TABLE daily_summary (
   event_date   Date,
   event_type   String,
   total_events UInt64,
   total_users  UInt64,
   total_amount Float64
)
ENGINE = MergeTree
PARTITION BY toYYYYMM(event_date)
ORDER BY (event_date, event_type);


'''

CREATE TABLE raw_events (
   event_time   DateTime,
   user_id      UInt64,
   event_type   String,
   amount       Float64
)


CREATE TABLE daily_summary (
   event_date   Date,
   event_type   String,
   total_events UInt64,
   total_users  UInt64,
   total_amount Float64
)

insert into daily_summary
select concat(", ", event_type)
       , count(event_type)
       , count(distinct user_id)
       , sum(amount)
group by event_time::Date
from raw_events