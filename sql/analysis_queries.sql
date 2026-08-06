-- SQL Analysis Queries for Job Market Analytics

USE job_market_db;

-- 1. Top Job Titles
SELECT 
    title, 
    COUNT(*) AS job_count
FROM job_postings
GROUP BY title
ORDER BY job_count DESC
LIMIT 10;

-- 2. Job Seniority Levels Distribution
SELECT 
    experience_level, 
    COUNT(*) AS job_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM job_postings), 2) AS percentage
FROM job_postings
GROUP BY experience_level
ORDER BY job_count DESC;

-- 3. Top Job Locations
SELECT 
    location, 
    COUNT(*) AS job_count
FROM job_postings
GROUP BY location
ORDER BY job_count DESC
LIMIT 10;

-- 4. Work Type Breakdown (Remote vs Hybrid vs Onsite)
SELECT 
    work_type, 
    COUNT(*) AS total_jobs,
    ROUND(AVG(salary), 2) AS avg_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM job_postings
WHERE salary IS NOT NULL
GROUP BY work_type
ORDER BY total_jobs DESC;

-- 5. Average Salary by Experience Level
SELECT 
    experience_level, 
    ROUND(AVG(salary), 2) AS avg_salary,
    COUNT(*) AS job_count
FROM job_postings
WHERE salary IS NOT NULL
GROUP BY experience_level
ORDER BY avg_salary DESC;

-- 6. Experience Requirements
SELECT 
    ROUND(years_experience, 1) AS experience_years,
    COUNT(*) AS job_count
FROM job_postings
WHERE years_experience IS NOT NULL
GROUP BY ROUND(years_experience, 1)
ORDER BY experience_years ASC;

-- 7. Jobs by Work Type and Experience Level
SELECT 
    work_type,
    experience_level,
    COUNT(*) AS job_count
FROM job_postings
GROUP BY work_type, experience_level
ORDER BY job_count DESC;

-- 8. Salary Ranges by Work Type and Experience Level
SELECT 
    work_type,
    experience_level,
    COUNT(*) AS job_count,
    ROUND(AVG(salary), 2) AS avg_salary
FROM job_postings
WHERE salary IS NOT NULL
GROUP BY work_type, experience_level
ORDER BY avg_salary DESC;
