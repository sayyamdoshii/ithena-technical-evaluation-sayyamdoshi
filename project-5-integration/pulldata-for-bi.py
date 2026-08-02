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
