"""
QUESTION 24: Write a Python script that connects to Snowflake (or Postgres as a stand-in) via
snowflake-connector-python or sqlalchemy, pulls a parameterized query (configurable
"last N days"), and writes clean output to CSV/Parquet ready for BI consumption.
"""
import pandas as pd
from sqlalchemy import create_engine, text
db_file = "subscriptions.db"
last_n_days = 900
connection_string = "sqlite:///" + db_file
engine = create_engine(connection_string)
days_ago = "-" + str(last_n_days) + " days"
query = text("""
SELECT *
FROM subscriptions
WHERE start_date >= date('now', :days_ago)
""")
connection = engine.connect()
df = pd.read_sql(query, connection, params={"days_ago": days_ago})
connection.close()
df = df.dropna(how="all")
df.columns = [col.lower() for col in df.columns]
output_filename = "subscriptions_last_" + str(last_n_days) + "_days.csv"
df.to_csv(output_filename, index=False)
print("Saved " + str(len(df)) + " rows to " + output_filename)
print(df.shape)
print(df.head(10))
