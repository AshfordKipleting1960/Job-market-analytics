# Job Market Analytics Project

A simple data analytics project to track in-demand tech skills, experience levels, and hiring trends for data related jobs using Python, MySQL, and Power BI.

## What it does

When looking for a job, it's easy to get overwhelmed by conflicting advice on what skills to learn. This project takes real job listing data, cleans it up, and answers a few practical questions:
- Which programming languages and tools (like Python, SQL, or Power BI) pop up the most?
- How many years of experience do employers actually ask for?
- Where are most of these jobs located?
- Which tools and languages are most frequently requested together?
- Are remote roles more common for certain skills?

## Tech stack

- **Python** (Pandas, NumPy) for cleaning and parsing data
- **MySQL** for storing data and running queries
- **Power BI** for building charts and dashboards
- **GitHub** for version control

## Workflow

1. **Get the data:** Download job posting datasets containing listings, descriptions, and requirements.
2. **Clean it up:** Use Python and Pandas to drop duplicates, fix messy text, and extract specific keywords like skills and locations.
3. **Explore:** Run quick checks in Jupyter notebooks to spot patterns or trends in the data.
4. **Store in MySQL:** Load the clean data into a database to practice writing queries and aggregations.
5. **Visualize:** Connect the data to Power BI to build a dashboard and charts.

## Folder structure

- `data/` – Raw and cleaned CSV files
  - `raw/` – Raw job posting CSV files
  - `cleaned/` – Output from ETL pipeline
- `notebooks/` – Jupyter notebooks for exploratory data analysis
- `sql/` – Database schema and analysis queries
- `scripts/` – ETL pipeline and data loading scripts
- `reports/` – Power BI dashboards (.pbix files)
- `tests/` – Unit tests for data cleaning functions

## 𝙺𝚎𝚢 𝙵𝚒𝚗𝚍𝚒𝚗𝚐𝚜

Out of 52,000 job postings analyzed (including over 10,000 AI roles), a few clear patterns emerged:

*  **𝚁𝚘𝚕𝚎 𝙳𝚎𝚖𝚊𝚗𝚍:** Data Engineers took the top spot with 445 open listings, followed by Business Analysts (407), Data Scientists (360), and Data Analysts (280).
*  **𝚃𝚘𝚙 𝚂𝚔𝚒𝚕𝚕𝚜:** Machine Learning and Cloud/AWS were the most requested technical skills at ~5.3k listings each, with SQL and Deep Learning right behind at ~5.2k.
*  **𝚆𝚘𝚛𝚔 𝙻𝚘𝚌𝚊𝚝𝚒𝚘𝚗:** Listings were split almost evenly three ways—Remote (34%), Hybrid (33%), and Onsite (33%).
*  **𝙴𝚡𝚙𝚎𝚛𝚒𝚎𝚗𝚌𝚎 𝙻𝚎𝚟𝚎𝚕𝚜:** The market heavily favors mid-to-senior talent. Roughly 89% of listings targeted mid-senior roles (~11k postings).
*  **𝙷𝚒𝚛𝚒𝚗𝚐 𝙷𝚞𝚋𝚜:** New York led all cities in total job volume, followed by Chicago, London, San Francisco, and Washington, D.C.

## Dashboard Overview

### 1. Market Overview & Seniority Distribution
![Job Market Overview](images/page1.png)

### 2. Skill Demand & Remote Work Breakdown
![Skill Demand and Work Types](images/page2.png)

### 3. Top Roles, Salary & Job Titles Analysis
![Roles and Salary Breakdown](images/page3.png)

---

## Tech Stack & Tools

* **Data Processing & EDA:** Python (Pandas, NumPy, Jupyter Notebooks)
* **Database & Querying:** MySQL (Aggregations, Grouping, Analysis)
* **ORM & Connection:** Python `mysql-connector-python`
* **Visualization & BI:** Power BI (DAX, Interactive Slicers, Custom Layouts)
* **Testing:** pytest for unit tests
* **Version Control:** Git & GitHub

## ʜᴏᴡ ᴛᴏ ᴇxᴘʟᴏʀᴇ & ʀᴇᴘʀᴏᴅᴜᴄᴇ

### 1. ᴄʟᴏɴᴇ ᴛʜᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ
```bash
git clone https://github.com/AshfordKipleting1960/Job-market-analytics.git
cd Job-market-analytics
```

### 2. sᴇᴛ ᴜᴘ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ & ᴅᴇᴘᴇɴᴅᴇɴᴄɪᴇs
```bash
# Using Makefile
make venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
make install

# Or manually using pip:
pip install -r requirements.txt
```

