-- SQL queries 


USE job_market_db;

-- 1. Top In-Demand Skills
SELECT 
    'Python' AS skill, SUM(skills_python) AS total FROM ai_job_market_trends
UNION ALL
SELECT 
    'SQL' AS skill, SUM(skills_sql) AS total FROM ai_job_market_trends
UNION ALL
SELECT 
    'Machine Learning' AS skill, SUM(skills_ml) AS total FROM ai_job_market_trends
ORDER BY total DESC;

-- 2. Job Seniority Levels
SELECT 
    job_level, 
    COUNT(*) AS job_count
FROM cleaned_job_postings
GROUP BY job_level
ORDER BY job_count DESC;

-- 3. Top Job Locations
SELECT 
    job_location, 
    COUNT(*) AS job_count
FROM cleaned_job_postings
GROUP BY job_location
ORDER BY job_location DESC
LIMIT 10;

-- 4. Python & SQL Co-occurrence
SELECT 
    skills_python, 
    skills_sql, 
    COUNT(*) AS total_jobs
FROM ai_job_market_trends
GROUP BY skills_python, skills_sql;

-- 5. Remote Type Breakdown
SELECT 
    remote_type, 
    COUNT(*) AS total_jobs
FROM ai_job_market_trends
GROUP BY remote_type
ORDER BY total_jobs DESC;
