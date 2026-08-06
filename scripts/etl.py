import argparse
import os
import pandas as pd


def clean_postings(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans job postings dataset."""
    df = df.drop_duplicates()
    if "job_location" in df.columns:
        df["job_location"] = (
            df["job_location"].fillna("Unknown").str.strip().str.title()
        )
    if "job_level" in df.columns:
        df["job_level"] = (
            df["job_level"].fillna("Not Specified").str.strip()
        )
    if "job_title" in df.columns:
        df["job_title"] = df["job_title"].str.strip().str.title()
    return df


def clean_details(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans jobs detail dataset."""
    df = df.drop_duplicates()
    if "skills" in df.columns:
        df["skills"] = df["skills"].fillna("[]")
    return df


def clean_ai_trends(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans AI job market trends dataset."""
    df = df.drop_duplicates()
    if "remote_type" in df.columns:
        df["remote_type"] = (
            df["remote_type"].fillna("Unknown").str.strip().str.capitalize()
        )
    return df


def run_pipeline(data_dir: str, output_dir: str):
    """Loads raw CSVs, runs cleaning functions, and exports to cleaned directory."""

    # Define paths
    postings_path = os.path.join(data_dir, "job_postings.csv")
    details_path = os.path.join(data_dir, "final_clean_jobs_dataset.csv")
    ai_path = os.path.join(data_dir, "AI_Job_Market_Trends_2026.csv")

    print(f" Reading raw datasets from: {data_dir}")
    df_postings = pd.read_csv(postings_path)
    df_clean = pd.read_csv(details_path)
    df_ai = pd.read_csv(ai_path)

    print(" Executing cleaning pipeline...")
    df_postings_cleaned = clean_postings(df_postings)
    df_clean_cleaned = clean_details(df_clean)
    df_ai_cleaned = clean_ai_trends(df_ai)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    print(f" Exporting cleaned files to: {output_dir}")
    df_postings_cleaned.to_csv(
        os.path.join(output_dir, "cleaned_job_postings.csv"), index=False
    )
    df_clean_cleaned.to_csv(
        os.path.join(output_dir, "cleaned_jobs_detail.csv"), index=False
    )
    df_ai_cleaned.to_csv(
        os.path.join(output_dir, "cleaned_ai_job_trends.csv"), index=False
    )

    print(" ETL PIPELINE COMPLETED SUCCESSFULLY!")


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
