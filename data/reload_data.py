# This file reloads CSV data into MySQL automatically

import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# MySQL connection
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Create MySQL engine
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Read CSV file
df = pd.read_csv("data/online_shoppers_intention.csv")

# Clean column names
df.columns = [col.strip().replace(" ", "_") for col in df.columns]

# Convert TRUE/FALSE values
df["Weekend"] = df["Weekend"].astype(int)
df["Revenue"] = df["Revenue"].astype(int)

# Drop table if exists
with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS online_shoppers"))
    conn.commit()

# Load dataframe into MySQL
df.to_sql(
    name="online_shoppers",
    con=engine,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(df)} rows into MySQL table: online_shoppers")