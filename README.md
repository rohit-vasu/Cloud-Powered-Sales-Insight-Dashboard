📊 Cloud-Powered Sales Insights Dashboard
🚀 Project Overview
This project demonstrates how raw sales data can be transformed into business-ready insights using AWS cloud and analytics stack. The solution integrates AWS (S3), PostgreSQL, Python (ETL), and Tableau to deliver an interactive sales dashboard that helps businesses answer key performance questions.

🛠️ Tech Stack
AWS Cloud Services
S3 → Stores raw CSV sales data and project files
Python → ETL script using Pandas + psycopg2 to clean and load data into PostgreSQL
PostgreSQL → Central analytics database (managed in pgAdmin)
Tableau → Interactive dashboard and visual analytics

📂 Workflow
Data Ingestion
Raw CSV uploaded to Amazon S3 (backup + centralized storage).
ETL & Processing (Python)
Python script reads CSV, cleans data, and ensures correct formatting.
Data is uploaded into PostgreSQL using psycopg2.
Database Layer (PostgreSQL)
PostgreSQL acts as the data warehouse.
Tables store sales records for querying.
Visualization Layer (Tableau)
Tableau connects directly to PostgreSQL.
Interactive dashboard built with filters (Date, Product, Region).

📈 Dashboard Features
Sales Performance Overview
Total Sales Revenue
Time-Series Trends
Sales by Month/Quarter (line chart)
Seasonal spikes in demand
🔧 How to Run
Clone this repository
Install dependencies bash CopyEdit pip install pandas psycopg2
Update database credentials in pgAdmin Upload.py
Run the Python script to upload CSV data to PostgreSQL
Connect Tableau to PostgreSQL and load the dataset
Open the dashboard .twb file or create your own

☁️ AWS + Analytics Architecture Diagram
(Simple diagram: S3 → Python ETL → PostgreSQL → Tableau)


📬 Connect with Me
👤 Rohit Vasu
🌐 https://www.linkedin.com/in/rohitvasusoftware/
📧rohitvasu91@gmail.com
