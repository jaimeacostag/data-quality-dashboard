# 🔍 SKU Master Data Quality Object
## 📌 Project Overview

This project shows a real-world data quality monitoring worklow. The project uses a **synthetic SKU master dataset**; no real data was used in this project. The goal is to simulate common item master data issues, then build a repeatable process for detection, tracking, and visualization of data quality exceptions.

I leveraged AI and Python to generate the synthetic data set with intentional data errors. I then loaded the data a PostgreSQL database to mimic a real-life, Source of Truch scenario. I used PowerBI to connect to this database, and I evaluated the data using rule-based checks in the form of custom columns. I used this output to create a PowerBI dashboard designed to help data stewards monitor data quality and create actionables for data cleansing.

This project closely reflects my day-to-day work in inventory analytics and data governance.

---

## 🧠 Problem Statement

Item master data is instrumental in supply chain, regulatory, and commercial operations. Issues with SKU set-ups can cause downstream failures in ERP, WMS, reporting, and compliance processes. Some of these issues not following SKU-naming rules, setting invalid attributes, or leaving critical fields blank. 

---

## 🏗️ Workflow and Tools Overview

Python (Synthetic Data Generation)

  ⬇️
  
PostgresSQL (Relational Database Storage)

  ⬇️
  
PowerBI (Ingestion, Rule Validation, Visualization)

---

## 🛠️ Data Genration (Python)

-  Leveraged AI to create a Python script used to generate a synthetic SKU master dataset with over 5000 SKUs
-  Included fields such as:
    -  SKU Number/Material Number
    -  Description with dosage form and strength
    -  Commercial Classification
    -  Brand/Label Type
-  Errors introduced
    -  Missing values
    -  Inconsistent SKU Numbers
    -  Conflicting values
 ---


🗄️ Data Storage (PostgreSQL)

Loaded the synthetic dataset into PostgreSQL

Designed the table to resemble a simplified item master structure

Enabled Power BI to connect directly to a relational data source, mirroring production analytics patterns

🔍 Data Quality Rules (Power BI)

Within Power BI, I created custom columns to evaluate data quality rules such as:

Description consistency vs. commercial classification

Required field completeness

Detection of “Sample” or “Private Label” indicators

Identification of records that fail one or more validation checks

Each rule produces a Boolean or categorical result that feeds into overall data quality scoring.

📊 Dashboard Features

The Power BI dashboard includes:

Overall data quality score

Count of SKUs failing one or more rules

Breakdown of failures by rule

Trend views to monitor data quality over time

Drill-down capability to identify specific SKUs with issues

The dashboard is designed for data stewards, inventory analysts, and master data teams who need quick visibility into data health.

🛠️ Tools & Technologies

Python – Synthetic data generation

PostgreSQL – Relational database storage

Power BI – Data modeling, rule validation, and visualization

SQL – Data validation and querying

GitHub – Version control and project documentation

🚀 Why This Project Matters

This project demonstrates:

Practical experience with data quality and governance concepts

End-to-end data workflows from generation to visualization

Use of rule-based validation in analytics tools

Familiarity with enterprise-style data architectures

Ability to translate business rules into technical logic

It directly reflects the type of analytical and data stewardship work required in pharmaceutical, manufacturing, and regulated supply chain environments.

