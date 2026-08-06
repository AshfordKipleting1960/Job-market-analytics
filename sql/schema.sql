-- Schema definition for Job Market Analytics
DROP TABLE IF EXISTS job_postings;

CREATE TABLE job_postings (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    company VARCHAR(255),
    location VARCHAR(255),
    work_type VARCHAR(50),          -- Remote, Hybrid, Onsite
    experience_level VARCHAR(50),   -- Mid-Senior, Associate, Entry, Executive
    years_experience NUMERIC,
    skills TEXT,                    -- Machine Learning, SQL, Python, etc.
    salary NUMERIC,
    posted_date DATE
);
