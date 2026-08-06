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
    skills LONGTEXT,                -- Python, SQL, Machine Learning (comma-separated or JSON)
    salary DECIMAL(10,2),
    posted_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    KEY idx_work_type (work_type),
    KEY idx_location (location),
    KEY idx_experience_level (experience_level)
);
