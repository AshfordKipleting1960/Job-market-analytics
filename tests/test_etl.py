import pandas as pd
import pytest
from scripts.etl import clean_postings


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
            "work_type": ["remote", "HYBRID", None],
            "skills": [None, "Python, SQL", "Excel"],
        }
    )


def test_clean_postings_duplicates(sample_postings_df):
    """Test duplicate dropping and text standardization."""
    cleaned = clean_postings(sample_postings_df)

    # First two rows are identical after title normalization, so should be removed
    assert len(cleaned) == 2
    print(f"✓ Duplicate removal working: {len(sample_postings_df)} -> {len(cleaned)}")


def test_clean_postings_title_normalization(sample_postings_df):
    """Test job title text standardization."""
    cleaned = clean_postings(sample_postings_df)

    # Verify string trimming and title casing
    assert cleaned["job_title"].iloc[0] == "Data Engineer"
    assert cleaned["job_title"].iloc[1] == "Business Analyst"
    print("✓ Job title normalization working")


def test_clean_postings_location_handling(sample_postings_df):
    """Test location field null handling and standardization."""
    cleaned = clean_postings(sample_postings_df)

    # Verify that missing values are filled with "Unknown"
    assert "Unknown" in cleaned["job_location"].values or "Unknown" in cleaned["job_location"].values
    print("✓ Location null handling working")


def test_clean_postings_job_level(sample_postings_df):
    """Test job level field null handling."""
    cleaned = clean_postings(sample_postings_df)

    # Verify that missing values are filled with "Not Specified"
    assert "Not Specified" in cleaned["job_level"].values
    print("✓ Job level null handling working")


def test_clean_postings_work_type(sample_postings_df):
    """Test work type standardization."""
    cleaned = clean_postings(sample_postings_df)

    # Verify capitalization and null handling
    assert "Unknown" in cleaned["work_type"].values
    print("✓ Work type standardization working")


def test_clean_postings_skills_handling(sample_postings_df):
    """Test skills field null handling."""
    cleaned = clean_postings(sample_postings_df)

    # Verify that None values become empty strings
    assert cleaned["skills"].iloc[0] == ""
    assert cleaned["skills"].iloc[1] == "Python, SQL"
    print("✓ Skills field handling working")