### 3. ᴀᴅᴅ ʏᴏᴜʀ ᴊᴏʙ ᴅᴀᴛᴀ
Place your raw job posting CSV file in the `data/raw/` directory:
```bash
# Your CSV should have these columns (or similar):
# - job_title
# - company_name
# - job_location
# - work_type (Remote, Hybrid, Onsite)
# - job_level (Entry, Associate, Mid-Senior, Senior, Executive)
# - years_exp
# - skills
# - salary
# - posted_date

cp your_job_postings.csv data/raw/job_postings.csv
```

### 4. ʀᴜɴ ᴛʜᴇ ᴇᴛʟ ᴘɪᴘᴇʟɪɴᴇ
Extracts raw CSV from `data/raw/`, cleans fields, drops duplicates, and exports cleaned data to `data/cleaned/`:

```bash
make run-etl
# Or manually: python scripts/etl.py
```

### 5. sᴇᴛᴜᴘ ᴍʏsǫʟ ᴅᴀᴛᴀʙᴀsᴇ
Before loading data, ensure MySQL is installed and running:

```bash
# Install MySQL (if not already installed)
# macOS: brew install mysql
# Windows: Download from https://dev.mysql.com/downloads/mysql/

# Start MySQL server
# macOS: brew services start mysql
# Windows: Open MySQL Workbench or services

# Create database and user (run once)
mysql -u root
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_password';
mysql> FLUSH PRIVILEGES;
mysql> EXIT;

# Update DB_CONFIG in scripts/load_db.py with your password
```

### 6. ʟᴏᴀᴅ ᴅᴀᴛᴀ ɪɴᴛᴏ ᴍʏsǫʟ ᴅᴀᴛᴀʙᴀsᴇ
Executes `sql/schema.sql` and bulk loads the cleaned dataset into MySQL:

```bash
python scripts/load_db.py
```

### 7. ʀᴜɴ ᴜɴɪᴛ ᴛᴇsᴛs
Verify data transformation functions using `pytest`:

```bash
make test
# Or manually: pytest -v
```

### 8. ᴇxᴘʟᴏʀᴇ sǫʟ ǫᴜᴇʀɪᴇs & ᴘᴏᴡᴇʀ ʙɪ ʀᴇᴘᴏʀᴛs
*  **ᴠɪᴇᴡ sǫʟ ǫᴜᴇʀɪᴇs:** Check out `.sql` scripts inside [`sql/`](./sql/) for data aggregation logic. These queries answer key business questions like top locations, salary by experience level, and work type distribution.
*  **ʀᴜɴ ǫᴜᴇʀɪᴇs:** Connect to your MySQL database and run queries from `sql/analysis_queries.sql`
*  **ʀᴇᴠɪᴇᴡ ᴅᴀᴛᴀ ᴘʀᴇᴘ:** Inspect Jupyter Notebooks in [`notebooks/`](./notebooks/) for exploratory analysis routines.
*  **ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ʀᴇᴘᴏʀᴛ:** Open the `.pbix` file inside [`reports/`](./reports/) using **Power BI Desktop** to explore interactive dashboards.

---

## Database Schema

The project uses a single unified table structure for simplicity and clarity:

**Table: `job_postings`**
| Column | Type | Description |
|--------|------|-------------|
| `job_id` | INT (PK) | Unique job posting identifier |
| `title` | VARCHAR(255) | Job title |
| `company` | VARCHAR(255) | Company name |
| `location` | VARCHAR(255) | Job location (city, region) |
| `work_type` | VARCHAR(50) | Remote, Hybrid, or Onsite |
| `experience_level` | VARCHAR(50) | Entry, Associate, Mid-Senior, Senior, Executive |
| `years_experience` | DECIMAL(5,2) | Years of experience required |
| `skills` | LONGTEXT | Required skills (comma-separated) |
| `salary` | DECIMAL(10,2) | Annual salary (if available) |
| `posted_date` | DATE | Job posting date |
| `created_at` | TIMESTAMP | Record creation timestamp |

---

## Example SQL Queries

Run these queries against your database to uncover insights:

```sql
-- Top 10 job titles by volume
SELECT title, COUNT(*) AS job_count 
FROM job_postings 
GROUP BY title 
ORDER BY job_count DESC LIMIT 10;

-- Average salary by work type
SELECT work_type, ROUND(AVG(salary), 2) AS avg_salary 
FROM job_postings 
WHERE salary IS NOT NULL
GROUP BY work_type;

-- Experience level distribution
SELECT experience_level, COUNT(*) AS job_count 
FROM job_postings 
GROUP BY experience_level 
ORDER BY job_count DESC;
```

See [`sql/analysis_queries.sql`](./sql/analysis_queries.sql) for more examples.
