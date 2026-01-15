# 🔍 SKU Master Data Quality Object
## 📌 Project Overview

This project shows a real-world data quality monitoring worklow. The project uses a **synthetic SKU master dataset**; no real data was used in this project. The goal is to simulate common item master data issues, then build a repeatable process for detection, tracking, and visualization of data quality exceptions.

I leveraged AI and Python to generate the synthetic data set with intentional data errors. I then loaded the data a PostgreSQL database to serve as the source of truth. I used PowerBI to connect to this database and I evaluated the data using rule-based checks in the form of custom columns. I used this output to create a PowerBI dashboard designed to help data stewards monitor data quality and create actionables for data cleansing.

This project closely reflects my day-to-day work in inventory analytics and data governance.

**Note:** This project is an oversimplification of a real item master data structure. For this project I am relying on a **single** data table with synthetic data.

---

## 🧠 Problem Statement

Item master data is instrumental in supply chain, regulatory, and commercial operations. Issues with SKU set-ups can cause downstream failures in ERP, WMS, reporting, and compliance processes. Some of these issues not following SKU-naming rules, setting invalid attributes, or leaving critical fields blank. 

---

## 🛠️ Tools & Technologies

Python – Synthetic data generation

PostgreSQL – Relational database storage

Power BI – Data modeling, rule validation, and visualization

SQL – Data validation and querying

GitHub – Version control and project documentation

--

## 🏗️ Workflow and Tools Overview

Python (Synthetic Data Generation)

  ⬇️
  
PostgresSQL (Relational Database Storage)

  ⬇️
  
PowerBI (Ingestion, Rule Validation, Visualization)

---

### 🛠️ Data Genration (Python)

-  Leveraged AI to create a Python script used to generate a synthetic SKU master dataset with over 5000 SKUs. The script allowed me to customize output, including the # of SKUs to generate and the percentage of errors to insert in the dataset.
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


### 🗄️ Data Storage (PostgreSQL)

Loaded the synthetic dataset of Pharma and OTC products (csv format) into a local PostgreSQL database using the pgAdmin 4 admin tool. The table design resembled that of the csv dataset. No cleansing was performed, only verification that all data was loaded properly.
**[screenshot first 10 rows]**![Alt text for the image](image_url_or_path) 

**[screenshot columns]**![Alt text for the image](image_url_or_path)

**[screenshot count of records]**![Alt text for the image](image_url_or_path)

### 🔍 Data Ingestion and Data Quality Rules (Power BI)

-  I used PowerQuery to conenct to the local PostgreSQL database, and then loaded the data using using Import Mode so I could add Custom Columns.
-  Added Custom Columns to apply data rules to generate a boolean value. True = exception, False = no exception (data follows rule).
    -  SKU number must folllow a ######ABC naming format (6 integers, 3 chars)
    -  Description must contain commercial classification ('General Market', 'Sample', 'Private Label') and, conversely, Commercial Classification must match this description
    -  Product Type must be 'OTC' or 'Pharma' with no blanks
    -  Lot Control has to be set to 'Yes' for all products with no blanks
    -  Primary Distribution Center must be one of five valid DCs with no blanks
    -  ABC Code for accounting and cycle-count activities must be entered with no blank ('A', 'B', 'C')

**[screenshot powerquery]**![Alt text for the image](image_url_or_path)

**[screenshot custom columns]**![Alt text for the image](image_url_or_path)

### 📊 Dashboard Features and Insights

The design of the PowerBI dashboard includes:
-  Overall data quality score
-  Count of SKUs failing one or more rules
-  Count of rule failures across the entire dataset
-  Count of SKUs being considered in the analysis
-  Breakdown of rule failures by type
-  Breakdown of SKUs failing one or more rules by Product Type and Commercial Classification
-  Table of all SKUs failine one or more rules, with the option to filter/search by SKU.

The dashboard is designed for data stewards, inventory analysts, and master data teams who need quick visibility into data health. This dashboard can help determine what products types are the most affected, and also what are the most common points of failure.

Several actionables can be set by using this dashboard
  -  SKU naming conventions can be easily resolved. This only affects 5 SKUs but it is low-hanging fruit. This would be a quick win.
  -  Lot Control flag should be set as YES to on all SKUs. This update should be quick using SQL (UPDATE table, SET lot_control_flag = 'Yes';), and would impact ### if SKUs. This is also a quick win.
  -  Incorrect Primary DC or blank values would require input from Supply Chain and Logistics teams, but this only affects ### of SKUs.
  -  SKU Description and Commercial Classification. If Product Description includes the Commercial Classification, but the Commercial Classification is incorrect or blank

--

## 🚀 Why This Project Matters

This project demonstrates:

Practical experience with data quality and governance concepts

End-to-end data workflows from generation to visualization

Use of rule-based validation in analytics tools

Familiarity with enterprise-style data architectures

Ability to translate business rules into technical logic

It directly reflects the type of analytical and data stewardship work required in pharmaceutical, manufacturing, and regulated supply chain environments.

