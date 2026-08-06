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
    "password": "your_password",  # Update with your MySQL password
    "database": "job_market_db"
}

def load_data():
    if not CSV_PATH.exists():
        print(f"❌ Error: Cleaned data not found at {CSV_PATH}")
        print("Run the ETL pipeline first: python scripts/etl.py")
        return

    try:
        print("🔌 Connecting to MySQL database...")
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS job_market_db")
        cursor.execute("USE job_market_db")

        print("📋 Executing schema from sql/schema.sql...")
        with open(SCHEMA_PATH, "r") as schema_file:
            schema_sql = schema_file.read()
            for statement in schema_sql.split(";"):
                if statement.strip():
                    cursor.execute(statement)

        print(f"📥 Loading dataset into database from {CSV_PATH.name}...")
        df = pd.read_csv(CSV_PATH)
        
        # Column mapping: CSV columns -> Database columns
        # Adjust these based on your actual CSV column names
        column_mapping = {
            "job_title": "title",
            "company_name": "company",
            "job_location": "location",
            "work_type": "work_type",
            "job_level": "experience_level",
            "years_exp": "years_experience",
            "skills": "skills",
            "salary": "salary",
            "posted_date": "posted_date"
        }
        
        # Rename columns to match database schema
        df = df.rename(columns=column_mapping)
        
        # Keep only columns needed for database
        required_cols = ["title", "company", "location", "work_type", "experience_level", "years_experience", "skills", "salary", "posted_date"]
        available_cols = [col for col in required_cols if col in df.columns]
        df = df[available_cols]
        
        # Replace NaN with None for SQL NULL
        df = df.where(pd.notna(df), None)
        
        # Bulk insert into job_postings table
        insert_count = 0
        for _, row in df.iterrows():
            # Build dynamic SQL based on available columns
            cols = ", ".join(available_cols)
            placeholders = ", ".join(["%s"] * len(available_cols))
            sql = f"INSERT INTO job_postings ({cols}) VALUES ({placeholders})"
            cursor.execute(sql, tuple(row))
            insert_count += 1
        
        conn.commit()

        # Verification query
        cursor.execute("SELECT COUNT(*) FROM job_postings")
        count = cursor.fetchone()[0]
        print(f"✅ Successfully loaded {count:,} records into 'job_postings'!")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"❌ MySQL Error: {err}")
        print("💡 Make sure MySQL is running and your password is correct in DB_CONFIG")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    load_data()
