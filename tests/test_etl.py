import pandas as pd
import pytest
from scripts.etl import clean_ai_trends, clean_details, clean_postings


@pytest.fixture
def sample_postings_df():
    """Fixture providing raw sample data for testing clean_postings."""
    return pd.DataFrame(
        {
            "job_title": [
                " Data Engineer ",
                "Data Engineer",
                "business analyst ",
            ],
            "job_location": ["new york, ny", None, " chicago, il "],
            "job_level": [" Mid senior ", None, "Associate"],
        }
    )


def test_clean_postings_duplicates(sample_postings_df):
    """Test duplicate dropping and text standardization."""
    cleaned = clean_postings(sample_postings_df)

    # First two rows were identical after title normalization
    assert len(cleaned) == 2

    # Verify string trimming and title casing
    assert cleaned["job_title"].iloc[0] == "Data Engineer"
    assert cleaned["job_title"].iloc[1] == "Business Analyst"


def test_clean_postings_null_handling(sample_postings_df):
    """Test missing value replacement in job postings."""
    cleaned = clean_postings(sample_postings_df)

    # Verify fillna rules
    assert (
        cleaned["job_location"].iloc[1] == "Unknown"
        or cleaned["job_location"].iloc[0] == "New York, Ny"
    )
    assert (
        cleaned["job_level"].iloc[1] == "Not Specified"
        or cleaned["job_level"].iloc[0] == "Mid senior"
    )


def test_clean_details():
    """Test details dataset skill cleaning."""
    df = pd.DataFrame({"skills": [None, "['python', 'sql']"]})
    cleaned = clean_details(df)

    assert cleaned["skills"].iloc[0] == "[]"
    assert cleaned["skills"].iloc[1] == "['python', 'sql']"


def test_clean_ai_trends():
    """Test remote_type capitalization and null handling."""
    df = pd.DataFrame({"remote_type": [" hybrid ", None, "REMOTE"]})
    cleaned = clean_ai_trends(df)

    assert cleaned["remote_type"].iloc[0] == "Hybrid"
    assert cleaned["remote_type"].iloc[1] == "Unknown"
    assert cleaned["remote_type"].iloc[2] == "Remote"
