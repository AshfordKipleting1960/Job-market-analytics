-- Schema definition for Job Market Analytics (MySQL)
DROP TABLE IF EXISTS job_postings;

CREATE TABLE job_postings (
    job_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    company VARCHAR(255),
    location VARCHAR(255),
    work_type VARCHAR(50),          -- Remote, Hybrid, Onsite
    experience_level VARCHAR(50),   -- Mid-Senior, Associate, Entry, Executive
    years_experience DECIMAL(5,2),
    skills LONGTEXT,                -- Machine Learning, SQL, Python, etc.
    salary DECIMAL(10,2),
    posted_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    KEY idx_work_type (work_type),  -- Add indexing for common queries
    KEY idx_location (location)
);
