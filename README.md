# 🔍 SKU Master Data Quality Object
## 📌 Project Overview

This project shows a real-world data quality monitoring worklow. The project uses a **synthetic SKU master dataset**; no real data was used in this project. The goal is to simulate common item master data issues, then build a repeatable process for detection, tracking, and visualization of data quality exceptions.

I leveraged AI and Python to generate the synthetic data set with intentional data errors. I then loaded the data a PostgreSQL database to mimic a real-life, Source of Truch scenario. I used PowerBI to connect to this database, and I evaluated the data using rule-based checks in the form of custom columns. I used this output to create a PowerBI dashboard designed to help data stewards monitor data quality and create actionables for data cleansing.

This project closely reflects my day-to-day work in inventory analytics and data governance.

---

## 🧠 Problem Statement

Item master data is instrumental in supply chain, regulatory, and commercial operations. 


## 📌 Project Overview

The dashboard displays current stream conditions for **three New Jersey streams** using publicly available USGS data. The project demonstrates a simple, end-to-end BI workflow:

**USGS API → Power Query (ETL) → Power BI Dashboard**

The focus is on clean data ingestion, repeatable transformations, and clear visual design for quick decision-making.

---

## 🎯 Purpose of the Project

This project serves two goals:

1. **Personal Use** – Quickly assess stream conditions before fly fishing outings  
2. **Portfolio Demonstration** – Showcase practical BI skills using a real-world public API

The project mirrors common operational dashboards used in enterprise settings: current-state monitoring, standardized transformations, and refreshable data models.

---

## 🛠️ Tools & Technologies

- **Data Source:** USGS Water Services API  
- **ETL / Data Transformation:** Power Query  
- **Data Modeling & Visualization:** Power BI  
- **Concepts Demonstrated:**
  - API-based data ingestion
  - Power Query transformations and normalization
  - BI modeling and dashboard design

---

## 🧱 Dashboard Build Process

This section outlines the high-level steps used to build the dashboard.

### 1. Data Ingestion
- Connected to the USGS Water Services API using Power Query
- Parsed JSON responses into tabular format and removed unnecessary elements
  ![Power Query ETL](docs/screenshots/powerquery_json_parsed.png)

### 2. Data Transformation (Power Query)
- Pivoted columns
- Changed timestamps to EST and separated into separate date and time columns
- Renamed columns and changed data types
- **Note:** Air temperature is recorded at a slightly different time than flow conditions.
  ![Power Query ETL](docs/screenshots/powerquery_columns_pivoted_cleaned.png)

### 3. Dashboard Design (Power BI)
- Designed visuals for quick “at-a-glance” assessment
- Used scales and conditional formatting for each stream measurement based on personal experience
  ![Power Query ETL](docs/screenshots/dashboard.png)

---

## 📊 Dashboard Features

- Current streamflow and gauge height by river
- Timestamp of the most recent USGS reading
- At-a-glance comparison across rivers
- Clean, minimal layout optimized for fast condition checks

---



## 🗂️ Repository Structure

```text
/
├── powerquery/           # Power Query (M) scripts for API ingestion and ETL
├── powerbi/              # Power BI dashboard files
├── docs/                 # Screenshots
└── README.md
