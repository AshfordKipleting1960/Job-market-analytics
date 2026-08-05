# Job Market Analytics Project

A simple data analytics project to track in-demand tech skills, experience levels, and hiring trends for data related jobs  using Python, SQL, and Power BI.

## What it does

When looking for a job, it's easy to get overwhelmed by conflicting advice on what skills to learn. This project takes real job listing data, cleans it up, and answers a few practical questions:
- Which programming languages and tools (like Python, SQL, or Power BI) pop up the most?
- How many years of experience do employers actually ask for?
- Where are most of these jobs located?
- Which tools and languages are most frequently requested together ?
- Are remote roles more common for certain skills ?

## Tech stack

- **Python** (Pandas, NumPy) for cleaning and parsing data
- **SQL** for storing data and running queries
- **Power BI** for building charts and dashboards
- **GitHub** for version control

## Workflow

1. **Get the data:** Download job posting datasets containing listings, descriptions, and requirements.
2. **Clean it up:** Use Python and Pandas to drop duplicates, fix messy text, and extract specific keywords like skills and locations.
3. **Explore:** Run quick checks in Jupyter notebooks to spot patterns or trends in the data.
4. **Store in SQL:** Load the clean data into a database to practice writing queries and aggregations.
5. **Visualize:** Connect the data to Power BI to build a dashboard and charts.

## Folder structure

- `data/` – Raw and cleaned CSV files
- `notebooks/` – Jupyter notebooks for playing around with the data
- `sql/` – Database queries
- `reports/` – Power BI files
- `visuals/` – Saved charts and screenshots

##  Key Findings & Insights

Based on an analysis of over **52,000 job openings** (including **10,000+ AI-focused roles**):

* **Top Job Openings by Role:** Data Engineers lead the market (**445 postings**), followed closely by Business Analysts (**407**), Data Scientists (**360**), and Data Analysts (**280**).
* **Core Skill Demand:** Core technical skills show high, balanced demand across the board:
  * **Machine Learning & Cloud (AWS):** Top requested skills (~5.3K postings each).
  * **SQL & Deep Learning:** Tied for second (~5.2K postings each).
  * **Python:** Highly requested across data science and engineering roles (~5.1K postings).
* **Work Arrangement Breakdown:** Work location models are evenly distributed across the tech industry:
  * **Remote:** 33.96% (3.51K postings)
  * **Hybrid:** 33.06% (3.42K postings)
  * **Onsite:** 32.98% (3.41K postings)
* **Seniority & Experience Distribution:** **89.37%** of listings target **Mid-Senior** professionals (~11K postings), while **10.63%** target **Associate** tier roles (~1K postings).
* **Top Hiring Hubs:** **New York, NY** is the leading location by job volume, followed by **Chicago, IL**, **London, UK**, **San Francisco, CA**, and **Washington, DC**.

---

##  Dashboard Overview

### 1. Market Overview & Seniority Distribution
![Job Market Overview](images/page1.png)

### 2. Skill Demand & Remote Work Breakdown
![Skill Demand and Work Types](images/page2.png)

### 3. Top Roles, Salary & Job Titles Analysis
![Roles and Salary Breakdown](images/page3.png)

---

##  Tech Stack & Tools

* **Data Processing & EDA:** Python (Pandas, NumPy, Jupyter Notebooks)
* **Database & Querying:** SQL (Aggregations, Grouping, Skill Extraction)
* **Visualization & BI:** Power BI (DAX, Interactive Slicers, Custom Layouts)
* **Version Control:** Git & GitHub

## ʜᴏᴡ ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴛʜɪs ᴘʀᴏᴊᴇᴄᴛ

1.  **ᴠɪᴇᴡ ᴛʜᴇ qᴜᴇʀɪᴇs:** Check out the `.sql` scripts inside the [`sql/`](./sql/) directory to see data aggregation logic.
2.  **ʀᴇᴠɪᴇᴡ ᴅᴀᴛᴀ ᴘʀᴇᴘ:** Open Jupyter Notebooks in [`notebooks/`](./notebooks/) to inspect data cleaning routines.
3.  **ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ʀᴇᴘᴏʀᴛ:** Open the `.pbix` file inside [`reports/`](./reports/) using **Power BI Desktop** to interact with dynamic filters.
