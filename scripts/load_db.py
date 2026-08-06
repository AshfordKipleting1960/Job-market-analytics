import mysql.connector
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "cleaned" / "cleaned_job_postings.csv"
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"

# MySQL connection config
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",  # Use env vars in production
    "database": "job_market_db"
}

def load_data():
    if not CSV_PATH.exists():
        print(f" Error: Cleaned data not found at {CSV_PATH}")
        print("Run the ETL pipeline first: python scripts/etl.py")
        return

    try:
        print(" Connecting to MySQL database...")
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS job_market_db")
        cursor.execute("USE job_market_db")

        print("📋 Executing schema from sql/schema.sql...")
        with open(SCHEMA_PATH, "r") as schema_file:
            schema_sql = schema_file.read()
            # Execute each statement separately for MySQL
            for statement in schema_sql.split(";"):
                if statement.strip():
                    cursor.execute(statement)

        print(f" Loading dataset into database from {CSV_PATH.name}...")
        df = pd.read_csv(CSV_PATH)
        
        # Bulk insert into job_postings table
        for _, row in df.iterrows():
            sql = """
            INSERT INTO job_postings 
            (title, company, location, work_type, experience_level, years_experience, skills, salary, posted_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, tuple(row))
        
        conn.commit()

        # Verification query
        cursor.execute("SELECT COUNT(*) FROM job_postings")
        count = cursor.fetchone()[0]
        print(f" Successfully loaded {count:,} records into 'job_postings'!")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f" MySQL Error: {err}")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    load_data()
