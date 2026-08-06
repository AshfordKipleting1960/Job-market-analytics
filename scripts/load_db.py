import sqlite3
import pandas as pd
from pathlib import Path

# Resolve base repository path
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "cleaned" / "job_postings_cleaned.csv"
DB_PATH = BASE_DIR / "data" / "job_market.db"
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"

def load_data():
    if not CSV_PATH.exists():
        print(f" Error: Cleaned data not found at {CSV_PATH}")
        print(" Run the ETL pipeline first: python scripts/etl.py")
        return

    print("🔌 Connecting to local SQLite database...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(" Executing schema from sql/schema.sql...")
    with open(SCHEMA_PATH, "r") as schema_file:
        cursor.executescript(schema_file.read())

    print(f" Loading dataset into database from {CSV_PATH.name}...")
    df = pd.read_csv(CSV_PATH)
    
    # Bulk insert into job_postings table
    df.to_sql("job_postings", conn, if_exists="append", index=False)
    conn.commit()

    # Verification query
    cursor.execute("SELECT COUNT(*) FROM job_postings;")
    count = cursor.fetchone()[0]
    print(f" Successfully loaded {count:,} records into table 'job_postings'!")

    conn.close()

if __name__ == "__main__":
    load_data()
