# Job Market Analytics Project

A simple data analytics project to track in-demand tech skills, experience levels, and hiring trends using Python, SQL, and Power BI.

## What it does

When looking for a job, it's easy to get overwhelmed by conflicting advice on what skills to learn. This project takes real job listing data, cleans it up, and answers a few practical questions:
- Which programming languages and tools (like Python, SQL, or Power BI) pop up the most?
- How many years of experience do employers actually ask for?
- Where are most of these jobs located?

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
- `src/` – Python code for processing files
- `sql/` – Database queries
- `dashboard/` – Power BI files
- `visuals/` – Saved charts and screenshots

## Current Status

Working on cleaning the data and setting up the analysis scripts.
