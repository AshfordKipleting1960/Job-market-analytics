import argparse
import os
import pandas as pd


def clean_postings(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans job postings dataset: removes duplicates and standardizes text fields."""
    df = df.drop_duplicates()
    
    # Standardize location field
    if "job_location" in df.columns:
        df["job_location"] = (
            df["job_location"].fillna("Unknown").str.strip().str.title()
        )
    
    # Standardize experience level field
    if "job_level" in df.columns:
        df["job_level"] = (
            df["job_level"].fillna("Not Specified").str.strip()
        )
    
    # Standardize job title field
    if "job_title" in df.columns:
        df["job_title"] = df["job_title"].str.strip().str.title()
    
    # Handle work type field
    if "work_type" in df.columns:
        df["work_type"] = (
            df["work_type"].fillna("Unknown").str.strip().str.capitalize()
        )
    
    # Handle skills field (ensure empty values are standardized)
    if "skills" in df.columns:
        df["skills"] = df["skills"].fillna("")
    
    return df


def run_pipeline(data_dir: str, output_dir: str):
    """
    Loads raw CSV, cleans it, and exports to cleaned directory.
    
    Expected input file: job_postings.csv (raw data from job listings)
    Output file: cleaned_job_postings.csv (cleaned and ready for database)
    """

    # Define paths
    postings_path = os.path.join(data_dir, "job_postings.csv")

    # Check if input file exists
    if not os.path.exists(postings_path):
        print(f"❌ Error: {postings_path} not found!")
        print(f"   Please add your job_postings.csv file to {data_dir}/")
        return

    print(f"📂 Reading raw dataset from: {data_dir}")
    try:
        df_postings = pd.read_csv(postings_path)
        print(f"   Loaded {len(df_postings):,} records")
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return

    print("🧹 Executing cleaning pipeline...")
    df_postings_cleaned = clean_postings(df_postings)
    print(f"   After deduplication: {len(df_postings_cleaned):,} records")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    print(f"💾 Exporting cleaned files to: {output_dir}")
    output_path = os.path.join(output_dir, "cleaned_job_postings.csv")
    df_postings_cleaned.to_csv(output_path, index=False)
    print(f"   ✅ Saved to {output_path}")

    print(" ETL PIPELINE COMPLETED SUCCESSFULLY!")
    print(f"\n📊 Summary:")
    print(f"   - Input records: {len(df_postings):,}")
    print(f"   - Output records: {len(df_postings_cleaned):,}")
    print(f"   - Duplicates removed: {len(df_postings) - len(df_postings_cleaned):,}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run ETL process for Job Market Analytics"
    )
    parser.add_argument(
        "--data_dir",
        type=str,
        default="data/raw",
        help="Directory where raw CSV files are stored",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="data/cleaned",
        help="Directory to save cleaned CSV files",
    )

    args = parser.parse_args()
    run_pipeline(args.data_dir, args.output_dir)
