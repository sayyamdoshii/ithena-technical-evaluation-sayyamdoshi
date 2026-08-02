"""
QUESTION 24: Write a Python script that connects to Snowflake (or Postgres as a stand-in) via
snowflake-connector-python or sqlalchemy, pulls a parameterized query (configurable
"last N days"), and writes clean output to CSV/Parquet ready for BI consumption.
"""


import pandas as pd
from sqlalchemy import create_engine, text

username = "your_username"
password = "your_password"
host = "localhost"
port = "5432"
database = "your_database"
last_n_days = 30
conn_str = f"postgresql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(conn_str)

query = text("""
SELECT *
FROM subscriptions
WHERE start_date >= CURRENT_DATE - INTERVAL '1 day' * :days
""")

conn = engine.connect()
df = pd.read_sql(query, conn, params={"days": last_n_days})
conn.close()

print(df.shape)
print(df.head())
df = df.dropna(how="all")

new_cols = []
for col in df.columns:
new_cols.append(col.lower())
df.columns = new_cols

output_filename = "subscriptions_last_" + str(last_n_days) + "_days.csv"
df.to_csv(output_filename, index=False)

print("done, saved to", output_filename)
print("rows:", len(df))
